from _typeshed import Incomplete
from sympy.core import S as S, Symbol as Symbol, sympify as sympify
from sympy.core.function import expand_mul as expand_mul
from sympy.core.numbers import I as I, pi as pi
from sympy.functions.elementary.trigonometric import cos as cos, sin as sin
from sympy.ntheory import isprime as isprime, primitive_root as primitive_root
from sympy.utilities.iterables import ibin as ibin, iterable as iterable
from sympy.utilities.misc import as_int as as_int

def fft(seq, dps: Incomplete | None = None):
    """
    Performs the Discrete Fourier Transform (**DFT**) in the complex domain.

    The sequence is automatically padded to the right with zeros, as the
    *radix-2 FFT* requires the number of sample points to be a power of 2.

    This method should be used with default arguments only for short sequences
    as the complexity of expressions increases with the size of the sequence.

    Parameters
    ==========

    seq : iterable
        The sequence on which **DFT** is to be applied.
    dps : Integer
        Specifies the number of decimal digits for precision.

    Examples
    ========

    >>> from sympy import fft, ifft

    >>> fft([1, 2, 3, 4])
    [10, -2 - 2*I, -2, -2 + 2*I]
    >>> ifft(_)
    [1, 2, 3, 4]

    >>> ifft([1, 2, 3, 4])
    [5/2, -1/2 + I/2, -1/2, -1/2 - I/2]
    >>> fft(_)
    [1, 2, 3, 4]

    >>> ifft([1, 7, 3, 4], dps=15)
    [3.75, -0.5 - 0.75*I, -1.75, -0.5 + 0.75*I]
    >>> fft(_)
    [1.0, 7.0, 3.0, 4.0]

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Cooley%E2%80%93Tukey_FFT_algorithm
    .. [2] https://mathworld.wolfram.com/FastFourierTransform.html

    """
def ifft(seq, dps: Incomplete | None = None): ...
def ntt(seq, prime):
    """
    Performs the Number Theoretic Transform (**NTT**), which specializes the
    Discrete Fourier Transform (**DFT**) over quotient ring `Z/pZ` for prime
    `p` instead of complex numbers `C`.

    The sequence is automatically padded to the right with zeros, as the
    *radix-2 NTT* requires the number of sample points to be a power of 2.

    Parameters
    ==========

    seq : iterable
        The sequence on which **DFT** is to be applied.
    prime : Integer
        Prime modulus of the form `(m 2^k + 1)` to be used for performing
        **NTT** on the sequence.

    Examples
    ========

    >>> from sympy import ntt, intt
    >>> ntt([1, 2, 3, 4], prime=3*2**8 + 1)
    [10, 643, 767, 122]
    >>> intt(_, 3*2**8 + 1)
    [1, 2, 3, 4]
    >>> intt([1, 2, 3, 4], prime=3*2**8 + 1)
    [387, 415, 384, 353]
    >>> ntt(_, prime=3*2**8 + 1)
    [1, 2, 3, 4]

    References
    ==========

    .. [1] http://www.apfloat.org/ntt.html
    .. [2] https://mathworld.wolfram.com/NumberTheoreticTransform.html
    .. [3] https://en.wikipedia.org/wiki/Discrete_Fourier_transform_(general%29

    """
def intt(seq, prime): ...
def fwht(seq):
    """
    Performs the Walsh Hadamard Transform (**WHT**), and uses Hadamard
    ordering for the sequence.

    The sequence is automatically padded to the right with zeros, as the
    *radix-2 FWHT* requires the number of sample points to be a power of 2.

    Parameters
    ==========

    seq : iterable
        The sequence on which WHT is to be applied.

    Examples
    ========

    >>> from sympy import fwht, ifwht
    >>> fwht([4, 2, 2, 0, 0, 2, -2, 0])
    [8, 0, 8, 0, 8, 8, 0, 0]
    >>> ifwht(_)
    [4, 2, 2, 0, 0, 2, -2, 0]

    >>> ifwht([19, -1, 11, -9, -7, 13, -15, 5])
    [2, 0, 4, 0, 3, 10, 0, 0]
    >>> fwht(_)
    [19, -1, 11, -9, -7, 13, -15, 5]

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Hadamard_transform
    .. [2] https://en.wikipedia.org/wiki/Fast_Walsh%E2%80%93Hadamard_transform

    """
def ifwht(seq): ...
def mobius_transform(seq, subset: bool = True):
    """
    Performs the Mobius Transform for subset lattice with indices of
    sequence as bitmasks.

    The indices of each argument, considered as bit strings, correspond
    to subsets of a finite set.

    The sequence is automatically padded to the right with zeros, as the
    definition of subset/superset based on bitmasks (indices) requires
    the size of sequence to be a power of 2.

    Parameters
    ==========

    seq : iterable
        The sequence on which Mobius Transform is to be applied.
    subset : bool
        Specifies if Mobius Transform is applied by enumerating subsets
        or supersets of the given set.

    Examples
    ========

    >>> from sympy import symbols
    >>> from sympy import mobius_transform, inverse_mobius_transform
    >>> x, y, z = symbols('x y z')

    >>> mobius_transform([x, y, z])
    [x, x + y, x + z, x + y + z]
    >>> inverse_mobius_transform(_)
    [x, y, z, 0]

    >>> mobius_transform([x, y, z], subset=False)
    [x + y + z, y, z, 0]
    >>> inverse_mobius_transform(_, subset=False)
    [x, y, z, 0]

    >>> mobius_transform([1, 2, 3, 4])
    [1, 3, 4, 10]
    >>> inverse_mobius_transform(_)
    [1, 2, 3, 4]
    >>> mobius_transform([1, 2, 3, 4], subset=False)
    [10, 6, 7, 4]
    >>> inverse_mobius_transform(_, subset=False)
    [1, 2, 3, 4]

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/M%C3%B6bius_inversion_formula
    .. [2] https://people.csail.mit.edu/rrw/presentations/subset-conv.pdf
    .. [3] https://arxiv.org/pdf/1211.0189.pdf

    """
def inverse_mobius_transform(seq, subset: bool = True): ...
