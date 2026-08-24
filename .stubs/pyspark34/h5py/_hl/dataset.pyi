from . import filters as filters
from .. import h5 as h5, h5d as h5d, h5ds as h5ds, h5fd as h5fd, h5p as h5p, h5r as h5r, h5s as h5s, h5t as h5t
from .base import Empty as Empty, HLObject as HLObject, array_for_new_object as array_for_new_object, cached_property as cached_property, find_item_type as find_item_type, phil as phil, product as product, with_phil as with_phil
from .compat import filename_decode as filename_decode
from .datatype import Datatype as Datatype
from .vds import VDSmap as VDSmap, vds_support as vds_support
from _typeshed import Incomplete

MPI: Incomplete

def make_new_dset(parent, shape: Incomplete | None = None, dtype: Incomplete | None = None, data: Incomplete | None = None, name: Incomplete | None = None, chunks: Incomplete | None = None, compression: Incomplete | None = None, shuffle: Incomplete | None = None, fletcher32: Incomplete | None = None, maxshape: Incomplete | None = None, compression_opts: Incomplete | None = None, fillvalue: Incomplete | None = None, scaleoffset: Incomplete | None = None, track_times: bool = False, external: Incomplete | None = None, track_order: Incomplete | None = None, dcpl: Incomplete | None = None, dapl: Incomplete | None = None, efile_prefix: Incomplete | None = None, virtual_prefix: Incomplete | None = None, allow_unknown_filter: bool = False, rdcc_nslots: Incomplete | None = None, rdcc_nbytes: Incomplete | None = None, rdcc_w0: Incomplete | None = None):
    """ Return a new low-level dataset identifier """
def open_dset(parent, name, dapl: Incomplete | None = None, efile_prefix: Incomplete | None = None, virtual_prefix: Incomplete | None = None, rdcc_nslots: Incomplete | None = None, rdcc_nbytes: Incomplete | None = None, rdcc_w0: Incomplete | None = None, **kwds):
    """ Return an existing low-level dataset identifier """

class AstypeWrapper:
    """Wrapper to convert data on reading from a dataset.
    """
    def __init__(self, dset, dtype) -> None: ...
    def __getitem__(self, args): ...
    def __len__(self) -> int:
        """ Get the length of the underlying dataset

        >>> length = len(dataset.astype('f8'))
        """
    def __array__(self, dtype: Incomplete | None = None): ...

class AsStrWrapper:
    """Wrapper to decode strings on reading the dataset"""
    encoding: Incomplete
    errors: Incomplete
    def __init__(self, dset, encoding, errors: str = 'strict') -> None: ...
    def __getitem__(self, args): ...
    def __len__(self) -> int:
        """ Get the length of the underlying dataset

        >>> length = len(dataset.asstr())
        """
    def __array__(self): ...

class FieldsWrapper:
    """Wrapper to extract named fields from a dataset with a struct dtype"""
    extract_field: Incomplete
    read_dtype: Incomplete
    def __init__(self, dset, prior_dtype, names) -> None: ...
    def __array__(self, dtype: Incomplete | None = None): ...
    def __getitem__(self, args): ...
    def __len__(self) -> int:
        """ Get the length of the underlying dataset

        >>> length = len(dataset.fields(['x', 'y']))
        """

def readtime_dtype(basetype, names):
    """Make a NumPy compound dtype with a subset of available fields"""

class CollectiveContext:
    """ Manages collective I/O in MPI mode """
    def __init__(self, dset) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, *args) -> None: ...

class ChunkIterator:
    """
    Class to iterate through list of chunks of a given dataset
    """
    def __init__(self, dset, source_sel: Incomplete | None = None) -> None: ...
    def __iter__(self): ...
    def __next__(self): ...

