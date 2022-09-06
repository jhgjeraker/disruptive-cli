import dtcli


CLAIM = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='target_project_id',
        flags=['target-project-id'],
        xid=True,
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='kit_ids',
        flags=['--kit-ids'],
        metavar='',
        format=dtcli.format.str2list,
    ),
    dtcli.parser.Arg(
        key='device_ids',
        flags=['--device-ids'],
        metavar='',
        format=dtcli.format.str2list,
    ),
    dtcli.parser.Arg(
        key='dry_run',
        flags=['--dry-run'],
        metavar='',
        format=dtcli.format.to_bool,
    ),
])


INFO = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='identifier',
        flags=['identifier'],
        xid=False,
        format=dtcli.format.to_string,
    ),
])
