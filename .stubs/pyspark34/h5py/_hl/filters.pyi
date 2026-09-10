from .. import h5d as h5d, h5f as h5f, h5p as h5p, h5z as h5z
from .base import product as product
from .compat import filename_encode as filename_encode
from _typeshed import Incomplete
from collections.abc import Mapping

DEFAULT_GZIP: int
DEFAULT_SZIP: Incomplete
decode: Incomplete
encode: Incomplete

class FilterRefBase(Mapping):
    """Base class for referring to an HDF5 and describing its options

    Your subclass must define filter_id, and may define a filter_options tuple.
    """
    filter_id: Incomplete
    filter_options: Incomplete
    def __hash__(self): ...
    def __eq__(self, other): ...
    def __len__(self) -> int: ...
    def __iter__(self): ...
    def __getitem__(self, item): ...

class Gzip(FilterRefBase):
    filter_id: Incomplete
    filter_options: Incomplete
    def __init__(self, level=...) -> None: ...

def fill_dcpl(plist, shape, dtype, chunks, compression, compression_opts, shuffle, fletcher32, maxshape, scaleoffset, external, allow_unknown_filter: bool = False):
    """ Generate a dataset creation property list.

    Undocumented and subject to change without warning.
    """
def get_filters(plist):
    """ Extract a dictionary of active filters from a DCPL, along with
    their settings.

    Undocumented and subject to change without warning.
    """

CHUNK_BASE: Incomplete
CHUNK_MIN: Incomplete
CHUNK_MAX: Incomplete

def guess_chunk(shape, maxshape, typesize):
    """ Guess an appropriate chunk layout for a dataset, given its shape and
    the size of each element in bytes.  Will allocate chunks only as large
    as MAX_SIZE.  Chunks are generally close to some power-of-2 fraction of
    each axis, slightly favoring bigger values for the last index.

    Undocumented and subject to change without warning.
    """
