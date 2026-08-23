from ..iostream import BackgroundSocket as BackgroundSocket, IOPubThread as IOPubThread, OutStream as OutStream
from .constants import INPROCESS_KEY as INPROCESS_KEY
from .socket import DummySocket as DummySocket
from _typeshed import Incomplete
from ipykernel.ipkernel import IPythonKernel as IPythonKernel
from ipykernel.jsonutil import json_clean as json_clean
from ipykernel.zmqshell import ZMQInteractiveShell as ZMQInteractiveShell

class InProcessKernel(IPythonKernel):
    """An in-process kernel."""
    frontends: Incomplete
    gui: Incomplete
    raw_input_str: Incomplete
    stdout: Incomplete
    stderr: Incomplete
    shell_class: Incomplete
    iopub_thread: IOPubThread
    shell_stream: Incomplete
    iopub_socket: BackgroundSocket
    stdin_socket: Incomplete
    def __init__(self, **traits) -> None:
        """Initialize the kernel."""
    async def execute_request(self, stream, ident, parent) -> None:
        """Override for temporary IO redirection."""
    def start(self) -> None:
        """Override registration of dispatchers for streams."""

class InProcessInteractiveShell(ZMQInteractiveShell):
    """An in-process interactive shell."""
    kernel: InProcessKernel
    active_eventloop: Incomplete
    def enable_gui(self, gui: Incomplete | None = None) -> None:
        """Enable GUI integration for the kernel."""
    def enable_matplotlib(self, gui: Incomplete | None = None):
        """Enable matplotlib integration for the kernel."""
    def enable_pylab(self, gui: Incomplete | None = None, import_all: bool = True, welcome_message: bool = False):
        """Activate pylab support at runtime."""
