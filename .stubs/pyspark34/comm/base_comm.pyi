from _typeshed import Incomplete

__all__ = ['CommManager', 'BaseComm']

class BaseComm:
    """Class for communicating between a Frontend and a Kernel

    Must be subclassed with a publish_msg method implementation which
    sends comm messages through the iopub channel.
    """
    comm_id: Incomplete
    primary: Incomplete
    target_name: Incomplete
    target_module: Incomplete
    topic: Incomplete
    def __init__(self, target_name: str = 'comm', data: Incomplete | None = None, metadata: Incomplete | None = None, buffers: Incomplete | None = None, comm_id: Incomplete | None = None, primary: bool = True, target_module: Incomplete | None = None, topic: Incomplete | None = None, _open_data: Incomplete | None = None, _close_data: Incomplete | None = None, **kwargs) -> None: ...
    def publish_msg(self, msg_type, data: Incomplete | None = None, metadata: Incomplete | None = None, buffers: Incomplete | None = None, **keys) -> None: ...
    def __del__(self) -> None:
        """trigger close on gc"""
    def open(self, data: Incomplete | None = None, metadata: Incomplete | None = None, buffers: Incomplete | None = None) -> None:
        """Open the frontend-side version of this comm"""
    def close(self, data: Incomplete | None = None, metadata: Incomplete | None = None, buffers: Incomplete | None = None, deleting: bool = False) -> None:
        """Close the frontend-side version of this comm"""
    def send(self, data: Incomplete | None = None, metadata: Incomplete | None = None, buffers: Incomplete | None = None) -> None:
        """Send a message to the frontend-side version of this comm"""
    def on_close(self, callback) -> None:
        """Register a callback for comm_close

        Will be called with the `data` of the close message.

        Call `on_close(None)` to disable an existing callback.
        """
    def on_msg(self, callback) -> None:
        """Register a callback for comm_msg

        Will be called with the `data` of any comm_msg messages.

        Call `on_msg(None)` to disable an existing callback.
        """
    def handle_close(self, msg) -> None:
        """Handle a comm_close message"""
    def handle_msg(self, msg) -> None:
        """Handle a comm_msg message"""

class CommManager:
    """Default CommManager singleton implementation for Comms in the Kernel"""
    comms: Incomplete
    targets: Incomplete
    def __init__(self) -> None: ...
    def register_target(self, target_name, f) -> None:
        """Register a callable f for a given target name

        f will be called with two arguments when a comm_open message is received with `target`:

        - the Comm instance
        - the `comm_open` message itself.

        f can be a Python callable or an import string for one.
        """
    def unregister_target(self, target_name, f):
        """Unregister a callable registered with register_target"""
    def register_comm(self, comm):
        """Register a new comm"""
    def unregister_comm(self, comm) -> None:
        """Unregister a comm, and close its counterpart"""
    def get_comm(self, comm_id):
        """Get a comm with a particular id

        Returns the comm if found, otherwise None.

        This will not raise an error,
        it will log messages if the comm cannot be found.
        """
    def comm_open(self, stream, ident, msg) -> None:
        """Handler for comm_open messages"""
    def comm_msg(self, stream, ident, msg) -> None:
        """Handler for comm_msg messages"""
    def comm_close(self, stream, ident, msg) -> None:
        """Handler for comm_close messages"""
