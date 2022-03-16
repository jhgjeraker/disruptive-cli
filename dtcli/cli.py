import click

import dtcli


def add_options(options):
    def _add_options(func):
        for opt in reversed(options):
            func = opt(func)
        return func
    return _add_options


@click.group()
def cli_root():
    pass


# --------------------------------------------------
#                       GET
#
@cli_root.group()
def get():
    dtcli.auth()


# Common options for all get calls.
def get_options(f):
    f = click.option(
        '-o', '--output',
        type=click.Choice(
            ['wide', 'csv', 'tsv', 'json'],
            case_sensitive=False,
        ),
        default=None,
        multiple=True,
    )(f)
    f = click.option('-c', '--columns')(f)
    f = click.option('-x', '--exclude')(f)
    f = click.option('--header/--no-header', default=True)(f)
    return f


# GET DEVICE
# ----------
@get.command()
@get_options
@click.argument('device-id')
def device(**kwargs):
    dtcli.get.device(**kwargs)


# GET DEVICES
# -----------
@get.command()
@get_options
@click.argument('project-id')
@click.option('--query')
@click.option('--device-ids')
@click.option('--device-types')
@click.option('--label-filters')
@click.option('--order-by')
def devices(**kwargs):
    dtcli.get.devices(**kwargs)


# GET PROJECT
# -----------
@get.command()
@get_options
@click.argument('project-id')
def project(**kwargs):
    dtcli.get.project(**kwargs)


# GET PROJECTS
# ------------
@get.command()
@get_options
@click.option('--organization-id')
@click.option('--query')
def projects(**kwargs):
    dtcli.get.projects(**kwargs)


# GET HISTORY
# -----------
@get.command()
@get_options
@click.argument('device-id')
@click.argument('project-id')
@click.option('--event-types')
@click.option('--start-time')
@click.option('--end-time')
def history(**kwargs):
    dtcli.get.history(**kwargs)


# --------------------------------------------------
#                       STREAM
#
@cli_root.group()
def stream():
    dtcli.auth()


@stream.command()
@get_options
@click.argument('project-id')
@click.option('--device-ids')
@click.option('--label-filters')
@click.option('--device-types')
@click.option('--event-types')
def events(**kwargs):
    dtcli.stream.events(**kwargs)


# --------------------------------------------------
#                      CONFIG
#
@cli_root.group()
def config():
    pass


@config.command()
def default():
    dtcli.config.set_default()


@config.group()
def set():
    pass


@set.command()
@click.argument('spaces')
def padding(**kwargs):
    dtcli.config.set_padding(**kwargs)
