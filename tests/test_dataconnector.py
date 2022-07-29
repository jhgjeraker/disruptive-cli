import sys
from typing import Any, List
from dataclasses import dataclass
import tests.api_responses as responses
import tests.framework as framework


class TestDataconnector():

    def test_dataconnector_get(self, dt_dataconnector_mock):
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
                give_args=['data-connector-id', 'project-id'],
                give_res=responses.dataconnector,
                want_n_cols=5,
                want_n_rows=2,
                want_row_type=str,
                want_error=None,
            ),
            TestCase(
                name='--json',
                give_args=['data-connector-id', 'project-id', '--json'],
                give_res=responses.dataconnector,
                want_n_cols=5,
                want_n_rows=1,
                want_row_type=str,
                want_error=None,
            ),
            TestCase(
                name='--full',
                give_args=['data-connector-id', 'project-id', '--full'],
                give_res=responses.dataconnector,
                want_n_cols=9,
                want_n_rows=2,
                want_row_type=str,
                want_error=None,
            ),
            TestCase(
                name='missing IDs',
                give_args=[],
                give_res={},
                want_n_cols=0,
                want_n_rows=0,
                want_row_type=None,
                want_error=BaseException,
            ),
        ]

        for test in tests:
            sys.argv = ['main.py', 'data-connector', 'get'] + test.give_args
            dt_dataconnector_mock.res = test.give_res
            framework.table_test(test)

    def test_dataconnector_list(self, dt_dataconnector_mock):
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
                give_args=['project-id'],
                give_res=[
                    responses.dataconnector,
                    responses.dataconnector,
                    responses.dataconnector,
                ],
                want_n_cols=5,
                want_n_rows=4,
                want_row_type=str,
                want_error=None,
            ),
            TestCase(
                name='--json',
                give_args=['project-id', '--json'],
                give_res=[
                    responses.dataconnector,
                    responses.dataconnector,
                    responses.dataconnector,
                ],
                want_n_cols=5,
                want_n_rows=3,
                want_row_type=str,
                want_error=None,
            ),
            TestCase(
                name='missing ID',
                give_args=[],
                give_res=[],
                want_n_cols=0,
                want_n_rows=0,
                want_row_type=None,
                want_error=BaseException,
            ),
        ]

        for test in tests:
            sys.argv = ['main.py', 'data-connector', 'list'] + test.give_args
            dt_dataconnector_mock.res = test.give_res
            framework.table_test(test)

    def test_dataconnector_create(self, dt_dataconnector_mock):
        @dataclass
        class TestCase:
            name: str
            give_args: list
            give_res: dict
            want_n_rows: int
            want_n_cols: int
            want_row_type: Any
            want_error: Any = None

        tests = [
            TestCase(
                name='http-push minimal',
                give_args=['http-push', 'project-id', 'https://some-url.url'],
                give_res=responses.dataconnector,
                want_n_rows=2,
                want_n_cols=5,
                want_row_type=str,
            ),
            TestCase(
                name='http-push all args',
                give_args=[
                    'http-push',
                    'project-id',
                    'https://some-url.url',
                    '--signature-secret', 'abc',
                    '--headers', 'key1=value1,key2,key3=value3',
                    '--display-name', 'My DCON',
                    '--status', 'ACTIVE',
                    '--event-types', 'networkStatus,touch',
                    '--labels', 'key1=value1,key2',
                ],
                give_res=responses.dataconnector,
                want_n_rows=2,
                want_n_cols=5,
                want_row_type=str,
            ),
            TestCase(
                name='http-push --full',
                give_args=[
                    'http-push',
                    'project-id',
                    'https://some-url.url',
                    '--full',
                ],
                give_res=responses.dataconnector,
                want_n_rows=2,
                want_n_cols=9,
                want_row_type=str,
            ),
        ]

        for test in tests:
            sys.argv = ['main.py', 'data-connector', 'create'] + test.give_args
            dt_dataconnector_mock.res = test.give_res
            framework.table_test(test)

    def test_dataconnector_update(self, dt_dataconnector_mock):
        @dataclass
        class TestCase:
            name: str
            give_args: list
            give_res: dict
            want_n_rows: int
            want_n_cols: int
            want_row_type: Any
            want_error: Any = None

        tests = [
            TestCase(
                name='http-push minimal',
                give_args=['http-push', 'data-connector-id', 'project-id'],
                give_res=responses.dataconnector,
                want_n_rows=2,
                want_n_cols=5,
                want_row_type=str,
            ),
            TestCase(
                name='http-push --full',
                give_args=[
                    'http-push',
                    'data-connector-id',
                    'project-id',
                    '--full',
                ],
                give_res=responses.dataconnector,
                want_n_rows=2,
                want_n_cols=9,
                want_row_type=str,
            ),
            TestCase(
                name='http-push all args',
                give_args=[
                    'http-push',
                    'dcon-id',
                    'project-id',
                    '--url', 'https://some-url.url',
                    '--signature-secret', 'abc',
                    '--headers', 'key1=value1,key2,key3=value3',
                    '--display-name', 'My DCON',
                    '--status', 'ACTIVE',
                    '--event-types', 'networkStatus,touch',
                    '--labels', 'key1=value1,key2',
                ],
                give_res=responses.dataconnector,
                want_n_rows=2,
                want_n_cols=5,
                want_row_type=str,
            ),
        ]

        for test in tests:
            sys.argv = ['main.py', 'data-connector', 'update'] + test.give_args
            dt_dataconnector_mock.res = test.give_res
            framework.table_test(test)

    def test_dataconnector_delete(self, dt_dataconnector_mock):
        @dataclass
        class TestCase:
            name: str
            give_args: list
            give_res: dict
            want_n_rows: int
            want_n_cols: int
            want_row_type: Any
            want_error: Any = None

        tests = [
            TestCase(
                name='minimal',
                give_args=['data-connector-id', 'project-id'],
                give_res=responses.dataconnector,
                want_n_rows=0,
                want_n_cols=0,
                want_row_type=None,
            ),
            TestCase(
                name='minimal --full',
                give_args=['data-connector-id', 'project-id', '--full'],
                give_res=responses.dataconnector,
                want_n_rows=0,
                want_n_cols=0,
                want_row_type=None,
            ),
        ]

        for test in tests:
            sys.argv = ['main.py', 'data-connector', 'delete'] + test.give_args
            dt_dataconnector_mock.res = test.give_res
            framework.table_test(test)

    def test_dataconnector_sync(self, dt_dataconnector_mock):
        @dataclass
        class TestCase:
            name: str
            give_args: list
            give_res: dict
            want_n_rows: int
            want_n_cols: int
            want_row_type: Any
            want_error: Any = None

        tests = [
            TestCase(
                name='minimal',
                give_args=['data-connector-id', 'project-id'],
                give_res=responses.dataconnector,
                want_n_rows=0,
                want_n_cols=0,
                want_row_type=None,
            ),
            TestCase(
                name='--full',
                give_args=['data-connector-id', 'project-id', '--full'],
                give_res=responses.dataconnector,
                want_n_rows=0,
                want_n_cols=0,
                want_row_type=None,
            ),
        ]

        for test in tests:
            sys.argv = ['main.py', 'data-connector', 'sync'] + test.give_args
            dt_dataconnector_mock.res = test.give_res
            framework.table_test(test)

    def test_dataconnector_metrics(self, dt_dataconnector_mock):
        @dataclass
        class TestCase:
            name: str
            give_args: list
            give_res: dict
            want_n_rows: int
            want_n_cols: int
            want_row_type: Any
            want_error: Any = None

        tests = [
            TestCase(
                name='minimal',
                give_args=['data-connector-id', 'project-id'],
                give_res=responses.dataconnector,
                want_n_rows=2,
                want_n_cols=3,
                want_row_type=str,
            ),
            TestCase(
                name='--full',
                give_args=['data-connector-id', 'project-id', '--full'],
                give_res=responses.dataconnector,
                want_n_rows=2,
                want_n_cols=3,
                want_row_type=str,
            ),
        ]

        for test in tests:
            sys.argv = ['main.py', 'data-connector', 'metrics'] \
                + test.give_args
            dt_dataconnector_mock.res = test.give_res
            framework.table_test(test)
