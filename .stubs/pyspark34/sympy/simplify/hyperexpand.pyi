from _typeshed import Incomplete
from sympy import SYMPY_DEBUG as SYMPY_DEBUG
from sympy.core import Add as Add, Dummy as Dummy, EulerGamma as EulerGamma, Expr as Expr, I as I, Mul as Mul, Rational as Rational, S as S, Tuple as Tuple, expand as expand, expand_func as expand_func, nan as nan, oo as oo, pi as pi, symbols as symbols, sympify as sympify, zoo as zoo
from sympy.core.mod import Mod as Mod
from sympy.core.sorting import default_sort_key as default_sort_key
from sympy.functions import Chi as Chi, Ci as Ci, Ei as Ei, Piecewise as Piecewise, Shi as Shi, Si as Si, besseli as besseli, besselj as besselj, ceiling as ceiling, cos as cos, cosh as cosh, elliptic_e as elliptic_e, elliptic_k as elliptic_k, erf as erf, exp as exp, exp_polar as exp_polar, expint as expint, factorial as factorial, floor as floor, fresnelc as fresnelc, fresnels as fresnels, gamma as gamma, lerchphi as lerchphi, log as log, lowergamma as lowergamma, polar_lift as polar_lift, re as re, rf as rf, root as root, sin as sin, sinh as sinh, sqrt as sqrt, uppergamma as uppergamma
from sympy.functions.elementary.complexes import polarify as polarify, unpolarify as unpolarify
from sympy.functions.special.hyper import HyperRep_asin1 as HyperRep_asin1, HyperRep_asin2 as HyperRep_asin2, HyperRep_atanh as HyperRep_atanh, HyperRep_cosasin as HyperRep_cosasin, HyperRep_log1 as HyperRep_log1, HyperRep_log2 as HyperRep_log2, HyperRep_power1 as HyperRep_power1, HyperRep_power2 as HyperRep_power2, HyperRep_sinasin as HyperRep_sinasin, HyperRep_sqrts1 as HyperRep_sqrts1, HyperRep_sqrts2 as HyperRep_sqrts2, hyper as hyper, meijerg as meijerg
from sympy.matrices import Matrix as Matrix, eye as eye, zeros as zeros
from sympy.polys import Poly as Poly, apart as apart, poly as poly
from sympy.series import residue as residue
from sympy.simplify.powsimp import powdenest as powdenest
from sympy.utilities.iterables import sift as sift

def add_formulae(formulae):
    """ Create our knowledge base. """
def add_meijerg_formulae(formulae): ...
def make_simp(z):
    """ Create a function that simplifies rational functions in ``z``. """
def debug(*args) -> None: ...

class Hyper_Function(Expr):
    """ A generalized hypergeometric function. """
    def __new__(cls, ap, bq): ...
    @property
    def args(self): ...
    @property
    def sizes(self): ...
    @property
    def gamma(self):
        """
        Number of upper parameters that are negative integers

        This is a transformation invariant.
        """
    def __call__(self, arg): ...
    def build_invariants(self):
        """
        Compute the invariant vector.

        Explanation
        ===========

        The invariant vector is:
            (gamma, ((s1, n1), ..., (sk, nk)), ((t1, m1), ..., (tr, mr)))
        where gamma is the number of integer a < 0,
              s1 < ... < sk
              nl is the number of parameters a_i congruent to sl mod 1
              t1 < ... < tr
              ml is the number of parameters b_i congruent to tl mod 1

        If the index pair contains parameters, then this is not truly an
        invariant, since the parameters cannot be sorted uniquely mod1.

        Examples
        ========

        >>> from sympy.simplify.hyperexpand import Hyper_Function
        >>> from sympy import S
        >>> ap = (S.Half, S.One/3, S(-1)/2, -2)
        >>> bq = (1, 2)

        Here gamma = 1,
             k = 3, s1 = 0, s2 = 1/3, s3 = 1/2
                    n1 = 1, n2 = 1,   n2 = 2
             r = 1, t1 = 0
                    m1 = 2:

        >>> Hyper_Function(ap, bq).build_invariants()
        (1, ((0, 1), (1/3, 1), (1/2, 2)), ((0, 2),))
        """
    def difficulty(self, func):
        """ Estimate how many steps it takes to reach ``func`` from self.
            Return -1 if impossible. """

