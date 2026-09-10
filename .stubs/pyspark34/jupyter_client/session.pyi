import pickle
import typing as t
import zmq
from ._version import protocol_version as protocol_version
from .adapter import adapt as adapt
from .jsonutil import extract_dates as extract_dates, json_clean as json_clean, json_default as json_default, squash_dates as squash_dates
from _typeshed import Incomplete
from datetime import datetime
from traitlets.config.configurable import Configurable, LoggingConfigurable
from zmq.eventloop.zmqstream import ZMQStream

PICKLE_PROTOCOL: Incomplete
utc: Incomplete

def squash_unicode(obj: t.Any) -> t.Any:
    """coerce unicode back to bytestrings."""

MAX_ITEMS: int
MAX_BYTES: int

def json_packer(obj: t.Any) -> bytes:
    """Convert a json object to a bytes."""
def json_unpacker(s: str | bytes) -> t.Any:
    """Convert a json bytes or string to an object."""
def pickle_packer(o: t.Any) -> bytes:
    """Pack an object using the pickle module."""
pickle_unpacker = pickle.loads
default_packer = json_packer
default_unpacker = json_unpacker
DELIM: bytes
DONE: Incomplete

def new_id() -> str:
    """Generate a new random id.

    Avoids problematic runtime import in stdlib uuid on Python 2.

    Returns
    -------

    id string (16 random bytes as hex-encoded text, chunks separated by '-')
    """
def new_id_bytes() -> bytes:
    """Return new_id as ascii bytes"""

session_aliases: Incomplete
session_flags: Incomplete

def default_secure(cfg: t.Any) -> None:
    """Set the default behavior for a config environment to be secure.

    If Session.key/keyfile have not been set, set Session.key to
    a new random UUID.
    """
def utcnow() -> datetime:
    """Return timezone-aware UTC timestamp"""

class SessionFactory(LoggingConfigurable):
    """The Base class for configurables that have a Session, Context, logger,
    and IOLoop.
    """
    logname: Incomplete
    context: Incomplete
    session: Incomplete
    loop: Incomplete
    def __init__(self, **kwargs: t.Any) -> None:
        """Initialize a session factory."""

class Message:
    """A simple message object that maps dict keys to attributes.

    A Message can be created from a dict and a dict from a Message instance
    simply by calling dict(msg_obj)."""
    def __init__(self, msg_dict: dict[str, t.Any]) -> None:
        """Initialize a message."""
    def __iter__(self) -> t.ItemsView[str, t.Any]: ...
    def __contains__(self, k: object) -> bool: ...
    def __getitem__(self, k: str) -> t.Any: ...

def msg_header(msg_id: str, msg_type: str, username: str, session: Session | str) -> dict[str, t.Any]:
    """Create a new message header"""
def extract_header(msg_or_header: dict[str, t.Any]) -> dict[str, t.Any]:
    """Given a message or header, return the header."""

