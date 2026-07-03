import abc
from .integrals import Integral as Integral
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from dataclasses import dataclass
from sympy.core.add import Add as Add
from sympy.core.cache import cacheit as cacheit
from sympy.core.containers import Dict as Dict
from sympy.core.expr import Expr as Expr
from sympy.core.function import Derivative as Derivative
from sympy.core.logic import fuzzy_not as fuzzy_not
from sympy.core.mul import Mul as Mul
from sympy.core.numbers import E as E, Integer as Integer, Number as Number
from sympy.core.power import Pow as Pow
from sympy.core.relational import Boolean as Boolean, Eq as Eq, Ne as Ne
from sympy.core.singleton import S as S
from sympy.core.symbol import Dummy as Dummy, Symbol as Symbol, Wild as Wild
from sympy.functions.elementary.complexes import Abs as Abs
from sympy.functions.elementary.exponential import exp as exp, log as log
from sympy.functions.elementary.hyperbolic import HyperbolicFunction as HyperbolicFunction, asinh as asinh, cosh as cosh, coth as coth, csch as csch, sech as sech, sinh as sinh, tanh as tanh
from sympy.functions.elementary.miscellaneous import sqrt as sqrt
from sympy.functions.elementary.piecewise import Piecewise as Piecewise
from sympy.functions.elementary.trigonometric import TrigonometricFunction as TrigonometricFunction, acos as acos, acot as acot, acsc as acsc, asec as asec, asin as asin, atan as atan, cos as cos, cot as cot, csc as csc, sec as sec, sin as sin, tan as tan
from sympy.functions.special.delta_functions import DiracDelta as DiracDelta, Heaviside as Heaviside
from sympy.functions.special.elliptic_integrals import elliptic_e as elliptic_e, elliptic_f as elliptic_f
from sympy.functions.special.error_functions import Chi as Chi, Ci as Ci, Ei as Ei, Shi as Shi, Si as Si, erf as erf, erfi as erfi, fresnelc as fresnelc, fresnels as fresnels, li as li
from sympy.functions.special.gamma_functions import uppergamma as uppergamma
from sympy.functions.special.polynomials import OrthogonalPolynomial as OrthogonalPolynomial, assoc_laguerre as assoc_laguerre, chebyshevt as chebyshevt, chebyshevu as chebyshevu, gegenbauer as gegenbauer, hermite as hermite, jacobi as jacobi, laguerre as laguerre, legendre as legendre
from sympy.functions.special.zeta_functions import polylog as polylog
from sympy.logic.boolalg import And as And
from sympy.ntheory.factor_ import primefactors as primefactors
from sympy.polys.polytools import Poly as Poly, degree as degree, gcd_list as gcd_list, lcm_list as lcm_list
from sympy.simplify.radsimp import fraction as fraction
from sympy.simplify.simplify import simplify as simplify
from sympy.solvers.solvers import solve as solve
from sympy.strategies.core import condition as condition, do_one as do_one, null_safe as null_safe, switch as switch
from sympy.utilities.iterables import iterable as iterable
from sympy.utilities.misc import debug as debug
from typing import NamedTuple, Sequence

@dataclass
class Rule(ABC, metaclass=abc.ABCMeta):
    integrand: Expr
    variable: Symbol
    @abstractmethod
    def eval(self) -> Expr: ...
    @abstractmethod
    def contains_dont_know(self) -> bool: ...
    def __init__(self, integrand, variable) -> None: ...

@dataclass
class AtomicRule(Rule, ABC, metaclass=abc.ABCMeta):
    """A simple rule that does not depend on other rules"""
    def contains_dont_know(self) -> bool: ...
    def __init__(self, integrand, variable) -> None: ...

@dataclass
class ConstantRule(AtomicRule):
    """integrate(a, x)  ->  a*x"""
    def eval(self) -> Expr: ...
    def __init__(self, integrand, variable) -> None: ...

@dataclass
class ConstantTimesRule(Rule):
    """integrate(a*f(x), x)  ->  a*integrate(f(x), x)"""
    constant: Expr
    other: Expr
    substep: Rule
    def eval(self) -> Expr: ...
    def contains_dont_know(self) -> bool: ...
    def __init__(self, integrand, variable, constant, other, substep) -> None: ...

