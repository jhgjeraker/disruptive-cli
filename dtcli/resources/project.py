from typing import List

import disruptive as dt

import dtcli
from dtcli.table import Table, Column


def _projects(projects: List[dt.Project], cfg: dict, **kwargs: dict) -> Table:
    table = Table(
        default_columns=[
            Column('project_id', False),
            Column('display_name', False),
            Column('organization_id', True),
            Column('organization_display_name', True),
            Column('sensor_count', False),
            Column('cloud_connector_count', False),
        ],
        cfg=cfg,
        opts=kwargs,
    )
    table.expand_rows(projects)
    table.new_entries(projects)

    return table


def _members(members: List[dt.outputs.Member],
             cfg: dict,
             **kwargs: dict,
             ) -> Table:

    table = dtcli.table.Table(
        default_columns=[
            dtcli.table.Column('member_id', False),
            dtcli.table.Column('display_name', False),
            dtcli.table.Column('status', False),
            dtcli.table.Column('roles', False),
            dtcli.table.Column('account_type', False),
            dtcli.table.Column('email', True),
            dtcli.table.Column('create_time', True),
        ],
        cfg=cfg,
        opts=kwargs,
    )

    table.expand_rows(members)
    table.new_entries(members)

    return table


def project_get(cfg: dict, **kwargs: dict) -> Table:
    ok, args = dtcli.args.project.GET.reparse(**kwargs)
    if not ok:
        return Table.empty()

    return _projects(
        projects=dtcli.args.project.GET.call(
            method=dt.Project.get_project,
            method_args=args,
        ),
        cfg=cfg,
        **kwargs
    )


def project_list(cfg: dict, **kwargs: dict) -> Table:
    ok, args = dtcli.args.project.LIST.reparse(**kwargs)
    if not ok:
        return Table.empty()

    return _projects(
        projects=dtcli.args.project.LIST.call(
            method=dt.Project.list_projects,
            method_args=args,
        ),
        cfg=cfg,
        **kwargs,
    )


def project_create(cfg: dict, **kwargs: dict) -> Table:
    ok, args = dtcli.args.project.CREATE.reparse(**kwargs)
    if not ok:
        return Table.empty()

    return _projects(
        projects=dtcli.args.project.CREATE.call(
            method=dt.Project.create_project,
            method_args=args,
        ),
        cfg=cfg,
        **kwargs,
    )


def project_update(**kwargs: dict) -> Table:
    ok, args = dtcli.args.project.UPDATE.reparse(**kwargs)
    if not ok:
        return Table.empty()

    dtcli.args.project.UPDATE.call(
        method=dt.Project.update_project,
        method_args=args,
    )
    return Table.empty()


def project_delete(**kwargs: dict) -> Table:
    ok, args = dtcli.args.project.DELETE.reparse(**kwargs)
    if not ok:
        return Table.empty()

    dtcli.args.project.DELETE.call(
        method=dt.Project.delete_project,
        method_args=args,
    )
    return Table.empty()


def project_member_add(cfg: dict, **kwargs: dict) -> Table:
    ok, args = dtcli.args.project.MEMBER_ADD.reparse(**kwargs)
    if not ok:
        return Table.empty()

    return _members(
        members=dtcli.args.project.MEMBER_ADD.call(
            method=dt.Project.add_member,
            method_args=args,
        ),
        cfg=cfg,
        **kwargs,
    )


def project_member_remove(**kwargs: dict) -> Table:
    ok, args = dtcli.args.project.MEMBER_REMOVE.reparse(**kwargs)
    if not ok:
        return Table.empty()

    dtcli.args.project.MEMBER_REMOVE.call(
        method=dt.Project.remove_member,
        method_args=args,
    )
    return Table.empty()


def project_member_get(cfg: dict, **kwargs: dict) -> Table:
    ok, args = dtcli.args.project.MEMBER_GET.reparse(**kwargs)
    if not ok:
        return Table.empty()

    return _members(
        members=dtcli.args.project.MEMBER_GET.call(
            method=dt.Project.get_member,
            method_args=args,
        ),
        cfg=cfg,
        **kwargs,
    )


def project_member_update(cfg: dict, **kwargs: dict) -> Table:
    ok, args = dtcli.args.project.MEMBER_UPDATE.reparse(**kwargs)
    if not ok:
        return Table.empty()

    return _members(
        members=dtcli.args.project.MEMBER_UPDATE.call(
            method=dt.Project.update_member,
            method_args=args,
        ),
        cfg=cfg,
        **kwargs,
    )


def project_member_list(cfg: dict, **kwargs: dict) -> Table:
    ok, args = dtcli.args.project.MEMBER_LIST.reparse(**kwargs)
    if not ok:
        return Table.empty()

    return _members(
        members=dtcli.args.project.MEMBER_LIST.call(
            method=dt.Project.list_members,
            method_args=args,
        ),
        cfg=cfg,
        **kwargs,
    )


def project_member_invite_url(**kwargs: dict) -> Table:
    ok, args = dtcli.args.project.MEMBER_INVITE_URL.reparse(**kwargs)
    if not ok:
        return Table.empty()

    urls = dtcli.args.project.MEMBER_INVITE_URL.call(
        method=dt.Project.get_member_invite_url,
        method_args=args,
    )

    for url in urls:
        dtcli.format.stdout(url)

    return Table.empty()


def project_permissions(**kwargs: dict) -> Table:
    ok, args = dtcli.args.project.PERMISSIONS.reparse(**kwargs)
    if not ok:
        return Table.empty()

    permissions = dtcli.args.project.PERMISSIONS.call(
        method=dt.Project.list_permissions,
        method_args=args,
    )

    for permission in permissions:
        dtcli.format.stdout(permission)

    return Table.empty()
