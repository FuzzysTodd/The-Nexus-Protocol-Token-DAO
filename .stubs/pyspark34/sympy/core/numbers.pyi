import math
from .add import Add as Add
from .basic import Basic as Basic
from .cache import cacheit as cacheit, clear_cache as clear_cache
from .containers import Tuple as Tuple
from .evalf import pure_complex as pure_complex
from .expr import AtomicExpr as AtomicExpr, Expr as Expr
from .kind import NumberKind as NumberKind
from .logic import fuzzy_not as fuzzy_not
from .mul import Mul as Mul
from .parameters import global_parameters as global_parameters
from .power import Pow as Pow, integer_nthroot as integer_nthroot
from .singleton import S as S, Singleton as Singleton
from .sympify import SympifyError as SympifyError, sympify as sympify
from _typeshed import Incomplete
from sympy.external.gmpy import HAS_GMPY as HAS_GMPY, SYMPY_INTS as SYMPY_INTS, gmpy as gmpy
from sympy.multipledispatch import dispatch as dispatch
from sympy.utilities.misc import as_int as as_int, debug as debug, filldedent as filldedent

def comp(z1, z2, tol: Incomplete | None = None):
    """Return a bool indicating whether the error between z1 and z2
    is $\\le$ ``tol``.

    Examples
    ========

    If ``tol`` is ``None`` then ``True`` will be returned if
    :math:`|z1 - z2|\\times 10^p \\le 5` where $p$ is minimum value of the
    decimal precision of each value.

    >>> from sympy import comp, pi
    >>> pi4 = pi.n(4); pi4
    3.142
    >>> comp(_, 3.142)
    True
    >>> comp(pi4, 3.141)
    False
    >>> comp(pi4, 3.143)
    False

    A comparison of strings will be made
    if ``z1`` is a Number and ``z2`` is a string or ``tol`` is ''.

    >>> comp(pi4, 3.1415)
    True
    >>> comp(pi4, 3.1415, '')
    False

    When ``tol`` is provided and $z2$ is non-zero and
    :math:`|z1| > 1` the error is normalized by :math:`|z1|`:

    >>> abs(pi4 - 3.14)/pi4
    0.000509791731426756
    >>> comp(pi4, 3.14, .001)  # difference less than 0.1%
    True
    >>> comp(pi4, 3.14, .0005)  # difference less than 0.1%
    False

    When :math:`|z1| \\le 1` the absolute error is used:

    >>> 1/pi4
    0.3183
    >>> abs(1/pi4 - 0.3183)/(1/pi4)
    3.07371499106316e-5
    >>> abs(1/pi4 - 0.3183)
    9.78393554684764e-6
    >>> comp(1/pi4, 0.3183, 1e-5)
    True

    To see if the absolute error between ``z1`` and ``z2`` is less
    than or equal to ``tol``, call this as ``comp(z1 - z2, 0, tol)``
    or ``comp(z1 - z2, tol=tol)``:

    >>> abs(pi4 - 3.14)
    0.00160156249999988
    >>> comp(pi4 - 3.14, 0, .002)
    True
    >>> comp(pi4 - 3.14, 0, .001)
    False
    """
def mpf_norm(mpf, prec):
    '''Return the mpf tuple normalized appropriately for the indicated
    precision after doing a check to see if zero should be returned or
    not when the mantissa is 0. ``mpf_normlize`` always assumes that this
    is zero, but it may not be since the mantissa for mpf\'s values "+inf",
    "-inf" and "nan" have a mantissa of zero, too.

    Note: this is not intended to validate a given mpf tuple, so sending
    mpf tuples that were not created by mpmath may produce bad results. This
    is only a wrapper to ``mpf_normalize`` which provides the check for non-
    zero mpfs that have a 0 for the mantissa.
    '''
def seterr(divide: bool = False) -> None:
    """
    Should SymPy raise an exception on 0/0 or return a nan?

    divide == True .... raise an exception
    divide == False ... return nan
    """
def igcd(*args):
    """Computes nonnegative integer greatest common divisor.

    Explanation
    ===========

    The algorithm is based on the well known Euclid's algorithm [1]_. To
    improve speed, ``igcd()`` has its own caching mechanism.

    Examples
    ========

    >>> from sympy import igcd
    >>> igcd(2, 4)
    2
    >>> igcd(5, 10, 15)
    5

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Euclidean_algorithm

    """
igcd2 = math.gcd

def igcd_lehmer(a, b):
    """Computes greatest common divisor of two integers.

    Explanation
    ===========

    Euclid's algorithm for the computation of the greatest
    common divisor ``gcd(a, b)``  of two (positive) integers
    $a$ and $b$ is based on the division identity
       $$ a = q \\times b + r$$,
    where the quotient  $q$  and the remainder  $r$  are integers
    and  $0 \\le r < b$. Then each common divisor of  $a$  and  $b$
    divides  $r$, and it follows that  ``gcd(a, b) == gcd(b, r)``.
    The algorithm works by constructing the sequence
    r0, r1, r2, ..., where  r0 = a, r1 = b,  and each  rn
    is the remainder from the division of the two preceding
    elements.

    In Python, ``q = a // b``  and  ``r = a % b``  are obtained by the
    floor division and the remainder operations, respectively.
    These are the most expensive arithmetic operations, especially
    for large  a  and  b.

    Lehmer's algorithm [1]_ is based on the observation that the quotients
    ``qn = r(n-1) // rn``  are in general small integers even
    when  a  and  b  are very large. Hence the quotients can be
    usually determined from a relatively small number of most
    significant bits.

    The efficiency of the algorithm is further enhanced by not
    computing each long remainder in Euclid's sequence. The remainders
    are linear combinations of  a  and  b  with integer coefficients
    derived from the quotients. The coefficients can be computed
    as far as the quotients can be determined from the chosen
    most significant parts of  a  and  b. Only then a new pair of
    consecutive remainders is computed and the algorithm starts
    anew with this pair.

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Lehmer%27s_GCD_algorithm

    """
def ilcm(*args):
    """Computes integer least common multiple.

    Examples
    ========

    >>> from sympy import ilcm
    >>> ilcm(5, 10)
    10
    >>> ilcm(7, 3)
    21
    >>> ilcm(5, 10, 15)
    30

    """
def igcdex(a, b):
    """Returns x, y, g such that g = x*a + y*b = gcd(a, b).

    Examples
    ========

    >>> from sympy.core.numbers import igcdex
    >>> igcdex(2, 3)
    (-1, 1, 1)
    >>> igcdex(10, 12)
    (-1, 1, 2)

    >>> x, y, g = igcdex(100, 2004)
    >>> x, y, g
    (-20, 1, 4)
    >>> x*100 + y*2004
    4

    """
