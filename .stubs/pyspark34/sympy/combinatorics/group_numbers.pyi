from sympy import factorint as factorint
from sympy.core import Integer as Integer, Mod as Mod, Pow as Pow

def is_nilpotent_number(n):
    """
    Check whether `n` is a nilpotent number. A number `n` is said to be
    nilpotent if and only if every finite group of order `n` is nilpotent.
    For more information see [1]_.

    Examples
    ========

    >>> from sympy.combinatorics.group_numbers import is_nilpotent_number
    >>> from sympy import randprime
    >>> is_nilpotent_number(21)
    False
    >>> is_nilpotent_number(randprime(1, 30)**12)
    True

    References
    ==========

    .. [1] Pakianathan, J., Shankar, K., *Nilpotent Numbers*,
            The American Mathematical Monthly, 107(7), 631-634.


    """
def is_abelian_number(n):
    """
    Check whether `n` is an abelian number. A number `n` is said to be abelian
    if and only if every finite group of order `n` is abelian. For more
    information see [1]_.

    Examples
    ========

    >>> from sympy.combinatorics.group_numbers import is_abelian_number
    >>> from sympy import randprime
    >>> is_abelian_number(4)
    True
    >>> is_abelian_number(randprime(1, 2000)**2)
    True
    >>> is_abelian_number(60)
    False

    References
    ==========

    .. [1] Pakianathan, J., Shankar, K., *Nilpotent Numbers*,
            The American Mathematical Monthly, 107(7), 631-634.


    """
def is_cyclic_number(n):
    """
    Check whether `n` is a cyclic number. A number `n` is said to be cyclic
    if and only if every finite group of order `n` is cyclic. For more
    information see [1]_.

    Examples
    ========

    >>> from sympy.combinatorics.group_numbers import is_cyclic_number
    >>> from sympy import randprime
    >>> is_cyclic_number(15)
    True
    >>> is_cyclic_number(randprime(1, 2000)**2)
    False
    >>> is_cyclic_number(4)
    False

    References
    ==========

    .. [1] Pakianathan, J., Shankar, K., *Nilpotent Numbers*,
            The American Mathematical Monthly, 107(7), 631-634.

    """
