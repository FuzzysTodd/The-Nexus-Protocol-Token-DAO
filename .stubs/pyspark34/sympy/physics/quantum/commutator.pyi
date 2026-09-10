from sympy.core.expr import Expr

__all__ = ['Commutator']

class Commutator(Expr):
    """The standard commutator, in an unevaluated state.

    Explanation
    ===========

    Evaluating a commutator is defined [1]_ as: ``[A, B] = A*B - B*A``. This
    class returns the commutator in an unevaluated form. To evaluate the
    commutator, use the ``.doit()`` method.

    Canonical ordering of a commutator is ``[A, B]`` for ``A < B``. The
    arguments of the commutator are put into canonical order using ``__cmp__``.
    If ``B < A``, then ``[B, A]`` is returned as ``-[A, B]``.

    Parameters
    ==========

    A : Expr
        The first argument of the commutator [A,B].
    B : Expr
        The second argument of the commutator [A,B].

    Examples
    ========

    >>> from sympy.physics.quantum import Commutator, Dagger, Operator
    >>> from sympy.abc import x, y
    >>> A = Operator('A')
    >>> B = Operator('B')
    >>> C = Operator('C')

    Create a commutator and use ``.doit()`` to evaluate it:

    >>> comm = Commutator(A, B)
    >>> comm
    [A,B]
    >>> comm.doit()
    A*B - B*A

    The commutator orders it arguments in canonical order:

    >>> comm = Commutator(B, A); comm
    -[A,B]

    Commutative constants are factored out:

    >>> Commutator(3*x*A, x*y*B)
    3*x**2*y*[A,B]

    Using ``.expand(commutator=True)``, the standard commutator expansion rules
    can be applied:

    >>> Commutator(A+B, C).expand(commutator=True)
    [A,C] + [B,C]
    >>> Commutator(A, B+C).expand(commutator=True)
    [A,B] + [A,C]
    >>> Commutator(A*B, C).expand(commutator=True)
    [A,C]*B + A*[B,C]
    >>> Commutator(A, B*C).expand(commutator=True)
    [A,B]*C + B*[A,C]

    Adjoint operations applied to the commutator are properly applied to the
    arguments:

    >>> Dagger(Commutator(A, B))
    -[Dagger(A),Dagger(B)]

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Commutator
    """
    is_commutative: bool
    def __new__(cls, A, B): ...
    @classmethod
    def eval(cls, a, b): ...
    def doit(self, **hints):
        """ Evaluate commutator """
