import datetime
import graphviz
import pandas as pd
from sempy._utils._log import log as log, log_error as log_error, log_tables as log_tables
from sempy._utils._pandas_utils import rename_and_validate_from_records as rename_and_validate_from_records
from sempy.fabric._client import DatasetRestClient as DatasetRestClient, DatasetXmlaClient as DatasetXmlaClient
from sempy.fabric._client._connection_mode import ConnectionMode as ConnectionMode, parse_connection_mode as parse_connection_mode
from sempy.fabric._client._refresh_execution_details import RefreshExecutionDetails as RefreshExecutionDetails
from sempy.fabric._dataframe._fabric_dataframe import FabricDataFrame as FabricDataFrame
from sempy.fabric._token_provider import SynapseTokenProvider as SynapseTokenProvider
from sempy.fabric._trace._trace import Trace as Trace
from sempy.fabric._trace._trace_connection import TraceConnection as TraceConnection
from sempy.fabric._utils import collection_to_dataframe as collection_to_dataframe, dotnet_to_pandas_date as dotnet_to_pandas_date, is_valid_uuid as is_valid_uuid
from sempy.relationships import plot_relationship_metadata as plot_relationship_metadata
from typing import Literal
from uuid import UUID

def execute_tmsl(script: dict | str, refresh_tom_cache: bool = True, workspace: str | UUID | None = None):
    """
    Execute TMSL script.

    Parameters
    ----------
    script : Dict or str
        The TMSL script json.
    refresh_tom_cache : bool, default=True
        Whether or not to refresh the dataset after executing the TMSL script.
    workspace : str or uuid.UUID, default=None
        The Fabric workspace name or UUID object containing the workspace ID.
        Defaults to None which resolves to the workspace of the attached lakehouse
        or if no lakehouse attached, resolves to the workspace of the notebook.
    """
def refresh_tom_cache(workspace: str | UUID | None = None):
    """
    Refresh TOM cache in the notebook kernel.

    Parameters
    ----------
    workspace : str or uuid.UUID, default=None
        The Fabric workspace name or UUID object containing the workspace ID.
        Defaults to None which resolves to the workspace of the attached lakehouse
        or if no lakehouse attached, resolves to the workspace of the notebook.
    """
def get_roles(dataset: str | UUID, include_members: bool = False, additional_xmla_properties: str | list[str] | None = None, workspace: str | UUID | None = None) -> pd.DataFrame:
    """
    Retrieve all roles associated with the dataset.

    Parameters
    ----------
    dataset : str or uuid.UUID
        Name or UUID of the dataset.
    include_members : bool, default=False
        Whether or not to include members for each role.
    additional_xmla_properties : str or List[str], default=None
        Additional XMLA `role <https://learn.microsoft.com/en-us/dotnet/api/microsoft.analysisservices.tabular.role?view=analysisservices-dotnet>`_
        properties to include in the returned dataframe.
    workspace : str or uuid.UUID, default=None
        The Fabric workspace name or UUID object containing the workspace ID.
        Defaults to None which resolves to the workspace of the attached lakehouse
        or if no lakehouse attached, resolves to the workspace of the notebook.

    Returns
    -------
    pandas.DataFrame
        Dataframe listing roles and with their attributes.
    """
def get_row_level_security_permissions(dataset: str | UUID, additional_xmla_properties: str | list[str] | None = None, workspace: str | UUID | None = None) -> pd.DataFrame:
    """
    Retrieve row level security permissions for a dataset.

    Parameters
    ----------
    dataset : str or uuid.UUID
        Name or UUID of the dataset.
    additional_xmla_properties : str or List[str], default=None
        Additional XMLA `tablepermission <https://learn.microsoft.com/en-us/dotnet/api/microsoft.analysisservices.tabular.tablepermission?view=analysisservices-dotnet>`_
        properties to include in the returned dataframe.
    workspace : str or uuid.UUID, default=None
        The Fabric workspace name or UUID object containing the workspace ID.
        Defaults to None which resolves to the workspace of the attached lakehouse
        or if no lakehouse attached, resolves to the workspace of the notebook.

    Returns
    -------
    pandas.DataFrame
        Dataframe listing tables and row filter expressions (DAX) for the dataset.
    """
