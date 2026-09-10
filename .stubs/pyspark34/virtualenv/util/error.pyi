from _typeshed import Incomplete

class ProcessCallFailedError(RuntimeError):
    """Failed a process call."""
    code: Incomplete
    out: Incomplete
    err: Incomplete
    cmd: Incomplete
    def __init__(self, code, out, err, cmd) -> None: ...
