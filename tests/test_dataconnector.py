import sys
from typing import Any, List
from dataclasses import dataclass

import pytest

import dtcli
import tests.api_responses as responses


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
                give_args=['dataconnector-id', 'project-id'],
                give_res=responses.dataconnector,
                want_n_cols=5,
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
            sys.argv = ['main.py', 'dataconnector', 'get'] + test.give_args
            dt_dataconnector_mock.res = test.give_res

            if test.want_error is None:
                table = dtcli.cli.main()

                assert test.want_n_rows == table.n_rows, test.name
                assert test.want_n_cols == table.n_columns, test.name

                for row in table.rows:
                    assert isinstance(row, test.want_row_type), test.name
            else:
                with pytest.raises(test.want_error):
                    dtcli.cli.main()

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
            sys.argv = ['main.py', 'dataconnector', 'list'] + test.give_args
            dt_dataconnector_mock.res = test.give_res

            if test.want_error is None:
                table = dtcli.cli.main()

                assert test.want_n_rows == table.n_rows, test.name
                assert test.want_n_cols == table.n_columns, test.name

                for row in table.rows:
                    assert isinstance(row, test.want_row_type), test.name
            else:
                with pytest.raises(test.want_error):
                    dtcli.cli.main()
