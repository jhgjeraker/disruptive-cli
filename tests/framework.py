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


class DTProjectMock(DTMock):

    def __init__(self, mocker):
        super().__init__(mocker)

        self.project_get_patcher = self._mocker.patch(
            'disruptive.Project.get_project',
            side_effect=self._patched_project_get,
        )
        self.project_list_patcher = self._mocker.patch(
            'disruptive.Project.list_projects',
            side_effect=self._patched_project_list,
        )
        self.project_create_patcher = self._mocker.patch(
            'disruptive.Project.create_project',
            side_effect=self._patched_project_create,
        )
        self.project_update_patcher = self._mocker.patch(
            'disruptive.Project.update_project',
            side_effect=self._patched_project_update,
        )
        self.project_delete_patcher = self._mocker.patch(
            'disruptive.Project.delete_project',
            side_effect=self._patched_project_delete,
        )
        self.project_permissions_patcher = self._mocker.patch(
            'disruptive.Project.list_permissions',
            side_effect=self._patched_project_permissions,
        )
        self.project_member_add_patcher = self._mocker.patch(
            'disruptive.Project.add_member',
            side_effect=self._patched_project_member_add,
        )
        self.project_member_remove_patcher = self._mocker.patch(
            'disruptive.Project.remove_member',
            side_effect=self._patched_project_member_remove,
        )
        self.project_member_get_patcher = self._mocker.patch(
            'disruptive.Project.get_member',
            side_effect=self._patched_project_member_get,
        )
        self.project_member_update_patcher = self._mocker.patch(
            'disruptive.Project.update_member',
            side_effect=self._patched_project_member_update,
        )
        self.project_member_list_patcher = self._mocker.patch(
            'disruptive.Project.list_members',
            side_effect=self._patched_project_member_list,
        )
        self.project_member_invite_url_patcher = self._mocker.patch(
            'disruptive.Project.get_member_invite_url',
            side_effect=self._patched_project_member_invite_url,
        )

    def _patched_project_get(self, project_id, **kwargs):
        return dt.Project(self.res)

    def _patched_project_list(self, **kwargs):
        return [dt.Project(res) for res in self.res]

    def _patched_project_create(self, **kwargs):
        return dt.Project(self.res)

    def _patched_project_update(self, **kwargs):
        return None

    def _patched_project_delete(self, **kwargs):
        return None

    def _patched_project_permissions(self, **kwargs):
        return self.res

    def _patched_project_member_add(self, **kwargs):
        return dt.Member(self.res)

    def _patched_project_member_remove(self, **kwargs):
        return None

    def _patched_project_member_get(self, **kwargs):
        return dt.Member(self.res)

    def _patched_project_member_update(self, **kwargs):
        return dt.Member(self.res)

    def _patched_project_member_list(self, **kwargs):
        return [dt.Member(res) for res in self.res]

    def _patched_project_member_invite_url(self, **kwargs):
        return self.res


class DTServiceAccountMock(DTMock):

    def __init__(self, mocker):
        super().__init__(mocker)

        self.serviceaccount_get_patcher = self._mocker.patch(
            'disruptive.ServiceAccount.get_service_account',
            side_effect=self._patched_serviceaccount_get,
        )
        self.serviceaccount_list_patcher = self._mocker.patch(
            'disruptive.ServiceAccount.list_service_accounts',
            side_effect=self._patched_serviceaccount_list,
        )
        self.serviceaccount_create_patcher = self._mocker.patch(
            'disruptive.ServiceAccount.create_service_account',
            side_effect=self._patched_serviceaccount_create,
        )
        self.serviceaccount_update_patcher = self._mocker.patch(
            'disruptive.ServiceAccount.update_service_account',
            side_effect=self._patched_serviceaccount_update,
        )
        self.serviceaccount_delete_patcher = self._mocker.patch(
            'disruptive.ServiceAccount.delete_service_account',
            side_effect=self._patched_serviceaccount_delete,
        )
        self.serviceaccount_key_get_patcher = self._mocker.patch(
            'disruptive.ServiceAccount.get_key',
            side_effect=self._patched_serviceaccount_key_get,
        )
        self.serviceaccount_key_create_patcher = self._mocker.patch(
            'disruptive.ServiceAccount.create_key',
            side_effect=self._patched_serviceaccount_key_create,
        )
        self.serviceaccount_key_list_patcher = self._mocker.patch(
            'disruptive.ServiceAccount.list_keys',
            side_effect=self._patched_serviceaccount_key_list,
        )
        self.serviceaccount_key_delete_patcher = self._mocker.patch(
            'disruptive.ServiceAccount.delete_key',
            side_effect=self._patched_serviceaccount_key_delete,
        )

    def _patched_serviceaccount_get(self, **kwargs):
        return dt.ServiceAccount(self.res)

    def _patched_serviceaccount_list(self, **kwargs):
        return [dt.ServiceAccount(res) for res in self.res]

    def _patched_serviceaccount_create(self, **kwargs):
        return dt.ServiceAccount(self.res)

    def _patched_serviceaccount_update(self, **kwargs):
        return dt.ServiceAccount(self.res)

    def _patched_serviceaccount_delete(self, **kwargs):
        return self.res

    def _patched_serviceaccount_key_get(self, **kwargs):
        return dt.Key(self.res)

    def _patched_serviceaccount_key_create(self, **kwargs):
        return dt.Key(self.res)

    def _patched_serviceaccount_key_list(self, **kwargs):
        return [dt.Key(res) for res in self.res]

    def _patched_serviceaccount_key_delete(self, **kwargs):
        return self.res