def list_datasets(workspace: str | UUID | None = None, mode: str = 'xmla', additional_xmla_properties: str | list[str] | None = None) -> pd.DataFrame:
    '''
    List datasets in a `Fabric workspace <https://learn.microsoft.com/en-us/fabric/get-started/workspaces>`_.

    Parameters
    ----------
    workspace : str or uuid.UUID, default=None
        The Fabric workspace name or UUID object containing the workspace ID.
        Defaults to None which resolves to the workspace of the attached lakehouse
        or if no lakehouse attached, resolves to the workspace of the notebook.
    mode : str, default="xmla"
        Whether to use the XMLA "xmla" or REST API "rest".
        See `REST docs <https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/get-datasets>`_ for returned fields.
    additional_xmla_properties : str or List[str], default=None
        Additional XMLA `model <https://learn.microsoft.com/en-us/dotnet/api/microsoft.analysisservices.tabular.model?view=analysisservices-dotnet>`_
        properties to include in the returned dataframe.

    Returns
    -------
    pandas.DataFrame
        Dataframe listing databases and their attributes.
    '''
def list_measures(dataset: str | UUID, additional_xmla_properties: str | list[str] | None = None, workspace: str | UUID | None = None) -> pd.DataFrame:
    """
    Retrieve all measures associated with the given dataset.

    Parameters
    ----------
    dataset : str or uuid.UUID
        Name or UUID of the dataset.
    additional_xmla_properties : str or List[str], default=None
        Additional XMLA `measure <https://learn.microsoft.com/en-us/dotnet/api/microsoft.analysisservices.tabular.measure?view=analysisservices-dotnet>`_
        properties to include in the returned dataframe.
    workspace : str or uuid.UUID, default=None
        The Fabric workspace name or UUID object containing the workspace ID.
        Defaults to None which resolves to the workspace of the attached lakehouse
        or if no lakehouse attached, resolves to the workspace of the notebook.

    Returns
    -------
    pandas.DataFrame
        Dataframe listing measures and their attributes.
    """
def refresh_dataset(dataset: str | UUID, workspace: str | UUID | None = None, refresh_type: str = 'automatic', max_parallelism: int = 10, commit_mode: str = 'transactional', retry_count: int = 0, objects: list | None = None, apply_refresh_policy: bool = True, effective_date: datetime.date = ..., verbose: int = 0) -> str:
    '''
    Refresh data associated with the given dataset.

    For detailed documentation on the implementation see
    `Enhanced refresh with the Power BI REST API <https://learn.microsoft.com/en-us/power-bi/connect-data/asynchronous-refresh>`_.

    Parameters
    ----------
    dataset : str or uuid.UUID
        Name or UUID of the dataset.
    workspace : str or uuid.UUID, default=None
        The Fabric workspace name or UUID object containing the workspace ID.
        Defaults to None which resolves to the workspace of the attached lakehouse
        or if no lakehouse attached, resolves to the workspace of the notebook.
    refresh_type : str, default="automatic"
        The type of processing to perform. Types align with the TMSL refresh command types: full,
        clearValues, calculate, dataOnly, automatic, and defragment. The add type isn\'t supported.
        Defaults to "automatic".
    max_parallelism : int, default=10
        Determines the maximum number of threads that can run the processing commands in parallel.
        This value aligns with the MaxParallelism property that can be set in the TMSL Sequence
        command or by using other methods. Defaults to 10.
    commit_mode : str, default="transactional"
        Determines whether to commit objects in batches or only when complete.
        Modes are "transactional" and "partialBatch". Defaults to "transactional".
    retry_count : int, default=0
        Number of times the operation retries before failing. Defaults to 0.
    objects : List, default=None
        A list of objects to process. Each object includes table when processing an entire table,
        or table and partition when processing a partition. If no objects are specified,
        the entire dataset refreshes. Pass output of json.dumps of a structure that specifies the
        objects that you want to refresh. For example, this is to refresh "DimCustomer1" partition
        of table "DimCustomer" and complete table "DimDate"::

            [
                {
                    "table": "DimCustomer",
                    "partition": "DimCustomer1"
                },
                {
                    "table": "DimDate"
                }
            ]

    apply_refresh_policy : bool, default=True
        If an incremental refresh policy is defined, determines whether to apply the policy.
        Modes are true or false. If the policy isn\'t applied, the full process leaves partition
        definitions unchanged, and fully refreshes all partitions in the table. If commitMode is
        transactional, applyRefreshPolicy can be true or false. If commitMode is partialBatch,
        applyRefreshPolicy of true isn\'t supported, and applyRefreshPolicy must be set to false.
    effective_date : datetime.date, default=datetime.date.today()
        If an incremental refresh policy is applied, the effectiveDate parameter overrides the current date.
    verbose : int, default=0
        If set to non-zero, extensive log output is printed.

    Returns
    -------
    str
        The refresh request id.
    '''
