from typing import Callable, Dict
from argparse import _SubParsersAction, ArgumentParser

import dtcli
from dtcli.table import Table


def add(subparser: _SubParsersAction,
        common_opts: Callable,
        ) -> Dict[str, ArgumentParser]:

    event_parser = subparser.add_parser(
        name='event',
        help='Fetch events for one- or more devices.',
        formatter_class=dtcli.format.SubcommandHelpFormatter,
    )

    event_subparser = event_parser.add_subparsers(
        title='available commands',
        dest='event',
        metavar=None,
    )

    # -----------
    # List Events
    list_parser = event_subparser.add_parser(
        name='list',
        help='List events from one- or more devices.',
    )
    dtcli.args.event.LIST.to_parser(list_parser)
    common_opts(list_parser)

    # -------------
    # Stream Events
    stream_parser = event_subparser.add_parser(
        name='stream',
        help='Stream events from one- or more devices.',
    )
    dtcli.args.event.STREAM.to_parser(stream_parser)
    common_opts(stream_parser)

    assert isinstance(event_parser, ArgumentParser)
    return {'event': event_parser}


def do(parsers: Dict[str, ArgumentParser], cfg: dict, **kwargs: dict) -> Table:
    if kwargs['event'] == 'list':
        return dtcli.resources.event.list_events(cfg, **kwargs)
    elif kwargs['event'] == 'stream':
        return dtcli.resources.event.stream_events(cfg, **kwargs)
    else:
        print(parsers['event'].format_help())
        return Table.empty()
