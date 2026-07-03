import numpy as np
from _typeshed import Incomplete
from pyspark.mllib._typing import NormType
from pyspark.sql.types import StructType, UserDefinedType
from typing import Any, Dict, Iterable, List, Tuple, Type, overload

__all__ = ['Vector', 'DenseVector', 'SparseVector', 'Vectors', 'Matrix', 'DenseMatrix', 'SparseMatrix', 'Matrices']

class VectorUDT(UserDefinedType):
    """
    SQL user-defined type (UDT) for Vector.
    """
    @classmethod
    def sqlType(cls) -> StructType: ...
    @classmethod
    def module(cls) -> str: ...
    @classmethod
    def scalaUDT(cls) -> str: ...
    def serialize(self, obj: Vector) -> Tuple[int, int | None, List[int] | None, List[float]]: ...
    def deserialize(self, datum: Tuple[int, int | None, List[int] | None, List[float]]) -> Vector: ...
    def simpleString(self) -> str: ...

class MatrixUDT(UserDefinedType):
    """
    SQL user-defined type (UDT) for Matrix.
    """
    @classmethod
    def sqlType(cls) -> StructType: ...
    @classmethod
    def module(cls) -> str: ...
    @classmethod
    def scalaUDT(cls) -> str: ...
    def serialize(self, obj: Matrix) -> Tuple[int, int, int, List[int] | None, List[int] | None, List[float], bool]: ...
    def deserialize(self, datum: Tuple[int, int, int, List[int] | None, List[int] | None, List[float], bool]) -> Matrix: ...
    def simpleString(self) -> str: ...

class Vector:
    __UDT__: Incomplete
    def toArray(self) -> np.ndarray:
        """
        Convert the vector into an numpy.ndarray

        :return: numpy.ndarray
        """
    def __len__(self) -> int: ...

class DenseVector(Vector):
    """
    A dense vector represented by a value array. We use numpy array for
    storage and arithmetics will be delegated to the underlying numpy
    array.

    Examples
    --------
    >>> v = Vectors.dense([1.0, 2.0])
    >>> u = Vectors.dense([3.0, 4.0])
    >>> v + u
    DenseVector([4.0, 6.0])
    >>> 2 - v
    DenseVector([1.0, 0.0])
    >>> v / 2
    DenseVector([0.5, 1.0])
    >>> v * u
    DenseVector([3.0, 8.0])
    >>> u / v
    DenseVector([3.0, 2.0])
    >>> u % 2
    DenseVector([1.0, 0.0])
    >>> -v
    DenseVector([-1.0, -2.0])
    """
    array: Incomplete
    def __init__(self, ar: bytes | np.ndarray | Iterable[float]) -> None: ...
    def __reduce__(self) -> Tuple[Type['DenseVector'], Tuple[bytes]]: ...
    def numNonzeros(self) -> int:
        """
        Number of nonzero elements. This scans all active values and count non zeros
        """
    def norm(self, p: NormType) -> np.float64:
        """
        Calculates the norm of a DenseVector.

        Examples
        --------
        >>> a = DenseVector([0, -1, 2, -3])
        >>> a.norm(2)
        3.7...
        >>> a.norm(1)
        6.0
        """
    def dot(self, other: Iterable[float]) -> np.float64:
        """
        Compute the dot product of two Vectors. We support
        (Numpy array, list, SparseVector, or SciPy sparse)
        and a target NumPy array that is either 1- or 2-dimensional.
        Equivalent to calling numpy.dot of the two vectors.

        Examples
        --------
        >>> dense = DenseVector(array.array('d', [1., 2.]))
        >>> dense.dot(dense)
        5.0
        >>> dense.dot(SparseVector(2, [0, 1], [2., 1.]))
        4.0
        >>> dense.dot(range(1, 3))
        5.0
        >>> dense.dot(np.array(range(1, 3)))
        5.0
        >>> dense.dot([1.,])
        Traceback (most recent call last):
            ...
        AssertionError: dimension mismatch
        >>> dense.dot(np.reshape([1., 2., 3., 4.], (2, 2), order='F'))
        array([  5.,  11.])
        >>> dense.dot(np.reshape([1., 2., 3.], (3, 1), order='F'))
        Traceback (most recent call last):
            ...
        AssertionError: dimension mismatch
        """
    def squared_distance(self, other: Iterable[float]) -> np.float64:
        """
        Squared distance of two Vectors.

        Examples
        --------
        >>> dense1 = DenseVector(array.array('d', [1., 2.]))
        >>> dense1.squared_distance(dense1)
        0.0
        >>> dense2 = np.array([2., 1.])
        >>> dense1.squared_distance(dense2)
        2.0
        >>> dense3 = [2., 1.]
        >>> dense1.squared_distance(dense3)
        2.0
        >>> sparse1 = SparseVector(2, [0, 1], [2., 1.])
        >>> dense1.squared_distance(sparse1)
        2.0
        >>> dense1.squared_distance([1.,])
        Traceback (most recent call last):
            ...
        AssertionError: dimension mismatch
        >>> dense1.squared_distance(SparseVector(1, [0,], [1.,]))
        Traceback (most recent call last):
            ...
        AssertionError: dimension mismatch
        """
    def toArray(self) -> np.ndarray:
        """
        Returns the underlying numpy.ndarray
        """
    @property
    def values(self) -> np.ndarray:
        """
        Returns the underlying numpy.ndarray
        """
    @overload
    def __getitem__(self, item: int) -> np.float64: ...
    @overload
    def __getitem__(self, item: slice) -> np.ndarray: ...
    def __len__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
    def __getattr__(self, item: str) -> Any: ...
    def __neg__(self) -> DenseVector: ...
    __add__: Incomplete
    __sub__: Incomplete
    __mul__: Incomplete
    __div__: Incomplete
    __truediv__: Incomplete
    __mod__: Incomplete
    __radd__: Incomplete
    __rsub__: Incomplete
    __rmul__: Incomplete
    __rdiv__: Incomplete
    __rtruediv__: Incomplete
    __rmod__: Incomplete

