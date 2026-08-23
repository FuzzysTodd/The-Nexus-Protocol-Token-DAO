from sympy.core import Symbol as Symbol
from sympy.logic.boolalg import And as And, Or as Or

def load(s):
    """Loads a boolean expression from a string.

    Examples
    ========

    >>> from sympy.logic.utilities.dimacs import load
    >>> load('1')
    cnf_1
    >>> load('1 2')
    cnf_1 | cnf_2
    >>> load('1 \\n 2')
    cnf_1 & cnf_2
    >>> load('1 2 \\n 3')
    cnf_3 & (cnf_1 | cnf_2)
    """
def load_file(location):
    """Loads a boolean expression from a file."""