class Session(Configurable):
    """Object for handling serialization and sending of messages.

    The Session object handles building messages and sending them
    with ZMQ sockets or ZMQStream objects.  Objects can communicate with each
    other over the network via Session objects, and only need to work with the
    dict-based IPython message spec. The Session will handle
    serialization/deserialization, security, and metadata.

    Sessions support configurable serialization via packer/unpacker traits,
    and signing with HMAC digests via the key/keyfile traits.

    Parameters
    ----------

    debug : bool
        whether to trigger extra debugging statements
    packer/unpacker : str : 'json', 'pickle' or import_string
        importstrings for methods to serialize message parts.  If just
        'json' or 'pickle', predefined JSON and pickle packers will be used.
        Otherwise, the entire importstring must be used.

        The functions must accept at least valid JSON input, and output *bytes*.

        For example, to use msgpack:
        packer = 'msgpack.packb', unpacker='msgpack.unpackb'
    pack/unpack : callables
        You can also set the pack/unpack callables for serialization directly.
    session : bytes
        the ID of this Session object.  The default is to generate a new UUID.
    username : unicode
        username added to message headers.  The default is to ask the OS.
    key : bytes
        The key used to initialize an HMAC signature.  If unset, messages
        will not be signed or checked.
    keyfile : filepath
        The file containing a key.  If this is set, `key` will be initialized
        to the contents of the file.

    """
    debug: Incomplete
    check_pid: Incomplete
    packer: Incomplete
    unpacker: Incomplete
    session: Incomplete
    bsession: Incomplete
    username: Incomplete
    metadata: Incomplete
    adapt_version: Incomplete
    key: Incomplete
    signature_scheme: Incomplete
    digest_mod: Incomplete
    auth: Incomplete
    digest_history: Incomplete
    digest_history_size: Incomplete
    keyfile: Incomplete
    pid: Incomplete
    pack: Incomplete
    unpack: Incomplete
    copy_threshold: Incomplete
    buffer_threshold: Incomplete
    item_threshold: Incomplete
    none: Incomplete
    def __init__(self, **kwargs: t.Any) -> None:
        """create a Session object

        Parameters
        ----------

        debug : bool
            whether to trigger extra debugging statements
        packer/unpacker : str : 'json', 'pickle' or import_string
            importstrings for methods to serialize message parts.  If just
            'json' or 'pickle', predefined JSON and pickle packers will be used.
            Otherwise, the entire importstring must be used.

            The functions must accept at least valid JSON input, and output
            *bytes*.

            For example, to use msgpack:
            packer = 'msgpack.packb', unpacker='msgpack.unpackb'
        pack/unpack : callables
            You can also set the pack/unpack callables for serialization
            directly.
        session : unicode (must be ascii)
            the ID of this Session object.  The default is to generate a new
            UUID.
        bsession : bytes
            The session as bytes
        username : unicode
            username added to message headers.  The default is to ask the OS.
        key : bytes
            The key used to initialize an HMAC signature.  If unset, messages
            will not be signed or checked.
        signature_scheme : str
            The message digest scheme. Currently must be of the form 'hmac-HASH',
            where 'HASH' is a hashing function available in Python's hashlib.
            The default is 'hmac-sha256'.
            This is ignored if 'key' is empty.
        keyfile : filepath
            The file containing a key.  If this is set, `key` will be
            initialized to the contents of the file.
        """
    def clone(self) -> Session:
        """Create a copy of this Session

        Useful when connecting multiple times to a given kernel.
        This prevents a shared digest_history warning about duplicate digests
        due to multiple connections to IOPub in the same process.

        .. versionadded:: 5.1
        """
    message_count: int
    @property
    def msg_id(self) -> str: ...
    def msg_header(self, msg_type: str) -> dict[str, t.Any]:
        """Create a header for a message type."""
    def msg(self, msg_type: str, content: dict | None = None, parent: dict[str, t.Any] | None = None, header: dict[str, t.Any] | None = None, metadata: dict[str, t.Any] | None = None) -> dict[str, t.Any]:
        """Return the nested message dict.

        This format is different from what is sent over the wire. The
        serialize/deserialize methods converts this nested message dict to the wire
        format, which is a list of message parts.
        """
    def sign(self, msg_list: list) -> bytes:
        """Sign a message with HMAC digest. If no auth, return b''.

        Parameters
        ----------
        msg_list : list
            The [p_header,p_parent,p_content] part of the message list.
        """
    def serialize(self, msg: dict[str, t.Any], ident: list[bytes] | bytes | None = None) -> list[bytes]:
        """Serialize the message components to bytes.

        This is roughly the inverse of deserialize. The serialize/deserialize
        methods work with full message lists, whereas pack/unpack work with
        the individual message parts in the message list.

        Parameters
        ----------
        msg : dict or Message
            The next message dict as returned by the self.msg method.

        Returns
        -------
        msg_list : list
            The list of bytes objects to be sent with the format::

                [ident1, ident2, ..., DELIM, HMAC, p_header, p_parent,
                 p_metadata, p_content, buffer1, buffer2, ...]

            In this list, the ``p_*`` entities are the packed or serialized
            versions, so if JSON is used, these are utf8 encoded JSON strings.
        """
    def send(self, stream: zmq.sugar.socket.Socket | ZMQStream | None, msg_or_type: dict[str, t.Any] | str, content: dict[str, t.Any] | None = None, parent: dict[str, t.Any] | None = None, ident: bytes | list[bytes] | None = None, buffers: list[bytes] | None = None, track: bool = False, header: dict[str, t.Any] | None = None, metadata: dict[str, t.Any] | None = None) -> dict[str, t.Any] | None:
        """Build and send a message via stream or socket.

        The message format used by this function internally is as follows:

        [ident1,ident2,...,DELIM,HMAC,p_header,p_parent,p_content,
         buffer1,buffer2,...]

        The serialize/deserialize methods convert the nested message dict into this
        format.

        Parameters
        ----------

        stream : zmq.Socket or ZMQStream
            The socket-like object used to send the data.
        msg_or_type : str or Message/dict
            Normally, msg_or_type will be a msg_type unless a message is being
            sent more than once. If a header is supplied, this can be set to
            None and the msg_type will be pulled from the header.

        content : dict or None
            The content of the message (ignored if msg_or_type is a message).
        header : dict or None
            The header dict for the message (ignored if msg_to_type is a message).
        parent : Message or dict or None
            The parent or parent header describing the parent of this message
            (ignored if msg_or_type is a message).
        ident : bytes or list of bytes
            The zmq.IDENTITY routing path.
        metadata : dict or None
            The metadata describing the message
        buffers : list or None
            The already-serialized buffers to be appended to the message.
        track : bool
            Whether to track.  Only for use with Sockets, because ZMQStream
            objects cannot track messages.


        Returns
        -------
        msg : dict
            The constructed message.
        """
    def send_raw(self, stream: zmq.sugar.socket.Socket, msg_list: list, flags: int = 0, copy: bool = True, ident: bytes | list[bytes] | None = None) -> None:
        """Send a raw message via ident path.

        This method is used to send a already serialized message.

        Parameters
        ----------
        stream : ZMQStream or Socket
            The ZMQ stream or socket to use for sending the message.
        msg_list : list
            The serialized list of messages to send. This only includes the
            [p_header,p_parent,p_metadata,p_content,buffer1,buffer2,...] portion of
            the message.
        ident : ident or list
            A single ident or a list of idents to use in sending.
        """
    def recv(self, socket: zmq.sugar.socket.Socket, mode: int = ..., content: bool = True, copy: bool = True) -> tuple[list[bytes] | None, dict[str, t.Any] | None]:
        """Receive and unpack a message.

        Parameters
        ----------
        socket : ZMQStream or Socket
            The socket or stream to use in receiving.

        Returns
        -------
        [idents], msg
            [idents] is a list of idents and msg is a nested message dict of
            same format as self.msg returns.
        """
    def feed_identities(self, msg_list: list[bytes] | list[zmq.Message], copy: bool = True) -> tuple[list[bytes], list[bytes] | list[zmq.Message]]:
        """Split the identities from the rest of the message.

        Feed until DELIM is reached, then return the prefix as idents and
        remainder as msg_list. This is easily broken by setting an IDENT to DELIM,
        but that would be silly.

        Parameters
        ----------
        msg_list : a list of Message or bytes objects
            The message to be split.
        copy : bool
            flag determining whether the arguments are bytes or Messages

        Returns
        -------
        (idents, msg_list) : two lists
            idents will always be a list of bytes, each of which is a ZMQ
            identity. msg_list will be a list of bytes or zmq.Messages of the
            form [HMAC,p_header,p_parent,p_content,buffer1,buffer2,...] and
            should be unpackable/unserializable via self.deserialize at this
            point.
        """
    def deserialize(self, msg_list: list[bytes] | list[zmq.Message], content: bool = True, copy: bool = True) -> dict[str, t.Any]:
        """Unserialize a msg_list to a nested message dict.

        This is roughly the inverse of serialize. The serialize/deserialize
        methods work with full message lists, whereas pack/unpack work with
        the individual message parts in the message list.

        Parameters
        ----------
        msg_list : list of bytes or Message objects
            The list of message parts of the form [HMAC,p_header,p_parent,
            p_metadata,p_content,buffer1,buffer2,...].
        content : bool (True)
            Whether to unpack the content dict (True), or leave it packed
            (False).
        copy : bool (True)
            Whether msg_list contains bytes (True) or the non-copying Message
            objects in each place (False).

        Returns
        -------
        msg : dict
            The nested message dict with top-level keys [header, parent_header,
            content, buffers].  The buffers are returned as memoryviews.
        """
    def unserialize(self, *args: t.Any, **kwargs: t.Any) -> dict[str, t.Any]:
        """**DEPRECATED** Use deserialize instead."""
