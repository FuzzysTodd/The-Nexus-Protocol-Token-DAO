import pandas as pd
from sempy.fabric._client._dataset_xmla_client import DatasetXmlaClient as DatasetXmlaClient
from sempy.fabric._trace._trace import Trace as Trace
from typing import Callable

class TraceConnection:
    """
    Connection object for starting, viewing, and removing Traces.

    Python wrapper around `Microsoft Analysis Services Tabular Server <https://learn.microsoft.com/en-us/dotnet/api/microsoft.analysisservices.tabular.server?view=analysisservices-dotnet>`_.

    Parameters
    ----------
    dataset_client : DatasetXmlaClient
        Client for a specific dataset.
    """
    def __init__(self, dataset_client: DatasetXmlaClient) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, exc_tb: types.TracebackType | None) -> None: ...
    def create_trace(self, event_schema: dict[str, list[str]], name: str | None = None, filter_predicate: Callable[..., bool] | None = None, stop_event: str | None = None) -> Trace:
        '''
        Create a blank Trace object on this connection.

        Parameters
        ----------
        event_schema : dict
            Dictionary containing event types as keys and list of column names for that event as values.
            Both event and column names must be specified as strings, either in Space Delimited Case or PascalCase.
        name : str, default=None
            Name identifying trace. If None, the trace name will be "SemanticLinkTrace_<GUID>".
        filter_predicate : Callable
            Function that takes in `TraceEventArgs <https://learn.microsoft.com/en-us/dotnet/api/microsoft.analysisservices.tabular.traceeventargs?view=analysisservices-dotnet>`_,
            and returns a boolean based on whether or not the trace with those args should be recorded.
        stop_event : str, default=None
            Event class that signals the end of the trace. `trace.stop()` will wait for this event (with specified timeout) before returning logs.

        Returns
        -------
        Trace
            Trace object to be customized and started.
        '''
    def list_traces(self) -> pd.DataFrame:
        """
        List all stored (active or inactive) traces on a this connection.

        Returns
        -------
        pandas.DataFrame
            DataFrame containing the ID, name, timestamp, and state of each trace.
        """
    def drop_traces(self) -> None:
        """
        Remove all traces on a server.
        """
    def drop_trace(self, trace_name: str) -> None:
        """
        Drop the trace with the specified name from the server.

        Parameters
        ----------
        trace_name : str
            Name of trace to drop.
        """
    def disconnect_and_dispose(self) -> None:
        """
        Clear all traces on a server.
        """
    def discover_event_schema(self) -> pd.DataFrame:
        """
        Discover all event categories, events, and corresponding columns available to use for Tracing.

        Returns
        -------
        pandas.DataFrame
            DataFrame containing the schema information.
        """
