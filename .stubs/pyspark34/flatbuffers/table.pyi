from . import encode as encode
from _typeshed import Incomplete

class Table:
    """Table wraps a byte slice and provides read access to its data.

    The variable `Pos` indicates the root of the FlatBuffers object therein."""
    Bytes: Incomplete
    Pos: Incomplete
    def __init__(self, buf, pos) -> None: ...
    def Offset(self, vtableOffset):
        """Offset provides access into the Table's vtable.

        Deprecated fields are ignored by checking the vtable's length."""
    def Indirect(self, off):
        """Indirect retrieves the relative offset stored at `offset`."""
    def String(self, off):
        """String gets a string from data stored inside the flatbuffer."""
    def VectorLen(self, off):
        '''VectorLen retrieves the length of the vector whose offset is stored
           at "off" in this object.'''
    def Vector(self, off):
        '''Vector retrieves the start of data of the vector whose offset is
           stored at "off" in this object.'''
    def Union(self, t2, off) -> None:
        """Union initializes any Table-derived type to point to the union at
           the given offset."""
    def Get(self, flags, off):
        """
        Get retrieves a value of the type specified by `flags`  at the
        given offset.
        """
    def GetSlot(self, slot, d, validator_flags): ...
    def GetVectorAsNumpy(self, flags, off):
        """
        GetVectorAsNumpy returns the vector that starts at `Vector(off)`
        as a numpy array with the type specified by `flags`. The array is
        a `view` into Bytes, so modifying the returned array will
        modify Bytes in place.
        """
    def GetArrayAsNumpy(self, flags, off, length):
        """
        GetArrayAsNumpy returns the array with fixed width that starts at `Vector(offset)`
        with length `length` as a numpy array with the type specified by `flags`. The
        array is a `view` into Bytes so modifying the returned will modify Bytes in place.
        """
    def GetVOffsetTSlot(self, slot, d):
        """
        GetVOffsetTSlot retrieves the VOffsetT that the given vtable location
        points to. If the vtable value is zero, the default value `d`
        will be returned.
        """
