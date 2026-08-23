from sempy.fabric._client._dataset_rest_client import DatasetRestClient as DatasetRestClient
from sempy.fabric._client._dataset_xmla_client import DatasetXmlaClient as DatasetXmlaClient
from sempy.fabric._client._tools import import_pbix_sample as import_pbix_sample
from sempy.fabric._client._workspace_client import WorkspaceClient as WorkspaceClient

__all__ = ['WorkspaceClient', 'DatasetRestClient', 'DatasetXmlaClient', 'import_pbix_sample']
