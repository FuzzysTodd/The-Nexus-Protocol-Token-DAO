import abc
from .channelsabc import ChannelABC as ChannelABC
from typing import Any

class KernelClientABC(metaclass=abc.ABCMeta):
    """KernelManager ABC.

    The docstrings for this class can be found in the base implementation:

    `jupyter_client.client.KernelClient`
    """
    @property
    @abc.abstractmethod
    def kernel(self) -> Any: ...
    @property
    @abc.abstractmethod
    def shell_channel_class(self) -> type[ChannelABC]: ...
    @property
    @abc.abstractmethod
    def iopub_channel_class(self) -> type[ChannelABC]: ...
    @property
    @abc.abstractmethod
    def hb_channel_class(self) -> type[ChannelABC]: ...
    @property
    @abc.abstractmethod
    def stdin_channel_class(self) -> type[ChannelABC]: ...
    @property
    @abc.abstractmethod
    def control_channel_class(self) -> type[ChannelABC]: ...
    @abc.abstractmethod
    def start_channels(self, shell: bool = True, iopub: bool = True, stdin: bool = True, hb: bool = True, control: bool = True) -> None:
        """Start the channels for the client."""
    @abc.abstractmethod
    def stop_channels(self) -> None:
        """Stop the channels for the client."""
    @property
    @abc.abstractmethod
    def channels_running(self) -> bool:
        """Get whether the channels are running."""
    @property
    @abc.abstractmethod
    def shell_channel(self) -> ChannelABC: ...
    @property
    @abc.abstractmethod
    def iopub_channel(self) -> ChannelABC: ...
    @property
    @abc.abstractmethod
    def stdin_channel(self) -> ChannelABC: ...
    @property
    @abc.abstractmethod
    def hb_channel(self) -> ChannelABC: ...
    @property
    @abc.abstractmethod
    def control_channel(self) -> ChannelABC: ...
