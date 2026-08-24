from _typeshed import Incomplete
from sympy.assumptions import Q as Q, ask as ask
from sympy.codegen.cfunctions import exp2 as exp2, expm1 as expm1, log1p as log1p, log2 as log2
from sympy.codegen.matrix_nodes import MatrixSolve as MatrixSolve
from sympy.codegen.numpy_nodes import logaddexp as logaddexp, logaddexp2 as logaddexp2
from sympy.codegen.scipy_nodes import cosm1 as cosm1, powm1 as powm1
from sympy.core.expr import UnevaluatedExpr as UnevaluatedExpr
from sympy.core.function import expand_log as expand_log
from sympy.core.mul import Mul as Mul
from sympy.core.power import Pow as Pow
from sympy.core.singleton import S as S
from sympy.core.symbol import Wild as Wild
from sympy.functions.elementary.complexes import sign as sign
from sympy.functions.elementary.exponential import exp as exp, log as log
from sympy.functions.elementary.miscellaneous import Max as Max, Min as Min
from sympy.functions.elementary.trigonometric import cos as cos, sin as sin, sinc as sinc
from sympy.matrices.expressions.matexpr import MatrixSymbol as MatrixSymbol
from sympy.utilities.iterables import sift as sift

class Optimization:
    """ Abstract base class for rewriting optimization.

    Subclasses should implement ``__call__`` taking an expression
    as argument.

    Parameters
    ==========
    cost_function : callable returning number
    priority : number

    """
    cost_function: Incomplete
    priority: Incomplete
    def __init__(self, cost_function: Incomplete | None = None, priority: int = 1) -> None: ...
    def cheapest(self, *args): ...

class ReplaceOptim(Optimization):
    """ Rewriting optimization calling replace on expressions.

    Explanation
    ===========

    The instance can be used as a function on expressions for which
    it will apply the ``replace`` method (see
    :meth:`sympy.core.basic.Basic.replace`).

    Parameters
    ==========

    query :
        First argument passed to replace.
    value :
        Second argument passed to replace.

    Examples
    ========

    >>> from sympy import Symbol
    >>> from sympy.codegen.rewriting import ReplaceOptim
    >>> from sympy.codegen.cfunctions import exp2
    >>> x = Symbol('x')
    >>> exp2_opt = ReplaceOptim(lambda p: p.is_Pow and p.base == 2,
    ...     lambda p: exp2(p.exp))
    >>> exp2_opt(2**x)
    exp2(x)

    """
    query: Incomplete
    value: Incomplete
    def __init__(self, query, value, **kwargs) -> None: ...
    def __call__(self, expr): ...

def optimize(expr, optimizations):
    """ Apply optimizations to an expression.

    Parameters
    ==========

    expr : expression
    optimizations : iterable of ``Optimization`` instances
        The optimizations will be sorted with respect to ``priority`` (highest first).

    Examples
    ========

    >>> from sympy import log, Symbol
    >>> from sympy.codegen.rewriting import optims_c99, optimize
    >>> x = Symbol('x')
    >>> optimize(log(x+3)/log(2) + log(x**2 + 1), optims_c99)
    log1p(x**2) + log2(x + 3)

    """

exp2_opt: Incomplete
sinc_opt1: Incomplete
sinc_opt2: Incomplete
sinc_opts: Incomplete
log2_opt: Incomplete
log2const_opt: Incomplete
logsumexp_2terms_opt: Incomplete

class FuncMinusOneOptim(ReplaceOptim):
    '''Specialization of ReplaceOptim for functions evaluating "f(x) - 1".

    Explanation
    ===========

    Numerical functions which go toward one as x go toward zero is often best
    implemented by a dedicated function in order to avoid catastrophic
    cancellation. One such example is ``expm1(x)`` in the C standard library
    which evaluates ``exp(x) - 1``. Such functions preserves many more
    significant digits when its argument is much smaller than one, compared
    to subtracting one afterwards.

    Parameters
    ==========

    func :
        The function which is subtracted by one.
    func_m_1 :
        The specialized function evaluating ``func(x) - 1``.
    opportunistic : bool
        When ``True``, apply the transformation as long as the magnitude of the
        remaining number terms decreases. When ``False``, only apply the
        transformation if it completely eliminates the number term.

    Examples
    ========

    >>> from sympy import symbols, exp
    >>> from sympy.codegen.rewriting import FuncMinusOneOptim
    >>> from sympy.codegen.cfunctions import expm1
    >>> x, y = symbols(\'x y\')
    >>> expm1_opt = FuncMinusOneOptim(exp, expm1)
    >>> expm1_opt(exp(x) + 2*exp(5*y) - 3)
    expm1(x) + 2*expm1(5*y)


    '''
    func: Incomplete
    func_m_1: Incomplete
    opportunistic: Incomplete
    def __init__(self, func, func_m_1, opportunistic: bool = True) -> None: ...
    def replace_in_Add(self, e):
        """ passed as second argument to Basic.replace(...) """
    def __call__(self, expr): ...

expm1_opt: Incomplete
cosm1_opt: Incomplete
powm1_opt: Incomplete
log1p_opt: Incomplete

def create_expand_pow_optimization(limit, *, base_req=...):
    """ Creates an instance of :class:`ReplaceOptim` for expanding ``Pow``.

    Explanation
    ===========

    The requirements for expansions are that the base needs to be a symbol
    and the exponent needs to be an Integer (and be less than or equal to
    ``limit``).

    Parameters
    ==========

    limit : int
         The highest power which is expanded into multiplication.
    base_req : function returning bool
         Requirement on base for expansion to happen, default is to return
         the ``is_symbol`` attribute of the base.

    Examples
    ========

    >>> from sympy import Symbol, sin
    >>> from sympy.codegen.rewriting import create_expand_pow_optimization
    >>> x = Symbol('x')
    >>> expand_opt = create_expand_pow_optimization(3)
    >>> expand_opt(x**5 + x**3)
    x**5 + x*x*x
    >>> expand_opt(x**5 + x**3 + sin(x)**3)
    x**5 + sin(x)**3 + x*x*x
    >>> opt2 = create_expand_pow_optimization(3, base_req=lambda b: not b.is_Function)
    >>> opt2((x+1)**2 + sin(x)**2)
    sin(x)**2 + (x + 1)*(x + 1)

    """

matinv_opt: Incomplete
logaddexp_opt: Incomplete
logaddexp2_opt: Incomplete
optims_c99: Incomplete
optims_numpy: Incomplete
optims_scipy: Incomplete
