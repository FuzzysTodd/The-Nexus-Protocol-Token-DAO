from _typeshed import Incomplete
from nni.nas.execution.common import AbstractExecutionEngine, AbstractGraphListener, Evaluator, Model
from typing import Any, Iterable

__all__ = ['BaseGraphData', 'BaseExecutionEngine']

class BaseGraphData:
    """
    Data sent between strategy and trial, in graph-based execution engine.

    Attributes
    ----------
    model_script
        code of an instantiated PyTorch model
    evaluator
        training approach for model_script
    mutation_summary
        a dict of all the choices during mutations in the HPO search space format
    """
    model_script: Incomplete
    evaluator: Incomplete
    mutation_summary: Incomplete
    def __init__(self, model_script: str, evaluator: Evaluator, mutation_summary: dict) -> None: ...
    def dump(self) -> dict: ...
    @staticmethod
    def load(data) -> BaseGraphData: ...

class BaseExecutionEngine(AbstractExecutionEngine):
    """
    The execution engine with no optimization at all.
    Resource management is implemented in this class.
    """
    port: Incomplete
    url_prefix: Incomplete
    resources: int
    def __init__(self, rest_port: int | None = None, rest_url_prefix: str | None = None) -> None:
        """
        Upon initialization, advisor callbacks need to be registered.
        Advisor will call the callbacks when the corresponding event has been triggered.
        Base execution engine will get those callbacks and broadcast them to graph listener.

        Parameters
        ----------
        rest_port
            The port of the experiment's rest server
        rest_url_prefix
            The url prefix of the experiment's rest entry
        """
    def submit_models(self, *models: Model) -> None: ...
    def list_models(self) -> Iterable[Model]: ...
    def register_graph_listener(self, listener: AbstractGraphListener) -> None: ...
    def query_available_resource(self) -> int: ...
    def budget_exhausted(self) -> bool: ...
    @classmethod
    def pack_model_data(cls, model: Model) -> Any: ...
    @classmethod
    def trial_execute_graph(cls) -> None:
        """
        Initialize the model, hand it over to trainer.
        """
