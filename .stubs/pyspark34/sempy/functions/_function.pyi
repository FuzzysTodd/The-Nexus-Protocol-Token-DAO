from _typeshed import Incomplete
from sempy._metadata._mdataframe import MDataFrame as MDataFrame
from sempy._metadata._mseries import MSeries as MSeries
from sempy.fabric._dataframe._fabric_dataframe import FabricDataFrame as FabricDataFrame
from sempy.fabric._dataframe._fabric_series import FabricSeries as FabricSeries
from typing import Callable

class SemanticFunction:
    """
    A base class for functions that can be suggested to the user based on semantic context.

    Parameters
    ----------
    name : str
        Function name.
    function : callable
        Function definition.
    requirement : callable
        Function that returns True if this SemanticFunction is applicable to a FabricDataFrame
        that is passed as an argument to the function.
    suggestion : list of str
        List of suggestions.
    """
    function: Callable
    wrapped_function: Callable
    requirement: Callable
    suggestion: Callable
    is_property: bool
    auto_args: Callable | None
    name: Incomplete
    signature: Incomplete
    def __init__(self, name, func: Callable, wrapped_function: Callable, self_type: type, is_property: bool = False, requirement: Incomplete | None = None, suggestion: Incomplete | None = None) -> None: ...
    def __call__(self, df_or_series: FabricDataFrame | FabricSeries, *args, **kwargs):
        """
        Allow invocation of the function on a FabricDataFrame.

        Parameters
        ----------
        df_or_series : FabricDataFrame or FabricSeries
            Dataframe to apply the function to.
        *args : any
            Passed to `SemanticFunction.function`.
        **kwargs : any
            Passed to `SemanticFunction.function`.

        Returns
        -------
        any
            Value returned from this SemanticFunction's _function_.
        """
    def is_applicable(self, df_or_series: MDataFrame | MSeries) -> bool:
        """
        Return True if function can be applied to the provided FabricDataFrame.

        Parameters
        ----------
        df_or_series : MDataFrame or MSeries
             Target semantic data frame.

        Returns
        -------
        bool
            Return True if function can be applied to the provided FabricDataFrame.
        """
    def suggest_signature(self, df_or_series: MDataFrame | MSeries) -> list[str]:
        """
        Suggest signature for the provided FabricDataFrame.

        Parameters
        ----------
        df_or_series : MDataFrame or MSeries
            Target semantic data frame.

        Returns
        -------
        list of str
            List of suggestions.
        """
    def apply(self, df_or_series: FabricDataFrame | FabricSeries):
        """
        Return a callable that applies the SemanticFunction to the given FabricDataFrame.

        Parameters
        ----------
        df_or_series : FabricDataFrame or FabricSeries
            Target semantic data frame.

        Returns
        -------
        callable
            A callable that applies the SemanticFunction to the given dataframe.
        """
