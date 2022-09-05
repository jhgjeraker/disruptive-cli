from typing import Callable, Any, Dict
from argparse import _SubParsersAction, ArgumentParser

import dtcli
from dtcli.table import Table


def add(subparser: _SubParsersAction,
        common_opts: Callable,
        ) -> Dict[str, ArgumentParser]:

    claim_parser = subparser.add_parser(
        name='claim',
        help='Interact with the Claim resource.',
        formatter_class=dtcli.format.SubcommandHelpFormatter,
    )
    claim_subparser = claim_parser.add_subparsers(
        title='available commands',
        dest='claim',
        metavar=None,
    )

    # -----------
    # claim claim
    claim_item_parser = claim_subparser.add_parser(
        name='claim',
        help='Claim kits and devices.',
    )
    dtcli.args.claim.CLAIM.to_parser(claim_item_parser)
    common_opts(claim_item_parser)

    # ----------
    # claim info
    claim_info_parser = claim_subparser.add_parser(
        name='info',
        help='Get claim info about a kit or device.',
    )
    dtcli.args.claim.INFO.to_parser(claim_info_parser)
    common_opts(claim_info_parser)

    assert isinstance(claim_parser, ArgumentParser)

    return {'claim': claim_parser}


def do(parsers: dict, cfg: dict, **kwargs: Any) -> Table:
    if kwargs['claim'] == 'claim':
        return dtcli.resources.claim.claim_item(cfg, **kwargs)
    elif kwargs['claim'] == 'info':
        return dtcli.resources.claim.claim_info(cfg, **kwargs)
    else:
        print(parsers['claim'].format_help())

    return Table.empty()
