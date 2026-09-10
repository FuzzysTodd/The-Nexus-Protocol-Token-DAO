import zmq
from .connect import get_connection_info as get_connection_info, write_connection_file as write_connection_file
from .control import ControlThread as ControlThread
from .heartbeat import Heartbeat as Heartbeat
from .iostream import IOPubThread as IOPubThread
from .ipkernel import IPythonKernel as IPythonKernel
from .parentpoller import ParentPollerUnix as ParentPollerUnix, ParentPollerWindows as ParentPollerWindows
from .zmqshell import ZMQInteractiveShell as ZMQInteractiveShell
from IPython.core.application import BaseIPythonApplication
from IPython.core.shellapp import InteractiveShellApp
from _typeshed import Incomplete
from jupyter_client.connect import ConnectionFileMixin

kernel_aliases: Incomplete
kernel_flags: Incomplete

class IPKernelApp(BaseIPythonApplication, InteractiveShellApp, ConnectionFileMixin):
    """The IPYKernel application class."""
    name: str
    aliases: Incomplete
    flags: Incomplete
    classes: Incomplete
    kernel_class: Incomplete
    kernel: Incomplete
    poller: Incomplete
    heartbeat: Incomplete
    context: zmq.Context | None
    shell_socket: Incomplete
    control_socket: Incomplete
    debugpy_socket: Incomplete
    debug_shell_socket: Incomplete
    stdin_socket: Incomplete
    iopub_socket: Incomplete
    iopub_thread: Incomplete
    control_thread: Incomplete
    subcommands: Incomplete
    connection_dir: Incomplete
    @property
    def abs_connection_file(self): ...
    no_stdout: Incomplete
    no_stderr: Incomplete
    trio_loop: Incomplete
    quiet: Incomplete
    outstream_class: Incomplete
    displayhook_class: Incomplete
    capture_fd_output: Incomplete
    parent_handle: Incomplete
    interrupt: Incomplete
    def init_crash_handler(self) -> None:
        """Initialize the crash handler."""
    def excepthook(self, etype, evalue, tb) -> None:
        """Handle an exception."""
    def init_poller(self) -> None:
        """Initialize the poller."""
    def write_connection_file(self) -> None:
        """write connection info to JSON file"""
    def cleanup_connection_file(self) -> None:
        """Clean up our connection file."""
    connection_file: Incomplete
    def init_connection_file(self) -> None:
        """Initialize our connection file."""
    shell_port: Incomplete
    stdin_port: Incomplete
    def init_sockets(self) -> None:
        """Create a context, a session, and the kernel sockets."""
    control_port: Incomplete
    def init_control(self, context) -> None:
        """Initialize the control channel."""
    iopub_port: Incomplete
    def init_iopub(self, context) -> None:
        """Initialize the iopub channel."""
    hb_port: Incomplete
    def init_heartbeat(self) -> None:
        """start the heart beating"""
    def close(self) -> None:
        """Close zmq sockets in an orderly fashion"""
    def log_connection_info(self) -> None:
        """display connection info, and store ports"""
    def init_blackhole(self) -> None:
        """redirects stdout/stderr to devnull if necessary"""
    displayhook: Incomplete
    def init_io(self) -> None:
        """Redirect input streams and set a display hook."""
    def reset_io(self) -> None:
        """restore original io

        restores state after init_io
        """
    def patch_io(self):
        """Patch important libraries that can't handle sys.stdout forwarding"""
    def init_signal(self) -> None:
        """Initialize the signal handler."""
    def init_kernel(self):
        """Create the Kernel object itself"""
    def init_gui_pylab(self) -> None:
        """Enable GUI event loop integration, taking pylab into account."""
    shell: Incomplete
    def init_shell(self) -> None:
        """Initialize the shell channel."""
    def configure_tornado_logger(self) -> None:
        """Configure the tornado logging.Logger.

        Must set up the tornado logger or else tornado will call
        basicConfig for the root logger which makes the root logger
        go to the real sys.stderr instead of the capture streams.
        This function mimics the setup of logging.basicConfig.
        """
    def init_pdb(self) -> None:
        """Replace pdb with IPython's version that is interruptible.

        With the non-interruptible version, stopping pdb() locks up the kernel in a
        non-recoverable state.
        """
    def initialize(self, argv: Incomplete | None = None) -> None:
        """Initialize the application."""
    io_loop: Incomplete
    def start(self):
        """Start the application."""

launch_new_instance: Incomplete

def main() -> None:
    """Run an IPKernel as an application"""
