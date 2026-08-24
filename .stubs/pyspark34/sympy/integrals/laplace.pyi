from _typeshed import Incomplete
from sympy.core import I as I, S as S, pi as pi
from sympy.core.add import Add as Add
from sympy.core.cache import cacheit as cacheit
from sympy.core.function import AppliedUndef as AppliedUndef, Derivative as Derivative, Lambda as Lambda, WildFunction as WildFunction, diff as diff, expand as expand, expand_complex as expand_complex, expand_mul as expand_mul, expand_trig as expand_trig
from sympy.core.mul import Mul as Mul, prod as prod
from sympy.core.relational import Eq as Eq, Ge as Ge, Gt as Gt, Lt as Lt, Unequality as Unequality
from sympy.core.sorting import ordered as ordered
from sympy.core.symbol import Dummy as Dummy, Wild as Wild, symbols as symbols
from sympy.functions.elementary.complexes import Abs as Abs, arg as arg, im as im, periodic_argument as periodic_argument, polar_lift as polar_lift, re as re
from sympy.functions.elementary.exponential import exp as exp, log as log
from sympy.functions.elementary.hyperbolic import asinh as asinh, cosh as cosh, coth as coth, sinh as sinh
from sympy.functions.elementary.miscellaneous import Max as Max, Min as Min, sqrt as sqrt
from sympy.functions.elementary.piecewise import Piecewise as Piecewise
from sympy.functions.elementary.trigonometric import atan as atan, cos as cos, sin as sin
from sympy.functions.special.bessel import besseli as besseli, besselj as besselj, besselk as besselk, bessely as bessely
from sympy.functions.special.delta_functions import DiracDelta as DiracDelta, Heaviside as Heaviside
from sympy.functions.special.error_functions import Ei as Ei, erf as erf, erfc as erfc
from sympy.functions.special.gamma_functions import digamma as digamma, gamma as gamma, lowergamma as lowergamma
from sympy.integrals import Integral as Integral, integrate as integrate
from sympy.integrals.transforms import IntegralTransform as IntegralTransform, IntegralTransformError as IntegralTransformError
from sympy.logic.boolalg import And as And, Or as Or, conjuncts as conjuncts, disjuncts as disjuncts, to_cnf as to_cnf
from sympy.matrices.matrices import MatrixBase as MatrixBase
from sympy.polys.polyerrors import PolynomialError as PolynomialError
from sympy.polys.polyroots import roots as roots
from sympy.polys.polytools import Poly as Poly
from sympy.polys.rationaltools import together as together
from sympy.polys.rootoftools import RootSum as RootSum
from sympy.utilities.exceptions import SymPyDeprecationWarning as SymPyDeprecationWarning, ignore_warnings as ignore_warnings, sympy_deprecation_warning as sympy_deprecation_warning
from sympy.utilities.misc import debug as debug, debugf as debugf

def expand_dirac_delta(expr):
    """
    Expand an expression involving DiractDelta to get it as a linear
    combination of DiracDelta functions.
    """

class LaplaceTransform(IntegralTransform):
    """
    Class representing unevaluated Laplace transforms.

    For usage of this class, see the :class:`IntegralTransform` docstring.

    For how to compute Laplace transforms, see the :func:`laplace_transform`
    docstring.

    If this is called with ``.doit()``, it returns the Laplace transform as an
    expression. If it is called with ``.doit(noconds=False)``, it returns a
    tuple containing the same expression, a convergence plane, and conditions.
    """
    def doit(self, **hints):
        """
        Try to evaluate the transform in closed form.

        Explanation
        ===========

        Standard hints are the following:
        - ``noconds``:  if True, do not return convergence conditions. The
        default setting is `True`.
        - ``simplify``: if True, it simplifies the final result. The
        default setting is `False`.
        """

