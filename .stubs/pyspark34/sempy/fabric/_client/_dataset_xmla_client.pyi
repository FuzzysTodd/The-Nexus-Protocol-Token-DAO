from sempy._utils._log import log as log, log_xmla as log_xmla
from sempy.fabric._client import WorkspaceClient as WorkspaceClient
from sempy.fabric._client._adomd_connection import AdomdConnection as AdomdConnection
from sempy.fabric._client._base_dataset_client import BaseDatasetClient as BaseDatasetClient
from sempy.fabric._environment import get_workspace_id as get_workspace_id
from sempy.fabric._token_provider import TokenProvider as TokenProvider
from sempy.fabric._utils import clr_to_pandas_dtype as clr_to_pandas_dtype
from uuid import UUID

class DatasetXmlaClient(BaseDatasetClient):
    """
    Client for access to Power BI data in a specific dataset (database) using an XMLA client.

    Generally, a single instance of the class is needed per dataset (database),
    where it can execute multiple DAX queries.

    In contrast to :class:`PowerBIWorkspace` it wraps a different XMLA client:
    `AdomdDataAdapter <https://learn.microsoft.com/en-us/dotnet/api/microsoft.analysisservices.adomdclient.adomddataadapter?view=analysisservices-dotnet>`__
    which deals with data access rather than the PowerBI Model (metadata).
    Each client will usually map to a Dataset (Database) i.e. one or more clients can be instantiated
    within each accessed workspace.

    Parameters
    ----------
    workspace : str or WorkspaceClient
        PowerBI workspace name or workspace client that the dataset originates from.
    dataset : str or UUID
        Dataset name or UUID object containing the dataset ID.
    token_provider : TokenProvider, default=None
        Implementation of TokenProvider that can provide auth token
        for access to the PowerBI workspace. Will attempt to acquire token
        from its execution environment if not provided.
    """
    adomd_connection: AdomdConnection | None
    def __init__(self, workspace: str | UUID | WorkspaceClient | None, dataset: str | UUID, token_provider: TokenProvider | None = None) -> None: ...
    def get_adomd_connection(self) -> AdomdConnection:
        """
        Get python AdomdConnection object

        Returns
        -------
        AdomdConnection
            Python AdomdConnection object.
        """
