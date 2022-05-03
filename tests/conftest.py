import pytest

from tests.framework import DTMock, DTDeviceMock


@pytest.fixture()
def dt_mock(mocker):
    return DTMock(mocker)


@pytest.fixture()
def dt_device_mock(mocker):
    return DTDeviceMock(mocker)
