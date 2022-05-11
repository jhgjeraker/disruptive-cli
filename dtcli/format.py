import sys
import argparse
from typing import Any, Optional, Dict


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


def to_int(x: Any) -> int:
    return int(x)


def to_float(x: Any) -> float:
    return float(x)


def to_bool(x: Any) -> bool:
    if isinstance(x, bool):
        return x
    elif isinstance(x, str):
        return x.lower() in ['true', 'yes', '1']
    elif isinstance(x, int) or isinstance(x, float):
        return int(x) != 0
    else:
        raise TypeError(f'value {x} can not be converted to bool')


def str_attr_format(x: str) -> str:
    return x.replace('-', '_').replace(' ', '_').lower()


def str_col_format(x: str) -> str:
    return x.replace('_', '-').replace(' ', '-').upper()


def stderr(*args: Any, **kwargs: Any) -> None:
    print(*args, file=sys.stderr, flush=True, **kwargs)


def stdout(*args: Any, **kwargs: Any) -> None:
    print(*args, file=sys.stdout, flush=True, **kwargs)


def args_replace_dash(args: dict) -> dict:
    pruned = {}
    for key in args.keys():
        pruned[key.replace('-', '_')] = args[key]
    return pruned


def str2dict(entry: Optional[str]) -> Dict[str, str]:
    out: Dict[str, str] = {}

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


def str2list(entry: Optional[str]) -> list:
    if entry is None:
        return []

    entries = entry.replace('\n', ',').replace(' ', ',').split(',')
    return [entry for entry in entries if len(entry) > 0]


def is_xid(entry: Optional[str]) -> bool:
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