@dataclass
class PowerRule(AtomicRule):
    """integrate(x**a, x)"""
    base: Expr
    exp: Expr
    def eval(self) -> Expr: ...
    def __init__(self, integrand, variable, base, exp) -> None: ...

@dataclass
class NestedPowRule(AtomicRule):
    """integrate((x**a)**b, x)"""
    base: Expr
    exp: Expr
    def eval(self) -> Expr: ...
    def __init__(self, integrand, variable, base, exp) -> None: ...

@dataclass
class AddRule(Rule):
    """integrate(f(x) + g(x), x) -> integrate(f(x), x) + integrate(g(x), x)"""
    substeps: list[Rule]
    def eval(self) -> Expr: ...
    def contains_dont_know(self) -> bool: ...
    def __init__(self, integrand, variable, substeps) -> None: ...

@dataclass
class URule(Rule):
    """integrate(f(g(x))*g'(x), x) -> integrate(f(u), u), u = g(x)"""
    u_var: Symbol
    u_func: Expr
    substep: Rule
    def eval(self) -> Expr: ...
    def contains_dont_know(self) -> bool: ...
    def __init__(self, integrand, variable, u_var, u_func, substep) -> None: ...

@dataclass
class PartsRule(Rule):
    """integrate(u(x)*v'(x), x) -> u(x)*v(x) - integrate(u'(x)*v(x), x)"""
    u: Symbol
    dv: Expr
    v_step: Rule
    second_step: Rule | None
    def eval(self) -> Expr: ...
    def contains_dont_know(self) -> bool: ...
    def __init__(self, integrand, variable, u, dv, v_step, second_step) -> None: ...

@dataclass
class CyclicPartsRule(Rule):
    """Apply PartsRule multiple times to integrate exp(x)*sin(x)"""
    parts_rules: list[PartsRule]
    coefficient: Expr
    def eval(self) -> Expr: ...
    def contains_dont_know(self) -> bool: ...
    def __init__(self, integrand, variable, parts_rules, coefficient) -> None: ...

@dataclass
class TrigRule(AtomicRule, ABC, metaclass=abc.ABCMeta):
    def __init__(self, integrand, variable) -> None: ...

@dataclass
class SinRule(TrigRule):
    """integrate(sin(x), x) -> -cos(x)"""
    def eval(self) -> Expr: ...
    def __init__(self, integrand, variable) -> None: ...

@dataclass
class CosRule(TrigRule):
    """integrate(cos(x), x) -> sin(x)"""
    def eval(self) -> Expr: ...
    def __init__(self, integrand, variable) -> None: ...

@dataclass
class SecTanRule(TrigRule):
    """integrate(sec(x)*tan(x), x) -> sec(x)"""
    def eval(self) -> Expr: ...
    def __init__(self, integrand, variable) -> None: ...

@dataclass
class CscCotRule(TrigRule):
    """integrate(csc(x)*cot(x), x) -> -csc(x)"""
    def eval(self) -> Expr: ...
    def __init__(self, integrand, variable) -> None: ...

@dataclass
class Sec2Rule(TrigRule):
    """integrate(sec(x)**2, x) -> tan(x)"""
    def eval(self) -> Expr: ...
    def __init__(self, integrand, variable) -> None: ...

@dataclass
class Csc2Rule(TrigRule):
    """integrate(csc(x)**2, x) -> -cot(x)"""
    def eval(self) -> Expr: ...
    def __init__(self, integrand, variable) -> None: ...

@dataclass
class HyperbolicRule(AtomicRule, ABC, metaclass=abc.ABCMeta):
    def __init__(self, integrand, variable) -> None: ...

@dataclass
class SinhRule(HyperbolicRule):
    """integrate(sinh(x), x) -> cosh(x)"""
    def eval(self) -> Expr: ...
    def __init__(self, integrand, variable) -> None: ...

@dataclass
class CoshRule(HyperbolicRule):
    """integrate(cosh(x), x) -> sinh(x)"""
    def eval(self): ...
    def __init__(self, integrand, variable) -> None: ...