class SparseVector(Vector):
    """
    A simple sparse vector class for passing data to MLlib. Users may
    alternatively pass SciPy's {scipy.sparse} data types.
    """
    @overload
    def __init__(self, size: int, __indices: bytes, __values: bytes) -> None: ...
    @overload
    def __init__(self, size: int, *args: Tuple[int, float]) -> None: ...
    @overload
    def __init__(self, size: int, __indices: Iterable[int], __values: Iterable[float]) -> None: ...
    @overload
    def __init__(self, size: int, __pairs: Iterable[Tuple[int, float]]) -> None: ...
    @overload
    def __init__(self, size: int, __map: Dict[int, float]) -> None: ...
    def numNonzeros(self) -> int:
        """
        Number of nonzero elements. This scans all active values and count non zeros.
        """
    def norm(self, p: NormType) -> np.float64:
        """
        Calculates the norm of a SparseVector.

        Examples
        --------
        >>> a = SparseVector(4, [0, 1], [3., -4.])
        >>> a.norm(1)
        7.0
        >>> a.norm(2)
        5.0
        """
    def __reduce__(self) -> Tuple[Type['SparseVector'], Tuple[int, bytes, bytes]]: ...
    def dot(self, other: Iterable[float]) -> np.float64:
        """
        Dot product with a SparseVector or 1- or 2-dimensional Numpy array.

        Examples
        --------
        >>> a = SparseVector(4, [1, 3], [3.0, 4.0])
        >>> a.dot(a)
        25.0
        >>> a.dot(array.array('d', [1., 2., 3., 4.]))
        22.0
        >>> b = SparseVector(4, [2], [1.0])
        >>> a.dot(b)
        0.0
        >>> a.dot(np.array([[1, 1], [2, 2], [3, 3], [4, 4]]))
        array([ 22.,  22.])
        >>> a.dot([1., 2., 3.])
        Traceback (most recent call last):
            ...
        AssertionError: dimension mismatch
        >>> a.dot(np.array([1., 2.]))
        Traceback (most recent call last):
            ...
        AssertionError: dimension mismatch
        >>> a.dot(DenseVector([1., 2.]))
        Traceback (most recent call last):
            ...
        AssertionError: dimension mismatch
        >>> a.dot(np.zeros((3, 2)))
        Traceback (most recent call last):
            ...
        AssertionError: dimension mismatch
        """
    def squared_distance(self, other: Iterable[float]) -> np.float64:
        """
        Squared distance from a SparseVector or 1-dimensional NumPy array.

        Examples
        --------
        >>> a = SparseVector(4, [1, 3], [3.0, 4.0])
        >>> a.squared_distance(a)
        0.0
        >>> a.squared_distance(array.array('d', [1., 2., 3., 4.]))
        11.0
        >>> a.squared_distance(np.array([1., 2., 3., 4.]))
        11.0
        >>> b = SparseVector(4, [2], [1.0])
        >>> a.squared_distance(b)
        26.0
        >>> b.squared_distance(a)
        26.0
        >>> b.squared_distance([1., 2.])
        Traceback (most recent call last):
            ...
        AssertionError: dimension mismatch
        >>> b.squared_distance(SparseVector(3, [1,], [1.0,]))
        Traceback (most recent call last):
            ...
        AssertionError: dimension mismatch
        """
    def toArray(self) -> np.ndarray:
        """
        Returns a copy of this SparseVector as a 1-dimensional numpy.ndarray.
        """
    def __len__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def __getitem__(self, index: int) -> np.float64: ...
    def __ne__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...

