import threading
from _typeshed import Incomplete

class Poller(threading.Thread):
    daemon: bool
    stopped: Incomplete
    interval: Incomplete
    execute: Incomplete
    args: Incomplete
    kwargs: Incomplete
    def __init__(self, interval, execute, *args, **kwargs) -> None: ...
    def stop(self) -> None: ...
    def run(self) -> None: ...