def mod_inverse(a, m):
    """
    Return the number $c$ such that, $a \\times c = 1 \\pmod{m}$
    where $c$ has the same sign as $m$. If no such value exists,
    a ValueError is raised.

    Examples
    ========

    >>> from sympy import mod_inverse, S

    Suppose we wish to find multiplicative inverse $x$ of
    3 modulo 11. This is the same as finding $x$ such
    that $3x = 1 \\pmod{11}$. One value of x that satisfies
    this congruence is 4. Because $3 \\times 4 = 12$ and $12 = 1 \\pmod{11}$.
    This is the value returned by ``mod_inverse``:

    >>> mod_inverse(3, 11)
    4
    >>> mod_inverse(-3, 11)
    7

    When there is a common factor between the numerators of
    `a` and `m` the inverse does not exist:

    >>> mod_inverse(2, 4)
    Traceback (most recent call last):
    ...
    ValueError: inverse of 2 mod 4 does not exist

    >>> mod_inverse(S(2)/7, S(5)/2)
    7/2

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Modular_multiplicative_inverse
    .. [2] https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
    """

class Number(AtomicExpr):
    """Represents atomic numbers in SymPy.

    Explanation
    ===========

    Floating point numbers are represented by the Float class.
    Rational numbers (of any size) are represented by the Rational class.
    Integer numbers (of any size) are represented by the Integer class.
    Float and Rational are subclasses of Number; Integer is a subclass
    of Rational.

    For example, ``2/3`` is represented as ``Rational(2, 3)`` which is
    a different object from the floating point number obtained with
    Python division ``2/3``. Even for numbers that are exactly
    represented in binary, there is a difference between how two forms,
    such as ``Rational(1, 2)`` and ``Float(0.5)``, are used in SymPy.
    The rational form is to be preferred in symbolic computations.

    Other kinds of numbers, such as algebraic numbers ``sqrt(2)`` or
    complex numbers ``3 + 4*I``, are not instances of Number class as
    they are not atomic.

    See Also
    ========

    Float, Integer, Rational
    """
    is_commutative: bool
    is_number: bool
    is_Number: bool
    kind = NumberKind
    def __new__(cls, *obj): ...
    def could_extract_minus_sign(self): ...
    def invert(self, other, *gens, **args): ...
    def __divmod__(self, other): ...
    def __rdivmod__(self, other): ...
    def __float__(self) -> float: ...
    def floor(self) -> None: ...
    def ceiling(self) -> None: ...
    def __floor__(self) -> int: ...
    def __ceil__(self) -> int: ...
    @classmethod
    def class_key(cls): ...
    def sort_key(self, order: Incomplete | None = None): ...
    def __add__(self, other): ...
    def __sub__(self, other): ...
    def __mul__(self, other): ...
    def __truediv__(self, other): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...
    def __hash__(self): ...
    def is_constant(self, *wrt, **flags): ...
    def as_coeff_mul(self, *deps, rational: bool = True, **kwargs): ...
    def as_coeff_add(self, *deps): ...
    def as_coeff_Mul(self, rational: bool = False):
        """Efficiently extract the coefficient of a product."""
    def as_coeff_Add(self, rational: bool = False):
        """Efficiently extract the coefficient of a summation."""
    def gcd(self, other):
        """Compute GCD of `self` and `other`. """
    def lcm(self, other):
        """Compute LCM of `self` and `other`. """
    def cofactors(self, other):
        """Compute GCD and cofactors of `self` and `other`. """

class Float(Number):
    '''Represent a floating-point number of arbitrary precision.

    Examples
    ========

    >>> from sympy import Float
    >>> Float(3.5)
    3.50000000000000
    >>> Float(3)
    3.00000000000000

    Creating Floats from strings (and Python ``int`` and ``long``
    types) will give a minimum precision of 15 digits, but the
    precision will automatically increase to capture all digits
    entered.

    >>> Float(1)
    1.00000000000000
    >>> Float(10**20)
    100000000000000000000.
    >>> Float(\'1e20\')
    100000000000000000000.

    However, *floating-point* numbers (Python ``float`` types) retain
    only 15 digits of precision:

    >>> Float(1e20)
    1.00000000000000e+20
    >>> Float(1.23456789123456789)
    1.23456789123457

    It may be preferable to enter high-precision decimal numbers
    as strings:

    >>> Float(\'1.23456789123456789\')
    1.23456789123456789

    The desired number of digits can also be specified:

    >>> Float(\'1e-3\', 3)
    0.00100
    >>> Float(100, 4)
    100.0

    Float can automatically count significant figures if a null string
    is sent for the precision; spaces or underscores are also allowed. (Auto-
    counting is only allowed for strings, ints and longs).

    >>> Float(\'123 456 789.123_456\', \'\')
    123456789.123456
    >>> Float(\'12e-3\', \'\')
    0.012
    >>> Float(3, \'\')
    3.

    If a number is written in scientific notation, only the digits before the
    exponent are considered significant if a decimal appears, otherwise the
    "e" signifies only how to move the decimal:

    >>> Float(\'60.e2\', \'\')  # 2 digits significant
    6.0e+3
    >>> Float(\'60e2\', \'\')  # 4 digits significant
    6000.
    >>> Float(\'600e-2\', \'\')  # 3 digits significant
    6.00

    Notes
    =====

    Floats are inexact by their nature unless their value is a binary-exact
    value.

    >>> approx, exact = Float(.1, 1), Float(.125, 1)

    For calculation purposes, evalf needs to be able to change the precision
    but this will not increase the accuracy of the inexact value. The
    following is the most accurate 5-digit approximation of a value of 0.1
    that had only 1 digit of precision:

    >>> approx.evalf(5)
    0.099609

    By contrast, 0.125 is exact in binary (as it is in base 10) and so it
    can be passed to Float or evalf to obtain an arbitrary precision with
    matching accuracy:

    >>> Float(exact, 5)
    0.12500
    >>> exact.evalf(20)
    0.12500000000000000000

    Trying to make a high-precision Float from a float is not disallowed,
    but one must keep in mind that the *underlying float* (not the apparent
    decimal value) is being obtained with high precision. For example, 0.3
    does not have a finite binary representation. The closest rational is
    the fraction 5404319552844595/2**54. So if you try to obtain a Float of
    0.3 to 20 digits of precision you will not see the same thing as 0.3
    followed by 19 zeros:

    >>> Float(0.3, 20)
    0.29999999999999998890

    If you want a 20-digit value of the decimal 0.3 (not the floating point
    approximation of 0.3) you should send the 0.3 as a string. The underlying
    representation is still binary but a higher precision than Python\'s float
    is used:

    >>> Float(\'0.3\', 20)
    0.30000000000000000000

    Although you can increase the precision of an existing Float using Float
    it will not increase the accuracy -- the underlying value is not changed:

    >>> def show(f): # binary rep of Float
    ...     from sympy import Mul, Pow
    ...     s, m, e, b = f._mpf_
    ...     v = Mul(int(m), Pow(2, int(e), evaluate=False), evaluate=False)
    ...     print(\'%s at prec=%s\' % (v, f._prec))
    ...
    >>> t = Float(\'0.3\', 3)
    >>> show(t)
    4915/2**14 at prec=13
    >>> show(Float(t, 20)) # higher prec, not higher accuracy
    4915/2**14 at prec=70
    >>> show(Float(t, 2)) # lower prec
    307/2**10 at prec=10

    The same thing happens when evalf is used on a Float:

    >>> show(t.evalf(20))
    4915/2**14 at prec=70
    >>> show(t.evalf(2))
    307/2**10 at prec=10

    Finally, Floats can be instantiated with an mpf tuple (n, c, p) to
    produce the number (-1)**n*c*2**p:

    >>> n, c, p = 1, 5, 0
    >>> (-1)**n*c*2**p
    -5
    >>> Float((1, 5, 0))
    -5.00000000000000

    An actual mpf tuple also contains the number of bits in c as the last
    element of the tuple:

    >>> _._mpf_
    (1, 5, 0, 3)

    This is not needed for instantiation and is not the same thing as the
    precision. The mpf tuple and the precision are two separate quantities
    that Float tracks.

    In SymPy, a Float is a number that can be computed with arbitrary
    precision. Although floating point \'inf\' and \'nan\' are not such
    numbers, Float can create these numbers:

    >>> Float(\'-inf\')
    -oo
    >>> _.is_Float
    False

    Zero in Float only has a single value. Values are not separate for
    positive and negative zeroes.
    '''
    is_rational: Incomplete
    is_irrational: Incomplete
    is_number: bool
    is_real: bool
    is_extended_real: bool
    is_Float: bool
    def __new__(cls, num, dps: Incomplete | None = None, precision: Incomplete | None = None): ...
    def __getnewargs_ex__(self): ...
    def floor(self): ...
    def ceiling(self): ...
    def __floor__(self) -> int: ...
    def __ceil__(self) -> int: ...
    @property
    def num(self): ...
    def __bool__(self) -> bool: ...
    def __neg__(self): ...
    def __add__(self, other): ...
    def __sub__(self, other): ...
    def __mul__(self, other): ...
    def __truediv__(self, other): ...
    def __mod__(self, other): ...
    def __rmod__(self, other): ...
    def __abs__(self): ...
    def __int__(self) -> int: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __hash__(self): ...
    def epsilon_eq(self, other, epsilon: str = '1e-15'): ...
    def __format__(self, format_spec) -> str: ...