class G_Function(Expr):
    """ A Meijer G-function. """
    def __new__(cls, an, ap, bm, bq): ...
    @property
    def args(self): ...
    def __call__(self, z): ...
    def compute_buckets(self):
        """
        Compute buckets for the fours sets of parameters.

        Explanation
        ===========

        We guarantee that any two equal Mod objects returned are actually the
        same, and that the buckets are sorted by real part (an and bq
        descendending, bm and ap ascending).

        Examples
        ========

        >>> from sympy.simplify.hyperexpand import G_Function
        >>> from sympy.abc import y
        >>> from sympy import S

        >>> a, b = [1, 3, 2, S(3)/2], [1 + y, y, 2, y + 3]
        >>> G_Function(a, b, [2], [y]).compute_buckets()
        ({0: [3, 2, 1], 1/2: [3/2]},
        {0: [2], y: [y, y + 1, y + 3]}, {0: [2]}, {y: [y]})

        """
    @property
    def signature(self): ...

class Formula:
    """
    This class represents hypergeometric formulae.

    Explanation
    ===========

    Its data members are:
    - z, the argument
    - closed_form, the closed form expression
    - symbols, the free symbols (parameters) in the formula
    - func, the function
    - B, C, M (see _compute_basis)

    Examples
    ========

    >>> from sympy.abc import a, b, z
    >>> from sympy.simplify.hyperexpand import Formula, Hyper_Function
    >>> func = Hyper_Function((a/2, a/3 + b, (1+a)/2), (a, b, (a+b)/7))
    >>> f = Formula(func, z, None, [a, b])

    """
    z: Incomplete
    symbols: Incomplete
    B: Incomplete
    C: Incomplete
    M: Incomplete
    func: Incomplete
    def __init__(self, func, z, res, symbols, B: Incomplete | None = None, C: Incomplete | None = None, M: Incomplete | None = None) -> None: ...
    @property
    def closed_form(self): ...
    def find_instantiations(self, func):
        """
        Find substitutions of the free symbols that match ``func``.

        Return the substitution dictionaries as a list. Note that the returned
        instantiations need not actually match, or be valid!

        """

class FormulaCollection:
    """ A collection of formulae to use as origins. """
    symbolic_formulae: Incomplete
    concrete_formulae: Incomplete
    formulae: Incomplete
    def __init__(self) -> None:
        """ Doing this globally at module init time is a pain ... """
    def lookup_origin(self, func):
        """
        Given the suitable target ``func``, try to find an origin in our
        knowledge base.

        Examples
        ========

        >>> from sympy.simplify.hyperexpand import (FormulaCollection,
        ...     Hyper_Function)
        >>> f = FormulaCollection()
        >>> f.lookup_origin(Hyper_Function((), ())).closed_form
        exp(_z)
        >>> f.lookup_origin(Hyper_Function([1], ())).closed_form
        HyperRep_power1(-1, _z)

        >>> from sympy import S
        >>> i = Hyper_Function([S('1/4'), S('3/4 + 4')], [S.Half])
        >>> f.lookup_origin(i).closed_form
        HyperRep_sqrts1(-1/4, _z)
        """

class MeijerFormula:
    """
    This class represents a Meijer G-function formula.

    Its data members are:
    - z, the argument
    - symbols, the free symbols (parameters) in the formula
    - func, the function
    - B, C, M (c/f ordinary Formula)
    """
    func: Incomplete
    z: Incomplete
    symbols: Incomplete
    B: Incomplete
    C: Incomplete
    M: Incomplete
    def __init__(self, an, ap, bm, bq, z, symbols, B, C, M, matcher) -> None: ...
    @property
    def closed_form(self): ...
    def try_instantiate(self, func):
        """
        Try to instantiate the current formula to (almost) match func.
        This uses the _matcher passed on init.
        """

