from _typeshed import Incomplete
from sympy.core.numbers import NumberSymbol
from sympy.core.singleton import Singleton

__all__ = ['hbar', 'HBar']

class HBar(NumberSymbol, metaclass=Singleton):
    """Reduced Plank's constant in numerical and symbolic form [1]_.

    Examples
    ========

        >>> from sympy.physics.quantum.constants import hbar
        >>> hbar.evalf()
        1.05457162000000e-34

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Planck_constant
    """
    is_real: bool
    is_positive: bool
    is_negative: bool
    is_irrational: bool

hbar: Incomplete
