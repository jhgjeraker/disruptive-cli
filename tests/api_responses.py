
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
