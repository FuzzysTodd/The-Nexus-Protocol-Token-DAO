from . import function_docs as function_docs, rational as rational
from .libmp import ComplexResult as ComplexResult, MPZ as MPZ, MPZ_ONE as MPZ_ONE, MPZ_ZERO as MPZ_ZERO, bitcount as bitcount, dps_to_prec as dps_to_prec, finf as finf, fnan as fnan, fninf as fninf, fone as fone, from_Decimal as from_Decimal, from_float as from_float, from_int as from_int, from_man_exp as from_man_exp, from_npfloat as from_npfloat, from_pickable as from_pickable, from_rational as from_rational, from_str as from_str, fzero as fzero, int_types as int_types, mpc_abs as mpc_abs, mpc_add as mpc_add, mpc_add_mpf as mpc_add_mpf, mpc_conjugate as mpc_conjugate, mpc_div as mpc_div, mpc_div_mpf as mpc_div_mpf, mpc_hash as mpc_hash, mpc_is_nonzero as mpc_is_nonzero, mpc_mpf_div as mpc_mpf_div, mpc_mul as mpc_mul, mpc_mul_int as mpc_mul_int, mpc_mul_mpf as mpc_mul_mpf, mpc_neg as mpc_neg, mpc_pos as mpc_pos, mpc_pow as mpc_pow, mpc_pow_int as mpc_pow_int, mpc_pow_mpf as mpc_pow_mpf, mpc_sub as mpc_sub, mpc_sub_mpf as mpc_sub_mpf, mpc_to_complex as mpc_to_complex, mpc_to_str as mpc_to_str, mpf_abs as mpf_abs, mpf_add as mpf_add, mpf_apery as mpf_apery, mpf_catalan as mpf_catalan, mpf_cmp as mpf_cmp, mpf_degree as mpf_degree, mpf_div as mpf_div, mpf_e as mpf_e, mpf_eq as mpf_eq, mpf_euler as mpf_euler, mpf_ge as mpf_ge, mpf_glaisher as mpf_glaisher, mpf_gt as mpf_gt, mpf_hash as mpf_hash, mpf_khinchin as mpf_khinchin, mpf_le as mpf_le, mpf_ln10 as mpf_ln10, mpf_ln2 as mpf_ln2, mpf_lt as mpf_lt, mpf_mertens as mpf_mertens, mpf_mod as mpf_mod, mpf_mul as mpf_mul, mpf_mul_int as mpf_mul_int, mpf_neg as mpf_neg, mpf_phi as mpf_phi, mpf_pi as mpf_pi, mpf_pos as mpf_pos, mpf_pow as mpf_pow, mpf_pow_int as mpf_pow_int, mpf_rand as mpf_rand, mpf_rdiv_int as mpf_rdiv_int, mpf_sub as mpf_sub, mpf_sum as mpf_sum, mpf_twinprime as mpf_twinprime, normalize as normalize, prec_to_dps as prec_to_dps, repr_dps as repr_dps, round_ceiling as round_ceiling, round_floor as round_floor, round_nearest as round_nearest, to_fixed as to_fixed, to_float as to_float, to_int as to_int, to_pickable as to_pickable, to_str as to_str
from .libmp.backend import basestring as basestring, exec_ as exec_
from _typeshed import Incomplete

new: Incomplete

class mpnumeric:
    """Base class for mpf and mpc."""
    def __new__(cls, val) -> None: ...