def list_refresh_requests(dataset: str | UUID, workspace: str | UUID | None = None, top_n: int | None = None) -> pd.DataFrame:
    """
    Poll the status or refresh requests for a given dataset using Enhanced refresh with the Power BI REST API.

    See details in: `PBI Documentation <https://learn.microsoft.com/en-us/power-bi/connect-data/asynchronous-refresh>`_

    Parameters
    ----------
    dataset : str or uuid.UUID
        Name or UUID of the dataset.
    workspace : str or uuid.UUID, default=None
        The Fabric workspace name or UUID object containing the workspace ID.
        Defaults to None which resolves to the workspace of the attached lakehouse
        or if no lakehouse attached, resolves to the workspace of the notebook.
    top_n : int, default = None
        Limit the number of refresh operations returned.

    Returns
    -------
    pandas.DataFrame:
        Dataframe with statuses of refresh request retrieved based on the passed parameters.
    """
def get_refresh_execution_details(dataset: str | UUID, refresh_request_id: str | UUID, workspace: str | UUID | None = None) -> RefreshExecutionDetails:
    """
    Poll the status for a specific refresh requests using Enhanced refresh with the Power BI REST API.

    More details on the underlying implementation in `PBI Documentation <https://learn.microsoft.com/en-us/power-bi/connect-data/asynchronous-refresh>`_

    Parameters
    ----------
    dataset : str or uuid.UUID
        Name or UUID of the dataset.
    refresh_request_id : str or uuid.UUID
        Id of refresh request on which to check the status.
    workspace : str or uuid.UUID, default=None
        The Fabric workspace name or UUID object containing the workspace ID.
        Defaults to None which resolves to the workspace of the attached lakehouse
        or if no lakehouse attached, resolves to the workspace of the notebook.

    Returns
    -------
    RefreshExecutionDetails:
        RefreshExecutionDetails instance with statuses of refresh request retrieved based on the passed URL.
    """
def read_table(dataset: str | UUID, table: str, fully_qualified_columns: bool = False, num_rows: int | None = None, multiindex_hierarchies: bool = False, mode: Literal['xmla', 'rest', 'onelake'] = 'xmla', onelake_import_method: Literal['spark', 'pandas'] | None = None, workspace: str | UUID | None = None, verbose: int = 0) -> FabricDataFrame:
    '''
    Read a PowerBI table into a FabricDataFrame.

    Parameters
    ----------
    dataset : str or uuid.UUID
        Name or UUID of the dataset.
    table : str
        Name of the table to read.
    fully_qualified_columns : bool, default=False
        Whether or not to represent columns in their fully qualified form (TableName[ColumnName]).
    num_rows : int, default=None
        How many rows of the table to return. If None, all rows are returned.
    multiindex_hierarchies : bool, default=False
        Whether or not to convert existing `PowerBI Hierarchies <https://learn.microsoft.com/en-us/power-bi/create-reports/service-metrics-get-started-hierarchies>`_
        to pandas MultiIndex.
    mode : {"xmla", "rest", "onelake"}
        Whether to use the XMLA "xmla", REST API "rest", export of import datasets to Onelake "onelake" to retrieve the data.
    onelake_import_method : {"spark", "pandas"}, default=None
        The method to read from the onelake. Only be effective when the mode is "onelake". Use "spark" to read the table with spark API,
        "deltalake" with the deltalake API, or None with the proper method auto-selected based on the current runtime.
    workspace : str or uuid.UUID, default=None
        The Fabric workspace name or UUID object containing the workspace ID. Defaults to None which resolves to the workspace of the attached lakehouse
        or if no lakehouse attached, resolves to the workspace of the notebook.
    verbose : int, default=0
        Verbosity. 0 means no verbosity.

    Returns
    -------
    FabricDataFrame
        Dataframe for the given table name with metadata from the PowerBI model.
    '''
