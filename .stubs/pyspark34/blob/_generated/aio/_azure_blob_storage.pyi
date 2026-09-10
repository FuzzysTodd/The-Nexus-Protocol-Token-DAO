from .._serialization import Deserializer as Deserializer, Serializer as Serializer
from ._configuration import AzureBlobStorageConfiguration as AzureBlobStorageConfiguration
from .operations import AppendBlobOperations as AppendBlobOperations, BlobOperations as BlobOperations, BlockBlobOperations as BlockBlobOperations, ContainerOperations as ContainerOperations, PageBlobOperations as PageBlobOperations, ServiceOperations as ServiceOperations
from _typeshed import Incomplete
from azure.core.rest import AsyncHttpResponse as AsyncHttpResponse, HttpRequest as HttpRequest
from typing import Any

class AzureBlobStorage:
    '''AzureBlobStorage.

    :ivar service: ServiceOperations operations
    :vartype service: azure.storage.blob.aio.operations.ServiceOperations
    :ivar container: ContainerOperations operations
    :vartype container: azure.storage.blob.aio.operations.ContainerOperations
    :ivar blob: BlobOperations operations
    :vartype blob: azure.storage.blob.aio.operations.BlobOperations
    :ivar page_blob: PageBlobOperations operations
    :vartype page_blob: azure.storage.blob.aio.operations.PageBlobOperations
    :ivar append_blob: AppendBlobOperations operations
    :vartype append_blob: azure.storage.blob.aio.operations.AppendBlobOperations
    :ivar block_blob: BlockBlobOperations operations
    :vartype block_blob: azure.storage.blob.aio.operations.BlockBlobOperations
    :param url: The URL of the service account, container, or blob that is the target of the
     desired operation. Required.
    :type url: str
    :param base_url: Service URL. Required. Default value is "".
    :type base_url: str
    :keyword version: Specifies the version of the operation to use for this request. Default value
     is "2021-12-02". Note that overriding this default value may result in unsupported behavior.
    :paramtype version: str
    '''
    service: Incomplete
    container: Incomplete
    blob: Incomplete
    page_blob: Incomplete
    append_blob: Incomplete
    block_blob: Incomplete
    def __init__(self, url: str, base_url: str = '', **kwargs: Any) -> None: ...
    async def close(self) -> None: ...
    async def __aenter__(self) -> AzureBlobStorage: ...
    async def __aexit__(self, *exc_details: Any) -> None: ...
