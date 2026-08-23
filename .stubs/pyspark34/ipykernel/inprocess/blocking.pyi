from .channels import InProcessChannel as InProcessChannel
from .client import InProcessKernelClient as InProcessKernelClient
from _typeshed import Incomplete

class BlockingInProcessChannel(InProcessChannel):
    """A blocking in-process channel."""
    def __init__(self, *args, **kwds) -> None:
        """Initialize the channel."""
    def call_handlers(self, msg) -> None:
        """Call the handlers for a message."""
    def get_msg(self, block: bool = True, timeout: Incomplete | None = None):
        """Gets a message if there is one that is ready."""
    def get_msgs(self):
        """Get all messages that are currently ready."""
    def msg_ready(self):
        """Is there a message that has been received?"""

class BlockingInProcessStdInChannel(BlockingInProcessChannel):
    """A blocking in-process stdin channel."""
    def call_handlers(self, msg) -> None:
        """Overridden for the in-process channel.

        This methods simply calls raw_input directly.
        """

class BlockingInProcessKernelClient(InProcessKernelClient):
    """A blocking in-process kernel client."""
    shell_channel_class: Incomplete
    iopub_channel_class: Incomplete
    stdin_channel_class: Incomplete
    def wait_for_ready(self) -> None:
        """Wait for kernel info reply on shell channel."""
