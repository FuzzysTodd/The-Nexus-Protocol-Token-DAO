from _typeshed import Incomplete
from sympy.core.basic import Basic as Basic
from sympy.core.containers import Tuple as Tuple
from sympy.core.singleton import S as S
from sympy.tensor.array.mutable_ndim_array import MutableNDimArray as MutableNDimArray
from sympy.tensor.array.ndim_array import ArrayKind as ArrayKind, ImmutableNDimArray as ImmutableNDimArray, NDimArray as NDimArray
from sympy.utilities.iterables import flatten as flatten

class DenseNDimArray(NDimArray):
    def __new__(self, *args, **kwargs): ...
    @property
    def kind(self) -> ArrayKind: ...
    def __getitem__(self, index):
        """
        Allows to get items from N-dim array.

        Examples
        ========

        >>> from sympy import MutableDenseNDimArray
        >>> a = MutableDenseNDimArray([0, 1, 2, 3], (2, 2))
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


        Symbolic index:

        >>> from sympy.abc import i, j
        >>> a[i, j]
        [[0, 1], [2, 3]][i, j]

        Replace `i` and `j` to get element `(1, 1)`:

        >>> a[i, j].subs({i: 1, j: 1})
        3

        """
    @classmethod
    def zeros(cls, *shape): ...
    def tomatrix(self):
        """
        Converts MutableDenseNDimArray to Matrix. Can convert only 2-dim array, else will raise error.

        Examples
        ========

        >>> from sympy import MutableDenseNDimArray
        >>> a = MutableDenseNDimArray([1 for i in range(9)], (3, 3))
        >>> b = a.tomatrix()
        >>> b
        Matrix([
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]])

        """
    def reshape(self, *newshape):
        """
        Returns MutableDenseNDimArray instance with new shape. Elements number
        must be        suitable to new shape. The only argument of method sets
        new shape.

        Examples
        ========

        >>> from sympy import MutableDenseNDimArray
        >>> a = MutableDenseNDimArray([1, 2, 3, 4, 5, 6], (2, 3))
        >>> a.shape
        (2, 3)
        >>> a
        [[1, 2, 3], [4, 5, 6]]
        >>> b = a.reshape(3, 2)
        >>> b.shape
        (3, 2)
        >>> b
        [[1, 2], [3, 4], [5, 6]]

        """

class ImmutableDenseNDimArray(DenseNDimArray, ImmutableNDimArray):
    def __new__(cls, iterable, shape: Incomplete | None = None, **kwargs): ...
    def __setitem__(self, index, value) -> None: ...
    def as_mutable(self): ...

class MutableDenseNDimArray(DenseNDimArray, MutableNDimArray):
    def __new__(cls, iterable: Incomplete | None = None, shape: Incomplete | None = None, **kwargs): ...
    def __setitem__(self, index, value) -> None:
        """Allows to set items to MutableDenseNDimArray.

        Examples
        ========

        >>> from sympy import MutableDenseNDimArray
        >>> a = MutableDenseNDimArray.zeros(2,  2)
        >>> a[0,0] = 1
        >>> a[1,1] = 1
        >>> a
        [[1, 0], [0, 1]]

        """
    def as_immutable(self): ...
    @property
    def free_symbols(self): ...
