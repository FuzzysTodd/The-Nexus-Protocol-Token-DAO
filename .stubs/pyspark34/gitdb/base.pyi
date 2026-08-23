from _typeshed import Incomplete

__all__ = ['OInfo', 'OPackInfo', 'ODeltaPackInfo', 'OStream', 'OPackStream', 'ODeltaPackStream', 'IStream', 'InvalidOInfo', 'InvalidOStream']

class OInfo(tuple):
    """Carries information about an object in an ODB, providing information
    about the binary sha of the object, the type_string as well as the uncompressed size
    in bytes.

    It can be accessed using tuple notation and using attribute access notation::

        assert dbi[0] == dbi.binsha
        assert dbi[1] == dbi.type
        assert dbi[2] == dbi.size

    The type is designed to be as lightweight as possible."""
    def __new__(cls, sha, type, size): ...
    def __init__(self, *args) -> None: ...
    @property
    def binsha(self):
        """:return: our sha as binary, 20 bytes"""
    @property
    def hexsha(self):
        """:return: our sha, hex encoded, 40 bytes"""
    @property
    def type(self): ...
    @property
    def type_id(self): ...
    @property
    def size(self): ...

class OPackInfo(tuple):
    """As OInfo, but provides a type_id property to retrieve the numerical type id, and
    does not include a sha.

    Additionally, the pack_offset is the absolute offset into the packfile at which
    all object information is located. The data_offset property points to the absolute
    location in the pack at which that actual data stream can be found."""
    def __new__(cls, packoffset, type, size): ...
    def __init__(self, *args) -> None: ...
    @property
    def pack_offset(self): ...
    @property
    def type(self): ...
    @property
    def type_id(self): ...
    @property
    def size(self): ...

class ODeltaPackInfo(OPackInfo):
    """Adds delta specific information,
    Either the 20 byte sha which points to some object in the database,
    or the negative offset from the pack_offset, so that pack_offset - delta_info yields
    the pack offset of the base object"""
    def __new__(cls, packoffset, type, size, delta_info): ...
    @property
    def delta_info(self): ...

class OStream(OInfo):
    """Base for object streams retrieved from the database, providing additional
    information about the stream.
    Generally, ODB streams are read-only as objects are immutable"""
    def __new__(cls, sha, type, size, stream, *args, **kwargs):
        """Helps with the initialization of subclasses"""
    def __init__(self, *args, **kwargs) -> None: ...
    def read(self, size: int = -1): ...
    @property
    def stream(self): ...

class ODeltaStream(OStream):
    """Uses size info of its stream, delaying reads"""
    def __new__(cls, sha, type, size, stream, *args, **kwargs):
        """Helps with the initialization of subclasses"""
    @property
    def size(self): ...

class OPackStream(OPackInfo):
    """Next to pack object information, a stream outputting an undeltified base object
    is provided"""
    def __new__(cls, packoffset, type, size, stream, *args):
        """Helps with the initialization of subclasses"""
    def read(self, size: int = -1): ...
    @property
    def stream(self): ...

class ODeltaPackStream(ODeltaPackInfo):
    """Provides a stream outputting the uncompressed offset delta information"""
    def __new__(cls, packoffset, type, size, delta_info, stream): ...
    def read(self, size: int = -1): ...
    @property
    def stream(self): ...

class IStream(list):
    """Represents an input content stream to be fed into the ODB. It is mutable to allow
    the ODB to record information about the operations outcome right in this instance.

    It provides interfaces for the OStream and a StreamReader to allow the instance
    to blend in without prior conversion.

    The only method your content stream must support is 'read'"""
    def __new__(cls, type, size, stream, sha: Incomplete | None = None): ...
    def __init__(self, type, size, stream, sha: Incomplete | None = None) -> None: ...
    @property
    def hexsha(self):
        """:return: our sha, hex encoded, 40 bytes"""
    error: Incomplete
    def read(self, size: int = -1):
        """Implements a simple stream reader interface, passing the read call on
            to our internal stream"""
    binsha: Incomplete
    type: Incomplete
    size: Incomplete
    stream: Incomplete

class InvalidOInfo(tuple):
    """Carries information about a sha identifying an object which is invalid in
    the queried database. The exception attribute provides more information about
    the cause of the issue"""
    def __new__(cls, sha, exc): ...
    def __init__(self, sha, exc) -> None: ...
    @property
    def binsha(self): ...
    @property
    def hexsha(self): ...
    @property
    def error(self):
        """:return: exception instance explaining the failure"""

class InvalidOStream(InvalidOInfo):
    """Carries information about an invalid ODB stream"""
