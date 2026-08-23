from . import sign_string as sign_string
from _typeshed import Incomplete
from azure.core.exceptions import ClientAuthenticationError
from azure.core.pipeline.policies import SansIOHTTPPolicy

logger: Incomplete

class AzureSigningError(ClientAuthenticationError):
    """
    Represents a fatal error when attempting to sign a request.
    In general, the cause of this exception is user error. For example, the given account key is not valid.
    Please visit https://docs.microsoft.com/en-us/azure/storage/common/storage-create-storage-account for more info.
    """

class SharedKeyCredentialPolicy(SansIOHTTPPolicy):
    account_name: Incomplete
    account_key: Incomplete
    def __init__(self, account_name, account_key) -> None: ...
    def on_request(self, request) -> None: ...

class StorageHttpChallenge:
    authorization_uri: Incomplete
    resource_id: Incomplete
    tenant_id: Incomplete
    def __init__(self, challenge) -> None:
        """ Parses an HTTP WWW-Authentication Bearer challenge from the Storage service. """
    def get_value(self, key): ...
