__all__ = ['has', 'curve_keypair', 'curve_public']

def has(capability):
    """Check for zmq capability by name (e.g. 'ipc', 'curve')

    .. versionadded:: libzmq-4.1
    .. versionadded:: 14.1
    """
def curve_keypair():
    """generate a Z85 key pair for use with zmq.CURVE security

    Requires libzmq (≥ 4.0) to have been built with CURVE support.

    Returns
    -------
    (public, secret) : two bytestrings
        The public and private key pair as 40 byte z85-encoded bytestrings.
    """
def curve_public(private):
    """Compute the public key corresponding to a private key for use
    with zmq.CURVE security

    Requires libzmq (≥ 4.2) to have been built with CURVE support.

    Parameters
    ----------
    private
        The private key as a 40 byte z85-encoded bytestring
    Returns
    -------
    bytestring
        The public key as a 40 byte z85-encoded bytestring.
    """
