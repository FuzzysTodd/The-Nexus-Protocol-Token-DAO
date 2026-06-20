from _typeshed import Incomplete
from pyu2f import errors as errors, u2f as u2f
from pyu2f.convenience import baseauthenticator as baseauthenticator

class LocalAuthenticator(baseauthenticator.BaseAuthenticator):
    """Authenticator wrapper around the native python u2f implementation."""
    origin: Incomplete
    def __init__(self, origin) -> None: ...
    def Authenticate(self, app_id, challenge_data, print_callback=...):
        """See base class."""
    def IsAvailable(self):
        """See base class."""
