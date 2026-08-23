from .dense import ddm_berk as ddm_berk, ddm_iadd as ddm_iadd, ddm_idet as ddm_idet, ddm_iinv as ddm_iinv, ddm_ilu_solve as ddm_ilu_solve, ddm_ilu_split as ddm_ilu_split, ddm_imatmul as ddm_imatmul, ddm_imul as ddm_imul, ddm_ineg as ddm_ineg, ddm_irmul as ddm_irmul, ddm_irref as ddm_irref, ddm_isub as ddm_isub, ddm_transpose as ddm_transpose
from .exceptions import DMBadInputError as DMBadInputError, DMDomainError as DMDomainError, DMShapeError as DMShapeError
from .lll import ddm_lll as ddm_lll, ddm_lll_transform as ddm_lll_transform
from .sdm import SDM as SDM
from _typeshed import Incomplete
from sympy.polys.domains import QQ as QQ

class DDM(list):
    """Dense matrix based on polys domain elements

    This is a list subclass and is a wrapper for a list of lists that supports
    basic matrix arithmetic +, -, *, **.
    """
    fmt: str
    shape: Incomplete
    domain: Incomplete
    def __init__(self, rowslist, shape, domain) -> None: ...
    def getitem(self, i, j): ...
    def setitem(self, i, j, value) -> None: ...
    def extract_slice(self, slice1, slice2): ...
    def extract(self, rows, cols): ...
    def to_list(self): ...
    def to_list_flat(self): ...
    def flatiter(self): ...
    def flat(self): ...
    def to_dok(self): ...
    def to_ddm(self): ...
    def to_sdm(self): ...
    def convert_to(self, K): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    @classmethod
    def zeros(cls, shape, domain): ...
    @classmethod
    def ones(cls, shape, domain): ...
    @classmethod
    def eye(cls, size, domain): ...
    def copy(self): ...
    def transpose(self): ...
    def __add__(a, b): ...
    def __sub__(a, b): ...
    def __neg__(a): ...
    def __mul__(a, b): ...
    def __rmul__(a, b): ...
    def __matmul__(a, b): ...
    def add(a, b):
        """a + b"""
    def sub(a, b):
        """a - b"""
    def neg(a):
        """-a"""
    def mul(a, b): ...
    def rmul(a, b): ...
    def matmul(a, b):
        """a @ b (matrix product)"""
    def mul_elementwise(a, b): ...
    def hstack(A, *B):
        """Horizontally stacks :py:class:`~.DDM` matrices.

        Examples
        ========

        >>> from sympy import ZZ
        >>> from sympy.polys.matrices.sdm import DDM

        >>> A = DDM([[ZZ(1), ZZ(2)], [ZZ(3), ZZ(4)]], (2, 2), ZZ)
        >>> B = DDM([[ZZ(5), ZZ(6)], [ZZ(7), ZZ(8)]], (2, 2), ZZ)
        >>> A.hstack(B)
        [[1, 2, 5, 6], [3, 4, 7, 8]]

        >>> C = DDM([[ZZ(9), ZZ(10)], [ZZ(11), ZZ(12)]], (2, 2), ZZ)
        >>> A.hstack(B, C)
        [[1, 2, 5, 6, 9, 10], [3, 4, 7, 8, 11, 12]]
        """
    def vstack(A, *B):
        """Vertically stacks :py:class:`~.DDM` matrices.

        Examples
        ========

        >>> from sympy import ZZ
        >>> from sympy.polys.matrices.sdm import DDM

        >>> A = DDM([[ZZ(1), ZZ(2)], [ZZ(3), ZZ(4)]], (2, 2), ZZ)
        >>> B = DDM([[ZZ(5), ZZ(6)], [ZZ(7), ZZ(8)]], (2, 2), ZZ)
        >>> A.vstack(B)
        [[1, 2], [3, 4], [5, 6], [7, 8]]

        >>> C = DDM([[ZZ(9), ZZ(10)], [ZZ(11), ZZ(12)]], (2, 2), ZZ)
        >>> A.vstack(B, C)
        [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]]
        """
    def applyfunc(self, func, domain): ...
    def scc(a):
        """Strongly connected components of a square matrix *a*.

        Examples
        ========

        >>> from sympy import ZZ
        >>> from sympy.polys.matrices.sdm import DDM
        >>> A = DDM([[ZZ(1), ZZ(0)], [ZZ(0), ZZ(1)]], (2, 2), ZZ)
        >>> A.scc()
        [[0], [1]]

        See also
        ========

        sympy.polys.matrices.domainmatrix.DomainMatrix.scc

        """
    def rref(a):
        """Reduced-row echelon form of a and list of pivots"""
    def nullspace(a): ...
    def particular(a): ...
    def det(a):
        """Determinant of a"""
    def inv(a):
        """Inverse of a"""
    def lu(a):
        """L, U decomposition of a"""
    def lu_solve(a, b):
        """x where a*x = b"""
    def charpoly(a):
        """Coefficients of characteristic polynomial of a"""
    def is_zero_matrix(self):
        """
        Says whether this matrix has all zero entries.
        """
    def is_upper(self):
        """
        Says whether this matrix is upper-triangular. True can be returned
        even if the matrix is not square.
        """
    def is_lower(self):
        """
        Says whether this matrix is lower-triangular. True can be returned
        even if the matrix is not square.
        """
    def lll(A, delta=...): ...
    def lll_transform(A, delta=...): ...
