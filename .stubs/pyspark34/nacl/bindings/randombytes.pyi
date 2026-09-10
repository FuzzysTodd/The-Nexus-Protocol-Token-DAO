from nacl._sodium import ffi as ffi, lib as lib

randombytes_SEEDBYTES: int

def randombytes(size: int) -> bytes:
    """
    Returns ``size`` number of random bytes from a cryptographically secure
    random source.

    :param size: int
    :rtype: bytes
    """
def randombytes_buf_deterministic(size: int, seed: bytes) -> bytes:
    """
    Returns ``size`` number of deterministically generated pseudorandom bytes
    from a seed

    :param size: int
    :param seed: bytes
    :rtype: bytes
    """
