import dtcli

GET = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='service_account_id',
        flags=['service-account-id'],
        help='target service account identifier',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        help='target project identifier',
        format=dtcli.format.to_string,
    ),
])

LIST = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        help='target project identifier',
        format=dtcli.format.to_string,
    ),
])

CREATE = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        help='target project identifier',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='display_name',
        flags=['--display-name'],
        help='give the service account a name',
        metavar='',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='basic_auth_enabled',
        flags=['--basic-auth'],
        help='enables basic auth',
        metavar='',
        format=dtcli.format.to_bool,
    ),
])

UPDATE = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='service_account_id',
        flags=['service-account-id'],
        help='target service account identifier',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        help='target project identifier',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='display_name',
        flags=['--display-name'],
        help='new service account name',
        metavar='',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='basic_auth_enabled',
        flags=['--basic-auth'],
        help='enable (1) or disable (0) basic auth',
        format=dtcli.format.to_bool,
    ),
])

DELETE = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='service_account_id',
        flags=['service-account-id'],
        help='target service account identifier',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        help='target project identifier',
        format=dtcli.format.to_string,
    ),
])

KEY_GET = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='key_id',
        flags=['key-id'],
        help='target service account key identifier',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='service_account_id',
        flags=['service-account-id'],
        help='target service account identifier',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        help='target project identifier',
        format=dtcli.format.to_string,
    ),
])

KEY_LIST = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='service_account_id',
        flags=['service-account-id'],
        help='target service account identifier',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        help='target project identifier',
        format=dtcli.format.to_string,
    ),
])

KEY_CREATE = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='service_account_id',
        flags=['service-account-id'],
        help='target service account identifier',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        help='target project identifier',
        format=dtcli.format.to_string,
    ),
])

KEY_DELETE = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='key_id',
        flags=['key-id'],
        help='target service account key identifier',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='service_account_id',
        flags=['service-account-id'],
        help='target service account identifier',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        help='target project identifier',
        format=dtcli.format.to_string,
    ),
])
