from .. import models as _models
from .._serialization import Serializer as Serializer
from _typeshed import Incomplete
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from typing import Any, Callable, Dict, Iterable, TypeVar

T = TypeVar('T')
ClsType = Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any] | None

def build_list_file_systems_request(url: str, *, prefix: str | None = None, continuation: str | None = None, max_results: int | None = None, request_id_parameter: str | None = None, timeout: int | None = None, **kwargs: Any) -> HttpRequest: ...

class ServiceOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.storage.filedatalake.AzureDataLakeStorageRESTAPI`'s
        :attr:`service` attribute.
    """
    models: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def list_file_systems(self, prefix: str | None = None, continuation: str | None = None, max_results: int | None = None, request_id_parameter: str | None = None, timeout: int | None = None, **kwargs: Any) -> Iterable['_models.FileSystem']:
        '''List FileSystems.

        List filesystems and their properties in given account.

        :param prefix: Filters results to filesystems within the specified prefix. Default value is
         None.
        :type prefix: str
        :param continuation: Optional.  When deleting a directory, the number of paths that are deleted
         with each invocation is limited.  If the number of paths to be deleted exceeds this limit, a
         continuation token is returned in this response header.  When a continuation token is returned
         in the response, it must be specified in a subsequent invocation of the delete operation to
         continue deleting the directory. Default value is None.
        :type continuation: str
        :param max_results: An optional value that specifies the maximum number of items to return. If
         omitted or greater than 5,000, the response will include up to 5,000 items. Default value is
         None.
        :type max_results: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :keyword resource: The value must be "account" for all account operations. Default value is
         "account". Note that overriding this default value may result in unsupported behavior.
        :paramtype resource: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either FileSystem or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.storage.filedatalake.models.FileSystem]
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
