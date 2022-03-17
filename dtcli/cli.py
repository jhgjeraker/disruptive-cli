import click
from click_option_group import optgroup

import dtcli.auth
import dtcli.output

import dtcli.resources.project
import dtcli.resources.device
import dtcli.resources.history


GLOBAL_OPTS = [
    optgroup.group('\n  Filters'),
    optgroup.option('--no-header', is_flag=True),
    optgroup.option('--full', is_flag=True),
    optgroup.option('-x', '--exclude', help='Excludes one- or more columns.'),
    optgroup.group('\n  Formatting'),
    optgroup.option('--csv', is_flag=True),
    optgroup.option('--tsv', is_flag=True),
    optgroup.option('--json', is_flag=True, help='Output JSON format.'),
]


def add_options(options):
    def _add_options(func):
        for opt in reversed(options):
            func = opt(func)
        return func
    return _add_options


@click.group()
def entry_point():
    pass


# --------------------------------------------------
#                       GET
#
GET_GROUP_OPTS = [] + GLOBAL_OPTS


@entry_point.group()
def get():
    dtcli.auth.auth()


# GET DEVICE
# ----------
@get.command()
@click.argument('device-id')
@add_options(GET_GROUP_OPTS)
def device(**kwargs):
    dtcli.get.device(**kwargs)


# GET DEVICES
# -----------
@get.command()
@click.argument('project-id')
@click.option('--query')
@click.option('--device-ids')
@click.option('--device-types')
@click.option('--label-filters')
@click.option('--order-by')
@add_options(GET_GROUP_OPTS)
def devices(**kwargs):
    dtcli.get.devices(**kwargs)


# GET PROJECT
# -----------
@get.command()
@click.argument('project-id')
@add_options(GET_GROUP_OPTS)
def project(**kwargs):
    dtcli.resources.project.get_project(**kwargs)


# GET PROJECTS
# ------------
@get.command()
@optgroup.group('Parameters')
@optgroup.option('--organization-id', help='Organization ID')
@optgroup.option('--query')
@add_options(GET_GROUP_OPTS)
def projects(**kwargs):
    """
    Docstrings work here too!

    """
    dtcli.resources.project.get_projects(**kwargs)


# GET HISTORY
# -----------
@get.command()
@click.argument('device-id')
@click.argument('project-id')
@click.option('--event-types')
@click.option('--start-time')
@click.option('--end-time')
@add_options(GET_GROUP_OPTS)
def history(**kwargs):
    dtcli.get.history(**kwargs)


# --------------------------------------------------
#                       STREAM
#
STREAM_GROUP_OPTS = [] + GLOBAL_OPTS


@entry_point.group()
def stream():
    dtcli.auth()


@stream.command()
@click.argument('project-id')
@click.option('--device-ids')
@click.option('--label-filters')
@click.option('--device-types')
@click.option('--event-types')
@add_options(STREAM_GROUP_OPTS)
def events(**kwargs):
    dtcli.stream.events(**kwargs)


# --------------------------------------------------
#                      CONFIG
#
CONFIG_GROUP_OPTS = [] + GLOBAL_OPTS


@entry_point.group()
def config():
    pass


@config.command()
@add_options(CONFIG_GROUP_OPTS)
def default():
    dtcli.config.set_default()


@config.group()
@add_options(CONFIG_GROUP_OPTS)
def set():
    pass


@set.command()
@click.argument('spaces')
@add_options(CONFIG_GROUP_OPTS)
def padding(**kwargs):
    dtcli.config.set_padding(**kwargs)
