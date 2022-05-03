from typing import Callable, Dict
from argparse import _SubParsersAction, ArgumentParser

import dtcli
from dtcli.table import Table


def member_add(subparser: _SubParsersAction,
               common_opts: Callable,
               ) -> ArgumentParser:

    member_parser = subparser.add_parser(
        name='member',
        help='interact with members in a project',
        formatter_class=dtcli.format.SubcommandHelpFormatter,
    )
    member_subparser = member_parser.add_subparsers(
        title='available commands',
        dest='project_member',
        metavar=None,
    )

    # ----------
    # member add
    add_parser = member_subparser.add_parser(
        name='add',
        help='add a new member',
    )
    dtcli.args.project.MEMBER_ADD.to_parser(add_parser)
    common_opts(add_parser)

    # -------------
    # member remove
    remove_parser = member_subparser.add_parser(
        name='remove',
        help='remove a member',
    )
    dtcli.args.project.MEMBER_REMOVE.to_parser(remove_parser)
    common_opts(remove_parser)

    # ----------
    # member get
    get_parser = member_subparser.add_parser(
        name='get',
        help='get a member',
    )
    dtcli.args.project.MEMBER_GET.to_parser(get_parser)
    common_opts(get_parser)

    # -------------
    # member update
    update_parser = member_subparser.add_parser(
        name='update',
        help='update member details',
    )
    dtcli.args.project.MEMBER_UPDATE.to_parser(update_parser)
    common_opts(update_parser)

    # -----------
    # member list
    list_parser = member_subparser.add_parser(
        name='list',
        help='list members in project',
    )
    dtcli.args.project.MEMBER_LIST.to_parser(list_parser)
    common_opts(list_parser)

    # -----------------
    # member invite-url
    invite_url_parser = member_subparser.add_parser(
        name='invite-url',
        help='get member invite URL',
    )
    dtcli.args.project.MEMBER_INVITE_URL.to_parser(invite_url_parser)
    common_opts(invite_url_parser)

    assert isinstance(member_parser, ArgumentParser)

    return member_parser


def add(subparser: _SubParsersAction,
        common_opts: Callable,
        ) -> Dict[str, ArgumentParser]:

    project_parser = subparser.add_parser(
        name='project',
        help='Interact with the Project resource.',
        formatter_class=dtcli.format.SubcommandHelpFormatter,
    )
    project_subparser = project_parser.add_subparsers(
        title='available commands',
        dest='project',
        metavar=None,
    )

    # -----------
    # project get
    get_parser = project_subparser.add_parser(
        name='get',
        help='get a single project',
    )
    dtcli.args.project.GET.to_parser(get_parser)
    common_opts(get_parser)

    # -------------
    # projects list
    list_parser = project_subparser.add_parser(
        'list',
        help='list multiple projects',
        formatter_class=dtcli.format.SubcommandHelpFormatter,
    )
    dtcli.args.project.LIST.to_parser(list_parser)
    common_opts(list_parser)

    # --------------
    # project create
    create_parser = project_subparser.add_parser(
        'create',
        help='create a new project',
    )
    dtcli.args.project.CREATE.to_parser(create_parser)
    common_opts(create_parser)

    # --------------
    # project update
    update_parser = project_subparser.add_parser(
        'update',
        help='update a project',
    )
    dtcli.args.project.UPDATE.to_parser(update_parser)
    common_opts(update_parser)

    # --------------
    # project delete
    delete_parser = project_subparser.add_parser(
        'delete',
        help='delete a project',
    )
    dtcli.args.project.DELETE.to_parser(delete_parser)
    common_opts(delete_parser)

    # ------------------
    # project permissions
    permissions_parser = project_subparser.add_parser(
        name='permissions',
        help='list permissions available to caller',
    )
    dtcli.args.project.PERMISSIONS.to_parser(permissions_parser)
    common_opts(permissions_parser)

    # --------------
    # project member
    member_parser = member_add(
        project_subparser,
        common_opts,
    )

    assert isinstance(project_parser, ArgumentParser)
    assert isinstance(member_parser, ArgumentParser)

    return {'project': project_parser, 'project_member': member_parser}


def do(parsers: Dict[str, ArgumentParser], cfg: dict, **kwargs: dict) -> Table:
    if kwargs['project'] == 'get':
        return dtcli.resources.project.project_get(cfg, **kwargs)
    elif kwargs['project'] == 'list':
        return dtcli.resources.project.project_list(cfg, **kwargs)
    elif kwargs['project'] == 'create':
        return dtcli.resources.project.project_create(cfg, **kwargs)
    elif kwargs['project'] == 'update':
        return dtcli.resources.project.project_update(**kwargs)
    elif kwargs['project'] == 'delete':
        return dtcli.resources.project.project_delete(**kwargs)
    elif kwargs['project'] == 'permissions':
        return dtcli.resources.project.project_permissions(**kwargs)
    elif kwargs['project'] == 'member':
        if kwargs['project_member'] == 'add':
            return dtcli.resources.project.project_member_add(cfg, **kwargs)
        elif kwargs['project_member'] == 'remove':
            return dtcli.resources.project.project_member_remove(**kwargs)
        elif kwargs['project_member'] == 'get':
            return dtcli.resources.project.project_member_get(cfg, **kwargs)
        elif kwargs['project_member'] == 'update':
            return dtcli.resources.project.project_member_update(cfg, **kwargs)
        elif kwargs['project_member'] == 'list':
            return dtcli.resources.project.project_member_list(cfg, **kwargs)
        elif kwargs['project_member'] == 'invite-url':
            return dtcli.resources.project.project_member_invite_url(**kwargs)
        else:
            print(parsers['project_member'].format_help())
            return Table.empty()
    else:
        print(parsers['project'].format_help())
        return Table.empty()
