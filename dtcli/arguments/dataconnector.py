import dtcli

GET = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='data_connector_id',
        flags=['dataconnector-id'],
        help='target data connector id',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        help='target project id',
        format=dtcli.format.to_string,
    )
])

LIST = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        help='target project id',
        format=dtcli.format.to_string,
    )
])