class MeijerFormulaCollection:
    """
    This class holds a collection of meijer g formulae.
    """
    formulae: Incomplete
    def __init__(self) -> None: ...
    def lookup_origin(self, func):
        """ Try to find a formula that matches func. """

class Operator:
    """
    Base class for operators to be applied to our functions.

    Explanation
    ===========

    These operators are differential operators. They are by convention
    expressed in the variable D = z*d/dz (although this base class does
    not actually care).
    Note that when the operator is applied to an object, we typically do
    *not* blindly differentiate but instead use a different representation
    of the z*d/dz operator (see make_derivative_operator).

    To subclass from this, define a __init__ method that initializes a
    self._poly variable. This variable stores a polynomial. By convention
    the generator is z*d/dz, and acts to the right of all coefficients.

    Thus this poly
        x**2 + 2*z*x + 1
    represents the differential operator
        (z*d/dz)**2 + 2*z**2*d/dz.

    This class is used only in the implementation of the hypergeometric
    function expansion algorithm.
    """
    def apply(self, obj, op):
        """
        Apply ``self`` to the object ``obj``, where the generator is ``op``.

        Examples
        ========

        >>> from sympy.simplify.hyperexpand import Operator
        >>> from sympy.polys.polytools import Poly
        >>> from sympy.abc import x, y, z
        >>> op = Operator()
        >>> op._poly = Poly(x**2 + z*x + y, x)
        >>> op.apply(z**7, lambda f: f.diff(z))
        y*z**7 + 7*z**7 + 42*z**5
        """

class MultOperator(Operator):
    ''' Simply multiply by a "constant" '''
    def __init__(self, p) -> None: ...

class ShiftA(Operator):
    """ Increment an upper index. """
    def __init__(self, ai) -> None: ...

class ShiftB(Operator):
    """ Decrement a lower index. """
    def __init__(self, bi) -> None: ...

class UnShiftA(Operator):
    """ Decrement an upper index. """
    def __init__(self, ap, bq, i, z) -> None:
        """ Note: i counts from zero! """

class UnShiftB(Operator):
    """ Increment a lower index. """
    def __init__(self, ap, bq, i, z) -> None:
        """ Note: i counts from zero! """

class MeijerShiftA(Operator):
    """ Increment an upper b index. """
    def __init__(self, bi) -> None: ...

class MeijerShiftB(Operator):
    """ Decrement an upper a index. """
    def __init__(self, bi) -> None: ...

class MeijerShiftC(Operator):
    """ Increment a lower b index. """
    def __init__(self, bi) -> None: ...

class MeijerShiftD(Operator):
    """ Decrement a lower a index. """
    def __init__(self, bi) -> None: ...

class MeijerUnShiftA(Operator):
    """ Decrement an upper b index. """
    def __init__(self, an, ap, bm, bq, i, z) -> None:
        """ Note: i counts from zero! """

class MeijerUnShiftB(Operator):
    """ Increment an upper a index. """
    def __init__(self, an, ap, bm, bq, i, z) -> None:
        """ Note: i counts from zero! """

class MeijerUnShiftC(Operator):
    """ Decrement a lower b index. """
    def __init__(self, an, ap, bm, bq, i, z) -> None:
        """ Note: i counts from zero! """

class MeijerUnShiftD(Operator):
    """ Increment a lower a index. """
    def __init__(self, an, ap, bm, bq, i, z) -> None:
        """ Note: i counts from zero! """

class ReduceOrder(Operator):
    """ Reduce Order by cancelling an upper and a lower index. """
    def __new__(cls, ai, bj):
        """ For convenience if reduction is not possible, return None. """
    @classmethod
    def meijer_minus(cls, b, a): ...
    @classmethod
    def meijer_plus(cls, a, b): ...

