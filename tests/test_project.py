import sys
from typing import List, Any
from dataclasses import dataclass

import tests.api_responses as responses
import tests.framework as framework


class TestProject():

    def test_project_get(self, dt_project_mock):
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
                give_args=['project_id'],
                give_res=responses.project,
                want_n_cols=4,
                want_n_rows=2,
                want_row_type=str,
                want_error=None,
            ),
            TestCase(
                name='--full',
                give_args=['project_id', '--full'],
                give_res=responses.project,
                want_n_cols=6,
                want_n_rows=2,
                want_row_type=str,
                want_error=None,
            ),
        ]

        for test in tests:
            sys.argv = ['main.py', 'project', 'get'] + test.give_args
            dt_project_mock.res = test.give_res
            framework.table_test(test)

    def test_project_list(self, dt_project_mock):
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
                give_res=responses.projects,
                want_n_cols=4,
                want_n_rows=5,
                want_row_type=str,
                want_error=None,
            ),
            TestCase(
                name='all args',
                give_args=[
                    '--organization-id', 'target-org',
                    '--query', 'oslo',
                ],
                give_res=responses.projects,
                want_n_cols=4,
                want_n_rows=5,
                want_row_type=str,
                want_error=None,
            ),
            TestCase(
                name='--full',
                give_args=['--full'],
                give_res=responses.projects,
                want_n_cols=6,
                want_n_rows=5,
                want_row_type=str,
                want_error=None,
            ),
        ]

        for test in tests:
            sys.argv = ['main.py', 'project', 'list'] + test.give_args
            dt_project_mock.res = test.give_res
            framework.table_test(test)

    def test_project_create(self, dt_project_mock):
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
                give_args=[
                    'org-id',
                    'display-name',
                ],
                give_res=responses.project,
                want_n_cols=4,
                want_n_rows=2,
                want_row_type=str,
                want_error=None,
            ),
            TestCase(
                name='--full',
                give_args=[
                    'org-id',
                    'display-name',
                    '--full',
                ],
                give_res=responses.project,
                want_n_cols=6,
                want_n_rows=2,
                want_row_type=str,
                want_error=None,
            ),
        ]

        for test in tests:
            sys.argv = ['main.py', 'project', 'create'] + test.give_args
            dt_project_mock.res = test.give_res
            framework.table_test(test)

    def test_project_update(self, dt_project_mock):
        @dataclass
        class TestCase:
            name: str
            give_args: List[str]
            want_n_rows: int
            want_n_cols: int
            want_row_type: Any
            want_error: Any

        tests = [
            TestCase(
                name='minimal',
                give_args=[
                    'project-id',
                    '--display-name', 'new name',
                ],
                want_n_cols=0,
                want_n_rows=0,
                want_row_type=None,
                want_error=None,
            ),
            TestCase(
                name='--full',
                give_args=[
                    'project-id',
                    '--display-name', 'new name',
                    '--full',
                ],
                want_n_cols=0,
                want_n_rows=0,
                want_row_type=None,
                want_error=None,
            ),
        ]

        for test in tests:
            sys.argv = ['main.py', 'project', 'update'] + test.give_args
            dt_project_mock.res = None
            framework.table_test(test)

    def test_project_delete(self, dt_project_mock):
        @dataclass
        class TestCase:
            name: str
            give_args: List[str]
            want_n_rows: int
            want_n_cols: int
            want_row_type: Any
            want_error: Any

        tests = [
            TestCase(
                name='minimal',
                give_args=[
                    'project-id',
                ],
                want_n_cols=0,
                want_n_rows=0,
                want_row_type=None,
                want_error=None,
            ),
            TestCase(
                name='--full',
                give_args=[
                    'project-id',
                    '--full',
                ],
                want_n_cols=0,
                want_n_rows=0,
                want_row_type=None,
                want_error=None,
            ),
        ]

        for test in tests:
            sys.argv = ['main.py', 'project', 'delete'] + test.give_args
            dt_project_mock.res = None
            framework.table_test(test)

    def test_project_permissions(self, dt_project_mock):
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
                give_args=[
                    'project-id',
                ],
                give_res=responses.project_permissions,
                want_n_cols=0,
                want_n_rows=0,
                want_row_type=None,
                want_error=None,
            ),
            TestCase(
                name='--full',
                give_args=[
                    'project-id',
                    '--full',
                ],
                give_res=responses.project_permissions,
                want_n_cols=0,
                want_n_rows=0,
                want_row_type=None,
                want_error=None,
            ),
        ]

        for test in tests:
            sys.argv = ['main.py', 'project', 'permissions'] + test.give_args
            dt_project_mock.res = None
            framework.table_test(test)

    def test_project_member_add(self, dt_project_mock):
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
                give_args=[
                    'project-id',
                    'email',
                    'role1,role2,role3',
                ],
                give_res=responses.member_pending_user,
                want_n_cols=5,
                want_n_rows=2,
                want_row_type=str,
                want_error=None,
            ),
            TestCase(
                name='--full',
                give_args=[
                    'project-id',
                    'email',
                    'role1,role2,role3',
                    '--full',
                ],
                give_res=responses.member_pending_user,
                want_n_cols=7,
                want_n_rows=2,
                want_row_type=str,
                want_error=None,
            ),
        ]

        for test in tests:
            sys.argv = ['main.py', 'project', 'member', 'add'] + test.give_args
            dt_project_mock.res = test.give_res
            framework.table_test(test)

    def test_project_member_remove(self, dt_project_mock):
        @dataclass
        class TestCase:
            name: str
            give_args: List[str]
            want_n_rows: int
            want_n_cols: int
            want_row_type: Any
            want_error: Any

        tests = [
            TestCase(
                name='minimal',
                give_args=[
                    'member-id',
                    'project-id',
                ],
                want_n_cols=0,
                want_n_rows=0,
                want_row_type=None,
                want_error=None,
            ),
            TestCase(
                name='--full',
                give_args=[
                    'member-id',
                    'project-id',
                    '--full',
                ],
                want_n_cols=0,
                want_n_rows=0,
                want_row_type=None,
                want_error=None,
            ),
        ]

        for test in tests:
            sys.argv = ['main.py', 'project', 'member', 'remove'] \
                + test.give_args
            dt_project_mock.res = None
            framework.table_test(test)

    def test_project_member_get(self, dt_project_mock):
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
                give_args=[
                    'member-id',
                    'project-id',
                ],
                give_res=responses.member_pending_user,
                want_n_cols=5,
                want_n_rows=2,
                want_row_type=str,
                want_error=None,
            ),
            TestCase(
                name='--full',
                give_args=[
                    'member-id',
                    'project-id',
                    '--full',
                ],
                give_res=responses.member_pending_user,
                want_n_cols=7,
                want_n_rows=2,
                want_row_type=str,
                want_error=None,
            ),
        ]

        for test in tests:
            sys.argv = ['main.py', 'project', 'member', 'get'] + test.give_args
            dt_project_mock.res = test.give_res
            framework.table_test(test)

    def test_project_member_update(self, dt_project_mock):
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
                give_args=[
                    'member-id',
                    'project-id',
                    'role1,role2',
                ],
                give_res=responses.member_pending_user,
                want_n_cols=5,
                want_n_rows=2,
                want_row_type=str,
                want_error=None,
            ),
            TestCase(
                name='--full',
                give_args=[
                    'member-id',
                    'project-id',
                    'role1,role2',
                    '--full',
                ],
                give_res=responses.member_pending_user,
                want_n_cols=7,
                want_n_rows=2,
                want_row_type=str,
                want_error=None,
            ),
        ]

        for test in tests:
            sys.argv = ['main.py', 'project', 'member', 'update'] \
                + test.give_args
            dt_project_mock.res = test.give_res
            framework.table_test(test)

    def test_project_member_list(self, dt_project_mock):
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
                give_args=[
                    'project-id',
                ],
                give_res=responses.members,
                want_n_cols=5,
                want_n_rows=4,
                want_row_type=str,
                want_error=None,
            ),
            TestCase(
                name='--full',
                give_args=[
                    'project-id',
                    '--full',
                ],
                give_res=responses.members,
                want_n_cols=7,
                want_n_rows=4,
                want_row_type=str,
                want_error=None,
            ),
        ]

        for test in tests:
            sys.argv = ['main.py', 'project', 'member', 'list'] \
                + test.give_args
            dt_project_mock.res = test.give_res
            framework.table_test(test)

    def test_project_member_invite_url(self, dt_project_mock):
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
                give_args=[
                    'member-id',
                    'project-id',
                ],
                give_res='some-url',
                want_n_cols=0,
                want_n_rows=0,
                want_row_type=str,
                want_error=None,
            ),
            TestCase(
                name='--full',
                give_args=[
                    'member-id',
                    'project-id',
                    '--full',
                ],
                give_res='some-url',
                want_n_cols=0,
                want_n_rows=0,
                want_row_type=str,
                want_error=None,
            ),
        ]

        for test in tests:
            sys.argv = ['main.py', 'project', 'member', 'invite-url'] \
                + test.give_args
            dt_project_mock.res = test.give_res
            framework.table_test(test)
