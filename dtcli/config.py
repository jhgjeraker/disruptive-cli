import pathlib
from typing import Any

import yaml

CFG_DIR = pathlib.Path().home() / '.config' / 'disruptive'
CFG_FILE = CFG_DIR / 'disruptive-cli.yaml'

_default_cfg = {
    'output': {
        'padding': 3,
    },
}


def _load_config() -> dict[str, Any]:
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
    _write_config(_default_cfg)


def set_padding(**kwargs):
    # Parse (or use default) config file.
    cfg = _load_config()

    # Update config with provided value.
    cfg['output']['padding'] = int(kwargs['spaces'])

    # Write updated config to file.
    _write_config(cfg)
