from _typeshed import Incomplete

__all__ = ['represent', 'rep_innerproduct', 'rep_expectation', 'integrate_result', 'get_basis', 'enumerate_states']

def represent(expr, **options):
    """Represent the quantum expression in the given basis.

    In quantum mechanics abstract states and operators can be represented in
    various basis sets. Under this operation the follow transforms happen:

    * Ket -> column vector or function
    * Bra -> row vector of function
    * Operator -> matrix or differential operator

    This function is the top-level interface for this action.

    This function walks the SymPy expression tree looking for ``QExpr``
    instances that have a ``_represent`` method. This method is then called
    and the object is replaced by the representation returned by this method.
    By default, the ``_represent`` method will dispatch to other methods
    that handle the representation logic for a particular basis set. The
    naming convention for these methods is the following::

        def _represent_FooBasis(self, e, basis, **options)

    This function will have the logic for representing instances of its class
    in the basis set having a class named ``FooBasis``.

    Parameters
    ==========

    expr  : Expr
        The expression to represent.
    basis : Operator, basis set
        An object that contains the information about the basis set. If an
        operator is used, the basis is assumed to be the orthonormal
        eigenvectors of that operator. In general though, the basis argument
        can be any object that contains the basis set information.
    options : dict
        Key/value pairs of options that are passed to the underlying method
        that finds the representation. These options can be used to
        control how the representation is done. For example, this is where
        the size of the basis set would be set.

    Returns
    =======

    e : Expr
        The SymPy expression of the represented quantum expression.

    Examples
    ========

    Here we subclass ``Operator`` and ``Ket`` to create the z-spin operator
    and its spin 1/2 up eigenstate. By defining the ``_represent_SzOp``
    method, the ket can be represented in the z-spin basis.

    >>> from sympy.physics.quantum import Operator, represent, Ket
    >>> from sympy import Matrix

    >>> class SzUpKet(Ket):
    ...     def _represent_SzOp(self, basis, **options):
    ...         return Matrix([1,0])
    ...
    >>> class SzOp(Operator):
    ...     pass
    ...
    >>> sz = SzOp('Sz')
    >>> up = SzUpKet('up')
    >>> represent(up, basis=sz)
    Matrix([
    [1],
    [0]])

    Here we see an example of representations in a continuous
    basis. We see that the result of representing various combinations
    of cartesian position operators and kets give us continuous
    expressions involving DiracDelta functions.

    >>> from sympy.physics.quantum.cartesian import XOp, XKet, XBra
    >>> X = XOp()
    >>> x = XKet()
    >>> y = XBra('y')
    >>> represent(X*x)
    x*DiracDelta(x - x_2)
    >>> represent(X*x*y)
    x*DiracDelta(x - x_3)*DiracDelta(x_1 - y)

    """
def rep_innerproduct(expr, **options):
    """
    Returns an innerproduct like representation (e.g. ``<x'|x>``) for the
    given state.

    Attempts to calculate inner product with a bra from the specified
    basis. Should only be passed an instance of KetBase or BraBase

    Parameters
    ==========

    expr : KetBase or BraBase
        The expression to be represented

    Examples
    ========

    >>> from sympy.physics.quantum.represent import rep_innerproduct
    >>> from sympy.physics.quantum.cartesian import XOp, XKet, PxOp, PxKet
    >>> rep_innerproduct(XKet())
    DiracDelta(x - x_1)
    >>> rep_innerproduct(XKet(), basis=PxOp())
    sqrt(2)*exp(-I*px_1*x/hbar)/(2*sqrt(hbar)*sqrt(pi))
    >>> rep_innerproduct(PxKet(), basis=XOp())
    sqrt(2)*exp(I*px*x_1/hbar)/(2*sqrt(hbar)*sqrt(pi))

    """
def rep_expectation(expr, **options):
    """
    Returns an ``<x'|A|x>`` type representation for the given operator.

    Parameters
    ==========

    expr : Operator
        Operator to be represented in the specified basis

    Examples
    ========

    >>> from sympy.physics.quantum.cartesian import XOp, PxOp, PxKet
    >>> from sympy.physics.quantum.represent import rep_expectation
    >>> rep_expectation(XOp())
    x_1*DiracDelta(x_1 - x_2)
    >>> rep_expectation(XOp(), basis=PxOp())
    <px_2|*X*|px_1>
    >>> rep_expectation(XOp(), basis=PxKet())
    <px_2|*X*|px_1>

    """
