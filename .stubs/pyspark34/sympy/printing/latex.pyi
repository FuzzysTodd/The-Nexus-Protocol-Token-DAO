from _typeshed import Incomplete
from sympy.core import Add as Add, Expr as Expr, Float as Float, Mod as Mod, Mul as Mul, Number as Number, S as S, Symbol as Symbol
from sympy.core.alphabets import greeks as greeks
from sympy.core.containers import Tuple as Tuple
from sympy.core.function import AppliedUndef as AppliedUndef, Derivative as Derivative, Function as Function
from sympy.core.operations import AssocOp as AssocOp
from sympy.core.power import Pow as Pow
from sympy.core.sorting import default_sort_key as default_sort_key
from sympy.core.sympify import SympifyError as SympifyError
from sympy.logic.boolalg import BooleanFalse as BooleanFalse, BooleanTrue as BooleanTrue, true as true
from sympy.printing.conventions import requires_partial as requires_partial, split_super_sub as split_super_sub
from sympy.printing.precedence import PRECEDENCE as PRECEDENCE, precedence as precedence, precedence_traditional as precedence_traditional
from sympy.printing.printer import Printer as Printer, print_function as print_function
from sympy.tensor.array import NDimArray as NDimArray
from sympy.utilities.iterables import has_variety as has_variety, sift as sift
from sympy.vector.basisdependent import BasisDependent as BasisDependent
from typing import Callable

accepted_latex_functions: Incomplete
tex_greek_dictionary: Incomplete
other_symbols: Incomplete
modifier_dict: dict[str, Callable[[str], str]]
greek_letters_set: Incomplete

def latex_escape(s: str) -> str:
    """
    Escape a string such that latex interprets it as plaintext.

    We cannot use verbatim easily with mathjax, so escaping is easier.
    Rules from https://tex.stackexchange.com/a/34586/41112.
    """

class LatexPrinter(Printer):
    printmethod: str
    def __init__(self, settings: Incomplete | None = None) -> None: ...
    def parenthesize(self, item, level, is_neg: bool = False, strict: bool = False) -> str: ...
    def parenthesize_super(self, s):
        """
        Protect superscripts in s

        If the parenthesize_super option is set, protect with parentheses, else
        wrap in braces.
        """
    def doprint(self, expr) -> str: ...
    def emptyPrinter(self, expr): ...

def translate(s: str) -> str:
    '''
    Check for a modifier ending the string.  If present, convert the
    modifier to latex and translate the rest recursively.

    Given a description of a Greek letter or other special character,
    return the appropriate latex.

    Let everything else pass as given.

    >>> from sympy.printing.latex import translate
    >>> translate(\'alphahatdotprime\')
    "{\\\\dot{\\\\hat{\\\\alpha}}}\'"
    '''
