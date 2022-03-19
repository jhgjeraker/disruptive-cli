import sys
import argparse


class SubcommandHelpFormatter(argparse.RawDescriptionHelpFormatter):
    def _format_action(self, action):
        parts = super()._format_action(action)
        if action.nargs == argparse.PARSER:
            parts = "\n".join(parts.split("\n")[1:])
        return parts


def str_attr_format(x):
    return x.replace('-', '_').replace(' ', '_').lower()


def str_col_format(x):
    return x.replace('_', '-').replace(' ', '-').upper()


def stderr(*args, **kwargs):
    print(*args, file=sys.stderr, flush=True, **kwargs)


def stdout(*args, **kwargs):
    print(*args, file=sys.stdout, flush=True, **kwargs)


def args_replace_dash(args: dict[str, str | None]):
    pruned = {}
    for key in args.keys():
        pruned[key.replace('-', '_')] = args[key]
    return pruned
