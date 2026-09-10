import abc
from _typeshed import Incomplete
from jax._src.typing import Array

__all__ = ['c_', 'index_exp', 'mgrid', 'ogrid', 'r_', 's_']

class _Mgrid:
    '''Return dense multi-dimensional "meshgrid".

  LAX-backend implementation of :obj:`numpy.mgrid`. This is a convenience wrapper for
  functionality provided by :func:`jax.numpy.meshgrid` with ``sparse=False``.

  See Also:
    jnp.ogrid: open/sparse version of jnp.mgrid

  Examples:
    Pass ``[start:stop:step]`` to generate values similar to :func:`jax.numpy.arange`:

    >>> jnp.mgrid[0:4:1]
    Array([0, 1, 2, 3], dtype=int32)

    Passing an imaginary step generates values similar to :func:`jax.numpy.linspace`:

    >>> jnp.mgrid[0:1:4j]
    Array([0.        , 0.33333334, 0.6666667 , 1.        ], dtype=float32)

    Multiple slices can be used to create broadcasted grids of indices:

    >>> jnp.mgrid[:2, :3]
    Array([[[0, 0, 0],
            [1, 1, 1]],
           [[0, 1, 2],
            [0, 1, 2]]], dtype=int32)
  '''
    def __getitem__(self, key: slice | tuple[slice, ...]) -> Array: ...

mgrid: Incomplete

class _Ogrid:
    '''Return open multi-dimensional "meshgrid".

  LAX-backend implementation of :obj:`numpy.ogrid`. This is a convenience wrapper for
  functionality provided by :func:`jax.numpy.meshgrid` with ``sparse=True``.

  See Also:
    jnp.mgrid: dense version of jnp.ogrid

  Examples:
    Pass ``[start:stop:step]`` to generate values similar to :func:`jax.numpy.arange`:

    >>> jnp.ogrid[0:4:1]
    Array([0, 1, 2, 3], dtype=int32)

    Passing an imaginary step generates values similar to :func:`jax.numpy.linspace`:

    >>> jnp.ogrid[0:1:4j]
    Array([0.        , 0.33333334, 0.6666667 , 1.        ], dtype=float32)

    Multiple slices can be used to create sparse grids of indices:

    >>> jnp.ogrid[:2, :3]
    [Array([[0],
            [1]], dtype=int32),
     Array([[0, 1, 2]], dtype=int32)]
  '''
    def __getitem__(self, key: slice | tuple[slice, ...]) -> Array | list[Array]: ...

ogrid: Incomplete

class _AxisConcat(abc.ABC):
    """Concatenates slices, scalars and array-like objects along a given axis."""
    axis: int
    ndmin: int
    trans1d: int
    op_name: str
    def __getitem__(self, key: _IndexType | tuple[_IndexType, ...]) -> Array: ...
    def __len__(self) -> int: ...

class RClass(_AxisConcat):
    '''Concatenate slices, scalars and array-like objects along the first axis.

  LAX-backend implementation of :obj:`numpy.r_`.

  See Also:
    ``jnp.c_``: Concatenates slices, scalars and array-like objects along the last axis.

  Examples:
    Passing slices in the form ``[start:stop:step]`` generates ``jnp.arange`` objects:

    >>> jnp.r_[-1:5:1, 0, 0, jnp.array([1,2,3])]
    Array([-1,  0,  1,  2,  3,  4,  0,  0,  1,  2,  3], dtype=int32)

    An imaginary value for ``step`` will create a ``jnp.linspace`` object instead,
    which includes the right endpoint:

    >>> jnp.r_[-1:1:6j, 0, jnp.array([1,2,3])]
    Array([-1.        , -0.6       , -0.20000002,  0.20000005,
           0.6       ,  1.        ,  0.        ,  1.        ,
           2.        ,  3.        ], dtype=float32)

    Use a string directive of the form ``"axis,dims,trans1d"`` as the first argument to
    specify concatenation axis, minimum number of dimensions, and the position of the
    upgraded array\'s original dimensions in the resulting array\'s shape tuple:

    >>> jnp.r_[\'0,2\', [1,2,3], [4,5,6]] # concatenate along first axis, 2D output
    Array([[1, 2, 3],
           [4, 5, 6]], dtype=int32)

    >>> jnp.r_[\'0,2,0\', [1,2,3], [4,5,6]] # push last input axis to the front
    Array([[1],
           [2],
           [3],
           [4],
           [5],
           [6]], dtype=int32)

    Negative values for ``trans1d`` offset the last axis towards the start
    of the shape tuple:

    >>> jnp.r_[\'0,2,-2\', [1,2,3], [4,5,6]]
    Array([[1],
           [2],
           [3],
           [4],
           [5],
           [6]], dtype=int32)

    Use the special directives ``"r"`` or ``"c"`` as the first argument on flat inputs
    to create an array with an extra row or column axis, respectively:

    >>> jnp.r_[\'r\',[1,2,3], [4,5,6]]
    Array([[1, 2, 3, 4, 5, 6]], dtype=int32)

    >>> jnp.r_[\'c\',[1,2,3], [4,5,6]]
    Array([[1],
           [2],
           [3],
           [4],
           [5],
           [6]], dtype=int32)

    For higher-dimensional inputs (``dim >= 2``), both directives ``"r"`` and ``"c"``
    give the same result.
  '''
    axis: int
    ndmin: int
    trans1d: int
    op_name: str

r_: Incomplete

class CClass(_AxisConcat):
    '''Concatenate slices, scalars and array-like objects along the last axis.

  LAX-backend implementation of :obj:`numpy.c_`.

  See Also:
    ``jnp.r_``: Concatenates slices, scalars and array-like objects along the first axis.

  Examples:

    >>> a = jnp.arange(6).reshape((2,3))
    >>> jnp.c_[a,a]
    Array([[0, 1, 2, 0, 1, 2],
           [3, 4, 5, 3, 4, 5]], dtype=int32)

    Use a string directive of the form ``"axis:dims:trans1d"`` as the first argument to specify
    concatenation axis, minimum number of dimensions, and the position of the upgraded array\'s
    original dimensions in the resulting array\'s shape tuple:

    >>> jnp.c_[\'0,2\', [1,2,3], [4,5,6]]
    Array([[1],
           [2],
           [3],
           [4],
           [5],
           [6]], dtype=int32)

    >>> jnp.c_[\'0,2,-1\', [1,2,3], [4,5,6]]
    Array([[1, 2, 3],
           [4, 5, 6]], dtype=int32)

    Use the special directives ``"r"`` or ``"c"`` as the first argument on flat inputs
    to create an array with inputs stacked along the last axis:

    >>> jnp.c_[\'r\',[1,2,3], [4,5,6]]
    Array([[1, 4],
           [2, 5],
           [3, 6]], dtype=int32)
  '''
    axis: int
    ndmin: int
    trans1d: int
    op_name: str

c_: Incomplete
s_: Incomplete
index_exp: Incomplete