def integrate_result(orig_expr, result, **options):
    """
    Returns the result of integrating over any unities ``(|x><x|)`` in
    the given expression. Intended for integrating over the result of
    representations in continuous bases.

    This function integrates over any unities that may have been
    inserted into the quantum expression and returns the result.
    It uses the interval of the Hilbert space of the basis state
    passed to it in order to figure out the limits of integration.
    The unities option must be
    specified for this to work.

    Note: This is mostly used internally by represent(). Examples are
    given merely to show the use cases.

    Parameters
    ==========

    orig_expr : quantum expression
        The original expression which was to be represented

    result: Expr
        The resulting representation that we wish to integrate over

    Examples
    ========

    >>> from sympy import symbols, DiracDelta
    >>> from sympy.physics.quantum.represent import integrate_result
    >>> from sympy.physics.quantum.cartesian import XOp, XKet
    >>> x_ket = XKet()
    >>> X_op = XOp()
    >>> x, x_1, x_2 = symbols('x, x_1, x_2')
    >>> integrate_result(X_op*x_ket, x*DiracDelta(x-x_1)*DiracDelta(x_1-x_2))
    x*DiracDelta(x - x_1)*DiracDelta(x_1 - x_2)
    >>> integrate_result(X_op*x_ket, x*DiracDelta(x-x_1)*DiracDelta(x_1-x_2),
    ...     unities=[1])
    x*DiracDelta(x - x_2)

    """
def get_basis(expr, *, basis: Incomplete | None = None, replace_none: bool = True, **options):
    """
    Returns a basis state instance corresponding to the basis specified in
    options=s. If no basis is specified, the function tries to form a default
    basis state of the given expression.

    There are three behaviors:

    1. The basis specified in options is already an instance of StateBase. If
       this is the case, it is simply returned. If the class is specified but
       not an instance, a default instance is returned.

    2. The basis specified is an operator or set of operators. If this
       is the case, the operator_to_state mapping method is used.

    3. No basis is specified. If expr is a state, then a default instance of
       its class is returned.  If expr is an operator, then it is mapped to the
       corresponding state.  If it is neither, then we cannot obtain the basis
       state.

    If the basis cannot be mapped, then it is not changed.

    This will be called from within represent, and represent will
    only pass QExpr's.

    TODO (?): Support for Muls and other types of expressions?

    Parameters
    ==========

    expr : Operator or StateBase
        Expression whose basis is sought

    Examples
    ========

    >>> from sympy.physics.quantum.represent import get_basis
    >>> from sympy.physics.quantum.cartesian import XOp, XKet, PxOp, PxKet
    >>> x = XKet()
    >>> X = XOp()
    >>> get_basis(x)
    |x>
    >>> get_basis(X)
    |x>
    >>> get_basis(x, basis=PxOp())
    |px>
    >>> get_basis(x, basis=PxKet)
    |px>

    """
def enumerate_states(*args, **options):
    """
    Returns instances of the given state with dummy indices appended

    Operates in two different modes:

    1. Two arguments are passed to it. The first is the base state which is to
       be indexed, and the second argument is a list of indices to append.

    2. Three arguments are passed. The first is again the base state to be
       indexed. The second is the start index for counting.  The final argument
       is the number of kets you wish to receive.

    Tries to call state._enumerate_state. If this fails, returns an empty list

    Parameters
    ==========

    args : list
        See list of operation modes above for explanation

    Examples
    ========

    >>> from sympy.physics.quantum.cartesian import XBra, XKet
    >>> from sympy.physics.quantum.represent import enumerate_states
    >>> test = XKet('foo')
    >>> enumerate_states(test, 1, 3)
    [|foo_1>, |foo_2>, |foo_3>]
    >>> test2 = XBra('bar')
    >>> enumerate_states(test2, [4, 5, 10])
    [<bar_4|, <bar_5|, <bar_10|]

    """
