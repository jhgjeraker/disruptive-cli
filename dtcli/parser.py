import sys
from argparse import ArgumentParser
from typing import Any, Callable, Tuple, List, Dict, Optional

import disruptive as dt

import dtcli


def is_interactive() -> bool:
    return '-i' in sys.argv or '--interactive' in sys.argv


class Arg():
    def __init__(self,
                 key: str,
                 flags: List[str],
                 format: Callable,
                 check_xid: bool = False,
                 default_value: Any = None,
                 required_by: Dict[str, Any] = {},
                 action: Optional[str] = None,
                 metavar: Optional[str] = None,
                 help: Optional[str] = None,
                 **kwargs: Any,
                 ) -> None:

        """
        Represents arguments accepted by the CLI.
        These are often an image of the arguments expected
        by the `disruptive` package.

        Parameters
        ----------
        key : str
            Name of the argument used as key in dictionaries.
            Should mirror argument name of `disruptive` methods.
        flags : list[str]
            One or more flags exposed by the CLI.
            Should be formatted as ` key-name` for required arguments
            and `--key-name` for optional arguments.
        format : Callable
            Function applied to argument value before passing it on.
            Is usually one of the string-operations found in `dtcli.format`.
        check_xid : bool
            Whether or not the argument should be verified as xid format.
        default_value : Any
            Value passed if none is provided.

        """

        self.key = key
        self.flags = flags
        self._snaked_flags = self._flag_to_snakecase(flags)
        self.format: Callable = format
        self.kwargs = kwargs
        self.check_xid: bool = check_xid
        self.default_value = default_value
        self.required_by = required_by

        self._value: Optional[str] = None
        self._set: bool = False
        self.pipe: bool = False

        self.argparse_kwargs = {}
        if action is not None:
            self.argparse_kwargs['action'] = action
        if help is not None:
            self.argparse_kwargs['help'] = help
        if metavar is not None:
            self.argparse_kwargs['metavar'] = metavar

    @property
    def value(self) -> Any:
        if self._set:
            return self.format(self._value)
        else:
            return self.default_value

    def _flag_to_snakecase(self, flags: List[str]) -> List[str]:
        out = []
        for flag in flags:
            if flag.startswith('--'):
                flag = flag[2:]
            elif flag.startswith('-'):
                flag = flag[1:]
            flag = flag.replace('-', '_')
            out.append(flag)
        return out

    def _required_str(self) -> str:
        if any([v.startswith('--') for v in self.flags]):
            return 'optional'
        else:
            return 'required'

    def _set_value(self, value: Any) -> None:
        self._value = value
        if value is not None:
            self._set = True

        # If the string '-' is provided, accept input from pipe.
        # But not if in interactive mode, that causes a hang.
        if isinstance(value, str) and value == '-':
            self.pipe = True
            self.format = dtcli.format.str2list
            self._value = sys.stdin.read()

    def to_argparse(self) -> Tuple[List[str], dict]:
        return self.flags, self.argparse_kwargs
        # kwargs = {}
        # for key in ['metavar', 'help', 'action', 'type']:
        #     if key in self.kwargs:
        #         kwargs[key] = self.kwargs[key]

        # return self.flags, kwargs

    def _from_interactive(self) -> None:
        val = input(f'{self._required_str()} > {self.key}: ')
        self._set_value(val if len(val) > 0 else None)

    def _resolve_value(self, **kwargs: dict) -> None:
        if is_interactive():
            self._from_interactive()
        else:
            for key in kwargs:
                if key in self._snaked_flags:
                    self._set_value(kwargs[key])
                    return

            raise Exception(f'Missing key {self.key} in kwargs')


def add_cmd_argument(parser: ArgumentParser,
                     *args: Any,
                     **kwargs: Any,
                     ) -> None:
    if is_interactive():
        return

    parser.add_argument(
        *args,
        **kwargs,
    )


class CmdArgs():
    def __init__(self, args_list: List[Arg]) -> None:
        self.args_list = args_list
        self.keyed_args = {arg.key: arg for arg in self.args_list}

    def _dependency_check(self) -> bool:
        for arg in self.args_list:
            if len(arg.required_by) > 0:
                for key in arg.required_by:
                    want_val = arg.required_by[key]
                    has_val = self.keyed_args[key].value

                    if want_val != has_val:
                        continue

                    msg = f'{key}={has_val} requires flag {arg.flags[-1]}'

                    if not arg._set:
                        dtcli.format.stderr(msg)
                        return False

        return True

    def to_parser(self, parser: ArgumentParser) -> None:
        if not is_interactive():
            for arg in self.args_list:
                flags, kwargs = arg.to_argparse()
                parser.add_argument(
                    *flags,
                    **kwargs,
                )

    def to_method(self, **kwargs: dict) -> dict:
        self._arg_from_kwargs(**kwargs)
        return self._to_dict()

    def _arg_from_kwargs(self, **kwargs: dict) -> None:
        for arg in self.args_list:
            arg._resolve_value(**kwargs)

    def _to_dict(self) -> dict:
        out = {}
        for arg in self.args_list:
            # Only include arguments that are set.
            if arg._set:
                out[arg.key] = arg.value
        return out

    def _call_pipe(self, pipe: Arg,
                   method: Callable,
                   method_args: dict,
                   ) -> list:
        res = []

        if pipe.value is None:
            raise ValueError('pipe value must not be None')

        # Otherwise, iterate through pipe entries.
        for i, entry in enumerate(pipe.value):
            dtcli.format.stderr(f'{i + 1} / {len(pipe.value)}')
            # If the piped argument is xid, validate format before call.
            if pipe.check_xid and not dtcli.format.is_xid(entry):
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

    def call(self, method: Callable, method_args: dict) -> list:
        # If a pipe is provided, use it.
        for arg in self.args_list:
            if arg.pipe and arg.value is not None:
                # Should be removed from args dict to avoid conflict.
                method_args.pop(arg.key)

                # If more than one pipe is given, only acknowledge the first.
                return self._call_pipe(arg, method, method_args)

        res = method(**method_args)
        return res if isinstance(res, list) else [res]

    def reparse(self, **kwargs: dict) -> Tuple[bool, dict]:
        # Use the kwargs provided by argparse to get key values.
        self._arg_from_kwargs(**kwargs)

        # Do a dependency check on the arguments.
        if not self._dependency_check():
            return False, {}

        # Convert arguments to dictionary form.
        return True, self._to_dict()
