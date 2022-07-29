import pytest

import tests.framework as fw


@pytest.fixture()
def dt_mock(mocker):
    return fw.DTMock(mocker)


@pytest.fixture()
def dt_device_mock(mocker):
    return fw.DTDeviceMock(mocker)


@pytest.fixture()
def dt_dataconnector_mock(mocker):
    return fw.DTDataconnectorMock(mocker)
