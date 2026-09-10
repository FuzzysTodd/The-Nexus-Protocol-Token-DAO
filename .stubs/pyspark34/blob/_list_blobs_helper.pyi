from ._deserialize import get_blob_properties_from_generated_code as get_blob_properties_from_generated_code, load_many_xml_nodes as load_many_xml_nodes, load_xml_int as load_xml_int, load_xml_string as load_xml_string, parse_tags as parse_tags
from ._generated._serialization import Deserializer as Deserializer
from ._generated.models import BlobItemInternal as BlobItemInternal, FilterBlobItem as FilterBlobItem
from ._models import BlobProperties as BlobProperties, FilteredBlob as FilteredBlob
from ._shared.models import DictMixin as DictMixin
from ._shared.response_handlers import process_storage_error as process_storage_error, return_context_and_deserialized as return_context_and_deserialized, return_raw_deserialized as return_raw_deserialized
from _typeshed import Incomplete
from azure.core.paging import ItemPaged, PageIterator

class IgnoreListBlobsDeserializer(Deserializer):
    def __call__(self, target_obj, response_data, content_type: Incomplete | None = None) -> None: ...

class BlobPropertiesPaged(PageIterator):
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
    :ivar str delimiter: A delimiting character used for hierarchy listing.

    :param callable command: Function to retrieve the next page of items.
    :param str container: The name of the container.
    :param str prefix: Filters the results to return only blobs whose names
        begin with the specified prefix.
    :param int results_per_page: The maximum number of blobs to retrieve per
        call.
    :param str continuation_token: An opaque continuation token.
    :param str delimiter:
        Used to capture blobs whose names begin with the same substring up to
        the appearance of the delimiter character. The delimiter may be a single
        character or a string.
    :param location_mode: Specifies the location the request should be sent to.
        This mode only applies for RA-GRS accounts which allow secondary read access.
        Options include \'primary\' or \'secondary\'.
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

class BlobNamesPaged(PageIterator):
    '''An Iterable of Blob names.

    :ivar str service_endpoint: The service URL.
    :ivar str prefix: A blob name prefix being used to filter the list.
    :ivar str marker: The continuation token of the current page of results.
    :ivar int results_per_page: The maximum number of results retrieved per API call.
    :ivar str continuation_token: The continuation token to retrieve the next page of results.
    :ivar str location_mode: The location mode being used to list results. The available
        options include "primary" and "secondary".
    :ivar current_page: The current page of listed results.
    :vartype current_page: list(str)
    :ivar str container: The container that the blobs are listed from.
    :ivar str delimiter: A delimiting character used for hierarchy listing.

    :param callable command: Function to retrieve the next page of items.
    :param str container: The name of the container.
    :param str prefix: Filters the results to return only blobs whose names
        begin with the specified prefix.
    :param int results_per_page: The maximum number of blobs to retrieve per
        call.
    :param str continuation_token: An opaque continuation token.
    :param location_mode: Specifies the location the request should be sent to.
        This mode only applies for RA-GRS accounts which allow secondary read access.
        Options include \'primary\' or \'secondary\'.
    '''
    service_endpoint: Incomplete
    prefix: Incomplete
    marker: Incomplete
    results_per_page: Incomplete
    container: Incomplete
    current_page: Incomplete
    location_mode: Incomplete
    def __init__(self, command, container: Incomplete | None = None, prefix: Incomplete | None = None, results_per_page: Incomplete | None = None, continuation_token: Incomplete | None = None, location_mode: Incomplete | None = None) -> None: ...

class BlobPrefixPaged(BlobPropertiesPaged):
    name: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class BlobPrefix(ItemPaged, DictMixin):
    '''An Iterable of Blob properties.

    Returned from walk_blobs when a delimiter is used.
    Can be thought of as a virtual blob directory.

    :ivar str name: The prefix, or "directory name" of the blob.
    :ivar str service_endpoint: The service URL.
    :ivar str prefix: A blob name prefix being used to filter the list.
    :ivar str marker: The continuation token of the current page of results.
    :ivar int results_per_page: The maximum number of results retrieved per API call.
    :ivar str next_marker: The continuation token to retrieve the next page of results.
    :ivar str location_mode: The location mode being used to list results. The available
        options include "primary" and "secondary".
    :ivar current_page: The current page of listed results.
    :vartype current_page: list(~azure.storage.blob.BlobProperties)
    :ivar str container: The container that the blobs are listed from.
    :ivar str delimiter: A delimiting character used for hierarchy listing.

    :param callable command: Function to retrieve the next page of items.
    :param str prefix: Filters the results to return only blobs whose names
        begin with the specified prefix.
    :param int results_per_page: The maximum number of blobs to retrieve per
        call.
    :param str marker: An opaque continuation token.
    :param str delimiter:
        Used to capture blobs whose names begin with the same substring up to
        the appearance of the delimiter character. The delimiter may be a single
        character or a string.
    :param location_mode: Specifies the location the request should be sent to.
        This mode only applies for RA-GRS accounts which allow secondary read access.
        Options include \'primary\' or \'secondary\'.
    '''
    name: Incomplete
    prefix: Incomplete
    results_per_page: Incomplete
    container: Incomplete
    delimiter: Incomplete
    location_mode: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class FilteredBlobPaged(PageIterator):
    '''An Iterable of Blob properties.

    :ivar str service_endpoint: The service URL.
    :ivar str prefix: A blob name prefix being used to filter the list.
    :ivar str marker: The continuation token of the current page of results.
    :ivar int results_per_page: The maximum number of results retrieved per API call.
    :ivar str continuation_token: The continuation token to retrieve the next page of results.
    :ivar str location_mode: The location mode being used to list results. The available
        options include "primary" and "secondary".
    :ivar current_page: The current page of listed results.
    :vartype current_page: list(~azure.storage.blob.FilteredBlob)
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
