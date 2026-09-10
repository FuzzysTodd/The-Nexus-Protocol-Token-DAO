from _typeshed import Incomplete
from pyu2f.convenience import baseauthenticator as baseauthenticator, customauthenticator as customauthenticator, localauthenticator as localauthenticator

def CreateCompositeAuthenticator(origin): ...

class CompositeAuthenticator(baseauthenticator.BaseAuthenticator):
    """Composes multiple authenticators into a single authenticator.

  Priority is based on the order of the list initialized with the instance.
  """
    authenticators: Incomplete
    def __init__(self, authenticators) -> None: ...
    def Authenticate(self, app_id, challenge_data, print_callback=...):
        """See base class."""
    def IsAvailable(self):
        """See base class."""
