from typing import Tuple

__all__ = ['crypto_box_keypair', 'crypto_box']

def crypto_box_keypair() -> Tuple[bytes, bytes]:
    """
    Returns a randomly generated public and secret key.

    :rtype: (bytes(public_key), bytes(secret_key))
    """
def crypto_box(message: bytes, nonce: bytes, pk: bytes, sk: bytes) -> bytes:
    """
    Encrypts and returns a message ``message`` using the secret key ``sk``,
    public key ``pk``, and the nonce ``nonce``.

    :param message: bytes
    :param nonce: bytes
    :param pk: bytes
    :param sk: bytes
    :rtype: bytes
    """
