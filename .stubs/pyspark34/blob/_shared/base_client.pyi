from .._version import VERSION as VERSION
from .authentication import SharedKeyCredentialPolicy as SharedKeyCredentialPolicy
from .constants import CONNECTION_TIMEOUT as CONNECTION_TIMEOUT, READ_TIMEOUT as READ_TIMEOUT, SERVICE_HOST_BASE as SERVICE_HOST_BASE
from .models import LocationMode as LocationMode
from .policies import ExponentialRetry as ExponentialRetry, QueueMessagePolicy as QueueMessagePolicy, StorageBearerTokenCredentialPolicy as StorageBearerTokenCredentialPolicy, StorageContentValidation as StorageContentValidation, StorageHeadersPolicy as StorageHeadersPolicy, StorageHosts as StorageHosts, StorageLoggingPolicy as StorageLoggingPolicy, StorageRequestHook as StorageRequestHook, StorageResponseHook as StorageResponseHook
from .request_handlers import serialize_batch_body as serialize_batch_body
from .response_handlers import PartialBatchErrorException as PartialBatchErrorException, process_storage_error as process_storage_error
from .shared_access_signature import QueryStringConstants as QueryStringConstants
from _typeshed import Incomplete
from azure.core.configuration import Configuration
from azure.core.credentials import AzureNamedKeyCredential, AzureSasCredential, TokenCredential as TokenCredential
from azure.core.pipeline.transport import HttpTransport
from typing import Any, Dict

class StorageAccountHostsMixin:
    scheme: Incomplete
    account_name: Incomplete
    credential: Incomplete
    def __init__(self, parsed_url: Any, service: str, credential: str | Dict[str, str] | AzureNamedKeyCredential | AzureSasCredential | TokenCredential | None = None, **kwargs: Any) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *args) -> None: ...
    def close(self) -> None:
        """ This method is to close the sockets opened by the client.
        It need not be used when using with a context manager.
        """
    @property
    def url(self):
        """The full endpoint URL to this entity, including SAS token if used.

        This could be either the primary endpoint,
        or the secondary endpoint depending on the current :func:`location_mode`.
        :returns: The full endpoint URL to this entity, including SAS token if used.
        :rtype: str
        """
    @property
    def primary_endpoint(self):
        """The full primary endpoint URL.

        :type: str
        """
    @property
    def primary_hostname(self):
        """The hostname of the primary endpoint.

        :type: str
        """
    @property
    def secondary_endpoint(self):
        """The full secondary endpoint URL if configured.

        If not available a ValueError will be raised. To explicitly specify a secondary hostname, use the optional
        `secondary_hostname` keyword argument on instantiation.

        :type: str
        :raise ValueError:
        """
    @property
    def secondary_hostname(self):
        """The hostname of the secondary endpoint.

        If not available this will be None. To explicitly specify a secondary hostname, use the optional
        `secondary_hostname` keyword argument on instantiation.

        :type: str or None
        """
    @property
    def location_mode(self):
        '''The location mode that the client is currently using.

        By default this will be "primary". Options include "primary" and "secondary".

        :type: str
        '''
    @location_mode.setter
    def location_mode(self, value) -> None: ...
    @property
    def api_version(self):
        """The version of the Storage API used for requests.

        :type: str
        """

class TransportWrapper(HttpTransport):
    """Wrapper class that ensures that an inner client created
    by a `get_client` method does not close the outer transport for the parent
    when used in a context manager.
    """
    def __init__(self, transport) -> None: ...
    def send(self, request, **kwargs): ...
    def open(self) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, *args) -> None: ...

def parse_connection_str(conn_str, credential, service): ...
def create_configuration(**kwargs: Any) -> Configuration: ...
def parse_query(query_str): ...
def is_credential_sastoken(credential): ...
