from .add import Add as Add
from .basic import Basic as Basic
from .cache import cacheit as cacheit
from .containers import Dict as Dict, Tuple as Tuple
from .evalf import pure_complex as pure_complex
from .expr import AtomicExpr as AtomicExpr, Expr as Expr
from .logic import FuzzyBool as FuzzyBool, fuzzy_and as fuzzy_and, fuzzy_not as fuzzy_not, fuzzy_or as fuzzy_or
from .mul import Mul as Mul
from .numbers import Float as Float, Integer as Integer, Rational as Rational
from .operations import LatticeOp as LatticeOp
from .parameters import global_parameters as global_parameters
from .rules import Transform as Transform
from .singleton import S as S
from .sorting import default_sort_key as default_sort_key, ordered as ordered
from .symbol import Dummy as Dummy, Symbol as Symbol
from .sympify import sympify as sympify
from _typeshed import Incomplete
from sympy.utilities.exceptions import SymPyDeprecationWarning as SymPyDeprecationWarning, ignore_warnings as ignore_warnings, sympy_deprecation_warning as sympy_deprecation_warning
from sympy.utilities.iterables import has_dups as has_dups, is_sequence as is_sequence, iterable as iterable, sift as sift, topological_sort as topological_sort, uniq as uniq
from sympy.utilities.lambdify import MPMATH_TRANSLATIONS as MPMATH_TRANSLATIONS
from sympy.utilities.misc import as_int as as_int, filldedent as filldedent, func_name as func_name
from typing import Any

class PoleError(Exception): ...
class ArgumentIndexError(ValueError): ...
class BadSignatureError(TypeError):
    """Raised when a Lambda is created with an invalid signature"""
class BadArgumentsError(TypeError):
    """Raised when a Lambda is called with an incorrect number of arguments"""

def arity(cls):
    """Return the arity of the function if it is known, else None.

    Explanation
    ===========

    When default values are specified for some arguments, they are
    optional and the arity is reported as a tuple of possible values.

    Examples
    ========

    >>> from sympy import arity, log
    >>> arity(lambda x: x)
    1
    >>> arity(log)
    (1, 2)
    >>> arity(lambda *x: sum(x)) is None
    True
    """

class FunctionClass(type):
    """
    Base class for function classes. FunctionClass is a subclass of type.

    Use Function('<function name>' [ , signature ]) to create
    undefined function classes.
    """
    def __init__(cls, *args, **kwargs) -> None: ...
    @property
    def __signature__(self):
        """
        Allow Python 3's inspect.signature to give a useful signature for
        Function subclasses.
        """
    @property
    def free_symbols(self): ...
    @property
    def xreplace(self): ...
    @property
    def nargs(self):
        """Return a set of the allowed number of arguments for the function.

        Examples
        ========

        >>> from sympy import Function
        >>> f = Function('f')

        If the function can take any number of arguments, the set of whole
        numbers is returned:

        >>> Function('f').nargs
        Naturals0

        If the function was initialized to accept one or more arguments, a
        corresponding set will be returned:

        >>> Function('f', nargs=1).nargs
        {1}
        >>> Function('f', nargs=(2, 1)).nargs
        {1, 2}

        The undefined function, after application, also has the nargs
        attribute; the actual number of arguments is always available by
        checking the ``args`` attribute:

        >>> f = Function('f')
        >>> f(1).nargs
        Naturals0
        >>> len(f(1).args)
        1
        """

class Application(Basic, metaclass=FunctionClass):
    """
    Base class for applied functions.

    Explanation
    ===========

    Instances of Application represent the result of applying an application of
    any type to any object.
    """
    is_Function: bool
    def __new__(cls, *args, **options): ...
    @classmethod
    def eval(cls, *args) -> None:
        '''
        Returns a canonical form of cls applied to arguments args.

        Explanation
        ===========

        The ``eval()`` method is called when the class ``cls`` is about to be
        instantiated and it should return either some simplified instance
        (possible of some other class), or if the class ``cls`` should be
        unmodified, return None.

        Examples of ``eval()`` for the function "sign"

        .. code-block:: python

            @classmethod
            def eval(cls, arg):
                if arg is S.NaN:
                    return S.NaN
                if arg.is_zero: return S.Zero
                if arg.is_positive: return S.One
                if arg.is_negative: return S.NegativeOne
                if isinstance(arg, Mul):
                    coeff, terms = arg.as_coeff_Mul(rational=True)
                    if coeff is not S.One:
                        return cls(coeff) * cls(terms)

        '''
    @property
    def func(self): ...

class Function(Application, Expr):
    """
    Base class for applied mathematical functions.

    It also serves as a constructor for undefined function classes.

    See the :ref:`custom-functions` guide for details on how to subclass
    ``Function`` and what methods can be defined.

    Examples
    ========

    **Undefined Functions**

    To create an undefined function, pass a string of the function name to
    ``Function``.

    >>> from sympy import Function, Symbol
    >>> x = Symbol('x')
    >>> f = Function('f')
    >>> g = Function('g')(x)
    >>> f
    f
    >>> f(x)
    f(x)
    >>> g
    g(x)
    >>> f(x).diff(x)
    Derivative(f(x), x)
    >>> g.diff(x)
    Derivative(g(x), x)

    Assumptions can be passed to ``Function`` the same as with a
    :class:`~.Symbol`. Alternatively, you can use a ``Symbol`` with
    assumptions for the function name and the function will inherit the name
    and assumptions associated with the ``Symbol``:

    >>> f_real = Function('f', real=True)
    >>> f_real(x).is_real
    True
    >>> f_real_inherit = Function(Symbol('f', real=True))
    >>> f_real_inherit(x).is_real
    True

    Note that assumptions on a function are unrelated to the assumptions on
    the variables it is called on. If you want to add a relationship, subclass
    ``Function`` and define custom assumptions handler methods. See the
    :ref:`custom-functions-assumptions` section of the :ref:`custom-functions`
    guide for more details.

    **Custom Function Subclasses**

    The :ref:`custom-functions` guide has several
    :ref:`custom-functions-complete-examples` of how to subclass ``Function``
    to create a custom function.

    """
    def __new__(cls, *args, **options): ...
    @classmethod
    def class_key(cls): ...
    @classmethod
    def is_singular(cls, a):
        """
        Tests whether the argument is an essential singularity
        or a branch point, or the functions is non-holomorphic.
        """
    def as_base_exp(self):
        """
        Returns the method as the 2-tuple (base, exponent).
        """
    def fdiff(self, argindex: int = 1):
        """
        Returns the first derivative of the function.
        """

