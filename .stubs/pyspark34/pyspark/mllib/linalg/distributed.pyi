from _typeshed import Incomplete
from pyspark import RDD
from pyspark.ml._typing import VectorLike
from pyspark.mllib.common import JavaModelWrapper
from pyspark.mllib.linalg import Matrix, QRDecomposition, Vector
from pyspark.mllib.stat import MultivariateStatisticalSummary
from pyspark.sql import DataFrame
from pyspark.storagelevel import StorageLevel
from typing import Generic, Tuple, TypeVar

__all__ = ['BlockMatrix', 'CoordinateMatrix', 'DistributedMatrix', 'IndexedRow', 'IndexedRowMatrix', 'MatrixEntry', 'RowMatrix', 'SingularValueDecomposition']

UT = TypeVar('UT', bound='DistributedMatrix')
VT = TypeVar('VT', bound='Matrix')

class DistributedMatrix:
    """
    Represents a distributively stored matrix backed by one or
    more RDDs.

    """
    def numRows(self) -> int:
        """Get or compute the number of rows."""
    def numCols(self) -> int:
        """Get or compute the number of cols."""

class RowMatrix(DistributedMatrix):
    """
    Represents a row-oriented distributed Matrix with no meaningful
    row indices.


    Parameters
    ----------
    rows : :py:class:`pyspark.RDD` or :py:class:`pyspark.sql.DataFrame`
        An RDD or DataFrame of vectors. If a DataFrame is provided, it must have a single
        vector typed column.
    numRows : int, optional
        Number of rows in the matrix. A non-positive
        value means unknown, at which point the number
        of rows will be determined by the number of
        records in the `rows` RDD.
    numCols : int, optional
        Number of columns in the matrix. A non-positive
        value means unknown, at which point the number
        of columns will be determined by the size of
        the first row.
    """
    def __init__(self, rows: RDD[Vector] | DataFrame, numRows: int = 0, numCols: int = 0) -> None:
        """
        Note: This docstring is not shown publicly.

        Create a wrapper over a Java RowMatrix.

        Publicly, we require that `rows` be an RDD or DataFrame.  However, for
        internal usage, `rows` can also be a Java RowMatrix
        object, in which case we can wrap it directly.  This
        assists in clean matrix conversions.

        Examples
        --------
        >>> rows = sc.parallelize([[1, 2, 3], [4, 5, 6]])
        >>> mat = RowMatrix(rows)

        >>> mat_diff = RowMatrix(rows)
        >>> (mat_diff._java_matrix_wrapper._java_model ==
        ...  mat._java_matrix_wrapper._java_model)
        False

        >>> mat_same = RowMatrix(mat._java_matrix_wrapper._java_model)
        >>> (mat_same._java_matrix_wrapper._java_model ==
        ...  mat._java_matrix_wrapper._java_model)
        True
        """
    @property
    def rows(self) -> RDD[Vector]:
        """
        Rows of the RowMatrix stored as an RDD of vectors.

        Examples
        --------
        >>> mat = RowMatrix(sc.parallelize([[1, 2, 3], [4, 5, 6]]))
        >>> rows = mat.rows
        >>> rows.first()
        DenseVector([1.0, 2.0, 3.0])
        """
    def numRows(self) -> int:
        """
        Get or compute the number of rows.

        Examples
        --------
        >>> rows = sc.parallelize([[1, 2, 3], [4, 5, 6],
        ...                        [7, 8, 9], [10, 11, 12]])

        >>> mat = RowMatrix(rows)
        >>> print(mat.numRows())
        4

        >>> mat = RowMatrix(rows, 7, 6)
        >>> print(mat.numRows())
        7
        """
    def numCols(self) -> int:
        """
        Get or compute the number of cols.

        Examples
        --------
        >>> rows = sc.parallelize([[1, 2, 3], [4, 5, 6],
        ...                        [7, 8, 9], [10, 11, 12]])

        >>> mat = RowMatrix(rows)
        >>> print(mat.numCols())
        3

        >>> mat = RowMatrix(rows, 7, 6)
        >>> print(mat.numCols())
        6
        """
    def computeColumnSummaryStatistics(self) -> MultivariateStatisticalSummary:
        """
        Computes column-wise summary statistics.

        .. versionadded:: 2.0.0

        Returns
        -------
        :py:class:`MultivariateStatisticalSummary`
            object containing column-wise summary statistics.

        Examples
        --------
        >>> rows = sc.parallelize([[1, 2, 3], [4, 5, 6]])
        >>> mat = RowMatrix(rows)

        >>> colStats = mat.computeColumnSummaryStatistics()
        >>> colStats.mean()
        array([ 2.5,  3.5,  4.5])
        """
    def computeCovariance(self) -> Matrix:
        """
        Computes the covariance matrix, treating each row as an
        observation.

        .. versionadded:: 2.0.0

        Notes
        -----
        This cannot be computed on matrices with more than 65535 columns.

        Examples
        --------
        >>> rows = sc.parallelize([[1, 2], [2, 1]])
        >>> mat = RowMatrix(rows)

        >>> mat.computeCovariance()
        DenseMatrix(2, 2, [0.5, -0.5, -0.5, 0.5], 0)
        """
    def computeGramianMatrix(self) -> Matrix:
        """
        Computes the Gramian matrix `A^T A`.

        .. versionadded:: 2.0.0

        Notes
        -----
        This cannot be computed on matrices with more than 65535 columns.

        Examples
        --------
        >>> rows = sc.parallelize([[1, 2, 3], [4, 5, 6]])
        >>> mat = RowMatrix(rows)

        >>> mat.computeGramianMatrix()
        DenseMatrix(3, 3, [17.0, 22.0, 27.0, 22.0, 29.0, 36.0, 27.0, 36.0, 45.0], 0)
        """
    def columnSimilarities(self, threshold: float = 0.0) -> CoordinateMatrix:
        """
        Compute similarities between columns of this matrix.

        The threshold parameter is a trade-off knob between estimate
        quality and computational cost.

        The default threshold setting of 0 guarantees deterministically
        correct results, but uses the brute-force approach of computing
        normalized dot products.

        Setting the threshold to positive values uses a sampling
        approach and incurs strictly less computational cost than the
        brute-force approach. However the similarities computed will
        be estimates.

        The sampling guarantees relative-error correctness for those
        pairs of columns that have similarity greater than the given
        similarity threshold.

        To describe the guarantee, we set some notation:

        - Let A be the smallest in magnitude non-zero element of
          this matrix.
        - Let B be the largest in magnitude non-zero element of
          this matrix.
        - Let L be the maximum number of non-zeros per row.

        For example, for {0,1} matrices: A=B=1.
        Another example, for the Netflix matrix: A=1, B=5

        For those column pairs that are above the threshold, the
        computed similarity is correct to within 20% relative error
        with probability at least 1 - (0.981)^10/B^

        The shuffle size is bounded by the *smaller* of the following
        two expressions:

        - O(n log(n) L / (threshold * A))
        - O(m L^2^)

        The latter is the cost of the brute-force approach, so for
        non-zero thresholds, the cost is always cheaper than the
        brute-force approach.

        .. versionadded:: 2.0.0

        Parameters
        ----------
        threshold : float, optional
            Set to 0 for deterministic guaranteed
            correctness. Similarities above this
            threshold are estimated with the cost vs
            estimate quality trade-off described above.

        Returns
        -------
        :py:class:`CoordinateMatrix`
            An n x n sparse upper-triangular CoordinateMatrix of
            cosine similarities between columns of this matrix.

        Examples
        --------
        >>> rows = sc.parallelize([[1, 2], [1, 5]])
        >>> mat = RowMatrix(rows)

        >>> sims = mat.columnSimilarities()
        >>> sims.entries.first().value
        0.91914503...
        """
    def tallSkinnyQR(self, computeQ: bool = False) -> QRDecomposition[RowMatrix | None, Matrix]:
        '''
        Compute the QR decomposition of this RowMatrix.

        The implementation is designed to optimize the QR decomposition
        (factorization) for the RowMatrix of a tall and skinny shape [1]_.

        .. [1] Paul G. Constantine, David F. Gleich. "Tall and skinny QR
            factorizations in MapReduce architectures"
            https://doi.org/10.1145/1996092.1996103

        .. versionadded:: 2.0.0

        Parameters
        ----------
        computeQ : bool, optional
            whether to computeQ

        Returns
        -------
        :py:class:`pyspark.mllib.linalg.QRDecomposition`
            QRDecomposition(Q: RowMatrix, R: Matrix), where
            Q = None if computeQ = false.

        Examples
        --------
        >>> rows = sc.parallelize([[3, -6], [4, -8], [0, 1]])
        >>> mat = RowMatrix(rows)
        >>> decomp = mat.tallSkinnyQR(True)
        >>> Q = decomp.Q
        >>> R = decomp.R

        >>> # Test with absolute values
        >>> absQRows = Q.rows.map(lambda row: abs(row.toArray()).tolist())
        >>> absQRows.collect()
        [[0.6..., 0.0], [0.8..., 0.0], [0.0, 1.0]]

        >>> # Test with absolute values
        >>> abs(R.toArray()).tolist()
        [[5.0, 10.0], [0.0, 1.0]]
        '''
    def computeSVD(self, k: int, computeU: bool = False, rCond: float = 1e-09) -> SingularValueDecomposition[RowMatrix, Matrix]:
        """
        Computes the singular value decomposition of the RowMatrix.

        The given row matrix A of dimension (m X n) is decomposed into
        U * s * V'T where

        - U: (m X k) (left singular vectors) is a RowMatrix whose
          columns are the eigenvectors of (A X A')
        - s: DenseVector consisting of square root of the eigenvalues
          (singular values) in descending order.
        - v: (n X k) (right singular vectors) is a Matrix whose columns
          are the eigenvectors of (A' X A)

        For more specific details on implementation, please refer
        the Scala documentation.

        .. versionadded:: 2.2.0

        Parameters
        ----------
        k : int
            Number of leading singular values to keep (`0 < k <= n`).
            It might return less than k if there are numerically zero singular values
            or there are not enough Ritz values converged before the maximum number of
            Arnoldi update iterations is reached (in case that matrix A is ill-conditioned).
        computeU : bool, optional
            Whether or not to compute U. If set to be
            True, then U is computed by A * V * s^-1
        rCond : float, optional
            Reciprocal condition number. All singular values
            smaller than rCond * s[0] are treated as zero
            where s[0] is the largest singular value.

        Returns
        -------
        :py:class:`SingularValueDecomposition`

        Examples
        --------
        >>> rows = sc.parallelize([[3, 1, 1], [-1, 3, 1]])
        >>> rm = RowMatrix(rows)

        >>> svd_model = rm.computeSVD(2, True)
        >>> svd_model.U.rows.collect()
        [DenseVector([-0.7071, 0.7071]), DenseVector([-0.7071, -0.7071])]
        >>> svd_model.s
        DenseVector([3.4641, 3.1623])
        >>> svd_model.V
        DenseMatrix(3, 2, [-0.4082, -0.8165, -0.4082, 0.8944, -0.4472, ...0.0], 0)
        """
    def computePrincipalComponents(self, k: int) -> Matrix:
        """
        Computes the k principal components of the given row matrix

        .. versionadded:: 2.2.0

        Notes
        -----
        This cannot be computed on matrices with more than 65535 columns.

        Parameters
        ----------
        k : int
            Number of principal components to keep.

        Returns
        -------
        :py:class:`pyspark.mllib.linalg.DenseMatrix`

        Examples
        --------
        >>> rows = sc.parallelize([[1, 2, 3], [2, 4, 5], [3, 6, 1]])
        >>> rm = RowMatrix(rows)

        >>> # Returns the two principal components of rm
        >>> pca = rm.computePrincipalComponents(2)
        >>> pca
        DenseMatrix(3, 2, [-0.349, -0.6981, 0.6252, -0.2796, -0.5592, -0.7805], 0)

        >>> # Transform into new dimensions with the greatest variance.
        >>> rm.multiply(pca).rows.collect() # doctest: +NORMALIZE_WHITESPACE
        [DenseVector([0.1305, -3.7394]), DenseVector([-0.3642, -6.6983]),         DenseVector([-4.6102, -4.9745])]
        """
    def multiply(self, matrix: Matrix) -> RowMatrix:
        """
        Multiply this matrix by a local dense matrix on the right.

        .. versionadded:: 2.2.0

        Parameters
        ----------
        matrix : :py:class:`pyspark.mllib.linalg.Matrix`
            a local dense matrix whose number of rows must match the number of columns
            of this matrix

        Returns
        -------
        :py:class:`RowMatrix`

        Examples
        --------
        >>> rm = RowMatrix(sc.parallelize([[0, 1], [2, 3]]))
        >>> rm.multiply(DenseMatrix(2, 2, [0, 2, 1, 3])).rows.collect()
        [DenseVector([2.0, 3.0]), DenseVector([6.0, 11.0])]
        """

