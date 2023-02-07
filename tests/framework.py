from typing import Optional, List

import pytest
import disruptive as dt

import dtcli


def table_test(test):
    if test.want_error is None:
        table = dtcli.cli.main()

        assert test.want_n_rows == table.n_rows, test.name
        assert test.want_n_cols == table.n_columns, test.name

        for row in table.rows:
            assert isinstance(row, test.want_row_type), test.name
    else:
        with pytest.raises(test.want_error):
            dtcli.cli.main()


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
        self.device_transfer_patcher = self._mocker.patch(
            'disruptive.Device.transfer_devices',
            side_effect=self._patched_device_transfer,
        )
        self.device_label_set_patcher = self._mocker.patch(
            'disruptive.Device.batch_update_labels',
            side_effect=self._patched_device_label_set,
        )

    def _patched_device_get(self, device_id, **kwargs):
        return dt.Device(self.res)

    def _patched_device_list(self, project_id, **kwargs):
        return [dt.Device(res) for res in self.res]

    def _patched_device_transfer(self,
                                 device_ids,
                                 source_project_id,
                                 target_project_id,
                                 **kwargs,
                                 ):
        return [dt.errors.TransferDeviceError(err) for err in self.res]

    def _patched_device_label_set(self,
                                  device_ids,
                                  project_id,
                                  set_labels,
                                  **kwargs,
                                  ):
        return [dt.errors.LabelUpdateError(err) for err in self.res]


class DTDataconnectorMock(DTMock):

    def __init__(self, mocker):
        super().__init__(mocker)

        self.dataconnector_get_patcher = self._mocker.patch(
            'disruptive.DataConnector.get_data_connector',
            side_effect=self._patched_dataconnector_get,
        )
        self.dataconnector_list_patcher = self._mocker.patch(
            'disruptive.DataConnector.list_data_connectors',
            side_effect=self._patched_dataconnector_list,
        )
        self.dataconnector_create_patcher = self._mocker.patch(
            'disruptive.DataConnector.create_data_connector',
            side_effect=self._patched_dataconnector_create,
        )
        self.dataconnector_update_patcher = self._mocker.patch(
            'disruptive.DataConnector.update_data_connector',
            side_effect=self._patched_dataconnector_update,
        )
        self.dataconnector_delete_patcher = self._mocker.patch(
            'disruptive.DataConnector.delete_data_connector',
            side_effect=self._patched_dataconnector_delete,
        )
        self.dataconnector_sync_patcher = self._mocker.patch(
            'disruptive.DataConnector.sync_data_connector',
            side_effect=self._patched_dataconnector_sync,
        )
        self.dataconnector_metrics_patcher = self._mocker.patch(
            'disruptive.DataConnector.get_metrics',
            side_effect=self._patched_dataconnector_metrics,
        )

    def _patched_dataconnector_get(self,
                                   data_connector_id,
                                   project_id,
                                   **kwargs):
        return dt.DataConnector(self.res)

    def _patched_dataconnector_list(self, project_id, **kwargs):
        return [dt.DataConnector(res) for res in self.res]

    def _patched_dataconnector_create(self,
                                      project_id,
                                      config,
                                      display_name: str = '',
                                      status: str = 'ACTIVE',
                                      event_types: List[str] = [],
                                      labels: List[str] = [],
                                      **kwargs):
        return dt.DataConnector(self.res)

    def _patched_dataconnector_update(self,
                                      data_connector_id: str,
                                      project_id: str,
                                      config: 
                                      Optional[dt.DataConnector.HttpPushConfig]
                                      = None,
                                      display_name: Optional[str] = None,
                                      status: Optional[str] = None,
                                      event_types: Optional[List[str]] = None,
                                      labels: Optional[List[str]] = None,
                                      **kwargs):
        return dt.DataConnector(self.res)

    def _patched_dataconnector_delete(self,
                                      data_connector_id: str,
                                      project_id: str,
                                      **kwargs):
        return None

    def _patched_dataconnector_sync(self,
                                    data_connector_id: str,
                                    project_id: str,
                                    **kwargs):
        return None

    def _patched_dataconnector_metrics(self,
                                       data_connector_id: str,
                                       project_id: str,
                                       **kwargs):
        return None