def get_tmsl(dataset: str | UUID, workspace: str | UUID | None = None) -> str:
    """
    Retrieve the Tabular Model Scripting Language (`TMSL <https://learn.microsoft.com/en-us/analysis-services/tmsl/tabular-model-scripting-language-tmsl-reference?view=asallproducts-allversions>`_) for a given dataset.

    Parameters
    ----------
    dataset : str or uuid.UUID
        Name or UUID of the dataset.
    workspace : str or uuid.UUID, default=None
        The Fabric workspace name or UUID object containing the workspace ID. Defaults to None which resolves to the workspace of the attached lakehouse
        or if no lakehouse attached, resolves to the workspace of the notebook.

    Returns
    -------
    str
        `TMSL <https://learn.microsoft.com/en-us/analysis-services/tmsl/tabular-model-scripting-language-tmsl-reference?view=asallproducts-allversions>`_ for the given dataset.
    """
def list_tables(dataset: str | UUID, include_columns: bool = False, include_partitions: bool = False, extended: bool = False, additional_xmla_properties: str | list[str] | None = None, workspace: str | UUID | None = None) -> pd.DataFrame:
    """
    List all tables in a dataset.

    Parameters
    ----------
    dataset : str or uuid.UUID
        Name or UUID of the dataset.
    include_columns : bool, default=False
        Whether or not to include column level information.
        Cannot be combined with include_partitions or extended.
    include_partitions : bool, default=False
        Whether or not to include partition level information.
        Cannot be combined with include_columns or extended.
    extended : bool, default False
        Fetches extended table information information.
        Cannot be combined with include_columns or include_partitions.
    additional_xmla_properties : str or List[str], default=None
        Additional XMLA `table <https://learn.microsoft.com/en-us/dotnet/api/microsoft.analysisservices.tabular.table?view=analysisservices-dotnet>`_
        properties to include in the returned dataframe.
    workspace : str or uuid.UUID, default=None
        The Fabric workspace name or UUID object containing the workspace ID.
        Defaults to None which resolves to the workspace of the attached lakehouse
        or if no lakehouse attached, resolves to the workspace of the notebook.

    Returns
    -------
    pandas.DataFrame
        Dataframe listing the tables and optional columns.
    """
def list_translations(dataset: str | UUID, additional_xmla_properties: str | list[str] | None = None, workspace: str | UUID | None = None) -> pd.DataFrame:
    """
    List all translations in a dataset.

    Parameters
    ----------
    dataset : str or uuid.UUID
        Name or UUID of the dataset.
    additional_xmla_properties : str or List[str], default=None
        Additional XMLA `tramslation <https://learn.microsoft.com/en-us/dotnet/api/microsoft.analysisservices.translation?view=analysisservices-dotnet>`_
        properties to include in the returned dataframe.
    workspace : str or uuid.UUID, default=None
        The Fabric workspace name or UUID object containing the workspace ID.
        Defaults to None which resolves to the workspace of the attached lakehouse
        or if no lakehouse attached, resolves to the workspace of the notebook.

    Returns
    -------
    pandas.DataFrame
        Dataframe listing the translations.
    """
def list_expressions(dataset: str | UUID, additional_xmla_properties: str | list[str] | None = None, workspace: str | UUID | None = None) -> pd.DataFrame:
    """
    List all expressions in a dataset.

    Parameters
    ----------
    dataset : str or uuid.UUID
        Name or UUID of the dataset.
    additional_xmla_properties : str or List[str], default=None
        Additional XMLA `expression <https://learn.microsoft.com/en-us/dotnet/api/microsoft.analysisservices.tabular.namedexpression?view=analysisservices-dotnet>`_
        properties to include in the returned dataframe.
    workspace : str or uuid.UUID, default=None
        The Fabric workspace name or UUID object containing the workspace ID.
        Defaults to None which resolves to the workspace of the attached lakehouse
        or if no lakehouse attached, resolves to the workspace of the notebook.

    Returns
    -------
    pandas.DataFrame
        Dataframe listing the expressions.
    """
