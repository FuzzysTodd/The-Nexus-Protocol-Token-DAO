from . import base as base
from .. import h5 as h5, h5a as h5a, h5p as h5p, h5s as h5s, h5t as h5t
from .base import Empty as Empty, is_empty_dataspace as is_empty_dataspace, phil as phil, product as product, with_phil as with_phil
from .datatype import Datatype as Datatype
from _typeshed import Incomplete

class AttributeManager(base.MutableMappingHDF5, base.CommonStateObject):
    """
        Allows dictionary-style access to an HDF5 object's attributes.

        These are created exclusively by the library and are available as
        a Python attribute at <object>.attrs

        Like Group objects, attributes provide a minimal dictionary-
        style interface.  Anything which can be reasonably converted to a
        Numpy array or Numpy scalar can be stored.

        Attributes are automatically created on assignment with the
        syntax <obj>.attrs[name] = value, with the HDF5 type automatically
        deduced from the value.  Existing attributes are overwritten.

        To modify an existing attribute while preserving its type, use the
        method modify().  To specify an attribute of a particular type and
        shape, use create().
    """
    def __init__(self, parent) -> None:
        """ Private constructor.
        """
    def __getitem__(self, name):
        """ Read the value of an attribute.
        """
    def get_id(self, name):
        """Get a low-level AttrID object for the named attribute.
        """
    def __setitem__(self, name, value) -> None:
        """ Set a new attribute, overwriting any existing attribute.

        The type and shape of the attribute are determined from the data.  To
        use a specific type or shape, or to preserve the type of an attribute,
        use the methods create() and modify().
        """
    def __delitem__(self, name) -> None:
        """ Delete an attribute (which must already exist). """
    def create(self, name, data, shape: Incomplete | None = None, dtype: Incomplete | None = None) -> None:
        """ Create a new attribute, overwriting any existing attribute.

        name
            Name of the new attribute (required)
        data
            An array to initialize the attribute (required)
        shape
            Shape of the attribute.  Overrides data.shape if both are
            given, in which case the total number of points must be unchanged.
        dtype
            Data type of the attribute.  Overrides data.dtype if both
            are given.
        """
    def modify(self, name, value) -> None:
        """ Change the value of an attribute while preserving its type.

        Differs from __setitem__ in that if the attribute already exists, its
        type is preserved.  This can be very useful for interacting with
        externally generated files.

        If the attribute doesn't exist, it will be automatically created.
        """
    def __len__(self) -> int:
        """ Number of attributes attached to the object. """
    def __iter__(self):
        """ Iterate over the names of attributes. """
    def __contains__(self, name) -> bool:
        """ Determine if an attribute exists, by name. """