@dataclass
class ExpRule(AtomicRule):
    """integrate(a**x, x) -> a**x/ln(a)"""
    base: Expr
    exp: Expr
    def eval(self) -> Expr: ...
    def __init__(self, integrand, variable, base, exp) -> None: ...

@dataclass
class ReciprocalRule(AtomicRule):
    """integrate(1/x, x) -> ln(x)"""
    base: Expr
    def eval(self) -> Expr: ...
    def __init__(self, integrand, variable, base) -> None: ...

@dataclass
class ArcsinRule(AtomicRule):
    """integrate(1/sqrt(1-x**2), x) -> asin(x)"""
    def eval(self) -> Expr: ...
    def __init__(self, integrand, variable) -> None: ...

@dataclass
class ArcsinhRule(AtomicRule):
    """integrate(1/sqrt(1+x**2), x) -> asin(x)"""
    def eval(self) -> Expr: ...
    def __init__(self, integrand, variable) -> None: ...

@dataclass
class ReciprocalSqrtQuadraticRule(AtomicRule):
    """integrate(1/sqrt(a+b*x+c*x**2), x) -> log(2*sqrt(c)*sqrt(a+b*x+c*x**2)+b+2*c*x)/sqrt(c)"""
    a: Expr
    b: Expr
    c: Expr
    def eval(self) -> Expr: ...
    def __init__(self, integrand, variable, a, b, c) -> None: ...

@dataclass
class SqrtQuadraticDenomRule(AtomicRule):
    """integrate(poly(x)/sqrt(a+b*x+c*x**2), x)"""
    a: Expr
    b: Expr
    c: Expr
    coeffs: list[Expr]
    def eval(self) -> Expr: ...
    def __init__(self, integrand, variable, a, b, c, coeffs) -> None: ...

@dataclass
class SqrtQuadraticRule(AtomicRule):
    """integrate(sqrt(a+b*x+c*x**2), x)"""
    a: Expr
    b: Expr
    c: Expr
    def eval(self) -> Expr: ...
    def __init__(self, integrand, variable, a, b, c) -> None: ...

@dataclass
class AlternativeRule(Rule):
    """Multiple ways to do integration."""
    alternatives: list[Rule]
    def eval(self) -> Expr: ...
    def contains_dont_know(self) -> bool: ...
    def __init__(self, integrand, variable, alternatives) -> None: ...

@dataclass
class DontKnowRule(Rule):
    """Leave the integral as is."""
    def eval(self) -> Expr: ...
    def contains_dont_know(self) -> bool: ...
    def __init__(self, integrand, variable) -> None: ...

@dataclass
class DerivativeRule(AtomicRule):
    """integrate(f'(x), x) -> f(x)"""
    def eval(self) -> Expr: ...
    def __init__(self, integrand, variable) -> None: ...

@dataclass
class RewriteRule(Rule):
    """Rewrite integrand to another form that is easier to handle."""
    rewritten: Expr
    substep: Rule
    def eval(self) -> Expr: ...
    def contains_dont_know(self) -> bool: ...
    def __init__(self, integrand, variable, rewritten, substep) -> None: ...

@dataclass
class CompleteSquareRule(RewriteRule):
    """Rewrite a+b*x+c*x**2 to a-b**2/(4*c) + c*(x+b/(2*c))**2"""
    def __init__(self, integrand, variable, rewritten, substep) -> None: ...

@dataclass
class PiecewiseRule(Rule):
    subfunctions: Sequence[tuple[Rule, bool | Boolean]]
    def eval(self) -> Expr: ...
    def contains_dont_know(self) -> bool: ...
    def __init__(self, integrand, variable, subfunctions) -> None: ...

@dataclass
class HeavisideRule(Rule):
    harg: Expr
    ibnd: Expr
    substep: Rule
    def eval(self) -> Expr: ...
    def contains_dont_know(self) -> bool: ...
    def __init__(self, integrand, variable, harg, ibnd, substep) -> None: ...