def evaluate_measure(dataset: str | UUID, measure: str | list[str], groupby_columns: list[str] | None = None, filters: dict[str, list[str]] | None = None, fully_qualified_columns: bool | None = None, num_rows: int | None = None, use_xmla: bool = False, workspace: str | UUID | None = None, verbose: int = 0) -> FabricDataFrame:
    '''
    Compute `PowerBI measure <https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-measures>`_ for a given dataset.

    Parameters
    ----------
    dataset : str or uuid.UUID
        Name or UUID of the dataset.
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
        Whether to output columns in their fully qualified form (TableName[ColumnName] for dimensions).
        Measures are always represented without the table name.
        If None, the fully qualified form will only be used if there is a name conflict between columns from different tables.
    num_rows : int, default=None
        How many rows of the table to return. If None, all rows are returned.
    use_xmla : bool, default=False
        Whether or not to use `XMLA <https://learn.microsoft.com/en-us/analysis-services/xmla/xml-for-analysis-xmla-reference?view=asallproducts-allversions>`_
        as the backend for evaluation. When False, REST backend will be used.
    workspace : str or uuid.UUID, default=None
        The Fabric workspace name or UUID object containing the workspace ID.
        Defaults to None which resolves to the workspace of the attached lakehouse
        or if no lakehouse attached, resolves to the workspace of the notebook.
    verbose : int, default=0
        Verbosity. 0 means no verbosity.

    Returns
    -------
    FabricDataFrame
        :class:`~sempy.fabric.FabricDataFrame` holding the computed measure stratified by groupby columns.
    '''
def evaluate_dax(dataset: str | UUID, dax_string: str, workspace: str | UUID | None = None, verbose: int = 0, num_rows: int | None = None) -> FabricDataFrame:
    """
    Compute `DAX <https://learn.microsoft.com/en-us/dax/>`_ query for a given dataset.

    Parameters
    ----------
    dataset : str or uuid.UUID
        Name or UUID of the dataset.
    dax_string : str
        The DAX query.
    workspace : str or uuid.UUID, default=None
        The Fabric workspace name or UUID object containing the workspace ID.
        Defaults to None which resolves to the workspace of the attached lakehouse
        or if no lakehouse attached, resolves to the workspace of the notebook.
    verbose : int, default=0
        Verbosity. 0 means no verbosity.
    num_rows : int, default=None
        Maximum number of rows to read from the result. None means read all rows.

    Returns
    -------
    FabricDataFrame
        :class:`~sempy.fabric.FabricDataFrame` holding the result of the DAX query.
    """
def execute_xmla(dataset: str | UUID, xmla_command: str, workspace: str | UUID | None = None) -> int:
    """
    Execute XMLA command for a given dataset.

    e.g. `clear cache <https://learn.microsoft.com/en-us/analysis-services/instances/clear-the-analysis-services-caches?view=asallproducts-allversions>`_
    when optimizing DAX queries.

    Parameters
    ----------
    dataset : str or uuid.UUID
        Name or UUID of the dataset.
    xmla_command : str
        The XMLA command.
    workspace : str or uuid.UUID, default=None
        The Fabric workspace name or UUID object containing the workspace ID.
        Defaults to None which resolves to the workspace of the attached lakehouse
        or if no lakehouse attached, resolves to the workspace of the notebook.

    Returns
    -------
    int
        Number of rows affected.
    """
def plot_relationships(tables: dict[str, FabricDataFrame] | list[FabricDataFrame], include_columns: str = 'keys', missing_key_errors: str = 'raise', *, graph_attributes: dict | None = None) -> graphviz.Digraph:
    '''
    Visualize relationship dataframe with a graph.

    Parameters
    ----------
    tables : dict[str, sempy.fabric.FabricDataFrame] or list[sempy.fabric.FabricDataFrame]
        A dictionary that maps table names to the dataframes with table content.
        If a list of dataframes is provided, the function will try to infer the names from the
        session variables and if it cannot, it will use the positional index to describe them in
        the results.
        It needs to provided only when `include_columns` = \'all\' and it will be used
        for mapping table names from relationships to the dataframe columns.
    include_columns : str, default=\'keys\'
        One of \'keys\', \'all\', \'none\'. Indicates which columns should be included in the graph.
    missing_key_errors : str, default=\'raise\'
        One of \'raise\', \'warn\', \'ignore\'. Action to take when either table or column
        of the relationship is not found in the elements of the argument *tables*.
    graph_attributes : dict, default=None
        Attributes passed to graphviz. Note that all values need to be strings. Useful attributes are:

        - *rankdir*: "TB" (top-bottom) or "LR" (left-right)
        - *dpi*:  "100", "30", etc. (dots per inch)
        - *splines*: "ortho", "compound", "line", "curved", "spline" (line shape)

    Returns
    -------
    graphviz.Digraph
        Graph object containing all relationships.
        If include_attributes is true, attributes are represented as ports in the graph.
    '''
