import pandas as pd
from sempy._utils._log import log as log
from sempy.fabric._flat import evaluate_dax as evaluate_dax
from sempy.fabric._utils import collection_to_dataframe as collection_to_dataframe, dotnet_to_pandas_date as dotnet_to_pandas_date
from uuid import UUID

def list_partitions(dataset: str | UUID, table: str | None = None, extended: bool | None = False, additional_xmla_properties: str | list[str] | None = None, workspace: str | UUID | None = None) -> pd.DataFrame:
    """
    List all partitions in a dataset.

    Parameters
    ----------
    dataset : str or uuid.UUID
        Name or UUID of the dataset.
    table : str, default=None
        Name of the table.
    extended : bool, default=False
        Fetches extended column information.
    additional_xmla_properties : str or List[str], default=None
        Additional XMLA `partition <https://learn.microsoft.com/en-us/dotnet/api/microsoft.analysisservices.tabular.partition?view=analysisservices-dotnet>`_
        properties to include in the returned dataframe.
        Use Parent to navigate to the parent level.
    workspace : str or uuid.UUID, default=None
        The Fabric workspace name or UUID object containing the workspace ID.
        Defaults to None which resolves to the workspace of the attached lakehouse
        or if no lakehouse attached, resolves to the workspace of the notebook.

    Returns
    -------
    pandas.DataFrame
        Dataframe listing the partitions.
    """
