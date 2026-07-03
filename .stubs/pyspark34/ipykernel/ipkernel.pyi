from .comm.comm import BaseComm as BaseComm
from .comm.manager import CommManager as CommManager
from .compiler import XCachingCompiler as XCachingCompiler
from .debugger import Debugger as Debugger
from .kernelbase import Kernel as KernelBase
from .zmqshell import ZMQInteractiveShell as ZMQInteractiveShell
from _typeshed import Incomplete

class IPythonKernel(KernelBase):
    """The IPython Kernel class."""
    shell: Incomplete
    shell_class: Incomplete
    use_experimental_completions: Incomplete
    debugpy_stream: Incomplete
    user_module: Incomplete
    user_ns: Incomplete
    debugger: Incomplete
    comm_manager: Incomplete
    def __init__(self, **kwargs) -> None:
        """Initialize the kernel."""
    help_links: Incomplete
    implementation: str
    implementation_version: Incomplete
    language_info: Incomplete
    def dispatch_debugpy(self, msg) -> None: ...
    @property
    def banner(self): ...
    async def poll_stopped_queue(self) -> None:
        """Poll the stopped queue."""
    def start(self) -> None:
        """Start the kernel."""
    def set_parent(self, ident, parent, channel: str = 'shell') -> None:
        """Overridden from parent to tell the display hook and output streams
        about the parent message.
        """
    def init_metadata(self, parent):
        """Initialize metadata.

        Run at the beginning of each execution request.
        """
    def finish_metadata(self, parent, metadata, reply_content):
        """Finish populating metadata.

        Run after completing an execution request.
        """
    @property
    def execution_count(self): ...
    @execution_count.setter
    def execution_count(self, value) -> None: ...
    async def do_execute(self, code, silent, store_history: bool = True, user_expressions: Incomplete | None = None, allow_stdin: bool = False, *, cell_id: Incomplete | None = None):
        """Handle code execution."""
    def do_complete(self, code, cursor_pos):
        """Handle code completion."""
    async def do_debug_request(self, msg):
        """Handle a debug request."""
    def do_inspect(self, code, cursor_pos, detail_level: int = 0, omit_sections=()):
        """Handle code inspection."""
    def do_history(self, hist_access_type, output, raw, session: int = 0, start: int = 0, stop: Incomplete | None = None, n: Incomplete | None = None, pattern: Incomplete | None = None, unique: bool = False):
        """Handle code history."""
    def do_shutdown(self, restart):
        """Handle kernel shutdown."""
    def do_is_complete(self, code):
        """Handle an is_complete request."""
    def do_apply(self, content, bufs, msg_id, reply_metadata):
        """Handle an apply request."""
    def do_clear(self):
        """Clear the kernel."""

class Kernel(IPythonKernel):
    """DEPRECATED.  An alias for the IPython kernel class."""
    def __init__(self, *args, **kwargs) -> None:
        """DEPRECATED."""
