import pathlib
from typing import Any, Dict

import yaml

CFG_DIR = pathlib.Path().home() / '.config' / 'disruptive'
CFG_FILE = CFG_DIR / 'dt-cli.yaml'

_default_cfg = {
    'output': {
        'padding': 3,
    },
}


def load_config() -> Dict[str, Any]:
    try:
        with open(str(CFG_FILE), 'r') as f:
            cfg = yaml.full_load(f)
    except FileNotFoundError:
        cfg = _default_cfg

    assert isinstance(cfg, dict)

    return cfg


def _write_config(cfg: Dict[str, Any]) -> None:
    if not CFG_DIR.exists():
        CFG_DIR.mkdir(parents=True, exist_ok=True)

    with open(str(CFG_FILE), 'w') as f:
        yaml.dump(cfg, f)


def set_default() -> None:
    _write_config(_default_cfg)


def set_padding(**kwargs: dict) -> None:
    # Parse (or use default) config file.
    cfg = load_config()

    # Update config with provided value.
    cfg['output']['padding'] = kwargs['spaces']
    cfg['output']['padding'] = int(cfg['output']['padding'])

    # Write updated config to file.
    _write_config(cfg)
