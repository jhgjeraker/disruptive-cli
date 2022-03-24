import disruptive as dt

import dtcli.table


def _projects(projects: list[dt.Project], cfg: dict, **kwargs):
    table = dtcli.table.Table(
        default_columns=[
            dtcli.table.Column('id', False),
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


def project_get(cfg: dict, **kwargs):
    _projects([dt.Project.get_project(kwargs['project_id'])], cfg, **kwargs)


def project_list(cfg: dict, **kwargs):
    _projects(dt.Project.list_projects(
        organization_id=kwargs['organization_id'],
        query=kwargs['query'],
    ), cfg, **kwargs)
