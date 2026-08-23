from ... import models as _models
from ...operations._file_system_operations import build_create_request as build_create_request, build_delete_request as build_delete_request, build_get_properties_request as build_get_properties_request, build_list_blob_hierarchy_segment_request as build_list_blob_hierarchy_segment_request, build_list_paths_request as build_list_paths_request, build_set_properties_request as build_set_properties_request
from _typeshed import Incomplete
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from typing import Any, Callable, Dict, List, Literal, TypeVar

T = TypeVar('T')
ClsType = Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any] | None

class FileSystemOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.storage.filedatalake.aio.AzureDataLakeStorageRESTAPI`'s
        :attr:`file_system` attribute.
    """
    models: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    async def create(self, request_id_parameter: str | None = None, timeout: int | None = None, properties: str | None = None, **kwargs: Any) -> None:
        '''Create FileSystem.

        Create a FileSystem rooted at the specified location. If the FileSystem already exists, the
        operation fails.  This operation does not support conditional HTTP requests.

        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param properties: Optional. User-defined properties to be stored with the filesystem, in the
         format of a comma-separated list of name and value pairs "n1=v1, n2=v2, ...", where each value
         is a base64 encoded string. Note that the string may only contain ASCII characters in the
         ISO-8859-1 character set.  If the filesystem exists, any properties not included in the list
         will be removed.  All properties are removed if the header is omitted.  To merge new and
         existing properties, first get all existing properties and the current E-Tag, then make a
         conditional request with the E-Tag and include values for all properties. Default value is
         None.
        :type properties: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    async def set_properties(self, request_id_parameter: str | None = None, timeout: int | None = None, properties: str | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, **kwargs: Any) -> None:
        '''Set FileSystem Properties.

        Set properties for the FileSystem.  This operation supports conditional HTTP requests.  For
        more information, see `Specifying Conditional Headers for Blob Service Operations
        <https://docs.microsoft.com/en-us/rest/api/storageservices/specifying-conditional-headers-for-blob-service-operations>`_.

        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param properties: Optional. User-defined properties to be stored with the filesystem, in the
         format of a comma-separated list of name and value pairs "n1=v1, n2=v2, ...", where each value
         is a base64 encoded string. Note that the string may only contain ASCII characters in the
         ISO-8859-1 character set.  If the filesystem exists, any properties not included in the list
         will be removed.  All properties are removed if the header is omitted.  To merge new and
         existing properties, first get all existing properties and the current E-Tag, then make a
         conditional request with the E-Tag and include values for all properties. Default value is
         None.
        :type properties: str
        :param modified_access_conditions: Parameter group. Default value is None.
        :type modified_access_conditions: ~azure.storage.filedatalake.models.ModifiedAccessConditions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    async def get_properties(self, request_id_parameter: str | None = None, timeout: int | None = None, **kwargs: Any) -> None:
        '''Get FileSystem Properties.

        All system and user-defined filesystem properties are specified in the response headers.

        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    async def delete(self, request_id_parameter: str | None = None, timeout: int | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, **kwargs: Any) -> None:
        '''Delete FileSystem.

        Marks the FileSystem for deletion.  When a FileSystem is deleted, a FileSystem with the same
        identifier cannot be created for at least 30 seconds. While the filesystem is being deleted,
        attempts to create a filesystem with the same identifier will fail with status code 409
        (Conflict), with the service returning additional error information indicating that the
        filesystem is being deleted. All other operations, including operations on any files or
        directories within the filesystem, will fail with status code 404 (Not Found) while the
        filesystem is being deleted. This operation supports conditional HTTP requests.  For more
        information, see `Specifying Conditional Headers for Blob Service Operations
        <https://docs.microsoft.com/en-us/rest/api/storageservices/specifying-conditional-headers-for-blob-service-operations>`_.

        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param modified_access_conditions: Parameter group. Default value is None.
        :type modified_access_conditions: ~azure.storage.filedatalake.models.ModifiedAccessConditions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    async def list_paths(self, recursive: bool, request_id_parameter: str | None = None, timeout: int | None = None, continuation: str | None = None, path: str | None = None, max_results: int | None = None, upn: bool | None = None, **kwargs: Any) -> _models.PathList:
        '''List Paths.

        List FileSystem paths and their properties.

        :param recursive: Required. Required.
        :type recursive: bool
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param continuation: Optional.  When deleting a directory, the number of paths that are deleted
         with each invocation is limited.  If the number of paths to be deleted exceeds this limit, a
         continuation token is returned in this response header.  When a continuation token is returned
         in the response, it must be specified in a subsequent invocation of the delete operation to
         continue deleting the directory. Default value is None.
        :type continuation: str
        :param path: Optional.  Filters results to paths within the specified directory. An error
         occurs if the directory does not exist. Default value is None.
        :type path: str
        :param max_results: An optional value that specifies the maximum number of items to return. If
         omitted or greater than 5,000, the response will include up to 5,000 items. Default value is
         None.
        :type max_results: int
        :param upn: Optional. Valid only when Hierarchical Namespace is enabled for the account. If
         "true", the user identity values returned in the x-ms-owner, x-ms-group, and x-ms-acl response
         headers will be transformed from Azure Active Directory Object IDs to User Principal Names.  If
         "false", the values will be returned as Azure Active Directory Object IDs. The default value is
         false. Note that group and application Object IDs are not translated because they do not have
         unique friendly names. Default value is None.
        :type upn: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PathList or the result of cls(response)
        :rtype: ~azure.storage.filedatalake.models.PathList
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    async def list_blob_hierarchy_segment(self, prefix: str | None = None, delimiter: str | None = None, marker: str | None = None, max_results: int | None = None, include: List[str | _models.ListBlobsIncludeItem] | None = None, showonly: Literal['deleted'] = 'deleted', timeout: int | None = None, request_id_parameter: str | None = None, **kwargs: Any) -> _models.ListBlobsHierarchySegmentResponse:
        '''The List Blobs operation returns a list of the blobs under the specified container.

        :param prefix: Filters results to filesystems within the specified prefix. Default value is
         None.
        :type prefix: str
        :param delimiter: When the request includes this parameter, the operation returns a BlobPrefix
         element in the response body that acts as a placeholder for all blobs whose names begin with
         the same substring up to the appearance of the delimiter character. The delimiter may be a
         single character or a string. Default value is None.
        :type delimiter: str
        :param marker: A string value that identifies the portion of the list of containers to be
         returned with the next listing operation. The operation returns the NextMarker value within the
         response body if the listing operation did not return all containers remaining to be listed
         with the current page. The NextMarker value can be used as the value for the marker parameter
         in a subsequent call to request the next page of list items. The marker value is opaque to the
         client. Default value is None.
        :type marker: str
        :param max_results: An optional value that specifies the maximum number of items to return. If
         omitted or greater than 5,000, the response will include up to 5,000 items. Default value is
         None.
        :type max_results: int
        :param include: Include this parameter to specify one or more datasets to include in the
         response. Default value is None.
        :type include: list[str or ~azure.storage.filedatalake.models.ListBlobsIncludeItem]
        :param showonly: Include this parameter to specify one or more datasets to include in the
         response. Known values are "deleted" and None. Default value is "deleted".
        :type showonly: str
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :keyword restype: restype. Default value is "container". Note that overriding this default
         value may result in unsupported behavior.
        :paramtype restype: str
        :keyword comp: comp. Default value is "list". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ListBlobsHierarchySegmentResponse or the result of cls(response)
        :rtype: ~azure.storage.filedatalake.models.ListBlobsHierarchySegmentResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
