import json
from typing import Callable, List, Optional, Any

import disruptive

import dtcli.format


class Column():
    def __init__(self, name: str, hidden: bool, width: Optional[int] = None):
        self.name = name
        self.hidden = hidden
        self.width = width if width is not None else len(name)

    @property
    def attr_name(self) -> str:
        return dtcli.format.str_attr_format(self.name)

    @property
    def col_name(self) -> str:
        return dtcli.format.str_col_format(self.name)

    @classmethod
    def from_opts(cls, name: str) -> 'Column':
        return cls(name, False, len(name))

    def get_obj_attr_str(self, obj: object) -> str:
        if hasattr(obj, self.attr_name):
            attr = getattr(obj, self.attr_name)
            if isinstance(attr, disruptive.outputs.OutputBase):
                attr = json.dumps(attr.raw)
            elif isinstance(attr, dict):
                attr = json.dumps(attr)
            elif isinstance(attr, list):
                return ','.join(attr)
            return str(attr)
        else:
            return ''


class Table():
    def __init__(self, default_columns: list, cfg: dict, opts: dict) -> None:
        self.cfg = cfg
        self.opts = opts
        self.n_rows = 0
        self.columns = self._parse_columns(default_columns)
        self.n_columns = len(self.columns)

        # This attribute will be appended for each new stdout print.
        self.rows: List[str] = []

    @classmethod
    def empty(cls) -> 'Table':
        return cls(
            default_columns=[],
            cfg={},
            opts={},
        )

    def _parse_columns(self, columns: List[Column]) -> List[Column]:
        # Make a copy of input.
        use_columns = [c for c in columns]

        # If --include is provided, only use columns specified.
        if 'include' in self.opts and self.opts['include'] is not None:
            names = self.opts['include'].split(',')
            names = [dtcli.format.str_attr_format(n) for n in names]
            return [c for c in use_columns if c.attr_name in names]

        # If `--full` is not provided, show only partial output.
        if 'full' in self.opts and not self.opts['full']:
            return [c for c in use_columns if not c.hidden]

        return use_columns

    def _should_print_header(self) -> bool:
        if self.opts['no_header'] or len(self.columns) < 2:
            return False
        else:
            return True

    def expand_rows(self, objects: list) -> None:
        for i, col in enumerate(self.columns):
            for obj in objects:
                attr_width = len(col.get_obj_attr_str(obj))
                if attr_width > col.width:
                    self.columns[i].width = attr_width

    def _csv_entry_func(self, obj: object, header: bool = False) -> str:
        line = ''
        for col in self.columns:
            value = col.attr_name if header else col.get_obj_attr_str(obj)
            line += str(value) + ','
        return line[:-1]

    def _tsv_entry_func(self, obj: object, header: bool = False) -> str:
        line = ''
        for col in self.columns:
            value = col.attr_name if header else col.get_obj_attr_str(obj)
            line += str(value) + '\t'
        return line[:-1]

    def _table_entry_func(self, obj: object, header: bool = False) -> str:
        line = ''
        for col in self.columns:
            if header:
                value = col.col_name
            else:
                value = col.get_obj_attr_str(obj)
            line += f'{str(value):<{col.width}}'
            line += ' ' * self.cfg['output']['padding']
        return line[:-self.cfg['output']['padding']]

    def _json_entry_func(self, obj: Any, header: bool = False) -> str:
        if header:
            return ''

        if hasattr(obj, 'raw'):
            return json.dumps(obj.raw)
        else:
            return ''

    def _resolve_row_func(self) -> Callable:
        if self.opts['csv']:
            return self._csv_entry_func
        elif self.opts['tsv']:
            return self._tsv_entry_func
        elif self.opts['json']:
            return self._json_entry_func
        else:
            return self._table_entry_func

    def _row_to_stdout(self, entry: str) -> None:
        dtcli.format.stdout(entry)
        self.rows.append(entry)
        self.n_rows += 1

    def new_entry(self, obj: object) -> None:
        entry_func = self._resolve_row_func()

        # Print header only on first try.
        if self.n_rows == 0 and self._should_print_header():
            header_str = entry_func(obj, header=True)
            if len(header_str) > 0:
                self._row_to_stdout(header_str)

        self._row_to_stdout(entry_func(obj))

    def new_entries(self, objects: list) -> None:
        for obj in objects:
            self.new_entry(obj)
