from _typeshed import Incomplete
from sympy.core.mul import Mul as Mul
from sympy.core.singleton import S as S
from sympy.matrices.dense import eye as eye
from sympy.matrices.expressions.trace import trace as trace
from sympy.tensor.tensor import TensAdd as TensAdd, TensMul as TensMul, Tensor as Tensor, TensorHead as TensorHead, TensorIndex as TensorIndex, TensorIndexType as TensorIndexType, TensorSymmetry as TensorSymmetry, tensor_mul as tensor_mul

LorentzIndex: Incomplete
GammaMatrix: Incomplete

def extract_type_tens(expression, component):
    """
    Extract from a ``TensExpr`` all tensors with `component`.

    Returns two tensor expressions:

    * the first contains all ``Tensor`` of having `component`.
    * the second contains all remaining.


    """
def simplify_gamma_expression(expression): ...
def simplify_gpgp(ex, sort: bool = True):
    """
    simplify products ``G(i)*p(-i)*G(j)*p(-j) -> p(i)*p(-i)``

    Examples
    ========

    >>> from sympy.physics.hep.gamma_matrices import GammaMatrix as G,         LorentzIndex, simplify_gpgp
    >>> from sympy.tensor.tensor import tensor_indices, tensor_heads
    >>> p, q = tensor_heads('p, q', [LorentzIndex])
    >>> i0,i1,i2,i3,i4,i5 = tensor_indices('i0:6', LorentzIndex)
    >>> ps = p(i0)*G(-i0)
    >>> qs = q(i0)*G(-i0)
    >>> simplify_gpgp(ps*qs*qs)
    GammaMatrix(-L_0)*p(L_0)*q(L_1)*q(-L_1)
    """
def gamma_trace(t):
    """
    trace of a single line of gamma matrices

    Examples
    ========

    >>> from sympy.physics.hep.gamma_matrices import GammaMatrix as G,         gamma_trace, LorentzIndex
    >>> from sympy.tensor.tensor import tensor_indices, tensor_heads
    >>> p, q = tensor_heads('p, q', [LorentzIndex])
    >>> i0,i1,i2,i3,i4,i5 = tensor_indices('i0:6', LorentzIndex)
    >>> ps = p(i0)*G(-i0)
    >>> qs = q(i0)*G(-i0)
    >>> gamma_trace(G(i0)*G(i1))
    4*metric(i0, i1)
    >>> gamma_trace(ps*ps) - 4*p(i0)*p(-i0)
    0
    >>> gamma_trace(ps*qs + ps*ps) - 4*p(i0)*p(-i0) - 4*p(i0)*q(-i0)
    0

    """
def kahane_simplify(expression):
    """
    This function cancels contracted elements in a product of four
    dimensional gamma matrices, resulting in an expression equal to the given
    one, without the contracted gamma matrices.

    Parameters
    ==========

    `expression`    the tensor expression containing the gamma matrices to simplify.

    Notes
    =====

    If spinor indices are given, the matrices must be given in
    the order given in the product.

    Algorithm
    =========

    The idea behind the algorithm is to use some well-known identities,
    i.e., for contractions enclosing an even number of `\\gamma` matrices

    `\\gamma^\\mu \\gamma_{a_1} \\cdots \\gamma_{a_{2N}} \\gamma_\\mu = 2 (\\gamma_{a_{2N}} \\gamma_{a_1} \\cdots \\gamma_{a_{2N-1}} + \\gamma_{a_{2N-1}} \\cdots \\gamma_{a_1} \\gamma_{a_{2N}} )`

    for an odd number of `\\gamma` matrices

    `\\gamma^\\mu \\gamma_{a_1} \\cdots \\gamma_{a_{2N+1}} \\gamma_\\mu = -2 \\gamma_{a_{2N+1}} \\gamma_{a_{2N}} \\cdots \\gamma_{a_{1}}`

    Instead of repeatedly applying these identities to cancel out all contracted indices,
    it is possible to recognize the links that would result from such an operation,
    the problem is thus reduced to a simple rearrangement of free gamma matrices.

    Examples
    ========

    When using, always remember that the original expression coefficient
    has to be handled separately

    >>> from sympy.physics.hep.gamma_matrices import GammaMatrix as G, LorentzIndex
    >>> from sympy.physics.hep.gamma_matrices import kahane_simplify
    >>> from sympy.tensor.tensor import tensor_indices
    >>> i0, i1, i2 = tensor_indices('i0:3', LorentzIndex)
    >>> ta = G(i0)*G(-i0)
    >>> kahane_simplify(ta)
    Matrix([
    [4, 0, 0, 0],
    [0, 4, 0, 0],
    [0, 0, 4, 0],
    [0, 0, 0, 4]])
    >>> tb = G(i0)*G(i1)*G(-i0)
    >>> kahane_simplify(tb)
    -2*GammaMatrix(i1)
    >>> t = G(i0)*G(-i0)
    >>> kahane_simplify(t)
    Matrix([
    [4, 0, 0, 0],
    [0, 4, 0, 0],
    [0, 0, 4, 0],
    [0, 0, 0, 4]])
    >>> t = G(i0)*G(-i0)
    >>> kahane_simplify(t)
    Matrix([
    [4, 0, 0, 0],
    [0, 4, 0, 0],
    [0, 0, 4, 0],
    [0, 0, 0, 4]])

    If there are no contractions, the same expression is returned

    >>> tc = G(i0)*G(i1)
    >>> kahane_simplify(tc)
    GammaMatrix(i0)*GammaMatrix(i1)

    References
    ==========

    [1] Algorithm for Reducing Contracted Products of gamma Matrices,
    Joseph Kahane, Journal of Mathematical Physics, Vol. 9, No. 10, October 1968.
    """
