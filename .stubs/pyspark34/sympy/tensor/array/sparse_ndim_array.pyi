from _typeshed import Incomplete
from sympy.core.basic import Basic as Basic
from sympy.core.containers import Dict as Dict, Tuple as Tuple
from sympy.core.singleton import S as S
from sympy.tensor.array.mutable_ndim_array import MutableNDimArray as MutableNDimArray
from sympy.tensor.array.ndim_array import ImmutableNDimArray as ImmutableNDimArray, NDimArray as NDimArray
from sympy.utilities.iterables import flatten as flatten

class SparseNDimArray(NDimArray):
    def __new__(self, *args, **kwargs): ...
    def __getitem__(self, index):
        """
        Get an element from a sparse N-dim array.

        Examples
        ========

        >>> from sympy import MutableSparseNDimArray
        >>> a = MutableSparseNDimArray(range(4), (2, 2))
        >>> a
        [[0, 1], [2, 3]]
        >>> a[0, 0]
        0
        >>> a[1, 1]
        3
        >>> a[0]
        [0, 1]
        >>> a[1]
        [2, 3]

        Symbolic indexing:

        >>> from sympy.abc import i, j
        >>> a[i, j]
        [[0, 1], [2, 3]][i, j]

        Replace `i` and `j` to get element `(0, 0)`:

        >>> a[i, j].subs({i: 0, j: 0})
        0

        """
    @classmethod
    def zeros(cls, *shape):
        """
        Return a sparse N-dim array of zeros.
        """
    def tomatrix(self):
        """
        Converts MutableDenseNDimArray to Matrix. Can convert only 2-dim array, else will raise error.

        Examples
        ========

        >>> from sympy import MutableSparseNDimArray
        >>> a = MutableSparseNDimArray([1 for i in range(9)], (3, 3))
        >>> b = a.tomatrix()
        >>> b
        Matrix([
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]])
        """
    def reshape(self, *newshape): ...

class ImmutableSparseNDimArray(SparseNDimArray, ImmutableNDimArray):
    def __new__(cls, iterable: Incomplete | None = None, shape: Incomplete | None = None, **kwargs): ...
    def __setitem__(self, index, value) -> None: ...
    def as_mutable(self): ...

class MutableSparseNDimArray(MutableNDimArray, SparseNDimArray):
    def __new__(cls, iterable: Incomplete | None = None, shape: Incomplete | None = None, **kwargs): ...
    def __setitem__(self, index, value) -> None:
        """Allows to set items to MutableDenseNDimArray.

        Examples
        ========

        >>> from sympy import MutableSparseNDimArray
        >>> a = MutableSparseNDimArray.zeros(2, 2)
        >>> a[0, 0] = 1
        >>> a[1, 1] = 1
        >>> a
        [[1, 0], [0, 1]]
        """
    def as_immutable(self): ...
    @property
    def free_symbols(self): ...
