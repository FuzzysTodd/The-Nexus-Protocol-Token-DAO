from numba.core import cgutils as cgutils, types as types
from numba.core.extending import intrinsic as intrinsic

def dump_refcount(typingctx, obj):
    """Dump the refcount of an object to stdout.

    Returns True if and only if object is reference-counted and NRT is enabled.
    """
def get_refcount(typingctx, obj):
    """Get the current refcount of an object.

    FIXME: only handles the first object
    """
