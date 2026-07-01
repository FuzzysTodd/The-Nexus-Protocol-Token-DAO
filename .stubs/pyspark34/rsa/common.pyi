import typing
from _typeshed import Incomplete

class NotRelativePrimeError(ValueError):
    a: Incomplete
    b: Incomplete
    d: Incomplete
    def __init__(self, a: int, b: int, d: int, msg: str = '') -> None: ...

def bit_size(num: int) -> int:
    """
    Number of bits needed to represent a integer excluding any prefix
    0 bits.

    Usage::

        >>> bit_size(1023)
        10
        >>> bit_size(1024)
        11
        >>> bit_size(1025)
        11

    :param num:
        Integer value. If num is 0, returns 0. Only the absolute value of the
        number is considered. Therefore, signed integers will be abs(num)
        before the number's bit length is determined.
    :returns:
        Returns the number of bits in the integer.
    """
def byte_size(number: int) -> int:
    """
    Returns the number of bytes required to hold a specific long number.

    The number of bytes is rounded up.

    Usage::

        >>> byte_size(1 << 1023)
        128
        >>> byte_size((1 << 1024) - 1)
        128
        >>> byte_size(1 << 1024)
        129

    :param number:
        An unsigned integer
    :returns:
        The number of bytes required to hold a specific long number.
    """
def ceil_div(num: int, div: int) -> int:
    """
    Returns the ceiling function of a division between `num` and `div`.

    Usage::

        >>> ceil_div(100, 7)
        15
        >>> ceil_div(100, 10)
        10
        >>> ceil_div(1, 4)
        1

    :param num: Division's numerator, a number
    :param div: Division's divisor, a number

    :return: Rounded up result of the division between the parameters.
    """
def extended_gcd(a: int, b: int) -> typing.Tuple[int, int, int]:
    """Returns a tuple (r, i, j) such that r = gcd(a, b) = ia + jb"""
def inverse(x: int, n: int) -> int:
    """Returns the inverse of x % n under multiplication, a.k.a x^-1 (mod n)

    >>> inverse(7, 4)
    3
    >>> (inverse(143, 4) * 143) % 4
    1
    """
def crt(a_values: typing.Iterable[int], modulo_values: typing.Iterable[int]) -> int:
    """Chinese Remainder Theorem.

    Calculates x such that x = a[i] (mod m[i]) for each i.

    :param a_values: the a-values of the above equation
    :param modulo_values: the m-values of the above equation
    :returns: x such that x = a[i] (mod m[i]) for each i


    >>> crt([2, 3], [3, 5])
    8

    >>> crt([2, 3, 2], [3, 5, 7])
    23

    >>> crt([2, 3, 0], [7, 11, 15])
    135
    """