def laplace_transform(f, t, s, legacy_matrix: bool = True, **hints):
    """
    Compute the Laplace Transform `F(s)` of `f(t)`,

    .. math :: F(s) = \\int_{0^{-}}^\\infty e^{-st} f(t) \\mathrm{d}t.

    Explanation
    ===========

    For all sensible functions, this converges absolutely in a
    half-plane

    .. math :: a < \\operatorname{Re}(s)

    This function returns ``(F, a, cond)`` where ``F`` is the Laplace
    transform of ``f``, `a` is the half-plane of convergence, and `cond` are
    auxiliary convergence conditions.

    The implementation is rule-based, and if you are interested in which
    rules are applied, and whether integration is attempted, you can switch
    debug information on by setting ``sympy.SYMPY_DEBUG=True``. The numbers
    of the rules in the debug information (and the code) refer to Bateman's
    Tables of Integral Transforms [1].

    The lower bound is `0-`, meaning that this bound should be approached
    from the lower side. This is only necessary if distributions are involved.
    At present, it is only done if `f(t)` contains ``DiracDelta``, in which
    case the Laplace transform is computed implicitly as

    .. math ::
        F(s) = \\lim_{\\tau\\to 0^{-}} \\int_{\\tau}^\\infty e^{-st}
        f(t) \\mathrm{d}t

    by applying rules.

    If the Laplace transform cannot be fully computed in closed form, this
    function returns expressions containing unevaluated
    :class:`LaplaceTransform` objects.

    For a description of possible hints, refer to the docstring of
    :func:`sympy.integrals.transforms.IntegralTransform.doit`. If
    ``noconds=True``, only `F` will be returned (i.e. not ``cond``, and also
    not the plane ``a``).

    .. deprecated:: 1.9
        Legacy behavior for matrices where ``laplace_transform`` with
        ``noconds=False`` (the default) returns a Matrix whose elements are
        tuples. The behavior of ``laplace_transform`` for matrices will change
        in a future release of SymPy to return a tuple of the transformed
        Matrix and the convergence conditions for the matrix as a whole. Use
        ``legacy_matrix=False`` to enable the new behavior.

    Examples
    ========

    >>> from sympy import DiracDelta, exp, laplace_transform
    >>> from sympy.abc import t, s, a
    >>> laplace_transform(t**4, t, s)
    (24/s**5, 0, True)
    >>> laplace_transform(t**a, t, s)
    (gamma(a + 1)/(s*s**a), 0, re(a) > -1)
    >>> laplace_transform(DiracDelta(t)-a*exp(-a*t), t, s, simplify=True)
    (s/(a + s), -re(a), True)

    References
    ==========

    .. [1] Erdelyi, A. (ed.), Tables of Integral Transforms, Volume 1,
           Bateman Manuscript Prooject, McGraw-Hill (1954), available:
           https://resolver.caltech.edu/CaltechAUTHORS:20140123-101456353

    See Also
    ========

    inverse_laplace_transform, mellin_transform, fourier_transform
    hankel_transform, inverse_hankel_transform

    """

class InverseLaplaceTransform(IntegralTransform):
    """
    Class representing unevaluated inverse Laplace transforms.

    For usage of this class, see the :class:`IntegralTransform` docstring.

    For how to compute inverse Laplace transforms, see the
    :func:`inverse_laplace_transform` docstring.
    """
    def __new__(cls, F, s, x, plane, **opts): ...
    @property
    def fundamental_plane(self): ...
    def doit(self, **hints):
        """
        Try to evaluate the transform in closed form.

        Explanation
        ===========

        Standard hints are the following:
        - ``noconds``:  if True, do not return convergence conditions. The
        default setting is `True`.
        - ``simplify``: if True, it simplifies the final result. The
        default setting is `False`.
        """

def inverse_laplace_transform(F, s, t, plane: Incomplete | None = None, **hints):
    """
    Compute the inverse Laplace transform of `F(s)`, defined as

    .. math ::
        f(t) = \\frac{1}{2\\pi i} \\int_{c-i\\infty}^{c+i\\infty} e^{st}
        F(s) \\mathrm{d}s,

    for `c` so large that `F(s)` has no singularites in the
    half-plane `\\operatorname{Re}(s) > c-\\epsilon`.

    Explanation
    ===========

    The plane can be specified by
    argument ``plane``, but will be inferred if passed as None.

    Under certain regularity conditions, this recovers `f(t)` from its
    Laplace Transform `F(s)`, for non-negative `t`, and vice
    versa.

    If the integral cannot be computed in closed form, this function returns
    an unevaluated :class:`InverseLaplaceTransform` object.

    Note that this function will always assume `t` to be real,
    regardless of the SymPy assumption on `t`.

    For a description of possible hints, refer to the docstring of
    :func:`sympy.integrals.transforms.IntegralTransform.doit`.

    Examples
    ========

    >>> from sympy import inverse_laplace_transform, exp, Symbol
    >>> from sympy.abc import s, t
    >>> a = Symbol('a', positive=True)
    >>> inverse_laplace_transform(exp(-a*s)/s, s, t)
    Heaviside(-a + t)

    See Also
    ========

    laplace_transform
    hankel_transform, inverse_hankel_transform
    """
