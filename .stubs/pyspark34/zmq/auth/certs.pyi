import os
from typing import Dict, Tuple

__all__ = ['create_certificates', 'load_certificate', 'load_certificates']

def create_certificates(key_dir: str | os.PathLike, name: str, metadata: Dict[str, str] | None = None) -> Tuple[str, str]:
    """Create zmq certificates.

    Returns the file paths to the public and secret certificate files.
    """
def load_certificate(filename: str | os.PathLike) -> Tuple[bytes, bytes | None]:
    """Load public and secret key from a zmq certificate.

    Returns (public_key, secret_key)

    If the certificate file only contains the public key,
    secret_key will be None.

    If there is no public key found in the file, ValueError will be raised.
    """
def load_certificates(directory: str | os.PathLike = '.') -> Dict[bytes, bool]:
    """Load public keys from all certificates in a directory"""