class _mpf(mpnumeric):
    """
    An mpf instance holds a real-valued floating-point number. mpf:s
    work analogously to Python floats, but support arbitrary-precision
    arithmetic.
    """
    def __new__(cls, val=..., **kwargs):
        """A new mpf can be created from a Python float, an int, a
        or a decimal string representing a number in floating-point
        format."""
    @classmethod
    def mpf_convert_arg(cls, x, prec, rounding): ...
    @classmethod
    def mpf_convert_rhs(cls, x): ...
    @classmethod
    def mpf_convert_lhs(cls, x): ...
    man_exp: Incomplete
    man: Incomplete
    exp: Incomplete
    bc: Incomplete
    real: Incomplete
    imag: Incomplete
    conjugate: Incomplete
    def __hash__(s): ...
    def __int__(s) -> int: ...
    def __long__(s): ...
    def __float__(s) -> float: ...
    def __complex__(s) -> complex: ...
    def __nonzero__(s): ...
    __bool__ = __nonzero__
    def __abs__(s): ...
    def __pos__(s): ...
    def __neg__(s): ...
    def __cmp__(s, t): ...
    def __lt__(s, t): ...
    def __gt__(s, t): ...
    def __le__(s, t): ...
    def __ge__(s, t): ...
    def __ne__(s, t): ...
    def __rsub__(s, t): ...
    def __rdiv__(s, t): ...
    def __rpow__(s, t): ...
    def __rmod__(s, t): ...
    def sqrt(s): ...
    def ae(s, t, rel_eps: Incomplete | None = None, abs_eps: Incomplete | None = None): ...
    def to_fixed(self, prec): ...
    def __round__(self, *args): ...

mpf_binary_op: str
return_mpf: str
return_mpc: str
mpf_pow_same: Incomplete

def binary_op(name, with_mpf: str = '', with_int: str = '', with_mpc: str = ''): ...

class _constant(_mpf):
    """Represents a mathematical constant with dynamic precision.
    When printed or used in an arithmetic operation, a constant
    is converted to a regular mpf at the working precision. A
    regular mpf can also be obtained using the operation +x."""
    def __new__(cls, func, name, docname: str = ''): ...
    def __call__(self, prec: Incomplete | None = None, dps: Incomplete | None = None, rounding: Incomplete | None = None): ...

class _mpc(mpnumeric):
    """
    An mpc represents a complex number using a pair of mpf:s (one
    for the real part and another for the imaginary part.) The mpc
    class behaves fairly similarly to Python's complex type.
    """
    def __new__(cls, real: int = 0, imag: int = 0): ...
    real: Incomplete
    imag: Incomplete
    def __complex__(s) -> complex: ...
    def __pos__(s): ...
    def __abs__(s): ...
    def __neg__(s): ...
    def conjugate(s): ...
    def __nonzero__(s): ...
    __bool__ = __nonzero__
    def __hash__(s): ...
    @classmethod
    def mpc_convert_lhs(cls, x): ...
    def __eq__(s, t): ...
    def __ne__(s, t): ...
    __gt__: Incomplete
    __le__: Incomplete
    __ge__: Incomplete
    def __add__(s, t): ...
    def __sub__(s, t): ...
    def __mul__(s, t): ...
    def __div__(s, t): ...
    def __pow__(s, t): ...
    __radd__ = __add__
    def __rsub__(s, t): ...
    def __rmul__(s, t): ...
    def __rdiv__(s, t): ...
    def __rpow__(s, t): ...
    __truediv__ = __div__
    __rtruediv__ = __rdiv__
    def ae(s, t, rel_eps: Incomplete | None = None, abs_eps: Incomplete | None = None): ...

complex_types: Incomplete

