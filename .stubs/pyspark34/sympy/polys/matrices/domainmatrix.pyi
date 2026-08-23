from ..constructor import construct_domain as construct_domain
from ..domains import Domain as Domain
from .ddm import DDM as DDM
from .domainscalar import DomainScalar as DomainScalar
from .exceptions import DMBadInputError as DMBadInputError, DMDomainError as DMDomainError, DMFormatError as DMFormatError, DMNonSquareMatrixError as DMNonSquareMatrixError, DMNotAField as DMNotAField, DMShapeError as DMShapeError
from .sdm import SDM as SDM
from _typeshed import Incomplete
from sympy.polys.domains import EXRAW as EXRAW, QQ as QQ, ZZ as ZZ
from typing import Tuple as tTuple

def DM(rows, domain):
    """Convenient alias for DomainMatrix.from_list

    Examples
    =======

    >>> from sympy import ZZ
    >>> from sympy.polys.matrices import DM
    >>> DM([[1, 2], [3, 4]], ZZ)
    DomainMatrix([[1, 2], [3, 4]], (2, 2), ZZ)

    See also
    =======

    DomainMatrix.from_list
    """

class DomainMatrix:
    '''
    Associate Matrix with :py:class:`~.Domain`

    Explanation
    ===========

    DomainMatrix uses :py:class:`~.Domain` for its internal representation
    which makes it faster than the SymPy Matrix class (currently) for many
    common operations, but this advantage makes it not entirely compatible
    with Matrix. DomainMatrix are analogous to numpy arrays with "dtype".
    In the DomainMatrix, each element has a domain such as :ref:`ZZ`
    or  :ref:`QQ(a)`.


    Examples
    ========

    Creating a DomainMatrix from the existing Matrix class:

    >>> from sympy import Matrix
    >>> from sympy.polys.matrices import DomainMatrix
    >>> Matrix1 = Matrix([
    ...    [1, 2],
    ...    [3, 4]])
    >>> A = DomainMatrix.from_Matrix(Matrix1)
    >>> A
    DomainMatrix({0: {0: 1, 1: 2}, 1: {0: 3, 1: 4}}, (2, 2), ZZ)

    Directly forming a DomainMatrix:

    >>> from sympy import ZZ
    >>> from sympy.polys.matrices import DomainMatrix
    >>> A = DomainMatrix([
    ...    [ZZ(1), ZZ(2)],
    ...    [ZZ(3), ZZ(4)]], (2, 2), ZZ)
    >>> A
    DomainMatrix([[1, 2], [3, 4]], (2, 2), ZZ)

    See Also
    ========

    DDM
    SDM
    Domain
    Poly

    '''
    rep: SDM | DDM
    shape: tTuple[int, int]
    domain: Domain
    def __new__(cls, rows, shape, domain, *, fmt: Incomplete | None = None):
        """
        Creates a :py:class:`~.DomainMatrix`.

        Parameters
        ==========

        rows : Represents elements of DomainMatrix as list of lists
        shape : Represents dimension of DomainMatrix
        domain : Represents :py:class:`~.Domain` of DomainMatrix

        Raises
        ======

        TypeError
            If any of rows, shape and domain are not provided

        """
    def __getnewargs__(self): ...
    def __getitem__(self, key): ...
    def getitem_sympy(self, i, j): ...
    def extract(self, rowslist, colslist): ...
    def __setitem__(self, key, value) -> None: ...
    @classmethod
    def from_rep(cls, rep):
        """Create a new DomainMatrix efficiently from DDM/SDM.

        Examples
        ========

        Create a :py:class:`~.DomainMatrix` with an dense internal
        representation as :py:class:`~.DDM`:

        >>> from sympy.polys.domains import ZZ
        >>> from sympy.polys.matrices import DomainMatrix
        >>> from sympy.polys.matrices.ddm import DDM
        >>> drep = DDM([[ZZ(1), ZZ(2)], [ZZ(3), ZZ(4)]], (2, 2), ZZ)
        >>> dM = DomainMatrix.from_rep(drep)
        >>> dM
        DomainMatrix([[1, 2], [3, 4]], (2, 2), ZZ)

        Create a :py:class:`~.DomainMatrix` with a sparse internal
        representation as :py:class:`~.SDM`:

        >>> from sympy.polys.matrices import DomainMatrix
        >>> from sympy.polys.matrices.sdm import SDM
        >>> from sympy import ZZ
        >>> drep = SDM({0:{1:ZZ(1)},1:{0:ZZ(2)}}, (2, 2), ZZ)
        >>> dM = DomainMatrix.from_rep(drep)
        >>> dM
        DomainMatrix({0: {1: 1}, 1: {0: 2}}, (2, 2), ZZ)

        Parameters
        ==========

        rep: SDM or DDM
            The internal sparse or dense representation of the matrix.

        Returns
        =======

        DomainMatrix
            A :py:class:`~.DomainMatrix` wrapping *rep*.

        Notes
        =====

        This takes ownership of rep as its internal representation. If rep is
        being mutated elsewhere then a copy should be provided to
        ``from_rep``. Only minimal verification or checking is done on *rep*
        as this is supposed to be an efficient internal routine.

        """
    @classmethod
    def from_list(cls, rows, domain):
        """
        Convert a list of lists into a DomainMatrix

        Parameters
        ==========

        rows: list of lists
            Each element of the inner lists should be either the single arg,
            or tuple of args, that would be passed to the domain constructor
            in order to form an element of the domain. See examples.

        Returns
        =======

        DomainMatrix containing elements defined in rows

        Examples
        ========

        >>> from sympy.polys.matrices import DomainMatrix
        >>> from sympy import FF, QQ, ZZ
        >>> A = DomainMatrix.from_list([[1, 0, 1], [0, 0, 1]], ZZ)
        >>> A
        DomainMatrix([[1, 0, 1], [0, 0, 1]], (2, 3), ZZ)
        >>> B = DomainMatrix.from_list([[1, 0, 1], [0, 0, 1]], FF(7))
        >>> B
        DomainMatrix([[1 mod 7, 0 mod 7, 1 mod 7], [0 mod 7, 0 mod 7, 1 mod 7]], (2, 3), GF(7))
        >>> C = DomainMatrix.from_list([[(1, 2), (3, 1)], [(1, 4), (5, 1)]], QQ)
        >>> C
        DomainMatrix([[1/2, 3], [1/4, 5]], (2, 2), QQ)

        See Also
        ========

        from_list_sympy

        """
    @classmethod
    def from_list_sympy(cls, nrows, ncols, rows, **kwargs):
        """
        Convert a list of lists of Expr into a DomainMatrix using construct_domain

        Parameters
        ==========

        nrows: number of rows
        ncols: number of columns
        rows: list of lists

        Returns
        =======

        DomainMatrix containing elements of rows

        Examples
        ========

        >>> from sympy.polys.matrices import DomainMatrix
        >>> from sympy.abc import x, y, z
        >>> A = DomainMatrix.from_list_sympy(1, 3, [[x, y, z]])
        >>> A
        DomainMatrix([[x, y, z]], (1, 3), ZZ[x,y,z])

        See Also
        ========

        sympy.polys.constructor.construct_domain, from_dict_sympy

        """
    @classmethod
    def from_dict_sympy(cls, nrows, ncols, elemsdict, **kwargs):
        """

        Parameters
        ==========

        nrows: number of rows
        ncols: number of cols
        elemsdict: dict of dicts containing non-zero elements of the DomainMatrix

        Returns
        =======

        DomainMatrix containing elements of elemsdict

        Examples
        ========

        >>> from sympy.polys.matrices import DomainMatrix
        >>> from sympy.abc import x,y,z
        >>> elemsdict = {0: {0:x}, 1:{1: y}, 2: {2: z}}
        >>> A = DomainMatrix.from_dict_sympy(3, 3, elemsdict)
        >>> A
        DomainMatrix({0: {0: x}, 1: {1: y}, 2: {2: z}}, (3, 3), ZZ[x,y,z])

        See Also
        ========

        from_list_sympy

        """
    @classmethod
    def from_Matrix(cls, M, fmt: str = 'sparse', **kwargs):
        """
        Convert Matrix to DomainMatrix

        Parameters
        ==========

        M: Matrix

        Returns
        =======

        Returns DomainMatrix with identical elements as M

        Examples
        ========

        >>> from sympy import Matrix
        >>> from sympy.polys.matrices import DomainMatrix
        >>> M = Matrix([
        ...    [1.0, 3.4],
        ...    [2.4, 1]])
        >>> A = DomainMatrix.from_Matrix(M)
        >>> A
        DomainMatrix({0: {0: 1.0, 1: 3.4}, 1: {0: 2.4, 1: 1.0}}, (2, 2), RR)

        We can keep internal representation as ddm using fmt='dense'
        >>> from sympy import Matrix, QQ
        >>> from sympy.polys.matrices import DomainMatrix
        >>> A = DomainMatrix.from_Matrix(Matrix([[QQ(1, 2), QQ(3, 4)], [QQ(0, 1), QQ(0, 1)]]), fmt='dense')
        >>> A.rep
        [[1/2, 3/4], [0, 0]]

        See Also
        ========

        Matrix

        """
    @classmethod
    def get_domain(cls, items_sympy, **kwargs): ...
    def copy(self): ...
    def convert_to(self, K):
        """
        Change the domain of DomainMatrix to desired domain or field

        Parameters
        ==========

        K : Represents the desired domain or field.
            Alternatively, ``None`` may be passed, in which case this method
            just returns a copy of this DomainMatrix.

        Returns
        =======

        DomainMatrix
            DomainMatrix with the desired domain or field

        Examples
        ========

        >>> from sympy import ZZ, ZZ_I
        >>> from sympy.polys.matrices import DomainMatrix
        >>> A = DomainMatrix([
        ...    [ZZ(1), ZZ(2)],
        ...    [ZZ(3), ZZ(4)]], (2, 2), ZZ)

        >>> A.convert_to(ZZ_I)
        DomainMatrix([[1, 2], [3, 4]], (2, 2), ZZ_I)

        """
    def to_sympy(self): ...
    def to_field(self):
        """
        Returns a DomainMatrix with the appropriate field

        Returns
        =======

        DomainMatrix
            DomainMatrix with the appropriate field

        Examples
        ========

        >>> from sympy import ZZ
        >>> from sympy.polys.matrices import DomainMatrix
        >>> A = DomainMatrix([
        ...    [ZZ(1), ZZ(2)],
        ...    [ZZ(3), ZZ(4)]], (2, 2), ZZ)

        >>> A.to_field()
        DomainMatrix([[1, 2], [3, 4]], (2, 2), QQ)

        """
    def to_sparse(self):
        """
        Return a sparse DomainMatrix representation of *self*.

        Examples
        ========

        >>> from sympy.polys.matrices import DomainMatrix
        >>> from sympy import QQ
        >>> A = DomainMatrix([[1, 0],[0, 2]], (2, 2), QQ)
        >>> A.rep
        [[1, 0], [0, 2]]
        >>> B = A.to_sparse()
        >>> B.rep
        {0: {0: 1}, 1: {1: 2}}
        """
    def to_dense(self):
        """
        Return a dense DomainMatrix representation of *self*.

        Examples
        ========

        >>> from sympy.polys.matrices import DomainMatrix
        >>> from sympy import QQ
        >>> A = DomainMatrix({0: {0: 1}, 1: {1: 2}}, (2, 2), QQ)
        >>> A.rep
        {0: {0: 1}, 1: {1: 2}}
        >>> B = A.to_dense()
        >>> B.rep
        [[1, 0], [0, 2]]

        """
    def unify(self, *others, fmt: Incomplete | None = None):
        """
        Unifies the domains and the format of self and other
        matrices.

        Parameters
        ==========

        others : DomainMatrix

        fmt: string 'dense', 'sparse' or `None` (default)
            The preferred format to convert to if self and other are not
            already in the same format. If `None` or not specified then no
            conversion if performed.

        Returns
        =======

        Tuple[DomainMatrix]
            Matrices with unified domain and format

        Examples
        ========

        Unify the domain of DomainMatrix that have different domains:

        >>> from sympy import ZZ, QQ
        >>> from sympy.polys.matrices import DomainMatrix
        >>> A = DomainMatrix([[ZZ(1), ZZ(2)]], (1, 2), ZZ)
        >>> B = DomainMatrix([[QQ(1, 2), QQ(2)]], (1, 2), QQ)
        >>> Aq, Bq = A.unify(B)
        >>> Aq
        DomainMatrix([[1, 2]], (1, 2), QQ)
        >>> Bq
        DomainMatrix([[1/2, 2]], (1, 2), QQ)

        Unify the format (dense or sparse):

        >>> A = DomainMatrix([[ZZ(1), ZZ(2)]], (1, 2), ZZ)
        >>> B = DomainMatrix({0:{0: ZZ(1)}}, (2, 2), ZZ)
        >>> B.rep
        {0: {0: 1}}

        >>> A2, B2 = A.unify(B, fmt='dense')
        >>> B2.rep
        [[1, 0], [0, 0]]

        See Also
        ========

        convert_to, to_dense, to_sparse

        """
    def to_Matrix(self):
        """
        Convert DomainMatrix to Matrix

        Returns
        =======

        Matrix
            MutableDenseMatrix for the DomainMatrix

        Examples
        ========

        >>> from sympy import ZZ
        >>> from sympy.polys.matrices import DomainMatrix
        >>> A = DomainMatrix([
        ...    [ZZ(1), ZZ(2)],
        ...    [ZZ(3), ZZ(4)]], (2, 2), ZZ)

        >>> A.to_Matrix()
        Matrix([
            [1, 2],
            [3, 4]])

        See Also
        ========

        from_Matrix

        """
    def to_list(self): ...
    def to_list_flat(self): ...
    def to_dok(self): ...
    def transpose(self):
        """Matrix transpose of ``self``"""
    def flat(self): ...
    @property
    def is_zero_matrix(self): ...
    @property
    def is_upper(self):
        """
        Says whether this matrix is upper-triangular. True can be returned
        even if the matrix is not square.
        """
    @property
    def is_lower(self):
        """
        Says whether this matrix is lower-triangular. True can be returned
        even if the matrix is not square.
        """
    @property
    def is_square(self): ...
    def rank(self): ...
    def hstack(A, *B):
        """Horizontally stack the given matrices.

        Parameters
        ==========

        B: DomainMatrix
            Matrices to stack horizontally.

        Returns
        =======

        DomainMatrix
            DomainMatrix by stacking horizontally.

        Examples
        ========

        >>> from sympy import ZZ
        >>> from sympy.polys.matrices import DomainMatrix

        >>> A = DomainMatrix([[ZZ(1), ZZ(2)], [ZZ(3), ZZ(4)]], (2, 2), ZZ)
        >>> B = DomainMatrix([[ZZ(5), ZZ(6)], [ZZ(7), ZZ(8)]], (2, 2), ZZ)
        >>> A.hstack(B)
        DomainMatrix([[1, 2, 5, 6], [3, 4, 7, 8]], (2, 4), ZZ)

        >>> C = DomainMatrix([[ZZ(9), ZZ(10)], [ZZ(11), ZZ(12)]], (2, 2), ZZ)
        >>> A.hstack(B, C)
        DomainMatrix([[1, 2, 5, 6, 9, 10], [3, 4, 7, 8, 11, 12]], (2, 6), ZZ)

        See Also
        ========

        unify
        """
    def vstack(A, *B):
        """Vertically stack the given matrices.

        Parameters
        ==========

        B: DomainMatrix
            Matrices to stack vertically.

        Returns
        =======

        DomainMatrix
            DomainMatrix by stacking vertically.

        Examples
        ========

        >>> from sympy import ZZ
        >>> from sympy.polys.matrices import DomainMatrix

        >>> A = DomainMatrix([[ZZ(1), ZZ(2)], [ZZ(3), ZZ(4)]], (2, 2), ZZ)
        >>> B = DomainMatrix([[ZZ(5), ZZ(6)], [ZZ(7), ZZ(8)]], (2, 2), ZZ)
        >>> A.vstack(B)
        DomainMatrix([[1, 2], [3, 4], [5, 6], [7, 8]], (4, 2), ZZ)

        >>> C = DomainMatrix([[ZZ(9), ZZ(10)], [ZZ(11), ZZ(12)]], (2, 2), ZZ)
        >>> A.vstack(B, C)
        DomainMatrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]], (6, 2), ZZ)

        See Also
        ========

        unify
        """
    def applyfunc(self, func, domain: Incomplete | None = None): ...
    def __add__(A, B): ...
    def __sub__(A, B): ...
    def __neg__(A): ...
    def __mul__(A, B):
        """A * B"""
    def __rmul__(A, B): ...
    def __pow__(A, n):
        """A ** n"""
    def add(A, B):
        """
        Adds two DomainMatrix matrices of the same Domain

        Parameters
        ==========

        A, B: DomainMatrix
            matrices to add

        Returns
        =======

        DomainMatrix
            DomainMatrix after Addition

        Raises
        ======

        DMShapeError
            If the dimensions of the two DomainMatrix are not equal

        ValueError
            If the domain of the two DomainMatrix are not same

        Examples
        ========

        >>> from sympy import ZZ
        >>> from sympy.polys.matrices import DomainMatrix
        >>> A = DomainMatrix([
        ...    [ZZ(1), ZZ(2)],
        ...    [ZZ(3), ZZ(4)]], (2, 2), ZZ)
        >>> B = DomainMatrix([
        ...    [ZZ(4), ZZ(3)],
        ...    [ZZ(2), ZZ(1)]], (2, 2), ZZ)

        >>> A.add(B)
        DomainMatrix([[5, 5], [5, 5]], (2, 2), ZZ)

        See Also
        ========

        sub, matmul

        """
    def sub(A, B):
        """
        Subtracts two DomainMatrix matrices of the same Domain

        Parameters
        ==========

        A, B: DomainMatrix
            matrices to subtract

        Returns
        =======

        DomainMatrix
            DomainMatrix after Subtraction

        Raises
        ======

        DMShapeError
            If the dimensions of the two DomainMatrix are not equal

        ValueError
            If the domain of the two DomainMatrix are not same

        Examples
        ========

        >>> from sympy import ZZ
        >>> from sympy.polys.matrices import DomainMatrix
        >>> A = DomainMatrix([
        ...    [ZZ(1), ZZ(2)],
        ...    [ZZ(3), ZZ(4)]], (2, 2), ZZ)
        >>> B = DomainMatrix([
        ...    [ZZ(4), ZZ(3)],
        ...    [ZZ(2), ZZ(1)]], (2, 2), ZZ)

        >>> A.sub(B)
        DomainMatrix([[-3, -1], [1, 3]], (2, 2), ZZ)

        See Also
        ========

        add, matmul

        """
    def neg(A):
        """
        Returns the negative of DomainMatrix

        Parameters
        ==========

        A : Represents a DomainMatrix

        Returns
        =======

        DomainMatrix
            DomainMatrix after Negation

        Examples
        ========

        >>> from sympy import ZZ
        >>> from sympy.polys.matrices import DomainMatrix
        >>> A = DomainMatrix([
        ...    [ZZ(1), ZZ(2)],
        ...    [ZZ(3), ZZ(4)]], (2, 2), ZZ)

        >>> A.neg()
        DomainMatrix([[-1, -2], [-3, -4]], (2, 2), ZZ)

        """
    def mul(A, b):
        """
        Performs term by term multiplication for the second DomainMatrix
        w.r.t first DomainMatrix. Returns a DomainMatrix whose rows are
        list of DomainMatrix matrices created after term by term multiplication.

        Parameters
        ==========

        A, B: DomainMatrix
            matrices to multiply term-wise

        Returns
        =======

        DomainMatrix
            DomainMatrix after term by term multiplication

        Examples
        ========

        >>> from sympy import ZZ
        >>> from sympy.polys.matrices import DomainMatrix
        >>> A = DomainMatrix([
        ...    [ZZ(1), ZZ(2)],
        ...    [ZZ(3), ZZ(4)]], (2, 2), ZZ)
        >>> B = DomainMatrix([
        ...    [ZZ(1), ZZ(1)],
        ...    [ZZ(0), ZZ(1)]], (2, 2), ZZ)

        >>> A.mul(B)
        DomainMatrix([[DomainMatrix([[1, 1], [0, 1]], (2, 2), ZZ),
        DomainMatrix([[2, 2], [0, 2]], (2, 2), ZZ)],
        [DomainMatrix([[3, 3], [0, 3]], (2, 2), ZZ),
        DomainMatrix([[4, 4], [0, 4]], (2, 2), ZZ)]], (2, 2), ZZ)

        See Also
        ========

        matmul

        """
    def rmul(A, b): ...
    def matmul(A, B):
        """
        Performs matrix multiplication of two DomainMatrix matrices

        Parameters
        ==========

        A, B: DomainMatrix
            to multiply

        Returns
        =======

        DomainMatrix
            DomainMatrix after multiplication

        Examples
        ========

        >>> from sympy import ZZ
        >>> from sympy.polys.matrices import DomainMatrix
        >>> A = DomainMatrix([
        ...    [ZZ(1), ZZ(2)],
        ...    [ZZ(3), ZZ(4)]], (2, 2), ZZ)
        >>> B = DomainMatrix([
        ...    [ZZ(1), ZZ(1)],
        ...    [ZZ(0), ZZ(1)]], (2, 2), ZZ)

        >>> A.matmul(B)
        DomainMatrix([[1, 3], [3, 7]], (2, 2), ZZ)

        See Also
        ========

        mul, pow, add, sub

        """
    def scalarmul(A, lamda): ...
    def rscalarmul(A, lamda): ...
    def mul_elementwise(A, B): ...
    def __truediv__(A, lamda):
        """ Method for Scalar Division"""
    def pow(A, n):
        """
        Computes A**n

        Parameters
        ==========

        A : DomainMatrix

        n : exponent for A

        Returns
        =======

        DomainMatrix
            DomainMatrix on computing A**n

        Raises
        ======

        NotImplementedError
            if n is negative.

        Examples
        ========

        >>> from sympy import ZZ
        >>> from sympy.polys.matrices import DomainMatrix
        >>> A = DomainMatrix([
        ...    [ZZ(1), ZZ(1)],
        ...    [ZZ(0), ZZ(1)]], (2, 2), ZZ)

        >>> A.pow(2)
        DomainMatrix([[1, 2], [0, 1]], (2, 2), ZZ)

        See Also
        ========

        matmul

        """
    def scc(self):
        """Compute the strongly connected components of a DomainMatrix

        Explanation
        ===========

        A square matrix can be considered as the adjacency matrix for a
        directed graph where the row and column indices are the vertices. In
        this graph if there is an edge from vertex ``i`` to vertex ``j`` if
        ``M[i, j]`` is nonzero. This routine computes the strongly connected
        components of that graph which are subsets of the rows and columns that
        are connected by some nonzero element of the matrix. The strongly
        connected components are useful because many operations such as the
        determinant can be computed by working with the submatrices
        corresponding to each component.

        Examples
        ========

        Find the strongly connected components of a matrix:

        >>> from sympy import ZZ
        >>> from sympy.polys.matrices import DomainMatrix
        >>> M = DomainMatrix([[ZZ(1), ZZ(0), ZZ(2)],
        ...                   [ZZ(0), ZZ(3), ZZ(0)],
        ...                   [ZZ(4), ZZ(6), ZZ(5)]], (3, 3), ZZ)
        >>> M.scc()
        [[1], [0, 2]]

        Compute the determinant from the components:

        >>> MM = M.to_Matrix()
        >>> MM
        Matrix([
        [1, 0, 2],
        [0, 3, 0],
        [4, 6, 5]])
        >>> MM[[1], [1]]
        Matrix([[3]])
        >>> MM[[0, 2], [0, 2]]
        Matrix([
        [1, 2],
        [4, 5]])
        >>> MM.det()
        -9
        >>> MM[[1], [1]].det() * MM[[0, 2], [0, 2]].det()
        -9

        The components are given in reverse topological order and represent a
        permutation of the rows and columns that will bring the matrix into
        block lower-triangular form:

        >>> MM[[1, 0, 2], [1, 0, 2]]
        Matrix([
        [3, 0, 0],
        [0, 1, 2],
        [6, 4, 5]])

        Returns
        =======

        List of lists of integers
            Each list represents a strongly connected component.

        See also
        ========

        sympy.matrices.matrices.MatrixBase.strongly_connected_components
        sympy.utilities.iterables.strongly_connected_components

        """
    def rref(self):
        """
        Returns reduced-row echelon form and list of pivots for the DomainMatrix

        Returns
        =======

        (DomainMatrix, list)
            reduced-row echelon form and list of pivots for the DomainMatrix

        Raises
        ======

        ValueError
            If the domain of DomainMatrix not a Field

        Examples
        ========

        >>> from sympy import QQ
        >>> from sympy.polys.matrices import DomainMatrix
        >>> A = DomainMatrix([
        ...     [QQ(2), QQ(-1), QQ(0)],
        ...     [QQ(-1), QQ(2), QQ(-1)],
        ...     [QQ(0), QQ(0), QQ(2)]], (3, 3), QQ)

        >>> rref_matrix, rref_pivots = A.rref()
        >>> rref_matrix
        DomainMatrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]], (3, 3), QQ)
        >>> rref_pivots
        (0, 1, 2)

        See Also
        ========

        convert_to, lu

        """
    def columnspace(self):
        """
        Returns the columnspace for the DomainMatrix

        Returns
        =======

        DomainMatrix
            The columns of this matrix form a basis for the columnspace.

        Examples
        ========

        >>> from sympy import QQ
        >>> from sympy.polys.matrices import DomainMatrix
        >>> A = DomainMatrix([
        ...    [QQ(1), QQ(-1)],
        ...    [QQ(2), QQ(-2)]], (2, 2), QQ)
        >>> A.columnspace()
        DomainMatrix([[1], [2]], (2, 1), QQ)

        """
    def rowspace(self):
        """
        Returns the rowspace for the DomainMatrix

        Returns
        =======

        DomainMatrix
            The rows of this matrix form a basis for the rowspace.

        Examples
        ========

        >>> from sympy import QQ
        >>> from sympy.polys.matrices import DomainMatrix
        >>> A = DomainMatrix([
        ...    [QQ(1), QQ(-1)],
        ...    [QQ(2), QQ(-2)]], (2, 2), QQ)
        >>> A.rowspace()
        DomainMatrix([[1, -1]], (1, 2), QQ)

        """
    def nullspace(self):
        """
        Returns the nullspace for the DomainMatrix

        Returns
        =======

        DomainMatrix
            The rows of this matrix form a basis for the nullspace.

        Examples
        ========

        >>> from sympy import QQ
        >>> from sympy.polys.matrices import DomainMatrix
        >>> A = DomainMatrix([
        ...    [QQ(1), QQ(-1)],
        ...    [QQ(2), QQ(-2)]], (2, 2), QQ)
        >>> A.nullspace()
        DomainMatrix([[1, 1]], (1, 2), QQ)

        """
    def inv(self):
        """
        Finds the inverse of the DomainMatrix if exists

        Returns
        =======

        DomainMatrix
            DomainMatrix after inverse

        Raises
        ======

        ValueError
            If the domain of DomainMatrix not a Field

        DMNonSquareMatrixError
            If the DomainMatrix is not a not Square DomainMatrix

        Examples
        ========

        >>> from sympy import QQ
        >>> from sympy.polys.matrices import DomainMatrix
        >>> A = DomainMatrix([
        ...     [QQ(2), QQ(-1), QQ(0)],
        ...     [QQ(-1), QQ(2), QQ(-1)],
        ...     [QQ(0), QQ(0), QQ(2)]], (3, 3), QQ)
        >>> A.inv()
        DomainMatrix([[2/3, 1/3, 1/6], [1/3, 2/3, 1/3], [0, 0, 1/2]], (3, 3), QQ)

        See Also
        ========

        neg

        """
    def det(self):
        """
        Returns the determinant of a Square DomainMatrix

        Returns
        =======

        S.Complexes
            determinant of Square DomainMatrix

        Raises
        ======

        ValueError
            If the domain of DomainMatrix not a Field

        Examples
        ========

        >>> from sympy import ZZ
        >>> from sympy.polys.matrices import DomainMatrix
        >>> A = DomainMatrix([
        ...    [ZZ(1), ZZ(2)],
        ...    [ZZ(3), ZZ(4)]], (2, 2), ZZ)

        >>> A.det()
        -2

        """
    def lu(self):
        """
        Returns Lower and Upper decomposition of the DomainMatrix

        Returns
        =======

        (L, U, exchange)
            L, U are Lower and Upper decomposition of the DomainMatrix,
            exchange is the list of indices of rows exchanged in the decomposition.

        Raises
        ======

        ValueError
            If the domain of DomainMatrix not a Field

        Examples
        ========

        >>> from sympy import QQ
        >>> from sympy.polys.matrices import DomainMatrix
        >>> A = DomainMatrix([
        ...    [QQ(1), QQ(-1)],
        ...    [QQ(2), QQ(-2)]], (2, 2), QQ)
        >>> A.lu()
        (DomainMatrix([[1, 0], [2, 1]], (2, 2), QQ), DomainMatrix([[1, -1], [0, 0]], (2, 2), QQ), [])

        See Also
        ========

        lu_solve

        """
    def lu_solve(self, rhs):
        """
        Solver for DomainMatrix x in the A*x = B

        Parameters
        ==========

        rhs : DomainMatrix B

        Returns
        =======

        DomainMatrix
            x in A*x = B

        Raises
        ======

        DMShapeError
            If the DomainMatrix A and rhs have different number of rows

        ValueError
            If the domain of DomainMatrix A not a Field

        Examples
        ========

        >>> from sympy import QQ
        >>> from sympy.polys.matrices import DomainMatrix
        >>> A = DomainMatrix([
        ...    [QQ(1), QQ(2)],
        ...    [QQ(3), QQ(4)]], (2, 2), QQ)
        >>> B = DomainMatrix([
        ...    [QQ(1), QQ(1)],
        ...    [QQ(0), QQ(1)]], (2, 2), QQ)

        >>> A.lu_solve(B)
        DomainMatrix([[-2, -1], [3/2, 1]], (2, 2), QQ)

        See Also
        ========

        lu

        """
    def charpoly(self):
        """
        Returns the coefficients of the characteristic polynomial
        of the DomainMatrix. These elements will be domain elements.
        The domain of the elements will be same as domain of the DomainMatrix.

        Returns
        =======

        list
            coefficients of the characteristic polynomial

        Raises
        ======

        DMNonSquareMatrixError
            If the DomainMatrix is not a not Square DomainMatrix

        Examples
        ========

        >>> from sympy import ZZ
        >>> from sympy.polys.matrices import DomainMatrix
        >>> A = DomainMatrix([
        ...    [ZZ(1), ZZ(2)],
        ...    [ZZ(3), ZZ(4)]], (2, 2), ZZ)

        >>> A.charpoly()
        [1, -5, -2]

        """
    @classmethod
    def eye(cls, shape, domain):
        """
        Return identity matrix of size n

        Examples
        ========

        >>> from sympy.polys.matrices import DomainMatrix
        >>> from sympy import QQ
        >>> DomainMatrix.eye(3, QQ)
        DomainMatrix({0: {0: 1}, 1: {1: 1}, 2: {2: 1}}, (3, 3), QQ)

        """
    @classmethod
    def diag(cls, diagonal, domain, shape: Incomplete | None = None):
        """
        Return diagonal matrix with entries from ``diagonal``.

        Examples
        ========

        >>> from sympy.polys.matrices import DomainMatrix
        >>> from sympy import ZZ
        >>> DomainMatrix.diag([ZZ(5), ZZ(6)], ZZ)
        DomainMatrix({0: {0: 5}, 1: {1: 6}}, (2, 2), ZZ)

        """
    @classmethod
    def zeros(cls, shape, domain, *, fmt: str = 'sparse'):
        """Returns a zero DomainMatrix of size shape, belonging to the specified domain

        Examples
        ========

        >>> from sympy.polys.matrices import DomainMatrix
        >>> from sympy import QQ
        >>> DomainMatrix.zeros((2, 3), QQ)
        DomainMatrix({}, (2, 3), QQ)

        """
    @classmethod
    def ones(cls, shape, domain):
        """Returns a DomainMatrix of 1s, of size shape, belonging to the specified domain

        Examples
        ========

        >>> from sympy.polys.matrices import DomainMatrix
        >>> from sympy import QQ
        >>> DomainMatrix.ones((2,3), QQ)
        DomainMatrix([[1, 1, 1], [1, 1, 1]], (2, 3), QQ)

        """
    def __eq__(A, B):
        """
        Checks for two DomainMatrix matrices to be equal or not

        Parameters
        ==========

        A, B: DomainMatrix
            to check equality

        Returns
        =======

        Boolean
            True for equal, else False

        Raises
        ======

        NotImplementedError
            If B is not a DomainMatrix

        Examples
        ========

        >>> from sympy import ZZ
        >>> from sympy.polys.matrices import DomainMatrix
        >>> A = DomainMatrix([
        ...    [ZZ(1), ZZ(2)],
        ...    [ZZ(3), ZZ(4)]], (2, 2), ZZ)
        >>> B = DomainMatrix([
        ...    [ZZ(1), ZZ(1)],
        ...    [ZZ(0), ZZ(1)]], (2, 2), ZZ)
        >>> A.__eq__(A)
        True
        >>> A.__eq__(B)
        False

        """
    def unify_eq(A, B): ...
    def lll(A, delta=...):
        '''
        Performs the Lenstra–Lenstra–Lovász (LLL) basis reduction algorithm.
        See [1]_ and [2]_.

        Parameters
        ==========

        delta : QQ, optional
            The Lovász parameter. Must be in the interval (0.25, 1), with larger
            values producing a more reduced basis. The default is 0.75 for
            historical reasons.

        Returns
        =======

        The reduced basis as a DomainMatrix over ZZ.

        Throws
        ======

        DMValueError: if delta is not in the range (0.25, 1)
        DMShapeError: if the matrix is not of shape (m, n) with m <= n
        DMDomainError: if the matrix domain is not ZZ
        DMRankError: if the matrix contains linearly dependent rows

        Examples
        ========

        >>> from sympy.polys.domains import ZZ, QQ
        >>> from sympy.polys.matrices import DM
        >>> x = DM([[1, 0, 0, 0, -20160],
        ...         [0, 1, 0, 0, 33768],
        ...         [0, 0, 1, 0, 39578],
        ...         [0, 0, 0, 1, 47757]], ZZ)
        >>> y = DM([[10, -3, -2, 8, -4],
        ...         [3, -9, 8, 1, -11],
        ...         [-3, 13, -9, -3, -9],
        ...         [-12, -7, -11, 9, -1]], ZZ)
        >>> assert x.lll(delta=QQ(5, 6)) == y

        Notes
        =====

        The implementation is derived from the Maple code given in Figures 4.3
        and 4.4 of [3]_ (pp.68-69). It uses the efficient method of only calculating
        state updates as they are required.

        See also
        ========

        lll_transform

        References
        ==========

        .. [1] https://en.wikipedia.org/wiki/Lenstra–Lenstra–Lovász_lattice_basis_reduction_algorithm
        .. [2] https://web.archive.org/web/20221029115428/https://web.cs.elte.hu/~lovasz/scans/lll.pdf
        .. [3] Murray R. Bremner, "Lattice Basis Reduction: An Introduction to the LLL Algorithm and Its Applications"

        '''
    def lll_transform(A, delta=...):
        """
        Performs the Lenstra–Lenstra–Lovász (LLL) basis reduction algorithm
        and returns the reduced basis and transformation matrix.

        Explanation
        ===========

        Parameters, algorithm and basis are the same as for :meth:`lll` except that
        the return value is a tuple `(B, T)` with `B` the reduced basis and
        `T` a transformation matrix. The original basis `A` is transformed to
        `B` with `T*A == B`. If only `B` is needed then :meth:`lll` should be
        used as it is a little faster.

        Examples
        ========

        >>> from sympy.polys.domains import ZZ, QQ
        >>> from sympy.polys.matrices import DM
        >>> X = DM([[1, 0, 0, 0, -20160],
        ...         [0, 1, 0, 0, 33768],
        ...         [0, 0, 1, 0, 39578],
        ...         [0, 0, 0, 1, 47757]], ZZ)
        >>> B, T = X.lll_transform(delta=QQ(5, 6))
        >>> T * X == B
        True

        See also
        ========

        lll

        """
