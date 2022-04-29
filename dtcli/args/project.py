import dtcli


GET = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        help='project identifier',
        format=dtcli.format.to_string,
    )
])

LIST = dtcli.parser.CmdArgs([
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

CREATE = dtcli.parser.CmdArgs([
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

UPDATE = dtcli.parser.CmdArgs([
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

DELETE = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        help='target project identifier',
        format=dtcli.format.to_string,
    ),
])

PERMISSIONS = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        help='target project identifier',
        format=dtcli.format.to_string,
    ),
])

MEMBER_ADD = dtcli.parser.CmdArgs([
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

MEMBER_REMOVE = dtcli.parser.CmdArgs([
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

MEMBER_GET = dtcli.parser.CmdArgs([
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

MEMBER_UPDATE = dtcli.parser.CmdArgs([
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

MEMBER_LIST = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        help='target project identifier',
        format=dtcli.format.to_string,
    ),
])

MEMBER_INVITE_URL = dtcli.parser.CmdArgs([
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
