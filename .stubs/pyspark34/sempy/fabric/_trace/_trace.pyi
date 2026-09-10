import pandas as pd
from sempy.fabric._utils import clr_to_pandas_dtype as clr_to_pandas_dtype, convert_pascal_case_to_space_delimited as convert_pascal_case_to_space_delimited, convert_space_delimited_case_to_pascal as convert_space_delimited_case_to_pascal, dotnet_to_pandas_date as dotnet_to_pandas_date
from typing import Callable

class Trace:
    '''
    Trace object for collecting diagnostic and performance related information from the Microsoft Analysis Services Tabular server.

    Python wrapper around `Microsoft Analysis Services Trace <https://learn.microsoft.com/en-us/analysis-services/trace-events/analysis-services-trace-events?view=asallproducts-allversions>`_

    NOTE: This feature is only intended for exploratory use. Due to the asynchronous communication required between the
    Microsoft Analysis Services (AS) Server and other AS clients, trace events are registered on a best-effort basis where timings are
    dependent on server load.

    Parameters
    ----------
    server : Microsoft.AnalysisServices.Tabular.Server
        Server object to add trace to.
    event_schema : dict
        Dictionary containing event types as keys and list of column names for that event as values.
        Both event and column names must be specified as strings, either in Space Delimited Case or PascalCase.
    name : str, default=None
        Name identifying trace. If None, the trace name will be "SemanticLinkTrace_%GUID%".
    filter_predicate : Callable, default=None
        Function that takes in `TraceEventArgs <https://learn.microsoft.com/en-us/dotnet/api/microsoft.analysisservices.tabular.traceeventargs?view=analysisservices-dotnet>`_
        and returns a boolean based on whether or not the trace with those args should be recorded.
    stop_event : str, default=None
        Event class that signals the end of the trace. `trace.stop()` will wait for this event (with specified timeout) before returning logs.
    '''
    def __init__(self, server, event_schema: dict[str, list[str]], name: str | None = None, filter_predicate: Callable[..., bool] | None = None, stop_event: str | None = None) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, exc_tb: types.TracebackType | None) -> None: ...
    @property
    def is_started(self) -> bool:
        """
        Whether or not this trace is currently started.
        """
    @property
    def name(self) -> str:
        """
        Name of the trace.
        """
    def add_events(self, event_schema: dict[str, list[str]]) -> None:
        """
        Add events and their corresponding columns to the trace.

        The trace must be stopped in order to add events.

        Parameters
        ----------
        event_schema : dict
            Dictionary containing event types as keys and list of column names for that event as values.
            Both event and column names must be specified as strings, either in Space Delimited Case or PascalCase.
        """
    def set_filter(self, filter_predicate: Callable[..., bool]) -> None:
        """
        Set a custom filter predicate for event preprocessing.

        Parameters
        ----------
        filter_predicate : Callable
            Function that takes in `TraceEventArgs <https://learn.microsoft.com/en-us/dotnet/api/microsoft.analysisservices.tabular.traceeventargs?view=analysisservices-dotnet>`_,
            and returns a boolean based on whether or not the trace with those args should be recorded.
        """
    def start(self, delay: int = 3) -> None:
        """
        Start the trace.

        Note: After starting the trace, there may be a slight delay as the engine registers and subscribes to trace events.
        The exact time of this delay may vary, but if you see that no trace events are being logged, you can increase the `delay` parameter.

        Parameters
        ----------
        delay : int, default=3
            Number of seconds to sleep for after starting the trace to allow engine to subscribe to added trace events.
        """
    def stop(self, timeout: int = 5) -> pd.DataFrame:
        """
        Stop the trace and retrieve the trace logs.

        Parameters
        ----------
        timeout : int, default=5
            Number of seconds to wait for stop event (specified in constructor) to register.
            If stop event is not reached in this time frame, the collected trace logs will still be returned but may be incomplete.

        Returns
        -------
        pandas.DataFrame
            DataFrame where every row is data from the events added to the trace.
        """
    def get_trace_logs(self) -> pd.DataFrame:
        """
        Retrieve the trace logs as a DataFrame.

        This can be executed while the trace is still running.

        Returns
        -------
        pandas.DataFrame
            DataFrame where every row is data from the events added to the trace.
        """
    def drop(self) -> None:
        """
        Remove the current trace from its parent Server connection.
        """
    def add_event_handler(self, on_event_func: Callable) -> None:
        """
        Add a custom handler for trace events.

        Parameters
        ----------
        on_event_func : Callable
            Function to execute on every event.
        """
    @staticmethod
    def get_default_query_trace_schema() -> dict[str, list[str]]:
        '''
        Get a default event schema for DAX Query Tracing.

        Default event classes: "QueryBegin", "QueryEnd", "VertiPaqSEQueryBegin", "VertiPaqSEQueryEnd", "VertiPaqSEQueryCacheMatch", "DirectQueryBegin", "DirectQueryEnd"
        Default event columns: "EventClass", "EventSubclass", "CurrentTime", "TextData", "SessionID", "StartTime", "EndTime", "Duration", "CpuTime", "Success"

        Returns
        -------
        dict
            Dictionary containing event types as keys and list of column names for that event as values.
        '''