class SingularValueDecomposition(JavaModelWrapper, Generic[UT, VT]):
    """
    Represents singular value decomposition (SVD) factors.

    .. versionadded:: 2.2.0
    """
    @property
    def U(self) -> UT | None:
        """
        Returns a distributed matrix whose columns are the left
        singular vectors of the SingularValueDecomposition if computeU was set to be True.
        """
    @property
    def s(self) -> Vector:
        """
        Returns a DenseVector with singular values in descending order.
        """
    @property
    def V(self) -> VT:
        """
        Returns a DenseMatrix whose columns are the right singular
        vectors of the SingularValueDecomposition.
        """

class IndexedRow:
    """
    Represents a row of an IndexedRowMatrix.

    Just a wrapper over a (int, vector) tuple.

    Parameters
    ----------
    index : int
        The index for the given row.
    vector : :py:class:`pyspark.mllib.linalg.Vector` or convertible
        The row in the matrix at the given index.
    """
    index: Incomplete
    vector: Incomplete
    def __init__(self, index: int, vector: VectorLike) -> None: ...

class IndexedRowMatrix(DistributedMatrix):
    """
    Represents a row-oriented distributed Matrix with indexed rows.

    Parameters
    ----------
    rows : :py:class:`pyspark.RDD`
        An RDD of IndexedRows or (int, vector) tuples or a DataFrame consisting of a
        int typed column of indices and a vector typed column.
    numRows : int, optional
        Number of rows in the matrix. A non-positive
        value means unknown, at which point the number
        of rows will be determined by the max row
        index plus one.
    numCols : int, optional
        Number of columns in the matrix. A non-positive
        value means unknown, at which point the number
        of columns will be determined by the size of
        the first row.
    """
    def __init__(self, rows: RDD[Tuple[int, 'VectorLike'] | IndexedRow], numRows: int = 0, numCols: int = 0) -> None:
        """
        Note: This docstring is not shown publicly.

        Create a wrapper over a Java IndexedRowMatrix.

        Publicly, we require that `rows` be an RDD or DataFrame.  However, for
        internal usage, `rows` can also be a Java IndexedRowMatrix
        object, in which case we can wrap it directly.  This
        assists in clean matrix conversions.

        Examples
        --------
        >>> rows = sc.parallelize([IndexedRow(0, [1, 2, 3]),
        ...                        IndexedRow(1, [4, 5, 6])])
        >>> mat = IndexedRowMatrix(rows)

        >>> mat_diff = IndexedRowMatrix(rows)
        >>> (mat_diff._java_matrix_wrapper._java_model ==
        ...  mat._java_matrix_wrapper._java_model)
        False

        >>> mat_same = IndexedRowMatrix(mat._java_matrix_wrapper._java_model)
        >>> (mat_same._java_matrix_wrapper._java_model ==
        ...  mat._java_matrix_wrapper._java_model)
        True
        """
    @property
    def rows(self) -> RDD[IndexedRow]:
        """
        Rows of the IndexedRowMatrix stored as an RDD of IndexedRows.

        Examples
        --------
        >>> mat = IndexedRowMatrix(sc.parallelize([IndexedRow(0, [1, 2, 3]),
        ...                                        IndexedRow(1, [4, 5, 6])]))
        >>> rows = mat.rows
        >>> rows.first()
        IndexedRow(0, [1.0,2.0,3.0])
        """
    def numRows(self) -> int:
        """
        Get or compute the number of rows.

        Examples
        --------
        >>> rows = sc.parallelize([IndexedRow(0, [1, 2, 3]),
        ...                        IndexedRow(1, [4, 5, 6]),
        ...                        IndexedRow(2, [7, 8, 9]),
        ...                        IndexedRow(3, [10, 11, 12])])

        >>> mat = IndexedRowMatrix(rows)
        >>> print(mat.numRows())
        4

        >>> mat = IndexedRowMatrix(rows, 7, 6)
        >>> print(mat.numRows())
        7
        """
    def numCols(self) -> int:
        """
        Get or compute the number of cols.

        Examples
        --------
        >>> rows = sc.parallelize([IndexedRow(0, [1, 2, 3]),
        ...                        IndexedRow(1, [4, 5, 6]),
        ...                        IndexedRow(2, [7, 8, 9]),
        ...                        IndexedRow(3, [10, 11, 12])])

        >>> mat = IndexedRowMatrix(rows)
        >>> print(mat.numCols())
        3

        >>> mat = IndexedRowMatrix(rows, 7, 6)
        >>> print(mat.numCols())
        6
        """
    def columnSimilarities(self) -> CoordinateMatrix:
        """
        Compute all cosine similarities between columns.

        Examples
        --------
        >>> rows = sc.parallelize([IndexedRow(0, [1, 2, 3]),
        ...                        IndexedRow(6, [4, 5, 6])])
        >>> mat = IndexedRowMatrix(rows)
        >>> cs = mat.columnSimilarities()
        >>> print(cs.numCols())
        3
        """
    def computeGramianMatrix(self) -> Matrix:
        """
        Computes the Gramian matrix `A^T A`.

        .. versionadded:: 2.0.0

        Notes
        -----
        This cannot be computed on matrices with more than 65535 columns.

        Examples
        --------
        >>> rows = sc.parallelize([IndexedRow(0, [1, 2, 3]),
        ...                        IndexedRow(1, [4, 5, 6])])
        >>> mat = IndexedRowMatrix(rows)

        >>> mat.computeGramianMatrix()
        DenseMatrix(3, 3, [17.0, 22.0, 27.0, 22.0, 29.0, 36.0, 27.0, 36.0, 45.0], 0)
        """
    def toRowMatrix(self) -> RowMatrix:
        """
        Convert this matrix to a RowMatrix.

        Examples
        --------
        >>> rows = sc.parallelize([IndexedRow(0, [1, 2, 3]),
        ...                        IndexedRow(6, [4, 5, 6])])
        >>> mat = IndexedRowMatrix(rows).toRowMatrix()
        >>> mat.rows.collect()
        [DenseVector([1.0, 2.0, 3.0]), DenseVector([4.0, 5.0, 6.0])]
        """
    def toCoordinateMatrix(self) -> CoordinateMatrix:
        """
        Convert this matrix to a CoordinateMatrix.

        Examples
        --------
        >>> rows = sc.parallelize([IndexedRow(0, [1, 0]),
        ...                        IndexedRow(6, [0, 5])])
        >>> mat = IndexedRowMatrix(rows).toCoordinateMatrix()
        >>> mat.entries.take(3)
        [MatrixEntry(0, 0, 1.0), MatrixEntry(0, 1, 0.0), MatrixEntry(6, 0, 0.0)]
        """
    def toBlockMatrix(self, rowsPerBlock: int = 1024, colsPerBlock: int = 1024) -> BlockMatrix:
        """
        Convert this matrix to a BlockMatrix.

        Parameters
        ----------
        rowsPerBlock : int, optional
            Number of rows that make up each block.
            The blocks forming the final rows are not
            required to have the given number of rows.
        colsPerBlock : int, optional
            Number of columns that make up each block.
            The blocks forming the final columns are not
            required to have the given number of columns.

        Examples
        --------
        >>> rows = sc.parallelize([IndexedRow(0, [1, 2, 3]),
        ...                        IndexedRow(6, [4, 5, 6])])
        >>> mat = IndexedRowMatrix(rows).toBlockMatrix()

        >>> # This IndexedRowMatrix will have 7 effective rows, due to
        >>> # the highest row index being 6, and the ensuing
        >>> # BlockMatrix will have 7 rows as well.
        >>> print(mat.numRows())
        7

        >>> print(mat.numCols())
        3
        """
    def computeSVD(self, k: int, computeU: bool = False, rCond: float = 1e-09) -> SingularValueDecomposition['IndexedRowMatrix', Matrix]:
        """
        Computes the singular value decomposition of the IndexedRowMatrix.

        The given row matrix A of dimension (m X n) is decomposed into
        U * s * V'T where

        * U: (m X k) (left singular vectors) is a IndexedRowMatrix
             whose columns are the eigenvectors of (A X A')
        * s: DenseVector consisting of square root of the eigenvalues
             (singular values) in descending order.
        * v: (n X k) (right singular vectors) is a Matrix whose columns
             are the eigenvectors of (A' X A)

        For more specific details on implementation, please refer
        the scala documentation.

        .. versionadded:: 2.2.0

        Parameters
        ----------
        k : int
            Number of leading singular values to keep (`0 < k <= n`).
            It might return less than k if there are numerically zero singular values
            or there are not enough Ritz values converged before the maximum number of
            Arnoldi update iterations is reached (in case that matrix A is ill-conditioned).
        computeU : bool, optional
            Whether or not to compute U. If set to be
            True, then U is computed by A * V * s^-1
        rCond : float, optional
            Reciprocal condition number. All singular values
            smaller than rCond * s[0] are treated as zero
            where s[0] is the largest singular value.

        Returns
        -------
        :py:class:`SingularValueDecomposition`

        Examples
        --------
        >>> rows = [(0, (3, 1, 1)), (1, (-1, 3, 1))]
        >>> irm = IndexedRowMatrix(sc.parallelize(rows))
        >>> svd_model = irm.computeSVD(2, True)
        >>> svd_model.U.rows.collect() # doctest: +NORMALIZE_WHITESPACE
        [IndexedRow(0, [-0.707106781187,0.707106781187]),        IndexedRow(1, [-0.707106781187,-0.707106781187])]
        >>> svd_model.s
        DenseVector([3.4641, 3.1623])
        >>> svd_model.V
        DenseMatrix(3, 2, [-0.4082, -0.8165, -0.4082, 0.8944, -0.4472, ...0.0], 0)
        """
    def multiply(self, matrix: Matrix) -> IndexedRowMatrix:
        """
        Multiply this matrix by a local dense matrix on the right.

        .. versionadded:: 2.2.0

        Parameters
        ----------
        matrix : :py:class:`pyspark.mllib.linalg.Matrix`
            a local dense matrix whose number of rows must match the number of columns
            of this matrix

        Returns
        -------
        :py:class:`IndexedRowMatrix`

        Examples
        --------
        >>> mat = IndexedRowMatrix(sc.parallelize([(0, (0, 1)), (1, (2, 3))]))
        >>> mat.multiply(DenseMatrix(2, 2, [0, 2, 1, 3])).rows.collect()
        [IndexedRow(0, [2.0,3.0]), IndexedRow(1, [6.0,11.0])]
        """

