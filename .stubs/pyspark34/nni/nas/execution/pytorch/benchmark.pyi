from .graph import BaseExecutionEngine as BaseExecutionEngine
from _typeshed import Incomplete
from nni.nas.execution.common import Model as Model, get_mutation_dict as get_mutation_dict, receive_trial_parameters as receive_trial_parameters
from typing import Any, Callable, Dict, List, Tuple

class BenchmarkGraphData:
    SUPPORTED_BENCHMARK_LIST: Incomplete
    mutation: Incomplete
    benchmark: Incomplete
    db_path: Incomplete
    def __init__(self, mutation: Dict[str, Any], benchmark: str, metric_name: str | None = None, db_path: str | None = None) -> None: ...
    def dump(self) -> dict: ...
    @staticmethod
    def load(data) -> BenchmarkGraphData: ...

class BenchmarkExecutionEngine(BaseExecutionEngine):
    """
    Execution engine that does not actually run any trial, but query the database for results.

    The database query is done on the trial end to make sure intermediate metrics are available.
    It will also support an accelerated mode that returns metric immediately without even running into NNI manager
    (not implemented yet).
    """
    benchmark: Incomplete
    acceleration: Incomplete
    def __init__(self, benchmark: str | Callable[[BenchmarkGraphData], Tuple[float, List[float]]], acceleration: bool = False) -> None: ...
    def pack_model_data(self, model: Model) -> Any: ...
    @classmethod
    def trial_execute_graph(cls) -> None: ...
    @staticmethod
    def query_in_benchmark(graph_data: BenchmarkGraphData) -> Tuple[float, List[float]]: ...
