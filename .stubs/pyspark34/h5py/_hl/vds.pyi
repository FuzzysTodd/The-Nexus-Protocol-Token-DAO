from .. import h5d as h5d, h5p as h5p, h5s as h5s, h5t as h5t
from .compat import filename_encode as filename_encode
from .datatype import Datatype as Datatype
from .selections import SimpleSelection as SimpleSelection, select as select
from _typeshed import Incomplete
from typing import NamedTuple

class VDSmap(NamedTuple('VDSmap', [('vspace', Incomplete), ('file_name', Incomplete), ('dset_name', Incomplete), ('src_space', Incomplete)])):
    """Defines a region in a virtual dataset mapping to part of a source dataset
    """

vds_support: bool

class VirtualSource:
    """Source definition for virtual data sets.

    Instantiate this class to represent an entire source dataset, and then
    slice it to indicate which regions should be used in the virtual dataset.

    path_or_dataset
        The path to a file, or an h5py dataset. If a dataset is given,
        no other parameters are allowed, as the relevant values are taken from
        the dataset instead.
    name
        The name of the source dataset within the file.
    shape
        A tuple giving the shape of the dataset.
    dtype
        Numpy dtype or string.
    maxshape
        The source dataset is resizable up to this shape. Use None for
        axes you want to be unlimited.
    """
    path: Incomplete
    name: Incomplete
    dtype: Incomplete
    maxshape: Incomplete
    sel: Incomplete
    def __init__(self, path_or_dataset, name: Incomplete | None = None, shape: Incomplete | None = None, dtype: Incomplete | None = None, maxshape: Incomplete | None = None) -> None: ...
    @property
    def shape(self): ...
    def __getitem__(self, key): ...

class VirtualLayout:
    """Object for building a virtual dataset.

    Instantiate this class to define a virtual dataset, assign to slices of it
    (using VirtualSource objects), and then pass it to
    group.create_virtual_dataset() to add the virtual dataset to a file.

    This class does not allow access to the data; the virtual dataset must
    be created in a file before it can be used.

    shape
        A tuple giving the shape of the dataset.
    dtype
        Numpy dtype or string.
    maxshape
        The virtual dataset is resizable up to this shape. Use None for
        axes you want to be unlimited.
    filename
        The name of the destination file, if known in advance. Mappings from
        data in the same file will be stored with filename '.', allowing the
        file to be renamed later.
    """
    shape: Incomplete
    dtype: Incomplete
    maxshape: Incomplete
    dcpl: Incomplete
    def __init__(self, shape, dtype, maxshape: Incomplete | None = None, filename: Incomplete | None = None) -> None: ...
    def __setitem__(self, key, source) -> None: ...
    def make_dataset(self, parent, name, fillvalue: Incomplete | None = None):
        """ Return a new low-level dataset identifier for a virtual dataset """