RealNumber = Float

class Rational(Number):
    '''Represents rational numbers (p/q) of any size.

    Examples
    ========

    >>> from sympy import Rational, nsimplify, S, pi
    >>> Rational(1, 2)
    1/2

    Rational is unprejudiced in accepting input. If a float is passed, the
    underlying value of the binary representation will be returned:

    >>> Rational(.5)
    1/2
    >>> Rational(.2)
    3602879701896397/18014398509481984

    If the simpler representation of the float is desired then consider
    limiting the denominator to the desired value or convert the float to
    a string (which is roughly equivalent to limiting the denominator to
    10**12):

    >>> Rational(str(.2))
    1/5
    >>> Rational(.2).limit_denominator(10**12)
    1/5

    An arbitrarily precise Rational is obtained when a string literal is
    passed:

    >>> Rational("1.23")
    123/100
    >>> Rational(\'1e-2\')
    1/100
    >>> Rational(".1")
    1/10
    >>> Rational(\'1e-2/3.2\')
    1/320

    The conversion of other types of strings can be handled by
    the sympify() function, and conversion of floats to expressions
    or simple fractions can be handled with nsimplify:

    >>> S(\'.[3]\')  # repeating digits in brackets
    1/3
    >>> S(\'3**2/10\')  # general expressions
    9/10
    >>> nsimplify(.3)  # numbers that have a simple form
    3/10

    But if the input does not reduce to a literal Rational, an error will
    be raised:

    >>> Rational(pi)
    Traceback (most recent call last):
    ...
    TypeError: invalid input: pi


    Low-level
    ---------

    Access numerator and denominator as .p and .q:

    >>> r = Rational(3, 4)
    >>> r
    3/4
    >>> r.p
    3
    >>> r.q
    4

    Note that p and q return integers (not SymPy Integers) so some care
    is needed when using them in expressions:

    >>> r.p/r.q
    0.75

    If an unevaluated Rational is desired, ``gcd=1`` can be passed and
    this will keep common divisors of the numerator and denominator
    from being eliminated. It is not possible, however, to leave a
    negative value in the denominator.

    >>> Rational(2, 4, gcd=1)
    2/4
    >>> Rational(2, -4, gcd=1).q
    4

    See Also
    ========
    sympy.core.sympify.sympify, sympy.simplify.simplify.nsimplify
    '''
    is_real: bool
    is_integer: bool
    is_rational: bool
    is_number: bool
    p: int
    q: int
    is_Rational: bool
    def __new__(cls, p, q: Incomplete | None = None, gcd: Incomplete | None = None): ...
    def limit_denominator(self, max_denominator: int = 1000000):
        """Closest Rational to self with denominator at most max_denominator.

        Examples
        ========

        >>> from sympy import Rational
        >>> Rational('3.141592653589793').limit_denominator(10)
        22/7
        >>> Rational('3.141592653589793').limit_denominator(100)
        311/99

        """
    def __getnewargs__(self): ...
    def __neg__(self): ...
    def __add__(self, other): ...
    __radd__ = __add__
    def __sub__(self, other): ...
    def __rsub__(self, other): ...
    def __mul__(self, other): ...
    __rmul__ = __mul__
    def __truediv__(self, other): ...
    def __rtruediv__(self, other): ...
    def __mod__(self, other): ...
    def __rmod__(self, other): ...
    def __abs__(self): ...
    def __int__(self) -> int: ...
    def floor(self): ...
    def ceiling(self): ...
    def __floor__(self) -> int: ...
    def __ceil__(self) -> int: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __hash__(self): ...
    def factors(self, limit: Incomplete | None = None, use_trial: bool = True, use_rho: bool = False, use_pm1: bool = False, verbose: bool = False, visual: bool = False):
        """A wrapper to factorint which return factors of self that are
        smaller than limit (or cheap to compute). Special methods of
        factoring are disabled by default so that only trial division is used.
        """
    @property
    def numerator(self): ...
    @property
    def denominator(self): ...
    def gcd(self, other): ...
    def lcm(self, other): ...
    def as_numer_denom(self): ...
    def as_content_primitive(self, radical: bool = False, clear: bool = True):
        """Return the tuple (R, self/R) where R is the positive Rational
        extracted from self.

        Examples
        ========

        >>> from sympy import S
        >>> (S(-3)/2).as_content_primitive()
        (3/2, -1)

        See docstring of Expr.as_content_primitive for more examples.
        """
    def as_coeff_Mul(self, rational: bool = False):
        """Efficiently extract the coefficient of a product."""
    def as_coeff_Add(self, rational: bool = False):
        """Efficiently extract the coefficient of a summation."""

