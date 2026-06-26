import abc
import socket
from .._core._tasks import create_task_group as create_task_group
from .._core._typedattr import TypedAttributeProvider as TypedAttributeProvider, TypedAttributeSet as TypedAttributeSet, typed_attribute as typed_attribute
from ._streams import ByteStream as ByteStream, Listener as Listener, UnreliableObjectStream as UnreliableObjectStream
from ._tasks import TaskGroup as TaskGroup
from abc import abstractmethod
from io import IOBase
from ipaddress import IPv4Address, IPv6Address
from socket import AddressFamily
from typing import Any, Callable, Collection, Mapping, Tuple, TypeVar

IPAddressType = str | IPv4Address | IPv6Address
IPSockAddrType = Tuple[str, int]
SockAddrType = IPSockAddrType | str
UDPPacketType = Tuple[bytes, IPSockAddrType]
T_Retval = TypeVar('T_Retval')

class SocketAttribute(TypedAttributeSet):
    family: AddressFamily
    local_address: SockAddrType
    local_port: int
    raw_socket: socket.socket
    remote_address: SockAddrType
    remote_port: int

class _SocketProvider(TypedAttributeProvider, metaclass=abc.ABCMeta):
    @property
    def extra_attributes(self) -> Mapping[Any, Callable[[], Any]]: ...

class SocketStream(ByteStream, _SocketProvider, metaclass=abc.ABCMeta):
    """
    Transports bytes over a socket.

    Supports all relevant extra attributes from :class:`~SocketAttribute`.
    """

class UNIXSocketStream(SocketStream, metaclass=abc.ABCMeta):
    @abstractmethod
    async def send_fds(self, message: bytes, fds: Collection[int | IOBase]) -> None:
        """
        Send file descriptors along with a message to the peer.

        :param message: a non-empty bytestring
        :param fds: a collection of files (either numeric file descriptors or open file or socket
            objects)
        """
    @abstractmethod
    async def receive_fds(self, msglen: int, maxfds: int) -> tuple[bytes, list[int]]:
        """
        Receive file descriptors along with a message from the peer.

        :param msglen: length of the message to expect from the peer
        :param maxfds: maximum number of file descriptors to expect from the peer
        :return: a tuple of (message, file descriptors)
        """

class SocketListener(Listener[SocketStream], _SocketProvider, metaclass=abc.ABCMeta):
    """
    Listens to incoming socket connections.

    Supports all relevant extra attributes from :class:`~SocketAttribute`.
    """
    @abstractmethod
    async def accept(self) -> SocketStream:
        """Accept an incoming connection."""
    async def serve(self, handler: Callable[[SocketStream], Any], task_group: TaskGroup | None = None) -> None: ...

class UDPSocket(UnreliableObjectStream[UDPPacketType], _SocketProvider, metaclass=abc.ABCMeta):
    """
    Represents an unconnected UDP socket.

    Supports all relevant extra attributes from :class:`~SocketAttribute`.
    """
    async def sendto(self, data: bytes, host: str, port: int) -> None:
        """Alias for :meth:`~.UnreliableObjectSendStream.send` ((data, (host, port)))."""

class ConnectedUDPSocket(UnreliableObjectStream[bytes], _SocketProvider, metaclass=abc.ABCMeta):
    """
    Represents an connected UDP socket.

    Supports all relevant extra attributes from :class:`~SocketAttribute`.
    """
