import sys
from typing import Any, List
from dataclasses import dataclass

import tests.api_responses as responses
import tests.framework as framework


class TestServiceAccount():

    def test_serviceaccount_get(self, dt_serviceaccount_mock):
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
                give_args=['sa-id', 'project-id'],
                give_res=responses.service_account,
                want_n_cols=4,
                want_n_rows=2,
                want_row_type=str,
                want_error=None,
            ),
            TestCase(
                name='--full',
                give_args=['sa-id', 'project-id', '--full'],
                give_res=responses.service_account,
                want_n_cols=6,
                want_n_rows=2,
                want_row_type=str,
                want_error=None,
            ),
        ]

        for test in tests:
            sys.argv = ['main.py', 'service-account', 'get'] + test.give_args
            dt_serviceaccount_mock.res = test.give_res
            framework.table_test(test)

    def test_serviceaccount_list(self, dt_serviceaccount_mock):
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
                give_args=['project-id'],
                give_res=responses.service_accounts,
                want_n_cols=4,
                want_n_rows=4,
                want_row_type=str,
                want_error=None,
            ),
            TestCase(
                name='--full',
                give_args=['project-id', '--full'],
                give_res=responses.service_accounts,
                want_n_cols=6,
                want_n_rows=4,
                want_row_type=str,
                want_error=None,
            ),
        ]

        for test in tests:
            sys.argv = ['main.py', 'service-account', 'list'] + test.give_args
            dt_serviceaccount_mock.res = test.give_res
            framework.table_test(test)

    def test_serviceaccount_create(self, dt_serviceaccount_mock):
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
                give_args=['project-id'],
                give_res=responses.service_account,
                want_n_cols=4,
                want_n_rows=2,
                want_row_type=str,
                want_error=None,
            ),
            TestCase(
                name='--full',
                give_args=['project-id', '--full'],
                give_res=responses.service_account,
                want_n_cols=6,
                want_n_rows=2,
                want_row_type=str,
                want_error=None,
            ),
            TestCase(
                name='all args',
                give_args=[
                    'project-id',
                    '--basic-auth', 'yes',
                    '--display-name', 'test-sa',
                ],
                give_res=responses.service_account,
                want_n_cols=4,
                want_n_rows=2,
                want_row_type=str,
                want_error=None,
            ),
            TestCase(
                name='no basic auth',
                give_args=[
                    'project-id',
                    '--basic-auth', 'no',
                ],
                give_res=responses.service_account,
                want_n_cols=4,
                want_n_rows=2,
                want_row_type=str,
                want_error=None,
            ),
        ]

        for test in tests:
            sys.argv = ['main.py', 'service-account', 'create'] + test.give_args
            dt_serviceaccount_mock.res = test.give_res
            framework.table_test(test)

    def test_serviceaccount_update(self, dt_serviceaccount_mock):
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
                give_args=['sa-id', 'project-id'],
                give_res=responses.service_account,
                want_n_cols=4,
                want_n_rows=2,
                want_row_type=str,
                want_error=None,
            ),
            TestCase(
                name='--full',
                give_args=['sa-id', 'project-id', '--full'],
                give_res=responses.service_account,
                want_n_cols=6,
                want_n_rows=2,
                want_row_type=str,
                want_error=None,
            ),
            TestCase(
                name='all args',
                give_args=[
                    'sa-id',
                    'project-id',
                    '--display-name', 'new-name',
                    '--basic-auth', 'no',
                ],
                give_res=responses.service_account,
                want_n_cols=4,
                want_n_rows=2,
                want_row_type=str,
                want_error=None,
            ),
        ]

        for test in tests:
            sys.argv = ['main.py', 'service-account', 'update'] + test.give_args
            dt_serviceaccount_mock.res = test.give_res
            framework.table_test(test)

    def test_serviceaccount_delete(self, dt_serviceaccount_mock):
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
                give_args=['sa-id', 'project-id'],
                give_res=None,
                want_n_cols=0,
                want_n_rows=0,
                want_row_type=None,
                want_error=None,
            ),
            TestCase(
                name='--full',
                give_args=['sa-id', 'project-id', '--full'],
                give_res=None,
                want_n_cols=0,
                want_n_rows=0,
                want_row_type=None,
                want_error=None,
            ),
        ]

        for test in tests:
            sys.argv = ['main.py', 'service-account', 'delete'] + test.give_args
            dt_serviceaccount_mock.res = test.give_res
            framework.table_test(test)

    def test_serviceaccount_key_get(self, dt_serviceaccount_mock):
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
                give_args=['key-id', 'sa-id', 'project-id'],
                give_res=responses.service_account_key,
                want_n_cols=3,
                want_n_rows=2,
                want_row_type=str,
                want_error=None,
            ),
            TestCase(
                name='--full',
                give_args=['key-id', 'sa-id', 'project-id', '--full'],
                give_res=responses.service_account_key,
                want_n_cols=3,
                want_n_rows=2,
                want_row_type=str,
                want_error=None,
            ),
        ]

        for test in tests:
            sys.argv = ['main.py', 'service-account', 'key', 'get'] + test.give_args
            dt_serviceaccount_mock.res = test.give_res
            framework.table_test(test)

    def test_serviceaccount_key_create(self, dt_serviceaccount_mock):
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
                give_args=['sa-id', 'project-id'],
                give_res=responses.service_account_key,
                want_n_cols=3,
                want_n_rows=2,
                want_row_type=str,
                want_error=None,
            ),
            TestCase(
                name='--full',
                give_args=['sa-id', 'project-id', '--full'],
                give_res=responses.service_account_key,
                want_n_cols=3,
                want_n_rows=2,
                want_row_type=str,
                want_error=None,
            ),
        ]

        for test in tests:
            sys.argv = ['main.py', 'service-account', 'key', 'create'] + test.give_args
            dt_serviceaccount_mock.res = test.give_res
            framework.table_test(test)

    def test_serviceaccount_key_list(self, dt_serviceaccount_mock):
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
                give_args=['sa-id', 'project-id'],
                give_res=responses.service_account_keys,
                want_n_cols=3,
                want_n_rows=6,
                want_row_type=str,
                want_error=None,
            ),
            TestCase(
                name='--full',
                give_args=['sa-id', 'project-id', '--full'],
                give_res=responses.service_account_keys,
                want_n_cols=3,
                want_n_rows=6,
                want_row_type=str,
                want_error=None,
            ),
        ]

        for test in tests:
            sys.argv = ['main.py', 'service-account', 'key', 'list'] + test.give_args
            dt_serviceaccount_mock.res = test.give_res
            framework.table_test(test)

    def test_serviceaccount_key_delete(self, dt_serviceaccount_mock):
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
                give_args=['key-id', 'sa-id', 'project-id'],
                give_res=None,
                want_n_cols=0,
                want_n_rows=0,
                want_row_type=None,
                want_error=None,
            ),
            TestCase(
                name='--full',
                give_args=['key-id', 'sa-id', 'project-id', '--full'],
                give_res=None,
                want_n_cols=0,
                want_n_rows=0,
                want_row_type=None,
                want_error=None,
            ),
        ]

        for test in tests:
            sys.argv = ['main.py', 'service-account', 'key', 'delete'] + test.give_args
            dt_serviceaccount_mock.res = test.give_res
            framework.table_test(test)