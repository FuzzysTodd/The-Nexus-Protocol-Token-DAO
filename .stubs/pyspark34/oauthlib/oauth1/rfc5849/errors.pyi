from _typeshed import Incomplete
from oauthlib.common import add_params_to_uri as add_params_to_uri, urlencode as urlencode

class OAuth1Error(Exception):
    error: Incomplete
    description: str
    uri: Incomplete
    status_code: Incomplete
    def __init__(self, description: Incomplete | None = None, uri: Incomplete | None = None, status_code: int = 400, request: Incomplete | None = None) -> None:
        '''
        description:    A human-readable ASCII [USASCII] text providing
                        additional information, used to assist the client
                        developer in understanding the error that occurred.
                        Values for the "error_description" parameter MUST NOT
                        include characters outside the set
                        x20-21 / x23-5B / x5D-7E.

        uri:    A URI identifying a human-readable web page with information
                about the error, used to provide the client developer with
                additional information about the error.  Values for the
                "error_uri" parameter MUST conform to the URI- Reference
                syntax, and thus MUST NOT include characters outside the set
                x21 / x23-5B / x5D-7E.

        state:  A CSRF protection value received from the client.

        request:  Oauthlib Request object
        '''
    def in_uri(self, uri): ...
    @property
    def twotuples(self): ...
    @property
    def urlencoded(self): ...

class InsecureTransportError(OAuth1Error):
    error: str
    description: str

class InvalidSignatureMethodError(OAuth1Error):
    error: str

class InvalidRequestError(OAuth1Error):
    error: str

class InvalidClientError(OAuth1Error):
    error: str
