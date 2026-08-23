__all__ = ['getprime']

def getprime(nbits: int, poolsize: int) -> int:
    """Returns a prime number that can be stored in 'nbits' bits.

    Works in multiple threads at the same time.

    >>> p = getprime(128, 3)
    >>> rsa.prime.is_prime(p-1)
    False
    >>> rsa.prime.is_prime(p)
    True
    >>> rsa.prime.is_prime(p+1)
    False

    >>> from rsa import common
    >>> common.bit_size(p) == 128
    True

    """