class Integer(Rational):
    '''Represents integer numbers of any size.

    Examples
    ========

    >>> from sympy import Integer
    >>> Integer(3)
    3

    If a float or a rational is passed to Integer, the fractional part
    will be discarded; the effect is of rounding toward zero.

    >>> Integer(3.8)
    3
    >>> Integer(-3.8)
    -3

    A string is acceptable input if it can be parsed as an integer:

    >>> Integer("9" * 20)
    99999999999999999999

    It is rarely needed to explicitly instantiate an Integer, because
    Python integers are automatically converted to Integer when they
    are used in SymPy expressions.
    '''
    q: int
    is_integer: bool
    is_number: bool
    is_Integer: bool
    def __new__(cls, i): ...
    def __getnewargs__(self): ...
    def __int__(self) -> int: ...
    def floor(self): ...
    def ceiling(self): ...
    def __floor__(self) -> int: ...
    def __ceil__(self) -> int: ...
    def __neg__(self): ...
    def __abs__(self): ...
    def __divmod__(self, other): ...
    def __rdivmod__(self, other): ...
    def __add__(self, other): ...
    def __radd__(self, other): ...
    def __sub__(self, other): ...
    def __rsub__(self, other): ...
    def __mul__(self, other): ...
    def __rmul__(self, other): ...
    def __mod__(self, other): ...
    def __rmod__(self, other): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __gt__(self, other): ...
    def __lt__(self, other): ...
    def __ge__(self, other): ...
    def __le__(self, other): ...
    def __hash__(self): ...
    def __index__(self) -> int: ...
    def as_numer_denom(self): ...
    def __floordiv__(self, other): ...
    def __rfloordiv__(self, other): ...
    def __lshift__(self, other): ...
    def __rlshift__(self, other): ...
    def __rshift__(self, other): ...
    def __rrshift__(self, other): ...
    def __and__(self, other): ...
    def __rand__(self, other): ...
    def __xor__(self, other): ...
    def __rxor__(self, other): ...
    def __or__(self, other): ...
    def __ror__(self, other): ...
    def __invert__(self): ...

