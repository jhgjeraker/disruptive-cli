import sys
from typing import Any
from dataclasses import dataclass

import pytest

import dtcli
import tests.api_responses as responses


class TestDevice():

    def test_device_get(self, dt_mock):
        @dataclass
        class TestCase:
            name: str
            give_args: list[str]
            give_raw: dict
            want_n_rows: int
            want_n_cols: int
            want_row_type: Any
            want_error: Any

        tests = [
            TestCase(
                name='successfull device get',
                give_args=['device_id'],
                give_raw=responses.touch_sensor,
                want_n_cols=4,
                want_n_rows=2,
                want_row_type=str,
                want_error=None,
            ),
            TestCase(
                name='successfull device get /w project id',
                give_args=['device_id', '--project-id', 'project_id'],
                give_raw=responses.touch_sensor,
                want_n_cols=4,
                want_n_rows=2,
                want_row_type=str,
                want_error=None,
            ),
            TestCase(
                name='missing device-id',
                give_raw={},
                give_args=[],
                want_n_cols=0,
                want_n_rows=0,
                want_row_type=None,
                want_error=BaseException,
            ),
            TestCase(
                name='supress header',
                give_args=['xid', '--no-header'],
                give_raw=responses.touch_sensor,
                want_n_rows=1,
                want_n_cols=4,
                want_row_type=str,
                want_error=None,
            ),
        ]

        for test in tests:
            sys.argv = ['main.py', 'device', 'get'] + test.give_args

            dt_mock.raw = test.give_raw

            if test.want_error is None:
                table = dtcli.cli.entry_point()

                assert test.want_n_rows == table.n_rows
                assert test.want_n_cols == table.n_columns

                for row in table.rows:
                    assert isinstance(row, test.want_row_type)
            else:
                with pytest.raises(test.want_error):
                    dtcli.cli.entry_point()
