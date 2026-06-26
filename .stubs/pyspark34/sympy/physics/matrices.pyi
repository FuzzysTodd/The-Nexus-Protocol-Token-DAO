from _typeshed import Incomplete
from sympy.core.numbers import I as I
from sympy.utilities.decorator import deprecated as deprecated

def msigma(i):
    """Returns a Pauli matrix `\\sigma_i` with `i=1,2,3`.

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Pauli_matrices

    Examples
    ========

    >>> from sympy.physics.matrices import msigma
    >>> msigma(1)
    Matrix([
    [0, 1],
    [1, 0]])
    """
def pat_matrix(m, dx, dy, dz):
    """Returns the Parallel Axis Theorem matrix to translate the inertia
    matrix a distance of `(dx, dy, dz)` for a body of mass m.

    Examples
    ========

    To translate a body having a mass of 2 units a distance of 1 unit along
    the `x`-axis we get:

    >>> from sympy.physics.matrices import pat_matrix
    >>> pat_matrix(2, 1, 0, 0)
    Matrix([
    [0, 0, 0],
    [0, 2, 0],
    [0, 0, 2]])

    """
def mgamma(mu, lower: bool = False):
    """Returns a Dirac gamma matrix `\\gamma^\\mu` in the standard
    (Dirac) representation.

    Explanation
    ===========

    If you want `\\gamma_\\mu`, use ``gamma(mu, True)``.

    We use a convention:

    `\\gamma^5 = i \\cdot \\gamma^0 \\cdot \\gamma^1 \\cdot \\gamma^2 \\cdot \\gamma^3`

    `\\gamma_5 = i \\cdot \\gamma_0 \\cdot \\gamma_1 \\cdot \\gamma_2 \\cdot \\gamma_3 = - \\gamma^5`

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Gamma_matrices

    Examples
    ========

    >>> from sympy.physics.matrices import mgamma
    >>> mgamma(1)
    Matrix([
    [ 0,  0, 0, 1],
    [ 0,  0, 1, 0],
    [ 0, -1, 0, 0],
    [-1,  0, 0, 0]])
    """

minkowski_tensor: Incomplete

def mdft(n):
    """
    .. deprecated:: 1.9

       Use DFT from sympy.matrices.expressions.fourier instead.

       To get identical behavior to ``mdft(n)``, use ``DFT(n).as_explicit()``.
    """