class AlgebraicNumber(Expr):
    """
    Class for representing algebraic numbers in SymPy.

    Symbolically, an instance of this class represents an element
    $\\alpha \\in \\mathbb{Q}(\\theta) \\hookrightarrow \\mathbb{C}$. That is, the
    algebraic number $\\alpha$ is represented as an element of a particular
    number field $\\mathbb{Q}(\\theta)$, with a particular embedding of this
    field into the complex numbers.

    Formally, the primitive element $\\theta$ is given by two data points: (1)
    its minimal polynomial (which defines $\\mathbb{Q}(\\theta)$), and (2) a
    particular complex number that is a root of this polynomial (which defines
    the embedding $\\mathbb{Q}(\\theta) \\hookrightarrow \\mathbb{C}$). Finally,
    the algebraic number $\\alpha$ which we represent is then given by the
    coefficients of a polynomial in $\\theta$.
    """
    is_AlgebraicNumber: bool
    is_algebraic: bool
    is_number: bool
    kind = NumberKind
    free_symbols: set[Basic]
    def __new__(cls, expr, coeffs: Incomplete | None = None, alias: Incomplete | None = None, **args):
        """
        Construct a new algebraic number $\\alpha$ belonging to a number field
        $k = \\mathbb{Q}(\\theta)$.

        There are four instance attributes to be determined:

        ===========  ============================================================================
        Attribute    Type/Meaning
        ===========  ============================================================================
        ``root``     :py:class:`~.Expr` for $\\theta$ as a complex number
        ``minpoly``  :py:class:`~.Poly`, the minimal polynomial of $\\theta$
        ``rep``      :py:class:`~sympy.polys.polyclasses.DMP` giving $\\alpha$ as poly in $\\theta$
        ``alias``    :py:class:`~.Symbol` for $\\theta$, or ``None``
        ===========  ============================================================================

        See Parameters section for how they are determined.

        Parameters
        ==========

        expr : :py:class:`~.Expr`, or pair $(m, r)$
            There are three distinct modes of construction, depending on what
            is passed as *expr*.

            **(1)** *expr* is an :py:class:`~.AlgebraicNumber`:
            In this case we begin by copying all four instance attributes from
            *expr*. If *coeffs* were also given, we compose the two coeff
            polynomials (see below). If an *alias* was given, it overrides.

            **(2)** *expr* is any other type of :py:class:`~.Expr`:
            Then ``root`` will equal *expr*. Therefore it
            must express an algebraic quantity, and we will compute its
            ``minpoly``.

            **(3)** *expr* is an ordered pair $(m, r)$ giving the
            ``minpoly`` $m$, and a ``root`` $r$ thereof, which together
            define $\\theta$. In this case $m$ may be either a univariate
            :py:class:`~.Poly` or any :py:class:`~.Expr` which represents the
            same, while $r$ must be some :py:class:`~.Expr` representing a
            complex number that is a root of $m$, including both explicit
            expressions in radicals, and instances of
            :py:class:`~.ComplexRootOf` or :py:class:`~.AlgebraicNumber`.

        coeffs : list, :py:class:`~.ANP`, None, optional (default=None)
            This defines ``rep``, giving the algebraic number $\\alpha$ as a
            polynomial in $\\theta$.

            If a list, the elements should be integers or rational numbers.
            If an :py:class:`~.ANP`, we take its coefficients (using its
            :py:meth:`~.ANP.to_list()` method). If ``None``, then the list of
            coefficients defaults to ``[1, 0]``, meaning that $\\alpha = \\theta$
            is the primitive element of the field.

            If *expr* was an :py:class:`~.AlgebraicNumber`, let $g(x)$ be its
            ``rep`` polynomial, and let $f(x)$ be the polynomial defined by
            *coeffs*. Then ``self.rep`` will represent the composition
            $(f \\circ g)(x)$.

        alias : str, :py:class:`~.Symbol`, None, optional (default=None)
            This is a way to provide a name for the primitive element. We
            described several ways in which the *expr* argument can define the
            value of the primitive element, but none of these methods gave it
            a name. Here, for example, *alias* could be set as
            ``Symbol('theta')``, in order to make this symbol appear when
            $\\alpha$ is printed, or rendered as a polynomial, using the
            :py:meth:`~.as_poly()` method.

        Examples
        ========

        Recall that we are constructing an algebraic number as a field element
        $\\alpha \\in \\mathbb{Q}(\\theta)$.

        >>> from sympy import AlgebraicNumber, sqrt, CRootOf, S
        >>> from sympy.abc import x

        Example (1): $\\alpha = \\theta = \\sqrt{2}$

        >>> a1 = AlgebraicNumber(sqrt(2))
        >>> a1.minpoly_of_element().as_expr(x)
        x**2 - 2
        >>> a1.evalf(10)
        1.414213562

        Example (2): $\\alpha = 3 \\sqrt{2} - 5$, $\\theta = \\sqrt{2}$. We can
        either build on the last example:

        >>> a2 = AlgebraicNumber(a1, [3, -5])
        >>> a2.as_expr()
        -5 + 3*sqrt(2)

        or start from scratch:

        >>> a2 = AlgebraicNumber(sqrt(2), [3, -5])
        >>> a2.as_expr()
        -5 + 3*sqrt(2)

        Example (3): $\\alpha = 6 \\sqrt{2} - 11$, $\\theta = \\sqrt{2}$. Again we
        can build on the previous example, and we see that the coeff polys are
        composed:

        >>> a3 = AlgebraicNumber(a2, [2, -1])
        >>> a3.as_expr()
        -11 + 6*sqrt(2)

        reflecting the fact that $(2x - 1) \\circ (3x - 5) = 6x - 11$.

        Example (4): $\\alpha = \\sqrt{2}$, $\\theta = \\sqrt{2} + \\sqrt{3}$. The
        easiest way is to use the :py:func:`~.to_number_field()` function:

        >>> from sympy import to_number_field
        >>> a4 = to_number_field(sqrt(2), sqrt(2) + sqrt(3))
        >>> a4.minpoly_of_element().as_expr(x)
        x**2 - 2
        >>> a4.to_root()
        sqrt(2)
        >>> a4.primitive_element()
        sqrt(2) + sqrt(3)
        >>> a4.coeffs()
        [1/2, 0, -9/2, 0]

        but if you already knew the right coefficients, you could construct it
        directly:

        >>> a4 = AlgebraicNumber(sqrt(2) + sqrt(3), [S(1)/2, 0, S(-9)/2, 0])
        >>> a4.to_root()
        sqrt(2)
        >>> a4.primitive_element()
        sqrt(2) + sqrt(3)

        Example (5): Construct the Golden Ratio as an element of the 5th
        cyclotomic field, supposing we already know its coefficients. This time
        we introduce the alias $\\zeta$ for the primitive element of the field:

        >>> from sympy import cyclotomic_poly
        >>> from sympy.abc import zeta
        >>> a5 = AlgebraicNumber(CRootOf(cyclotomic_poly(5), -1),
        ...                  [-1, -1, 0, 0], alias=zeta)
        >>> a5.as_poly().as_expr()
        -zeta**3 - zeta**2
        >>> a5.evalf()
        1.61803398874989

        (The index ``-1`` to ``CRootOf`` selects the complex root with the
        largest real and imaginary parts, which in this case is
        $\\mathrm{e}^{2i\\pi/5}$. See :py:class:`~.ComplexRootOf`.)

        Example (6): Building on the last example, construct the number
        $2 \\phi \\in \\mathbb{Q}(\\phi)$, where $\\phi$ is the Golden Ratio:

        >>> from sympy.abc import phi
        >>> a6 = AlgebraicNumber(a5.to_root(), coeffs=[2, 0], alias=phi)
        >>> a6.as_poly().as_expr()
        2*phi
        >>> a6.primitive_element().evalf()
        1.61803398874989

        Note that we needed to use ``a5.to_root()``, since passing ``a5`` as
        the first argument would have constructed the number $2 \\phi$ as an
        element of the field $\\mathbb{Q}(\\zeta)$:

        >>> a6_wrong = AlgebraicNumber(a5, coeffs=[2, 0])
        >>> a6_wrong.as_poly().as_expr()
        -2*zeta**3 - 2*zeta**2
        >>> a6_wrong.primitive_element().evalf()
        0.309016994374947 + 0.951056516295154*I

        """
    def __hash__(self): ...
    @property
    def is_aliased(self):
        """Returns ``True`` if ``alias`` was set. """
    def as_poly(self, x: Incomplete | None = None):
        """Create a Poly instance from ``self``. """
    def as_expr(self, x: Incomplete | None = None):
        """Create a Basic expression from ``self``. """
    def coeffs(self):
        """Returns all SymPy coefficients of an algebraic number. """
    def native_coeffs(self):
        """Returns all native coefficients of an algebraic number. """
    def to_algebraic_integer(self):
        """Convert ``self`` to an algebraic integer. """
    def field_element(self, coeffs):
        """
        Form another element of the same number field.

        Explanation
        ===========

        If we represent $\\alpha \\in \\mathbb{Q}(\\theta)$, form another element
        $\\beta \\in \\mathbb{Q}(\\theta)$ of the same number field.

        Parameters
        ==========

        coeffs : list, :py:class:`~.ANP`
            Like the *coeffs* arg to the class
            :py:meth:`constructor<.AlgebraicNumber.__new__>`, defines the
            new element as a polynomial in the primitive element.

            If a list, the elements should be integers or rational numbers.
            If an :py:class:`~.ANP`, we take its coefficients (using its
            :py:meth:`~.ANP.to_list()` method).

        Examples
        ========

        >>> from sympy import AlgebraicNumber, sqrt
        >>> a = AlgebraicNumber(sqrt(5), [-1, 1])
        >>> b = a.field_element([3, 2])
        >>> print(a)
        1 - sqrt(5)
        >>> print(b)
        2 + 3*sqrt(5)
        >>> print(b.primitive_element() == a.primitive_element())
        True

        See Also
        ========

        AlgebraicNumber
        """
    @property
    def is_primitive_element(self):
        """
        Say whether this algebraic number $\\alpha \\in \\mathbb{Q}(\\theta)$ is
        equal to the primitive element $\\theta$ for its field.
        """
    def primitive_element(self):
        """
        Get the primitive element $\\theta$ for the number field
        $\\mathbb{Q}(\\theta)$ to which this algebraic number $\\alpha$ belongs.

        Returns
        =======

        AlgebraicNumber

        """
    def to_primitive_element(self, radicals: bool = True):
        """
        Convert ``self`` to an :py:class:`~.AlgebraicNumber` instance that is
        equal to its own primitive element.

        Explanation
        ===========

        If we represent $\\alpha \\in \\mathbb{Q}(\\theta)$, $\\alpha \\neq \\theta$,
        construct a new :py:class:`~.AlgebraicNumber` that represents
        $\\alpha \\in \\mathbb{Q}(\\alpha)$.

        Examples
        ========

        >>> from sympy import sqrt, to_number_field
        >>> from sympy.abc import x
        >>> a = to_number_field(sqrt(2), sqrt(2) + sqrt(3))

        The :py:class:`~.AlgebraicNumber` ``a`` represents the number
        $\\sqrt{2}$ in the field $\\mathbb{Q}(\\sqrt{2} + \\sqrt{3})$. Rendering
        ``a`` as a polynomial,

        >>> a.as_poly().as_expr(x)
        x**3/2 - 9*x/2

        reflects the fact that $\\sqrt{2} = \\theta^3/2 - 9 \\theta/2$, where
        $\\theta = \\sqrt{2} + \\sqrt{3}$.

        ``a`` is not equal to its own primitive element. Its minpoly

        >>> a.minpoly.as_poly().as_expr(x)
        x**4 - 10*x**2 + 1

        is that of $\\theta$.

        Converting to a primitive element,

        >>> a_prim = a.to_primitive_element()
        >>> a_prim.minpoly.as_poly().as_expr(x)
        x**2 - 2

        we obtain an :py:class:`~.AlgebraicNumber` whose ``minpoly`` is that of
        the number itself.

        Parameters
        ==========

        radicals : boolean, optional (default=True)
            If ``True``, then we will try to return an
            :py:class:`~.AlgebraicNumber` whose ``root`` is an expression
            in radicals. If that is not possible (or if *radicals* is
            ``False``), ``root`` will be a :py:class:`~.ComplexRootOf`.

        Returns
        =======

        AlgebraicNumber

        See Also
        ========

        is_primitive_element

        """
    def minpoly_of_element(self):
        """
        Compute the minimal polynomial for this algebraic number.

        Explanation
        ===========

        Recall that we represent an element $\\alpha \\in \\mathbb{Q}(\\theta)$.
        Our instance attribute ``self.minpoly`` is the minimal polynomial for
        our primitive element $\\theta$. This method computes the minimal
        polynomial for $\\alpha$.

        """
    def to_root(self, radicals: bool = True, minpoly: Incomplete | None = None):
        """
        Convert to an :py:class:`~.Expr` that is not an
        :py:class:`~.AlgebraicNumber`, specifically, either a
        :py:class:`~.ComplexRootOf`, or, optionally and where possible, an
        expression in radicals.

        Parameters
        ==========

        radicals : boolean, optional (default=True)
            If ``True``, then we will try to return the root as an expression
            in radicals. If that is not possible, we will return a
            :py:class:`~.ComplexRootOf`.

        minpoly : :py:class:`~.Poly`
            If the minimal polynomial for `self` has been pre-computed, it can
            be passed in order to save time.

        """

