from typing import Tuple

__all__ = ['crypto_kx_keypair', 'crypto_kx_client_session_keys', 'crypto_kx_server_session_keys', 'crypto_kx_PUBLIC_KEY_BYTES', 'crypto_kx_SECRET_KEY_BYTES', 'crypto_kx_SEED_BYTES', 'crypto_kx_SESSION_KEY_BYTES']

crypto_kx_PUBLIC_KEY_BYTES: int
crypto_kx_SECRET_KEY_BYTES: int
crypto_kx_SEED_BYTES: int
crypto_kx_SESSION_KEY_BYTES: int

def crypto_kx_keypair() -> Tuple[bytes, bytes]:
    """
    Generate a keypair.
    This is a duplicate crypto_box_keypair, but
    is included for api consistency.
    :return: (public_key, secret_key)
    :rtype: (bytes, bytes)
    """
def crypto_kx_client_session_keys(client_public_key: bytes, client_secret_key: bytes, server_public_key: bytes) -> Tuple[bytes, bytes]:
    """
    Generate session keys for the client.
    :param client_public_key:
    :type client_public_key: bytes
    :param client_secret_key:
    :type client_secret_key: bytes
    :param server_public_key:
    :type server_public_key: bytes
    :return: (rx_key, tx_key)
    :rtype: (bytes, bytes)
    """
def crypto_kx_server_session_keys(server_public_key: bytes, server_secret_key: bytes, client_public_key: bytes) -> Tuple[bytes, bytes]:
    """
    Generate session keys for the server.
    :param server_public_key:
    :type server_public_key: bytes
    :param server_secret_key:
    :type server_secret_key: bytes
    :param client_public_key:
    :type client_public_key: bytes
    :return: (rx_key, tx_key)
    :rtype: (bytes, bytes)
    """