class Vectors:
    """
    Factory methods for working with vectors.

    Notes
    -----
    Dense vectors are simply represented as NumPy array objects,
    so there is no need to covert them for use in MLlib. For sparse vectors,
    the factory methods in this class create an MLlib-compatible type, or users
    can pass in SciPy's `scipy.sparse` column vectors.
    """
    @staticmethod
    @overload
    def sparse(size: int, __indices: bytes, __values: bytes) -> SparseVector: ...
    @staticmethod
    @overload
    def sparse(size: int, *args: Tuple[int, float]) -> SparseVector: ...
    @staticmethod
    @overload
    def sparse(size: int, __indices: Iterable[int], __values: Iterable[float]) -> SparseVector: ...
    @staticmethod
    @overload
    def sparse(size: int, __pairs: Iterable[Tuple[int, float]]) -> SparseVector: ...
    @staticmethod
    @overload
    def sparse(size: int, __map: Dict[int, float]) -> SparseVector: ...
    @overload
    @staticmethod
    def dense(*elements: float) -> DenseVector: ...
    @overload
    @staticmethod
    def dense(__arr: bytes) -> DenseVector: ...
    @overload
    @staticmethod
    def dense(__arr: Iterable[float]) -> DenseVector: ...
    @staticmethod
    def squared_distance(v1: Vector, v2: Vector) -> np.float64:
        """
        Squared distance between two vectors.
        a and b can be of type SparseVector, DenseVector, np.ndarray
        or array.array.

        Examples
        --------
        >>> a = Vectors.sparse(4, [(0, 1), (3, 4)])
        >>> b = Vectors.dense([2, 5, 4, 1])
        >>> a.squared_distance(b)
        51.0
        """
    @staticmethod
    def norm(vector: Vector, p: NormType) -> np.float64:
        """
        Find norm of the given vector.
        """
    @staticmethod
    def zeros(size: int) -> DenseVector: ...

class Matrix:
    __UDT__: Incomplete
    numRows: Incomplete
    numCols: Incomplete
    isTransposed: Incomplete
    def __init__(self, numRows: int, numCols: int, isTransposed: bool = False) -> None: ...
    def toArray(self) -> np.ndarray:
        """
        Returns its elements in a numpy.ndarray.
        """

class DenseMatrix(Matrix):
    """
    Column-major dense matrix.
    """
    values: Incomplete
    def __init__(self, numRows: int, numCols: int, values: bytes | Iterable[float], isTransposed: bool = False) -> None: ...
    def __reduce__(self) -> Tuple[Type['DenseMatrix'], Tuple[int, int, bytes, int]]: ...
    def toArray(self) -> np.ndarray:
        """
        Return a :py:class:`numpy.ndarray`

        Examples
        --------
        >>> m = DenseMatrix(2, 2, range(4))
        >>> m.toArray()
        array([[ 0.,  2.],
               [ 1.,  3.]])
        """
    def toSparse(self) -> SparseMatrix:
        """Convert to SparseMatrix"""
    def __getitem__(self, indices: Tuple[int, int]) -> np.float64: ...
    def __eq__(self, other: Any) -> bool: ...

class SparseMatrix(Matrix):
    """Sparse Matrix stored in CSC format."""
    colPtrs: Incomplete
    rowIndices: Incomplete
    values: Incomplete
    def __init__(self, numRows: int, numCols: int, colPtrs: bytes | Iterable[int], rowIndices: bytes | Iterable[int], values: bytes | Iterable[float], isTransposed: bool = False) -> None: ...
    def __reduce__(self) -> Tuple[Type['SparseMatrix'], Tuple[int, int, bytes, bytes, bytes, int]]: ...
    def __getitem__(self, indices: Tuple[int, int]) -> np.float64: ...
    def toArray(self) -> np.ndarray:
        """
        Return a numpy.ndarray
        """
    def toDense(self) -> DenseMatrix: ...
    def __eq__(self, other: Any) -> bool: ...

class Matrices:
    @staticmethod
    def dense(numRows: int, numCols: int, values: bytes | Iterable[float]) -> DenseMatrix:
        """
        Create a DenseMatrix
        """
    @staticmethod
    def sparse(numRows: int, numCols: int, colPtrs: bytes | Iterable[int], rowIndices: bytes | Iterable[int], values: bytes | Iterable[float]) -> SparseMatrix:
        """
        Create a SparseMatrix
        """
