from .errors import LaTeXParsingError as LaTeXParsingError
from sympy.external import import_module as import_module
from sympy.utilities.decorator import doctest_depends_on as doctest_depends_on

def parse_latex(s):
    '''Converts the string ``s`` to a SymPy ``Expr``

    Parameters
    ==========

    s : str
        The LaTeX string to parse. In Python source containing LaTeX,
        *raw strings* (denoted with ``r"``, like this one) are preferred,
        as LaTeX makes liberal use of the ``\\`` character, which would
        trigger escaping in normal Python strings.

    Examples
    ========

    >>> from sympy.parsing.latex import parse_latex
    >>> expr = parse_latex(r"\\frac {1 + \\sqrt {\\a}} {\\b}")
    >>> expr
    (sqrt(a) + 1)/b
    >>> expr.evalf(4, subs=dict(a=5, b=2))
    1.618
    '''
