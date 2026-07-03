from _typeshed import Incomplete
from posthog.request import APIError as APIError, DatetimeSerializer as DatetimeSerializer, batch_post as batch_post
from threading import Thread

MAX_MSG_SIZE: Incomplete
BATCH_SIZE_LIMIT: int

class Consumer(Thread):
    """Consumes the messages from the client's queue."""
    log: Incomplete
    daemon: bool
    flush_at: Incomplete
    flush_interval: Incomplete
    api_key: Incomplete
    host: Incomplete
    on_error: Incomplete
    queue: Incomplete
    gzip: Incomplete
    running: bool
    retries: Incomplete
    timeout: Incomplete
    def __init__(self, queue, api_key, flush_at: int = 100, host: Incomplete | None = None, on_error: Incomplete | None = None, flush_interval: float = 0.5, gzip: bool = False, retries: int = 10, timeout: int = 15) -> None:
        """Create a consumer thread."""
    def run(self) -> None:
        """Runs the consumer."""
    def pause(self) -> None:
        """Pause the consumer."""
    def upload(self):
        """Upload the next batch of items, return whether successful."""
    def next(self):
        """Return the next batch of items to upload."""
    def request(self, batch):
        """Attempt to upload the batch and retry before raising an error"""
