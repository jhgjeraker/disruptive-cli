import pathlib
from typing import Any

import yaml

import dtcli

CFG_DIR = pathlib.Path().home() / '.config' / 'disruptive'
CFG_FILE = CFG_DIR / 'dt-cli.yaml'

_default_cfg = {
    'output': {
        'padding': 3,
    },
}


def load_config() -> dict[str, Any]:
    try:
        with open(str(CFG_FILE), 'r') as f:
            cfg = yaml.full_load(f)
    except FileNotFoundError:
        cfg = _default_cfg

    return cfg


def _write_config(cfg: dict[str, Any]) -> None:
    if not CFG_DIR.exists():
        CFG_DIR.mkdir(parents=True, exist_ok=True)

    with open(str(CFG_FILE), 'w') as f:
        yaml.dump(cfg, f)


def set_default():
    _write_config()


def set_padding(**kwargs):
    # Parse (or use default) config file.
    cfg = load_config()

    # Update config with provided value.
    cfg['output']['padding'] = int(kwargs['spaces'])

    # Write updated config to file.
    _write_config(cfg)


def add_command(subparser, glob_func):
    cfg_parser = subparser.add_parser(
        name='config',
        help='Configure CLI behavior.',
        formatter_class=dtcli.format.SubcommandHelpFormatter,
    )

    cfg_subparser = cfg_parser.add_subparsers(
        title='available commands',
        dest='config',
        metavar=None,
    )
    cfg_subparser.add_parser('default', help='Generate default config file.')
    cfg_subparser.add_parser('padding', help='Set table column padding.')

    glob_func(cfg_parser)

    return cfg_parser


def do(parser, args):
    if args.config == 'default':
        set_default()
    else:
        print(parser.format_help())
