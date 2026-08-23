import typing as t
from IPython.core.displayhook import DisplayHook
from _typeshed import Incomplete
from ipykernel.jsonutil import encode_images as encode_images, json_clean as json_clean

class ZMQDisplayHook:
    """A simple displayhook that publishes the object's repr over a ZeroMQ
    socket."""
    topic: bytes
    session: Incomplete
    pub_socket: Incomplete
    parent_header: Incomplete
    def __init__(self, session, pub_socket) -> None:
        """Initialize the hook."""
    def get_execution_count(self):
        """This method is replaced in kernelapp"""
    def __call__(self, obj) -> None:
        """Handle a hook call."""
    def set_parent(self, parent) -> None:
        """Set the parent header."""

class ZMQShellDisplayHook(DisplayHook):
    """A displayhook subclass that publishes data using ZeroMQ. This is intended
    to work with an InteractiveShell instance. It sends a dict of different
    representations of the object."""
    topic: Incomplete
    session: Incomplete
    pub_socket: Incomplete
    parent_header: Incomplete
    msg: dict[str, t.Any] | None
    def set_parent(self, parent) -> None:
        """Set the parent for outbound messages."""
    def start_displayhook(self) -> None:
        """Start the display hook."""
    def write_output_prompt(self) -> None:
        """Write the output prompt."""
    def write_format_data(self, format_dict, md_dict: Incomplete | None = None) -> None:
        """Write format data to the message."""
    def finish_displayhook(self) -> None:
        """Finish up all displayhook activities."""