@dataclass
class DiracDeltaRule(AtomicRule):
    n: Expr
    a: Expr
    b: Expr
    def eval(self) -> Expr: ...
    def __init__(self, integrand, variable, n, a, b) -> None: ...

@dataclass
class TrigSubstitutionRule(Rule):
    theta: Expr
    func: Expr
    rewritten: Expr
    substep: Rule
    restriction: bool | Boolean
    def eval(self) -> Expr: ...
    def contains_dont_know(self) -> bool: ...
    def __init__(self, integrand, variable, theta, func, rewritten, substep, restriction) -> None: ...

@dataclass
class ArctanRule(AtomicRule):
    """integrate(a/(b*x**2+c), x) -> a/b / sqrt(c/b) * atan(x/sqrt(c/b))"""
    a: Expr
    b: Expr
    c: Expr
    def eval(self) -> Expr: ...
    def __init__(self, integrand, variable, a, b, c) -> None: ...

@dataclass
class OrthogonalPolyRule(AtomicRule, ABC, metaclass=abc.ABCMeta):
    n: Expr
    def __init__(self, integrand, variable, n) -> None: ...

@dataclass
class JacobiRule(OrthogonalPolyRule):
    a: Expr
    b: Expr
    def eval(self) -> Expr: ...
    def __init__(self, integrand, variable, n, a, b) -> None: ...

@dataclass
class GegenbauerRule(OrthogonalPolyRule):
    a: Expr
    def eval(self) -> Expr: ...
    def __init__(self, integrand, variable, n, a) -> None: ...

@dataclass
class ChebyshevTRule(OrthogonalPolyRule):
    def eval(self) -> Expr: ...
    def __init__(self, integrand, variable, n) -> None: ...

@dataclass
class ChebyshevURule(OrthogonalPolyRule):
    def eval(self) -> Expr: ...
    def __init__(self, integrand, variable, n) -> None: ...

@dataclass
class LegendreRule(OrthogonalPolyRule):
    def eval(self) -> Expr: ...
    def __init__(self, integrand, variable, n) -> None: ...

@dataclass
class HermiteRule(OrthogonalPolyRule):
    def eval(self) -> Expr: ...
    def __init__(self, integrand, variable, n) -> None: ...

@dataclass
class LaguerreRule(OrthogonalPolyRule):
    def eval(self) -> Expr: ...
    def __init__(self, integrand, variable, n) -> None: ...

@dataclass
class AssocLaguerreRule(OrthogonalPolyRule):
    a: Expr
    def eval(self) -> Expr: ...
    def __init__(self, integrand, variable, n, a) -> None: ...

@dataclass
class IRule(AtomicRule, ABC, metaclass=abc.ABCMeta):
    a: Expr
    b: Expr
    def __init__(self, integrand, variable, a, b) -> None: ...

@dataclass
class CiRule(IRule):
    def eval(self) -> Expr: ...
    def __init__(self, integrand, variable, a, b) -> None: ...

@dataclass
class ChiRule(IRule):
    def eval(self) -> Expr: ...
    def __init__(self, integrand, variable, a, b) -> None: ...

@dataclass
class EiRule(IRule):
    def eval(self) -> Expr: ...
    def __init__(self, integrand, variable, a, b) -> None: ...

@dataclass
class SiRule(IRule):
    def eval(self) -> Expr: ...
    def __init__(self, integrand, variable, a, b) -> None: ...

@dataclass
class ShiRule(IRule):
    def eval(self) -> Expr: ...
    def __init__(self, integrand, variable, a, b) -> None: ...

@dataclass
class LiRule(IRule):
    def eval(self) -> Expr: ...
    def __init__(self, integrand, variable, a, b) -> None: ...

@dataclass
class ErfRule(AtomicRule):
    a: Expr
    b: Expr
    c: Expr
    def eval(self) -> Expr: ...
    def __init__(self, integrand, variable, a, b, c) -> None: ...

@dataclass
class FresnelCRule(AtomicRule):
    a: Expr
    b: Expr
    c: Expr
    def eval(self) -> Expr: ...
    def __init__(self, integrand, variable, a, b, c) -> None: ...