class PythonMPContext:
    def __init__(ctx) -> None: ...
    def make_mpf(ctx, v): ...
    def make_mpc(ctx, v): ...
    def default(ctx) -> None: ...
    prec: Incomplete
    dps: Incomplete
    def convert(ctx, x, strings: bool = True):
        """
        Converts *x* to an ``mpf`` or ``mpc``. If *x* is of type ``mpf``,
        ``mpc``, ``int``, ``float``, ``complex``, the conversion
        will be performed losslessly.

        If *x* is a string, the result will be rounded to the present
        working precision. Strings representing fractions or complex
        numbers are permitted.

            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = False
            >>> mpmathify(3.5)
            mpf('3.5')
            >>> mpmathify('2.1')
            mpf('2.1000000000000001')
            >>> mpmathify('3/4')
            mpf('0.75')
            >>> mpmathify('2+3j')
            mpc(real='2.0', imag='3.0')

        """
    def npconvert(ctx, x):
        """
        Converts *x* to an ``mpf`` or ``mpc``. *x* should be a numpy
        scalar.
        """
    def isnan(ctx, x):
        """
        Return *True* if *x* is a NaN (not-a-number), or for a complex
        number, whether either the real or complex part is NaN;
        otherwise return *False*::

            >>> from mpmath import *
            >>> isnan(3.14)
            False
            >>> isnan(nan)
            True
            >>> isnan(mpc(3.14,2.72))
            False
            >>> isnan(mpc(3.14,nan))
            True

        """
    def isinf(ctx, x):
        """
        Return *True* if the absolute value of *x* is infinite;
        otherwise return *False*::

            >>> from mpmath import *
            >>> isinf(inf)
            True
            >>> isinf(-inf)
            True
            >>> isinf(3)
            False
            >>> isinf(3+4j)
            False
            >>> isinf(mpc(3,inf))
            True
            >>> isinf(mpc(inf,3))
            True

        """
    def isnormal(ctx, x):
        '''
        Determine whether *x* is "normal" in the sense of floating-point
        representation; that is, return *False* if *x* is zero, an
        infinity or NaN; otherwise return *True*. By extension, a
        complex number *x* is considered "normal" if its magnitude is
        normal::

            >>> from mpmath import *
            >>> isnormal(3)
            True
            >>> isnormal(0)
            False
            >>> isnormal(inf); isnormal(-inf); isnormal(nan)
            False
            False
            False
            >>> isnormal(0+0j)
            False
            >>> isnormal(0+3j)
            True
            >>> isnormal(mpc(2,nan))
            False
        '''
    def isint(ctx, x, gaussian: bool = False):
        """
        Return *True* if *x* is integer-valued; otherwise return
        *False*::

            >>> from mpmath import *
            >>> isint(3)
            True
            >>> isint(mpf(3))
            True
            >>> isint(3.2)
            False
            >>> isint(inf)
            False

        Optionally, Gaussian integers can be checked for::

            >>> isint(3+0j)
            True
            >>> isint(3+2j)
            False
            >>> isint(3+2j, gaussian=True)
            True

        """
    def fsum(ctx, terms, absolute: bool = False, squared: bool = False):
        """
        Calculates a sum containing a finite number of terms (for infinite
        series, see :func:`~mpmath.nsum`). The terms will be converted to
        mpmath numbers. For len(terms) > 2, this function is generally
        faster and produces more accurate results than the builtin
        Python function :func:`sum`.

            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = False
            >>> fsum([1, 2, 0.5, 7])
            mpf('10.5')

        With squared=True each term is squared, and with absolute=True
        the absolute value of each term is used.
        """
    def fdot(ctx, A, B: Incomplete | None = None, conjugate: bool = False):
        """
        Computes the dot product of the iterables `A` and `B`,

        .. math ::

            \\sum_{k=0} A_k B_k.

        Alternatively, :func:`~mpmath.fdot` accepts a single iterable of pairs.
        In other words, ``fdot(A,B)`` and ``fdot(zip(A,B))`` are equivalent.
        The elements are automatically converted to mpmath numbers.

        With ``conjugate=True``, the elements in the second vector
        will be conjugated:

        .. math ::

            \\sum_{k=0} A_k \\overline{B_k}

        **Examples**

            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = False
            >>> A = [2, 1.5, 3]
            >>> B = [1, -1, 2]
            >>> fdot(A, B)
            mpf('6.5')
            >>> list(zip(A, B))
            [(2, 1), (1.5, -1), (3, 2)]
            >>> fdot(_)
            mpf('6.5')
            >>> A = [2, 1.5, 3j]
            >>> B = [1+j, 3, -1-j]
            >>> fdot(A, B)
            mpc(real='9.5', imag='-1.0')
            >>> fdot(A, B, conjugate=True)
            mpc(real='3.5', imag='-5.0')

        """
    def mag(ctx, x):
        """
        Quick logarithmic magnitude estimate of a number. Returns an
        integer or infinity `m` such that `|x| <= 2^m`. It is not
        guaranteed that `m` is an optimal bound, but it will never
        be too large by more than 2 (and probably not more than 1).

        **Examples**

            >>> from mpmath import *
            >>> mp.pretty = True
            >>> mag(10), mag(10.0), mag(mpf(10)), int(ceil(log(10,2)))
            (4, 4, 4, 4)
            >>> mag(10j), mag(10+10j)
            (4, 5)
            >>> mag(0.01), int(ceil(log(0.01,2)))
            (-6, -6)
            >>> mag(0), mag(inf), mag(-inf), mag(nan)
            (-inf, +inf, +inf, nan)

        """
