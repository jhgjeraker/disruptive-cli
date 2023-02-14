import sys
from typing import Any, List
from dataclasses import dataclass

import tests.api_responses as responses
import tests.framework as framework


class TestOrganization():

    def test_organization_get(self, dt_organization_mock):
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
                give_args=['org_id'],
                give_res=responses.organization,
                want_n_cols=2,
                want_n_rows=2,
                want_row_type=str,
                want_error=None,
            ),
            TestCase(
                name='--full',
                give_args=['org_id', '--full'],
                give_res=responses.organization,
                want_n_cols=2,
                want_n_rows=2,
                want_row_type=str,
                want_error=None,
            ),
        ]

        for test in tests:
            sys.argv = ['main.py', 'organization', 'get'] + test.give_args
            dt_organization_mock.res = test.give_res
            framework.table_test(test)

    def test_organization_list(self, dt_organization_mock):
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
                give_res=responses.organizations,
                want_n_cols=2,
                want_n_rows=4,
                want_row_type=str,
                want_error=None,
            ),
            TestCase(
                name='--full',
                give_args=['--full'],
                give_res=responses.organizations,
                want_n_cols=2,
                want_n_rows=4,
                want_row_type=str,
                want_error=None,
            ),
        ]

        for test in tests:
            sys.argv = ['main.py', 'organization', 'list'] + test.give_args
            dt_organization_mock.res = test.give_res
            framework.table_test(test)

    def test_organization_permissions(self, dt_organization_mock):
        @dataclass
        class TestCase:
            name: str
            give_args: List[str]
            give_res: List[str]
            want_n_rows: int
            want_n_cols: int
            want_row_type: Any
            want_error: Any

        tests = [
            TestCase(
                name='minimal',
                give_args=['org-id'],
                give_res=responses.organization_permissions,
                want_n_cols=0,
                want_n_rows=0,
                want_row_type=str,
                want_error=None,
            ),
        ]

        for test in tests:
            sys.argv = ['main.py', 'organization', 'permissions'] \
                + test.give_args
            dt_organization_mock.res = test.give_res
            framework.table_test(test)

    def test_organization_member_add(self, dt_organization_mock):
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
                give_args=['org-id', 'email', 'role1,role2'],
                give_res=responses.organization_member,
                want_n_cols=5,
                want_n_rows=2,
                want_row_type=str,
                want_error=None,
            ),
            TestCase(
                name='--full',
                give_args=['org-id', 'email', 'role1,role2', '--full'],
                give_res=responses.organization_member,
                want_n_cols=7,
                want_n_rows=2,
                want_row_type=str,
                want_error=None,
            ),
        ]

        for test in tests:
            sys.argv = ['main.py', 'organization', 'member', 'add'] \
                + test.give_args
            dt_organization_mock.res = test.give_res
            framework.table_test(test)

    def test_organization_member_remove(self, dt_organization_mock):
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
                give_args=['member-id', 'org-id'],
                give_res=None,
                want_n_cols=0,
                want_n_rows=0,
                want_row_type=None,
                want_error=None,
            ),
            TestCase(
                name='--full',
                give_args=['member-id', 'org-id', '--full'],
                give_res=None,
                want_n_cols=0,
                want_n_rows=0,
                want_row_type=None,
                want_error=None,
            ),
        ]

        for test in tests:
            sys.argv = ['main.py', 'organization', 'member', 'remove'] \
                + test.give_args
            dt_organization_mock.res = test.give_res
            framework.table_test(test)

    def test_organization_member_get(self, dt_organization_mock):
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
                give_args=['member-id', 'org-id'],
                give_res=responses.organization_member,
                want_n_cols=5,
                want_n_rows=2,
                want_row_type=str,
                want_error=None,
            ),
            TestCase(
                name='--full',
                give_args=['member-id', 'org-id', '--full'],
                give_res=responses.organization_member,
                want_n_cols=7,
                want_n_rows=2,
                want_row_type=str,
                want_error=None,
            ),
        ]

        for test in tests:
            sys.argv = ['main.py', 'organization', 'member', 'get'] \
                + test.give_args
            dt_organization_mock.res = test.give_res
            framework.table_test(test)

    def test_organization_member_list(self, dt_organization_mock):
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
                give_args=['org-id'],
                give_res=responses.organization_members,
                want_n_cols=5,
                want_n_rows=5,
                want_row_type=str,
                want_error=None,
            ),
            TestCase(
                name='--full',
                give_args=['org-id', '--full'],
                give_res=responses.organization_members,
                want_n_cols=7,
                want_n_rows=5,
                want_row_type=str,
                want_error=None,
            ),
        ]

        for test in tests:
            sys.argv = ['main.py', 'organization', 'member', 'list'] \
                + test.give_args
            dt_organization_mock.res = test.give_res
            framework.table_test(test)

    def test_organization_member_invite_url(self, dt_organization_mock):
        @dataclass
        class TestCase:
            name: str
            give_args: List[str]
            give_res: str
            want_n_rows: int
            want_n_cols: int
            want_row_type: Any
            want_error: Any

        tests = [
            TestCase(
                name='minimal',
                give_args=['member-id', 'org-id'],
                give_res='some-url',
                want_n_cols=0,
                want_n_rows=0,
                want_row_type=str,
                want_error=None,
            ),
            TestCase(
                name='--full',
                give_args=['member-id', 'org-id', '--full'],
                give_res='some-url',
                want_n_cols=0,
                want_n_rows=0,
                want_row_type=str,
                want_error=None,
            ),
        ]

        for test in tests:
            sys.argv = ['main.py', 'organization', 'member', 'invite-url'] \
                + test.give_args
            dt_organization_mock.res = test.give_res
            framework.table_test(test)
