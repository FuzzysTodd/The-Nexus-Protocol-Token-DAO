from .._deserialize import get_deleted_path_properties_from_generated_code as get_deleted_path_properties_from_generated_code, process_storage_error as process_storage_error, return_headers_and_deserialized_path_list as return_headers_and_deserialized_path_list
from .._generated.models import BlobItemInternal as BlobItemInternal, Path as Path
from .._models import PathProperties as PathProperties
from .._shared.models import DictMixin as DictMixin
from .._shared.response_handlers import return_context_and_deserialized as return_context_and_deserialized
from _typeshed import Incomplete
from azure.core.async_paging import AsyncPageIterator

class DeletedPathPropertiesPaged(AsyncPageIterator):
    '''An Iterable of deleted path properties.

    :ivar str service_endpoint: The service URL.
    :ivar str prefix: A path name prefix being used to filter the list.
    :ivar str marker: The continuation token of the current page of results.
    :ivar int results_per_page: The maximum number of results retrieved per API call.
    :ivar str continuation_token: The continuation token to retrieve the next page of results.
    :ivar str location_mode: The location mode being used to list results. The available
        options include "primary" and "secondary".
    :ivar current_page: The current page of listed results.
    :vartype current_page: list(~azure.storage.filedatalake.DeletedPathProperties)
    :ivar str container: The container that the paths are listed from.
    :ivar str delimiter: A delimiting character used for hierarchy listing.

    :param callable command: Function to retrieve the next page of items.
    '''
    service_endpoint: Incomplete
    prefix: Incomplete
    marker: Incomplete
    results_per_page: Incomplete
    container: Incomplete
    delimiter: Incomplete
    current_page: Incomplete
    location_mode: Incomplete
    def __init__(self, command, container: Incomplete | None = None, prefix: Incomplete | None = None, results_per_page: Incomplete | None = None, continuation_token: Incomplete | None = None, delimiter: Incomplete | None = None, location_mode: Incomplete | None = None) -> None: ...

class DirectoryPrefix(DictMixin):
    '''Directory prefix.

    :ivar str name: Name of the deleted directory.
    :ivar int results_per_page: The maximum number of results retrieved per API call.
    :ivar str location_mode: The location mode being used to list results. The available
        options include "primary" and "secondary".
    :ivar str file_system: The file system that the deleted paths are listed from.
    :ivar str delimiter: A delimiting character used for hierarchy listing.
    '''
    name: Incomplete
    results_per_page: Incomplete
    file_system: Incomplete
    delimiter: Incomplete
    location_mode: Incomplete
    def __init__(self, **kwargs) -> None: ...

class PathPropertiesPaged(AsyncPageIterator):
    """An Iterable of Path properties.

    :ivar str path: Filters the results to return only paths under the specified path.
    :ivar int results_per_page: The maximum number of results retrieved per API call.
    :ivar str continuation_token: The continuation token to retrieve the next page of results.
    :ivar list(~azure.storage.filedatalake.PathProperties) current_page: The current page of listed results.

    :param callable command: Function to retrieve the next page of items.
    :param str path: Filters the results to return only paths under the specified path.
    :param int max_results: The maximum number of paths to retrieve per
        call.
    :param str continuation_token: An opaque continuation token.
    """
    recursive: Incomplete
    results_per_page: Incomplete
    path: Incomplete
    upn: Incomplete
    current_page: Incomplete
    path_list: Incomplete
    def __init__(self, command, recursive, path: Incomplete | None = None, max_results: Incomplete | None = None, continuation_token: Incomplete | None = None, upn: Incomplete | None = None) -> None: ...
