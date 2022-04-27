import dtcli

GET = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='organization_id',
        flags=['organization-id'],
        help='target organization identifier',
        format=dtcli.format.to_string,
    ),
])
