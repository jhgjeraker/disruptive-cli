import dtcli


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
    get_parser.add_argument(
        'project-id',
        metavar='',
    )
    common_opts(get_parser)

    # -------------
    # Projects List
    list_parser = project_subparser.add_parser(
        'list',
        help='List multiple projects.',
    )
    list_parser.add_argument(
        '--organization-id',
        metavar='',
    )
    list_parser.add_argument(
        '--query',
        metavar='',
    )
    common_opts(list_parser)

    return {'project': project_parser}


def do(parser, cfg, **kwargs):
    if kwargs['project'] == 'get':
        dtcli.resources.project.project_get(cfg, **kwargs)
    elif kwargs['project'] == 'list':
        dtcli.resources.project.project_list(cfg, **kwargs)
    else:
        print(parser['project'].format_help())
