from _typeshed import Incomplete
from nbformat import NotebookNode as NotebookNode
from typing import Dict

class CellControlSignal(Exception):
    """
    A custom exception used to indicate that the exception is used for cell
    control actions (not the best model, but it's needed to cover existing
    behavior without major refactors).
    """

class CellTimeoutError(TimeoutError, CellControlSignal):
    """
    A custom exception to capture when a cell has timed out during execution.
    """
    @classmethod
    def error_from_timeout_and_cell(cls, msg: str, timeout: int, cell: NotebookNode) -> CellTimeoutError:
        """Create an error from a timeout on a cell."""

class DeadKernelError(RuntimeError):
    """A dead kernel error."""
class CellExecutionComplete(CellControlSignal):
    """
    Used as a control signal for cell execution across execute_cell and
    process_message function calls. Raised when all execution requests
    are completed and no further messages are expected from the kernel
    over zeromq channels.
    """

class CellExecutionError(CellControlSignal):
    """
    Custom exception to propagate exceptions that are raised during
    notebook execution to the caller. This is mostly useful when
    using nbconvert as a library, since it allows to deal with
    failures gracefully.
    """
    traceback: Incomplete
    ename: Incomplete
    evalue: Incomplete
    def __init__(self, traceback: str, ename: str, evalue: str) -> None:
        """Initialize the error."""
    def __reduce__(self) -> tuple:
        """Reduce implementation."""
    @classmethod
    def from_cell_and_msg(cls, cell: NotebookNode, msg: Dict) -> CellExecutionError:
        """Instantiate from a code cell object and a message contents
        (message is either execute_reply or error)
        """

stream_output_msg: str
exec_err_msg: str
timeout_err_msg: str