class MatrixEntry:
    """
    Represents an entry of a CoordinateMatrix.

    Just a wrapper over a (int, int, float) tuple.

    Parameters
    ----------
    i : int
        The row index of the matrix.
    j : int
        The column index of the matrix.
    value : float
        The (i, j)th entry of the matrix, as a float.
    """
    i: Incomplete
    j: Incomplete
    value: Incomplete
    def __init__(self, i: int, j: int, value: float) -> None: ...

class CoordinateMatrix(DistributedMatrix):
    """
    Represents a matrix in coordinate format.

    Parameters
    ----------
    entries : :py:class:`pyspark.RDD`
        An RDD of MatrixEntry inputs or
        (int, int, float) tuples.
    numRows : int, optional
        Number of rows in the matrix. A non-positive
        value means unknown, at which point the number
        of rows will be determined by the max row
        index plus one.
    numCols : int, optional
        Number of columns in the matrix. A non-positive
        value means unknown, at which point the number
        of columns will be determined by the max row
        index plus one.
    """
    def __init__(self, entries: RDD[Tuple[int, int, float] | MatrixEntry], numRows: int = 0, numCols: int = 0) -> None:
        """
        Note: This docstring is not shown publicly.

        Create a wrapper over a Java CoordinateMatrix.

        Publicly, we require that `rows` be an RDD.  However, for
        internal usage, `rows` can also be a Java CoordinateMatrix
        object, in which case we can wrap it directly.  This
        assists in clean matrix conversions.

        Examples
        --------
        >>> entries = sc.parallelize([MatrixEntry(0, 0, 1.2),
        ...                           MatrixEntry(6, 4, 2.1)])
        >>> mat = CoordinateMatrix(entries)

        >>> mat_diff = CoordinateMatrix(entries)
        >>> (mat_diff._java_matrix_wrapper._java_model ==
        ...  mat._java_matrix_wrapper._java_model)
        False

        >>> mat_same = CoordinateMatrix(mat._java_matrix_wrapper._java_model)
        >>> (mat_same._java_matrix_wrapper._java_model ==
        ...  mat._java_matrix_wrapper._java_model)
        True
        """
    @property
    def entries(self) -> RDD[MatrixEntry]:
        """
        Entries of the CoordinateMatrix stored as an RDD of
        MatrixEntries.

        Examples
        --------
        >>> mat = CoordinateMatrix(sc.parallelize([MatrixEntry(0, 0, 1.2),
        ...                                        MatrixEntry(6, 4, 2.1)]))
        >>> entries = mat.entries
        >>> entries.first()
        MatrixEntry(0, 0, 1.2)
        """
    def numRows(self) -> int:
        """
        Get or compute the number of rows.

        Examples
        --------
        >>> entries = sc.parallelize([MatrixEntry(0, 0, 1.2),
        ...                           MatrixEntry(1, 0, 2),
        ...                           MatrixEntry(2, 1, 3.7)])

        >>> mat = CoordinateMatrix(entries)
        >>> print(mat.numRows())
        3

        >>> mat = CoordinateMatrix(entries, 7, 6)
        >>> print(mat.numRows())
        7
        """
    def numCols(self) -> int:
        """
        Get or compute the number of cols.

        Examples
        --------
        >>> entries = sc.parallelize([MatrixEntry(0, 0, 1.2),
        ...                           MatrixEntry(1, 0, 2),
        ...                           MatrixEntry(2, 1, 3.7)])

        >>> mat = CoordinateMatrix(entries)
        >>> print(mat.numCols())
        2

        >>> mat = CoordinateMatrix(entries, 7, 6)
        >>> print(mat.numCols())
        6
        """
    def transpose(self) -> CoordinateMatrix:
        """
        Transpose this CoordinateMatrix.

        .. versionadded:: 2.0.0

        Examples
        --------
        >>> entries = sc.parallelize([MatrixEntry(0, 0, 1.2),
        ...                           MatrixEntry(1, 0, 2),
        ...                           MatrixEntry(2, 1, 3.7)])
        >>> mat = CoordinateMatrix(entries)
        >>> mat_transposed = mat.transpose()

        >>> print(mat_transposed.numRows())
        2

        >>> print(mat_transposed.numCols())
        3
        """
    def toRowMatrix(self) -> RowMatrix:
        """
        Convert this matrix to a RowMatrix.

        Examples
        --------
        >>> entries = sc.parallelize([MatrixEntry(0, 0, 1.2),
        ...                           MatrixEntry(6, 4, 2.1)])
        >>> mat = CoordinateMatrix(entries).toRowMatrix()

        >>> # This CoordinateMatrix will have 7 effective rows, due to
        >>> # the highest row index being 6, but the ensuing RowMatrix
        >>> # will only have 2 rows since there are only entries on 2
        >>> # unique rows.
        >>> print(mat.numRows())
        2

        >>> # This CoordinateMatrix will have 5 columns, due to the
        >>> # highest column index being 4, and the ensuing RowMatrix
        >>> # will have 5 columns as well.
        >>> print(mat.numCols())
        5
        """
    def toIndexedRowMatrix(self) -> IndexedRowMatrix:
        """
        Convert this matrix to an IndexedRowMatrix.

        Examples
        --------
        >>> entries = sc.parallelize([MatrixEntry(0, 0, 1.2),
        ...                           MatrixEntry(6, 4, 2.1)])
        >>> mat = CoordinateMatrix(entries).toIndexedRowMatrix()

        >>> # This CoordinateMatrix will have 7 effective rows, due to
        >>> # the highest row index being 6, and the ensuing
        >>> # IndexedRowMatrix will have 7 rows as well.
        >>> print(mat.numRows())
        7

        >>> # This CoordinateMatrix will have 5 columns, due to the
        >>> # highest column index being 4, and the ensuing
        >>> # IndexedRowMatrix will have 5 columns as well.
        >>> print(mat.numCols())
        5
        """
    def toBlockMatrix(self, rowsPerBlock: int = 1024, colsPerBlock: int = 1024) -> BlockMatrix:
        """
        Convert this matrix to a BlockMatrix.

        Parameters
        ----------
        rowsPerBlock : int, optional
            Number of rows that make up each block.
            The blocks forming the final rows are not
            required to have the given number of rows.
        colsPerBlock : int, optional
            Number of columns that make up each block.
            The blocks forming the final columns are not
            required to have the given number of columns.

        Examples
        --------
        >>> entries = sc.parallelize([MatrixEntry(0, 0, 1.2),
        ...                           MatrixEntry(6, 4, 2.1)])
        >>> mat = CoordinateMatrix(entries).toBlockMatrix()

        >>> # This CoordinateMatrix will have 7 effective rows, due to
        >>> # the highest row index being 6, and the ensuing
        >>> # BlockMatrix will have 7 rows as well.
        >>> print(mat.numRows())
        7

        >>> # This CoordinateMatrix will have 5 columns, due to the
        >>> # highest column index being 4, and the ensuing
        >>> # BlockMatrix will have 5 columns as well.
        >>> print(mat.numCols())
        5
        """

