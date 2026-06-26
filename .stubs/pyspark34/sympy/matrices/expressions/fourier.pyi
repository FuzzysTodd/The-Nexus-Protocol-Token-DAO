from _typeshed import Incomplete
from sympy.core.numbers import I as I
from sympy.core.singleton import S as S
from sympy.functions.elementary.exponential import exp as exp
from sympy.functions.elementary.miscellaneous import sqrt as sqrt
from sympy.matrices.expressions import MatrixExpr as MatrixExpr

class DFT(MatrixExpr):
    """
    Returns a discrete Fourier transform matrix. The matrix is scaled
    with :math:`\\frac{1}{\\sqrt{n}}` so that it is unitary.

    Parameters
    ==========

    n : integer or Symbol
        Size of the transform.

    Examples
    ========

    >>> from sympy.abc import n
    >>> from sympy.matrices.expressions.fourier import DFT
    >>> DFT(3)
    DFT(3)
    >>> DFT(3).as_explicit()
    Matrix([
    [sqrt(3)/3,                sqrt(3)/3,                sqrt(3)/3],
    [sqrt(3)/3, sqrt(3)*exp(-2*I*pi/3)/3,  sqrt(3)*exp(2*I*pi/3)/3],
    [sqrt(3)/3,  sqrt(3)*exp(2*I*pi/3)/3, sqrt(3)*exp(-2*I*pi/3)/3]])
    >>> DFT(n).shape
    (n, n)

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/DFT_matrix

    """
    def __new__(cls, n): ...
    n: Incomplete
    shape: Incomplete

class IDFT(DFT):
    """
    Returns an inverse discrete Fourier transform matrix. The matrix is scaled
    with :math:`\\frac{1}{\\sqrt{n}}` so that it is unitary.

    Parameters
    ==========

    n : integer or Symbol
        Size of the transform

    Examples
    ========

    >>> from sympy.matrices.expressions.fourier import DFT, IDFT
    >>> IDFT(3)
    IDFT(3)
    >>> IDFT(4)*DFT(4)
    I

    See Also
    ========

    DFT

    """
