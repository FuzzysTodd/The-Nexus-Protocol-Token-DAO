from _typeshed import Incomplete

logger: Incomplete

class AssertionCreator:
    def create_normal_assertion(self, audience, issuer, subject, expires_at: Incomplete | None = None, expires_in: int = 600, issued_at: Incomplete | None = None, assertion_id: Incomplete | None = None, **kwargs) -> None:
        """Create an assertion in bytes, based on the provided claims.

        All parameter names are defined in https://tools.ietf.org/html/rfc7521#section-5
        except the expires_in is defined here as lifetime-in-seconds,
        which will be automatically translated into expires_at in UTC.
        """
    def create_regenerative_assertion(self, audience, issuer, subject: Incomplete | None = None, expires_in: int = 600, **kwargs):
        """Create an assertion as a callable,
        which will then compute the assertion later when necessary.

        This is a useful optimization to reuse the client assertion.
        """

class AutoRefresher:
    """Cache the output of a factory, and auto-refresh it when necessary. Usage::

        r = AutoRefresher(time.time, expires_in=5)
        for i in range(15):
            print(r())  # the timestamp change only after every 5 seconds
            time.sleep(1)
    """
    def __init__(self, factory, expires_in: int = 540) -> None: ...
    def __call__(self): ...

class JwtAssertionCreator(AssertionCreator):
    key: Incomplete
    algorithm: Incomplete
    headers: Incomplete
    def __init__(self, key, algorithm, sha1_thumbprint: Incomplete | None = None, headers: Incomplete | None = None) -> None:
        '''Construct a Jwt assertion creator.

        Args:

            key (str):
                An unencrypted private key for signing, in a base64 encoded string.
                It can also be a cryptography ``PrivateKey`` object,
                which is how you can work with a previously-encrypted key.
                See also https://github.com/jpadilla/pyjwt/pull/525
            algorithm (str):
                "RS256", etc.. See https://pyjwt.readthedocs.io/en/latest/algorithms.html
                RSA and ECDSA algorithms require "pip install cryptography".
            sha1_thumbprint (str): The x5t aka X.509 certificate SHA-1 thumbprint.
            headers (dict): Additional headers, e.g. "kid" or "x5c" etc.
        '''
    def create_normal_assertion(self, audience, issuer, subject: Incomplete | None = None, expires_at: Incomplete | None = None, expires_in: int = 600, issued_at: Incomplete | None = None, assertion_id: Incomplete | None = None, not_before: Incomplete | None = None, additional_claims: Incomplete | None = None, **kwargs):
        """Create a JWT Assertion.

        Parameters are defined in https://tools.ietf.org/html/rfc7523#section-3
        Key-value pairs in additional_claims will be added into payload as-is.
        """
Signer = AssertionCreator
JwtSigner = JwtAssertionCreator
