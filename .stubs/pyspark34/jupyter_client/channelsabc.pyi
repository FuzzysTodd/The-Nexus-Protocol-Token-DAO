import abc

class ChannelABC(metaclass=abc.ABCMeta):
    """A base class for all channel ABCs."""
    @abc.abstractmethod
    def start(self) -> None:
        """Start the channel."""
    @abc.abstractmethod
    def stop(self) -> None:
        """Stop the channel."""
    @abc.abstractmethod
    def is_alive(self) -> bool:
        """Test whether the channel is alive."""

class HBChannelABC(ChannelABC, metaclass=abc.ABCMeta):
    """HBChannel ABC.

    The docstrings for this class can be found in the base implementation:

    `jupyter_client.channels.HBChannel`
    """
    @property
    @abc.abstractmethod
    def time_to_dead(self) -> float: ...
    @abc.abstractmethod
    def pause(self) -> None:
        """Pause the heartbeat channel."""
    @abc.abstractmethod
    def unpause(self) -> None:
        """Unpause the heartbeat channel."""
    @abc.abstractmethod
    def is_beating(self) -> bool:
        """Test whether the channel is beating."""
