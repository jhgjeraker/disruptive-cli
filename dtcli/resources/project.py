import disruptive

import dtcli.table


def _projects(projects: list[disruptive.Project], **kwargs):
    table = dtcli.table.Table(
        default_columns=[
            dtcli.table.Column('id', False),
            dtcli.table.Column('display_name', True),
            dtcli.table.Column('organization_id', False),
            dtcli.table.Column('organization_display_name', True),
            dtcli.table.Column('sensor_count', False),
            dtcli.table.Column('cloud_connector_count', False),
        ],
        opts=kwargs,
    )
    table.expand_rows(projects)
    table.new_entries(projects)


def get_project(**kwargs):
    _projects([disruptive.Project.get_project(kwargs['project_id'])], **kwargs)


def get_projects(**kwargs):
    _projects(disruptive.Project.list_projects(
        organization_id=kwargs['organization_id'],
        query=kwargs['query'],
    ), **kwargs)
