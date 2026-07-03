from collections.abc import Generator
from mlflow.utils import logging_utils as logging_utils

class _WarningsController:
    """
    Provides threadsafe utilities to modify warning behavior for MLflow autologging, including:

    - Global disablement of MLflow warnings across all threads
    - Global rerouting of MLflow warnings to an MLflow event logger (i.e. `logger.warn()`)
      across all threads
    - Disablement of non-MLflow warnings for the current thread
    - Rerouting of non-MLflow warnings to an MLflow event logger for the current thread
    """
    def __init__(self) -> None: ...
    def set_mlflow_warnings_disablement_state_globally(self, disabled: bool = True) -> None:
        """
        Disables (or re-enables) MLflow warnings globally across all threads.

        :param disabled: If `True`, disables MLflow warnings globally across all threads.
                         If `False`, enables MLflow warnings globally across all threads.
        """
    def set_mlflow_warnings_rerouting_state_globally(self, rerouted: bool = True) -> None:
        """
        Enables (or disables) rerouting of MLflow warnings to an MLflow event logger with level
        WARNING (e.g. `logger.warning()`) globally across all threads.

        :param rerouted: If `True`, enables MLflow warning rerouting globally across all threads.
                         If `False`, disables MLflow warning rerouting globally across all threads.
        """
    def set_non_mlflow_warnings_disablement_state_for_current_thread(self, disabled: bool = True) -> None:
        """
        Disables (or re-enables) non-MLflow warnings for the current thread.

        :param disabled: If `True`, disables non-MLflow warnings for the current thread. If `False`,
                         enables non-MLflow warnings for the current thread. non-MLflow warning
                         behavior in other threads is unaffected.
        """
    def set_non_mlflow_warnings_rerouting_state_for_current_thread(self, rerouted: bool = True) -> None:
        """
        Enables (or disables) rerouting of non-MLflow warnings to an MLflow event logger with level
        WARNING (e.g. `logger.warning()`) for the current thread.

        :param rerouted: If `True`, enables non-MLflow warning rerouting for the current thread.
                         If `False`, disables non-MLflow warning rerouting for the current thread.
                         non-MLflow warning behavior in other threads is unaffected.
        """
    def get_warnings_disablement_state_for_current_thread(self):
        """
        :return: `True` if non-MLflow warnings are disabled for the current thread.
                 `False` otherwise.
        """
    def get_warnings_rerouting_state_for_current_thread(self):
        """
        :return: `True` if non-MLflow warnings are rerouted to an MLflow event logger with level
                 WARNING for the current thread. `False` otherwise.
        """

def set_non_mlflow_warnings_behavior_for_current_thread(disable_warnings, reroute_warnings) -> Generator[None, None, None]:
    """
    Context manager that modifies the behavior of non-MLflow warnings upon entry, according to the
    specified parameters.

    :param disable_warnings: If `True`, disable  (mutate & discard) non-MLflow warnings. If `False`,
                             do not disable non-MLflow warnings.
    :param reroute_warnings: If `True`, reroute non-MLflow warnings to an MLflow event logger with
                             level WARNING. If `False`, do not reroute non-MLflow warnings.
    """
def set_mlflow_events_and_warnings_behavior_globally(disable_event_logs, disable_warnings, reroute_warnings) -> Generator[None, None, None]:
    """
    Threadsafe context manager that modifies the behavior of MLflow event logging statements
    and MLflow warnings upon entry, according to the specified parameters. Modifications are
    applied globally across all threads and are not reverted until all threads that have made
    a particular modification have exited the context.

    :param disable_event_logs: If `True`, disable (mute & discard) MLflow event logging statements.
                               If `False`, do not disable MLflow event logging statements.
    :param disable_warnings: If `True`, disable  (mutate & discard) MLflow warnings. If `False`,
                             do not disable MLflow warnings.
    :param reroute_warnings: If `True`, reroute MLflow warnings to an MLflow event logger with
                             level WARNING. If `False`, do not reroute MLflow warnings.
    """

class _SetMLflowEventsAndWarningsBehaviorGlobally:
    def __init__(self, disable_event_logs, disable_warnings, reroute_warnings) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, *args, **kwargs) -> None: ...