class RationalConstant(Rational):
    """
    Abstract base class for rationals with specific behaviors

    Derived classes must define class attributes p and q and should probably all
    be singletons.
    """
    def __new__(cls): ...

class IntegerConstant(Integer):
    def __new__(cls): ...

class Zero(IntegerConstant, metaclass=Singleton):
    """The number zero.

    Zero is a singleton, and can be accessed by ``S.Zero``

    Examples
    ========

    >>> from sympy import S, Integer
    >>> Integer(0) is S.Zero
    True
    >>> 1/S.Zero
    zoo

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Zero
    """
    p: int
    q: int
    is_positive: bool
    is_negative: bool
    is_zero: bool
    is_number: bool
    is_comparable: bool
    def __getnewargs__(self): ...
    @staticmethod
    def __abs__(): ...
    @staticmethod
    def __neg__(): ...
    def __bool__(self) -> bool: ...

class One(IntegerConstant, metaclass=Singleton):
    """The number one.

    One is a singleton, and can be accessed by ``S.One``.

    Examples
    ========

    >>> from sympy import S, Integer
    >>> Integer(1) is S.One
    True

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/1_%28number%29
    """
    is_number: bool
    is_positive: bool
    p: int
    q: int
    def __getnewargs__(self): ...
    @staticmethod
    def __abs__(): ...
    @staticmethod
    def __neg__(): ...
    @staticmethod
    def factors(limit: Incomplete | None = None, use_trial: bool = True, use_rho: bool = False, use_pm1: bool = False, verbose: bool = False, visual: bool = False): ...

class NegativeOne(IntegerConstant, metaclass=Singleton):
    """The number negative one.

    NegativeOne is a singleton, and can be accessed by ``S.NegativeOne``.

    Examples
    ========

    >>> from sympy import S, Integer
    >>> Integer(-1) is S.NegativeOne
    True

    See Also
    ========

    One

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/%E2%88%921_%28number%29

    """
    is_number: bool
    p: int
    q: int
    def __getnewargs__(self): ...
    @staticmethod
    def __abs__(): ...
    @staticmethod
    def __neg__(): ...

class Half(RationalConstant, metaclass=Singleton):
    """The rational number 1/2.

    Half is a singleton, and can be accessed by ``S.Half``.

    Examples
    ========

    >>> from sympy import S, Rational
    >>> Rational(1, 2) is S.Half
    True

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/One_half
    """
    is_number: bool
    p: int
    q: int
    def __getnewargs__(self): ...
    @staticmethod
    def __abs__(): ...

