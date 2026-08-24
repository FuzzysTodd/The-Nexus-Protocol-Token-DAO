from .jsonutil import json_clean as json_clean
from _typeshed import Incomplete
from jupyter_client.client import KernelClient as KernelClient
from typing import Any, Dict, List

class OutputWidget:
    """This class mimics a front end output widget"""
    comm_id: Incomplete
    state: Incomplete
    kernel_client: Incomplete
    executor: Incomplete
    topic: Incomplete
    outputs: Incomplete
    clear_before_next_output: bool
    def __init__(self, comm_id: str, state: Dict[str, Any], kernel_client: KernelClient, executor: Any) -> None:
        """Initialize the widget."""
    parent_header: Incomplete
    def clear_output(self, outs: List, msg: Dict, cell_index: int) -> None:
        """Clear output."""
    def sync_state(self) -> None:
        """Sync state."""
    def send(self, data: Dict | None = None, metadata: Dict | None = None, buffers: List | None = None) -> None:
        """Send a comm message."""
    def output(self, outs: List, msg: Dict, display_id: str, cell_index: int) -> None:
        """Handle output."""
    msg_id: Incomplete
    def set_state(self, state: Dict) -> None:
        """Set the state."""
    def handle_msg(self, msg: Dict) -> None:
        """Handle a message."""
