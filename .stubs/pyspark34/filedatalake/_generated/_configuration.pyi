from _typeshed import Incomplete
from azure.core.configuration import Configuration
from typing import Any

VERSION: str

class AzureDataLakeStorageRESTAPIConfiguration(Configuration):
    '''Configuration for AzureDataLakeStorageRESTAPI.

    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param url: The URL of the service account, container, or blob that is the target of the
     desired operation. Required.
    :type url: str
    :param x_ms_lease_duration: The lease duration is required to acquire a lease, and specifies
     the duration of the lease in seconds.  The lease duration must be between 15 and 60 seconds or
     -1 for infinite lease. Default value is None.
    :type x_ms_lease_duration: int
    :keyword resource: The value must be "filesystem" for all filesystem operations. Default value
     is "filesystem". Note that overriding this default value may result in unsupported behavior.
    :paramtype resource: str
    :keyword version: Specifies the version of the operation to use for this request. Default value
     is "2021-06-08". Note that overriding this default value may result in unsupported behavior.
    :paramtype version: str
    '''
    url: Incomplete
    x_ms_lease_duration: Incomplete
    resource: Incomplete
    version: Incomplete
    def __init__(self, url: str, x_ms_lease_duration: int | None = None, **kwargs: Any) -> None: ...
