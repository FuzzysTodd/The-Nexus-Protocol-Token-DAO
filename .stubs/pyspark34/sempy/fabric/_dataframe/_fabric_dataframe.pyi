import deltalake
import graphviz
import pandas as pd
import pyarrow as pa
from numpy import ndarray
from pyspark.sql.types import StructType
from sempy._utils._log import log as log
from sempy.dependencies._stats import DataFrameDependencyStats as DataFrameDependencyStats
from sempy.fabric._utils import SparkConfigTemporarily as SparkConfigTemporarily, try_import as try_import
from sempy.fabric.exceptions import DatasetNotFoundException as DatasetNotFoundException, WorkspaceNotFoundException as WorkspaceNotFoundException
from sempy.functions import _SDataFrame
from typing import Any, Iterable, Literal
from uuid import UUID

class FabricDataFrame(_SDataFrame):
    """
    A dataframe for storage and propogation of PowerBI metadata.

    The elements of :attr:`~sempy.fabric.FabricDataFrame.column_metadata` can contain the following keys:

        - ``table``: table name in originating dataset
        - ``column``: column name
        - ``dataset``: originating dataset name
        - ``workspace_id``: string form of workspace GUID
        - ``workspace_name``: friendly name of originating workspace
        - ``description``: description of column (if one is present)
        - ``data_type``: `PowerBI data type <https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-data-types>`_ for this column
        - ``data_category``: `PowerBI data category <https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-data-categorization>`_ for this column
        - ``alignment``: `PowerBI visual alignment <https://learn.microsoft.com/en-us/dotnet/api/microsoft.analysisservices.tabular.alignment?view=analysisservices-dotnet>`_ for this column

    Parameters
    ----------
    data : numpy.ndarray, typing.Iterable, dict or pandas.DataFrame, default=None
        Dict can contain Series, arrays, constants, dataclass or list-like objects. If
        data is a dict, column order follows insertion-order. If a dict contains Series
        which have an index defined, it is aligned by its index. This alignment also
        occurs if data is a Series or a DataFrame itself. Alignment is done on
        Series/DataFrame inputs.

        If data is a list of dicts, column order follows insertion-order.
    *args : list
        Remaining arguments to be passed to standard pandas constructor.
    column_metadata : dict, default=None
        Information about dataframe columns to be stored and propogated.
    dataset : str or uuid.UUID, default=None
        Name or UUID of the dataset to list the measures for.
    workspace : str or uuid.UUID, default=None
        The Fabric workspace name or UUID object containing the workspace ID. Defaults to None which resolves to the workspace of the attached lakehouse
        or if no lakehouse attached, resolves to the workspace of the notebook.
    verbose : int, default=0
        Verbosity. 0 means no verbosity.
    **kwargs : dict
        Remaining kwargs to be passed to standard pandas constructor.
    """
    def __init__(self, data: ndarray | Iterable | dict | pd.DataFrame | None = None, *args: Any, column_metadata: dict[str, Any] | None = None, dataset: str | UUID | None = None, workspace: str | UUID | None = None, verbose: int = 0, **kwargs: Any) -> None: ...
    def add_measure(self, *measures: list[str], dataset: str | UUID | None = None, workspace: str | UUID | None = None, use_xmla: bool = False, verbose: int = 0) -> FabricDataFrame:
        """
        Join measures from the same dataset to the dataframe.

        Parameters
        ----------
        *measures : list[str]
            List of measure names to join.
        dataset : str or uuid.UUID, default=None
            Name or UUID of the dataset to list the measures for. If not provided it will be auto-resolved from column metadata.
        workspace : str or uuid.UUID, default=None
            The Fabric workspace name or UUID object containing the workspace ID. Defaults to None which resolves to the workspace of the attached lakehouse
            or if no lakehouse attached, resolves to the workspace of the notebook.
        use_xmla : bool, default=False
            Whether or not to use `XMLA <https://learn.microsoft.com/en-us/analysis-services/xmla/xml-for-analysis-xmla-reference?view=asallproducts-allversions>`_ as the backend for the client.
            If there are any issues using the default Client, make this argument True.
        verbose : int, default=0
            Verbosity. 0 means no verbosity.

        Returns
        -------
        FabricDataFrame
            A new FabricDataFrame with the joined measures.
        """
    def find_dependencies(self, dropna: bool = False, threshold: float = 0.01, verbose: int = 0) -> FabricDataFrame:
        """
        Detect functional dependencies between the columns of a dataframe.

        Columns that map 1:1 will be represented as a list.

        Uses a threshold on conditional entropy to discover approximate functional dependencies.
        Low conditional entropy means strong dependence (i.e. conditional entropy of 0 means complete dependence).
        Therefore a lower threshold is more selective.

        The function tries to prune the potential dependencies by removing transitive edges.

        When dropna=True is specified, rows that have a NaN in either columns are eliminated from evaluation.
        This may result in dependencies being non-transitive, as in the following example. Even though A maps 1:1
        with B and B maps 1:1 with C, A does not map 1:1 with C, because comparison of A and C includes
        additional NaN rows that are excluded when comparing A and C with B:

            ===  ===  ===
             A    B    C
            ===  ===  ===
             1    1    1
             1    1    1
             1   NaN   9
             2   NaN   2
             2    2    2
            ===  ===  ===

        In some dropna=True cases the dependency chain can form cycles. In the following example, NaN values mask
        the pairwise mappings in such a way that A->B, B->C, C->A:

            ===  ===  ===
             A    B    C
            ===  ===  ===
             1    1   NaN
             2    1   NaN
            NaN   1    1
            NaN   2    1
             1   NaN   1
             1   NaN   2
            ===  ===  ===

        Parameters
        ----------
        dropna : bool, default=False
            Ignore rows where either column is NaN in dependency calculations.
        threshold : float, default=0.01
            Threshold on conditional entropy to consider a pair of columns a dependency.
            Lower thresholds result in less dependencies (higher selectivity).
        verbose : int, default=0
            Verbosity. 0 means no verbosity.

        Returns
        -------
        pandas.DataFrame
            A dataframe with dependencies between columns and groups of columns.
            To better visualize the 1:1 groupgings, columns that belong to a single groups are
            put into a single cell. If no suitable candidates are found, returns an empty DataFrame.
        """
    def list_dependency_violations(self, determinant_col: str, dependent_col: str, *, dropna: bool = False, show_feeding_determinants: bool = False, max_violations: int = 10000, order_by: str = 'count') -> FabricDataFrame:
        '''
        Show violating values assuming a functional dependency.

        Assuming that there\'s a functional dependency between column A (determinant)
        and column B (dependent), show values that violate the functional dependency
        (along with the count of their respective occurences).

        Allows inspecting approximate dependencies and find data quality issues.

        For example, given a dataset with zipcodes and cities, we would expect the
        zipcode to determine the city. However, if the dataset looks like this
        (where ZIP is the determinant and CITY is the dependent):

            =====      ==============
            ZIP        CITY
            =====      ==============
            12345      Seattle
            12345      Boston
            12345      Boston
            98765      Baltimore
            00000      San Francisco
            =====      ==============

        Running this function would output the following violation:

            =====      ========    =====
            ZIP        CITY        count
            =====      ========    =====
            12345      Boston      2
            12345      Seattle     1
            =====      ========    =====

        The same zipcode is attached to multiple cities, which means there is some
        data quality issue within the dataset.

        Parameters
        ----------
        determinant_col : str
            Candidate determinant column.
        dependent_col : str
            Candidate dependent column.
        dropna : bool, default=False
            Whether to drop rows with NaN values in either column.
        show_feeding_determinants : bool, default=False
            Show values in a that are mapped to violating values in b,
            even if none of these values violate the functional constraint.
        max_violations : int, default=10,000
            The number of violations to return.
        order_by : str, default="count"
            Primary column to sort results by ("count" or "determinant").
            If "count", sorts in order of determinant with highest number of dependent occurences (grouped by determinant).
            If "determinant", sorts in alphabetical order based on determinant column.

        Returns
        -------
        FabricDataFrame
            FabricDataFrame containing all violating instances of functional dependency.
            If there are no violations, returns an empty DataFrame.
        '''
    def plot_dependency_violations(self, determinant_col: str, dependent_col: str, *, dropna: bool = False, show_feeding_determinants: bool = False, max_violations: int = 10000, order_by: str = 'count') -> graphviz.Graph:
        '''
        Show functional dependency violations in graphical format.

        Parameters
        ----------
        determinant_col : str
            Candidate determinant column.
        dependent_col : str
            Candidate dependent column.
        dropna : bool, default=False
            Whether to drop rows with NaN values in either column.
        show_feeding_determinants : bool, default=False
            Show values in a that are mapped to violating values in b,
            even if none of these values violate the functional constraint.
        max_violations : int, default=10,000
            The number of violations to return.
        order_by : str, default="count"
            Primary column to sort results by ("count" or "determinant").
            If "count", sorts in order of determinant with highest number of dependent occurences (grouped by determinant).
            If "determinant", sorts in alphabetical order based on determinant column.

        Returns
        -------
        graphviz.Graph
            Graph of violating values.
        '''
    def drop_dependency_violations(self, determinant_col: str, dependent_col: str, verbose: int = 0) -> FabricDataFrame:
        """
        Drop rows that violate a given functional constraint.

        Enforces a functional constraint between the determinant and dependent columns provided.
        For each value of the determinant, the most common value of the dependent is picked,
        and all rows with other values are dropped.
        For example given

            =====      =============
            ZIP        CITY
            =====      =============
            12345      Seattle
            12345      Boston
            12345      Boston
            98765      Baltimore
            00000      San Francisco
            =====      =============

        The row with CITY=Seattle would be dropped, and the functional dependency
        ZIP -> CITY holds in the output.

        Parameters
        ----------
        determinant_col : str
            Determining column name.
        dependent_col : str
            Dependent column name.
        verbose : int, default=0
            Verbosity; 0 means no messages, 1 means showing the number of dropped rows,
            greater than one shows entire row content of dropped rows.

        Returns
        -------
        FabricDataFrame
            New dataframe with constraint determinant -> dependent enforced.
        """
    def to_lakehouse_table(self, name: str, mode: Literal['error', 'append', 'overwrite', 'ignore'] = 'error', method: Literal['spark', 'deltalake'] | None = None, spark_schema: StructType | pa.Schema | deltalake.Schema | None = None, delta_column_mapping_mode: str = 'name') -> None:
        '''
        Write the data to OneLake as a Delta table with VOrdering enabled.

        Parameters
        ----------
        name : str
            The name of the table to write to.
        mode : {"error", "append", "overwrite", "ignore"}
            Specifies the behavior when table already exists, by default "error".
            Details of the modes are available in the `Spark docs <https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrameWriter.mode.html>`_.
        method : {"spark", "deltalake"}, default=None
            Specifies the API to write the table. If specified as None, the function will auto-select the proper API based on current runtime.
        spark_schema : pyspark.sql.types.StructType or pyarrow.Schema or deltalake.Schema, default=None
            Specifies the schema.
        delta_column_mapping_mode : str, default="name"
            Specifies the `column mapping mode <https://docs.delta.io/latest/delta-column-mapping.html>`_ to be used for the delta table. By default, it is set to "name".
        '''
    def to_parquet(self, path: str, *args, **kwargs) -> None:
        """
        Write DataFrame to a parquet file specified by path parameter using `Arrow <https://arrow.apache.org/docs/python/index.html>`_ including metadata.

        Parameters
        ----------
        path : str
            String containing the filepath to where the parquet should be saved.
        *args : list
            Other args to be passed to PyArrow ``write_table``.
        **kwargs : dict
            Other kwargs to be passed to PyArrow ``write_table``.
        """
    @property
    def column_metadata(self) -> dict | None:
        """
        Information for the columns in the table.
        """
    @column_metadata.setter
    def column_metadata(self, value: dict | None) -> None:
        """
        Update column_metadata to new value.

        Parameters
        ----------
        value : dict
            New value for column_metadata.
        """

def read_parquet(path: str) -> FabricDataFrame:
    """
    Read FabricDataFrame from a parquet file specified by path parameter using `Arrow <https://arrow.apache.org/docs/python/index.html>`_ including column metadata.

    Parameters
    ----------
    path : str
        String containing the filepath to where the parquet is located.

    Returns
    -------
    FabricDataFrame
        FabricDataFrame containing table data from specified parquet.
    """