class DTOrganizationMock(DTMock):

    def __init__(self, mocker):
        super().__init__(mocker)

        self.organization_get_patcher = self._mocker.patch(
            'disruptive.Organization.get_organization',
            side_effect=self._patched_organization_get,
        )
        self.organization_list_patcher = self._mocker.patch(
            'disruptive.Organization.list_organizations',
            side_effect=self._patched_organization_list,
        )
        self.organization_permissions_patcher = self._mocker.patch(
            'disruptive.Organization.list_permissions',
            side_effect=self._patched_organization_permissions,
        )
        self.organization_member_add_patcher = self._mocker.patch(
            'disruptive.Organization.add_member',
            side_effect=self._patched_organization_add_member,
        )
        self.organization_member_remove_patcher = self._mocker.patch(
            'disruptive.Organization.remove_member',
            side_effect=self._patched_organization_remove_member,
        )
        self.organization_member_get_patcher = self._mocker.patch(
            'disruptive.Organization.get_member',
            side_effect=self._patched_organization_get_member,
        )
        self.organization_member_list_patcher = self._mocker.patch(
            'disruptive.Organization.list_members',
            side_effect=self._patched_organization_list_members,
        )
        self.organization_member_invite_url_patcher = self._mocker.patch(
            'disruptive.Organization.get_member_invite_url',
            side_effect=self._patched_organization_member_invite_url,
        )

    def _patched_organization_get(self, **kwargs):
        return dt.Organization(self.res)

    def _patched_organization_list(self, **kwargs):
        return [dt.Organization(res) for res in self.res]

    def _patched_organization_permissions(self, **kwargs):
        return [res for res in self.res]

    def _patched_organization_add_member(self, **kwargs):
        return dt.Member(self.res)

    def _patched_organization_remove_member(self, **kwargs):
        return self.res

    def _patched_organization_get_member(self, **kwargs):
        return dt.Member(self.res)

    def _patched_organization_list_members(self, **kwargs):
        return [dt.Member(res) for res in self.res]

    def _patched_organization_member_invite_url(self, **kwargs):
        return self.res


class DTEventMock(DTMock):

    def __init__(self, mocker):
        super().__init__(mocker)

        self.event_list_patcher = self._mocker.patch(
            'disruptive.EventHistory.list_events',
            side_effect=self._patched_event_list,
        )

    def _patched_event_list(self, **kwargs):
        return dt.events.Event.from_mixed_list(self.res)


class DTRoleMock(DTMock):

    def __init__(self, mocker):
        super().__init__(mocker)

        self.role_get_patcher = self._mocker.patch(
            'disruptive.Role.get_role',
            side_effect=self._patched_role_get,
        )
        self.role_list_patcher = self._mocker.patch(
            'disruptive.Role.list_roles',
            side_effect=self._patched_role_list,
        )

    def _patched_role_get(self, **kwargs):
        return dt.Role(self.res)

    def _patched_role_list(self, **kwargs):
        return [dt.Role(res) for res in self.res]


class DTEmulatorMock(DTMock):

    def __init__(self, mocker):
        super().__init__(mocker)

        self.emulator_create_patcher = self._mocker.patch(
            'disruptive.Emulator.create_device',
            side_effect=self._patched_emulator_create,
        )
        self.emulator_delete_patcher = self._mocker.patch(
            'disruptive.Emulator.delete_device',
            side_effect=self._patched_emulator_delete,
        )
        self.emulator_publish_patcher = self._mocker.patch(
            'disruptive.Emulator.publish_event',
            side_effect=self._patched_emulator_publish,
        )

    def _patched_emulator_create(self, **kwargs):
        return dt.Device(self.res)

    def _patched_emulator_delete(self, **kwargs):
        return self.res

    def _patched_emulator_publish(self, **kwargs):
        return self.res