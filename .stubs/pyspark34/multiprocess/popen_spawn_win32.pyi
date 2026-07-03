from _typeshed import Incomplete

__all__ = ['Popen']

class Popen:
    """
    Start a subprocess to run the code of a process object
    """
    method: str
    pid: Incomplete
    returncode: Incomplete
    sentinel: Incomplete
    finalizer: Incomplete
    def __init__(self, process_obj) -> None: ...
    def duplicate_for_child(self, handle): ...
    def wait(self, timeout: Incomplete | None = None): ...
    def poll(self): ...
    def terminate(self) -> None: ...
    kill = terminate
    def close(self) -> None: ...
