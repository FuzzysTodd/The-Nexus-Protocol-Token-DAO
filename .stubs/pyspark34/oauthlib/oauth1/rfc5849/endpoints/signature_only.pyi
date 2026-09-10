from .. import errors as errors
from .base import BaseEndpoint as BaseEndpoint
from _typeshed import Incomplete

log: Incomplete

class SignatureOnlyEndpoint(BaseEndpoint):
    """An endpoint only responsible for verifying an oauth signature."""
    def validate_request(self, uri, http_method: str = 'GET', body: Incomplete | None = None, headers: Incomplete | None = None):
        """Validate a signed OAuth request.

        :param uri: The full URI of the token request.
        :param http_method: A valid HTTP verb, i.e. GET, POST, PUT, HEAD, etc.
        :param body: The request body as a string.
        :param headers: The request headers as a dict.
        :returns: A tuple of 2 elements.
                  1. True if valid, False otherwise.
                  2. An oauthlib.common.Request object.
        """