def list_relationship_violations(tables: dict[str, FabricDataFrame] | list[FabricDataFrame], missing_key_errors: str = 'raise', coverage_threshold: float = 1.0, n_keys: int = 10) -> pd.DataFrame:
    '''
    Validate if the content of tables matches relationships.

    Relationships are extracted from the metadata in FabricDataFrames.
    The function examines results of joins for provided relationships and
    searches for inconsistencies with the specified relationship multiplicity.

    Relationships from empty tables (dataframes) are assumed as valid.

    Parameters
    ----------
    tables : dict[str, sempy.fabric.FabricDataFrame] or list[sempy.fabric.FabricDataFrame]
        A dictionary that maps table names to the dataframes with table content.
        If a list of dataframes is provided, the function will try to infer the names from the
        session variables and if it cannot, it will use the positional index to describe them in
        the results.
    missing_key_errors : str, default=\'raise\'
        One of \'raise\', \'warn\', \'ignore\'. Action to take when either table or column
        of the relationship is not found in the elements of the argument *tables*.
    coverage_threshold : float, default=1.0
        Fraction of rows in the "from" part that need to join in inner join.
    n_keys : int, default=10
        Number of missing keys to report. Random collection can be reported.

    Returns
    -------
    pandas.DataFrame
        Dataframe with relationships, error type and error message.
        If there are no violations, returns an empty DataFrame.
    '''
def resolve_workspace_id(workspace: str | UUID | None = None) -> str:
    """
    Resolve the workspace name or ID to the workspace UUID.

    Parameters
    ----------
    workspace : str or uuid.UUID, default=None
        The Fabric workspace name or UUID object containing the workspace ID. Defaults to None
        which resolves to the workspace of the attached lakehouse
        or if no lakehouse attached, resolves to the workspace of the notebook.

    Returns
    -------
    uuid.UUID
        The workspace UUID.
    """
def resolve_workspace_name(workspace: str | UUID | None = None) -> str:
    """
    Resolve the workspace name or ID to the workspace name.

    Parameters
    ----------
    workspace : str or uuid.UUID, default=None
        The Fabric workspace name or UUID object containing the workspace ID. Defaults to None
        which resolves to the workspace of the attached lakehouse
        or if no lakehouse attached, resolves to the workspace of the notebook.

    Returns
    -------
    str
        The workspace name.
    """
def resolve_dataset_id(dataset_name: str, workspace: str | UUID | None = None) -> str:
    """
    Resolve the dataset ID by name in the specified workspace.

    Parameters
    ----------
    dataset_name : str
        Name of the dataset to be resolved.
    workspace : str or uuid.UUID, default=None
        The Fabric workspace name or UUID object containing the workspace ID. Defaults to None
        which resolves to the workspace of the attached lakehouse
        or if no lakehouse attached, resolves to the workspace of the notebook.

    Returns
    -------
    str
        The ID of the specified dataset.
    """
def resolve_dataset_name(dataset_id: str | UUID, workspace: str | UUID | None = None) -> str:
    """
    Resolve the dataset name by ID in the specified workspace.

    Parameters
    ----------
    dataset_id : str or uuid.UUID
        Dataset ID or UUID object containing the dataset ID to be resolved.
    workspace : str or uuid.UUID, default=None
        The Fabric workspace name or UUID object containing the workspace ID. Defaults to None
        which resolves to the workspace of the attached lakehouse
        or if no lakehouse attached, resolves to the workspace of the notebook.

    Returns
    -------
    str
        The name of the specified dataset.
    """
def resolve_item_id(item_name: str, type: str | None = None, workspace: str | UUID | None = None) -> str:
    """
    Resolve the item ID by name in the specified workspace.

    The item type can be given to limit the search. Otherwise the function will search for all items in the workspace.

    Please see `ItemTypes <https://learn.microsoft.com/en-us/rest/api/fabric/core/items/create-item?tabs=HTTP#itemtype>_`
    for all supported item types.

    Parameters
    ----------
    item_name : str
        Name of the item to be resolved.
    type : str, default = None
        Type of the item to be resolved.
    workspace : str or uuid.UUID, default=None
        The Fabric workspace name or UUID object containing the workspace ID. Defaults to None
        which resolves to the workspace of the attached lakehouse
        or if no lakehouse attached, resolves to the workspace of the notebook.

    Returns
    -------
    str
        The item ID of the specified item.
    """
