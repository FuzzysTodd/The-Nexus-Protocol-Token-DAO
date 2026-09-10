import typing as t
from ..channels import AsyncZMQSocketChannel as AsyncZMQSocketChannel, HBChannel as HBChannel
from ..client import KernelClient as KernelClient, reqrep as reqrep
from _typeshed import Incomplete

def wrapped(meth: t.Callable, channel: str) -> t.Callable:
    """Wrap a method on a channel and handle replies."""

class AsyncKernelClient(KernelClient):
    """A KernelClient with async APIs

    ``get_[channel]_msg()`` methods wait for and return messages on channels,
    raising :exc:`queue.Empty` if no message arrives within ``timeout`` seconds.
    """
    context: Incomplete
    get_shell_msg: Incomplete
    get_iopub_msg: Incomplete
    get_stdin_msg: Incomplete
    get_control_msg: Incomplete
    wait_for_ready: Incomplete
    shell_channel_class: Incomplete
    iopub_channel_class: Incomplete
    stdin_channel_class: Incomplete
    hb_channel_class: Incomplete
    control_channel_class: Incomplete
    execute: Incomplete
    history: Incomplete
    complete: Incomplete
    is_complete: Incomplete
    inspect: Incomplete
    kernel_info: Incomplete
    comm_info: Incomplete
    is_alive: Incomplete
    execute_interactive: Incomplete
    shutdown: Incomplete
