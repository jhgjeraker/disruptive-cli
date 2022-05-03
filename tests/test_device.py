import sys
from typing import Any, List
from dataclasses import dataclass

import pytest

import dtcli
import tests.api_responses as responses


class TestDevice():

    def test_device_get(self, dt_device_mock):
        @dataclass
        class TestCase:
            name: str
            give_args: List[str]
            give_res: dict
            want_n_rows: int
            want_n_cols: int
            want_row_type: Any
            want_error: Any

        tests = [
            TestCase(
                name='minimal',
                give_args=['device_id'],
                give_res=responses.touch_sensor,
                want_n_cols=4,
                want_n_rows=2,
                want_row_type=str,
                want_error=None,
            ),
            TestCase(
                name='with project id',
                give_args=['device_id', '--project-id', 'project_id'],
                give_res=responses.touch_sensor,
                want_n_cols=4,
                want_n_rows=2,
                want_row_type=str,
                want_error=None,
            ),
            TestCase(
                name='missing device-id',
                give_res={},
                give_args=[],
                want_n_cols=0,
                want_n_rows=0,
                want_row_type=None,
                want_error=BaseException,
            ),
        ]

        for test in tests:
            sys.argv = ['main.py', 'device', 'get'] + test.give_args

            dt_device_mock.res = test.give_res

            if test.want_error is None:
                table = dtcli.cli.main()

                assert test.want_n_rows == table.n_rows, test.name
                assert test.want_n_cols == table.n_columns, test.name

                for row in table.rows:
                    assert isinstance(row, test.want_row_type), test.name
            else:
                with pytest.raises(test.want_error):
                    dtcli.cli.entry_point()

    def test_device_list(self, dt_device_mock):
        @dataclass
        class TestCase:
            name: str
            give_args: List[str]
            give_res: List[dict]
            want_n_rows: int
            want_n_cols: int
            want_row_type: Any
            want_error: Any

        tests = [
            TestCase(
                name='minimal',
                give_args=['project_id'],
                give_res=[responses.touch_sensor],
                want_n_cols=4,
                want_n_rows=2,
                want_row_type=str,
                want_error=None,
            ),
            TestCase(
                name='multiple return',
                give_args=['project_id'],
                give_res=[
                    responses.touch_sensor,
                    responses.touch_sensor,
                    responses.touch_sensor,
                    responses.touch_sensor,
                    responses.touch_sensor,
                ],
                want_n_cols=4,
                want_n_rows=6,
                want_row_type=str,
                want_error=None,
            ),
            TestCase(
                name='full width',
                give_args=['project_id', '--full'],
                give_res=[responses.touch_sensor],
                want_n_cols=7,
                want_n_rows=2,
                want_row_type=str,
                want_error=None,
            ),
            TestCase(
                name='all flags',
                give_args=[
                    'project_id',
                    '--query', 'touch',
                    '--device-ids', 'xid1,xid2,xid3',
                    '--device-types', 'touch,temperature',
                    '--label-filters', 'key1=value1,key2,key3',
                ],
                give_res=[responses.touch_sensor],
                want_n_cols=4,
                want_n_rows=2,
                want_row_type=str,
                want_error=None,
            ),
            TestCase(
                name='missing project id',
                give_args=[
                    '--query', 'touch',
                    '--device-ids', 'xid1,xid2,xid3',
                    '--device-types', 'touch,temperature',
                    '--label-filters', 'key1=value1,key2,key3',
                ],
                give_res=[responses.touch_sensor],
                want_n_cols=4,
                want_n_rows=2,
                want_row_type=str,
                want_error=BaseException,
            ),
        ]

        for test in tests:
            sys.argv = ['main.py', 'device', 'list'] + test.give_args

            dt_device_mock.res = test.give_res

            if test.want_error is None:
                table = dtcli.cli.main()

                assert test.want_n_rows == table.n_rows, test.name
                assert test.want_n_cols == table.n_columns, test.name

                for row in table.rows:
                    assert isinstance(row, test.want_row_type), test.name
            else:
                with pytest.raises(test.want_error):
                    dtcli.cli.entry_point()
