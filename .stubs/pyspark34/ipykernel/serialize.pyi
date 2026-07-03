from _typeshed import Incomplete
from ipykernel.pickleutil import CannedObject as CannedObject, PICKLE_PROTOCOL as PICKLE_PROTOCOL, can as can, can_sequence as can_sequence, istype as istype, sequence_types as sequence_types, uncan as uncan, uncan_sequence as uncan_sequence

def serialize_object(obj, buffer_threshold=..., item_threshold=...):
    """Serialize an object into a list of sendable buffers.

    Parameters
    ----------
    obj : object
        The object to be serialized
    buffer_threshold : int
        The threshold (in bytes) for pulling out data buffers
        to avoid pickling them.
    item_threshold : int
        The maximum number of items over which canning will iterate.
        Containers (lists, dicts) larger than this will be pickled without
        introspection.

    Returns
    -------
    [bufs] : list of buffers representing the serialized object.
    """
def deserialize_object(buffers, g: Incomplete | None = None):
    """reconstruct an object serialized by serialize_object from data buffers.

    Parameters
    ----------
    buffers : list of buffers/bytes
    g : globals to be used when uncanning

    Returns
    -------
    (newobj, bufs) : unpacked object, and the list of remaining unused buffers.
    """
def pack_apply_message(f, args, kwargs, buffer_threshold=..., item_threshold=...):
    """pack up a function, args, and kwargs to be sent over the wire

    Each element of args/kwargs will be canned for special treatment,
    but inspection will not go any deeper than that.

    Any object whose data is larger than `threshold`  will not have their data copied
    (only numpy arrays and bytes/buffers support zero-copy)

    Message will be a list of bytes/buffers of the format:

    [ cf, pinfo, <arg_bufs>, <kwarg_bufs> ]

    With length at least two + len(args) + len(kwargs)
    """
def unpack_apply_message(bufs, g: Incomplete | None = None, copy: bool = True):
    """unpack f,args,kwargs from buffers packed by pack_apply_message()
    Returns: original f,args,kwargs"""
