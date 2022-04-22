import dtcli


def member_add(subparser, common_opts):
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
    dtcli.arguments.project.MEMBER_ADD.to_parser(add_parser)
    common_opts(add_parser)

    # -------------
    # member remove
    remove_parser = member_subparser.add_parser(
        name='remove',
        help='remove a member',
    )
    dtcli.arguments.project.MEMBER_REMOVE.to_parser(remove_parser)
    common_opts(remove_parser)

    # -------------
    # member update
    update_parser = member_subparser.add_parser(
        name='update',
        help='update member details',
    )
    dtcli.arguments.project.MEMBER_UPDATE.to_parser(update_parser)
    common_opts(update_parser)

    # -----------
    # member list
    list_parser = member_subparser.add_parser(
        name='list',
        help='list members in project',
    )
    dtcli.arguments.project.MEMBER_LIST.to_parser(list_parser)
    common_opts(list_parser)

    # -----------------
    # member invite-url
    invite_url_parser = member_subparser.add_parser(
        name='invite-url',
        help='get member invite URL',
    )
    dtcli.arguments.project.MEMBER_INVITE_URL.to_parser(invite_url_parser)
    common_opts(invite_url_parser)

    return member_parser


def add(subparser, common_opts):
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
    dtcli.arguments.project.GET.to_parser(get_parser)
    common_opts(get_parser)

    # -------------
    # projects list
    list_parser = project_subparser.add_parser(
        'list',
        help='list multiple projects',
        formatter_class=dtcli.format.SubcommandHelpFormatter,
    )
    dtcli.arguments.project.LIST.to_parser(list_parser)
    common_opts(list_parser)

    # --------------
    # project create
    create_parser = project_subparser.add_parser(
        'create',
        help='create a new project',
    )
    dtcli.arguments.project.CREATE.to_parser(create_parser)
    common_opts(create_parser)

    # --------------
    # project update
    update_parser = project_subparser.add_parser(
        'update',
        help='update a project',
    )
    dtcli.arguments.project.UPDATE.to_parser(update_parser)
    common_opts(update_parser)

    # --------------
    # project delete
    delete_parser = project_subparser.add_parser(
        'delete',
        help='delete a project',
    )
    dtcli.arguments.project.DELETE.to_parser(delete_parser)
    common_opts(delete_parser)

    # ------------------
    # project permissions
    permissions_parser = project_subparser.add_parser(
        name='permissions',
        help='list permissions available to caller',
    )
    dtcli.arguments.project.PERMISSIONS.to_parser(permissions_parser)
    common_opts(permissions_parser)

    # --------------
    # project member
    member_parser = member_add(
        project_subparser,
        common_opts,
    )

    return {'project': project_parser, 'member': member_parser}


def do(parsers, cfg, **kwargs):
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
    else:
        print(parsers['project'].format_help())
