import sys
from typing import Any, Optional
from dataclasses import dataclass

import pytest

import dtcli

class TestFormat():

    def test_to_bool(self):
        @dataclass
        class TestCase:
            name: str
            give_value: Any
            want_result: Optional[bool]
            want_error: Any = None

        tests = [
            TestCase('integer 1', 1, True),
            TestCase('integer 0', 0, False),
            TestCase('float 1.0', 1.0, True),
            TestCase('float 0.0', 0.0, False),
            TestCase('float 1.3', 1.3, True),
            TestCase('float 0.3', 0.3, False),
            TestCase('str "true"', 'true', True),
            TestCase('str "True"', 'true', True),
            TestCase('str "yes"', 'yes', True),
            TestCase('str "false"', 'false', False),
            TestCase('str "no"', 'no', False),
            TestCase('None', None, None, want_error=TypeError),
        ]

        for test in tests:
            if test.want_error is None:
                result = dtcli.format.to_bool(test.give_value)
                assert result == test.want_result
            else:
                with pytest.raises(test.want_error):
                    dtcli.format.to_bool(test.give_value)