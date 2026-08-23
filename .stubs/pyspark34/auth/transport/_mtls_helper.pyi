from _typeshed import Incomplete

CONTEXT_AWARE_METADATA_PATH: str

def get_client_ssl_credentials(generate_encrypted_key: bool = False, context_aware_metadata_path=...):
    """Returns the client side certificate, private key and passphrase.

    Args:
        generate_encrypted_key (bool): If set to True, encrypted private key
            and passphrase will be generated; otherwise, unencrypted private key
            will be generated and passphrase will be None.
        context_aware_metadata_path (str): The context_aware_metadata.json file path.

    Returns:
        Tuple[bool, bytes, bytes, bytes]:
            A boolean indicating if cert, key and passphrase are obtained, the
            cert bytes and key bytes both in PEM format, and passphrase bytes.

    Raises:
        google.auth.exceptions.ClientCertError: if problems occurs when getting
            the cert, key and passphrase.
    """
def get_client_cert_and_key(client_cert_callback: Incomplete | None = None):
    """Returns the client side certificate and private key. The function first
    tries to get certificate and key from client_cert_callback; if the callback
    is None or doesn't provide certificate and key, the function tries application
    default SSL credentials.

    Args:
        client_cert_callback (Optional[Callable[[], (bytes, bytes)]]): An
            optional callback which returns client certificate bytes and private
            key bytes both in PEM format.

    Returns:
        Tuple[bool, bytes, bytes]:
            A boolean indicating if cert and key are obtained, the cert bytes
            and key bytes both in PEM format.

    Raises:
        google.auth.exceptions.ClientCertError: if problems occurs when getting
            the cert and key.
    """
def decrypt_private_key(key, passphrase):
    """A helper function to decrypt the private key with the given passphrase.
    google-auth library doesn't support passphrase protected private key for
    mutual TLS channel. This helper function can be used to decrypt the
    passphrase protected private key in order to estalish mutual TLS channel.

    For example, if you have a function which produces client cert, passphrase
    protected private key and passphrase, you can convert it to a client cert
    callback function accepted by google-auth::

        from google.auth.transport import _mtls_helper

        def your_client_cert_function():
            return cert, encrypted_key, passphrase

        # callback accepted by google-auth for mutual TLS channel.
        def client_cert_callback():
            cert, encrypted_key, passphrase = your_client_cert_function()
            decrypted_key = _mtls_helper.decrypt_private_key(encrypted_key,
                passphrase)
            return cert, decrypted_key

    Args:
        key (bytes): The private key bytes in PEM format.
        passphrase (bytes): The passphrase bytes.

    Returns:
        bytes: The decrypted private key in PEM format.

    Raises:
        ImportError: If pyOpenSSL is not installed.
        OpenSSL.crypto.Error: If there is any problem decrypting the private key.
    """
