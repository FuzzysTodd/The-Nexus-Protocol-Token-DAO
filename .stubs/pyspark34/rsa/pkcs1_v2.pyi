__all__ = ['mgf1']

def mgf1(seed: bytes, length: int, hasher: str = 'SHA-1') -> bytes:
    """
    MGF1 is a Mask Generation Function based on a hash function.

    A mask generation function takes an octet string of variable length and a
    desired output length as input, and outputs an octet string of the desired
    length. The plaintext-awareness of RSAES-OAEP relies on the random nature of
    the output of the mask generation function, which in turn relies on the
    random nature of the underlying hash.

    :param bytes seed: seed from which mask is generated, an octet string
    :param int length: intended length in octets of the mask, at most 2^32(hLen)
    :param str hasher: hash function (hLen denotes the length in octets of the hash
        function output)

    :return: mask, an octet string of length `length`
    :rtype: bytes

    :raise OverflowError: when `length` is too large for the specified `hasher`
    :raise ValueError: when specified `hasher` is invalid
    """
