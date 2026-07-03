from _typeshed import Incomplete
from ppft import Server as Server, _Task

class ApplyResult(_Task):
    """result object for an 'apply' method in parallelpython

enables a pp._Task to mimic the multiprocessing.pool.ApplyResult interface
    """
    unpickled: bool
    def __init__(self, task) -> None: ...
    def ready(self):
        """Checks if the result is ready"""
    def successful(self):
        """Measures whether result is ready and loaded w/o printing"""
    def wait(self, timeout: Incomplete | None = None) -> None:
        """Waits for the task"""
    def get(self, timeout: Incomplete | None = None):
        """Retrieves result of the task"""
    def __call__(self, raw_result: bool = False):
        """Retrieves result of the task"""
    def finalize(self, sresult) -> None:
        """Finalizes the task  ***internal use only***"""
    @property
    def lock(self): ...
    @property
    def tid(self): ...
    @property
    def server(self): ...
    @property
    def callback(self): ...
    @property
    def callbackargs(self): ...
    @property
    def group(self): ...
    @property
    def finished(self): ...

class MapResult:
    callback: Incomplete
    callbackargs: Incomplete
    group: Incomplete
    finished: bool
    unpickled: bool
    def __init__(self, size, callback: Incomplete | None = None, callbackargs=(), group: str = 'default') -> None: ...
    def finalize(self, *results) -> None:
        """finalize the tasks  ***internal use only***"""
    def queue(self, *tasks) -> None:
        """Fill the MapResult with ApplyResult objects"""
    def __call__(self):
        """Retrieve the results of the tasks"""
    def wait(self, timeout: Incomplete | None = None) -> None:
        """Wait for the tasks"""
    def get(self, timeout: Incomplete | None = None):
        """Retrieves results of the tasks"""
    def ready(self):
        """Checks if the result is ready"""
    def successful(self):
        """Measures whether result is ready and loaded w/o printing"""
