import datetime
import pandas as pd
from sempy._utils._pandas_utils import rename_and_validate_from_records as rename_and_validate_from_records, safe_convert_rest_datetime as safe_convert_rest_datetime
from sempy.fabric._client import WorkspaceClient as WorkspaceClient
from sempy.fabric._client._base_dataset_client import BaseDatasetClient as BaseDatasetClient
from sempy.fabric._client._refresh_execution_details import RefreshExecutionDetails as RefreshExecutionDetails
from sempy.fabric._token_provider import TokenProvider as TokenProvider
from uuid import UUID

class DatasetRestClient(BaseDatasetClient):
    """
    Client for access to Power BI data in a specific dataset using REST API calls.

    Parameters
    ----------
    workspace : str or WorkspaceClient
        PowerBI workspace name or workspace client that the dataset originates from.
    dataset : str
        Dataset name or GUID.
    token_provider : TokenProvider, default=None
        Implementation of TokenProvider that can provide auth token
        for access to the PowerBI workspace. Will attempt to acquire token
        from its execution environment if not provided.
    """
    def __init__(self, workspace: str | WorkspaceClient, dataset: str | UUID, token_provider: TokenProvider | None = None) -> None: ...
    def refresh_async(self, refresh_type: str = 'automatic', max_parallelism: int = 10, commit_mode: str = 'transactional', retry_count: int = 1, objects: list | None = None, apply_refresh_policy: bool = True, effective_date: datetime.date = ..., verbose: int = 0) -> str: ...
    def get_refresh_execution_details(self, refresh_request_id: str | UUID) -> RefreshExecutionDetails: ...
    def list_refresh_history(self, top_n: int | None = None) -> pd.DataFrame: ...
