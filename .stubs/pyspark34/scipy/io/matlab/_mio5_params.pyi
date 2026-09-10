import numpy as np
from _typeshed import Incomplete

__all__ = ['MDTYPES', 'MatlabFunction', 'MatlabObject', 'MatlabOpaque', 'NP_TO_MTYPES', 'NP_TO_MXTYPES', 'OPAQUE_DTYPE', 'codecs_template', 'mat_struct', 'mclass_dtypes_template', 'mclass_info', 'mdtypes_template', 'miCOMPRESSED', 'miDOUBLE', 'miINT16', 'miINT32', 'miINT64', 'miINT8', 'miMATRIX', 'miSINGLE', 'miUINT16', 'miUINT32', 'miUINT64', 'miUINT8', 'miUTF16', 'miUTF32', 'miUTF8', 'mxCELL_CLASS', 'mxCHAR_CLASS', 'mxDOUBLE_CLASS', 'mxFUNCTION_CLASS', 'mxINT16_CLASS', 'mxINT32_CLASS', 'mxINT64_CLASS', 'mxINT8_CLASS', 'mxOBJECT_CLASS', 'mxOBJECT_CLASS_FROM_MATRIX_H', 'mxOPAQUE_CLASS', 'mxSINGLE_CLASS', 'mxSPARSE_CLASS', 'mxSTRUCT_CLASS', 'mxUINT16_CLASS', 'mxUINT32_CLASS', 'mxUINT64_CLASS', 'mxUINT8_CLASS']

miINT8: int
miUINT8: int
miINT16: int
miUINT16: int
miINT32: int
miUINT32: int
miSINGLE: int
miDOUBLE: int
miINT64: int
miUINT64: int
miMATRIX: int
miCOMPRESSED: int
miUTF8: int
miUTF16: int
miUTF32: int
mxCELL_CLASS: int
mxSTRUCT_CLASS: int
mxOBJECT_CLASS: int
mxCHAR_CLASS: int
mxSPARSE_CLASS: int
mxDOUBLE_CLASS: int
mxSINGLE_CLASS: int
mxINT8_CLASS: int
mxUINT8_CLASS: int
mxINT16_CLASS: int
mxUINT16_CLASS: int
mxINT32_CLASS: int
mxUINT32_CLASS: int
mxINT64_CLASS: int
mxUINT64_CLASS: int
mxFUNCTION_CLASS: int
mxOPAQUE_CLASS: int
mxOBJECT_CLASS_FROM_MATRIX_H: int
mdtypes_template: Incomplete
mclass_dtypes_template: Incomplete
mclass_info: Incomplete
NP_TO_MTYPES: Incomplete
NP_TO_MXTYPES: Incomplete
codecs_template: Incomplete
MDTYPES: Incomplete

class mat_struct:
    """Placeholder for holding read data from structs.

    We use instances of this class when the user passes False as a value to the
    ``struct_as_record`` parameter of the :func:`scipy.io.loadmat` function.
    """

class MatlabObject(np.ndarray):
    """Subclass of ndarray to signal this is a matlab object.

    This is a simple subclass of :class:`numpy.ndarray` meant to be used
    by :func:`scipy.io.loadmat` and should not be instantiated directly.
    """
    def __new__(cls, input_array, classname: Incomplete | None = None): ...
    classname: Incomplete
    def __array_finalize__(self, obj) -> None: ...

class MatlabFunction(np.ndarray):
    """Subclass for a MATLAB function.

    This is a simple subclass of :class:`numpy.ndarray` meant to be used
    by :func:`scipy.io.loadmat` and should not be directly instantiated.
    """
    def __new__(cls, input_array): ...

class MatlabOpaque(np.ndarray):
    """Subclass for a MATLAB opaque matrix.

    This is a simple subclass of :class:`numpy.ndarray` meant to be used
    by :func:`scipy.io.loadmat` and should not be directly instantiated.
    """
    def __new__(cls, input_array): ...

OPAQUE_DTYPE: Incomplete
