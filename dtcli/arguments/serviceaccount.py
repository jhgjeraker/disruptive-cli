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
