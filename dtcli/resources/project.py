import disruptive as dt

import dtcli
from dtcli.table import Table, Column


def _projects(projects: list[dt.Project], cfg: dict, **kwargs: dict) -> Table:
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


def _members(members: list[dt.outputs.Member],
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
    return _projects(
        projects=dtcli.arguments.project.GET.call(
            method=dt.Project.get_project,
            **kwargs,
        ),
        cfg=cfg,
        **kwargs
    )


def project_list(cfg: dict, **kwargs: dict) -> Table:
    return _projects(
        projects=dtcli.arguments.project.LIST.call(
            method=dt.Project.list_projects,
            **kwargs,
        ),
        cfg=cfg,
        **kwargs,
    )


def project_create(cfg: dict, **kwargs: dict) -> Table:
    return _projects(
        projects=dtcli.arguments.project.CREATE.call(
            method=dt.Project.create_project,
            **kwargs,
        ),
        cfg=cfg,
        **kwargs,
    )


def project_update(**kwargs: dict) -> Table:
    dtcli.arguments.project.UPDATE.call(
        method=dt.Project.update_project,
        **kwargs,
    )
    return Table.empty()


def project_delete(**kwargs: dict) -> Table:
    dtcli.arguments.project.DELETE.call(
        method=dt.Project.delete_project,
        **kwargs,
    )
    return Table.empty()


def project_member_add(cfg: dict, **kwargs: dict) -> Table:
    return _members(
        members=dtcli.arguments.project.MEMBER_ADD.call(
            method=dt.Project.add_member,
            **kwargs,
        ),
        cfg=cfg,
        **kwargs,
    )


def project_member_remove(**kwargs: dict) -> Table:
    dtcli.arguments.project.MEMBER_REMOVE.call(
        method=dt.Project.remove_member,
        **kwargs,
    )
    return Table.empty()


def project_member_update(cfg: dict, **kwargs: dict) -> Table:
    return _members(
        members=dtcli.arguments.project.MEMBER_UPDATE.call(
            method=dt.Project.update_member,
            **kwargs,
        ),
        cfg=cfg,
        **kwargs,
    )


def project_member_list(cfg: dict, **kwargs: dict) -> Table:
    return _members(
        members=dtcli.arguments.project.MEMBER_LIST.call(
            method=dt.Project.list_members,
            **kwargs,
        ),
        cfg=cfg,
        **kwargs,
    )


def project_member_invite_url(**kwargs: dict) -> Table:
    urls = dtcli.arguments.project.MEMBER_INVITE_URL.call(
        method=dt.Project.get_member_invite_url,
        **kwargs,
    )

    for url in urls:
        dtcli.format.stdout(url)

    return Table.empty()


def project_permissions(**kwargs: dict) -> Table:
    permissions = dtcli.arguments.project.PERMISSIONS.call(
        method=dt.Project.list_permissions,
        **kwargs,
    )

    for permission in permissions:
        dtcli.format.stdout(permission)

    return Table.empty()
