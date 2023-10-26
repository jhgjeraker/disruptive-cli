import sys
from typing import List, Any
from dataclasses import dataclass

import tests.api_responses as responses
import tests.framework as framework


class TestClaim():

    def test_claim_info(self, dt_claim_mock):
        @dataclass
        class TestCase:
            name: str
            give_args: List[str]
            give_res: dict
            want_n_rows: int
            want_n_cols: int
            want_row_type: Any
            want_error: Any = None

        tests = [
            TestCase(
                name='device',
                give_args=['cbvatvi87d5i8s51aagg'],
                want_n_cols=4,
                want_n_rows=2,
                want_row_type=str,
                give_res=responses.claim_device,
            ),
            TestCase(
                name='device with org_id',
                give_args=[
                    'cbvatvi87d5i8s51aagg',
                    '--organization-id', '123123',
                ],
                want_n_cols=4,
                want_n_rows=2,
                want_row_type=str,
                give_res=responses.claim_device,
            ),
            TestCase(
                name='kit',
                give_args=['abc-01-abc'],
                want_n_cols=4,
                want_n_rows=3,
                want_row_type=str,
                give_res=responses.claim_kit,
            ),
        ]

        for test in tests:
            sys.argv = ['main.py', 'claim', 'info'] + test.give_args
            dt_claim_mock.res = test.give_res
            framework.table_test(test)