@dataclass
class FresnelSRule(AtomicRule):
    a: Expr
    b: Expr
    c: Expr
    def eval(self) -> Expr: ...
    def __init__(self, integrand, variable, a, b, c) -> None: ...

@dataclass
class PolylogRule(AtomicRule):
    a: Expr
    b: Expr
    def eval(self) -> Expr: ...
    def __init__(self, integrand, variable, a, b) -> None: ...

@dataclass
class UpperGammaRule(AtomicRule):
    a: Expr
    e: Expr
    def eval(self) -> Expr: ...
    def __init__(self, integrand, variable, a, e) -> None: ...

@dataclass
class EllipticFRule(AtomicRule):
    a: Expr
    d: Expr
    def eval(self) -> Expr: ...
    def __init__(self, integrand, variable, a, d) -> None: ...

@dataclass
class EllipticERule(AtomicRule):
    a: Expr
    d: Expr
    def eval(self) -> Expr: ...
    def __init__(self, integrand, variable, a, d) -> None: ...

class IntegralInfo(NamedTuple):
    integrand: Expr
    symbol: Symbol

def manual_diff(f, symbol):
    """Derivative of f in form expected by find_substitutions

    SymPy's derivatives for some trig functions (like cot) are not in a form
    that works well with finding substitutions; this replaces the
    derivatives for those particular forms with something that works better.

    """
def manual_subs(expr, *args):
    """
    A wrapper for `expr.subs(*args)` with additional logic for substitution
    of invertible functions.
    """

inverse_trig_functions: Incomplete

def find_substitutions(integrand, symbol, u_var): ...
def rewriter(condition, rewrite):
    """Strategy that rewrites an integrand."""
def proxy_rewriter(condition, rewrite):
    """Strategy that rewrites an integrand based on some other criteria."""
def multiplexer(conditions):
    """Apply the rule that matches the condition, else None"""
def alternatives(*rules):
    """Strategy that makes an AlternativeRule out of multiple possible results."""
def constant_rule(integral): ...
def power_rule(integral): ...
def exp_rule(integral): ...
def orthogonal_poly_rule(integral): ...
def special_function_rule(integral): ...
def nested_pow_rule(integral: IntegralInfo): ...
def inverse_trig_rule(integral: IntegralInfo, degenerate: bool = True):
    """
    Set degenerate=False on recursive call where coefficient of quadratic term
    is assumed non-zero.
    """
def add_rule(integral): ...
def mul_rule(integral: IntegralInfo): ...
def parts_rule(integral): ...
def trig_rule(integral): ...
def trig_product_rule(integral: IntegralInfo): ...
def quadratic_denom_rule(integral): ...
def sqrt_linear_rule(integral: IntegralInfo):
    """
    Substitute common (a+b*x)**(1/n)
    """
def sqrt_quadratic_rule(integral: IntegralInfo, degenerate: bool = True): ...
def hyperbolic_rule(integral: tuple[Expr, Symbol]): ...
def make_wilds(symbol): ...
def sincos_pattern(symbol): ...
def tansec_pattern(symbol): ...
def cotcsc_pattern(symbol): ...
def heaviside_pattern(symbol): ...
def uncurry(func): ...
def trig_rewriter(rewrite): ...

sincos_botheven_condition: Incomplete
sincos_botheven: Incomplete
sincos_sinodd_condition: Incomplete
sincos_sinodd: Incomplete
sincos_cosodd_condition: Incomplete
sincos_cosodd: Incomplete
tansec_seceven_condition: Incomplete
tansec_seceven: Incomplete
tansec_tanodd_condition: Incomplete
tansec_tanodd: Incomplete
tan_tansquared_condition: Incomplete
tan_tansquared: Incomplete
cotcsc_csceven_condition: Incomplete
cotcsc_csceven: Incomplete
cotcsc_cotodd_condition: Incomplete
cotcsc_cotodd: Incomplete

def trig_sincos_rule(integral): ...
def trig_tansec_rule(integral): ...
def trig_cotcsc_rule(integral): ...
def trig_sindouble_rule(integral): ...
def trig_powers_products_rule(integral): ...
def trig_substitution_rule(integral): ...
def heaviside_rule(integral): ...
def dirac_delta_rule(integral: IntegralInfo): ...
def substitution_rule(integral): ...

