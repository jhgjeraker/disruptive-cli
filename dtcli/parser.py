import sys

import disruptive as dt

import dtcli


def is_interactive() -> bool:
    return '-i' in sys.argv or '--interactive' in sys.argv


class CmdArgs():
    def __init__(self, args_list):
        self.args_list = args_list

    def to_parser(self, parser):
        if not is_interactive():
            for arg in self.args_list:
                flags, kwargs = arg.to_argparse()
                parser.add_argument(
                    *flags,
                    **kwargs,
                )

    def to_method(self, **kwargs):
        self._reparse(**kwargs)
        return self._to_dict()

    def _reparse(self, **kwargs):
        for arg in self.args_list:
            arg._resolve_value(**kwargs)

    def _to_dict(self):
        out = {}
        for arg in self.args_list:
            out[arg.key] = arg.value
        return out

    def call(self, method, **kwargs) -> list:
        # Use the kwargs provided by argparse to get key values.
        self._reparse(**kwargs)

        # Convert arguments to dictionary form.
        method_args = self._to_dict()

        # If a pipe is provided, isolate it.
        pipe = None
        for arg in self.args_list:
            if arg.pipe:
                # Should be removed from args dict to avoid conflict.
                method_args.pop(arg.key)

                # If more than one pipe is given, only acknowledge the first.
                pipe = arg
                break

        # If pipe is not given, return method results directly.
        if pipe is None:
            res = method(**method_args)
            return res if isinstance(res, list) else [res]
        else:
            res = []

            # Otherwise, iterate through pipe entries.
            for entry in pipe.value:
                # If the piped argument is xid, validate format before call.
                if pipe.xid and not dtcli.format.is_xid(entry):
                    msg = f'{entry} is not a valid ID'
                    dtcli.format.stderr(msg)
                    continue

                # Set argument value for pipe key as entry.
                method_args[pipe.key] = entry

                # Raised exceptions are caught, logged, but continued.
                try:
                    r = method(**method_args)
                except dt.errors.DTApiError as e:
                    msg = f'{pipe.key}={entry} raised {type(e).__name__}'
                    dtcli.format.stderr(msg)
                    continue

                # Append method results to output.
                if isinstance(r, list):
                    res += r
                else:
                    res.append(r)

            return res


class Arg():
    def __init__(self, key, flags, format, xid=False, **kwargs):
        self.key = key
        self.flags = flags
        self._snaked_flags = self._flag_to_snakecase(flags)
        self.format = format
        self.kwargs = kwargs
        self.xid = xid

        self._value = None
        self._set = False
        self.pipe = False

    @property
    def value(self):
        if self._set:
            return self.format(self._value)
        else:
            return None

    def _flag_to_snakecase(self, flags):
        out = []
        for flag in flags:
            if flag.startswith('--'):
                flag = flag[2:]
            elif flag.startswith('-'):
                flag = flag[1:]
            flag = flag.replace('-', '_')
            out.append(flag)
        return out

    def _required_str(self):
        if any([v.startswith('--') for v in self.flags]):
            return 'optional'
        else:
            return 'required'

    def _set_value(self, value):
        self._value = value
        if value is not None:
            self._set = True

        # If the string '-' is provided, accept input from pipe.
        if isinstance(value, str) and value == '-':
            self.pipe = True
            self.format = dtcli.format.str2list
            self._value = sys.stdin.read()

    def to_argparse(self):
        kwargs = {}
        for key in ['metavar', 'help']:
            if key in self.kwargs:
                kwargs[key] = self.kwargs[key]

        return self.flags, kwargs

    def _from_interactive(self):
        val = input(f'{self._required_str()} > {self.key}: ')
        if len(val) < 1:
            val = None
        self._set_value(val)

    def _resolve_value(self, **kwargs):
        if is_interactive():
            self._from_interactive()
        else:
            for key in kwargs:
                if key in self._snaked_flags:
                    self._set_value(kwargs[key])
                    return

            raise Exception(f'Missing key {self.key} in kwargs')


def add_cmd_argument(parser,
                     *args,
                     **kwargs,
                     ):
    if is_interactive():
        return

    parser.add_argument(
        *args,
        **kwargs,
    )


def get_command_args(keys: list[str], **kwargs) -> dict:
    out = {}

    if is_interactive():
        dtcli.format.stderr('Interactive mode.')
        dtcli.format.stderr('Leave empty [Enter] for default value.')

        for key in keys:
            val = input(f'{key}: ')
            if len(val) < 1:
                val = None
            out[key] = val
    else:
        for key in keys:
            out[key] = kwargs[key]

    return out
