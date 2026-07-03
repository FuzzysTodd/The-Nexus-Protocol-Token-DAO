import pandas as pd
from sempy._utils._log import log as log
from sempy.fabric._utils import collection_to_dataframe as collection_to_dataframe
from uuid import UUID

def list_annotations(dataset: str | UUID, additional_xmla_properties: str | list[str] | None = None, workspace: str | UUID | None = None) -> pd.DataFrame:
    """
    List all annotations in a dataset.

    Parameters
    ----------
    dataset : str or uuid.UUID
        Name or UUID of the dataset.
    additional_xmla_properties : str or List[str], default=None
        Additional XMLA `annotation <https://learn.microsoft.com/en-us/dotnet/api/microsoft.analysisservices.tabular.annotation?view=analysisservices-dotnet>`_
        properties to include in the returned dataframe.
    workspace : str or uuid.UUID, default=None
        The Fabric workspace name or UUID object containing the workspace ID.
        Defaults to None which resolves to the workspace of the attached lakehouse
        or if no lakehouse attached, resolves to the workspace of the notebook.

    Returns
    -------
    pandas.DataFrame
        Dataframe listing all annotations.
    """