partial_fractions_rule: Incomplete
cancel_rule: Incomplete
distribute_expand_rule: Incomplete
trig_expand_rule: Incomplete

def derivative_rule(integral): ...
def rewrites_rule(integral): ...
def fallback_rule(integral): ...
def integral_steps(integrand, symbol, **options):
    """Returns the steps needed to compute an integral.

    Explanation
    ===========

    This function attempts to mirror what a student would do by hand as
    closely as possible.

    SymPy Gamma uses this to provide a step-by-step explanation of an
    integral. The code it uses to format the results of this function can be
    found at
    https://github.com/sympy/sympy_gamma/blob/master/app/logic/intsteps.py.

    Examples
    ========

    >>> from sympy import exp, sin
    >>> from sympy.integrals.manualintegrate import integral_steps
    >>> from sympy.abc import x
    >>> print(repr(integral_steps(exp(x) / (1 + exp(2 * x)), x)))     # doctest: +NORMALIZE_WHITESPACE
    URule(integrand=exp(x)/(exp(2*x) + 1), variable=x, u_var=_u, u_func=exp(x),
    substep=ArctanRule(integrand=1/(_u**2 + 1), variable=_u, a=1, b=1, c=1))
    >>> print(repr(integral_steps(sin(x), x)))     # doctest: +NORMALIZE_WHITESPACE
    SinRule(integrand=sin(x), variable=x)
    >>> print(repr(integral_steps((x**2 + 3)**2, x)))     # doctest: +NORMALIZE_WHITESPACE
    RewriteRule(integrand=(x**2 + 3)**2, variable=x, rewritten=x**4 + 6*x**2 + 9,
    substep=AddRule(integrand=x**4 + 6*x**2 + 9, variable=x,
    substeps=[PowerRule(integrand=x**4, variable=x, base=x, exp=4),
    ConstantTimesRule(integrand=6*x**2, variable=x, constant=6, other=x**2,
    substep=PowerRule(integrand=x**2, variable=x, base=x, exp=2)),
    ConstantRule(integrand=9, variable=x)]))

    Returns
    =======

    rule : Rule
        The first step; most rules have substeps that must also be
        considered. These substeps can be evaluated using ``manualintegrate``
        to obtain a result.

    """
def manualintegrate(f, var):
    """manualintegrate(f, var)

    Explanation
    ===========

    Compute indefinite integral of a single variable using an algorithm that
    resembles what a student would do by hand.

    Unlike :func:`~.integrate`, var can only be a single symbol.

    Examples
    ========

    >>> from sympy import sin, cos, tan, exp, log, integrate
    >>> from sympy.integrals.manualintegrate import manualintegrate
    >>> from sympy.abc import x
    >>> manualintegrate(1 / x, x)
    log(x)
    >>> integrate(1/x)
    log(x)
    >>> manualintegrate(log(x), x)
    x*log(x) - x
    >>> integrate(log(x))
    x*log(x) - x
    >>> manualintegrate(exp(x) / (1 + exp(2 * x)), x)
    atan(exp(x))
    >>> integrate(exp(x) / (1 + exp(2 * x)))
    RootSum(4*_z**2 + 1, Lambda(_i, _i*log(2*_i + exp(x))))
    >>> manualintegrate(cos(x)**4 * sin(x), x)
    -cos(x)**5/5
    >>> integrate(cos(x)**4 * sin(x), x)
    -cos(x)**5/5
    >>> manualintegrate(cos(x)**4 * sin(x)**3, x)
    cos(x)**7/7 - cos(x)**5/5
    >>> integrate(cos(x)**4 * sin(x)**3, x)
    cos(x)**7/7 - cos(x)**5/5
    >>> manualintegrate(tan(x), x)
    -log(cos(x))
    >>> integrate(tan(x), x)
    -log(cos(x))

    See Also
    ========

    sympy.integrals.integrals.integrate
    sympy.integrals.integrals.Integral.doit
    sympy.integrals.integrals.Integral
    """