def latex(expr, **settings):
    '''Convert the given expression to LaTeX string representation.

    Parameters
    ==========
    full_prec: boolean, optional
        If set to True, a floating point number is printed with full precision.
    fold_frac_powers : boolean, optional
        Emit ``^{p/q}`` instead of ``^{\\frac{p}{q}}`` for fractional powers.
    fold_func_brackets : boolean, optional
        Fold function brackets where applicable.
    fold_short_frac : boolean, optional
        Emit ``p / q`` instead of ``\\frac{p}{q}`` when the denominator is
        simple enough (at most two terms and no powers). The default value is
        ``True`` for inline mode, ``False`` otherwise.
    inv_trig_style : string, optional
        How inverse trig functions should be displayed. Can be one of
        ``\'abbreviated\'``, ``\'full\'``, or ``\'power\'``. Defaults to
        ``\'abbreviated\'``.
    itex : boolean, optional
        Specifies if itex-specific syntax is used, including emitting
        ``$$...$$``.
    ln_notation : boolean, optional
        If set to ``True``, ``\\ln`` is used instead of default ``\\log``.
    long_frac_ratio : float or None, optional
        The allowed ratio of the width of the numerator to the width of the
        denominator before the printer breaks off long fractions. If ``None``
        (the default value), long fractions are not broken up.
    mat_delim : string, optional
        The delimiter to wrap around matrices. Can be one of ``\'[\'``, ``\'(\'``,
        or the empty string ``\'\'``. Defaults to ``\'[\'``.
    mat_str : string, optional
        Which matrix environment string to emit. ``\'smallmatrix\'``,
        ``\'matrix\'``, ``\'array\'``, etc. Defaults to ``\'smallmatrix\'`` for
        inline mode, ``\'matrix\'`` for matrices of no more than 10 columns, and
        ``\'array\'`` otherwise.
    mode: string, optional
        Specifies how the generated code will be delimited. ``mode`` can be one
        of ``\'plain\'``, ``\'inline\'``, ``\'equation\'`` or ``\'equation*\'``.  If
        ``mode`` is set to ``\'plain\'``, then the resulting code will not be
        delimited at all (this is the default). If ``mode`` is set to
        ``\'inline\'`` then inline LaTeX ``$...$`` will be used. If ``mode`` is
        set to ``\'equation\'`` or ``\'equation*\'``, the resulting code will be
        enclosed in the ``equation`` or ``equation*`` environment (remember to
        import ``amsmath`` for ``equation*``), unless the ``itex`` option is
        set. In the latter case, the ``$$...$$`` syntax is used.
    mul_symbol : string or None, optional
        The symbol to use for multiplication. Can be one of ``None``,
        ``\'ldot\'``, ``\'dot\'``, or ``\'times\'``.
    order: string, optional
        Any of the supported monomial orderings (currently ``\'lex\'``,
        ``\'grlex\'``, or ``\'grevlex\'``), ``\'old\'``, and ``\'none\'``. This
        parameter does nothing for `~.Mul` objects. Setting order to ``\'old\'``
        uses the compatibility ordering for ``~.Add`` defined in Printer. For
        very large expressions, set the ``order`` keyword to ``\'none\'`` if
        speed is a concern.
    symbol_names : dictionary of strings mapped to symbols, optional
        Dictionary of symbols and the custom strings they should be emitted as.
    root_notation : boolean, optional
        If set to ``False``, exponents of the form 1/n are printed in fractonal
        form. Default is ``True``, to print exponent in root form.
    mat_symbol_style : string, optional
        Can be either ``\'plain\'`` (default) or ``\'bold\'``. If set to
        ``\'bold\'``, a `~.MatrixSymbol` A will be printed as ``\\mathbf{A}``,
        otherwise as ``A``.
    imaginary_unit : string, optional
        String to use for the imaginary unit. Defined options are ``\'i\'``
        (default) and ``\'j\'``. Adding ``r`` or ``t`` in front gives ``\\mathrm``
        or ``\\text``, so ``\'ri\'`` leads to ``\\mathrm{i}`` which gives
        `\\mathrm{i}`.
    gothic_re_im : boolean, optional
        If set to ``True``, `\\Re` and `\\Im` is used for ``re`` and ``im``, respectively.
        The default is ``False`` leading to `\\operatorname{re}` and `\\operatorname{im}`.
    decimal_separator : string, optional
        Specifies what separator to use to separate the whole and fractional parts of a
        floating point number as in `2.5` for the default, ``period`` or `2{,}5`
        when ``comma`` is specified. Lists, sets, and tuple are printed with semicolon
        separating the elements when ``comma`` is chosen. For example, [1; 2; 3] when
        ``comma`` is chosen and [1,2,3] for when ``period`` is chosen.
    parenthesize_super : boolean, optional
        If set to ``False``, superscripted expressions will not be parenthesized when
        powered. Default is ``True``, which parenthesizes the expression when powered.
    min: Integer or None, optional
        Sets the lower bound for the exponent to print floating point numbers in
        fixed-point format.
    max: Integer or None, optional
        Sets the upper bound for the exponent to print floating point numbers in
        fixed-point format.
    diff_operator: string, optional
        String to use for differential operator. Default is ``\'d\'``, to print in italic
        form. ``\'rd\'``, ``\'td\'`` are shortcuts for ``\\mathrm{d}`` and ``\\text{d}``.

    Notes
    =====

    Not using a print statement for printing, results in double backslashes for
    latex commands since that\'s the way Python escapes backslashes in strings.

    >>> from sympy import latex, Rational
    >>> from sympy.abc import tau
    >>> latex((2*tau)**Rational(7,2))
    \'8 \\\\sqrt{2} \\\\tau^{\\\\frac{7}{2}}\'
    >>> print(latex((2*tau)**Rational(7,2)))
    8 \\sqrt{2} \\tau^{\\frac{7}{2}}

    Examples
    ========

    >>> from sympy import latex, pi, sin, asin, Integral, Matrix, Rational, log
    >>> from sympy.abc import x, y, mu, r, tau

    Basic usage:

    >>> print(latex((2*tau)**Rational(7,2)))
    8 \\sqrt{2} \\tau^{\\frac{7}{2}}

    ``mode`` and ``itex`` options:

    >>> print(latex((2*mu)**Rational(7,2), mode=\'plain\'))
    8 \\sqrt{2} \\mu^{\\frac{7}{2}}
    >>> print(latex((2*tau)**Rational(7,2), mode=\'inline\'))
    $8 \\sqrt{2} \\tau^{7 / 2}$
    >>> print(latex((2*mu)**Rational(7,2), mode=\'equation*\'))
    \\begin{equation*}8 \\sqrt{2} \\mu^{\\frac{7}{2}}\\end{equation*}
    >>> print(latex((2*mu)**Rational(7,2), mode=\'equation\'))
    \\begin{equation}8 \\sqrt{2} \\mu^{\\frac{7}{2}}\\end{equation}
    >>> print(latex((2*mu)**Rational(7,2), mode=\'equation\', itex=True))
    $$8 \\sqrt{2} \\mu^{\\frac{7}{2}}$$
    >>> print(latex((2*mu)**Rational(7,2), mode=\'plain\'))
    8 \\sqrt{2} \\mu^{\\frac{7}{2}}
    >>> print(latex((2*tau)**Rational(7,2), mode=\'inline\'))
    $8 \\sqrt{2} \\tau^{7 / 2}$
    >>> print(latex((2*mu)**Rational(7,2), mode=\'equation*\'))
    \\begin{equation*}8 \\sqrt{2} \\mu^{\\frac{7}{2}}\\end{equation*}
    >>> print(latex((2*mu)**Rational(7,2), mode=\'equation\'))
    \\begin{equation}8 \\sqrt{2} \\mu^{\\frac{7}{2}}\\end{equation}
    >>> print(latex((2*mu)**Rational(7,2), mode=\'equation\', itex=True))
    $$8 \\sqrt{2} \\mu^{\\frac{7}{2}}$$

    Fraction options:

    >>> print(latex((2*tau)**Rational(7,2), fold_frac_powers=True))
    8 \\sqrt{2} \\tau^{7/2}
    >>> print(latex((2*tau)**sin(Rational(7,2))))
    \\left(2 \\tau\\right)^{\\sin{\\left(\\frac{7}{2} \\right)}}
    >>> print(latex((2*tau)**sin(Rational(7,2)), fold_func_brackets=True))
    \\left(2 \\tau\\right)^{\\sin {\\frac{7}{2}}}
    >>> print(latex(3*x**2/y))
    \\frac{3 x^{2}}{y}
    >>> print(latex(3*x**2/y, fold_short_frac=True))
    3 x^{2} / y
    >>> print(latex(Integral(r, r)/2/pi, long_frac_ratio=2))
    \\frac{\\int r\\, dr}{2 \\pi}
    >>> print(latex(Integral(r, r)/2/pi, long_frac_ratio=0))
    \\frac{1}{2 \\pi} \\int r\\, dr

    Multiplication options:

    >>> print(latex((2*tau)**sin(Rational(7,2)), mul_symbol="times"))
    \\left(2 \\times \\tau\\right)^{\\sin{\\left(\\frac{7}{2} \\right)}}

    Trig options:

    >>> print(latex(asin(Rational(7,2))))
    \\operatorname{asin}{\\left(\\frac{7}{2} \\right)}
    >>> print(latex(asin(Rational(7,2)), inv_trig_style="full"))
    \\arcsin{\\left(\\frac{7}{2} \\right)}
    >>> print(latex(asin(Rational(7,2)), inv_trig_style="power"))
    \\sin^{-1}{\\left(\\frac{7}{2} \\right)}

    Matrix options:

    >>> print(latex(Matrix(2, 1, [x, y])))
    \\left[\\begin{matrix}x\\\\y\\end{matrix}\\right]
    >>> print(latex(Matrix(2, 1, [x, y]), mat_str = "array"))
    \\left[\\begin{array}{c}x\\\\y\\end{array}\\right]
    >>> print(latex(Matrix(2, 1, [x, y]), mat_delim="("))
    \\left(\\begin{matrix}x\\\\y\\end{matrix}\\right)

    Custom printing of symbols:

    >>> print(latex(x**2, symbol_names={x: \'x_i\'}))
    x_i^{2}

    Logarithms:

    >>> print(latex(log(10)))
    \\log{\\left(10 \\right)}
    >>> print(latex(log(10), ln_notation=True))
    \\ln{\\left(10 \\right)}

    ``latex()`` also supports the builtin container types :class:`list`,
    :class:`tuple`, and :class:`dict`:

    >>> print(latex([2/x, y], mode=\'inline\'))
    $\\left[ 2 / x, \\  y\\right]$

    Unsupported types are rendered as monospaced plaintext:

    >>> print(latex(int))
    \\mathtt{\\text{<class \'int\'>}}
    >>> print(latex("plain % text"))
    \\mathtt{\\text{plain \\% text}}

    See :ref:`printer_method_example` for an example of how to override
    this behavior for your own types by implementing ``_latex``.

    .. versionchanged:: 1.7.0
        Unsupported types no longer have their ``str`` representation treated as valid latex.

    '''
