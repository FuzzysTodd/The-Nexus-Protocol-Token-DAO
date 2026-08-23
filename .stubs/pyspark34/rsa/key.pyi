import typing
from _typeshed import Incomplete

__all__ = ['PublicKey', 'PrivateKey', 'newkeys']

T = typing.TypeVar('T', bound='AbstractKey')

class AbstractKey:
    """Abstract superclass for private and public keys."""
    n: Incomplete
    e: Incomplete
    blindfac: int
    mutex: Incomplete
    def __init__(self, n: int, e: int) -> None: ...
    @classmethod
    def load_pkcs1(cls, keyfile: bytes, format: str = 'PEM') -> T:
        """Loads a key in PKCS#1 DER or PEM format.

        :param keyfile: contents of a DER- or PEM-encoded file that contains
            the key.
        :type keyfile: bytes
        :param format: the format of the file to load; 'PEM' or 'DER'
        :type format: str

        :return: the loaded key
        :rtype: AbstractKey
        """
    def save_pkcs1(self, format: str = 'PEM') -> bytes:
        """Saves the key in PKCS#1 DER or PEM format.

        :param format: the format to save; 'PEM' or 'DER'
        :type format: str
        :returns: the DER- or PEM-encoded key.
        :rtype: bytes
        """
    def blind(self, message: int) -> typing.Tuple[int, int]:
        """Performs blinding on the message.

        :param message: the message, as integer, to blind.
        :param r: the random number to blind with.
        :return: tuple (the blinded message, the inverse of the used blinding factor)

        The blinding is such that message = unblind(decrypt(blind(encrypt(message))).

        See https://en.wikipedia.org/wiki/Blinding_%28cryptography%29
        """
    def unblind(self, blinded: int, blindfac_inverse: int) -> int:
        """Performs blinding on the message using random number 'blindfac_inverse'.

        :param blinded: the blinded message, as integer, to unblind.
        :param blindfac: the factor to unblind with.
        :return: the original message.

        The blinding is such that message = unblind(decrypt(blind(encrypt(message))).

        See https://en.wikipedia.org/wiki/Blinding_%28cryptography%29
        """

class PublicKey(AbstractKey):
    """Represents a public RSA key.

    This key is also known as the 'encryption key'. It contains the 'n' and 'e'
    values.

    Supports attributes as well as dictionary-like access. Attribute access is
    faster, though.

    >>> PublicKey(5, 3)
    PublicKey(5, 3)

    >>> key = PublicKey(5, 3)
    >>> key.n
    5
    >>> key['n']
    5
    >>> key.e
    3
    >>> key['e']
    3

    """
    def __getitem__(self, key: str) -> int: ...
    def __eq__(self, other: typing.Any) -> bool: ...
    def __ne__(self, other: typing.Any) -> bool: ...
    def __hash__(self) -> int: ...
    @classmethod
    def load_pkcs1_openssl_pem(cls, keyfile: bytes) -> PublicKey:
        '''Loads a PKCS#1.5 PEM-encoded public key file from OpenSSL.

        These files can be recognised in that they start with BEGIN PUBLIC KEY
        rather than BEGIN RSA PUBLIC KEY.

        The contents of the file before the "-----BEGIN PUBLIC KEY-----" and
        after the "-----END PUBLIC KEY-----" lines is ignored.

        :param keyfile: contents of a PEM-encoded file that contains the public
            key, from OpenSSL.
        :type keyfile: bytes
        :return: a PublicKey object
        '''
    @classmethod
    def load_pkcs1_openssl_der(cls, keyfile: bytes) -> PublicKey:
        """Loads a PKCS#1 DER-encoded public key file from OpenSSL.

        :param keyfile: contents of a DER-encoded file that contains the public
            key, from OpenSSL.
        :return: a PublicKey object
        """

class PrivateKey(AbstractKey):
    """Represents a private RSA key.

    This key is also known as the 'decryption key'. It contains the 'n', 'e',
    'd', 'p', 'q' and other values.

    Supports attributes as well as dictionary-like access. Attribute access is
    faster, though.

    >>> PrivateKey(3247, 65537, 833, 191, 17)
    PrivateKey(3247, 65537, 833, 191, 17)

    exp1, exp2 and coef will be calculated:

    >>> pk = PrivateKey(3727264081, 65537, 3349121513, 65063, 57287)
    >>> pk.exp1
    55063
    >>> pk.exp2
    10095
    >>> pk.coef
    50797

    """
    d: Incomplete
    p: Incomplete
    q: Incomplete
    exp1: Incomplete
    exp2: Incomplete
    coef: Incomplete
    def __init__(self, n: int, e: int, d: int, p: int, q: int) -> None: ...
    def __getitem__(self, key: str) -> int: ...
    def __eq__(self, other: typing.Any) -> bool: ...
    def __ne__(self, other: typing.Any) -> bool: ...
    def __hash__(self) -> int: ...
    def blinded_decrypt(self, encrypted: int) -> int:
        """Decrypts the message using blinding to prevent side-channel attacks.

        :param encrypted: the encrypted message
        :type encrypted: int

        :returns: the decrypted message
        :rtype: int
        """
    def blinded_encrypt(self, message: int) -> int:
        """Encrypts the message using blinding to prevent side-channel attacks.

        :param message: the message to encrypt
        :type message: int

        :returns: the encrypted message
        :rtype: int
        """

def newkeys(nbits: int, accurate: bool = True, poolsize: int = 1, exponent: int = ...) -> typing.Tuple[PublicKey, PrivateKey]:
    """Generates public and private keys, and returns them as (pub, priv).

    The public key is also known as the 'encryption key', and is a
    :py:class:`rsa.PublicKey` object. The private key is also known as the
    'decryption key' and is a :py:class:`rsa.PrivateKey` object.

    :param nbits: the number of bits required to store ``n = p*q``.
    :param accurate: when True, ``n`` will have exactly the number of bits you
        asked for. However, this makes key generation much slower. When False,
        `n`` may have slightly less bits.
    :param poolsize: the number of processes to use to generate the prime
        numbers. If set to a number > 1, a parallel algorithm will be used.
        This requires Python 2.6 or newer.
    :param exponent: the exponent for the key; only change this if you know
        what you're doing, as the exponent influences how difficult your
        private key can be cracked. A very common choice for e is 65537.
    :type exponent: int

    :returns: a tuple (:py:class:`rsa.PublicKey`, :py:class:`rsa.PrivateKey`)

    The ``poolsize`` parameter was added in *Python-RSA 3.1* and requires
    Python 2.6 or newer.

    """
