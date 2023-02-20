
touch_sensor = {
    "name": "projects/c0md3mm0c7pet3vico8g/devices/emucpuc989qdqebrvv29so0",
    "type": "touch",
    "productNumber": "100110",
    "labels": {
        "name": "touch",
        "new-label": "99",
        "virtual-sensor": ""
    },
    "reported": {
        "networkStatus": {
            "signalStrength": 99,
            "rssi": -50,
            "updateTime": "2021-03-13T16:05:58.421952Z",
            "cloudConnectors": [
                {
                    "id": "emulated-ccon",
                    "signalStrength": 99,
                    "rssi": -50
                }
            ],
            "transmissionMode": "LOW_POWER_STANDARD_MODE"
        },
        "batteryStatus": {
            "percentage": 100,
            "updateTime": "2021-03-13T16:05:56.684645Z"
        },
        "touch": {
            "updateTime": "2021-03-13T16:05:55.084433Z"
        }
    }
}

dataconnector = {
    "name": "projects/c11u9p094l47cdv1o3pg/'\
        'dataconnectors/c3e56nnimbf5a5nfag00",
    "displayName": "ngrok",
    "type": "HTTP_PUSH",
    "status": "ACTIVE",
    "events": [
        "touch",
        "temperature",
        "humidity"
    ],
    "labels": [
        "name",
        "nlc"
    ],
    "httpConfig": {
        "url": "https://testurl.io/path",
        "signatureSecret": "test-secret",
        "headers": {
            "my-header": "my-value"
        }
    }
}

transfer_device_error = {
    "device": "projects/c0md3mm0c7pet3vico8g/devices/emucpuc989qdqebrvv29so0",
    "status": {
        "code": "404",
        "message": "missing device",
    },
}

label_set_error = {
    "device": "projects/c0md3mm0c7pet3vico8g/devices/emucpuc989qdqebrvv29so0",
    "status": {
        "code": "405",
        "message": "illegal key",
    },
}

project = {
    "name": "projects/c10u7p094l47cdv013pg",
    "displayName": "test-project",
    "organization": "organizations/c11hhmq0ss90036gu51g",
    "organizationDisplayName": "test-org",
    "sensorCount": 12,
    "cloudConnectorCount": 1,
    "inventory": False
}

projects = [
    project,
    project,
    project,
    project,
]

project_permissions = [
    'sensor.read',
    'serviceaccount.key.delete',
    'dataconnector.read',
    'membership.update',
    'serviceaccount.delete',
]

member_pending_user = {
    "name": "projects/c14u8u090l47cdv1o3pg/members/20744",
    "displayName": "some-email@addr.no",
    "roles": [
      "roles/project.user"
    ],
    "status": "PENDING",
    "email": "some-email@addr.no",
    "accountType": "USER",
    "createTime": "2023-02-07T10:47:06.993125Z"
}

members = [
    member_pending_user,
    member_pending_user,
    member_pending_user,
]

organization = {
    "name": "organizations/c11hum0oss88036gu53u",
    "displayName": "my-test-org"
}

organizations = [
    organization,
    organization,
    organization,
]

organization_permissions = [
    'membership.read',
    'subscription.read',
    'membership.delete',
    'billinginfo.read',
    'project.create',
    'organization.update',
]

organization_member = {
    "name": "organizations/c20humqoss98836gi93g/members/21800",
    "displayName": "some-email@your-domain.com",
    "roles": [
        "roles/organization.admin"
    ],
    "status": "PENDING",
    "email": "some-email@your-domain.com",
    "accountType": "USER",
    "createTime": "2023-02-14T14:27:39.116943Z"
}

organization_members = [
    organization_member,
    organization_member,
    organization_member,
    organization_member,
]

service_account = {
    "name": "projects/c15u8p094147udv103pg/serviceaccounts/c952Pftnladgo0bnhjt1",
    "email": "c852pttnlAdg01bmhito@c14u9p094l57wdu103pi.serviceaccount.d21s.com",
    "displayName": "test-sa",
    "enableBasicAuth": True,
    "createTime": "2022-02-14T10:19:43.392171Z",
    "updateTime": "2022-03-28T08:57:23.416978Z"
}

service_accounts = [
    service_account,
    service_account,
    service_account,
]

service_account_key = {
    "name": "projects/c14i2po94i42cdu1u3pg/serviceaccounts/c852ufbnladgi0buhjt0/keys/iflp4uhv2tbg01bf5600",
    "id": "iflp4uhv2tbg01bf5600",
    "createTime": "2023-02-14T13:54:02.543389Z"
}

service_account_keys = [
    service_account_key,
    service_account_key,
    service_account_key,
    service_account_key,
    service_account_key,
]

temperature_event = {
    "eventId": "cfp1104dbbioigt17s30",
    "targetName": "projects/c43bu3eb9da7puhjoor0/devices/bl7ukshbutbg109kco1u",
    "eventType": "temperature",
    "data": {
        "temperature": {
            "value": 17.1,
            "updateTime": "2023-02-19T13:14:04.227000Z",
            "samples": [
                {
                    "value": 17.1,
                    "sampleTime": "2023-02-19T13:14:04.227000Z"
                }
            ]
        }
    },
    "timestamp": "2023-02-19T13:14:04.227000Z"
}

network_status_event = {
    "eventId": "cfp1104dbbioigt17s30",
    "targetName": "projects/c43bu3eb9da7puhjoor0/devices/bl7ukshbutbg109kco1u",
    "eventType": "networkStatus",
    "data": {
        "networkStatus": {
            "signalStrength": 76,
            "rssi": -64,
            "updateTime": "2023-02-19T13:14:04.227000Z",
            "cloudConnectors": [
                {
                    "id": "bbefuu1c01111540t77g",
                    "signalStrength": 76,
                    "rssi": -64
                }
            ],
            "transmissionMode": "LOW_POWER_STANDARD_MODE"
        }
    },
    "timestamp": "2023-02-19T13:14:04.227000Z"
}

events_list = [
    temperature_event,
    network_status_event,
    temperature_event,
    network_status_event,
    temperature_event,
    network_status_event,
]

role_project_user = {
    "name": "roles/project.user",
    "displayName": "Project user",
    "description": "Users cannot change anything, just view the data in the Project",
    "permissions": [
        "project.read",
        "membership.read",
        "sensor.read",
        "device.read",
        "dataconnector.read",
        "serviceaccount.read",
        "serviceaccount.key.read",
        "emulator.read"
    ]
}

role_project_developer = {
    "name": "roles/project.developer",
    "displayName": "Project developer",
    "description": "Allows editing devices and Project settings",
    "permissions": [
        "project.read",
        "membership.read",
        "sensor.read",
        "sensor.update",
        "device.read",
        "device.update",
        "dataconnector.create",
        "dataconnector.read",
        "dataconnector.update",
        "dataconnector.delete",
        "serviceaccount.read",
        "serviceaccount.key.read",
        "emulator.read",
        "emulator.update",
        "emulator.create",
        "emulator.delete"
    ]
}

roles = [
    role_project_user,
    role_project_developer,
]