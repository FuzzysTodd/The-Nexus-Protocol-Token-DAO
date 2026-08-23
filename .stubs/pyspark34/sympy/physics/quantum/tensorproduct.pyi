from sympy.core.expr import Expr

__all__ = ['TensorProduct', 'tensor_product_simp']

class TensorProduct(Expr):
    """The tensor product of two or more arguments.

    For matrices, this uses ``matrix_tensor_product`` to compute the Kronecker
    or tensor product matrix. For other objects a symbolic ``TensorProduct``
    instance is returned. The tensor product is a non-commutative
    multiplication that is used primarily with operators and states in quantum
    mechanics.

    Currently, the tensor product distinguishes between commutative and
    non-commutative arguments.  Commutative arguments are assumed to be scalars
    and are pulled out in front of the ``TensorProduct``. Non-commutative
    arguments remain in the resulting ``TensorProduct``.

    Parameters
    ==========

    args : tuple
        A sequence of the objects to take the tensor product of.

    Examples
    ========

    Start with a simple tensor product of SymPy matrices::

        >>> from sympy import Matrix
        >>> from sympy.physics.quantum import TensorProduct

        >>> m1 = Matrix([[1,2],[3,4]])
        >>> m2 = Matrix([[1,0],[0,1]])
        >>> TensorProduct(m1, m2)
        Matrix([
        [1, 0, 2, 0],
        [0, 1, 0, 2],
        [3, 0, 4, 0],
        [0, 3, 0, 4]])
        >>> TensorProduct(m2, m1)
        Matrix([
        [1, 2, 0, 0],
        [3, 4, 0, 0],
        [0, 0, 1, 2],
        [0, 0, 3, 4]])

    We can also construct tensor products of non-commutative symbols:

        >>> from sympy import Symbol
        >>> A = Symbol('A',commutative=False)
        >>> B = Symbol('B',commutative=False)
        >>> tp = TensorProduct(A, B)
        >>> tp
        AxB

    We can take the dagger of a tensor product (note the order does NOT reverse
    like the dagger of a normal product):

        >>> from sympy.physics.quantum import Dagger
        >>> Dagger(tp)
        Dagger(A)xDagger(B)

    Expand can be used to distribute a tensor product across addition:

        >>> C = Symbol('C',commutative=False)
        >>> tp = TensorProduct(A+B,C)
        >>> tp
        (A + B)xC
        >>> tp.expand(tensorproduct=True)
        AxC + BxC
    """
    is_commutative: bool
    def __new__(cls, *args): ...
    @classmethod
    def flatten(cls, args): ...
    def doit(self, **hints): ...

def tensor_product_simp(e, **hints):
    """Try to simplify and combine TensorProducts.

    In general this will try to pull expressions inside of ``TensorProducts``.
    It currently only works for relatively simple cases where the products have
    only scalars, raw ``TensorProducts``, not ``Add``, ``Pow``, ``Commutators``
    of ``TensorProducts``. It is best to see what it does by showing examples.

    Examples
    ========

    >>> from sympy.physics.quantum import tensor_product_simp
    >>> from sympy.physics.quantum import TensorProduct
    >>> from sympy import Symbol
    >>> A = Symbol('A',commutative=False)
    >>> B = Symbol('B',commutative=False)
    >>> C = Symbol('C',commutative=False)
    >>> D = Symbol('D',commutative=False)

    First see what happens to products of tensor products:

    >>> e = TensorProduct(A,B)*TensorProduct(C,D)
    >>> e
    AxB*CxD
    >>> tensor_product_simp(e)
    (A*C)x(B*D)

    This is the core logic of this function, and it works inside, powers, sums,
    commutators and anticommutators as well:

    >>> tensor_product_simp(e**2)
    (A*C)x(B*D)**2

    """
