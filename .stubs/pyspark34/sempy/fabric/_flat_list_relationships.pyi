import pandas as pd
from sempy._utils._log import log as log
from sempy.fabric._flat import evaluate_dax as evaluate_dax
from sempy.fabric._flat_list_columns import list_columns as list_columns
from sempy.fabric._utils import collection_to_dataframe as collection_to_dataframe, dotnet_to_pandas_date as dotnet_to_pandas_date, to_multiplicity as to_multiplicity
from uuid import UUID

def list_relationships(dataset: str | UUID, extended: bool | None = False, additional_xmla_properties: str | list[str] | None = None, calculate_missing_rows: bool | None = False, workspace: str | UUID | None = None) -> pd.DataFrame:
    """
    List all relationship found within the Power BI model.

    Parameters
    ----------
    dataset : str or uuid.UUID
        Name or UUID of the dataset.
    extended : bool, default=False
        Fetches extended column information.
    additional_xmla_properties : str or List[str], default=None
        Additional XMLA `relationship <https://learn.microsoft.com/en-us/dotnet/api/microsoft.analysisservices.tabular.relationship?view=analysisservices-dotnet>`_
        properties to include in the returned dataframe.
        Use Parent to navigate to the parent level.
    calculate_missing_rows : bool, default=False
        Calculate the number of missing rows in the relationship.
    workspace : str or uuid.UUID, default=None
        The Fabric workspace name or UUID object containing the workspace ID. Defaults to None
        which resolves to the workspace of the attached lakehouse
        or if no lakehouse attached, resolves to the workspace of the notebook.

    Returns
    -------
    pandas.DataFrame
        DataFrame with one row per relationship.
    """
