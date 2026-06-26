import datetime
import pandas as pd
from _typeshed import Incomplete
from pandas._libs import NaTType as NaTType
from sempy.fabric import FabricDataFrame as FabricDataFrame
from sempy.relationships._multiplicity import Multiplicity as Multiplicity
from typing import Any, Callable, Iterable

def is_valid_uuid(val: str): ...

class LazyDotNetDate:
    def __init__(self, pandas_date) -> None: ...
    def dotnet_date(self): ...

def dotnet_to_pandas_date(dt, milliseconds: bool = False) -> datetime.datetime | NaTType: ...
def clr_to_pandas_dtype(input_type: str) -> str | None: ...
def convert_pascal_case_to_space_delimited(col_name: str) -> str:
    """
    Convert PascalCase to Space Delimited Case, handling all caps phrases like CPU and
    converting punctuation to spaces.
    """
def convert_space_delimited_case_to_pascal(col_name: str) -> str:
    """
    Convert Space Delimited Case to PascalCase.
    """
def get_properties(obj, properties: str | list[str] | None = None) -> dict[str, Any]: ...
def collection_to_dataframe(collection: Iterable, definition: list[tuple[str, Callable, str]], additional_properties: str | list[str] | None = None) -> pd.DataFrame:
    """
    Convert a collection of objects to a Pandas DataFrame.

    Parameters
    ----------
    collection : Iterable
        The collection to convert.
    definition : List[Tuple[str, Callable, str]]
        The definition of the columns to create. Each tuple contains the column name, a function to extract the value and
        the pandas data type.

    Returns
    -------
    pd.DataFrame
        The DataFrame.
    """
def try_import(module_name, error_message: str = '', show_source_error: bool = False, raise_exception: bool = True, verbose: bool = True): ...

class SparkConfigTemporarily:
    """
    Temporarily set a Spark configuration value and restore it afterwards.

    Parameters
    ----------
    spark : pyspark.sql.SparkSession
        Spark session to set the configuration value on.
    config : Dict[str, str]
    """
    spark: Incomplete
    config: Incomplete
    original_values: Incomplete
    def __init__(self, spark, config) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, exc_tb: types.TracebackType | None) -> None: ...

def to_multiplicity(relationship) -> str: ...