def resolve_item_name(item_id: str | UUID, type: str | None = None, workspace: str | UUID | None = None) -> str:
    """
    Resolve the item name by ID in the specified workspace.

    The item type can be given to limit the search. Otherwise the function will search for all items in the workspace.

    Please see `ItemTypes <https://learn.microsoft.com/en-us/rest/api/fabric/core/items/create-item?tabs=HTTP#itemtype>_`
    for all supported item types.

    Parameters
    ----------
    item_id : str or uuid.UUID
        Item ID or UUID object containing the item ID to be resolved.
    type : str, default = None
        Type of the item to be resolved.
    workspace : str or uuid.UUID, default=None
        The Fabric workspace name or UUID object containing the workspace ID. Defaults to None
        which resolves to the workspace of the attached lakehouse
        or if no lakehouse attached, resolves to the workspace of the notebook.

    Returns
    -------
    str
        The item ID of the specified item.
    """
def create_trace_connection(dataset: str | UUID, workspace: str | UUID | None = None) -> TraceConnection:
    """
    Create a TraceConnection to the server specified by the dataset.

    NOTE: This feature is only intended for exploratory use. Due to the asynchronous communication required between the
    Microsoft Analysis Services (AS) Server and other AS clients, trace events are registered on a best-effort basis where timings are
    dependent on server load.

    Parameters
    ----------
    dataset : str or uuid.UUID
        Name or UUID of the dataset to list traces on.
    workspace : str or uuid.UUID, default=None
        The Fabric workspace name or UUID object containing the workspace ID. Defaults to None
        which resolves to the workspace of the attached lakehouse
        or if no lakehouse attached, resolves to the workspace of the notebook.

    Returns
    -------
    TraceConnection
        Server connected to specified dataset.
    """
def list_workspaces(filter: str | None = None, top: int | None = None, skip: int | None = None) -> pd.DataFrame:
    '''
    Return a list of workspaces the user has access to.

    Parameters
    ----------
    filter : str, default=None
        OData filter expression. For example, to filter by name, use "name eq \'My workspace\'".
    top : int, default=None
        Maximum number of workspaces to return.
    skip : int, default=None
        Number of workspaces to skip.

    Returns
    -------
    pandas.DataFrame
        DataFrame with one row per workspace.
    '''
def list_capacities() -> pd.DataFrame:
    """
    Return a list of capacities that the principal has access to (`details <https://learn.microsoft.com/en-us/rest/api/fabric/core/capacities/list-capacities>`_).

    Returns
    -------
    pandas.DataFrame
        Dataframe listing the capacities.
    """
def list_reports(workspace: str | UUID | None = None) -> pd.DataFrame:
    """
    Return a list of reports in the specified workspace.

    Parameters
    ----------
    workspace : str or uuid.UUID, default=None
        The Fabric workspace name or UUID object containing the workspace ID. Defaults to None
        which resolves to the workspace of the attached lakehouse
        or if no lakehouse attached, resolves to the workspace of the notebook.

    Returns
    -------
    pandas.DataFrame
        DataFrame with one row per report.
    """
def list_items(type: str | None = None, workspace: str | UUID | None = None) -> pd.DataFrame:
    """
    Return a list of items in the specified workspace.

    Parameters
    ----------
    type : str, default=None
        Filter the list of items by the type specified (see `valid types <https://learn.microsoft.com/en-us/rest/api/fabric/core/items/list-items?tabs=HTTP#itemtype>`_).
    workspace : str or uuid.UUID, default=None
        The Fabric workspace name or UUID object containing the workspace ID. Defaults to None
        which resolves to the workspace of the attached lakehouse
        or if no lakehouse attached, resolves to the workspace of the notebook.

    Returns
    -------
    pandas.DataFrame
        DataFrame with one row per artifact.
    """
def create_workspace(display_name: str, capacity_id: str | None = None, description: str | None = None) -> str:
    """
    Create a workspace.

    Parameters
    ----------
    display_name : str
        The display name of the workspace.
    capacity_id : str, default=None
        The optional capacity id.
    description : str, default=None
        The optional description of the workspace.

    Returns
    -------
    str
        The id of workspace.
    """
