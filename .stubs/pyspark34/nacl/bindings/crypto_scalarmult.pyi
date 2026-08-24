from _typeshed import Incomplete
from nacl._sodium import ffi as ffi, lib as lib
from nacl.exceptions import ensure as ensure

has_crypto_scalarmult_ed25519: Incomplete
crypto_scalarmult_BYTES: int
crypto_scalarmult_SCALARBYTES: int
crypto_scalarmult_ed25519_BYTES: int
crypto_scalarmult_ed25519_SCALARBYTES: int

def crypto_scalarmult_base(n: bytes) -> bytes:
    """
    Computes and returns the scalar product of a standard group element and an
    integer ``n``.

    :param n: bytes
    :rtype: bytes
    """
def crypto_scalarmult(n: bytes, p: bytes) -> bytes:
    """
    Computes and returns the scalar product of the given group element and an
    integer ``n``.

    :param p: bytes
    :param n: bytes
    :rtype: bytes
    """
def crypto_scalarmult_ed25519_base(n: bytes) -> bytes:
    """
    Computes and returns the scalar product of a standard group element and an
    integer ``n`` on the edwards25519 curve.

    :param n: a :py:data:`.crypto_scalarmult_ed25519_SCALARBYTES` long bytes
              sequence representing a scalar
    :type n: bytes
    :return: a point on the edwards25519 curve, represented as a
             :py:data:`.crypto_scalarmult_ed25519_BYTES` long bytes sequence
    :rtype: bytes
    :raises nacl.exceptions.UnavailableError: If called when using a
        minimal build of libsodium.
    """
def crypto_scalarmult_ed25519_base_noclamp(n: bytes) -> bytes:
    """
    Computes and returns the scalar product of a standard group element and an
    integer ``n`` on the edwards25519 curve. The integer ``n`` is not clamped.

    :param n: a :py:data:`.crypto_scalarmult_ed25519_SCALARBYTES` long bytes
              sequence representing a scalar
    :type n: bytes
    :return: a point on the edwards25519 curve, represented as a
             :py:data:`.crypto_scalarmult_ed25519_BYTES` long bytes sequence
    :rtype: bytes
    :raises nacl.exceptions.UnavailableError: If called when using a
        minimal build of libsodium.
    """
def crypto_scalarmult_ed25519(n: bytes, p: bytes) -> bytes:
    """
    Computes and returns the scalar product of a *clamped* integer ``n``
    and the given group element on the edwards25519 curve.
    The scalar is clamped, as done in the public key generation case,
    by setting to zero the bits in position [0, 1, 2, 255] and setting
    to one the bit in position 254.

    :param n: a :py:data:`.crypto_scalarmult_ed25519_SCALARBYTES` long bytes
              sequence representing a scalar
    :type n: bytes
    :param p: a :py:data:`.crypto_scalarmult_ed25519_BYTES` long bytes sequence
              representing a point on the edwards25519 curve
    :type p: bytes
    :return: a point on the edwards25519 curve, represented as a
             :py:data:`.crypto_scalarmult_ed25519_BYTES` long bytes sequence
    :rtype: bytes
    :raises nacl.exceptions.UnavailableError: If called when using a
        minimal build of libsodium.
    """
def crypto_scalarmult_ed25519_noclamp(n: bytes, p: bytes) -> bytes:
    """
    Computes and returns the scalar product of an integer ``n``
    and the given group element on the edwards25519 curve. The integer
    ``n`` is not clamped.

    :param n: a :py:data:`.crypto_scalarmult_ed25519_SCALARBYTES` long bytes
              sequence representing a scalar
    :type n: bytes
    :param p: a :py:data:`.crypto_scalarmult_ed25519_BYTES` long bytes sequence
              representing a point on the edwards25519 curve
    :type p: bytes
    :return: a point on the edwards25519 curve, represented as a
             :py:data:`.crypto_scalarmult_ed25519_BYTES` long bytes sequence
    :rtype: bytes
    :raises nacl.exceptions.UnavailableError: If called when using a
        minimal build of libsodium.
    """
