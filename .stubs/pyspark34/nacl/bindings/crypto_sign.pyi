from _typeshed import Incomplete
from nacl._sodium import ffi as ffi, lib as lib
from nacl.exceptions import ensure as ensure
from typing import Tuple

crypto_sign_BYTES: int
crypto_sign_SEEDBYTES: int
crypto_sign_PUBLICKEYBYTES: int
crypto_sign_SECRETKEYBYTES: int
crypto_sign_curve25519_BYTES: int
crypto_sign_ed25519ph_STATEBYTES: int

def crypto_sign_keypair() -> Tuple[bytes, bytes]:
    """
    Returns a randomly generated public key and secret key.

    :rtype: (bytes(public_key), bytes(secret_key))
    """
def crypto_sign_seed_keypair(seed: bytes) -> Tuple[bytes, bytes]:
    """
    Computes and returns the public key and secret key using the seed ``seed``.

    :param seed: bytes
    :rtype: (bytes(public_key), bytes(secret_key))
    """
def crypto_sign(message: bytes, sk: bytes) -> bytes:
    """
    Signs the message ``message`` using the secret key ``sk`` and returns the
    signed message.

    :param message: bytes
    :param sk: bytes
    :rtype: bytes
    """
def crypto_sign_open(signed: bytes, pk: bytes) -> bytes:
    """
    Verifies the signature of the signed message ``signed`` using the public
    key ``pk`` and returns the unsigned message.

    :param signed: bytes
    :param pk: bytes
    :rtype: bytes
    """
def crypto_sign_ed25519_pk_to_curve25519(public_key_bytes: bytes) -> bytes:
    """
    Converts a public Ed25519 key (encoded as bytes ``public_key_bytes``) to
    a public Curve25519 key as bytes.

    Raises a ValueError if ``public_key_bytes`` is not of length
    ``crypto_sign_PUBLICKEYBYTES``

    :param public_key_bytes: bytes
    :rtype: bytes
    """
def crypto_sign_ed25519_sk_to_curve25519(secret_key_bytes: bytes) -> bytes:
    """
    Converts a secret Ed25519 key (encoded as bytes ``secret_key_bytes``) to
    a secret Curve25519 key as bytes.

    Raises a ValueError if ``secret_key_bytes``is not of length
    ``crypto_sign_SECRETKEYBYTES``

    :param secret_key_bytes: bytes
    :rtype: bytes
    """
def crypto_sign_ed25519_sk_to_pk(secret_key_bytes: bytes) -> bytes:
    """
    Extract the public Ed25519 key from a secret Ed25519 key (encoded
    as bytes ``secret_key_bytes``).

    Raises a ValueError if ``secret_key_bytes``is not of length
    ``crypto_sign_SECRETKEYBYTES``

    :param secret_key_bytes: bytes
    :rtype: bytes
    """
def crypto_sign_ed25519_sk_to_seed(secret_key_bytes: bytes) -> bytes:
    """
    Extract the seed from a secret Ed25519 key (encoded
    as bytes ``secret_key_bytes``).

    Raises a ValueError if ``secret_key_bytes``is not of length
    ``crypto_sign_SECRETKEYBYTES``

    :param secret_key_bytes: bytes
    :rtype: bytes
    """

class crypto_sign_ed25519ph_state:
    """
    State object wrapping the sha-512 state used in ed25519ph computation
    """
    state: Incomplete
    def __init__(self) -> None: ...

def crypto_sign_ed25519ph_update(edph: crypto_sign_ed25519ph_state, pmsg: bytes) -> None:
    """
    Update the hash state wrapped in edph

    :param edph: the ed25519ph state being updated
    :type edph: crypto_sign_ed25519ph_state
    :param pmsg: the partial message
    :type pmsg: bytes
    :rtype: None
    """
def crypto_sign_ed25519ph_final_create(edph: crypto_sign_ed25519ph_state, sk: bytes) -> bytes:
    """
    Create a signature for the data hashed in edph
    using the secret key sk

    :param edph: the ed25519ph state for the data
                 being signed
    :type edph: crypto_sign_ed25519ph_state
    :param sk: the ed25519 secret part of the signing key
    :type sk: bytes
    :return: ed25519ph signature
    :rtype: bytes
    """
def crypto_sign_ed25519ph_final_verify(edph: crypto_sign_ed25519ph_state, signature: bytes, pk: bytes) -> bool:
    """
    Verify a prehashed signature using the public key pk

    :param edph: the ed25519ph state for the data
                 being verified
    :type edph: crypto_sign_ed25519ph_state
    :param signature: the signature being verified
    :type signature: bytes
    :param pk: the ed25519 public part of the signing key
    :type pk: bytes
    :return: True if the signature is valid
    :rtype: boolean
    :raises exc.BadSignatureError: if the signature is not valid
    """
