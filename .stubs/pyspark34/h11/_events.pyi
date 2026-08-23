from ._headers import Headers
from abc import ABC
from dataclasses import dataclass
from typing import List, Tuple

__all__ = ['Event', 'Request', 'InformationalResponse', 'Response', 'Data', 'EndOfMessage', 'ConnectionClosed']

class Event(ABC):
    """
    Base class for h11 events.
    """

@dataclass(init=False, frozen=True)
class Request(Event):
    '''The beginning of an HTTP request.

    Fields:

    .. attribute:: method

       An HTTP method, e.g. ``b"GET"`` or ``b"POST"``. Always a byte
       string. :term:`Bytes-like objects <bytes-like object>` and native
       strings containing only ascii characters will be automatically
       converted to byte strings.

    .. attribute:: target

       The target of an HTTP request, e.g. ``b"/index.html"``, or one of the
       more exotic formats described in `RFC 7320, section 5.3
       <https://tools.ietf.org/html/rfc7230#section-5.3>`_. Always a byte
       string. :term:`Bytes-like objects <bytes-like object>` and native
       strings containing only ascii characters will be automatically
       converted to byte strings.

    .. attribute:: headers

       Request headers, represented as a list of (name, value) pairs. See
       :ref:`the header normalization rules <headers-format>` for details.

    .. attribute:: http_version

       The HTTP protocol version, represented as a byte string like
       ``b"1.1"``. See :ref:`the HTTP version normalization rules
       <http_version-format>` for details.

    '''
    method: bytes
    headers: Headers
    target: bytes
    http_version: bytes
    def __init__(self, *, method: bytes | str, headers: Headers | List[Tuple[bytes, bytes]] | List[Tuple[str, str]], target: bytes | str, http_version: bytes | str = b'1.1', _parsed: bool = False) -> None: ...
    __hash__ = ...

@dataclass(init=False, frozen=True)
class _ResponseBase(Event):
    headers: Headers
    http_version: bytes
    reason: bytes
    status_code: int
    def __init__(self, *, headers: Headers | List[Tuple[bytes, bytes]] | List[Tuple[str, str]], status_code: int, http_version: bytes | str = b'1.1', reason: bytes | str = b'', _parsed: bool = False) -> None: ...
    def __post_init__(self) -> None: ...
    __hash__ = ...

@dataclass(init=False, frozen=True)
class InformationalResponse(_ResponseBase):
    '''An HTTP informational response.

    Fields:

    .. attribute:: status_code

       The status code of this response, as an integer. For an
       :class:`InformationalResponse`, this is always in the range [100,
       200).

    .. attribute:: headers

       Request headers, represented as a list of (name, value) pairs. See
       :ref:`the header normalization rules <headers-format>` for
       details.

    .. attribute:: http_version

       The HTTP protocol version, represented as a byte string like
       ``b"1.1"``. See :ref:`the HTTP version normalization rules
       <http_version-format>` for details.

    .. attribute:: reason

       The reason phrase of this response, as a byte string. For example:
       ``b"OK"``, or ``b"Not Found"``.

    '''
    def __post_init__(self) -> None: ...
    __hash__ = ...

@dataclass(init=False, frozen=True)
class Response(_ResponseBase):
    '''The beginning of an HTTP response.

    Fields:

    .. attribute:: status_code

       The status code of this response, as an integer. For an
       :class:`Response`, this is always in the range [200,
       1000).

    .. attribute:: headers

       Request headers, represented as a list of (name, value) pairs. See
       :ref:`the header normalization rules <headers-format>` for details.

    .. attribute:: http_version

       The HTTP protocol version, represented as a byte string like
       ``b"1.1"``. See :ref:`the HTTP version normalization rules
       <http_version-format>` for details.

    .. attribute:: reason

       The reason phrase of this response, as a byte string. For example:
       ``b"OK"``, or ``b"Not Found"``.

    '''
    def __post_init__(self) -> None: ...
    __hash__ = ...

@dataclass(init=False, frozen=True)
class Data(Event):
    """Part of an HTTP message body.

    Fields:

    .. attribute:: data

       A :term:`bytes-like object` containing part of a message body. Or, if
       using the ``combine=False`` argument to :meth:`Connection.send`, then
       any object that your socket writing code knows what to do with, and for
       which calling :func:`len` returns the number of bytes that will be
       written -- see :ref:`sendfile` for details.

    .. attribute:: chunk_start

       A marker that indicates whether this data object is from the start of a
       chunked transfer encoding chunk. This field is ignored when when a Data
       event is provided to :meth:`Connection.send`: it is only valid on
       events emitted from :meth:`Connection.next_event`. You probably
       shouldn't use this attribute at all; see
       :ref:`chunk-delimiters-are-bad` for details.

    .. attribute:: chunk_end

       A marker that indicates whether this data object is the last for a
       given chunked transfer encoding chunk. This field is ignored when when
       a Data event is provided to :meth:`Connection.send`: it is only valid
       on events emitted from :meth:`Connection.next_event`. You probably
       shouldn't use this attribute at all; see
       :ref:`chunk-delimiters-are-bad` for details.

    """
    data: bytes
    chunk_start: bool
    chunk_end: bool
    def __init__(self, data: bytes, chunk_start: bool = False, chunk_end: bool = False) -> None: ...
    __hash__ = ...

@dataclass(init=False, frozen=True)
class EndOfMessage(Event):
    """The end of an HTTP message.

    Fields:

    .. attribute:: headers

       Default value: ``[]``

       Any trailing headers attached to this message, represented as a list of
       (name, value) pairs. See :ref:`the header normalization rules
       <headers-format>` for details.

       Must be empty unless ``Transfer-Encoding: chunked`` is in use.

    """
    headers: Headers
    def __init__(self, *, headers: Headers | List[Tuple[bytes, bytes]] | List[Tuple[str, str]] | None = None, _parsed: bool = False) -> None: ...
    __hash__ = ...

@dataclass(frozen=True)
class ConnectionClosed(Event):
    """This event indicates that the sender has closed their outgoing
    connection.

    Note that this does not necessarily mean that they can't *receive* further
    data, because TCP connections are composed to two one-way channels which
    can be closed independently. See :ref:`closing` for details.

    No fields.
    """
