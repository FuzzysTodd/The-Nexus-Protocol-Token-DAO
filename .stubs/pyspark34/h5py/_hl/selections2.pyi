from .. import h5s as h5s
from _typeshed import Incomplete

def read_dtypes(dataset_dtype, names):
    """ Returns a 2-tuple containing:

    1. Output dataset dtype
    2. Dtype containing HDF5-appropriate description of destination
    """
def read_selections_scalar(dsid, args):
    """ Returns a 2-tuple containing:

    1. Output dataset shape
    2. HDF5 dataspace containing source selection.

    Works for scalar datasets.
    """

class ScalarReadSelection:
    """
        Implements slicing for scalar datasets.
    """
    mshape: Incomplete
    mspace: Incomplete
    fspace: Incomplete
    def __init__(self, fspace, args) -> None: ...
    def __iter__(self): ...

def select_read(fspace, args):
    """ Top-level dispatch function for reading.

    At the moment, only supports reading from scalar datasets.
    """
