import pandas as pd
from _typeshed import Incomplete
from sempy._utils._pandas_utils import rename_and_validate_from_records as rename_and_validate_from_records
from sempy.fabric._client._connection_mode import ConnectionMode as ConnectionMode
from sempy.fabric._client._dataset_onelake_import import DatasetOneLakeImportClient as DatasetOneLakeImportClient
from sempy.fabric._client._dataset_rest_client import DatasetRestClient as DatasetRestClient
from sempy.fabric._client._dataset_xmla_client import DatasetXmlaClient as DatasetXmlaClient
from sempy.fabric._client._fabric_rest_api import OperationStart as OperationStart
from sempy.fabric._environment import get_workspace_id as get_workspace_id
from sempy.fabric._token_provider import SynapseTokenProvider as SynapseTokenProvider, TokenProvider as TokenProvider
from sempy.fabric._utils import collection_to_dataframe as collection_to_dataframe, dotnet_to_pandas_date as dotnet_to_pandas_date, get_properties as get_properties, is_valid_uuid as is_valid_uuid
from sempy.fabric.exceptions import DatasetNotFoundException as DatasetNotFoundException, WorkspaceNotFoundException as WorkspaceNotFoundException
from uuid import UUID

class WorkspaceClient:
    """
    Accessor class for a Power BI workspace.

    The workspace can contain multiple Datasets, which can be accessed via
    a PowerBIClient obtained via :meth:`get_dataset_client`.

    The class is a thin wrapper around
    `Microsoft.AnalysisServices.Tabular.Server <https://learn.microsoft.com/en-us/dotnet/api/microsoft.analysisservices.tabular.server?view=analysisservices-dotnet>`_
    client that accesses cloud Power BI workspace and its Tabular Object Model (TOM)
    via the XMLA interface. The client caches the connection to the server for faster performance.

    Parameters
    ----------
    workspace : str or UUID
        PowerBI Workspace Name or UUID object containing the workspace ID.
    token_provider : TokenProvider, default=None
        Implementation of :class:`~sempy.fabric._token_provider.TokenProvider` that can provide auth token
        for access to the PowerBI workspace. Will attempt to acquire token
        from its execution environment if not provided.
    """
    tom_server_readonly: Incomplete
    token_provider: Incomplete
    dataset_client_types: Incomplete
    def __init__(self, workspace: str | UUID | None = None, token_provider: TokenProvider | None = None) -> None: ...
    def get_workspace_id_from_name(self, workspace_name: str) -> str | None: ...
    def get_workspace_id(self) -> str:
        """
        Get workspace ID of associated workspace.

        Returns
        -------
        String
            Workspace ID.
        """
    def get_workspace_name(self) -> str:
        """
        Get name ID of associated workspace.

        Returns
        -------
        String
            Workspace name.
        """
    def get_datasets(self, mode: str, additional_xmla_properties: str | list[str] | None = None) -> pd.DataFrame:
        """
        Get a list of datasets in a PowerBI workspace.

        Each dataset is derived from
        `Microsoft.AnalysisServices.Tabular.Database <https://learn.microsoft.com/en-us/dotnet/api/microsoft.analysisservices.tabular.database?view=analysisservices-dotnet>`__

        The dataframe contains the following columns:

        - Dataset Name `see <https://learn.microsoft.com/en-us/dotnet/api/microsoft.analysisservices.namedcomponent.name?view=analysisservices-dotnet#microsoft-analysisservices-namedcomponent-name>`__
        - Created Date `see <https://learn.microsoft.com/en-us/dotnet/api/microsoft.analysisservices.majorobject.createdtimestamp?view=analysisservices-dotnet#microsoft-analysisservices-majorobject-createdtimestamp>`__
        - ID `see <https://learn.microsoft.com/en-us/dotnet/api/microsoft.analysisservices.namedcomponent.id?view=analysisservices-dotnet#microsoft-analysisservices-namedcomponent-id>`__
        - Last Update `see <https://learn.microsoft.com/en-us/dotnet/api/microsoft.analysisservices.core.database.lastupdate?view=analysisservices-dotnet#microsoft-analysisservices-core-database-lastupdate>`__

        Returns
        -------
        DataFrame
            Pandas DataFrame listing databases and their attributes.
        """
    def get_dataset(self, dataset: str | UUID):
        """
        Get PowerBI dataset for a given dataset_name.

        The dataset is derived from
        `Microsoft.AnalysisServices.Tabular.Database <https://learn.microsoft.com/en-us/dotnet/api/microsoft.analysisservices.tabular.database?view=analysisservices-dotnet>>`_

        Parameters
        ----------
        dataset : str or UUID
            Dataset name UUID object containing the dataset ID.

        Returns
        -------
        Dataset
            PowerBI Dataset represented as TOM Database object.
        """
    def get_tmsl(self, dataset: str | UUID) -> str:
        """
        Retrieve the TMSL for a given dataset.

        Parameters
        ----------
        dataset : str or UUID
            Name or UUID of the dataset to list the measures for.

        Returns
        -------
        str
            TMSL for the given dataset.
        """
    def execute_tmsl(self, script: str):
        """
        Executes TMSL script.

        Parameters
        ----------
        script : str
            The TMSL script json
        """
    def refresh_tom_cache(self) -> None:
        """
        Refresh the TOM Server (https://learn.microsoft.com/en-us/dotnet/api/microsoft.analysisservices.tabular.server?view=analysisservices-dotnet)
        to it's latest state.
        """
    def list_measures(self, dataset: str | UUID, additional_xmla_properties: str | list[str] | None = None) -> pd.DataFrame:
        """
        Retrieve all measures associated with the given dataset.

        Each measure is derived from
        `Microsoft.AnalysisServices.Tabular.Measure <https://learn.microsoft.com/en-us/dotnet/api/microsoft.analysisservices.tabular.measure?view=analysisservices-dotnet>`__

        Parameters
        ----------
        dataset : str or UUID
            Name or UUID of the dataset to list the measures for.
        additional_xmla_properties : str or List[str], default=None
            Additional XMLA `measure <https://learn.microsoft.com/en-us/dotnet/api/microsoft.analysisservices.tabular.measure?view=analysisservices-dotnet>`_
            properties to include in the returned dataframe.

        Returns
        -------
        DataFrame
            Pandas DataFrame listing measures and their attributes.
        """
    def get_dataset_client(self, dataset: str | UUID, mode: ConnectionMode = ...) -> DatasetRestClient | DatasetXmlaClient | DatasetOneLakeImportClient:
        """
        Get PowerBIClient for a given dataset name or GUID.

        The same cached reusable instance is returned for each dataset.

        Parameters
        ----------
        dataset : str or UUID
            Dataset name or UUID object containing the dataset ID.
        mode : ConnectionMode, default=REST
            Which client to use to connect to the dataset.

        Returns
        -------
        DatasetRestClient, DatasetXmlaClient or DatasetOneLakeImportClient
            Client facilitating data retrieval from a specified dataset.
        """
    def list_reports(self) -> pd.DataFrame:
        """
        Return a list of reports in the specified workspace.

        Returns
        -------
        pandas.DataFrame
            DataFrame with one row per report.
        """
    def list_items(self, type: str | None = None) -> pd.DataFrame: ...
    def create_lakehouse(self, display_name: str, description: str | None = None, max_attempts: int = 10) -> str: ...
    def create_workspace(self, display_name: str, description: str | None = None) -> str: ...
    def delete_item(self, item_id: str): ...
    def delete_workspace(self) -> None: ...
    def create_notebook(self, display_name: str, description: str | None = None, content: str | None = None, max_attempts: int = 10) -> str: ...
    def resolve_item_id(self, item_name: str, type: str | None = None) -> str: ...
    def resolve_item_name(self, item_id: str | UUID, type: str | None = None) -> str: ...
    def resolve_dataset_id(self, dataset_name: str) -> str: ...
    def resolve_dataset_name(self, dataset_id: str | UUID) -> str: ...
    def run_notebook_job(self, notebook_id: str, max_attempts: int = 10) -> str: ...
