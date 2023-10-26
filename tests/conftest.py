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


@pytest.fixture()
def dt_project_mock(mocker):
    return fw.DTProjectMock(mocker)


@pytest.fixture()
def dt_serviceaccount_mock(mocker):
    return fw.DTServiceAccountMock(mocker)


@pytest.fixture()
def dt_organization_mock(mocker):
    return fw.DTOrganizationMock(mocker)


@pytest.fixture()
def dt_event_mock(mocker):
    return fw.DTEventMock(mocker)


@pytest.fixture()
def dt_role_mock(mocker):
    return fw.DTRoleMock(mocker)


@pytest.fixture()
def dt_emulator_mock(mocker):
    return fw.DTEmulatorMock(mocker)


@pytest.fixture()
def dt_claim_mock(mocker):
    return fw.DTClaimMock(mocker)
