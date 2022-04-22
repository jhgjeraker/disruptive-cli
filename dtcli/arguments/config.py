import dtcli

PADDING = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='spaces',
        flags=['spaces'],
        help='number of spaces between columns',
        format=dtcli.format.to_string,
    )
])
