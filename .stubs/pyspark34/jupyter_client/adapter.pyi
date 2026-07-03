from ._version import protocol_version_info as protocol_version_info
from _typeshed import Incomplete
from typing import Any, Dict, Tuple

def code_to_line(code: str, cursor_pos: int) -> Tuple[str, int]:
    """Turn a multiline code block and cursor position into a single line
    and new cursor position.

    For adapting ``complete_`` and ``object_info_request``.
    """
def extract_oname_v4(code: str, cursor_pos: int) -> str:
    """Reimplement token-finding logic from IPython 2.x javascript

    for adapting object_info_request from v5 to v4
    """

class Adapter:
    """Base class for adapting messages

    Override message_type(msg) methods to create adapters.
    """
    msg_type_map: Dict[str, str]
    def update_header(self, msg: Dict[str, Any]) -> Dict[str, Any]:
        """Update the header."""
    def update_metadata(self, msg: Dict[str, Any]) -> Dict[str, Any]:
        """Update the metadata."""
    def update_msg_type(self, msg: Dict[str, Any]) -> Dict[str, Any]:
        """Update the message type."""
    def handle_reply_status_error(self, msg: Dict[str, Any]) -> Dict[str, Any]:
        """This will be called *instead of* the regular handler

        on any reply with status != ok
        """
    def __call__(self, msg: Dict[str, Any]) -> Dict[str, Any]: ...

class V5toV4(Adapter):
    """Adapt msg protocol v5 to v4"""
    version: str
    msg_type_map: Incomplete
    def update_header(self, msg: Dict[str, Any]) -> Dict[str, Any]:
        """Update the header."""
    def kernel_info_reply(self, msg: Dict[str, Any]) -> Dict[str, Any]:
        """Handle a kernel info reply."""
    def execute_request(self, msg: Dict[str, Any]) -> Dict[str, Any]:
        """Handle an execute request."""
    def execute_reply(self, msg: Dict[str, Any]) -> Dict[str, Any]:
        """Handle an execute reply."""
    def complete_request(self, msg: Dict[str, Any]) -> Dict[str, Any]:
        """Handle a complete request."""
    def complete_reply(self, msg: Dict[str, Any]) -> Dict[str, Any]:
        """Handle a complete reply."""
    def object_info_request(self, msg: Dict[str, Any]) -> Dict[str, Any]:
        """Handle an object info request."""
    def object_info_reply(self, msg: Dict[str, Any]) -> Dict[str, Any]:
        """inspect_reply can't be easily backward compatible"""
    def stream(self, msg: Dict[str, Any]) -> Dict[str, Any]:
        """Handle a stream message."""
    def display_data(self, msg: Dict[str, Any]) -> Dict[str, Any]:
        """Handle a display data message."""
    def input_request(self, msg: Dict[str, Any]) -> Dict[str, Any]:
        """Handle an input request."""

class V4toV5(Adapter):
    """Convert msg spec V4 to V5"""
    version: str
    msg_type_map: Incomplete
    def update_header(self, msg: Dict[str, Any]) -> Dict[str, Any]:
        """Update the header."""
    def kernel_info_reply(self, msg: Dict[str, Any]) -> Dict[str, Any]:
        """Handle a kernel info reply."""
    def execute_request(self, msg: Dict[str, Any]) -> Dict[str, Any]:
        """Handle an execute request."""
    def execute_reply(self, msg: Dict[str, Any]) -> Dict[str, Any]:
        """Handle an execute reply."""
    def complete_request(self, msg: Dict[str, Any]) -> Dict[str, Any]:
        """Handle a complete request."""
    def complete_reply(self, msg: Dict[str, Any]) -> Dict[str, Any]:
        """Handle a complete reply."""
    def inspect_request(self, msg: Dict[str, Any]) -> Dict[str, Any]:
        """Handle an inspect request."""
    def inspect_reply(self, msg: Dict[str, Any]) -> Dict[str, Any]:
        """inspect_reply can't be easily backward compatible"""
    def stream(self, msg: Dict[str, Any]) -> Dict[str, Any]:
        """Handle a stream message."""
    def display_data(self, msg: Dict[str, Any]) -> Dict[str, Any]:
        """Handle display data."""
    def input_request(self, msg: Dict[str, Any]) -> Dict[str, Any]:
        """Handle an input request."""

def adapt(msg: Dict[str, Any], to_version: int = ...) -> Dict[str, Any]:
    """Adapt a single message to a target version

    Parameters
    ----------

    msg : dict
        A Jupyter message.
    to_version : int, optional
        The target major version.
        If unspecified, adapt to the current version.

    Returns
    -------

    msg : dict
        A Jupyter message appropriate in the new version.
    """

adapters: Incomplete
