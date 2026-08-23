from _typeshed import Incomplete
from nacl._sodium import ffi as ffi, lib as lib
from nacl.exceptions import ensure as ensure
from typing import Tuple

crypto_secretstream_xchacha20poly1305_ABYTES: int
crypto_secretstream_xchacha20poly1305_HEADERBYTES: int
crypto_secretstream_xchacha20poly1305_KEYBYTES: int
crypto_secretstream_xchacha20poly1305_MESSAGEBYTES_MAX: int
crypto_secretstream_xchacha20poly1305_STATEBYTES: int
crypto_secretstream_xchacha20poly1305_TAG_MESSAGE: int
crypto_secretstream_xchacha20poly1305_TAG_PUSH: int
crypto_secretstream_xchacha20poly1305_TAG_REKEY: int
crypto_secretstream_xchacha20poly1305_TAG_FINAL: int

def crypto_secretstream_xchacha20poly1305_keygen() -> bytes:
    """
    Generate a key for use with
    :func:`.crypto_secretstream_xchacha20poly1305_init_push`.

    """

class crypto_secretstream_xchacha20poly1305_state:
    """
    An object wrapping the crypto_secretstream_xchacha20poly1305 state.

    """
    statebuf: Incomplete
    rawbuf: Incomplete
    tagbuf: Incomplete
    def __init__(self) -> None:
        """Initialize a clean state object."""

def crypto_secretstream_xchacha20poly1305_init_push(state: crypto_secretstream_xchacha20poly1305_state, key: bytes) -> bytes:
    """
    Initialize a crypto_secretstream_xchacha20poly1305 encryption buffer.

    :param state: a secretstream state object
    :type state: crypto_secretstream_xchacha20poly1305_state
    :param key: must be
                :data:`.crypto_secretstream_xchacha20poly1305_KEYBYTES` long
    :type key: bytes
    :return: header
    :rtype: bytes

    """
def crypto_secretstream_xchacha20poly1305_push(state: crypto_secretstream_xchacha20poly1305_state, m: bytes, ad: bytes | None = None, tag: int = ...) -> bytes:
    """
    Add an encrypted message to the secret stream.

    :param state: a secretstream state object
    :type state: crypto_secretstream_xchacha20poly1305_state
    :param m: the message to encrypt, the maximum length of an individual
              message is
              :data:`.crypto_secretstream_xchacha20poly1305_MESSAGEBYTES_MAX`.
    :type m: bytes
    :param ad: additional data to include in the authentication tag
    :type ad: bytes or None
    :param tag: the message tag, usually
                :data:`.crypto_secretstream_xchacha20poly1305_TAG_MESSAGE` or
                :data:`.crypto_secretstream_xchacha20poly1305_TAG_FINAL`.
    :type tag: int
    :return: ciphertext
    :rtype: bytes

    """
def crypto_secretstream_xchacha20poly1305_init_pull(state: crypto_secretstream_xchacha20poly1305_state, header: bytes, key: bytes) -> None:
    """
    Initialize a crypto_secretstream_xchacha20poly1305 decryption buffer.

    :param state: a secretstream state object
    :type state: crypto_secretstream_xchacha20poly1305_state
    :param header: must be
                :data:`.crypto_secretstream_xchacha20poly1305_HEADERBYTES` long
    :type header: bytes
    :param key: must be
                :data:`.crypto_secretstream_xchacha20poly1305_KEYBYTES` long
    :type key: bytes

    """
def crypto_secretstream_xchacha20poly1305_pull(state: crypto_secretstream_xchacha20poly1305_state, c: bytes, ad: bytes | None = None) -> Tuple[bytes, int]:
    """
    Read a decrypted message from the secret stream.

    :param state: a secretstream state object
    :type state: crypto_secretstream_xchacha20poly1305_state
    :param c: the ciphertext to decrypt, the maximum length of an individual
              ciphertext is
              :data:`.crypto_secretstream_xchacha20poly1305_MESSAGEBYTES_MAX` +
              :data:`.crypto_secretstream_xchacha20poly1305_ABYTES`.
    :type c: bytes
    :param ad: additional data to include in the authentication tag
    :type ad: bytes or None
    :return: (message, tag)
    :rtype: (bytes, int)

    """
def crypto_secretstream_xchacha20poly1305_rekey(state: crypto_secretstream_xchacha20poly1305_state) -> None:
    """
    Explicitly change the encryption key in the stream.

    Normally the stream is re-keyed as needed or an explicit ``tag`` of
    :data:`.crypto_secretstream_xchacha20poly1305_TAG_REKEY` is added to a
    message to ensure forward secrecy, but this method can be used instead
    if the re-keying is controlled without adding the tag.

    :param state: a secretstream state object
    :type state: crypto_secretstream_xchacha20poly1305_state

    """
