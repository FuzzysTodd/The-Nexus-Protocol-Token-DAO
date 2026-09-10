from .exceptions import *
from .ext import ExtType as ExtType, Timestamp as Timestamp
from .fallback import Unpacker as Unpacker, unpackb
from _typeshed import Incomplete

version: Incomplete
__version__: str

def pack(o, stream, **kwargs) -> None:
    """
    Pack object `o` and write it to `stream`

    See :class:`Packer` for options.
    """
def packb(o, **kwargs):
    """
    Pack object `o` and return packed bytes

    See :class:`Packer` for options.
    """
def unpack(stream, **kwargs):
    """
    Unpack an object from `stream`.

    Raises `ExtraData` when `stream` contains extra bytes.
    See :class:`Unpacker` for options.
    """
load = unpack
loads = unpackb
dump = pack
dumps = packb
