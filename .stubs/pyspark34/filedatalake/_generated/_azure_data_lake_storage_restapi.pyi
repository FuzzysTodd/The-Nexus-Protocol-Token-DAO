from ._configuration import AzureDataLakeStorageRESTAPIConfiguration as AzureDataLakeStorageRESTAPIConfiguration
from ._serialization import Deserializer as Deserializer, Serializer as Serializer
from .operations import FileSystemOperations as FileSystemOperations, PathOperations as PathOperations, ServiceOperations as ServiceOperations
from _typeshed import Incomplete
from azure.core.rest import HttpRequest as HttpRequest, HttpResponse as HttpResponse
from typing import Any

class AzureDataLakeStorageRESTAPI:
    '''Azure Data Lake Storage provides storage for Hadoop and other big data workloads.

    :ivar service: ServiceOperations operations
    :vartype service: azure.storage.filedatalake.operations.ServiceOperations
    :ivar file_system: FileSystemOperations operations
    :vartype file_system: azure.storage.filedatalake.operations.FileSystemOperations
    :ivar path: PathOperations operations
    :vartype path: azure.storage.filedatalake.operations.PathOperations
    :param url: The URL of the service account, container, or blob that is the target of the
     desired operation. Required.
    :type url: str
    :param base_url: Service URL. Required. Default value is "".
    :type base_url: str
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
    service: Incomplete
    file_system: Incomplete
    path: Incomplete
    def __init__(self, url: str, base_url: str = '', x_ms_lease_duration: int | None = None, **kwargs: Any) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> AzureDataLakeStorageRESTAPI: ...
    def __exit__(self, *exc_details: Any) -> None: ...
