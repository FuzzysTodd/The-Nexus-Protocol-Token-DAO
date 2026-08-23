import queue
import threading
from dataclasses import dataclass
from openai.openai_object import OpenAIObject as OpenAIObject

@dataclass
class StatusTracker:
    """
    Stores metadata about the script's progress. Only one instance is created.
    """
    num_tasks_started: int = ...
    num_tasks_in_progress: int = ...
    num_tasks_succeeded: int = ...
    num_tasks_failed: int = ...
    num_rate_limit_errors: int = ...
    num_api_errors: int = ...
    num_other_errors: int = ...
    time_of_last_rate_limit_error: int = ...
    lock: threading.Lock = ...
    def start_task(self) -> None: ...
    def complete_task(self, *, success: bool): ...
    def increment_num_rate_limit_errors(self) -> None: ...
    def increment_num_api_errors(self) -> None: ...
    def __init__(self, num_tasks_started, num_tasks_in_progress, num_tasks_succeeded, num_tasks_failed, num_rate_limit_errors, num_api_errors, num_other_errors, time_of_last_rate_limit_error, lock) -> None: ...

@dataclass
class APIRequest:
    """
    Stores an API request's inputs, outputs, and other metadata. Contains a method to make an API
    call.
    """
    index: int
    request_json: dict
    token_consumption: int
    attempts_left: int
    results: list[tuple[int, OpenAIObject]]
    def call_api(self, retry_queue: queue.Queue, status_tracker: StatusTracker):
        """
        Calls the OpenAI API and stores results.
        """
    def __init__(self, index, request_json, token_consumption, attempts_left, results) -> None: ...

def num_tokens_consumed_from_request(request_json: dict, api_endpoint: str, token_encoding_name: str):
    """
    Count the number of tokens in the request. Only supports completion and embedding requests.
    """
def process_api_requests(requests: list[dict[str, any]] = None, max_requests_per_minute: float = 3500, max_tokens_per_minute: float = 90000, token_encoding_name: str = 'cl100k_base', max_attempts: int = 5, max_workers: int = 10):
    """
    Processes API requests in parallel, throttling to stay under rate limits.
    """
