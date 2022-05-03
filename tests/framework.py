import disruptive as dt


class DTMock():

    def __init__(self, mocker):
        self._mocker = mocker

        self.res = {}


class DTDeviceMock(DTMock):

    def __init__(self, mocker):
        super().__init__(mocker)

        self.device_get_patcher = self._mocker.patch(
            'disruptive.Device.get_device',
            side_effect=self._patched_device_get,
        )
        self.device_list_patcher = self._mocker.patch(
            'disruptive.Device.list_devices',
            side_effect=self._patched_device_list,
        )

    def _patched_device_get(self, device_id, **kwargs):
        return dt.Device(self.res)

    def _patched_device_list(self, project_id, **kwargs):
        return [dt.Device(res) for res in self.res]
