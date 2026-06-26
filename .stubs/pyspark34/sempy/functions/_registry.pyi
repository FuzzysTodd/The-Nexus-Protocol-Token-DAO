from _typeshed import Incomplete
from sempy._metadata._mdataframe import MDataFrame as MDataFrame
from sempy._metadata._mseries import MSeries as MSeries
from sempy.functions._function import SemanticFunction as SemanticFunction
from typing import Callable

class _SemanticFunctionRegistry:
    def __init__(self) -> None: ...
    def add(self, name: str, func: Callable, wrapped_func: Callable, is_property: bool, requirement: Incomplete | None = None, suggestion: Incomplete | None = None) -> None: ...
    def get_applicable(self, df_or_series: MDataFrame | MSeries) -> list['SemanticFunction']:
        """
        Returns all functions that are applicable to the given DataFrame or Series.

        Returns
        -------
        List[SemanticFunction]
            List of applicable functions.
        """
    def get_suggestions(self, df_or_series: MDataFrame | MSeries) -> list[str]:
        """
        Return a list of IntelliSense suggestions for the given DataFrame or Series.
        If a function is applicable, it will return a suggestion with auto-completion for the function's parameters.
        Otherwise, the plain function name is returned.

        Parameters
        ----------
        df_or_series : MDataFrame or MSeries
            The DataFrame or Series to get suggestions for.

        Returns
        -------
        List[str]
            List of suggestions.
        """
    def get(self, name, type) -> SemanticFunction | None: ...
