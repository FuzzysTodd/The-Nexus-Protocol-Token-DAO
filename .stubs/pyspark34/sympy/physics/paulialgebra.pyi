from sympy.core.symbol import Symbol

__all__ = ['evaluate_pauli_product']

class Pauli(Symbol):
    '''
    The class representing algebraic properties of Pauli matrices.

    Explanation
    ===========

    The symbol used to display the Pauli matrices can be changed with an
    optional parameter ``label="sigma"``. Pauli matrices with different
    ``label`` attributes cannot multiply together.

    If the left multiplication of symbol or number with Pauli matrix is needed,
    please use parentheses  to separate Pauli and symbolic multiplication
    (for example: 2*I*(Pauli(3)*Pauli(2))).

    Another variant is to use evaluate_pauli_product function to evaluate
    the product of Pauli matrices and other symbols (with commutative
    multiply rules).

    See Also
    ========

    evaluate_pauli_product

    Examples
    ========

    >>> from sympy.physics.paulialgebra import Pauli
    >>> Pauli(1)
    sigma1
    >>> Pauli(1)*Pauli(2)
    I*sigma3
    >>> Pauli(1)*Pauli(1)
    1
    >>> Pauli(3)**4
    1
    >>> Pauli(1)*Pauli(2)*Pauli(3)
    I

    >>> from sympy.physics.paulialgebra import Pauli
    >>> Pauli(1, label="tau")
    tau1
    >>> Pauli(1)*Pauli(2, label="tau")
    sigma1*tau2
    >>> Pauli(1, label="tau")*Pauli(2, label="tau")
    I*tau3

    >>> from sympy import I
    >>> I*(Pauli(2)*Pauli(3))
    -sigma1

    >>> from sympy.physics.paulialgebra import evaluate_pauli_product
    >>> f = I*Pauli(2)*Pauli(3)
    >>> f
    I*sigma2*sigma3
    >>> evaluate_pauli_product(f)
    -sigma1
    '''
    def __new__(cls, i, label: str = 'sigma'): ...
    def __getnewargs_ex__(self): ...
    def __mul__(self, other): ...

def evaluate_pauli_product(arg):
    """Help function to evaluate Pauli matrices product
    with symbolic objects.

    Parameters
    ==========

    arg: symbolic expression that contains Paulimatrices

    Examples
    ========

    >>> from sympy.physics.paulialgebra import Pauli, evaluate_pauli_product
    >>> from sympy import I
    >>> evaluate_pauli_product(I*Pauli(1)*Pauli(2))
    -sigma3

    >>> from sympy.abc import x
    >>> evaluate_pauli_product(x**2*Pauli(2)*Pauli(1))
    -I*x**2*sigma3
    """
