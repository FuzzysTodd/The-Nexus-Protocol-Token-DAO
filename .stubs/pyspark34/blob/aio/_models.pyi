from .._deserialize import parse_tags as parse_tags
from .._generated.models import FilterBlobItem as FilterBlobItem
from .._models import ContainerProperties as ContainerProperties, FilteredBlob as FilteredBlob, parse_page_list as parse_page_list
from .._shared.response_handlers import process_storage_error as process_storage_error, return_context_and_deserialized as return_context_and_deserialized
from _typeshed import Incomplete
from azure.core.async_paging import AsyncPageIterator

class ContainerPropertiesPaged(AsyncPageIterator):
    '''An Iterable of Container properties.

    :ivar str service_endpoint: The service URL.
    :ivar str prefix: A container name prefix being used to filter the list.
    :ivar str marker: The continuation token of the current page of results.
    :ivar int results_per_page: The maximum number of results retrieved per API call.
    :ivar str location_mode: The location mode being used to list results. The available
        options include "primary" and "secondary".
    :ivar current_page: The current page of listed results.
    :vartype current_page: list(~azure.storage.blob.models.ContainerProperties)

    :param callable command: Function to retrieve the next page of items.
    :param str prefix: Filters the results to return only containers whose names
        begin with the specified prefix.
    :param int results_per_page: The maximum number of container names to retrieve per
        call.
    :param str continuation_token: An opaque continuation token.
    '''
    service_endpoint: Incomplete
    prefix: Incomplete
    marker: Incomplete
    results_per_page: Incomplete
    location_mode: Incomplete
    current_page: Incomplete
    def __init__(self, command, prefix: Incomplete | None = None, results_per_page: Incomplete | None = None, continuation_token: Incomplete | None = None) -> None: ...

class FilteredBlobPaged(AsyncPageIterator):
    '''An Iterable of Blob properties.

    :ivar str service_endpoint: The service URL.
    :ivar str prefix: A blob name prefix being used to filter the list.
    :ivar str marker: The continuation token of the current page of results.
    :ivar int results_per_page: The maximum number of results retrieved per API call.
    :ivar str continuation_token: The continuation token to retrieve the next page of results.
    :ivar str location_mode: The location mode being used to list results. The available
        options include "primary" and "secondary".
    :ivar current_page: The current page of listed results.
    :vartype current_page: list(~azure.storage.blob.BlobProperties)
    :ivar str container: The container that the blobs are listed from.
    :param callable command: Function to retrieve the next page of items.
    :param str container: The name of the container.
    :param int results_per_page: The maximum number of blobs to retrieve per
        call.
    :param str continuation_token: An opaque continuation token.
    :param location_mode: Specifies the location the request should be sent to.
        This mode only applies for RA-GRS accounts which allow secondary read access.
        Options include \'primary\' or \'secondary\'.
    '''
    service_endpoint: Incomplete
    marker: Incomplete
    results_per_page: Incomplete
    container: Incomplete
    current_page: Incomplete
    location_mode: Incomplete
    def __init__(self, command, container: Incomplete | None = None, results_per_page: Incomplete | None = None, continuation_token: Incomplete | None = None, location_mode: Incomplete | None = None) -> None: ...

class PageRangePaged(AsyncPageIterator):
    results_per_page: Incomplete
    location_mode: Incomplete
    current_page: Incomplete
    def __init__(self, command, results_per_page: Incomplete | None = None, continuation_token: Incomplete | None = None) -> None: ...
