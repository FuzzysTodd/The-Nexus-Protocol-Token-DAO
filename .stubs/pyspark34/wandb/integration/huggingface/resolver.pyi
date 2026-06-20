from _typeshed import Incomplete
from typing import Any, Dict, Sequence
from wandb.sdk.integration_utils.auto_logging import Response as Response
from wandb.sdk.lib.runid import generate_id as generate_id

logger: Incomplete
SUPPORTED_PIPELINE_TASKS: Incomplete
PIPELINES_WITH_TOP_K: Incomplete

class HuggingFacePipelineRequestResponseResolver:
    """Resolver for HuggingFace's pipeline request and responses, providing necessary data transformations and formatting.

    This is based off (from wandb.sdk.integration_utils.auto_logging import RequestResponseResolver)
    """
    autolog_id: Incomplete
    def __call__(self, args: Sequence[Any], kwargs: Dict[str, Any], response: Response, start_time: float, time_elapsed: float) -> Dict[str, Any] | None:
        """Main call method for this class.

        :param args: list of arguments
        :param kwargs: dictionary of keyword arguments
        :param response: the response from the request
        :param start_time: time when request started
        :param time_elapsed: time elapsed for the request
        :returns: packed data as a dictionary for logging to wandb, None if an exception occurred
        """
    def get_latest_id(self): ...
