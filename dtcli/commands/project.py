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
        help='GET a single project.',
    )
    GET_ARGS.to_parser(get_parser)
    common_opts(get_parser)

    # -------------
    # Projects List
    list_parser = project_subparser.add_parser(
        'list',
        help='List multiple projects.',
        formatter_class=dtcli.format.SubcommandHelpFormatter,
    )
    LIST_ARGS.to_parser(list_parser)
    common_opts(list_parser)

    # --------------
    # project create
    create_parser = project_subparser.add_parser(
        'create',
        help='Create a new project.',
    )
    create_parser.add_argument(
        'organization-id',
        help='identifier of owning organization',
    )
    common_opts(create_parser)

    return {'project': project_parser}


def do(parser, cfg, **kwargs):
    if kwargs['project'] == 'get':
        return dtcli.resources.project.project_get(cfg, **kwargs)
    elif kwargs['project'] == 'list':
        return dtcli.resources.project.project_list(cfg, **kwargs)
    elif kwargs['project'] == 'create':
        return dtcli.resources.project.project_create(cfg, **kwargs)
    else:
        print(parser['project'].format_help())
