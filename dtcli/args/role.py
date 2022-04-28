import dtcli

GET = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='role',
        flags=['role'],
        help='target role name',
        format=dtcli.format.to_string,
    ),
])

LIST = dtcli.parser.CmdArgs([])
