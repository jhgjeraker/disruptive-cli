import disruptive as dt


class DTMock():

    def __init__(self, mocker):
        self._mocker = mocker

        self.raw = {}

        self.device_get_patcher = self._mocker.patch(
            'disruptive.Device.get_device',
            side_effect=self._patched_device_get,
        )

    def _patched_device_get(self, device_id, **kwargs):
        return dt.Device(self.raw)
