import pandas as pd
from sempy._utils._pandas_utils import rename_and_validate_from_records as rename_and_validate_from_records
from sempy.fabric._token_provider import SynapseTokenProvider as SynapseTokenProvider

def list_apps() -> pd.DataFrame:
    """
    List all the Power BI apps.

    Returns
    =======
    pandas.DataFrame
        DataFrame with one row per app.
    """
