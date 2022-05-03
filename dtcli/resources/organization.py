from typing import Any, List

import disruptive as dt

import dtcli
from dtcli.table import Table, Column


def _organizations(organizations: List[dt.Organization],
                   cfg: dict,
                   **kwargs: Any,
                   ) -> Table:

    table = Table(
        default_columns=[
            Column('organization_id', False),
            Column('display_name', False),
        ],
        cfg=cfg,
        opts=kwargs,
    )
    table.expand_rows(organizations)
    table.new_entries(organizations)

    return table


def org_get(cfg: dict, **kwargs: Any) -> Table:
    ok, args = dtcli.args.organization.GET.reparse(**kwargs)
    if not ok:
        return Table.empty()

    return _organizations(
        organizations=dtcli.args.organization.GET.call(
            method=dt.Organization.get_organization,
            method_args=args,
        ),
        cfg=cfg,
        **kwargs,
    )


def org_list(cfg: dict, **kwargs: Any) -> Table:
    ok, args = dtcli.args.organization.LIST.reparse(**kwargs)
    if not ok:
        return Table.empty()

    return _organizations(
        organizations=dtcli.args.organization.LIST.call(
            method=dt.Organization.list_organizations,
            method_args=args,
        ),
        cfg=cfg,
        **kwargs,
    )


def org_permissions(cfg: dict, **kwargs: Any) -> Table:
    ok, args = dtcli.args.organization.PERMISSIONS.reparse(**kwargs)
    if not ok:
        return Table.empty()

    permissions = dtcli.args.organization.PERMISSIONS.call(
        method=dt.Organization.list_permissions,
        method_args=args,
    )

    for permission in permissions:
        dtcli.format.stdout(permission)

    return Table.empty()


def member_add(cfg: dict, **kwargs: dict) -> Table:
    ok, args = dtcli.args.organization.MEMBER_ADD.reparse(**kwargs)
    if not ok:
        return Table.empty()

    return dtcli.resources.project._members(
        members=dtcli.args.organization.MEMBER_ADD.call(
            method=dt.Organization.add_member,
            method_args=args,
        ),
        cfg=cfg,
        **kwargs,
    )


def member_get(cfg: dict, **kwargs: dict) -> Table:
    ok, args = dtcli.args.organization.MEMBER_GET.reparse(**kwargs)
    if not ok:
        return Table.empty()

    return dtcli.resources.project._members(
        members=dtcli.args.organization.MEMBER_GET.call(
            method=dt.Organization.get_member,
            method_args=args,
        ),
        cfg=cfg,
        **kwargs,
    )


def member_list(cfg: dict, **kwargs: dict) -> Table:
    ok, args = dtcli.args.organization.MEMBER_LIST.reparse(**kwargs)
    if not ok:
        return Table.empty()

    return dtcli.resources.project._members(
        members=dtcli.args.organization.MEMBER_LIST.call(
            method=dt.Organization.list_members,
            method_args=args,
        ),
        cfg=cfg,
        **kwargs,
    )


def member_remove(cfg: dict, **kwargs: dict) -> Table:
    ok, args = dtcli.args.organization.MEMBER_REMOVE.reparse(**kwargs)
    if not ok:
        return Table.empty()

    dtcli.args.organization.MEMBER_REMOVE.call(
        method=dt.Organization.remove_member,
        method_args=args,
    )

    return Table.empty()


def member_url(cfg: dict, **kwargs: dict) -> Table:
    ok, args = dtcli.args.organization.MEMBER_INVITE_URL.reparse(**kwargs)
    if not ok:
        return Table.empty()

    urls = dtcli.args.organization.MEMBER_INVITE_URL.call(
        method=dt.Organization.get_member_invite_url,
        method_args=args,
    )

    for url in urls:
        dtcli.format.stdout(url)

    return Table.empty()
