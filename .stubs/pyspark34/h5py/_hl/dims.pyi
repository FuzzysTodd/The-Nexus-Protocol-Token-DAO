from . import base as base
from .. import h5ds as h5ds
from ..h5py_warnings import H5pyDeprecationWarning as H5pyDeprecationWarning
from .base import phil as phil, with_phil as with_phil
from .dataset import Dataset as Dataset

class DimensionProxy(base.CommonStateObject):
    '''
        Represents an HDF5 "dimension".
    '''
    @property
    def label(self):
        """ Get or set the dimension scale label """
    @label.setter
    def label(self, val) -> None: ...
    def __init__(self, id_, dimension) -> None: ...
    def __hash__(self): ...
    def __eq__(self, other): ...
    def __iter__(self): ...
    def __len__(self) -> int: ...
    def __getitem__(self, item): ...
    def attach_scale(self, dset) -> None:
        """ Attach a scale to this dimension.

        Provide the Dataset of the scale you would like to attach.
        """
    def detach_scale(self, dset) -> None:
        """ Remove a scale from this dimension.

        Provide the Dataset of the scale you would like to remove.
        """
    def items(self):
        """ Get a list of (name, Dataset) pairs with all scales on this
        dimension.
        """
    def keys(self):
        """ Get a list of names for the scales on this dimension. """
    def values(self):
        """ Get a list of Dataset for scales on this dimension. """

class DimensionManager(base.CommonStateObject):
    '''
        Represents a collection of dimension associated with a dataset.

        Like AttributeManager, an instance of this class is returned when
        accessing the ".dims" property on a Dataset.
    '''
    def __init__(self, parent) -> None:
        """ Private constructor.
        """
    def __getitem__(self, index):
        """ Return a Dimension object
        """
    def __len__(self) -> int:
        """ Number of dimensions associated with the dataset. """
    def __iter__(self):
        """ Iterate over the dimensions. """
    def create_scale(self, dset, name: str = '') -> None:
        """ Create a new dimension, from an initial scale.

        Provide the dataset and a name for the scale.
        """