class Dataset(HLObject):
    """
        Represents an HDF5 dataset
    """
    def astype(self, dtype):
        """ Get a wrapper allowing you to perform reads to a
        different destination type, e.g.:

        >>> double_precision = dataset.astype('f8')[0:100:2]
        """
    def asstr(self, encoding: Incomplete | None = None, errors: str = 'strict'):
        """Get a wrapper to read string data as Python strings:

        >>> str_array = dataset.asstr()[:]

        The parameters have the same meaning as in ``bytes.decode()``.
        If ``encoding`` is unspecified, it will use the encoding in the HDF5
        datatype (either ascii or utf-8).
        """
    def fields(self, names, *, _prior_dtype: Incomplete | None = None):
        """Get a wrapper to read a subset of fields from a compound data type:

        >>> 2d_coords = dataset.fields(['x', 'y'])[:]

        If names is a string, a single field is extracted, and the resulting
        arrays will have that dtype. Otherwise, it should be an iterable,
        and the read data will have a compound dtype.
        """
    @property
    def collective(self):
        """ Context manager for MPI collective reads & writes """
    @property
    def dims(self):
        """ Access dimension scales attached to this dataset. """
    @property
    def ndim(self):
        """Numpy-style attribute giving the number of dimensions"""
    @property
    def shape(self):
        """Numpy-style shape tuple giving dataset dimensions"""
    @shape.setter
    def shape(self, shape) -> None: ...
    @property
    def size(self):
        """Numpy-style attribute giving the total dataset size"""
    @property
    def nbytes(self):
        """Numpy-style attribute giving the raw dataset size as the number of bytes"""
    @property
    def dtype(self):
        """Numpy dtype representing the datatype"""
    @property
    def chunks(self):
        """Dataset chunks (or None)"""
    @property
    def compression(self):
        """Compression strategy (or None)"""
    @property
    def compression_opts(self):
        """ Compression setting.  Int(0-9) for gzip, 2-tuple for szip. """
    @property
    def shuffle(self):
        """Shuffle filter present (T/F)"""
    @property
    def fletcher32(self):
        """Fletcher32 filter is present (T/F)"""
    @property
    def scaleoffset(self):
        """Scale/offset filter settings. For integer data types, this is
        the number of bits stored, or 0 for auto-detected. For floating
        point data types, this is the number of decimal places retained.
        If the scale/offset filter is not in use, this is None."""
    @property
    def external(self):
        """External file settings. Returns a list of tuples of
        (name, offset, size) for each external file entry, or returns None
        if no external files are used."""
    @property
    def maxshape(self):
        """Shape up to which this dataset can be resized.  Axes with value
        None have no resize limit. """
    @property
    def fillvalue(self):
        """Fill value for this dataset (0 by default)"""
    def __init__(self, bind, *, readonly: bool = False) -> None:
        """ Create a new Dataset object by binding to a low-level DatasetID.
        """
    def resize(self, size, axis: Incomplete | None = None) -> None:
        ''' Resize the dataset, or the specified axis.

        The dataset must be stored in chunked format; it can be resized up to
        the "maximum shape" (keyword maxshape) specified at creation time.
        The rank of the dataset cannot be changed.

        "Size" should be a shape tuple, or if an axis is specified, an integer.

        BEWARE: This functions differently than the NumPy resize() method!
        The data is not "reshuffled" to fit in the new shape; each axis is
        grown or shrunk independently.  The coordinates of existing data are
        fixed.
        '''
    def __len__(self) -> int:
        """ The size of the first axis.  TypeError if scalar.

        Limited to 2**32 on 32-bit systems; Dataset.len() is preferred.
        """
    def len(self):
        """ The size of the first axis.  TypeError if scalar.

        Use of this method is preferred to len(dset), as Python's built-in
        len() cannot handle values greater then 2**32 on 32-bit systems.
        """
    def __iter__(self):
        """ Iterate over the first axis.  TypeError if scalar.

        BEWARE: Modifications to the yielded data are *NOT* written to file.
        """
    def iter_chunks(self, sel: Incomplete | None = None):
        """ Return chunk iterator.  If set, the sel argument is a slice or
        tuple of slices that defines the region to be used. If not set, the
        entire dataspace will be used for the iterator.

        For each chunk within the given region, the iterator yields a tuple of
        slices that gives the intersection of the given chunk with the
        selection area.

        A TypeError will be raised if the dataset is not chunked.

        A ValueError will be raised if the selection region is invalid.

        """
    def __getitem__(self, args, new_dtype: Incomplete | None = None):
        ''' Read a slice from the HDF5 dataset.

        Takes slices and recarray-style field names (more than one is
        allowed!) in any order.  Obeys basic NumPy rules, including
        broadcasting.

        Also supports:

        * Boolean "mask" array indexing
        '''
    def __setitem__(self, args, val) -> None:
        ''' Write to the HDF5 dataset from a Numpy array.

        NumPy\'s broadcasting rules are honored, for "simple" indexing
        (slices and integers).  For advanced indexing, the shapes must
        match.
        '''
    def read_direct(self, dest, source_sel: Incomplete | None = None, dest_sel: Incomplete | None = None) -> None:
        """ Read data directly from HDF5 into an existing NumPy array.

        The destination array must be C-contiguous and writable.
        Selections must be the output of numpy.s_[<args>].

        Broadcasting is supported for simple indexing.
        """
    def write_direct(self, source, source_sel: Incomplete | None = None, dest_sel: Incomplete | None = None) -> None:
        """ Write data directly to HDF5 from a NumPy array.

        The source array must be C-contiguous.  Selections must be
        the output of numpy.s_[<args>].

        Broadcasting is supported for simple indexing.
        """
    def __array__(self, dtype: Incomplete | None = None):
        """ Create a Numpy array containing the whole dataset.  DON'T THINK
        THIS MEANS DATASETS ARE INTERCHANGEABLE WITH ARRAYS.  For one thing,
        you have to read the whole dataset every time this method is called.
        """
    def refresh(self) -> None:
        """ Refresh the dataset metadata by reloading from the file.

            This is part of the SWMR features and only exist when the HDF5
            library version >=1.9.178
            """
    def flush(self) -> None:
        """ Flush the dataset data and metadata to the file.
            If the dataset is chunked, raw data chunks are written to the file.

            This is part of the SWMR features and only exist when the HDF5
            library version >=1.9.178
            """
    @property
    def is_virtual(self):
        """Check if this is a virtual dataset"""
    def virtual_sources(self):
        """Get a list of the data mappings for a virtual dataset"""
    def make_scale(self, name: str = '') -> None:
        """Make this dataset an HDF5 dimension scale.

        You can then attach it to dimensions of other datasets like this::

            other_ds.dims[0].attach_scale(ds)

        You can optionally pass a name to associate with this scale.
        """
    @property
    def is_scale(self):
        """Return ``True`` if this dataset is also a dimension scale.

        Return ``False`` otherwise.
        """
