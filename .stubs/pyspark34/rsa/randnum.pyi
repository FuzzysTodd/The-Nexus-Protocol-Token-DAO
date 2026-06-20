from rsa import common as common, transform as transform

def read_random_bits(nbits: int) -> bytes:
    """Reads 'nbits' random bits.

    If nbits isn't a whole number of bytes, an extra byte will be appended with
    only the lower bits set.
    """
def read_random_int(nbits: int) -> int:
    """Reads a random integer of approximately nbits bits."""
def read_random_odd_int(nbits: int) -> int:
    """Reads a random odd integer of approximately nbits bits.

    >>> read_random_odd_int(512) & 1
    1
    """
def randint(maxvalue: int) -> int:
    """Returns a random integer x with 1 <= x <= maxvalue

    May take a very long time in specific situations. If maxvalue needs N bits
    to store, the closer maxvalue is to (2 ** N) - 1, the faster this function
    is.
    """