class BlockMatrix(DistributedMatrix):
    """
    Represents a distributed matrix in blocks of local matrices.

    Parameters
    ----------
    blocks : :py:class:`pyspark.RDD`
        An RDD of sub-matrix blocks
        ((blockRowIndex, blockColIndex), sub-matrix) that
        form this distributed matrix. If multiple blocks
        with the same index exist, the results for
        operations like add and multiply will be
        unpredictable.
    rowsPerBlock : int
        Number of rows that make up each block.
        The blocks forming the final rows are not
        required to have the given number of rows.
    colsPerBlock : int
        Number of columns that make up each block.
        The blocks forming the final columns are not
        required to have the given number of columns.
    numRows : int, optional
        Number of rows of this matrix. If the supplied
        value is less than or equal to zero, the number
        of rows will be calculated when `numRows` is
        invoked.
    numCols : int, optional
        Number of columns of this matrix. If the supplied
        value is less than or equal to zero, the number
        of columns will be calculated when `numCols` is
        invoked.
    """
    def __init__(self, blocks: RDD[Tuple[Tuple[int, int], Matrix]], rowsPerBlock: int, colsPerBlock: int, numRows: int = 0, numCols: int = 0) -> None:
        """
        Note: This docstring is not shown publicly.

        Create a wrapper over a Java BlockMatrix.

        Publicly, we require that `blocks` be an RDD.  However, for
        internal usage, `blocks` can also be a Java BlockMatrix
        object, in which case we can wrap it directly.  This
        assists in clean matrix conversions.

        Examples
        --------
        >>> blocks = sc.parallelize([((0, 0), Matrices.dense(3, 2, [1, 2, 3, 4, 5, 6])),
        ...                          ((1, 0), Matrices.dense(3, 2, [7, 8, 9, 10, 11, 12]))])
        >>> mat = BlockMatrix(blocks, 3, 2)

        >>> mat_diff = BlockMatrix(blocks, 3, 2)
        >>> (mat_diff._java_matrix_wrapper._java_model ==
        ...  mat._java_matrix_wrapper._java_model)
        False

        >>> mat_same = BlockMatrix(mat._java_matrix_wrapper._java_model, 3, 2)
        >>> (mat_same._java_matrix_wrapper._java_model ==
        ...  mat._java_matrix_wrapper._java_model)
        True
        """
    @property
    def blocks(self) -> RDD[Tuple[Tuple[int, int], Matrix]]:
        """
        The RDD of sub-matrix blocks
        ((blockRowIndex, blockColIndex), sub-matrix) that form this
        distributed matrix.

        Examples
        --------
        >>> mat = BlockMatrix(
        ...     sc.parallelize([((0, 0), Matrices.dense(3, 2, [1, 2, 3, 4, 5, 6])),
        ...                     ((1, 0), Matrices.dense(3, 2, [7, 8, 9, 10, 11, 12]))]), 3, 2)
        >>> blocks = mat.blocks
        >>> blocks.first()
        ((0, 0), DenseMatrix(3, 2, [1.0, 2.0, 3.0, 4.0, 5.0, 6.0], 0))

        """
    @property
    def rowsPerBlock(self) -> int:
        """
        Number of rows that make up each block.

        Examples
        --------
        >>> blocks = sc.parallelize([((0, 0), Matrices.dense(3, 2, [1, 2, 3, 4, 5, 6])),
        ...                          ((1, 0), Matrices.dense(3, 2, [7, 8, 9, 10, 11, 12]))])
        >>> mat = BlockMatrix(blocks, 3, 2)
        >>> mat.rowsPerBlock
        3
        """
    @property
    def colsPerBlock(self) -> int:
        """
        Number of columns that make up each block.

        Examples
        --------
        >>> blocks = sc.parallelize([((0, 0), Matrices.dense(3, 2, [1, 2, 3, 4, 5, 6])),
        ...                          ((1, 0), Matrices.dense(3, 2, [7, 8, 9, 10, 11, 12]))])
        >>> mat = BlockMatrix(blocks, 3, 2)
        >>> mat.colsPerBlock
        2
        """
    @property
    def numRowBlocks(self) -> int:
        """
        Number of rows of blocks in the BlockMatrix.

        Examples
        --------
        >>> blocks = sc.parallelize([((0, 0), Matrices.dense(3, 2, [1, 2, 3, 4, 5, 6])),
        ...                          ((1, 0), Matrices.dense(3, 2, [7, 8, 9, 10, 11, 12]))])
        >>> mat = BlockMatrix(blocks, 3, 2)
        >>> mat.numRowBlocks
        2
        """
    @property
    def numColBlocks(self) -> int:
        """
        Number of columns of blocks in the BlockMatrix.

        Examples
        --------
        >>> blocks = sc.parallelize([((0, 0), Matrices.dense(3, 2, [1, 2, 3, 4, 5, 6])),
        ...                          ((1, 0), Matrices.dense(3, 2, [7, 8, 9, 10, 11, 12]))])
        >>> mat = BlockMatrix(blocks, 3, 2)
        >>> mat.numColBlocks
        1
        """
    def numRows(self) -> int:
        """
        Get or compute the number of rows.

        Examples
        --------
        >>> blocks = sc.parallelize([((0, 0), Matrices.dense(3, 2, [1, 2, 3, 4, 5, 6])),
        ...                          ((1, 0), Matrices.dense(3, 2, [7, 8, 9, 10, 11, 12]))])

        >>> mat = BlockMatrix(blocks, 3, 2)
        >>> print(mat.numRows())
        6

        >>> mat = BlockMatrix(blocks, 3, 2, 7, 6)
        >>> print(mat.numRows())
        7
        """
    def numCols(self) -> int:
        """
        Get or compute the number of cols.

        Examples
        --------
        >>> blocks = sc.parallelize([((0, 0), Matrices.dense(3, 2, [1, 2, 3, 4, 5, 6])),
        ...                          ((1, 0), Matrices.dense(3, 2, [7, 8, 9, 10, 11, 12]))])

        >>> mat = BlockMatrix(blocks, 3, 2)
        >>> print(mat.numCols())
        2

        >>> mat = BlockMatrix(blocks, 3, 2, 7, 6)
        >>> print(mat.numCols())
        6
        """
    def cache(self) -> BlockMatrix:
        """
        Caches the underlying RDD.
        """
    def persist(self, storageLevel: StorageLevel) -> BlockMatrix:
        """
        Persists the underlying RDD with the specified storage level.
        """
    def validate(self) -> None:
        """
        Validates the block matrix info against the matrix data (`blocks`)
        and throws an exception if any error is found.
        """
    def add(self, other: BlockMatrix) -> BlockMatrix:
        """
        Adds two block matrices together. The matrices must have the
        same size and matching `rowsPerBlock` and `colsPerBlock` values.
        If one of the sub matrix blocks that are being added is a
        SparseMatrix, the resulting sub matrix block will also be a
        SparseMatrix, even if it is being added to a DenseMatrix. If
        two dense sub matrix blocks are added, the output block will
        also be a DenseMatrix.

        Examples
        --------
        >>> dm1 = Matrices.dense(3, 2, [1, 2, 3, 4, 5, 6])
        >>> dm2 = Matrices.dense(3, 2, [7, 8, 9, 10, 11, 12])
        >>> sm = Matrices.sparse(3, 2, [0, 1, 3], [0, 1, 2], [7, 11, 12])
        >>> blocks1 = sc.parallelize([((0, 0), dm1), ((1, 0), dm2)])
        >>> blocks2 = sc.parallelize([((0, 0), dm1), ((1, 0), dm2)])
        >>> blocks3 = sc.parallelize([((0, 0), sm), ((1, 0), dm2)])
        >>> mat1 = BlockMatrix(blocks1, 3, 2)
        >>> mat2 = BlockMatrix(blocks2, 3, 2)
        >>> mat3 = BlockMatrix(blocks3, 3, 2)

        >>> mat1.add(mat2).toLocalMatrix()
        DenseMatrix(6, 2, [2.0, 4.0, 6.0, 14.0, 16.0, 18.0, 8.0, 10.0, 12.0, 20.0, 22.0, 24.0], 0)

        >>> mat1.add(mat3).toLocalMatrix()
        DenseMatrix(6, 2, [8.0, 2.0, 3.0, 14.0, 16.0, 18.0, 4.0, 16.0, 18.0, 20.0, 22.0, 24.0], 0)
        """
    def subtract(self, other: BlockMatrix) -> BlockMatrix:
        """
        Subtracts the given block matrix `other` from this block matrix:
        `this - other`. The matrices must have the same size and
        matching `rowsPerBlock` and `colsPerBlock` values.  If one of
        the sub matrix blocks that are being subtracted is a
        SparseMatrix, the resulting sub matrix block will also be a
        SparseMatrix, even if it is being subtracted from a DenseMatrix.
        If two dense sub matrix blocks are subtracted, the output block
        will also be a DenseMatrix.

        .. versionadded:: 2.0.0

        Examples
        --------
        >>> dm1 = Matrices.dense(3, 2, [3, 1, 5, 4, 6, 2])
        >>> dm2 = Matrices.dense(3, 2, [7, 8, 9, 10, 11, 12])
        >>> sm = Matrices.sparse(3, 2, [0, 1, 3], [0, 1, 2], [1, 2, 3])
        >>> blocks1 = sc.parallelize([((0, 0), dm1), ((1, 0), dm2)])
        >>> blocks2 = sc.parallelize([((0, 0), dm2), ((1, 0), dm1)])
        >>> blocks3 = sc.parallelize([((0, 0), sm), ((1, 0), dm2)])
        >>> mat1 = BlockMatrix(blocks1, 3, 2)
        >>> mat2 = BlockMatrix(blocks2, 3, 2)
        >>> mat3 = BlockMatrix(blocks3, 3, 2)

        >>> mat1.subtract(mat2).toLocalMatrix()
        DenseMatrix(6, 2, [-4.0, -7.0, -4.0, 4.0, 7.0, 4.0, -6.0, -5.0, -10.0, 6.0, 5.0, 10.0], 0)

        >>> mat2.subtract(mat3).toLocalMatrix()
        DenseMatrix(6, 2, [6.0, 8.0, 9.0, -4.0, -7.0, -4.0, 10.0, 9.0, 9.0, -6.0, -5.0, -10.0], 0)
        """
    def multiply(self, other: BlockMatrix) -> BlockMatrix:
        """
        Left multiplies this BlockMatrix by `other`, another
        BlockMatrix. The `colsPerBlock` of this matrix must equal the
        `rowsPerBlock` of `other`. If `other` contains any SparseMatrix
        blocks, they will have to be converted to DenseMatrix blocks.
        The output BlockMatrix will only consist of DenseMatrix blocks.
        This may cause some performance issues until support for
        multiplying two sparse matrices is added.

        Examples
        --------
        >>> dm1 = Matrices.dense(2, 3, [1, 2, 3, 4, 5, 6])
        >>> dm2 = Matrices.dense(2, 3, [7, 8, 9, 10, 11, 12])
        >>> dm3 = Matrices.dense(3, 2, [1, 2, 3, 4, 5, 6])
        >>> dm4 = Matrices.dense(3, 2, [7, 8, 9, 10, 11, 12])
        >>> sm = Matrices.sparse(3, 2, [0, 1, 3], [0, 1, 2], [7, 11, 12])
        >>> blocks1 = sc.parallelize([((0, 0), dm1), ((0, 1), dm2)])
        >>> blocks2 = sc.parallelize([((0, 0), dm3), ((1, 0), dm4)])
        >>> blocks3 = sc.parallelize([((0, 0), sm), ((1, 0), dm4)])
        >>> mat1 = BlockMatrix(blocks1, 2, 3)
        >>> mat2 = BlockMatrix(blocks2, 3, 2)
        >>> mat3 = BlockMatrix(blocks3, 3, 2)

        >>> mat1.multiply(mat2).toLocalMatrix()
        DenseMatrix(2, 2, [242.0, 272.0, 350.0, 398.0], 0)

        >>> mat1.multiply(mat3).toLocalMatrix()
        DenseMatrix(2, 2, [227.0, 258.0, 394.0, 450.0], 0)
        """
    def transpose(self) -> BlockMatrix:
        """
        Transpose this BlockMatrix. Returns a new BlockMatrix
        instance sharing the same underlying data. Is a lazy operation.

        .. versionadded:: 2.0.0

        Examples
        --------
        >>> blocks = sc.parallelize([((0, 0), Matrices.dense(3, 2, [1, 2, 3, 4, 5, 6])),
        ...                          ((1, 0), Matrices.dense(3, 2, [7, 8, 9, 10, 11, 12]))])
        >>> mat = BlockMatrix(blocks, 3, 2)

        >>> mat_transposed = mat.transpose()
        >>> mat_transposed.toLocalMatrix()
        DenseMatrix(2, 6, [1.0, 4.0, 2.0, 5.0, 3.0, 6.0, 7.0, 10.0, 8.0, 11.0, 9.0, 12.0], 0)
        """
    def toLocalMatrix(self) -> Matrix:
        """
        Collect the distributed matrix on the driver as a DenseMatrix.

        Examples
        --------
        >>> blocks = sc.parallelize([((0, 0), Matrices.dense(3, 2, [1, 2, 3, 4, 5, 6])),
        ...                          ((1, 0), Matrices.dense(3, 2, [7, 8, 9, 10, 11, 12]))])
        >>> mat = BlockMatrix(blocks, 3, 2).toLocalMatrix()

        >>> # This BlockMatrix will have 6 effective rows, due to
        >>> # having two sub-matrix blocks stacked, each with 3 rows.
        >>> # The ensuing DenseMatrix will also have 6 rows.
        >>> print(mat.numRows)
        6

        >>> # This BlockMatrix will have 2 effective columns, due to
        >>> # having two sub-matrix blocks stacked, each with 2
        >>> # columns. The ensuing DenseMatrix will also have 2 columns.
        >>> print(mat.numCols)
        2
        """
    def toIndexedRowMatrix(self) -> IndexedRowMatrix:
        """
        Convert this matrix to an IndexedRowMatrix.

        Examples
        --------
        >>> blocks = sc.parallelize([((0, 0), Matrices.dense(3, 2, [1, 2, 3, 4, 5, 6])),
        ...                          ((1, 0), Matrices.dense(3, 2, [7, 8, 9, 10, 11, 12]))])
        >>> mat = BlockMatrix(blocks, 3, 2).toIndexedRowMatrix()

        >>> # This BlockMatrix will have 6 effective rows, due to
        >>> # having two sub-matrix blocks stacked, each with 3 rows.
        >>> # The ensuing IndexedRowMatrix will also have 6 rows.
        >>> print(mat.numRows())
        6

        >>> # This BlockMatrix will have 2 effective columns, due to
        >>> # having two sub-matrix blocks stacked, each with 2 columns.
        >>> # The ensuing IndexedRowMatrix will also have 2 columns.
        >>> print(mat.numCols())
        2
        """
    def toCoordinateMatrix(self) -> CoordinateMatrix:
        """
        Convert this matrix to a CoordinateMatrix.

        Examples
        --------
        >>> blocks = sc.parallelize([((0, 0), Matrices.dense(1, 2, [1, 2])),
        ...                          ((1, 0), Matrices.dense(1, 2, [7, 8]))])
        >>> mat = BlockMatrix(blocks, 1, 2).toCoordinateMatrix()
        >>> mat.entries.take(3)
        [MatrixEntry(0, 0, 1.0), MatrixEntry(0, 1, 2.0), MatrixEntry(1, 0, 7.0)]
        """
