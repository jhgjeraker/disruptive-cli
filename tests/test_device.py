import sys
from typing import Any, List
from dataclasses import dataclass

import tests.api_responses as responses
import tests.framework as framework


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
                name='w/ args',
                give_args=['device_id', '--project-id', 'project_id'],
                give_res=responses.touch_sensor,
                want_n_cols=4,
                want_n_rows=2,
                want_row_type=str,
                want_error=None,
            ),
            TestCase(
                name='missing device-id',
                give_args=[],
                give_res={},
                want_n_cols=0,
                want_n_rows=0,
                want_row_type=None,
                want_error=BaseException,
            ),
        ]

        for test in tests:
            sys.argv = ['main.py', 'device', 'get'] + test.give_args
            dt_device_mock.res = test.give_res
            framework.table_test(test)

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
                want_row_type=None,
                want_error=BaseException,
            ),
        ]

        for test in tests:
            sys.argv = ['main.py', 'device', 'list'] + test.give_args
            dt_device_mock.res = test.give_res
            framework.table_test(test)

    def test_device_transfer(self, dt_device_mock):
        @dataclass
        class TestCase:
            name: str
            give_args: List[str]
            give_res: Any
            want_n_rows: int
            want_n_cols: int
            want_row_type: Any
            want_error: Any

        tests = [
            TestCase(
                name='minimal',
                give_args=[
                    'xid1,xid2',  # device-ids
                    'project1',   # source-project-id
                    'project2',   # target-project-id
                ],
                give_res=[],
                want_n_rows=0,
                want_n_cols=4,
                want_row_type=None,
                want_error=None,
            ),
            TestCase(
                name='transfer error',
                give_args=[
                    'xid1,bad_id',  # device-ids
                    'project1',     # source-project-id
                    'project2',     # target-project-id
                ],
                give_res=[responses.transfer_device_error],
                want_n_rows=2,
                want_n_cols=4,
                want_row_type=str,
                want_error=None,
            ),
        ]

        for test in tests:
            sys.argv = ['main.py', 'device', 'transfer'] + test.give_args
            dt_device_mock.res = test.give_res
            framework.table_test(test)

    def test_device_label_set(self, dt_device_mock):
        @dataclass
        class TestCase:
            name: str
            give_args: List[str]
            give_res: Any
            want_n_rows: int
            want_n_cols: int
            want_row_type: Any
            want_error: Any

        tests = [
            TestCase(
                name='minimal',
                give_args=[
                    'xid1,xid2,xid3',           # device-ids
                    'project1',                 # project-id
                    'key1=value1,key2=value2',  # labels
                ],
                give_res=[],
                want_n_rows=0,
                want_n_cols=4,
                want_row_type=None,
                want_error=None,
            ),
            TestCase(
                name='transfer error',
                give_args=[
                    'xid1,xid2,xid3',           # device-ids
                    'project1',                 # project-id
                    'key1=value1,key2=value2',  # labels
                ],
                give_res=[
                    responses.label_set_error,
                    responses.label_set_error,
                ],
                want_n_rows=3,
                want_n_cols=4,
                want_row_type=str,
                want_error=None,
            ),
            TestCase(
                name='keys only',
                give_args=[
                    'xid1,xid2',       # device-ids
                    'project1',        # project-id
                    'key1,key2,key3',  # labels
                ],
                give_res=[],
                want_n_rows=0,
                want_n_cols=4,
                want_row_type=str,
                want_error=None,
            ),
        ]

        for test in tests:
            sys.argv = ['main.py', 'device', 'label', 'set'] + test.give_args
            dt_device_mock.res = test.give_res
            framework.table_test(test)
