import abc
import pandas as pd
from _typeshed import Incomplete
from sempy.fabric._client import WorkspaceClient as WorkspaceClient
from sempy.fabric._dataframe._fabric_dataframe import FabricDataFrame as FabricDataFrame
from sempy.fabric._metadatakeys import MetadataKeys as MetadataKeys
from sempy.fabric._token_provider import SynapseTokenProvider as SynapseTokenProvider, TokenProvider as TokenProvider
from sempy.fabric._utils import dotnet_to_pandas_date as dotnet_to_pandas_date, is_valid_uuid as is_valid_uuid, to_multiplicity as to_multiplicity
from sempy.fabric.exceptions import DatasetNotFoundException as DatasetNotFoundException, WorkspaceNotFoundException as WorkspaceNotFoundException
from typing import Any
from uuid import UUID

class WorkspaceDatasetResolver:
    """
    Resolves workspace and dataset names to their respective IDs and makes sure to avoid unnecessary API calls.
    """
    def __init__(self, workspace: str | UUID | WorkspaceClient, dataset: str | UUID, token_provider: TokenProvider) -> None: ...
    @property
    def workspace_client(self): ...
    @property
    def rest_api(self): ...
    @property
    def workspace_name_without_explicit_resolution(self) -> str | None: ...
    @property
    def workspace_name(self) -> str: ...
    @property
    def workspace_id_without_explicit_resolution(self) -> str | None: ...
    @property
    def workspace_id(self) -> str: ...
    @property
    def dataset_name_without_explicit_resolution(self) -> str | None: ...
    @property
    def dataset_name(self): ...
    @property
    def dataset_id(self): ...

class BaseDatasetClient(metaclass=abc.ABCMeta):
    """
    Client for access to Power BI data in a specific dataset (database).

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
    token_provider: Incomplete
    resolver: Incomplete
    def __init__(self, workspace: str | UUID | WorkspaceClient, dataset: str | UUID, token_provider: TokenProvider | None = None) -> None: ...
    def evaluate_dax(self, query: str, verbose: int = 0, num_rows: int | None = None) -> FabricDataFrame:
        """
        Retrieve results of DAX query as a FabricDataFrame.

        Parameters
        ----------
        query : str
            DAX query.
        verbose : int, default=0
            Verbosity. 0 means no verbosity.
        num_rows : int, default=-1
            Maximum number of rows to read from the result. -1 means read all rows.

        Returns
        -------
        FabricDataFrame
            FabricDataFrame converted from the results of a DAX query.
        """
    def evaluate_measure(self, measure: str | list[str], groupby_columns: list[str] | None = None, filters: dict[str, list[str]] | None = None, fully_qualified_columns: bool | None = None, num_rows: int | None = None, verbose: int = 0) -> FabricDataFrame:
        '''
        Compute PowerBI metric for a given dataset.

        Parameters
        ----------
        measure : str or list of str
            Name of the measure, or list of measures to compute.
        groupby_columns : list, default=None
            List of columns in a fully qualified form e.g. "TableName[ColumnName]" or "\'Table Name\'[Column Name]".
        filters : dict, default=None
            Dictionary containing a list of column values to filter the output by, where
            the key is a column reference, which must be fully qualified with the table name.
            Currently only supports the "in" filter. For example, to specify that in the "State" table
            the "Region" column can only be "East" or "Central" and that the "State" column
            can only be "WA" or "CA"::

                {
                    "State[Region]":    ["East", "Central"],
                    "State[State]":     ["WA", "CA"]
                }

        fully_qualified_columns : bool, default=None
            Whether to output columns in their fully qualified form ("TableName[ColumnName]" for dimensions).
            If None, the fully qualified form will only be used if there is a name conflict between columns from different tables.
        num_rows : int, default=None
            How many rows of the table to return. If None, all rows are returned.
        verbose : int, default=0
            Verbosity. 0 means no verbosity.

        Returns
        -------
        FabricDataFrame
            :class:`~sempy.fabric.FabricDataFrame` holding the computed measure stratified by groupby columns.
        '''
    def read_table(self, table_name: str, fully_qualified_columns: bool = False, num_rows: int | None = None, multiindex_hierarchies: bool = False, exclude_internal: bool = True, verbose: int = 0) -> FabricDataFrame:
        """
        Read specified PBI Dataset tables into FabricDataFrames with populated metadata.

        Parameters
        ----------
        table_name : str
            Name of table from dataset.
        fully_qualified_columns : bool, default=False
            Whether or not to represent columns in their fully qualified form (TableName[ColumnName]).
        num_rows : int, default=None
            How many rows of the table to return. If None, all rows are returned.
        multiindex_hierarchies : bool, default=False
            Whether or not to convert existing `PowerBI Hierarchies <https://learn.microsoft.com/en-us/power-bi/create-reports/service-metrics-get-started-hierarchies>`_
            to pandas MultiIndex.
        exclude_internal : bool, default=True
            Whether internal PowerBI columns should be excluded during the load operation.
        verbose : int
            Verbosity. 0 means no verbosity.

        Returns
        -------
        FabricDataFrame
            DataFrame with metadata from the PBI model.
        """
    def resolve_metadata(self, columns: pd.Index, verbose: int = 0) -> dict[str, Any]:
        '''
        Resolve column names to their Power BI metadata.

        Parameters
        ----------
        columns : list of str
            List of column names to resolve. Column names can be in any of the following formats:
            - Column name only: "Column Name"
            - Unquoted table name + column name (if no spaces in table name): "TableName[Column Name]"
            - Quoted table name + column name: "\'Table Name\'[Column Name]"
        verbose : int
            Verbosity. 0 means no verbosity.

        Returns
        -------
        Dict of str
            Dictionary containing mapping of column name to its metadata.
        '''
