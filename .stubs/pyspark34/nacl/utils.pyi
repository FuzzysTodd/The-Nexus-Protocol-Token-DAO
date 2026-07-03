from nacl import encoding as encoding

class EncryptedMessage(bytes):
    """
    A bytes subclass that holds a messaged that has been encrypted by a
    :class:`SecretBox`.
    """
    @property
    def nonce(self) -> bytes:
        """
        The nonce used during the encryption of the :class:`EncryptedMessage`.
        """
    @property
    def ciphertext(self) -> bytes:
        """
        The ciphertext contained within the :class:`EncryptedMessage`.
        """

class StringFixer: ...

def bytes_as_string(bytes_in: bytes) -> str: ...
def random(size: int = 32) -> bytes: ...
def randombytes_deterministic(size: int, seed: bytes, encoder: encoding.Encoder = ...) -> bytes:
    """
    Returns ``size`` number of deterministically generated pseudorandom bytes
    from a seed

    :param size: int
    :param seed: bytes
    :param encoder: The encoder class used to encode the produced bytes
    :rtype: bytes
    """
