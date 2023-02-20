import sys
from typing import Any, List
from dataclasses import dataclass

import tests.api_responses as responses
import tests.framework as framework


class TestEmulator():

    def test_emulator_create(self, dt_emulator_mock):
        @dataclass
        class TestCase:
            name: str
            give_args: List[str]
            give_res: dict
            want_n_rows: int
            want_n_cols: int
            want_row_type: Any
            want_error: Any

        tests = [
            TestCase(
                name='minimal',
                give_args=['project-id', 'device-type'],
                give_res=responses.touch_sensor,
                want_n_cols=4,
                want_n_rows=2,
                want_row_type=str,
                want_error=None,
            ),
            TestCase(
                name='--full',
                give_args=['project.user', 'device-type', '--full'],
                give_res=responses.touch_sensor,
                want_n_cols=7,
                want_n_rows=2,
                want_row_type=str,
                want_error=None,
            ),
        ]

        for test in tests:
            sys.argv = ['main.py', 'emulator', 'create'] + test.give_args
            dt_emulator_mock.res = test.give_res
            framework.table_test(test)

    def test_emulator_delete(self, dt_emulator_mock):
        @dataclass
        class TestCase:
            name: str
            give_args: List[str]
            give_res: Any
            want_n_rows: int
            want_n_cols: int
            want_row_type: Any
            want_error: Any

        tests = [
            TestCase(
                name='minimal',
                give_args=['device-id', 'project-id'],
                give_res=None,
                want_n_cols=0,
                want_n_rows=0,
                want_row_type=None,
                want_error=None,
            ),
            TestCase(
                name='--full',
                give_args=['device-id', 'project.user', '--full'],
                give_res=None,
                want_n_cols=0,
                want_n_rows=0,
                want_row_type=None,
                want_error=None,
            ),
        ]

        for test in tests:
            sys.argv = ['main.py', 'emulator', 'delete'] + test.give_args
            dt_emulator_mock.res = test.give_res
            framework.table_test(test)

    def test_emulator_publish(self, dt_emulator_mock):
        @dataclass
        class TestCase:
            name: str
            give_args: List[str]
            give_res: Any = None
            want_n_rows: int = 0
            want_n_cols: int = 0
            want_row_type: Any = None
            want_error: Any = None

        tests = [
            TestCase(
                name='touch',
                give_args=[
                    'touch',
                    'emulator-id',
                    'project-id',
                ],
                want_error=None,
            ),
            TestCase(
                name='temperature',
                give_args=[
                    'temperature',
                    'emulator-id',
                    'project-id',
                    '23',
                ],
                want_error=None,
            ),
            TestCase(
                name='objectPresent',
                give_args=[
                    'object-present',
                    'emulator-id',
                    'project-id',
                    'PRESENT',
                ],
                want_error=None,
            ),
            TestCase(
                name='humidity',
                give_args=[
                    'humidity',
                    'emulator-id',
                    'project-id',
                    '23',
                    '73',
                ],
                want_error=None,
            ),
            TestCase(
                name='objectPresentCount',
                give_args=[
                    'object-present-count',
                    'emulator-id',
                    'project-id',
                    '99',
                ],
                want_error=None,
            ),
            TestCase(
                name='touchCount',
                give_args=[
                    'touch-count',
                    'emulator-id',
                    'project-id',
                    '99',
                ],
                want_error=None,
            ),
            TestCase(
                name='waterPresent',
                give_args=[
                    'water-present',
                    'emulator-id',
                    'project-id',
                    'NOT_PRESENT',
                ],
                want_error=None,
            ),
            TestCase(
                name='networkStatus minimal',
                give_args=[
                    'network-status',
                    'emulator-id',
                    'project-id',
                ],
                want_error=None,
            ),
            TestCase(
                name='networkStatus optionals',
                give_args=[
                    'network-status',
                    'emulator-id',
                    'project-id',
                    '--signal-strength', '80',
                    '--rssi', '-44',
                    '--transmission-mode', 'LOW_POWER_STANDARD_MODE',
                ],
                want_error=None,
            ),
            TestCase(
                name='batteryStatus',
                give_args=[
                    'battery-status',
                    'emulator-id',
                    'project-id',
                    '89',
                ],
                want_error=None,
            ),
            TestCase(
                name='connectionStatus',
                give_args=[
                    'connection-status',
                    'emulator-id',
                    'project-id',
                    'ETHERNET',
                    'ETHERNET,CELLULAR',
                ],
                want_error=None,
            ),
            TestCase(
                name='ethernetStatus',
                give_args=[
                    'ethernet-status',
                    'emulator-id',
                    'project-id',
                    'mac-address',
                    'ip-address',
                ],
                want_error=None,
            ),
            TestCase(
                name='cellularStatus',
                give_args=[
                    'cellular-status',
                    'emulator-id',
                    'project-id',
                    '99',
                ],
                want_error=None,
            ),
            TestCase(
                name='co2',
                give_args=[
                    'co2',
                    'emulator-id',
                    'project-id',
                    '8888',
                ],
                want_error=None,
            ),
            TestCase(
                name='pressure',
                give_args=[
                    'pressure',
                    'emulator-id',
                    'project-id',
                    '8888',
                ],
                want_error=None,
            ),
            TestCase(
                name='motion',
                give_args=[
                    'motion',
                    'emulator-id',
                    'project-id',
                    'MOTION_DETECTED',
                ],
                want_error=None,
            ),
            TestCase(
                name='deskOccupancy',
                give_args=[
                    'desk-occupancy',
                    'emulator-id',
                    'project-id',
                    'DESK_OCCUPIED',
                ],
                want_error=None,
            ),
        ]

        for test in tests:
            sys.argv = ['main.py', 'emulator', 'publish'] + test.give_args
            dt_emulator_mock.res = test.give_res
            framework.table_test(test)