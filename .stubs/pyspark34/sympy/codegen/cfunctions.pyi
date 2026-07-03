from sympy.core.function import ArgumentIndexError as ArgumentIndexError, Function as Function
from sympy.core.numbers import Rational as Rational
from sympy.core.power import Pow as Pow
from sympy.core.singleton import S as S
from sympy.functions.elementary.exponential import exp as exp, log as log
from sympy.functions.elementary.miscellaneous import sqrt as sqrt

class expm1(Function):
    """
    Represents the exponential function minus one.

    Explanation
    ===========

    The benefit of using ``expm1(x)`` over ``exp(x) - 1``
    is that the latter is prone to cancellation under finite precision
    arithmetic when x is close to zero.

    Examples
    ========

    >>> from sympy.abc import x
    >>> from sympy.codegen.cfunctions import expm1
    >>> '%.0e' % expm1(1e-99).evalf()
    '1e-99'
    >>> from math import exp
    >>> exp(1e-99) - 1
    0.0
    >>> expm1(x).diff(x)
    exp(x)

    See Also
    ========

    log1p
    """
    nargs: int
    def fdiff(self, argindex: int = 1):
        """
        Returns the first derivative of this function.
        """
    @classmethod
    def eval(cls, arg): ...

class log1p(Function):
    """
    Represents the natural logarithm of a number plus one.

    Explanation
    ===========

    The benefit of using ``log1p(x)`` over ``log(x + 1)``
    is that the latter is prone to cancellation under finite precision
    arithmetic when x is close to zero.

    Examples
    ========

    >>> from sympy.abc import x
    >>> from sympy.codegen.cfunctions import log1p
    >>> from sympy import expand_log
    >>> '%.0e' % expand_log(log1p(1e-99)).evalf()
    '1e-99'
    >>> from math import log
    >>> log(1 + 1e-99)
    0.0
    >>> log1p(x).diff(x)
    1/(x + 1)

    See Also
    ========

    expm1
    """
    nargs: int
    def fdiff(self, argindex: int = 1):
        """
        Returns the first derivative of this function.
        """
    @classmethod
    def eval(cls, arg): ...

class exp2(Function):
    """
    Represents the exponential function with base two.

    Explanation
    ===========

    The benefit of using ``exp2(x)`` over ``2**x``
    is that the latter is not as efficient under finite precision
    arithmetic.

    Examples
    ========

    >>> from sympy.abc import x
    >>> from sympy.codegen.cfunctions import exp2
    >>> exp2(2).evalf() == 4.0
    True
    >>> exp2(x).diff(x)
    log(2)*exp2(x)

    See Also
    ========

    log2
    """
    nargs: int
    def fdiff(self, argindex: int = 1):
        """
        Returns the first derivative of this function.
        """
    @classmethod
    def eval(cls, arg): ...

class log2(Function):
    """
    Represents the logarithm function with base two.

    Explanation
    ===========

    The benefit of using ``log2(x)`` over ``log(x)/log(2)``
    is that the latter is not as efficient under finite precision
    arithmetic.

    Examples
    ========

    >>> from sympy.abc import x
    >>> from sympy.codegen.cfunctions import log2
    >>> log2(4).evalf() == 2.0
    True
    >>> log2(x).diff(x)
    1/(x*log(2))

    See Also
    ========

    exp2
    log10
    """
    nargs: int
    def fdiff(self, argindex: int = 1):
        """
        Returns the first derivative of this function.
        """
    @classmethod
    def eval(cls, arg): ...

class fma(Function):
    '''
    Represents "fused multiply add".

    Explanation
    ===========

    The benefit of using ``fma(x, y, z)`` over ``x*y + z``
    is that, under finite precision arithmetic, the former is
    supported by special instructions on some CPUs.

    Examples
    ========

    >>> from sympy.abc import x, y, z
    >>> from sympy.codegen.cfunctions import fma
    >>> fma(x, y, z).diff(x)
    y

    '''
    nargs: int
    def fdiff(self, argindex: int = 1):
        """
        Returns the first derivative of this function.
        """

class log10(Function):
    """
    Represents the logarithm function with base ten.

    Examples
    ========

    >>> from sympy.abc import x
    >>> from sympy.codegen.cfunctions import log10
    >>> log10(100).evalf() == 2.0
    True
    >>> log10(x).diff(x)
    1/(x*log(10))

    See Also
    ========

    log2
    """
    nargs: int
    def fdiff(self, argindex: int = 1):
        """
        Returns the first derivative of this function.
        """
    @classmethod
    def eval(cls, arg): ...

class Sqrt(Function):
    """
    Represents the square root function.

    Explanation
    ===========

    The reason why one would use ``Sqrt(x)`` over ``sqrt(x)``
    is that the latter is internally represented as ``Pow(x, S.Half)`` which
    may not be what one wants when doing code-generation.

    Examples
    ========

    >>> from sympy.abc import x
    >>> from sympy.codegen.cfunctions import Sqrt
    >>> Sqrt(x)
    Sqrt(x)
    >>> Sqrt(x).diff(x)
    1/(2*sqrt(x))

    See Also
    ========

    Cbrt
    """
    nargs: int
    def fdiff(self, argindex: int = 1):
        """
        Returns the first derivative of this function.
        """

class Cbrt(Function):
    """
    Represents the cube root function.

    Explanation
    ===========

    The reason why one would use ``Cbrt(x)`` over ``cbrt(x)``
    is that the latter is internally represented as ``Pow(x, Rational(1, 3))`` which
    may not be what one wants when doing code-generation.

    Examples
    ========

    >>> from sympy.abc import x
    >>> from sympy.codegen.cfunctions import Cbrt
    >>> Cbrt(x)
    Cbrt(x)
    >>> Cbrt(x).diff(x)
    1/(3*x**(2/3))

    See Also
    ========

    Sqrt
    """
    nargs: int
    def fdiff(self, argindex: int = 1):
        """
        Returns the first derivative of this function.
        """

class hypot(Function):
    """
    Represents the hypotenuse function.

    Explanation
    ===========

    The hypotenuse function is provided by e.g. the math library
    in the C99 standard, hence one may want to represent the function
    symbolically when doing code-generation.

    Examples
    ========

    >>> from sympy.abc import x, y
    >>> from sympy.codegen.cfunctions import hypot
    >>> hypot(3, 4).evalf() == 5.0
    True
    >>> hypot(x, y)
    hypot(x, y)
    >>> hypot(x, y).diff(x)
    x/hypot(x, y)

    """
    nargs: int
    def fdiff(self, argindex: int = 1):
        """
        Returns the first derivative of this function.
        """
