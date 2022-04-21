import dtcli


GET_ARGS = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        help='project identifier',
        format=dtcli.format.to_string,
    )
])

LIST_ARGS = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='organization_id',
        flags=['--organization-id'],
        metavar='',
        help='identifier of owning organization',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='query',
        flags=['--query'],
        metavar='',
        format=dtcli.format.to_string,
    )
])

CREATE_ARGS = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='organization_id',
        flags=['organization-id'],
        help='identifier of owning organization',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='display_name',
        flags=['display-name'],
        help='project name',
        format=dtcli.format.to_string,
    )
])

UPDATE_ARGS = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        help='target project identifier',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='display_name',
        flags=['--display-name'],
        help='new project name',
        format=dtcli.format.to_string,
    )
])

DELETE_ARGS = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        help='target project identifier',
        format=dtcli.format.to_string,
    ),
])

PERMISSIONS_ARGS = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        help='target project identifier',
        format=dtcli.format.to_string,
    ),
])


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
    # Project Get
    get_parser = project_subparser.add_parser(
        name='get',
        help='get a single project',
    )
    GET_ARGS.to_parser(get_parser)
    common_opts(get_parser)

    # -------------
    # Projects List
    list_parser = project_subparser.add_parser(
        'list',
        help='list multiple projects',
        formatter_class=dtcli.format.SubcommandHelpFormatter,
    )
    LIST_ARGS.to_parser(list_parser)
    common_opts(list_parser)

    # --------------
    # project create
    create_parser = project_subparser.add_parser(
        'create',
        help='create a new project',
    )
    CREATE_ARGS.to_parser(create_parser)
    common_opts(create_parser)

    # --------------
    # project update
    update_parser = project_subparser.add_parser(
        'update',
        help='update a project',
    )
    UPDATE_ARGS.to_parser(update_parser)
    common_opts(update_parser)

    # --------------
    # project delete
    delete_parser = project_subparser.add_parser(
        'delete',
        help='delete a project',
    )
    DELETE_ARGS.to_parser(delete_parser)
    common_opts(delete_parser)

    # ------------------
    # project permissions
    permissions_parser = project_subparser.add_parser(
        name='permissions',
        help='list permissions available to caller',
    )
    PERMISSIONS_ARGS.to_parser(permissions_parser)
    common_opts(permissions_parser)

    # --------------
    # project member
    member_parser = dtcli.commands.project_member.add_command(
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
        return dtcli.commands.project_member.do(parsers, cfg, **kwargs)
    else:
        print(parsers['project'].format_help())
