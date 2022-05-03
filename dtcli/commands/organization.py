from typing import Callable, Any, Dict
from argparse import _SubParsersAction, ArgumentParser

import dtcli
from dtcli.table import Table


def member_add(subparser: _SubParsersAction,
               common_opts: Callable,
               ) -> ArgumentParser:

    member_parser = subparser.add_parser(
        name='member',
        help='interact with members in an organization',
        formatter_class=dtcli.format.SubcommandHelpFormatter,
    )
    member_subparser = member_parser.add_subparsers(
        title='available commands',
        dest='org_member',
        metavar=None,
    )

    # ----------
    # member add
    add_parser = member_subparser.add_parser(
        name='add',
        help='add a new member',
    )
    dtcli.args.organization.MEMBER_ADD.to_parser(add_parser)
    common_opts(add_parser)

    # -------------
    # member remove
    remove_parser = member_subparser.add_parser(
        name='remove',
        help='remove a member',
    )
    dtcli.args.organization.MEMBER_REMOVE.to_parser(remove_parser)
    common_opts(remove_parser)

    # ----------
    # member get
    get_parser = member_subparser.add_parser(
        name='get',
        help='get a member',
    )
    dtcli.args.organization.MEMBER_GET.to_parser(get_parser)
    common_opts(get_parser)

    # -----------
    # member list
    list_parser = member_subparser.add_parser(
        name='list',
        help='list members in organization',
    )
    dtcli.args.organization.MEMBER_LIST.to_parser(list_parser)
    common_opts(list_parser)

    # -----------------
    # member invite-url
    invite_url_parser = member_subparser.add_parser(
        name='invite-url',
        help='get member invite URL',
    )
    dtcli.args.organization.MEMBER_INVITE_URL.to_parser(invite_url_parser)
    common_opts(invite_url_parser)

    assert isinstance(member_parser, ArgumentParser)

    return member_parser


def add(subparser: _SubParsersAction,
        common_opts: Callable,
        ) -> Dict[str, ArgumentParser]:

    organization_parser = subparser.add_parser(
        name='organization',
        help='Interact with the Organization resource.',
        formatter_class=dtcli.format.SubcommandHelpFormatter,
    )
    organization_subparser = organization_parser.add_subparsers(
        title='available commands',
        dest='organization',
        metavar=None,
    )

    # ----------------
    # organization get
    get_parser = organization_subparser.add_parser(
        name='get',
        help='get a single organization',
    )
    dtcli.args.organization.GET.to_parser(get_parser)
    common_opts(get_parser)

    # ----------------
    # organization list
    list_parser = organization_subparser.add_parser(
        name='list',
        help='list all organizations',
    )
    dtcli.args.organization.LIST.to_parser(list_parser)
    common_opts(list_parser)

    # ------------------------
    # organization permissions
    permissions_parser = organization_subparser.add_parser(
        name='permissions',
        help='list organization permissions',
    )
    dtcli.args.organization.PERMISSIONS.to_parser(permissions_parser)
    common_opts(permissions_parser)

    # -------------------
    # organization member
    member_parser = member_add(
        organization_subparser,
        common_opts,
    )

    assert isinstance(member_parser, ArgumentParser)
    assert isinstance(organization_parser, ArgumentParser)

    return {'organization': organization_parser, 'org_member': member_parser}


def do(parsers: dict, cfg: dict, **kwargs: Any) -> Table:
    if kwargs['organization'] == 'get':
        return dtcli.resources.organization.org_get(cfg, **kwargs)
    elif kwargs['organization'] == 'list':
        return dtcli.resources.organization.org_list(cfg, **kwargs)
    elif kwargs['organization'] == 'permissions':
        return dtcli.resources.organization.org_permissions(cfg, **kwargs)
    elif kwargs['organization'] == 'member':
        if kwargs['org_member'] == 'add':
            return dtcli.resources.organization.member_add(cfg, **kwargs)
        elif kwargs['org_member'] == 'remove':
            return dtcli.resources.organization.member_remove(cfg, **kwargs)
        elif kwargs['org_member'] == 'get':
            return dtcli.resources.organization.member_get(cfg, **kwargs)
        elif kwargs['org_member'] == 'list':
            return dtcli.resources.organization.member_list(cfg, **kwargs)
        elif kwargs['org_member'] == 'invite-url':
            return dtcli.resources.organization.member_url(cfg, **kwargs)
        else:
            print(parsers['org_member'].format_help())
    else:
        print(parsers['organization'].format_help())

    return Table.empty()
