import dtcli


ADD_ARGS = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        help='target project identifier',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='email',
        flags=['email'],
        help='member email address',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='roles',
        flags=['roles'],
        help='comma-separated list of roles',
        format=dtcli.format.str2list,
    )
])

REMOVE_ARGS = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='member_id',
        flags=['member-id'],
        help='target member identifier',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        help='target project identifier',
        format=dtcli.format.to_string,
    )
])

UPDATE_ARGS = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='member_id',
        flags=['member-id'],
        help='target member identifier',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        help='target project identifier',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='roles',
        flags=['roles'],
        help='comma-separated list of roles',
        format=dtcli.format.str2list,
    )
])

LIST_ARGS = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        help='target project identifier',
        format=dtcli.format.to_string,
    ),
])

INVITE_URL_ARGS = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='member_id',
        flags=['member-id'],
        help='target member identifier',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        help='target project identifier',
        format=dtcli.format.to_string,
    ),
])


def add_command(subparser, common_opts):
    member_parser = subparser.add_parser(
        name='member',
        help='interact with members in a project',
        formatter_class=dtcli.format.SubcommandHelpFormatter,
    )
    member_subparser = member_parser.add_subparsers(
        title='available commands',
        dest='member',
        metavar=None,
    )

    # ----------
    # member add
    add_parser = member_subparser.add_parser(
        name='add',
        help='add a new member',
    )
    ADD_ARGS.to_parser(add_parser)
    common_opts(add_parser)

    # -------------
    # member remove
    remove_parser = member_subparser.add_parser(
        name='remove',
        help='remove a member',
    )
    REMOVE_ARGS.to_parser(remove_parser)
    common_opts(remove_parser)

    # -------------
    # member update
    update_parser = member_subparser.add_parser(
        name='update',
        help='update member details',
    )
    UPDATE_ARGS.to_parser(update_parser)
    common_opts(update_parser)

    # -----------
    # member list
    list_parser = member_subparser.add_parser(
        name='list',
        help='list members in project',
    )
    LIST_ARGS.to_parser(list_parser)
    common_opts(list_parser)

    # -----------------
    # member invite-url
    invite_url_parser = member_subparser.add_parser(
        name='invite-url',
        help='get member invite URL',
    )
    INVITE_URL_ARGS.to_parser(invite_url_parser)
    common_opts(invite_url_parser)

    return member_parser


def do(parsers: dict, cfg: dict, **kwargs):
    if kwargs['member'] == 'add':
        return dtcli.resources.project.project_member_add(cfg, **kwargs)
    if kwargs['member'] == 'remove':
        return dtcli.resources.project.project_member_remove(**kwargs)
    if kwargs['member'] == 'update':
        return dtcli.resources.project.project_member_update(cfg, **kwargs)
    if kwargs['member'] == 'list':
        return dtcli.resources.project.project_member_list(cfg, **kwargs)
    if kwargs['member'] == 'invite-url':
        return dtcli.resources.project.project_member_invite_url(**kwargs)
    else:
        print(parsers['member'].format_help())
