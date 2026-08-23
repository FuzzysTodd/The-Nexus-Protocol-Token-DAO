import pandas as pd
from sempy._utils._log import log as log
from sempy._utils._pandas_utils import rename_and_validate_from_records as rename_and_validate_from_records
from sempy.fabric._token_provider import SynapseTokenProvider as SynapseTokenProvider
from uuid import UUID

def list_dataflows(workspace: str | UUID | None = None) -> pd.DataFrame:
    """
    List all the Power BI dataflows.

    Please see `Dataflows - Get Dataflows <https://learn.microsoft.com/en-us/rest/api/power-bi/dataflows/get-dataflows>`_
    for more details.

    Parameters
    ----------
    workspace : str or uuid.UUID, default=None
        The Fabric workspace name or UUID object containing the workspace ID. Defaults to None which resolves to the workspace of the attached lakehouse
        or if no lakehouse attached, resolves to the workspace of the notebook.

    Returns
    =======
    pandas.DataFrame
        DataFrame with one row per data flow.
    """
def list_dataflow_storage_accounts() -> pd.DataFrame:
    """
    List a list of dataflow storage accounts that the user has access to.

    Please see `Dataflow Storage Accounts - Get Dataflow Storage Accounts <https://learn.microsoft.com/en-us/rest/api/power-bi/dataflow-storage-accounts/get-dataflow-storage-accounts>`_
    for more details.

    Returns
    =======
    pandas.DataFrame
        DataFrame with one row per dataflow storage account.
    """
