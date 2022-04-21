import disruptive as dt

import dtcli


def _projects(projects: list[dt.Project], cfg: dict, **kwargs):
    table = dtcli.table.Table(
        default_columns=[
            dtcli.table.Column('project_id', False),
            dtcli.table.Column('display_name', False),
            dtcli.table.Column('organization_id', True),
            dtcli.table.Column('organization_display_name', True),
            dtcli.table.Column('sensor_count', False),
            dtcli.table.Column('cloud_connector_count', False),
        ],
        cfg=cfg,
        opts=kwargs,
    )
    table.expand_rows(projects)
    table.new_entries(projects)

    return table


def _members(members: list[dt.outputs.Member], cfg: dict, **kwargs):
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


def project_get(cfg: dict, **kwargs):
    return _projects(
        projects=dtcli.commands.project.GET_ARGS.call(
            method=dt.Project.get_project,
            **kwargs,
        ),
        cfg=cfg,
        **kwargs
    )


def project_list(cfg: dict, **kwargs):
    return _projects(
        projects=dtcli.commands.project.LIST_ARGS.call(
            method=dt.Project.list_projects,
            **kwargs,
        ),
        cfg=cfg,
        **kwargs,
    )


def project_create(cfg: dict, **kwargs):
    return _projects(
        projects=dtcli.commands.project.CREATE_ARGS.call(
            method=dt.Project.create_project,
            **kwargs,
        ),
        cfg=cfg,
        **kwargs,
    )


def project_update(**kwargs):
    dtcli.commands.project.UPDATE_ARGS.call(
        method=dt.Project.update_project,
        **kwargs,
    )


def project_delete(**kwargs):
    dtcli.commands.project.DELETE_ARGS.call(
        method=dt.Project.delete_project,
        **kwargs,
    )


def project_member_add(cfg: dict, **kwargs):
    return _members(
        members=dtcli.commands.project_member.ADD_ARGS.call(
            method=dt.Project.add_member,
            **kwargs,
        ),
        cfg=cfg,
        **kwargs,
    )


def project_member_remove(**kwargs):
    dtcli.commands.project_member.REMOVE_ARGS.call(
        method=dt.Project.remove_member,
        **kwargs,
    )


def project_member_update(cfg: dict, **kwargs):
    return _members(
        members=dtcli.commands.project_member.UPDATE_ARGS.call(
            method=dt.Project.update_member,
            **kwargs,
        ),
        cfg=cfg,
        **kwargs,
    )


def project_member_list(cfg: dict, **kwargs):
    return _members(
        members=dtcli.commands.project_member.LIST_ARGS.call(
            method=dt.Project.list_members,
            **kwargs,
        ),
        cfg=cfg,
        **kwargs,
    )


def project_member_invite_url(**kwargs):
    urls = dtcli.commands.project_member.INVITE_URL_ARGS.call(
        method=dt.Project.get_member_invite_url,
        **kwargs,
    )

    for url in urls:
        dtcli.format.stdout(url)


def project_permissions(**kwargs):
    permissions = dtcli.commands.project.PERMISSIONS_ARGS.call(
        method=dt.Project.list_permissions,
        **kwargs,
    )

    for permission in permissions:
        dtcli.format.stdout(permission)
