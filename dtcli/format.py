import sys
import argparse
from typing import Any


class SubcommandHelpFormatter(argparse.RawDescriptionHelpFormatter):
    def _format_action(self, action: Any) -> str:
        parts = super()._format_action(action)

        if action.nargs == argparse.PARSER:
            parts = "\n".join(parts.split("\n")[1:])

        return parts.replace(' ,', ',')


def to_string(x: Any) -> str:
    if isinstance(x, str):
        return x
    else:
        return str(x)


def str_attr_format(x: str) -> str:
    return x.replace('-', '_').replace(' ', '_').lower()


def str_col_format(x: str) -> str:
    return x.replace('_', '-').replace(' ', '-').upper()


def stderr(*args: Any, **kwargs: Any) -> None:
    print(*args, file=sys.stderr, flush=True, **kwargs)


def stdout(*args: Any, **kwargs: Any) -> None:
    print(*args, file=sys.stdout, flush=True, **kwargs)


def args_replace_dash(args: dict[str, str | None]) -> dict:
    pruned = {}
    for key in args.keys():
        pruned[key.replace('-', '_')] = args[key]
    return pruned


def str2dict(entry: str | None) -> dict[str, str]:
    out: dict[str, str] = {}

    if entry is None:
        return out

    for e in entry.split(','):
        if '=' in e:
            split = e.split('=')
            key = split[0]
            value = '='.join(split[1:])
        else:
            key = e
            value = ''

        out[key] = value
    return out


def str2list(entry: str | None) -> list:
    if entry is None:
        return []

    entries = entry.replace('\n', ',').replace(' ', ',').split(',')
    return [entry for entry in entries if len(entry) > 0]


def is_xid(entry: str | None) -> bool:
    if entry is None:
        return False

    def check1(x: str) -> bool:
        return x != x.lower()

    def check2(x: str) -> bool:
        return x.startswith('emu') and len(x) != 23

    def check3(x: str) -> bool:
        return not x.startswith('emu') and len(x) != 20

    for check in [check1, check2, check3]:
        if check(entry):
            return False

    return True