def reduce_order(func):
    """
    Given the hypergeometric function ``func``, find a sequence of operators to
    reduces order as much as possible.

    Explanation
    ===========

    Return (newfunc, [operators]), where applying the operators to the
    hypergeometric function newfunc yields func.

    Examples
    ========

    >>> from sympy.simplify.hyperexpand import reduce_order, Hyper_Function
    >>> reduce_order(Hyper_Function((1, 2), (3, 4)))
    (Hyper_Function((1, 2), (3, 4)), [])
    >>> reduce_order(Hyper_Function((1,), (1,)))
    (Hyper_Function((), ()), [<Reduce order by cancelling upper 1 with lower 1.>])
    >>> reduce_order(Hyper_Function((2, 4), (3, 3)))
    (Hyper_Function((2,), (3,)), [<Reduce order by cancelling
    upper 4 with lower 3.>])
    """
def reduce_order_meijer(func):
    """
    Given the Meijer G function parameters, ``func``, find a sequence of
    operators that reduces order as much as possible.

    Return newfunc, [operators].

    Examples
    ========

    >>> from sympy.simplify.hyperexpand import (reduce_order_meijer,
    ...                                         G_Function)
    >>> reduce_order_meijer(G_Function([3, 4], [5, 6], [3, 4], [1, 2]))[0]
    G_Function((4, 3), (5, 6), (3, 4), (2, 1))
    >>> reduce_order_meijer(G_Function([3, 4], [5, 6], [3, 4], [1, 8]))[0]
    G_Function((3,), (5, 6), (3, 4), (1,))
    >>> reduce_order_meijer(G_Function([3, 4], [5, 6], [7, 5], [1, 5]))[0]
    G_Function((3,), (), (), (1,))
    >>> reduce_order_meijer(G_Function([3, 4], [5, 6], [7, 5], [5, 3]))[0]
    G_Function((), (), (), ())
    """
def make_derivative_operator(M, z):
    """ Create a derivative operator, to be passed to Operator.apply. """
def apply_operators(obj, ops, op):
    """
    Apply the list of operators ``ops`` to object ``obj``, substituting
    ``op`` for the generator.
    """
def devise_plan(target, origin, z):
    """
    Devise a plan (consisting of shift and un-shift operators) to be applied
    to the hypergeometric function ``target`` to yield ``origin``.
    Returns a list of operators.

    Examples
    ========

    >>> from sympy.simplify.hyperexpand import devise_plan, Hyper_Function
    >>> from sympy.abc import z

    Nothing to do:

    >>> devise_plan(Hyper_Function((1, 2), ()), Hyper_Function((1, 2), ()), z)
    []
    >>> devise_plan(Hyper_Function((), (1, 2)), Hyper_Function((), (1, 2)), z)
    []

    Very simple plans:

    >>> devise_plan(Hyper_Function((2,), ()), Hyper_Function((1,), ()), z)
    [<Increment upper 1.>]
    >>> devise_plan(Hyper_Function((), (2,)), Hyper_Function((), (1,)), z)
    [<Increment lower index #0 of [], [1].>]

    Several buckets:

    >>> from sympy import S
    >>> devise_plan(Hyper_Function((1, S.Half), ()),
    ...             Hyper_Function((2, S('3/2')), ()), z) #doctest: +NORMALIZE_WHITESPACE
    [<Decrement upper index #0 of [3/2, 1], [].>,
    <Decrement upper index #0 of [2, 3/2], [].>]

    A slightly more complicated plan:

    >>> devise_plan(Hyper_Function((1, 3), ()), Hyper_Function((2, 2), ()), z)
    [<Increment upper 2.>, <Decrement upper index #0 of [2, 2], [].>]

    Another more complicated plan: (note that the ap have to be shifted first!)

    >>> devise_plan(Hyper_Function((1, -1), (2,)), Hyper_Function((3, -2), (4,)), z)
    [<Decrement lower 3.>, <Decrement lower 4.>,
    <Decrement upper index #1 of [-1, 2], [4].>,
    <Decrement upper index #1 of [-1, 3], [4].>, <Increment upper -2.>]
    """
