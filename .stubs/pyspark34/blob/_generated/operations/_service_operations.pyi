from .. import models as _models
from .._serialization import Serializer as Serializer
from _typeshed import Incomplete
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from typing import Any, Callable, Dict, IO, Iterator, List, TypeVar

T = TypeVar('T')
ClsType = Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any] | None

def build_set_properties_request(url: str, *, content: Any, timeout: int | None = None, request_id_parameter: str | None = None, **kwargs: Any) -> HttpRequest: ...
def build_get_properties_request(url: str, *, timeout: int | None = None, request_id_parameter: str | None = None, **kwargs: Any) -> HttpRequest: ...
def build_get_statistics_request(url: str, *, timeout: int | None = None, request_id_parameter: str | None = None, **kwargs: Any) -> HttpRequest: ...
def build_list_containers_segment_request(url: str, *, prefix: str | None = None, marker: str | None = None, maxresults: int | None = None, include: List[str | _models.ListContainersIncludeType] | None = None, timeout: int | None = None, request_id_parameter: str | None = None, **kwargs: Any) -> HttpRequest: ...
def build_get_user_delegation_key_request(url: str, *, content: Any, timeout: int | None = None, request_id_parameter: str | None = None, **kwargs: Any) -> HttpRequest: ...
def build_get_account_info_request(url: str, **kwargs: Any) -> HttpRequest: ...
def build_submit_batch_request(url: str, *, content_length: int, content: IO, timeout: int | None = None, request_id_parameter: str | None = None, **kwargs: Any) -> HttpRequest: ...
def build_filter_blobs_request(url: str, *, timeout: int | None = None, request_id_parameter: str | None = None, where: str | None = None, marker: str | None = None, maxresults: int | None = None, include: List[str | _models.FilterBlobsIncludeItem] | None = None, **kwargs: Any) -> HttpRequest: ...

class ServiceOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.storage.blob.AzureBlobStorage`'s
        :attr:`service` attribute.
    """
    models: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def set_properties(self, storage_service_properties: _models.StorageServiceProperties, timeout: int | None = None, request_id_parameter: str | None = None, **kwargs: Any) -> None:
        '''Sets properties for a storage account\'s Blob service endpoint, including properties for Storage
        Analytics and CORS (Cross-Origin Resource Sharing) rules.

        :param storage_service_properties: The StorageService properties. Required.
        :type storage_service_properties: ~azure.storage.blob.models.StorageServiceProperties
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :keyword restype: restype. Default value is "service". Note that overriding this default value
         may result in unsupported behavior.
        :paramtype restype: str
        :keyword comp: comp. Default value is "properties". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    def get_properties(self, timeout: int | None = None, request_id_parameter: str | None = None, **kwargs: Any) -> _models.StorageServiceProperties:
        '''gets the properties of a storage account\'s Blob service, including properties for Storage
        Analytics and CORS (Cross-Origin Resource Sharing) rules.

        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :keyword restype: restype. Default value is "service". Note that overriding this default value
         may result in unsupported behavior.
        :paramtype restype: str
        :keyword comp: comp. Default value is "properties". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: StorageServiceProperties or the result of cls(response)
        :rtype: ~azure.storage.blob.models.StorageServiceProperties
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    def get_statistics(self, timeout: int | None = None, request_id_parameter: str | None = None, **kwargs: Any) -> _models.StorageServiceStats:
        '''Retrieves statistics related to replication for the Blob service. It is only available on the
        secondary location endpoint when read-access geo-redundant replication is enabled for the
        storage account.

        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :keyword restype: restype. Default value is "service". Note that overriding this default value
         may result in unsupported behavior.
        :paramtype restype: str
        :keyword comp: comp. Default value is "stats". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: StorageServiceStats or the result of cls(response)
        :rtype: ~azure.storage.blob.models.StorageServiceStats
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    def list_containers_segment(self, prefix: str | None = None, marker: str | None = None, maxresults: int | None = None, include: List[str | _models.ListContainersIncludeType] | None = None, timeout: int | None = None, request_id_parameter: str | None = None, **kwargs: Any) -> _models.ListContainersSegmentResponse:
        '''The List Containers Segment operation returns a list of the containers under the specified
        account.

        :param prefix: Filters the results to return only containers whose name begins with the
         specified prefix. Default value is None.
        :type prefix: str
        :param marker: A string value that identifies the portion of the list of containers to be
         returned with the next listing operation. The operation returns the NextMarker value within the
         response body if the listing operation did not return all containers remaining to be listed
         with the current page. The NextMarker value can be used as the value for the marker parameter
         in a subsequent call to request the next page of list items. The marker value is opaque to the
         client. Default value is None.
        :type marker: str
        :param maxresults: Specifies the maximum number of containers to return. If the request does
         not specify maxresults, or specifies a value greater than 5000, the server will return up to
         5000 items. Note that if the listing operation crosses a partition boundary, then the service
         will return a continuation token for retrieving the remainder of the results. For this reason,
         it is possible that the service will return fewer results than specified by maxresults, or than
         the default of 5000. Default value is None.
        :type maxresults: int
        :param include: Include this parameter to specify that the container\'s metadata be returned as
         part of the response body. Default value is None.
        :type include: list[str or ~azure.storage.blob.models.ListContainersIncludeType]
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :keyword comp: comp. Default value is "list". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ListContainersSegmentResponse or the result of cls(response)
        :rtype: ~azure.storage.blob.models.ListContainersSegmentResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    def get_user_delegation_key(self, key_info: _models.KeyInfo, timeout: int | None = None, request_id_parameter: str | None = None, **kwargs: Any) -> _models.UserDelegationKey:
        '''Retrieves a user delegation key for the Blob service. This is only a valid operation when using
        bearer token authentication.

        :param key_info: Key information. Required.
        :type key_info: ~azure.storage.blob.models.KeyInfo
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :keyword restype: restype. Default value is "service". Note that overriding this default value
         may result in unsupported behavior.
        :paramtype restype: str
        :keyword comp: comp. Default value is "userdelegationkey". Note that overriding this default
         value may result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: UserDelegationKey or the result of cls(response)
        :rtype: ~azure.storage.blob.models.UserDelegationKey
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    def get_account_info(self, **kwargs: Any) -> None:
        '''Returns the sku name and account kind.

        :keyword restype: restype. Default value is "account". Note that overriding this default value
         may result in unsupported behavior.
        :paramtype restype: str
        :keyword comp: comp. Default value is "properties". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    def submit_batch(self, content_length: int, body: IO, timeout: int | None = None, request_id_parameter: str | None = None, **kwargs: Any) -> Iterator[bytes]:
        '''The Batch operation allows multiple API calls to be embedded into a single HTTP request.

        :param content_length: The length of the request. Required.
        :type content_length: int
        :param body: Initial data. Required.
        :type body: IO
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :keyword comp: comp. Default value is "batch". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Iterator of the response bytes or the result of cls(response)
        :rtype: Iterator[bytes]
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    def filter_blobs(self, timeout: int | None = None, request_id_parameter: str | None = None, where: str | None = None, marker: str | None = None, maxresults: int | None = None, include: List[str | _models.FilterBlobsIncludeItem] | None = None, **kwargs: Any) -> _models.FilterBlobSegment:
        '''The Filter Blobs operation enables callers to list blobs across all containers whose tags match
        a given search expression.  Filter blobs searches across all containers within a storage
        account but can be scoped within the expression to a single container.

        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param where: Filters the results to return only to return only blobs whose tags match the
         specified expression. Default value is None.
        :type where: str
        :param marker: A string value that identifies the portion of the list of containers to be
         returned with the next listing operation. The operation returns the NextMarker value within the
         response body if the listing operation did not return all containers remaining to be listed
         with the current page. The NextMarker value can be used as the value for the marker parameter
         in a subsequent call to request the next page of list items. The marker value is opaque to the
         client. Default value is None.
        :type marker: str
        :param maxresults: Specifies the maximum number of containers to return. If the request does
         not specify maxresults, or specifies a value greater than 5000, the server will return up to
         5000 items. Note that if the listing operation crosses a partition boundary, then the service
         will return a continuation token for retrieving the remainder of the results. For this reason,
         it is possible that the service will return fewer results than specified by maxresults, or than
         the default of 5000. Default value is None.
        :type maxresults: int
        :param include: Include this parameter to specify one or more datasets to include in the
         response. Default value is None.
        :type include: list[str or ~azure.storage.blob.models.FilterBlobsIncludeItem]
        :keyword comp: comp. Default value is "blobs". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: FilterBlobSegment or the result of cls(response)
        :rtype: ~azure.storage.blob.models.FilterBlobSegment
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
