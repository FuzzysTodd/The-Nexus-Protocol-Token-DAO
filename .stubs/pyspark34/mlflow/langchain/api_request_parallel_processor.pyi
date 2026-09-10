import langchain
import threading
from dataclasses import dataclass
from typing import Any, Dict, List

@dataclass
class StatusTracker:
    """
    Stores metadata about the script's progress. Only one instance is created.
    """
    num_tasks_started: int = ...
    num_tasks_in_progress: int = ...
    num_tasks_succeeded: int = ...
    num_tasks_failed: int = ...
    num_api_errors: int = ...
    lock: threading.Lock = ...
    def start_task(self) -> None: ...
    def complete_task(self, *, success: bool): ...
    def increment_num_api_errors(self) -> None: ...
    def __init__(self, num_tasks_started, num_tasks_in_progress, num_tasks_succeeded, num_tasks_failed, num_api_errors, lock) -> None: ...

@dataclass
class APIRequest:
    """
    Stores an API request's inputs, outputs, and other metadata. Contains a method to make an API
    call.
    """
    index: int
    lc_model: langchain.chains.base.Chain
    request_json: dict
    results: list[tuple[int, str]]
    def call_api(self, status_tracker: StatusTracker):
        """
        Calls the LangChain API and stores results.
        """
    def __init__(self, index, lc_model, request_json, results) -> None: ...

def process_api_requests(lc_model, requests: List[str | Dict[str, Any]] = None, max_workers: int = 10):
    """
    Processes API requests in parallel.
    """
