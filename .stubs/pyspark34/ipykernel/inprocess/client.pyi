from .channels import InProcessChannel as InProcessChannel, InProcessHBChannel as InProcessHBChannel
from _typeshed import Incomplete
from jupyter_client.client import KernelClient

class InProcessKernelClient(KernelClient):
    """A client for an in-process kernel.

    This class implements the interface of
    `jupyter_client.clientabc.KernelClientABC` and allows
    (asynchronous) frontends to be used seamlessly with an in-process kernel.

    See `jupyter_client.client.KernelClient` for docstrings.
    """
    shell_channel_class: Incomplete
    iopub_channel_class: Incomplete
    stdin_channel_class: Incomplete
    control_channel_class: Incomplete
    hb_channel_class: Incomplete
    kernel: Incomplete
    def get_connection_info(self):
        """Get the connection info for the client."""
    def start_channels(self, *args, **kwargs) -> None:
        """Start the channels on the client."""
    @property
    def shell_channel(self): ...
    @property
    def iopub_channel(self): ...
    @property
    def stdin_channel(self): ...
    @property
    def control_channel(self): ...
    @property
    def hb_channel(self): ...
    def execute(self, code, silent: bool = False, store_history: bool = True, user_expressions: Incomplete | None = None, allow_stdin: Incomplete | None = None):
        """Execute code on the client."""
    def complete(self, code, cursor_pos: Incomplete | None = None):
        """Get code completion."""
    def inspect(self, code, cursor_pos: Incomplete | None = None, detail_level: int = 0):
        """Get code inspection."""
    def history(self, raw: bool = True, output: bool = False, hist_access_type: str = 'range', **kwds):
        """Get code history."""
    def shutdown(self, restart: bool = False) -> None:
        """Handle shutdown."""
    def kernel_info(self):
        """Request kernel info."""
    def comm_info(self, target_name: Incomplete | None = None):
        """Request a dictionary of valid comms and their targets."""
    def input(self, string) -> None:
        """Handle kernel input."""
    def is_complete(self, code):
        """Handle an is_complete request."""
    def get_shell_msg(self, block: bool = True, timeout: Incomplete | None = None):
        """Get a shell message."""
    def get_iopub_msg(self, block: bool = True, timeout: Incomplete | None = None):
        """Get an iopub message."""
    def get_stdin_msg(self, block: bool = True, timeout: Incomplete | None = None):
        """Get a stdin message."""
    def get_control_msg(self, block: bool = True, timeout: Incomplete | None = None):
        """Get a control message."""
