import json

import disruptive

import dtcli.format


class Column():
    def __init__(self, name: str, hidden: bool, width: int | None = None):
        self.name = name
        self.hidden = hidden
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
                attr = json.dumps(attr.raw)
            elif isinstance(attr, dict):
                attr = json.dumps(attr)
            return str(attr)
        else:
            return ''


class Table():
    def __init__(self, default_columns: list, cfg: dict, opts: dict):
        self.cfg = cfg
        self.opts = opts
        self.row_count = 0
        self.columns = self._parse_columns(default_columns)

    def _parse_columns(self, columns: list[Column]):
        # Make a copy of input.
        use_columns = [c for c in columns]

        # If --include is provided, only use columns specified.
        if self.opts['include'] is not None:
            names = self.opts['include'].split(',')
            names = [dtcli.format.str_attr_format(n) for n in names]
            return [c for c in use_columns if c.attr_name in names]

        # If `--full` is not provided, show only partial output.
        if not self.opts['full']:
            return [c for c in use_columns if not c.hidden]

        return use_columns

    def _should_print_header(self):
        if self.opts['no_header'] or len(self.columns) < 2:
            return False
        else:
            return True

    def expand_rows(self, objects: list):
        for i, col in enumerate(self.columns):
            for obj in objects:
                attr_width = len(col.get_obj_attr_str(obj))
                if attr_width > col.width:
                    self.columns[i].width = attr_width

    def _csv_entry_func(self, obj: object, header: bool = False):
        line = ''
        for col in self.columns:
            value = col.attr_name if header else col.get_obj_attr_str(obj)
            line += str(value) + ','
        return line[:-1]

    def _tsv_entry_func(self, obj: object, header: bool = False):
        line = ''
        for col in self.columns:
            value = col.attr_name if header else col.get_obj_attr_str(obj)
            line += str(value) + '\t'
        return line[:-1]

    def _table_entry_func(self, obj: object, header: bool = False):
        line = ''
        for col in self.columns:
            if header:
                value = col.col_name
            else:
                value = col.get_obj_attr_str(obj)
            line += f'{str(value):<{col.width}}'
            line += ' ' * self.cfg['output']['padding']
        return line[:-self.cfg['output']['padding']]

    def _json_entry_func(self, obj: object, header: bool = False):
        if header:
            return ''

        if isinstance(obj, disruptive.outputs.OutputBase):
            return json.dumps(obj.raw)
        else:
            return ''

    def _resolve_row_func(self):
        if self.opts['csv']:
            return self._csv_entry_func
        elif self.opts['tsv']:
            return self._tsv_entry_func
        elif self.opts['json']:
            return self._json_entry_func
        else:
            return self._table_entry_func

    def new_entry(self, obj: object):
        entry_func = self._resolve_row_func()

        # Print header only on first try.
        if self.row_count == 0 and self._should_print_header():
            header_str = entry_func(obj, header=True)
            if len(header_str) > 0:
                dtcli.format.stdout(header_str)

        dtcli.format.stdout(entry_func(obj))
        self.row_count += 1

    def new_entries(self, objects: list):
        for obj in objects:
            self.new_entry(obj)
