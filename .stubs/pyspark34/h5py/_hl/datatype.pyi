from ..h5t import TypeID as TypeID
from .base import HLObject as HLObject, with_phil as with_phil

class Datatype(HLObject):
    '''
        Represents an HDF5 named datatype stored in a file.

        To store a datatype, simply assign it to a name in a group:

        >>> MyGroup["name"] = numpy.dtype("f")
        >>> named_type = MyGroup["name"]
        >>> assert named_type.dtype == numpy.dtype("f")
    '''
    @property
    def dtype(self):
        """Numpy dtype equivalent for this datatype"""
    def __init__(self, bind) -> None:
        """ Create a new Datatype object by binding to a low-level TypeID.
        """
