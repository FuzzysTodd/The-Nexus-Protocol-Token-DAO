from _typeshed import Incomplete
from nni.runtime.msg_dispatcher_base import MsgDispatcherBase
from typing import Any, Callable, Dict

__all__ = ['RetiariiAdvisor']

class RetiariiAdvisor(MsgDispatcherBase):
    """
    The class is to connect Retiarii components to NNI backend.
    It can be considered as a Python wrapper of NNI manager.

    It will function as the main thread when running a Retiarii experiment through NNI.
    Strategy will be launched as its thread, who will call APIs in execution engine. Execution
    engine will then find the advisor singleton and send payloads to advisor.

    When metrics are sent back, advisor will first receive the payloads, who will call the callback
    function (that is a member function in graph listener).

    The conversion advisor provides are minimum. It is only a send/receive module, and execution engine
    needs to handle all the rest.

    Attributes
    ----------
    send_trial_callback

    request_trial_jobs_callback

    trial_end_callback

    intermediate_metric_callback

    final_metric_callback
    """
    search_space: Incomplete
    send_trial_callback: Incomplete
    request_trial_jobs_callback: Incomplete
    trial_end_callback: Incomplete
    intermediate_metric_callback: Incomplete
    final_metric_callback: Incomplete
    parameters_count: int
    call_queue: Incomplete
    def __init__(self, url: str) -> None: ...
    def register_callbacks(self, callbacks: Dict[str, Callable[..., None]]):
        """
        Register callbacks for NNI backend.

        Parameters
        ----------
        callbacks
            A dictionary of callbacks.
            The key is the name of the callback. The value is the callback function.
        """
    def process_queued_callbacks(self) -> None:
        """
        Process callbacks in queue.
        Consume the messages that haven't been handled previously.
        """
    def invoke_callback(self, name: str, *args: Any) -> None:
        """
        Invoke callback.
        """
    def handle_initialize(self, data) -> None:
        """callback for initializing the advisor
        Parameters
        ----------
        data: dict
            search space
        """
    def send_trial(self, parameters, placement_constraint: Incomplete | None = None):
        """
        Send parameters to NNI.

        Parameters
        ----------
        parameters : Any
            Any payload.

        Returns
        -------
        int
            Parameter ID that is assigned to this parameter,
            which will be used for identification in future.
        """
    def mark_experiment_as_ending(self) -> None: ...
    def handle_request_trial_jobs(self, num_trials) -> None: ...
    def handle_update_search_space(self, data) -> None: ...
    def handle_trial_end(self, data) -> None: ...
    def handle_report_metric_data(self, data) -> None: ...
    def handle_import_data(self, data) -> None: ...
    def handle_add_customized_trial(self, data) -> None: ...
