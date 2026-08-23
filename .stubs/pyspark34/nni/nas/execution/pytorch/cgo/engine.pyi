from _typeshed import Incomplete
from dataclasses import dataclass
from nni.common.device import Device
from nni.experiment.config.training_services import RemoteConfig
from nni.nas.execution.common import AbstractExecutionEngine, AbstractGraphListener, Model, Node, WorkerInfo
from typing import Dict, Iterable, List

__all__ = ['CGOExecutionEngine', 'TrialSubmission']

@dataclass
class TrialSubmission:
    model: Model
    placement: Dict[Node, Device]
    grouped_models: List[Model]
    def __init__(self, model, placement, grouped_models) -> None: ...

class CGOExecutionEngine(AbstractExecutionEngine):
    """
    The execution engine with Cross-Graph Optimization (CGO).

    Only models using PyTorch Lighting and MultiModelSupervisedLearningModule as the evaluator can be optimized.
    Otherwise, a model will be submitted independently without any cross-graph optimization.

    Parameters
    ----------
    training_service
        The remote training service config.
    max_concurrency
        The maximum number of trials to run concurrently.
    batch_waiting_time
        Seconds to wait for each batch of trial submission.
        The trials within one batch could apply cross-graph optimization.
    rest_port
        The port of the experiment's rest server
    rest_url_prefix
        The url prefix of the experiment's rest entry
    """
    port: Incomplete
    url_prefix: Incomplete
    logical_plan_counter: int
    available_devices: Incomplete
    max_concurrency: Incomplete
    all_devices: Incomplete
    def __init__(self, training_service: RemoteConfig, max_concurrency: int = None, batch_waiting_time: int = 60, rest_port: int | None = None, rest_url_prefix: str | None = None) -> None: ...
    def join(self) -> None: ...
    def add_optimizer(self, opt) -> None: ...
    def submit_models(self, *models: List[Model]) -> None: ...
    def list_models(self) -> Iterable[Model]: ...
    def register_graph_listener(self, listener: AbstractGraphListener) -> None: ...
    def query_available_resource(self) -> List[WorkerInfo]: ...
    def budget_exhausted(self) -> bool: ...
    @classmethod
    def trial_execute_graph(cls) -> None:
        """
        Initialize the model, hand it over to trainer.
        """

class AssemblePolicy:
    @staticmethod
    def group(logical_plan, available_devices): ...
