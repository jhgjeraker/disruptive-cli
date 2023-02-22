import sys
from typing import Any, List
from dataclasses import dataclass

import tests.api_responses as responses
import tests.framework as framework


class TestEvent():

    def test_event_list(self, dt_event_mock):
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
                give_args=['device-id', 'project-id'],
                give_res=responses.events_list,
                want_n_cols=3,
                want_n_rows=7,
                want_row_type=str,
                want_error=None,
            ),
            TestCase(
                name='--full',
                give_args=['device-id', 'project-id', '--full'],
                give_res=responses.events_list,
                want_n_cols=5,
                want_n_rows=7,
                want_row_type=str,
                want_error=None,
            ),
            TestCase(
                name='all args',
                give_args=[
                    'device-id',
                    'project-id',
                    '--event-types', 'touch,temperature,networkStatus',
                    '--start-time', '2023-02-19T14:20:00Z',
                    '--end-time', '2023-02-20T14:20:00Z',
                ],
                give_res=responses.events_list,
                want_n_cols=3,
                want_n_rows=7,
                want_row_type=str,
                want_error=None,
            ),
        ]

        for test in tests:
            sys.argv = ['main.py', 'event', 'list'] + test.give_args
            dt_event_mock.res = test.give_res
            framework.table_test(test)

    def test_event_stream(self, dt_event_mock):
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
                give_res=responses.events_list,
                want_n_rows=6,
                want_n_cols=3,
                want_row_type=str,
                want_error=None,
            ),
            TestCase(
                name='--full',
                give_args=['project-id', '--full'],
                give_res=responses.events_list,
                want_n_rows=6,
                want_n_cols=5,
                want_row_type=str,
                want_error=None,
            ),
        ]

        for test in tests:
            sys.argv = ['main.py', 'event', 'stream'] + test.give_args
            dt_event_mock.res = test.give_res
            framework.table_test(test)