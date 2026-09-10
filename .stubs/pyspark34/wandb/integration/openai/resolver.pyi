import wandb
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import Any, Dict, List, Sequence
from wandb.sdk.data_types import trace_tree as trace_tree
from wandb.sdk.integration_utils.auto_logging import Response as Response

logger: Incomplete

@dataclass
class UsageMetrics:
    elapsed_time: float = ...
    prompt_tokens: int = ...
    completion_tokens: int = ...
    total_tokens: int = ...
    def __init__(self, elapsed_time, prompt_tokens, completion_tokens, total_tokens) -> None: ...

@dataclass
class Metrics:
    usage: UsageMetrics = ...
    stats: wandb.Table = ...
    trace: trace_tree.WBTraceTree = ...
    def __init__(self, usage, stats, trace) -> None: ...

usage_metric_keys: Incomplete

class OpenAIRequestResponseResolver:
    define_metrics_called: bool
    def __init__(self) -> None: ...
    def __call__(self, args: Sequence[Any], kwargs: Dict[str, Any], response: Response, start_time: float, time_elapsed: float) -> Dict[str, Any] | None: ...
    @staticmethod
    def results_to_trace_tree(request: Dict[str, Any], response: Response, results: List[trace_tree.Result], time_elapsed: float) -> trace_tree.WBTraceTree:
        """Converts the request, response, and results into a trace tree.

        params:
            request: The request dictionary
            response: The response object
            results: A list of results object
            time_elapsed: The time elapsed in seconds
        returns:
            A wandb trace tree object.
        """
