import dtcli


def add_command(subparser, common_opts):
    get_parser = subparser.add_parser(
        name='get',
        help='GET one- or more resources.',
        formatter_class=dtcli.format.SubcommandHelpFormatter,
    )

    get_subparser = get_parser.add_subparsers(
        title='available commands',
        dest='get',
        metavar=None,
    )

    # ----------
    # GET Device
    get_device_parser = get_subparser.add_parser(
        name='device',
        help='GET a single device.',
    )
    get_device_parser.add_argument('device-id')
    get_device_parser.add_argument('--project-id')
    common_opts(get_device_parser)

    # -----------
    # GET Devices
    get_devices_parser = get_subparser.add_parser(
        name='devices',
        help='GET multiple devices.',
    )
    get_devices_parser.add_argument('project-id')
    common_opts(get_devices_parser)

    # -----------
    # GET Project
    get_project_parser = get_subparser.add_parser(
        name='project',
        help='GET a single project.',
    )
    get_project_parser.add_argument('project-id')
    common_opts(get_project_parser)

    # ------------
    # GET Projects
    get_projects_parser = get_subparser.add_parser(
        'projects',
        help='GET multiple projects.',
    )
    get_projects_parser.add_argument('--organization-id')
    get_projects_parser.add_argument('--query')
    common_opts(get_projects_parser)

    return get_parser


def get_device(**kwargs):
    dtcli.resources.device.get_device(**kwargs)


def get_devices(**kwargs):
    dtcli.resources.device.get_devices(**kwargs)


def get_project(**kwargs):
    dtcli.resources.project.get_project(**kwargs)


def get_projects(**kwargs):
    dtcli.resources.project.get_projects(**kwargs)


def do(parser, **kwargs):
    if kwargs['get'] == 'device':
        get_device(**kwargs)
    elif kwargs['get'] == 'devices':
        get_devices(**kwargs)
    elif kwargs['get'] == 'project':
        get_project(**kwargs)
    elif kwargs['get'] == 'projects':
        get_projects(**kwargs)
    else:
        print(parser.format_help())
