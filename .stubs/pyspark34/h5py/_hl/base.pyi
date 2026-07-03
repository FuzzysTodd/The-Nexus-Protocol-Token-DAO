import abc
from .. import h5d as h5d, h5f as h5f, h5i as h5i, h5p as h5p, h5r as h5r, h5s as h5s, h5t as h5t
from .._objects import phil as phil, with_phil as with_phil
from .compat import filename_encode as filename_encode, fspath as fspath
from _typeshed import Incomplete
from collections.abc import Generator, ItemsView, KeysView, Mapping, MutableMapping, ValuesView

def is_hdf5(fname):
    """ Determine if a file is valid HDF5 (False if it doesn't exist). """
def find_item_type(data):
    """Find the item type of a simple object or collection of objects.

    E.g. [[['a']]] -> str

    The focus is on collections where all items have the same type; we'll return
    None if that's not the case.

    The aim is to treat numpy arrays of Python objects like normal Python
    collections, while treating arrays with specific dtypes differently.
    We're also only interested in array-like collections - lists and tuples,
    possibly nested - not things like sets or dicts.
    """
def guess_dtype(data):
    """ Attempt to guess an appropriate dtype for the object, returning None
    if nothing is appropriate (or if it should be left up the the array
    constructor to figure out)
    """
def is_float16_dtype(dt): ...
def array_for_new_object(data, specified_dtype: Incomplete | None = None):
    """Prepare an array from data used to create a new dataset or attribute"""
def default_lapl():
    """ Default link access property list """
def default_lcpl():
    """ Default link creation property list """

dlapl: Incomplete
dlcpl: Incomplete

def is_empty_dataspace(obj):
    """ Check if an object's dataspace is empty """

class CommonStateObject:
    '''
        Mixin class that allows sharing information between objects which
        reside in the same HDF5 file.  Requires that the host class have
        a ".id" attribute which returns a low-level ObjectID subclass.

        Also implements Unicode operations.
    '''

class _RegionProxy:
    """
        Proxy object which handles region references.

        To create a new region reference (datasets only), use slicing syntax:

            >>> newref = obj.regionref[0:10:2]

        To determine the target dataset shape from an existing reference:

            >>> shape = obj.regionref.shape(existingref)

        where <obj> may be any object in the file. To determine the shape of
        the selection in use on the target dataset:

            >>> selection_shape = obj.regionref.selection(existingref)
    """
    obj: Incomplete
    id: Incomplete
    def __init__(self, obj) -> None: ...
    def __getitem__(self, args): ...
    def shape(self, ref):
        """ Get the shape of the target dataspace referred to by *ref*. """
    def selection(self, ref):
        """ Get the shape of the target dataspace selection referred to by *ref*
        """

class HLObject(CommonStateObject):
    """
        Base class for high-level interface objects.
    """
    @property
    def file(self):
        """ Return a File instance associated with this object """
    @property
    def name(self):
        """ Return the full name of this object.  None if anonymous. """
    @property
    def parent(self):
        """Return the parent group of this object.

        This is always equivalent to obj.file[posixpath.dirname(obj.name)].
        ValueError if this object is anonymous.
        """
    @property
    def id(self):
        """ Low-level identifier appropriate for this object """
    @property
    def ref(self):
        """ An (opaque) HDF5 reference to this object """
    @property
    def regionref(self):
        """Create a region reference (Datasets only).

        The syntax is regionref[<slices>]. For example, dset.regionref[...]
        creates a region reference in which the whole dataset is selected.

        Can also be used to determine the shape of the referenced dataset
        (via .shape property), or the shape of the selection (via the
        .selection property).
        """
    @property
    def attrs(self):
        """ Attributes attached to this object """
    def __init__(self, oid) -> None:
        """ Setup this object, given its low-level identifier """
    def __hash__(self): ...
    def __eq__(self, other): ...
    def __bool__(self) -> bool: ...
    __nonzero__ = __bool__
    def __getnewargs__(self) -> None:
        """Disable pickle.

        Handles for HDF5 objects can't be reliably deserialised, because the
        recipient may not have access to the same files. So we do this to
        fail early.

        If you really want to pickle h5py objects and can live with some
        limitations, look at the h5pickle project on PyPI.
        """

class KeysViewHDF5(KeysView):
    def __reversed__(self) -> Generator[Incomplete, Incomplete, None]: ...

class ValuesViewHDF5(ValuesView):
    """
        Wraps e.g. a Group or AttributeManager to provide a value view.

        Note that __contains__ will have poor performance as it has
        to scan all the links or attributes.
    """
    def __contains__(self, value) -> bool: ...
    def __iter__(self): ...
    def __reversed__(self) -> Generator[Incomplete, None, None]: ...

class ItemsViewHDF5(ItemsView):
    """
        Wraps e.g. a Group or AttributeManager to provide an items view.
    """
    def __contains__(self, item) -> bool: ...
    def __iter__(self): ...
    def __reversed__(self) -> Generator[Incomplete, None, None]: ...

class MappingHDF5(Mapping, metaclass=abc.ABCMeta):
    """
        Wraps a Group, AttributeManager or DimensionManager object to provide
        an immutable mapping interface.

        We don't inherit directly from MutableMapping because certain
        subclasses, for example DimensionManager, are read-only.
    """
    def keys(self):
        """ Get a view object on member names """
    def values(self):
        """ Get a view object on member objects """
    def items(self):
        """ Get a view object on member items """

class MutableMappingHDF5(MappingHDF5, MutableMapping, metaclass=abc.ABCMeta):
    """
        Wraps a Group or AttributeManager object to provide a mutable
        mapping interface, in contrast to the read-only mapping of
        MappingHDF5.
    """

class Empty:
    """
        Proxy object to represent empty/null dataspaces (a.k.a H5S_NULL).

        This can have an associated dtype, but has no shape or data. This is not
        the same as an array with shape (0,).
    """
    shape: Incomplete
    size: Incomplete
    dtype: Incomplete
    def __init__(self, dtype) -> None: ...
    def __eq__(self, other): ...

def product(nums):
    """Calculate a numeric product

    For small amounts of data (e.g. shape tuples), this simple code is much
    faster than calling numpy.prod().
    """

class cached_property:
    __doc__: Incomplete
    func: Incomplete
    def __init__(self, func) -> None: ...
    def __get__(self, obj, cls): ...
