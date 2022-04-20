import pytest

from tests.framework import DTMock


@pytest.fixture()
def dt_mock(mocker):
    return DTMock(mocker)