class AppliedUndef(Function):
    """
    Base class for expressions resulting from the application of an undefined
    function.
    """
    is_number: bool
    def __new__(cls, *args, **options): ...

class UndefSageHelper:
    """
    Helper to facilitate Sage conversion.
    """
    def __get__(self, ins, typ): ...

class UndefinedFunction(FunctionClass):
    """
    The (meta)class of undefined functions.
    """
    def __new__(mcl, name, bases=..., __dict__: Incomplete | None = None, **kwargs): ...
    def __instancecheck__(cls, instance): ...
    def __hash__(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

class WildFunction(Function, AtomicExpr):
    """
    A WildFunction function matches any function (with its arguments).

    Examples
    ========

    >>> from sympy import WildFunction, Function, cos
    >>> from sympy.abc import x, y
    >>> F = WildFunction('F')
    >>> f = Function('f')
    >>> F.nargs
    Naturals0
    >>> x.match(F)
    >>> F.match(F)
    {F_: F_}
    >>> f(x).match(F)
    {F_: f(x)}
    >>> cos(x).match(F)
    {F_: cos(x)}
    >>> f(x, y).match(F)
    {F_: f(x, y)}

    To match functions with a given number of arguments, set ``nargs`` to the
    desired value at instantiation:

    >>> F = WildFunction('F', nargs=2)
    >>> F.nargs
    {2}
    >>> f(x).match(F)
    >>> f(x, y).match(F)
    {F_: f(x, y)}

    To match functions with a range of arguments, set ``nargs`` to a tuple
    containing the desired number of arguments, e.g. if ``nargs = (1, 2)``
    then functions with 1 or 2 arguments will be matched.

    >>> F = WildFunction('F', nargs=(1, 2))
    >>> F.nargs
    {1, 2}
    >>> f(x).match(F)
    {F_: f(x)}
    >>> f(x, y).match(F)
    {F_: f(x, y)}
    >>> f(x, y, 1).match(F)

    """
    include: set[Any]
    def __init__(cls, name, **assumptions) -> None: ...
    def matches(self, expr, repl_dict: Incomplete | None = None, old: bool = False): ...

class Derivative(Expr):
    """
    Carries out differentiation of the given expression with respect to symbols.

    Examples
    ========

    >>> from sympy import Derivative, Function, symbols, Subs
    >>> from sympy.abc import x, y
    >>> f, g = symbols('f g', cls=Function)

    >>> Derivative(x**2, x, evaluate=True)
    2*x

    Denesting of derivatives retains the ordering of variables:

        >>> Derivative(Derivative(f(x, y), y), x)
        Derivative(f(x, y), y, x)

    Contiguously identical symbols are merged into a tuple giving
    the symbol and the count:

        >>> Derivative(f(x), x, x, y, x)
        Derivative(f(x), (x, 2), y, x)

    If the derivative cannot be performed, and evaluate is True, the
    order of the variables of differentiation will be made canonical:

        >>> Derivative(f(x, y), y, x, evaluate=True)
        Derivative(f(x, y), x, y)

    Derivatives with respect to undefined functions can be calculated:

        >>> Derivative(f(x)**2, f(x), evaluate=True)
        2*f(x)

    Such derivatives will show up when the chain rule is used to
    evalulate a derivative:

        >>> f(g(x)).diff(x)
        Derivative(f(g(x)), g(x))*Derivative(g(x), x)

    Substitution is used to represent derivatives of functions with
    arguments that are not symbols or functions:

        >>> f(2*x + 3).diff(x) == 2*Subs(f(y).diff(y), y, 2*x + 3)
        True

    Notes
    =====

    Simplification of high-order derivatives:

    Because there can be a significant amount of simplification that can be
    done when multiple differentiations are performed, results will be
    automatically simplified in a fairly conservative fashion unless the
    keyword ``simplify`` is set to False.

        >>> from sympy import sqrt, diff, Function, symbols
        >>> from sympy.abc import x, y, z
        >>> f, g = symbols('f,g', cls=Function)

        >>> e = sqrt((x + 1)**2 + x)
        >>> diff(e, (x, 5), simplify=False).count_ops()
        136
        >>> diff(e, (x, 5)).count_ops()
        30

    Ordering of variables:

    If evaluate is set to True and the expression cannot be evaluated, the
    list of differentiation symbols will be sorted, that is, the expression is
    assumed to have continuous derivatives up to the order asked.

    Derivative wrt non-Symbols:

    For the most part, one may not differentiate wrt non-symbols.
    For example, we do not allow differentiation wrt `x*y` because
    there are multiple ways of structurally defining where x*y appears
    in an expression: a very strict definition would make
    (x*y*z).diff(x*y) == 0. Derivatives wrt defined functions (like
    cos(x)) are not allowed, either:

        >>> (x*y*z).diff(x*y)
        Traceback (most recent call last):
        ...
        ValueError: Can't calculate derivative wrt x*y.

    To make it easier to work with variational calculus, however,
    derivatives wrt AppliedUndef and Derivatives are allowed.
    For example, in the Euler-Lagrange method one may write
    F(t, u, v) where u = f(t) and v = f'(t). These variables can be
    written explicitly as functions of time::

        >>> from sympy.abc import t
        >>> F = Function('F')
        >>> U = f(t)
        >>> V = U.diff(t)

    The derivative wrt f(t) can be obtained directly:

        >>> direct = F(t, U, V).diff(U)

    When differentiation wrt a non-Symbol is attempted, the non-Symbol
    is temporarily converted to a Symbol while the differentiation
    is performed and the same answer is obtained:

        >>> indirect = F(t, U, V).subs(U, x).diff(x).subs(x, U)
        >>> assert direct == indirect

    The implication of this non-symbol replacement is that all
    functions are treated as independent of other functions and the
    symbols are independent of the functions that contain them::

        >>> x.diff(f(x))
        0
        >>> g(x).diff(f(x))
        0

    It also means that derivatives are assumed to depend only
    on the variables of differentiation, not on anything contained
    within the expression being differentiated::

        >>> F = f(x)
        >>> Fx = F.diff(x)
        >>> Fx.diff(F)  # derivative depends on x, not F
        0
        >>> Fxx = Fx.diff(x)
        >>> Fxx.diff(Fx)  # derivative depends on x, not Fx
        0

    The last example can be made explicit by showing the replacement
    of Fx in Fxx with y:

        >>> Fxx.subs(Fx, y)
        Derivative(y, x)

        Since that in itself will evaluate to zero, differentiating
        wrt Fx will also be zero:

        >>> _.doit()
        0

    Replacing undefined functions with concrete expressions

    One must be careful to replace undefined functions with expressions
    that contain variables consistent with the function definition and
    the variables of differentiation or else insconsistent result will
    be obtained. Consider the following example:

    >>> eq = f(x)*g(y)
    >>> eq.subs(f(x), x*y).diff(x, y).doit()
    y*Derivative(g(y), y) + g(y)
    >>> eq.diff(x, y).subs(f(x), x*y).doit()
    y*Derivative(g(y), y)

    The results differ because `f(x)` was replaced with an expression
    that involved both variables of differentiation. In the abstract
    case, differentiation of `f(x)` by `y` is 0; in the concrete case,
    the presence of `y` made that derivative nonvanishing and produced
    the extra `g(y)` term.

    Defining differentiation for an object

    An object must define ._eval_derivative(symbol) method that returns
    the differentiation result. This function only needs to consider the
    non-trivial case where expr contains symbol and it should call the diff()
    method internally (not _eval_derivative); Derivative should be the only
    one to call _eval_derivative.

    Any class can allow derivatives to be taken with respect to
    itself (while indicating its scalar nature). See the
    docstring of Expr._diff_wrt.

    See Also
    ========
    _sort_variable_count
    """
    is_Derivative: bool
    def __new__(cls, expr, *variables, **kwargs): ...
    @property
    def canonical(cls): ...
    def doit(self, **hints): ...
    def doit_numerically(self, z0):
        """
        Evaluate the derivative at z numerically.

        When we can represent derivatives at a point, this should be folded
        into the normal evalf. For now, we need a special method.
        """
    @property
    def expr(self): ...
    @property
    def variables(self): ...
    @property
    def variable_count(self): ...
    @property
    def derivative_count(self): ...
    @property
    def free_symbols(self): ...
    @property
    def kind(self): ...
    def as_finite_difference(self, points: int = 1, x0: Incomplete | None = None, wrt: Incomplete | None = None):
        ''' Expresses a Derivative instance as a finite difference.

        Parameters
        ==========

        points : sequence or coefficient, optional
            If sequence: discrete values (length >= order+1) of the
            independent variable used for generating the finite
            difference weights.
            If it is a coefficient, it will be used as the step-size
            for generating an equidistant sequence of length order+1
            centered around ``x0``. Default: 1 (step-size 1)

        x0 : number or Symbol, optional
            the value of the independent variable (``wrt``) at which the
            derivative is to be approximated. Default: same as ``wrt``.

        wrt : Symbol, optional
            "with respect to" the variable for which the (partial)
            derivative is to be approximated for. If not provided it
            is required that the derivative is ordinary. Default: ``None``.


        Examples
        ========

        >>> from sympy import symbols, Function, exp, sqrt, Symbol
        >>> x, h = symbols(\'x h\')
        >>> f = Function(\'f\')
        >>> f(x).diff(x).as_finite_difference()
        -f(x - 1/2) + f(x + 1/2)

        The default step size and number of points are 1 and
        ``order + 1`` respectively. We can change the step size by
        passing a symbol as a parameter:

        >>> f(x).diff(x).as_finite_difference(h)
        -f(-h/2 + x)/h + f(h/2 + x)/h

        We can also specify the discretized values to be used in a
        sequence:

        >>> f(x).diff(x).as_finite_difference([x, x+h, x+2*h])
        -3*f(x)/(2*h) + 2*f(h + x)/h - f(2*h + x)/(2*h)

        The algorithm is not restricted to use equidistant spacing, nor
        do we need to make the approximation around ``x0``, but we can get
        an expression estimating the derivative at an offset:

        >>> e, sq2 = exp(1), sqrt(2)
        >>> xl = [x-h, x+h, x+e*h]
        >>> f(x).diff(x, 1).as_finite_difference(xl, x+h*sq2)  # doctest: +ELLIPSIS
        2*h*((h + sqrt(2)*h)/(2*h) - (-sqrt(2)*h + h)/(2*h))*f(E*h + x)/...

        To approximate ``Derivative`` around ``x0`` using a non-equidistant
        spacing step, the algorithm supports assignment of undefined
        functions to ``points``:

        >>> dx = Function(\'dx\')
        >>> f(x).diff(x).as_finite_difference(points=dx(x), x0=x-h)
        -f(-h + x - dx(-h + x)/2)/dx(-h + x) + f(-h + x + dx(-h + x)/2)/dx(-h + x)

        Partial derivatives are also supported:

        >>> y = Symbol(\'y\')
        >>> d2fdxdy=f(x,y).diff(x,y)
        >>> d2fdxdy.as_finite_difference(wrt=x)
        -Derivative(f(x - 1/2, y), y) + Derivative(f(x + 1/2, y), y)

        We can apply ``as_finite_difference`` to ``Derivative`` instances in
        compound expressions using ``replace``:

        >>> (1 + 42**f(x).diff(x)).replace(lambda arg: arg.is_Derivative,
        ...     lambda arg: arg.as_finite_difference())
        42**(-f(x - 1/2) + f(x + 1/2)) + 1


        See also
        ========

        sympy.calculus.finite_diff.apply_finite_diff
        sympy.calculus.finite_diff.differentiate_finite
        sympy.calculus.finite_diff.finite_diff_weights

        '''

class Lambda(Expr):
    """
    Lambda(x, expr) represents a lambda function similar to Python's
    'lambda x: expr'. A function of several variables is written as
    Lambda((x, y, ...), expr).

    Examples
    ========

    A simple example:

    >>> from sympy import Lambda
    >>> from sympy.abc import x
    >>> f = Lambda(x, x**2)
    >>> f(4)
    16

    For multivariate functions, use:

    >>> from sympy.abc import y, z, t
    >>> f2 = Lambda((x, y, z, t), x + y**z + t**z)
    >>> f2(1, 2, 3, 4)
    73

    It is also possible to unpack tuple arguments:

    >>> f = Lambda(((x, y), z), x + y + z)
    >>> f((1, 2), 3)
    6

    A handy shortcut for lots of arguments:

    >>> p = x, y, z
    >>> f = Lambda(p, x + y*z)
    >>> f(*p)
    x + y*z

    """
    is_Function: bool
    def __new__(cls, signature, expr): ...
    @property
    def signature(self):
        """The expected form of the arguments to be unpacked into variables"""
    @property
    def expr(self):
        """The return value of the function"""
    @property
    def variables(self):
        """The variables used in the internal representation of the function"""
    @property
    def nargs(self): ...
    bound_symbols = variables
    @property
    def free_symbols(self): ...
    def __call__(self, *args): ...
    @property
    def is_identity(self):
        """Return ``True`` if this ``Lambda`` is an identity function. """

class Subs(Expr):
    """
    Represents unevaluated substitutions of an expression.

    ``Subs(expr, x, x0)`` represents the expression resulting
    from substituting x with x0 in expr.

    Parameters
    ==========

    expr : Expr
        An expression.

    x : tuple, variable
        A variable or list of distinct variables.

    x0 : tuple or list of tuples
        A point or list of evaluation points
        corresponding to those variables.

    Examples
    ========

    >>> from sympy import Subs, Function, sin, cos
    >>> from sympy.abc import x, y, z
    >>> f = Function('f')

    Subs are created when a particular substitution cannot be made. The
    x in the derivative cannot be replaced with 0 because 0 is not a
    valid variables of differentiation:

    >>> f(x).diff(x).subs(x, 0)
    Subs(Derivative(f(x), x), x, 0)

    Once f is known, the derivative and evaluation at 0 can be done:

    >>> _.subs(f, sin).doit() == sin(x).diff(x).subs(x, 0) == cos(0)
    True

    Subs can also be created directly with one or more variables:

    >>> Subs(f(x)*sin(y) + z, (x, y), (0, 1))
    Subs(z + f(x)*sin(y), (x, y), (0, 1))
    >>> _.doit()
    z + f(0)*sin(1)

    Notes
    =====

    ``Subs`` objects are generally useful to represent unevaluated derivatives
    calculated at a point.

    The variables may be expressions, but they are subjected to the limitations
    of subs(), so it is usually a good practice to use only symbols for
    variables, since in that case there can be no ambiguity.

    There's no automatic expansion - use the method .doit() to effect all
    possible substitutions of the object and also of objects inside the
    expression.

    When evaluating derivatives at a point that is not a symbol, a Subs object
    is returned. One is also able to calculate derivatives of Subs objects - in
    this case the expression is always expanded (for the unevaluated form, use
    Derivative()).

    In order to allow expressions to combine before doit is done, a
    representation of the Subs expression is used internally to make
    expressions that are superficially different compare the same:

    >>> a, b = Subs(x, x, 0), Subs(y, y, 0)
    >>> a + b
    2*Subs(x, x, 0)

    This can lead to unexpected consequences when using methods
    like `has` that are cached:

    >>> s = Subs(x, x, 0)
    >>> s.has(x), s.has(y)
    (True, False)
    >>> ss = s.subs(x, y)
    >>> ss.has(x), ss.has(y)
    (True, False)
    >>> s, ss
    (Subs(x, x, 0), Subs(y, y, 0))
    """
    def __new__(cls, expr, variables, point, **assumptions): ...
    def doit(self, **hints): ...
    def evalf(self, prec: Incomplete | None = None, **options): ...
    n = evalf
    @property
    def variables(self):
        """The variables to be evaluated"""
    bound_symbols = variables
    @property
    def expr(self):
        """The expression on which the substitution operates"""
    @property
    def point(self):
        """The values for which the variables are to be substituted"""
    @property
    def free_symbols(self): ...
    @property
    def expr_free_symbols(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __hash__(self): ...

def diff(f, *symbols, **kwargs):
    """
    Differentiate f with respect to symbols.

    Explanation
    ===========

    This is just a wrapper to unify .diff() and the Derivative class; its
    interface is similar to that of integrate().  You can use the same
    shortcuts for multiple variables as with Derivative.  For example,
    diff(f(x), x, x, x) and diff(f(x), x, 3) both return the third derivative
    of f(x).

    You can pass evaluate=False to get an unevaluated Derivative class.  Note
    that if there are 0 symbols (such as diff(f(x), x, 0), then the result will
    be the function (the zeroth derivative), even if evaluate=False.

    Examples
    ========

    >>> from sympy import sin, cos, Function, diff
    >>> from sympy.abc import x, y
    >>> f = Function('f')

    >>> diff(sin(x), x)
    cos(x)
    >>> diff(f(x), x, x, x)
    Derivative(f(x), (x, 3))
    >>> diff(f(x), x, 3)
    Derivative(f(x), (x, 3))
    >>> diff(sin(x)*cos(y), x, 2, y, 2)
    sin(x)*cos(y)

    >>> type(diff(sin(x), x))
    cos
    >>> type(diff(sin(x), x, evaluate=False))
    <class 'sympy.core.function.Derivative'>
    >>> type(diff(sin(x), x, 0))
    sin
    >>> type(diff(sin(x), x, 0, evaluate=False))
    sin

    >>> diff(sin(x))
    cos(x)
    >>> diff(sin(x*y))
    Traceback (most recent call last):
    ...
    ValueError: specify differentiation variables to differentiate sin(x*y)

    Note that ``diff(sin(x))`` syntax is meant only for convenience
    in interactive sessions and should be avoided in library code.

    References
    ==========

    .. [1] https://reference.wolfram.com/legacy/v5_2/Built-inFunctions/AlgebraicComputation/Calculus/D.html

    See Also
    ========

    Derivative
    idiff: computes the derivative implicitly

    """
def expand(e, deep: bool = True, modulus: Incomplete | None = None, power_base: bool = True, power_exp: bool = True, mul: bool = True, log: bool = True, multinomial: bool = True, basic: bool = True, **hints):
    """
    Expand an expression using methods given as hints.

    Explanation
    ===========

    Hints evaluated unless explicitly set to False are:  ``basic``, ``log``,
    ``multinomial``, ``mul``, ``power_base``, and ``power_exp`` The following
    hints are supported but not applied unless set to True:  ``complex``,
    ``func``, and ``trig``.  In addition, the following meta-hints are
    supported by some or all of the other hints:  ``frac``, ``numer``,
    ``denom``, ``modulus``, and ``force``.  ``deep`` is supported by all
    hints.  Additionally, subclasses of Expr may define their own hints or
    meta-hints.

    The ``basic`` hint is used for any special rewriting of an object that
    should be done automatically (along with the other hints like ``mul``)
    when expand is called. This is a catch-all hint to handle any sort of
    expansion that may not be described by the existing hint names. To use
    this hint an object should override the ``_eval_expand_basic`` method.
    Objects may also define their own expand methods, which are not run by
    default.  See the API section below.

    If ``deep`` is set to ``True`` (the default), things like arguments of
    functions are recursively expanded.  Use ``deep=False`` to only expand on
    the top level.

    If the ``force`` hint is used, assumptions about variables will be ignored
    in making the expansion.

    Hints
    =====

    These hints are run by default

    mul
    ---

    Distributes multiplication over addition:

    >>> from sympy import cos, exp, sin
    >>> from sympy.abc import x, y, z
    >>> (y*(x + z)).expand(mul=True)
    x*y + y*z

    multinomial
    -----------

    Expand (x + y + ...)**n where n is a positive integer.

    >>> ((x + y + z)**2).expand(multinomial=True)
    x**2 + 2*x*y + 2*x*z + y**2 + 2*y*z + z**2

    power_exp
    ---------

    Expand addition in exponents into multiplied bases.

    >>> exp(x + y).expand(power_exp=True)
    exp(x)*exp(y)
    >>> (2**(x + y)).expand(power_exp=True)
    2**x*2**y

    power_base
    ----------

    Split powers of multiplied bases.

    This only happens by default if assumptions allow, or if the
    ``force`` meta-hint is used:

    >>> ((x*y)**z).expand(power_base=True)
    (x*y)**z
    >>> ((x*y)**z).expand(power_base=True, force=True)
    x**z*y**z
    >>> ((2*y)**z).expand(power_base=True)
    2**z*y**z

    Note that in some cases where this expansion always holds, SymPy performs
    it automatically:

    >>> (x*y)**2
    x**2*y**2

    log
    ---

    Pull out power of an argument as a coefficient and split logs products
    into sums of logs.

    Note that these only work if the arguments of the log function have the
    proper assumptions--the arguments must be positive and the exponents must
    be real--or else the ``force`` hint must be True:

    >>> from sympy import log, symbols
    >>> log(x**2*y).expand(log=True)
    log(x**2*y)
    >>> log(x**2*y).expand(log=True, force=True)
    2*log(x) + log(y)
    >>> x, y = symbols('x,y', positive=True)
    >>> log(x**2*y).expand(log=True)
    2*log(x) + log(y)

    basic
    -----

    This hint is intended primarily as a way for custom subclasses to enable
    expansion by default.

    These hints are not run by default:

    complex
    -------

    Split an expression into real and imaginary parts.

    >>> x, y = symbols('x,y')
    >>> (x + y).expand(complex=True)
    re(x) + re(y) + I*im(x) + I*im(y)
    >>> cos(x).expand(complex=True)
    -I*sin(re(x))*sinh(im(x)) + cos(re(x))*cosh(im(x))

    Note that this is just a wrapper around ``as_real_imag()``.  Most objects
    that wish to redefine ``_eval_expand_complex()`` should consider
    redefining ``as_real_imag()`` instead.

    func
    ----

    Expand other functions.

    >>> from sympy import gamma
    >>> gamma(x + 1).expand(func=True)
    x*gamma(x)

    trig
    ----

    Do trigonometric expansions.

    >>> cos(x + y).expand(trig=True)
    -sin(x)*sin(y) + cos(x)*cos(y)
    >>> sin(2*x).expand(trig=True)
    2*sin(x)*cos(x)

    Note that the forms of ``sin(n*x)`` and ``cos(n*x)`` in terms of ``sin(x)``
    and ``cos(x)`` are not unique, due to the identity `\\sin^2(x) + \\cos^2(x)
    = 1`.  The current implementation uses the form obtained from Chebyshev
    polynomials, but this may change.  See `this MathWorld article
    <https://mathworld.wolfram.com/Multiple-AngleFormulas.html>`_ for more
    information.

    Notes
    =====

    - You can shut off unwanted methods::

        >>> (exp(x + y)*(x + y)).expand()
        x*exp(x)*exp(y) + y*exp(x)*exp(y)
        >>> (exp(x + y)*(x + y)).expand(power_exp=False)
        x*exp(x + y) + y*exp(x + y)
        >>> (exp(x + y)*(x + y)).expand(mul=False)
        (x + y)*exp(x)*exp(y)

    - Use deep=False to only expand on the top level::

        >>> exp(x + exp(x + y)).expand()
        exp(x)*exp(exp(x)*exp(y))
        >>> exp(x + exp(x + y)).expand(deep=False)
        exp(x)*exp(exp(x + y))

    - Hints are applied in an arbitrary, but consistent order (in the current
      implementation, they are applied in alphabetical order, except
      multinomial comes before mul, but this may change).  Because of this,
      some hints may prevent expansion by other hints if they are applied
      first. For example, ``mul`` may distribute multiplications and prevent
      ``log`` and ``power_base`` from expanding them. Also, if ``mul`` is
      applied before ``multinomial`, the expression might not be fully
      distributed. The solution is to use the various ``expand_hint`` helper
      functions or to use ``hint=False`` to this function to finely control
      which hints are applied. Here are some examples::

        >>> from sympy import expand, expand_mul, expand_power_base
        >>> x, y, z = symbols('x,y,z', positive=True)

        >>> expand(log(x*(y + z)))
        log(x) + log(y + z)

      Here, we see that ``log`` was applied before ``mul``.  To get the mul
      expanded form, either of the following will work::

        >>> expand_mul(log(x*(y + z)))
        log(x*y + x*z)
        >>> expand(log(x*(y + z)), log=False)
        log(x*y + x*z)

      A similar thing can happen with the ``power_base`` hint::

        >>> expand((x*(y + z))**x)
        (x*y + x*z)**x

      To get the ``power_base`` expanded form, either of the following will
      work::

        >>> expand((x*(y + z))**x, mul=False)
        x**x*(y + z)**x
        >>> expand_power_base((x*(y + z))**x)
        x**x*(y + z)**x

        >>> expand((x + y)*y/x)
        y + y**2/x

      The parts of a rational expression can be targeted::

        >>> expand((x + y)*y/x/(x + 1), frac=True)
        (x*y + y**2)/(x**2 + x)
        >>> expand((x + y)*y/x/(x + 1), numer=True)
        (x*y + y**2)/(x*(x + 1))
        >>> expand((x + y)*y/x/(x + 1), denom=True)
        y*(x + y)/(x**2 + x)

    - The ``modulus`` meta-hint can be used to reduce the coefficients of an
      expression post-expansion::

        >>> expand((3*x + 1)**2)
        9*x**2 + 6*x + 1
        >>> expand((3*x + 1)**2, modulus=5)
        4*x**2 + x + 1

    - Either ``expand()`` the function or ``.expand()`` the method can be
      used.  Both are equivalent::

        >>> expand((x + 1)**2)
        x**2 + 2*x + 1
        >>> ((x + 1)**2).expand()
        x**2 + 2*x + 1

    API
    ===

    Objects can define their own expand hints by defining
    ``_eval_expand_hint()``.  The function should take the form::

        def _eval_expand_hint(self, **hints):
            # Only apply the method to the top-level expression
            ...

    See also the example below.  Objects should define ``_eval_expand_hint()``
    methods only if ``hint`` applies to that specific object.  The generic
    ``_eval_expand_hint()`` method defined in Expr will handle the no-op case.

    Each hint should be responsible for expanding that hint only.
    Furthermore, the expansion should be applied to the top-level expression
    only.  ``expand()`` takes care of the recursion that happens when
    ``deep=True``.

    You should only call ``_eval_expand_hint()`` methods directly if you are
    100% sure that the object has the method, as otherwise you are liable to
    get unexpected ``AttributeError``s.  Note, again, that you do not need to
    recursively apply the hint to args of your object: this is handled
    automatically by ``expand()``.  ``_eval_expand_hint()`` should
    generally not be used at all outside of an ``_eval_expand_hint()`` method.
    If you want to apply a specific expansion from within another method, use
    the public ``expand()`` function, method, or ``expand_hint()`` functions.

    In order for expand to work, objects must be rebuildable by their args,
    i.e., ``obj.func(*obj.args) == obj`` must hold.

    Expand methods are passed ``**hints`` so that expand hints may use
    'metahints'--hints that control how different expand methods are applied.
    For example, the ``force=True`` hint described above that causes
    ``expand(log=True)`` to ignore assumptions is such a metahint.  The
    ``deep`` meta-hint is handled exclusively by ``expand()`` and is not
    passed to ``_eval_expand_hint()`` methods.

    Note that expansion hints should generally be methods that perform some
    kind of 'expansion'.  For hints that simply rewrite an expression, use the
    .rewrite() API.

    Examples
    ========

    >>> from sympy import Expr, sympify
    >>> class MyClass(Expr):
    ...     def __new__(cls, *args):
    ...         args = sympify(args)
    ...         return Expr.__new__(cls, *args)
    ...
    ...     def _eval_expand_double(self, *, force=False, **hints):
    ...         '''
    ...         Doubles the args of MyClass.
    ...
    ...         If there more than four args, doubling is not performed,
    ...         unless force=True is also used (False by default).
    ...         '''
    ...         if not force and len(self.args) > 4:
    ...             return self
    ...         return self.func(*(self.args + self.args))
    ...
    >>> a = MyClass(1, 2, MyClass(3, 4))
    >>> a
    MyClass(1, 2, MyClass(3, 4))
    >>> a.expand(double=True)
    MyClass(1, 2, MyClass(3, 4, 3, 4), 1, 2, MyClass(3, 4, 3, 4))
    >>> a.expand(double=True, deep=False)
    MyClass(1, 2, MyClass(3, 4), 1, 2, MyClass(3, 4))

    >>> b = MyClass(1, 2, 3, 4, 5)
    >>> b.expand(double=True)
    MyClass(1, 2, 3, 4, 5)
    >>> b.expand(double=True, force=True)
    MyClass(1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

    See Also
    ========

    expand_log, expand_mul, expand_multinomial, expand_complex, expand_trig,
    expand_power_base, expand_power_exp, expand_func, sympy.simplify.hyperexpand.hyperexpand

    """
def expand_mul(expr, deep: bool = True):
    """
    Wrapper around expand that only uses the mul hint.  See the expand
    docstring for more information.

    Examples
    ========

    >>> from sympy import symbols, expand_mul, exp, log
    >>> x, y = symbols('x,y', positive=True)
    >>> expand_mul(exp(x+y)*(x+y)*log(x*y**2))
    x*exp(x + y)*log(x*y**2) + y*exp(x + y)*log(x*y**2)

    """
def expand_multinomial(expr, deep: bool = True):
    """
    Wrapper around expand that only uses the multinomial hint.  See the expand
    docstring for more information.

    Examples
    ========

    >>> from sympy import symbols, expand_multinomial, exp
    >>> x, y = symbols('x y', positive=True)
    >>> expand_multinomial((x + exp(x + 1))**2)
    x**2 + 2*x*exp(x + 1) + exp(2*x + 2)

    """
def expand_log(expr, deep: bool = True, force: bool = False, factor: bool = False):
    """
    Wrapper around expand that only uses the log hint.  See the expand
    docstring for more information.

    Examples
    ========

    >>> from sympy import symbols, expand_log, exp, log
    >>> x, y = symbols('x,y', positive=True)
    >>> expand_log(exp(x+y)*(x+y)*log(x*y**2))
    (x + y)*(log(x) + 2*log(y))*exp(x + y)

    """
def expand_func(expr, deep: bool = True):
    """
    Wrapper around expand that only uses the func hint.  See the expand
    docstring for more information.

    Examples
    ========

    >>> from sympy import expand_func, gamma
    >>> from sympy.abc import x
    >>> expand_func(gamma(x + 2))
    x*(x + 1)*gamma(x)

    """
def expand_trig(expr, deep: bool = True):
    """
    Wrapper around expand that only uses the trig hint.  See the expand
    docstring for more information.

    Examples
    ========

    >>> from sympy import expand_trig, sin
    >>> from sympy.abc import x, y
    >>> expand_trig(sin(x+y)*(x+y))
    (x + y)*(sin(x)*cos(y) + sin(y)*cos(x))

    """
def expand_complex(expr, deep: bool = True):
    """
    Wrapper around expand that only uses the complex hint.  See the expand
    docstring for more information.

    Examples
    ========

    >>> from sympy import expand_complex, exp, sqrt, I
    >>> from sympy.abc import z
    >>> expand_complex(exp(z))
    I*exp(re(z))*sin(im(z)) + exp(re(z))*cos(im(z))
    >>> expand_complex(sqrt(I))
    sqrt(2)/2 + sqrt(2)*I/2

    See Also
    ========

    sympy.core.expr.Expr.as_real_imag
    """
def expand_power_base(expr, deep: bool = True, force: bool = False):
    """
    Wrapper around expand that only uses the power_base hint.

    A wrapper to expand(power_base=True) which separates a power with a base
    that is a Mul into a product of powers, without performing any other
    expansions, provided that assumptions about the power's base and exponent
    allow.

    deep=False (default is True) will only apply to the top-level expression.

    force=True (default is False) will cause the expansion to ignore
    assumptions about the base and exponent. When False, the expansion will
    only happen if the base is non-negative or the exponent is an integer.

    >>> from sympy.abc import x, y, z
    >>> from sympy import expand_power_base, sin, cos, exp, Symbol

    >>> (x*y)**2
    x**2*y**2

    >>> (2*x)**y
    (2*x)**y
    >>> expand_power_base(_)
    2**y*x**y

    >>> expand_power_base((x*y)**z)
    (x*y)**z
    >>> expand_power_base((x*y)**z, force=True)
    x**z*y**z
    >>> expand_power_base(sin((x*y)**z), deep=False)
    sin((x*y)**z)
    >>> expand_power_base(sin((x*y)**z), force=True)
    sin(x**z*y**z)

    >>> expand_power_base((2*sin(x))**y + (2*cos(x))**y)
    2**y*sin(x)**y + 2**y*cos(x)**y

    >>> expand_power_base((2*exp(y))**x)
    2**x*exp(y)**x

    >>> expand_power_base((2*cos(x))**y)
    2**y*cos(x)**y

    Notice that sums are left untouched. If this is not the desired behavior,
    apply full ``expand()`` to the expression:

    >>> expand_power_base(((x+y)*z)**2)
    z**2*(x + y)**2
    >>> (((x+y)*z)**2).expand()
    x**2*z**2 + 2*x*y*z**2 + y**2*z**2

    >>> expand_power_base((2*y)**(1+z))
    2**(z + 1)*y**(z + 1)
    >>> ((2*y)**(1+z)).expand()
    2*2**z*y**(z + 1)

    The power that is unexpanded can be expanded safely when
    ``y != 0``, otherwise different values might be obtained for the expression:

    >>> prev = _

    If we indicate that ``y`` is positive but then replace it with
    a value of 0 after expansion, the expression becomes 0:

    >>> p = Symbol('p', positive=True)
    >>> prev.subs(y, p).expand().subs(p, 0)
    0

    But if ``z = -1`` the expression would not be zero:

    >>> prev.subs(y, 0).subs(z, -1)
    1

    See Also
    ========

    expand

    """
def expand_power_exp(expr, deep: bool = True):
    """
    Wrapper around expand that only uses the power_exp hint.

    See the expand docstring for more information.

    Examples
    ========

    >>> from sympy import expand_power_exp, Symbol
    >>> from sympy.abc import x, y
    >>> expand_power_exp(3**(y + 2))
    9*3**y
    >>> expand_power_exp(x**(y + 2))
    x**(y + 2)

    If ``x = 0`` the value of the expression depends on the
    value of ``y``; if the expression were expanded the result
    would be 0. So expansion is only done if ``x != 0``:

    >>> expand_power_exp(Symbol('x', zero=False)**(y + 2))
    x**2*x**y
    """
def count_ops(expr, visual: bool = False):
    '''
    Return a representation (integer or expression) of the operations in expr.

    Parameters
    ==========

    expr : Expr
        If expr is an iterable, the sum of the op counts of the
        items will be returned.

    visual : bool, optional
        If ``False`` (default) then the sum of the coefficients of the
        visual expression will be returned.
        If ``True`` then the number of each type of operation is shown
        with the core class types (or their virtual equivalent) multiplied by the
        number of times they occur.

    Examples
    ========

    >>> from sympy.abc import a, b, x, y
    >>> from sympy import sin, count_ops

    Although there is not a SUB object, minus signs are interpreted as
    either negations or subtractions:

    >>> (x - y).count_ops(visual=True)
    SUB
    >>> (-x).count_ops(visual=True)
    NEG

    Here, there are two Adds and a Pow:

    >>> (1 + a + b**2).count_ops(visual=True)
    2*ADD + POW

    In the following, an Add, Mul, Pow and two functions:

    >>> (sin(x)*x + sin(x)**2).count_ops(visual=True)
    ADD + MUL + POW + 2*SIN

    for a total of 5:

    >>> (sin(x)*x + sin(x)**2).count_ops(visual=False)
    5

    Note that "what you type" is not always what you get. The expression
    1/x/y is translated by sympy into 1/(x*y) so it gives a DIV and MUL rather
    than two DIVs:

    >>> (1/x/y).count_ops(visual=True)
    DIV + MUL

    The visual option can be used to demonstrate the difference in
    operations for expressions in different forms. Here, the Horner
    representation is compared with the expanded form of a polynomial:

    >>> eq=x*(1 + x*(2 + x*(3 + x)))
    >>> count_ops(eq.expand(), visual=True) - count_ops(eq, visual=True)
    -MUL + 3*POW

    The count_ops function also handles iterables:

    >>> count_ops([x, sin(x), None, True, x + 2], visual=False)
    2
    >>> count_ops([x, sin(x), None, True, x + 2], visual=True)
    ADD + SIN
    >>> count_ops({x: sin(x), x + 2: y + 1}, visual=True)
    2*ADD + SIN

    '''
def nfloat(expr, n: int = 15, exponent: bool = False, dkeys: bool = False):
    """Make all Rationals in expr Floats except those in exponents
    (unless the exponents flag is set to True) and those in undefined
    functions. When processing dictionaries, do not modify the keys
    unless ``dkeys=True``.

    Examples
    ========

    >>> from sympy import nfloat, cos, pi, sqrt
    >>> from sympy.abc import x, y
    >>> nfloat(x**4 + x/2 + cos(pi/3) + 1 + sqrt(y))
    x**4 + 0.5*x + sqrt(y) + 1.5
    >>> nfloat(x**4 + sqrt(y), exponent=True)
    x**4.0 + y**0.5

    Container types are not modified:

    >>> type(nfloat((1, 2))) is tuple
    True
    """