def print_latex(expr, **settings) -> None:
    """Prints LaTeX representation of the given expression. Takes the same
    settings as ``latex()``."""
def multiline_latex(lhs, rhs, terms_per_line: int = 1, environment: str = 'align*', use_dots: bool = False, **settings):
    '''
    This function generates a LaTeX equation with a multiline right-hand side
    in an ``align*``, ``eqnarray`` or ``IEEEeqnarray`` environment.

    Parameters
    ==========

    lhs : Expr
        Left-hand side of equation

    rhs : Expr
        Right-hand side of equation

    terms_per_line : integer, optional
        Number of terms per line to print. Default is 1.

    environment : "string", optional
        Which LaTeX wnvironment to use for the output. Options are "align*"
        (default), "eqnarray", and "IEEEeqnarray".

    use_dots : boolean, optional
        If ``True``, ``\\\\dots`` is added to the end of each line. Default is ``False``.

    Examples
    ========

    >>> from sympy import multiline_latex, symbols, sin, cos, exp, log, I
    >>> x, y, alpha = symbols(\'x y alpha\')
    >>> expr = sin(alpha*y) + exp(I*alpha) - cos(log(y))
    >>> print(multiline_latex(x, expr))
    \\begin{align*}
    x = & e^{i \\alpha} \\\\\n    & + \\sin{\\left(\\alpha y \\right)} \\\\\n    & - \\cos{\\left(\\log{\\left(y \\right)} \\right)}
    \\end{align*}

    Using at most two terms per line:
    >>> print(multiline_latex(x, expr, 2))
    \\begin{align*}
    x = & e^{i \\alpha} + \\sin{\\left(\\alpha y \\right)} \\\\\n    & - \\cos{\\left(\\log{\\left(y \\right)} \\right)}
    \\end{align*}

    Using ``eqnarray`` and dots:
    >>> print(multiline_latex(x, expr, terms_per_line=2, environment="eqnarray", use_dots=True))
    \\begin{eqnarray}
    x & = & e^{i \\alpha} + \\sin{\\left(\\alpha y \\right)} \\dots\\nonumber\\\\\n    & & - \\cos{\\left(\\log{\\left(y \\right)} \\right)}
    \\end{eqnarray}

    Using ``IEEEeqnarray``:
    >>> print(multiline_latex(x, expr, environment="IEEEeqnarray"))
    \\begin{IEEEeqnarray}{rCl}
    x & = & e^{i \\alpha} \\nonumber\\\\\n    & & + \\sin{\\left(\\alpha y \\right)} \\nonumber\\\\\n    & & - \\cos{\\left(\\log{\\left(y \\right)} \\right)}
    \\end{IEEEeqnarray}

    Notes
    =====

    All optional parameters from ``latex`` can also be used.

    '''
