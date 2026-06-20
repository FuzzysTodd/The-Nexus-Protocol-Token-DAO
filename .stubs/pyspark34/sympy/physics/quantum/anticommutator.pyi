from sympy.core.expr import Expr

__all__ = ['AntiCommutator']

class AntiCommutator(Expr):
    """The standard anticommutator, in an unevaluated state.

    Explanation
    ===========

    Evaluating an anticommutator is defined [1]_ as: ``{A, B} = A*B + B*A``.
    This class returns the anticommutator in an unevaluated form.  To evaluate
    the anticommutator, use the ``.doit()`` method.

    Canonical ordering of an anticommutator is ``{A, B}`` for ``A < B``. The
    arguments of the anticommutator are put into canonical order using
    ``__cmp__``. If ``B < A``, then ``{A, B}`` is returned as ``{B, A}``.

    Parameters
    ==========

    A : Expr
        The first argument of the anticommutator {A,B}.
    B : Expr
        The second argument of the anticommutator {A,B}.

    Examples
    ========

    >>> from sympy import symbols
    >>> from sympy.physics.quantum import AntiCommutator
    >>> from sympy.physics.quantum import Operator, Dagger
    >>> x, y = symbols('x,y')
    >>> A = Operator('A')
    >>> B = Operator('B')

    Create an anticommutator and use ``doit()`` to multiply them out.

    >>> ac = AntiCommutator(A,B); ac
    {A,B}
    >>> ac.doit()
    A*B + B*A

    The commutator orders it arguments in canonical order:

    >>> ac = AntiCommutator(B,A); ac
    {A,B}

    Commutative constants are factored out:

    >>> AntiCommutator(3*x*A,x*y*B)
    3*x**2*y*{A,B}

    Adjoint operations applied to the anticommutator are properly applied to
    the arguments:

    >>> Dagger(AntiCommutator(A,B))
    {Dagger(A),Dagger(B)}

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Commutator
    """
    is_commutative: bool
    def __new__(cls, A, B): ...
    @classmethod
    def eval(cls, a, b): ...
    def doit(self, **hints):
        """ Evaluate anticommutator """