def create_lakehouse(display_name: str, description: str | None = None, max_attempts: int = 10, workspace: str | UUID | None = None) -> str:
    """
    Create a lakehouse in the specified workspace.

    Parameters
    ----------
    display_name : str
        The display name of the lakehouse.
    description : str, default=None
        The optional description of the lakehouse.
    max_attempts : int, default=10
        Maximum number of retries to wait for creation of the notebook.
    workspace : str or uuid.UUID, default=None
        The Fabric workspace name or UUID object containing the workspace ID. Defaults to None
        which resolves to the workspace of the attached lakehouse
        or if no lakehouse attached, resolves to the workspace of the notebook.

    Returns
    -------
    str
        The id of lakehouse.
    """
def delete_item(item_id: str, workspace: str | UUID | None = None):
    """
    Delete the item in the specified workspace.

    Parameters
    ----------
    item_id : str
        The id of the item.
    workspace : str or uuid.UUID, default=None
        The Fabric workspace name or UUID object containing the workspace ID. Defaults to None
        which resolves to the workspace of the attached lakehouse
        or if no lakehouse attached, resolves to the workspace of the notebook.
    """
def delete_workspace(workspace: str | UUID):
    """
    Delete the specified workspace.

    Parameters
    ----------
    workspace : str or uuid.UUID
        The Fabric workspace name or UUID object containing the workspace ID.
    """
def create_notebook(display_name: str, description: str | None = None, content: str | dict | None = None, default_lakehouse: str | UUID | None = None, default_lakehouse_workspace: str | UUID | None = None, max_attempts: int = 10, workspace: str | UUID | None = None) -> str:
    """
    Create a notebook in the specified workspace.

    Parameters
    ----------
    display_name : str
        The display name of the lakehouse.
    description : str, default=None
        The optional description of the lakehouse.
    content : str or dict, default=None
        The optional notebook content (JSON).
    default_lakehouse : str or uuid.UUID, default=None
        The optional lakehouse name or UUID object to attach to the new notebook.
    default_lakehouse_workspace : str or uuid.UUID, default=None
        The Fabric workspace name or UUID object containing the workspace ID the lakehouse is in.
        If None, the workspace specified for the notebook is used.
    max_attempts : int, default=10
        Maximum number of retries to wait for creation of the notebook.
    workspace : str or uuid.UUID, default=None
        The Fabric workspace name or UUID object containing the workspace ID. Defaults to None
        which resolves to the workspace of the attached lakehouse
        or if no lakehouse attached, resolves to the workspace of the notebook.

    Returns
    -------
    str
        The notebook id.
    """
def run_notebook_job(notebook_id: str, max_attempts: int = 10, workspace: str | UUID | None = None) -> str:
    """
    Run a notebook job and wait for it to complete.

    Parameters
    ----------
    notebook_id : str
        The id of the notebook to run.
    max_attempts : int, default=10
        Maximum number of retries to wait for creation of the notebook.
    workspace : str or uuid.UUID, default=None
        The Fabric workspace name or UUID object containing the workspace ID. Defaults to None
        which resolves to the workspace of the attached lakehouse
        or if no lakehouse attached, resolves to the workspace of the notebook.

    Returns
    -------
    str
        The job id.
    """
def create_tom_server(readonly: bool = True, workspace: str | UUID | None = None) -> object:
    """
    Create a TOM server for the specified workspace.

    Note that not all properties and methods of the `Tabular Object Model (TOM) <https://learn.microsoft.com/en-us/dotnet/api/microsoft.analysisservices.tabular.server?view=analysisservices-dotnet>`_
    are supported due to limitation when bridging Python to .NET.

    If changes are made to models, make sure to call SaveChanges() on the model object and invoke refresh_tom_cache().

    Parameters
    ----------
    readonly : bool, default=True
        Whether to create a read-only server.
    workspace : str or uuid.UUID, default=None
        The Fabric workspace name or UUID object containing the workspace ID. Defaults to None
        which resolves to the workspace of the attached lakehouse
        or if no lakehouse attached, resolves to the workspace of the notebook.

    Returns
    -------
    object
        The TOM server. See `Microsoft.AnalysisServices.Tabular.Server <https://learn.microsoft.com/en-us/dotnet/api/microsoft.analysisservices.tabular.server>`__.
    """
