from typing import List, Any

import disruptive as dt

import dtcli
from dtcli.table import Table, Column


class ClaimInfoDevice:
    def __init__(self, raw: dict) -> None:
        self.raw = raw
        self.kit_id = raw['kit_id']
        self.kit_name = raw['kit_name']
        self.device_id = raw['device_id']
        self.device_type = raw['device_type']
        self.product_number = raw['product_number']
        self.is_claimed = raw['is_claimed']
        self.error_code = raw['error_code']
        self.error_message = raw['error_message']

    @classmethod
    def from_claim(cls, claim: dt.Claim) -> List:
        if isinstance(claim.claimed_item, dt.Claim.ClaimDevice):
            return [cls.from_device(claim.claimed_item)]
        else:
            return cls.from_kit(claim.claimed_item)

    @classmethod
    def from_kit(cls, kit: dt.Claim.ClaimKit) -> List:
        devices = []
        for device in kit.devices:
            devices.append(cls.from_device(
                device=device,
                kit_id=kit.kit_id,
                kit_name=kit.display_name,
            ))
        return devices

    @classmethod
    def from_device(cls,
                    device: dt.Claim.ClaimDevice,
                    kit_id: str = '',
                    kit_name: str = '',
                    ) -> 'ClaimInfoDevice':
        return cls({
                'kit_id': kit_id,
                'kit_name': kit_name,
                'device_id': device.device_id,
                'device_type': device.device_type,
                'product_number': device.product_number,
                'is_claimed': device.is_claimed,
                'error_code': '',
                'error_message': '',
        })

    @classmethod
    def from_error(cls, err: Any) -> 'ClaimInfoDevice':
        device_id = err.device_id if hasattr(err, 'device_id') else ''
        kit_id = err.kit_id if hasattr(err, 'kit_id') else ''
        return cls({
            'kit_id': kit_id,
            'kit_name': '',
            'device_id': device_id,
            'device_type': '',
            'product_number': '',
            'is_claimed': False,
            'error_code': err.code,
            'error_message': err.message,
        })


def _claim_items(claims: List[ClaimInfoDevice],
                 cfg: dict,
                 **kwargs: dict,
                 ) -> Table:
    table = Table(
        default_columns=[
            Column('kit_id', False),
            Column('device_id', False),
            Column('error_code', False),
            Column('error_message', False),
        ],
        cfg=cfg,
        opts=kwargs,
    )
    table.expand_rows(claims)
    table.new_entries(claims)

    return table


def _claim_info(claims: List[ClaimInfoDevice],
                cfg: dict,
                **kwargs: dict,
                ) -> Table:
    table = Table(
        default_columns=[
            Column('kit_id', False),
            Column('kit_name', True),
            Column('device_id', False),
            Column('device_type', False),
            Column('product_number', True),
            Column('is_claimed', False),
        ],
        cfg=cfg,
        opts=kwargs,
    )
    table.expand_rows(claims)
    table.new_entries(claims)

    return table


def claim_item(cfg: dict, **kwargs: dict) -> Table:
    ok, args = dtcli.args.claim.CLAIM.reparse(**kwargs)
    if not ok:
        return Table.empty()

    claimed_devices, errors = dtcli.args.claim.CLAIM.call(
        method=dt.Claim.claim,
        method_args=args,
    )[0]

    entries = []
    for device in claimed_devices:
        entries.append(ClaimInfoDevice.from_device(device))

    for err in errors:
        entries.append(ClaimInfoDevice.from_error(err))

    claims_table = _claim_items(
        claims=entries,
        cfg=cfg,
        **kwargs,
    )

    return claims_table


def claim_info(cfg: dict, **kwargs: dict) -> Table:
    ok, args = dtcli.args.claim.INFO.reparse(**kwargs)
    if not ok:
        return Table.empty()

    claim_info = dtcli.args.claim.INFO.call(
        method=dt.Claim.claim_info,
        method_args=args,
    )

    entries = []
    for claim in claim_info:
        entries += ClaimInfoDevice.from_claim(claim)

    return _claim_info(
        claims=entries,
        cfg=cfg,
        **kwargs,
    )
