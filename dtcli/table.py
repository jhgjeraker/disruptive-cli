import json

import dtcli
import disruptive


class Column():
    def __init__(self, name: str, hide: bool, width: int | None = None):
        self.name = name
        self.hide = hide
        self.width = width if width is not None else len(name)

    @property
    def attr_name(self):
        return dtcli.format.str_attr_format(self.name)

    @property
    def col_name(self):
        return dtcli.format.str_col_format(self.name)

    @classmethod
    def from_opts(cls, name: str):
        return cls(name, False, len(name))

    def get_obj_attr_str(self, obj: object):
        if hasattr(obj, self.attr_name):
            attr = getattr(obj, self.attr_name)
            if isinstance(attr, disruptive.outputs.OutputBase):
                attr = json.dumps(attr._raw)
            elif isinstance(attr, dict):
                attr = json.dumps(attr)
            return str(attr)
        else:
            return ''


class Table():
    def __init__(self, default_columns: list[Column], opts: dict):
        self.opts = opts
        self.row_count = 0
        self.columns = self._parse_columns(default_columns)

    def _parse_columns(self, default_columns: list[Column]):
        # If no columns opts are given, use default.
        if self.opts['columns'] is None:
            use_columns = default_columns

            # If `wide` option not provided, hide some of the columns.
            if 'wide' not in self.opts['output']:
                use_columns = [c for c in use_columns if not c.hide]

        else:
            use_columns = self.opts['columns'].split(',')
            use_columns = [Column.from_opts(c) for c in use_columns]

        # Prune excluded columns if option is given.
        if self.opts['exclude'] is not None:
            filt = self.opts['exclude'].split(',')
            filt = [dtcli.format.str_attr_format(name) for name in filt]
            use_columns = [c for c in use_columns if c.attr_name not in filt]

        return use_columns

    def _print_header(self):
        pass

    def expand_rows(self, objects: list[object]):
        for i, col in enumerate(self.columns):
            for obj in objects:
                attr_width = len(col.get_obj_attr_str(obj))
                if attr_width > col.width:
                    self.columns[i].width = attr_width

    def _csv_row_func(self, obj: object, header: bool = False):
        line = ''
        for col in self.columns:
            if header:
                value = col.attr_name
            else:
                value = col.get_obj_attr_str(obj)
            line += f'{str(value):<{col.width}}' + ','

    def _table_row_func(self, obj: object, header: bool = False):
        line = ''
        for col in self.columns:
            if header:
                value = col.col_name
            else:
                value = col.get_obj_attr_str(obj)
            line += f'{str(value):<{col.width}}'
            line += ' ' * dtcli.cfg['output']['padding']
        dtcli.output.stdout(line[:-dtcli.cfg['output']['padding']])

    def _resolve_row_func(self):
        if 'csv' in self.opts['output']:
            pass
        elif 'tsv' in self.opts['output']:
            pass
        else:
            return self._table_row_func

    def new_row(self, obj: object):
        row_func = self._resolve_row_func()

        # Print header only on first try.
        if self.row_count == 0 and self.opts['header']:
            row_func(obj, header=True)

        row_func(obj)
        self.row_count += 1

    def print_rows(self, objects: list[object]):
        for obj in objects:
            self.new_row(obj)