class Infinity(Number, metaclass=Singleton):
    """Positive infinite quantity.

    Explanation
    ===========

    In real analysis the symbol `\\infty` denotes an unbounded
    limit: `x\\to\\infty` means that `x` grows without bound.

    Infinity is often used not only to define a limit but as a value
    in the affinely extended real number system.  Points labeled `+\\infty`
    and `-\\infty` can be added to the topological space of the real numbers,
    producing the two-point compactification of the real numbers.  Adding
    algebraic properties to this gives us the extended real numbers.

    Infinity is a singleton, and can be accessed by ``S.Infinity``,
    or can be imported as ``oo``.

    Examples
    ========

    >>> from sympy import oo, exp, limit, Symbol
    >>> 1 + oo
    oo
    >>> 42/oo
    0
    >>> x = Symbol('x')
    >>> limit(exp(x), x, oo)
    oo

    See Also
    ========

    NegativeInfinity, NaN

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Infinity
    """
    is_commutative: bool
    is_number: bool
    is_complex: bool
    is_extended_real: bool
    is_infinite: bool
    is_comparable: bool
    is_extended_positive: bool
    is_prime: bool
    def __new__(cls): ...
    def evalf(self, prec: Incomplete | None = None, **options): ...
    def __add__(self, other): ...
    __radd__ = __add__
    def __sub__(self, other): ...
    def __rsub__(self, other): ...
    def __mul__(self, other): ...
    __rmul__ = __mul__
    def __truediv__(self, other): ...
    def __abs__(self): ...
    def __neg__(self): ...
    def __hash__(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    __gt__: Incomplete
    __ge__: Incomplete
    __lt__: Incomplete
    __le__: Incomplete
    def __mod__(self, other): ...
    __rmod__ = __mod__
    def floor(self): ...
    def ceiling(self): ...

oo: Incomplete

class NegativeInfinity(Number, metaclass=Singleton):
    """Negative infinite quantity.

    NegativeInfinity is a singleton, and can be accessed
    by ``S.NegativeInfinity``.

    See Also
    ========

    Infinity
    """
    is_extended_real: bool
    is_complex: bool
    is_commutative: bool
    is_infinite: bool
    is_comparable: bool
    is_extended_negative: bool
    is_number: bool
    is_prime: bool
    def __new__(cls): ...
    def evalf(self, prec: Incomplete | None = None, **options): ...
    def __add__(self, other): ...
    __radd__ = __add__
    def __sub__(self, other): ...
    def __rsub__(self, other): ...
    def __mul__(self, other): ...
    __rmul__ = __mul__
    def __truediv__(self, other): ...
    def __abs__(self): ...
    def __neg__(self): ...
    def __hash__(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    __gt__: Incomplete
    __ge__: Incomplete
    __lt__: Incomplete
    __le__: Incomplete
    def __mod__(self, other): ...
    __rmod__ = __mod__
    def floor(self): ...
    def ceiling(self): ...
    def as_powers_dict(self): ...

class NaN(Number, metaclass=Singleton):
    """
    Not a Number.

    Explanation
    ===========

    This serves as a place holder for numeric values that are indeterminate.
    Most operations on NaN, produce another NaN.  Most indeterminate forms,
    such as ``0/0`` or ``oo - oo` produce NaN.  Two exceptions are ``0**0``
    and ``oo**0``, which all produce ``1`` (this is consistent with Python's
    float).

    NaN is loosely related to floating point nan, which is defined in the
    IEEE 754 floating point standard, and corresponds to the Python
    ``float('nan')``.  Differences are noted below.

    NaN is mathematically not equal to anything else, even NaN itself.  This
    explains the initially counter-intuitive results with ``Eq`` and ``==`` in
    the examples below.

    NaN is not comparable so inequalities raise a TypeError.  This is in
    contrast with floating point nan where all inequalities are false.

    NaN is a singleton, and can be accessed by ``S.NaN``, or can be imported
    as ``nan``.

    Examples
    ========

    >>> from sympy import nan, S, oo, Eq
    >>> nan is S.NaN
    True
    >>> oo - oo
    nan
    >>> nan + 1
    nan
    >>> Eq(nan, nan)   # mathematical equality
    False
    >>> nan == nan     # structural equality
    True

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/NaN

    """
    is_commutative: bool
    is_extended_real: Incomplete
    is_real: Incomplete
    is_rational: Incomplete
    is_algebraic: Incomplete
    is_transcendental: Incomplete
    is_integer: Incomplete
    is_comparable: bool
    is_finite: Incomplete
    is_zero: Incomplete
    is_prime: Incomplete
    is_positive: Incomplete
    is_negative: Incomplete
    is_number: bool
    def __new__(cls): ...
    def __neg__(self): ...
    def __add__(self, other): ...
    def __sub__(self, other): ...
    def __mul__(self, other): ...
    def __truediv__(self, other): ...
    def floor(self): ...
    def ceiling(self): ...
    def __hash__(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    __gt__: Incomplete
    __ge__: Incomplete
    __lt__: Incomplete
    __le__: Incomplete

nan: Incomplete

class ComplexInfinity(AtomicExpr, metaclass=Singleton):
    '''Complex infinity.

    Explanation
    ===========

    In complex analysis the symbol `\\tilde\\infty`, called "complex
    infinity", represents a quantity with infinite magnitude, but
    undetermined complex phase.

    ComplexInfinity is a singleton, and can be accessed by
    ``S.ComplexInfinity``, or can be imported as ``zoo``.

    Examples
    ========

    >>> from sympy import zoo
    >>> zoo + 42
    zoo
    >>> 42/zoo
    0
    >>> zoo + zoo
    nan
    >>> zoo*zoo
    zoo

    See Also
    ========

    Infinity
    '''
    is_commutative: bool
    is_infinite: bool
    is_number: bool
    is_prime: bool
    is_complex: bool
    is_extended_real: bool
    kind = NumberKind
    def __new__(cls): ...
    @staticmethod
    def __abs__(): ...
    def floor(self): ...
    def ceiling(self): ...
    @staticmethod
    def __neg__(): ...

zoo: Incomplete

class NumberSymbol(AtomicExpr):
    is_commutative: bool
    is_finite: bool
    is_number: bool
    is_NumberSymbol: bool
    kind = NumberKind
    def __new__(cls): ...
    def approximation(self, number_cls) -> None:
        """ Return an interval with number_cls endpoints
        that contains the value of NumberSymbol.
        If not implemented, then return None.
        """
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __le__(self, other): ...
    def __ge__(self, other): ...
    def __int__(self) -> int: ...
    def __hash__(self): ...

class Exp1(NumberSymbol, metaclass=Singleton):
    """The `e` constant.

    Explanation
    ===========

    The transcendental number `e = 2.718281828\\ldots` is the base of the
    natural logarithm and of the exponential function, `e = \\exp(1)`.
    Sometimes called Euler's number or Napier's constant.

    Exp1 is a singleton, and can be accessed by ``S.Exp1``,
    or can be imported as ``E``.

    Examples
    ========

    >>> from sympy import exp, log, E
    >>> E is exp(1)
    True
    >>> log(E)
    1

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/E_%28mathematical_constant%29
    """
    is_real: bool
    is_positive: bool
    is_negative: bool
    is_irrational: bool
    is_number: bool
    is_algebraic: bool
    is_transcendental: bool
    @staticmethod
    def __abs__(): ...
    def __int__(self) -> int: ...
    def approximation_interval(self, number_cls): ...

E: Incomplete

class Pi(NumberSymbol, metaclass=Singleton):
    """The `\\pi` constant.

    Explanation
    ===========

    The transcendental number `\\pi = 3.141592654\\ldots` represents the ratio
    of a circle's circumference to its diameter, the area of the unit circle,
    the half-period of trigonometric functions, and many other things
    in mathematics.

    Pi is a singleton, and can be accessed by ``S.Pi``, or can
    be imported as ``pi``.

    Examples
    ========

    >>> from sympy import S, pi, oo, sin, exp, integrate, Symbol
    >>> S.Pi
    pi
    >>> pi > 3
    True
    >>> pi.is_irrational
    True
    >>> x = Symbol('x')
    >>> sin(x + 2*pi)
    sin(x)
    >>> integrate(exp(-x**2), (x, -oo, oo))
    sqrt(pi)

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Pi
    """
    is_real: bool
    is_positive: bool
    is_negative: bool
    is_irrational: bool
    is_number: bool
    is_algebraic: bool
    is_transcendental: bool
    @staticmethod
    def __abs__(): ...
    def __int__(self) -> int: ...
    def approximation_interval(self, number_cls): ...

pi: Incomplete

class GoldenRatio(NumberSymbol, metaclass=Singleton):
    """The golden ratio, `\\phi`.

    Explanation
    ===========

    `\\phi = \\frac{1 + \\sqrt{5}}{2}` is an algebraic number.  Two quantities
    are in the golden ratio if their ratio is the same as the ratio of
    their sum to the larger of the two quantities, i.e. their maximum.

    GoldenRatio is a singleton, and can be accessed by ``S.GoldenRatio``.

    Examples
    ========

    >>> from sympy import S
    >>> S.GoldenRatio > 1
    True
    >>> S.GoldenRatio.expand(func=True)
    1/2 + sqrt(5)/2
    >>> S.GoldenRatio.is_irrational
    True

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Golden_ratio
    """
    is_real: bool
    is_positive: bool
    is_negative: bool
    is_irrational: bool
    is_number: bool
    is_algebraic: bool
    is_transcendental: bool
    def __int__(self) -> int: ...
    def approximation_interval(self, number_cls): ...

class TribonacciConstant(NumberSymbol, metaclass=Singleton):
    """The tribonacci constant.

    Explanation
    ===========

    The tribonacci numbers are like the Fibonacci numbers, but instead
    of starting with two predetermined terms, the sequence starts with
    three predetermined terms and each term afterwards is the sum of the
    preceding three terms.

    The tribonacci constant is the ratio toward which adjacent tribonacci
    numbers tend. It is a root of the polynomial `x^3 - x^2 - x - 1 = 0`,
    and also satisfies the equation `x + x^{-3} = 2`.

    TribonacciConstant is a singleton, and can be accessed
    by ``S.TribonacciConstant``.

    Examples
    ========

    >>> from sympy import S
    >>> S.TribonacciConstant > 1
    True
    >>> S.TribonacciConstant.expand(func=True)
    1/3 + (19 - 3*sqrt(33))**(1/3)/3 + (3*sqrt(33) + 19)**(1/3)/3
    >>> S.TribonacciConstant.is_irrational
    True
    >>> S.TribonacciConstant.n(20)
    1.8392867552141611326

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Generalizations_of_Fibonacci_numbers#Tribonacci_numbers
    """
    is_real: bool
    is_positive: bool
    is_negative: bool
    is_irrational: bool
    is_number: bool
    is_algebraic: bool
    is_transcendental: bool
    def __int__(self) -> int: ...
    def approximation_interval(self, number_cls): ...

class EulerGamma(NumberSymbol, metaclass=Singleton):
    """The Euler-Mascheroni constant.

    Explanation
    ===========

    `\\gamma = 0.5772157\\ldots` (also called Euler's constant) is a mathematical
    constant recurring in analysis and number theory.  It is defined as the
    limiting difference between the harmonic series and the
    natural logarithm:

    .. math:: \\gamma = \\lim\\limits_{n\\to\\infty}
              \\left(\\sum\\limits_{k=1}^n\\frac{1}{k} - \\ln n\\right)

    EulerGamma is a singleton, and can be accessed by ``S.EulerGamma``.

    Examples
    ========

    >>> from sympy import S
    >>> S.EulerGamma.is_irrational
    >>> S.EulerGamma > 0
    True
    >>> S.EulerGamma > 1
    False

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Euler%E2%80%93Mascheroni_constant
    """
    is_real: bool
    is_positive: bool
    is_negative: bool
    is_irrational: Incomplete
    is_number: bool
    def __int__(self) -> int: ...
    def approximation_interval(self, number_cls): ...

class Catalan(NumberSymbol, metaclass=Singleton):
    """Catalan's constant.

    Explanation
    ===========

    $G = 0.91596559\\ldots$ is given by the infinite series

    .. math:: G = \\sum_{k=0}^{\\infty} \\frac{(-1)^k}{(2k+1)^2}

    Catalan is a singleton, and can be accessed by ``S.Catalan``.

    Examples
    ========

    >>> from sympy import S
    >>> S.Catalan.is_irrational
    >>> S.Catalan > 0
    True
    >>> S.Catalan > 1
    False

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Catalan%27s_constant
    """
    is_real: bool
    is_positive: bool
    is_negative: bool
    is_irrational: Incomplete
    is_number: bool
    def __int__(self) -> int: ...
    def approximation_interval(self, number_cls): ...

class ImaginaryUnit(AtomicExpr, metaclass=Singleton):
    """The imaginary unit, `i = \\sqrt{-1}`.

    I is a singleton, and can be accessed by ``S.I``, or can be
    imported as ``I``.

    Examples
    ========

    >>> from sympy import I, sqrt
    >>> sqrt(-1)
    I
    >>> I*I
    -1
    >>> 1/I
    -I

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Imaginary_unit
    """
    is_commutative: bool
    is_imaginary: bool
    is_finite: bool
    is_number: bool
    is_algebraic: bool
    is_transcendental: bool
    kind = NumberKind
    @staticmethod
    def __abs__(): ...
    def as_base_exp(self): ...

I: Incomplete

def equal_valued(x, y):
    """Compare expressions treating plain floats as rationals.

    Examples
    ========

    >>> from sympy import S, symbols, Rational, Float
    >>> from sympy.core.numbers import equal_valued
    >>> equal_valued(1, 2)
    False
    >>> equal_valued(1, 1)
    True

    In SymPy expressions with Floats compare unequal to corresponding
    expressions with rationals:

    >>> x = symbols('x')
    >>> x**2 == x**2.0
    False

    However an individual Float compares equal to a Rational:

    >>> Rational(1, 2) == Float(0.5)
    True

    In a future version of SymPy this might change so that Rational and Float
    compare unequal. This function provides the behavior currently expected of
    ``==`` so that it could still be used if the behavior of ``==`` were to
    change in future.

    >>> equal_valued(1, 1.0) # Float vs Rational
    True
    >>> equal_valued(S(1).n(3), S(1).n(5)) # Floats of different precision
    True

    Explanation
    ===========

    In future SymPy verions Float and Rational might compare unequal and floats
    with different precisions might compare unequal. In that context a function
    is needed that can check if a number is equal to 1 or 0 etc. The idea is
    that instead of testing ``if x == 1:`` if we want to accept floats like
    ``1.0`` as well then the test can be written as ``if equal_valued(x, 1):``
    or ``if equal_valued(x, 2):``. Since this function is intended to be used
    in situations where one or both operands are expected to be concrete
    numbers like 1 or 0 the function does not recurse through the args of any
    compound expression to compare any nested floats.

    References
    ==========

    .. [1] https://github.com/sympy/sympy/pull/20033
    """
def sympify_fractions(f): ...
def sympify_mpz(x): ...
def sympify_mpq(x): ...
def sympify_mpmath_mpq(x): ...
def sympify_mpmath(x): ...
def sympify_complex(a): ...
