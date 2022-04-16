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
    print(kwargs)
    # project = dt.Project.create_project(
    #     organization_id=kwargs['organization_id']
    # )
