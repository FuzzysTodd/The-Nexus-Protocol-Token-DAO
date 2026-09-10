from sempy._utils._log import SemPyExtractor as SemPyExtractor, mds_log as mds_log
from sempy.fabric._dataframe._fabric_dataframe import FabricDataFrame as FabricDataFrame
from sempy.fabric._dataframe._fabric_series import FabricSeries as FabricSeries
from typing import Callable, TypeVar

T = TypeVar('T')

def semantic_parameters(*args, **kwargs) -> Callable:
    """
    Attach the column type matcher to a function.

    Parameters
    ----------
    *args : list
        A list of column type matchers for which the resolve column name is ignored.
    **kwargs : dict
        A dictionary of column type matchers where key is the column name and value is the matcher.

    Returns
    -------
    typing.Callable
        The decorated function injection the column type matchers.
    """
def semantic_property(name: str | None = None, requirement: Callable[[FabricDataFrame | FabricSeries], bool] | None = None, suggestion: Callable[[str, FabricDataFrame | FabricSeries], list[str]] | None = None, pip_packages: list[str] | None = None, series_type: type | None = None) -> Callable:
    """
    Decorator for registering a property as a SemanticFunction.

    Parameters
    ----------
    name : str, default=None
        Override function name.
    requirement : typing.Callable
        Function that returns True if this SemanticFunction is applicable to a dataframe
        that is passed as an argument to the function.
    suggestion : list of str
        List of suggestions.
    pip_packages : list of str
        List of pip packages to include in installation message.
    series_type : type
        Expected type if the semantic function should be applied on a :class:`~sempy.fabric.FabricSeries`.

    Returns
    -------
    typing.Callable
        Decorated function.
    """
def semantic_function(name: str | None = None, requirement: Callable[[FabricDataFrame | FabricSeries], bool] | None = None, suggestion: Callable[[str, FabricDataFrame | FabricSeries], list[str]] | None = None, pip_packages: list[str] | None = None, series_type: type | None = None) -> Callable:
    """
    Decorator for registering a function as a SemanticFunction.

    Parameters
    ----------
    name : str, default=None
        Override function name.
    requirement : typing.Callable
        Function that returns True if this SemanticFunction is applicable to a dataframe
        that is passed as an argument to the function.
    suggestion : list of str
        List of suggestions.
    pip_packages : list of str
        List of pip packages to include in installation message.
    series_type : type
        Expected type if the semantic function should be applied on a :class:`~sempy.fabric.FabricSeries`.

    Returns
    -------
    typing.Callable
        Decorated function.
    """
