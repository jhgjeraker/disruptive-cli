import sys
from typing import Any, List
from dataclasses import dataclass

import tests.api_responses as responses
import tests.framework as framework


class TestRole():

    def test_role_get(self, dt_role_mock):
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
                give_args=['project.user'],
                give_res=responses.role_project_user,
                want_n_cols=3,
                want_n_rows=2,
                want_row_type=str,
                want_error=None,
            ),
            TestCase(
                name='--full',
                give_args=['project.user', '--full'],
                give_res=responses.role_project_user,
                want_n_cols=4,
                want_n_rows=2,
                want_row_type=str,
                want_error=None,
            ),
        ]

        for test in tests:
            sys.argv = ['main.py', 'role', 'get'] + test.give_args
            dt_role_mock.res = test.give_res
            framework.table_test(test)

    def test_role_list(self, dt_role_mock):
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
                give_args=[],
                give_res=responses.roles,
                want_n_cols=3,
                want_n_rows=3,
                want_row_type=str,
                want_error=None,
            ),
            TestCase(
                name='--full',
                give_args=['--full'],
                give_res=responses.roles,
                want_n_cols=4,
                want_n_rows=3,
                want_row_type=str,
                want_error=None,
            ),
        ]

        for test in tests:
            sys.argv = ['main.py', 'role', 'list'] + test.give_args
            dt_role_mock.res = test.give_res
            framework.table_test(test)