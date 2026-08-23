from _typeshed import Incomplete
from sympy.core.numbers import equal_valued as equal_valued
from sympy.printing.codeprinter import CodePrinter as CodePrinter
from sympy.printing.precedence import PRECEDENCE as PRECEDENCE, precedence as precedence
from sympy.sets.fancysets import Range as Range

known_functions: Incomplete
reserved_words: Incomplete

class RCodePrinter(CodePrinter):
    """A printer to convert SymPy expressions to strings of R code"""
    printmethod: str
    language: str
    known_functions: Incomplete
    reserved_words: Incomplete
    def __init__(self, settings={}) -> None: ...
    def indent_code(self, code):
        """Accepts a string of code or a list of code lines"""

def rcode(expr, assign_to: Incomplete | None = None, **settings):
    '''Converts an expr to a string of r code

    Parameters
    ==========

    expr : Expr
        A SymPy expression to be converted.
    assign_to : optional
        When given, the argument is used as the name of the variable to which
        the expression is assigned. Can be a string, ``Symbol``,
        ``MatrixSymbol``, or ``Indexed`` type. This is helpful in case of
        line-wrapping, or for expressions that generate multi-line statements.
    precision : integer, optional
        The precision for numbers such as pi [default=15].
    user_functions : dict, optional
        A dictionary where the keys are string representations of either
        ``FunctionClass`` or ``UndefinedFunction`` instances and the values
        are their desired R string representations. Alternatively, the
        dictionary value can be a list of tuples i.e. [(argument_test,
        rfunction_string)] or [(argument_test, rfunction_formater)]. See below
        for examples.
    human : bool, optional
        If True, the result is a single string that may contain some constant
        declarations for the number symbols. If False, the same information is
        returned in a tuple of (symbols_to_declare, not_supported_functions,
        code_text). [default=True].
    contract: bool, optional
        If True, ``Indexed`` instances are assumed to obey tensor contraction
        rules and the corresponding nested loops over indices are generated.
        Setting contract=False will not generate loops, instead the user is
        responsible to provide values for the indices in the code.
        [default=True].

    Examples
    ========

    >>> from sympy import rcode, symbols, Rational, sin, ceiling, Abs, Function
    >>> x, tau = symbols("x, tau")
    >>> rcode((2*tau)**Rational(7, 2))
    \'8*sqrt(2)*tau^(7.0/2.0)\'
    >>> rcode(sin(x), assign_to="s")
    \'s = sin(x);\'

    Simple custom printing can be defined for certain types by passing a
    dictionary of {"type" : "function"} to the ``user_functions`` kwarg.
    Alternatively, the dictionary value can be a list of tuples i.e.
    [(argument_test, cfunction_string)].

    >>> custom_functions = {
    ...   "ceiling": "CEIL",
    ...   "Abs": [(lambda x: not x.is_integer, "fabs"),
    ...           (lambda x: x.is_integer, "ABS")],
    ...   "func": "f"
    ... }
    >>> func = Function(\'func\')
    >>> rcode(func(Abs(x) + ceiling(x)), user_functions=custom_functions)
    \'f(fabs(x) + CEIL(x))\'

    or if the R-function takes a subset of the original arguments:

    >>> rcode(2**x + 3**x, user_functions={\'Pow\': [
    ...   (lambda b, e: b == 2, lambda b, e: \'exp2(%s)\' % e),
    ...   (lambda b, e: b != 2, \'pow\')]})
    \'exp2(x) + pow(3, x)\'

    ``Piecewise`` expressions are converted into conditionals. If an
    ``assign_to`` variable is provided an if statement is created, otherwise
    the ternary operator is used. Note that if the ``Piecewise`` lacks a
    default term, represented by ``(expr, True)`` then an error will be thrown.
    This is to prevent generating an expression that may not evaluate to
    anything.

    >>> from sympy import Piecewise
    >>> expr = Piecewise((x + 1, x > 0), (x, True))
    >>> print(rcode(expr, assign_to=tau))
    tau = ifelse(x > 0,x + 1,x);

    Support for loops is provided through ``Indexed`` types. With
    ``contract=True`` these expressions will be turned into loops, whereas
    ``contract=False`` will just print the assignment expression that should be
    looped over:

    >>> from sympy import Eq, IndexedBase, Idx
    >>> len_y = 5
    >>> y = IndexedBase(\'y\', shape=(len_y,))
    >>> t = IndexedBase(\'t\', shape=(len_y,))
    >>> Dy = IndexedBase(\'Dy\', shape=(len_y-1,))
    >>> i = Idx(\'i\', len_y-1)
    >>> e=Eq(Dy[i], (y[i+1]-y[i])/(t[i+1]-t[i]))
    >>> rcode(e.rhs, assign_to=e.lhs, contract=False)
    \'Dy[i] = (y[i + 1] - y[i])/(t[i + 1] - t[i]);\'

    Matrices are also supported, but a ``MatrixSymbol`` of the same dimensions
    must be provided to ``assign_to``. Note that any expression that can be
    generated normally can also exist inside a Matrix:

    >>> from sympy import Matrix, MatrixSymbol
    >>> mat = Matrix([x**2, Piecewise((x + 1, x > 0), (x, True)), sin(x)])
    >>> A = MatrixSymbol(\'A\', 3, 1)
    >>> print(rcode(mat, A))
    A[0] = x^2;
    A[1] = ifelse(x > 0,x + 1,x);
    A[2] = sin(x);

    '''
def print_rcode(expr, **settings) -> None:
    """Prints R representation of the given expression."""