def try_shifted_sum(func, z):
    """ Try to recognise a hypergeometric sum that starts from k > 0. """
def try_polynomial(func, z):
    """ Recognise polynomial cases. Returns None if not such a case.
        Requires order to be fully reduced. """
def try_lerchphi(func):
    """
    Try to find an expression for Hyper_Function ``func`` in terms of Lerch
    Transcendents.

    Return None if no such expression can be found.
    """
def build_hypergeometric_formula(func):
    """
    Create a formula object representing the hypergeometric function ``func``.

    """
def hyperexpand_special(ap, bq, z):
    '''
    Try to find a closed-form expression for hyper(ap, bq, z), where ``z``
    is supposed to be a "special" value, e.g. 1.

    This function tries various of the classical summation formulae
    (Gauss, Saalschuetz, etc).
    '''
def devise_plan_meijer(fro, to, z):
    """
    Find operators to convert G-function ``fro`` into G-function ``to``.

    Explanation
    ===========

    It is assumed that ``fro`` and ``to`` have the same signatures, and that in fact
    any corresponding pair of parameters differs by integers, and a direct path
    is possible. I.e. if there are parameters a1 b1 c1  and a2 b2 c2 it is
    assumed that a1 can be shifted to a2, etc. The only thing this routine
    determines is the order of shifts to apply, nothing clever will be tried.
    It is also assumed that ``fro`` is suitable.

    Examples
    ========

    >>> from sympy.simplify.hyperexpand import (devise_plan_meijer,
    ...                                         G_Function)
    >>> from sympy.abc import z

    Empty plan:

    >>> devise_plan_meijer(G_Function([1], [2], [3], [4]),
    ...                    G_Function([1], [2], [3], [4]), z)
    []

    Very simple plans:

    >>> devise_plan_meijer(G_Function([0], [], [], []),
    ...                    G_Function([1], [], [], []), z)
    [<Increment upper a index #0 of [0], [], [], [].>]
    >>> devise_plan_meijer(G_Function([0], [], [], []),
    ...                    G_Function([-1], [], [], []), z)
    [<Decrement upper a=0.>]
    >>> devise_plan_meijer(G_Function([], [1], [], []),
    ...                    G_Function([], [2], [], []), z)
    [<Increment lower a index #0 of [], [1], [], [].>]

    Slightly more complicated plans:

    >>> devise_plan_meijer(G_Function([0], [], [], []),
    ...                    G_Function([2], [], [], []), z)
    [<Increment upper a index #0 of [1], [], [], [].>,
    <Increment upper a index #0 of [0], [], [], [].>]
    >>> devise_plan_meijer(G_Function([0], [], [0], []),
    ...                    G_Function([-1], [], [1], []), z)
    [<Increment upper b=0.>, <Decrement upper a=0.>]

    Order matters:

    >>> devise_plan_meijer(G_Function([0], [], [0], []),
    ...                    G_Function([1], [], [1], []), z)
    [<Increment upper a index #0 of [0], [], [1], [].>, <Increment upper b=0.>]
    """
def hyperexpand(f, allow_hyper: bool = False, rewrite: str = 'default', place: Incomplete | None = None):
    """
    Expand hypergeometric functions. If allow_hyper is True, allow partial
    simplification (that is a result different from input,
    but still containing hypergeometric functions).

    If a G-function has expansions both at zero and at infinity,
    ``place`` can be set to ``0`` or ``zoo`` to indicate the
    preferred choice.

    Examples
    ========

    >>> from sympy.simplify.hyperexpand import hyperexpand
    >>> from sympy.functions import hyper
    >>> from sympy.abc import z
    >>> hyperexpand(hyper([], [], z))
    exp(z)

    Non-hyperegeometric parts of the expression and hypergeometric expressions
    that are not recognised are left unchanged:

    >>> hyperexpand(1 + hyper([1, 1, 1], [], z))
    hyper((1, 1, 1), (), z) + 1
    """
