from . import key

__all__ = ['encrypt', 'decrypt', 'sign', 'verify', 'DecryptionError', 'VerificationError', 'CryptoError']

class CryptoError(Exception):
    """Base class for all exceptions in this module."""
class DecryptionError(CryptoError):
    """Raised when decryption fails."""
class VerificationError(CryptoError):
    """Raised when verification fails."""

def encrypt(message: bytes, pub_key: key.PublicKey) -> bytes:
    """Encrypts the given message using PKCS#1 v1.5

    :param message: the message to encrypt. Must be a byte string no longer than
        ``k-11`` bytes, where ``k`` is the number of bytes needed to encode
        the ``n`` component of the public key.
    :param pub_key: the :py:class:`rsa.PublicKey` to encrypt with.
    :raise OverflowError: when the message is too large to fit in the padded
        block.

    >>> from rsa import key, common
    >>> (pub_key, priv_key) = key.newkeys(256)
    >>> message = b'hello'
    >>> crypto = encrypt(message, pub_key)

    The crypto text should be just as long as the public key 'n' component:

    >>> len(crypto) == common.byte_size(pub_key.n)
    True

    """
def decrypt(crypto: bytes, priv_key: key.PrivateKey) -> bytes:
    """Decrypts the given message using PKCS#1 v1.5

    The decryption is considered 'failed' when the resulting cleartext doesn't
    start with the bytes 00 02, or when the 00 byte between the padding and
    the message cannot be found.

    :param crypto: the crypto text as returned by :py:func:`rsa.encrypt`
    :param priv_key: the :py:class:`rsa.PrivateKey` to decrypt with.
    :raise DecryptionError: when the decryption fails. No details are given as
        to why the code thinks the decryption fails, as this would leak
        information about the private key.


    >>> import rsa
    >>> (pub_key, priv_key) = rsa.newkeys(256)

    It works with strings:

    >>> crypto = encrypt(b'hello', pub_key)
    >>> decrypt(crypto, priv_key)
    b'hello'

    And with binary data:

    >>> crypto = encrypt(b'\\x00\\x00\\x00\\x00\\x01', pub_key)
    >>> decrypt(crypto, priv_key)
    b'\\x00\\x00\\x00\\x00\\x01'

    Altering the encrypted information will *likely* cause a
    :py:class:`rsa.pkcs1.DecryptionError`. If you want to be *sure*, use
    :py:func:`rsa.sign`.


    .. warning::

        Never display the stack trace of a
        :py:class:`rsa.pkcs1.DecryptionError` exception. It shows where in the
        code the exception occurred, and thus leaks information about the key.
        It's only a tiny bit of information, but every bit makes cracking the
        keys easier.

    >>> crypto = encrypt(b'hello', pub_key)
    >>> crypto = crypto[0:5] + b'X' + crypto[6:] # change a byte
    >>> decrypt(crypto, priv_key)
    Traceback (most recent call last):
    ...
    rsa.pkcs1.DecryptionError: Decryption failed

    """
def sign(message: bytes, priv_key: key.PrivateKey, hash_method: str) -> bytes:
    '''Signs the message with the private key.

    Hashes the message, then signs the hash with the given key. This is known
    as a "detached signature", because the message itself isn\'t altered.

    :param message: the message to sign. Can be an 8-bit string or a file-like
        object. If ``message`` has a ``read()`` method, it is assumed to be a
        file-like object.
    :param priv_key: the :py:class:`rsa.PrivateKey` to sign with
    :param hash_method: the hash method used on the message. Use \'MD5\', \'SHA-1\',
        \'SHA-224\', SHA-256\', \'SHA-384\' or \'SHA-512\'.
    :return: a message signature block.
    :raise OverflowError: if the private key is too small to contain the
        requested hash.

    '''
def verify(message: bytes, signature: bytes, pub_key: key.PublicKey) -> str:
    """Verifies that the signature matches the message.

    The hash method is detected automatically from the signature.

    :param message: the signed message. Can be an 8-bit string or a file-like
        object. If ``message`` has a ``read()`` method, it is assumed to be a
        file-like object.
    :param signature: the signature block, as created with :py:func:`rsa.sign`.
    :param pub_key: the :py:class:`rsa.PublicKey` of the person signing the message.
    :raise VerificationError: when the signature doesn't match the message.
    :returns: the name of the used hash.

    """
