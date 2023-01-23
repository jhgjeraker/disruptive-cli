import pathlib
from typing import Any, Dict

import yaml

from dtcli.table import Table

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


def _write_config(cfg: Dict[str, Any]) -> Table:
    if not CFG_DIR.exists():
        CFG_DIR.mkdir(parents=True, exist_ok=True)

    with open(str(CFG_FILE), 'w') as f:
        yaml.dump(cfg, f)

    return Table.empty()


def set_default() -> Table:
    _write_config(_default_cfg)
    return Table.empty()


def set_padding(**kwargs: dict) -> Table:
    # Parse (or use default) config file.
    cfg = load_config()

    # Update config with provided value.
    cfg['output']['padding'] = kwargs['spaces']
    cfg['output']['padding'] = int(cfg['output']['padding'])

    # Write updated config to file.
    _write_config(cfg)

    return Table.empty()
