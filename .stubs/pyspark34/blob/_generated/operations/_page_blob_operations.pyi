import datetime
from .. import models as _models
from .._serialization import Serializer as Serializer
from _typeshed import Incomplete
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from typing import Any, Callable, Dict, IO, TypeVar

T = TypeVar('T')
ClsType = Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any] | None

def build_create_request(url: str, *, content_length: int, blob_content_length: int, timeout: int | None = None, tier: str | _models.PremiumPageBlobAccessTier | None = None, blob_content_type: str | None = None, blob_content_encoding: str | None = None, blob_content_language: str | None = None, blob_content_md5: bytes | None = None, blob_cache_control: str | None = None, metadata: Dict[str, str] | None = None, lease_id: str | None = None, blob_content_disposition: str | None = None, encryption_key: str | None = None, encryption_key_sha256: str | None = None, encryption_algorithm: str | _models.EncryptionAlgorithmType | None = None, encryption_scope: str | None = None, if_modified_since: datetime.datetime | None = None, if_unmodified_since: datetime.datetime | None = None, if_match: str | None = None, if_none_match: str | None = None, if_tags: str | None = None, blob_sequence_number: int = 0, request_id_parameter: str | None = None, blob_tags_string: str | None = None, immutability_policy_expiry: datetime.datetime | None = None, immutability_policy_mode: str | _models.BlobImmutabilityPolicyMode | None = None, legal_hold: bool | None = None, **kwargs: Any) -> HttpRequest: ...
def build_upload_pages_request(url: str, *, content_length: int, content: IO, transactional_content_md5: bytes | None = None, transactional_content_crc64: bytes | None = None, timeout: int | None = None, range: str | None = None, lease_id: str | None = None, encryption_key: str | None = None, encryption_key_sha256: str | None = None, encryption_algorithm: str | _models.EncryptionAlgorithmType | None = None, encryption_scope: str | None = None, if_sequence_number_less_than_or_equal_to: int | None = None, if_sequence_number_less_than: int | None = None, if_sequence_number_equal_to: int | None = None, if_modified_since: datetime.datetime | None = None, if_unmodified_since: datetime.datetime | None = None, if_match: str | None = None, if_none_match: str | None = None, if_tags: str | None = None, request_id_parameter: str | None = None, **kwargs: Any) -> HttpRequest: ...
def build_clear_pages_request(url: str, *, content_length: int, timeout: int | None = None, range: str | None = None, lease_id: str | None = None, encryption_key: str | None = None, encryption_key_sha256: str | None = None, encryption_algorithm: str | _models.EncryptionAlgorithmType | None = None, encryption_scope: str | None = None, if_sequence_number_less_than_or_equal_to: int | None = None, if_sequence_number_less_than: int | None = None, if_sequence_number_equal_to: int | None = None, if_modified_since: datetime.datetime | None = None, if_unmodified_since: datetime.datetime | None = None, if_match: str | None = None, if_none_match: str | None = None, if_tags: str | None = None, request_id_parameter: str | None = None, **kwargs: Any) -> HttpRequest: ...
def build_upload_pages_from_url_request(url: str, *, source_url: str, source_range: str, content_length: int, range: str, source_content_md5: bytes | None = None, source_contentcrc64: bytes | None = None, timeout: int | None = None, encryption_key: str | None = None, encryption_key_sha256: str | None = None, encryption_algorithm: str | _models.EncryptionAlgorithmType | None = None, encryption_scope: str | None = None, lease_id: str | None = None, if_sequence_number_less_than_or_equal_to: int | None = None, if_sequence_number_less_than: int | None = None, if_sequence_number_equal_to: int | None = None, if_modified_since: datetime.datetime | None = None, if_unmodified_since: datetime.datetime | None = None, if_match: str | None = None, if_none_match: str | None = None, if_tags: str | None = None, source_if_modified_since: datetime.datetime | None = None, source_if_unmodified_since: datetime.datetime | None = None, source_if_match: str | None = None, source_if_none_match: str | None = None, request_id_parameter: str | None = None, copy_source_authorization: str | None = None, **kwargs: Any) -> HttpRequest: ...
def build_get_page_ranges_request(url: str, *, snapshot: str | None = None, timeout: int | None = None, range: str | None = None, lease_id: str | None = None, if_modified_since: datetime.datetime | None = None, if_unmodified_since: datetime.datetime | None = None, if_match: str | None = None, if_none_match: str | None = None, if_tags: str | None = None, request_id_parameter: str | None = None, marker: str | None = None, maxresults: int | None = None, **kwargs: Any) -> HttpRequest: ...
def build_get_page_ranges_diff_request(url: str, *, snapshot: str | None = None, timeout: int | None = None, prevsnapshot: str | None = None, prev_snapshot_url: str | None = None, range: str | None = None, lease_id: str | None = None, if_modified_since: datetime.datetime | None = None, if_unmodified_since: datetime.datetime | None = None, if_match: str | None = None, if_none_match: str | None = None, if_tags: str | None = None, request_id_parameter: str | None = None, marker: str | None = None, maxresults: int | None = None, **kwargs: Any) -> HttpRequest: ...
def build_resize_request(url: str, *, blob_content_length: int, timeout: int | None = None, lease_id: str | None = None, encryption_key: str | None = None, encryption_key_sha256: str | None = None, encryption_algorithm: str | _models.EncryptionAlgorithmType | None = None, encryption_scope: str | None = None, if_modified_since: datetime.datetime | None = None, if_unmodified_since: datetime.datetime | None = None, if_match: str | None = None, if_none_match: str | None = None, if_tags: str | None = None, request_id_parameter: str | None = None, **kwargs: Any) -> HttpRequest: ...
def build_update_sequence_number_request(url: str, *, sequence_number_action: str | _models.SequenceNumberActionType, timeout: int | None = None, lease_id: str | None = None, if_modified_since: datetime.datetime | None = None, if_unmodified_since: datetime.datetime | None = None, if_match: str | None = None, if_none_match: str | None = None, if_tags: str | None = None, blob_sequence_number: int = 0, request_id_parameter: str | None = None, **kwargs: Any) -> HttpRequest: ...
def build_copy_incremental_request(url: str, *, copy_source: str, timeout: int | None = None, if_modified_since: datetime.datetime | None = None, if_unmodified_since: datetime.datetime | None = None, if_match: str | None = None, if_none_match: str | None = None, if_tags: str | None = None, request_id_parameter: str | None = None, **kwargs: Any) -> HttpRequest: ...

class PageBlobOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.storage.blob.AzureBlobStorage`'s
        :attr:`page_blob` attribute.
    """
    models: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def create(self, content_length: int, blob_content_length: int, timeout: int | None = None, tier: str | _models.PremiumPageBlobAccessTier | None = None, metadata: Dict[str, str] | None = None, blob_sequence_number: int = 0, request_id_parameter: str | None = None, blob_tags_string: str | None = None, immutability_policy_expiry: datetime.datetime | None = None, immutability_policy_mode: str | _models.BlobImmutabilityPolicyMode | None = None, legal_hold: bool | None = None, blob_http_headers: _models.BlobHTTPHeaders | None = None, lease_access_conditions: _models.LeaseAccessConditions | None = None, cpk_info: _models.CpkInfo | None = None, cpk_scope_info: _models.CpkScopeInfo | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, **kwargs: Any) -> None:
        '''The Create operation creates a new page blob.

        :param content_length: The length of the request. Required.
        :type content_length: int
        :param blob_content_length: This header specifies the maximum size for the page blob, up to 1
         TB. The page blob size must be aligned to a 512-byte boundary. Required.
        :type blob_content_length: int
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param tier: Optional. Indicates the tier to be set on the page blob. Known values are: "P4",
         "P6", "P10", "P15", "P20", "P30", "P40", "P50", "P60", "P70", and "P80". Default value is None.
        :type tier: str or ~azure.storage.blob.models.PremiumPageBlobAccessTier
        :param metadata: Optional. Specifies a user-defined name-value pair associated with the blob.
         If no name-value pairs are specified, the operation will copy the metadata from the source blob
         or file to the destination blob. If one or more name-value pairs are specified, the destination
         blob is created with the specified metadata, and metadata is not copied from the source blob or
         file. Note that beginning with version 2009-09-19, metadata names must adhere to the naming
         rules for C# identifiers. See Naming and Referencing Containers, Blobs, and Metadata for more
         information. Default value is None.
        :type metadata: dict[str, str]
        :param blob_sequence_number: Set for page blobs only. The sequence number is a user-controlled
         value that you can use to track requests. The value of the sequence number must be between 0
         and 2^63 - 1. Default value is 0.
        :type blob_sequence_number: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param blob_tags_string: Optional.  Used to set blob tags in various blob operations. Default
         value is None.
        :type blob_tags_string: str
        :param immutability_policy_expiry: Specifies the date time when the blobs immutability policy
         is set to expire. Default value is None.
        :type immutability_policy_expiry: ~datetime.datetime
        :param immutability_policy_mode: Specifies the immutability policy mode to set on the blob.
         Known values are: "Mutable", "Unlocked", and "Locked". Default value is None.
        :type immutability_policy_mode: str or ~azure.storage.blob.models.BlobImmutabilityPolicyMode
        :param legal_hold: Specified if a legal hold should be set on the blob. Default value is None.
        :type legal_hold: bool
        :param blob_http_headers: Parameter group. Default value is None.
        :type blob_http_headers: ~azure.storage.blob.models.BlobHTTPHeaders
        :param lease_access_conditions: Parameter group. Default value is None.
        :type lease_access_conditions: ~azure.storage.blob.models.LeaseAccessConditions
        :param cpk_info: Parameter group. Default value is None.
        :type cpk_info: ~azure.storage.blob.models.CpkInfo
        :param cpk_scope_info: Parameter group. Default value is None.
        :type cpk_scope_info: ~azure.storage.blob.models.CpkScopeInfo
        :param modified_access_conditions: Parameter group. Default value is None.
        :type modified_access_conditions: ~azure.storage.blob.models.ModifiedAccessConditions
        :keyword blob_type: Specifies the type of blob to create: block blob, page blob, or append
         blob. Default value is "PageBlob". Note that overriding this default value may result in
         unsupported behavior.
        :paramtype blob_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    def upload_pages(self, content_length: int, body: IO, transactional_content_md5: bytes | None = None, transactional_content_crc64: bytes | None = None, timeout: int | None = None, range: str | None = None, request_id_parameter: str | None = None, lease_access_conditions: _models.LeaseAccessConditions | None = None, cpk_info: _models.CpkInfo | None = None, cpk_scope_info: _models.CpkScopeInfo | None = None, sequence_number_access_conditions: _models.SequenceNumberAccessConditions | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, **kwargs: Any) -> None:
        '''The Upload Pages operation writes a range of pages to a page blob.

        :param content_length: The length of the request. Required.
        :type content_length: int
        :param body: Initial data. Required.
        :type body: IO
        :param transactional_content_md5: Specify the transactional md5 for the body, to be validated
         by the service. Default value is None.
        :type transactional_content_md5: bytes
        :param transactional_content_crc64: Specify the transactional crc64 for the body, to be
         validated by the service. Default value is None.
        :type transactional_content_crc64: bytes
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param range: Return only the bytes of the blob in the specified range. Default value is None.
        :type range: str
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param lease_access_conditions: Parameter group. Default value is None.
        :type lease_access_conditions: ~azure.storage.blob.models.LeaseAccessConditions
        :param cpk_info: Parameter group. Default value is None.
        :type cpk_info: ~azure.storage.blob.models.CpkInfo
        :param cpk_scope_info: Parameter group. Default value is None.
        :type cpk_scope_info: ~azure.storage.blob.models.CpkScopeInfo
        :param sequence_number_access_conditions: Parameter group. Default value is None.
        :type sequence_number_access_conditions:
         ~azure.storage.blob.models.SequenceNumberAccessConditions
        :param modified_access_conditions: Parameter group. Default value is None.
        :type modified_access_conditions: ~azure.storage.blob.models.ModifiedAccessConditions
        :keyword comp: comp. Default value is "page". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword page_write: Required. You may specify one of the following options:


         * Update: Writes the bytes specified by the request body into the specified range. The Range
         and Content-Length headers must match to perform the update.
         * Clear: Clears the specified range and releases the space used in storage for that range. To
         clear a range, set the Content-Length header to zero, and the Range header to a value that
         indicates the range to clear, up to maximum blob size. Default value is "update". Note that
         overriding this default value may result in unsupported behavior.
        :paramtype page_write: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    def clear_pages(self, content_length: int, timeout: int | None = None, range: str | None = None, request_id_parameter: str | None = None, lease_access_conditions: _models.LeaseAccessConditions | None = None, cpk_info: _models.CpkInfo | None = None, cpk_scope_info: _models.CpkScopeInfo | None = None, sequence_number_access_conditions: _models.SequenceNumberAccessConditions | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, **kwargs: Any) -> None:
        '''The Clear Pages operation clears a set of pages from a page blob.

        :param content_length: The length of the request. Required.
        :type content_length: int
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param range: Return only the bytes of the blob in the specified range. Default value is None.
        :type range: str
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param lease_access_conditions: Parameter group. Default value is None.
        :type lease_access_conditions: ~azure.storage.blob.models.LeaseAccessConditions
        :param cpk_info: Parameter group. Default value is None.
        :type cpk_info: ~azure.storage.blob.models.CpkInfo
        :param cpk_scope_info: Parameter group. Default value is None.
        :type cpk_scope_info: ~azure.storage.blob.models.CpkScopeInfo
        :param sequence_number_access_conditions: Parameter group. Default value is None.
        :type sequence_number_access_conditions:
         ~azure.storage.blob.models.SequenceNumberAccessConditions
        :param modified_access_conditions: Parameter group. Default value is None.
        :type modified_access_conditions: ~azure.storage.blob.models.ModifiedAccessConditions
        :keyword comp: comp. Default value is "page". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword page_write: Required. You may specify one of the following options:


         * Update: Writes the bytes specified by the request body into the specified range. The Range
         and Content-Length headers must match to perform the update.
         * Clear: Clears the specified range and releases the space used in storage for that range. To
         clear a range, set the Content-Length header to zero, and the Range header to a value that
         indicates the range to clear, up to maximum blob size. Default value is "clear". Note that
         overriding this default value may result in unsupported behavior.
        :paramtype page_write: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    def upload_pages_from_url(self, source_url: str, source_range: str, content_length: int, range: str, source_content_md5: bytes | None = None, source_contentcrc64: bytes | None = None, timeout: int | None = None, request_id_parameter: str | None = None, copy_source_authorization: str | None = None, cpk_info: _models.CpkInfo | None = None, cpk_scope_info: _models.CpkScopeInfo | None = None, lease_access_conditions: _models.LeaseAccessConditions | None = None, sequence_number_access_conditions: _models.SequenceNumberAccessConditions | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, source_modified_access_conditions: _models.SourceModifiedAccessConditions | None = None, **kwargs: Any) -> None:
        '''The Upload Pages operation writes a range of pages to a page blob where the contents are read
        from a URL.

        :param source_url: Specify a URL to the copy source. Required.
        :type source_url: str
        :param source_range: Bytes of source data in the specified range. The length of this range
         should match the ContentLength header and x-ms-range/Range destination range header. Required.
        :type source_range: str
        :param content_length: The length of the request. Required.
        :type content_length: int
        :param range: The range of bytes to which the source range would be written. The range should
         be 512 aligned and range-end is required. Required.
        :type range: str
        :param source_content_md5: Specify the md5 calculated for the range of bytes that must be read
         from the copy source. Default value is None.
        :type source_content_md5: bytes
        :param source_contentcrc64: Specify the crc64 calculated for the range of bytes that must be
         read from the copy source. Default value is None.
        :type source_contentcrc64: bytes
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param copy_source_authorization: Only Bearer type is supported. Credentials should be a valid
         OAuth access token to copy source. Default value is None.
        :type copy_source_authorization: str
        :param cpk_info: Parameter group. Default value is None.
        :type cpk_info: ~azure.storage.blob.models.CpkInfo
        :param cpk_scope_info: Parameter group. Default value is None.
        :type cpk_scope_info: ~azure.storage.blob.models.CpkScopeInfo
        :param lease_access_conditions: Parameter group. Default value is None.
        :type lease_access_conditions: ~azure.storage.blob.models.LeaseAccessConditions
        :param sequence_number_access_conditions: Parameter group. Default value is None.
        :type sequence_number_access_conditions:
         ~azure.storage.blob.models.SequenceNumberAccessConditions
        :param modified_access_conditions: Parameter group. Default value is None.
        :type modified_access_conditions: ~azure.storage.blob.models.ModifiedAccessConditions
        :param source_modified_access_conditions: Parameter group. Default value is None.
        :type source_modified_access_conditions:
         ~azure.storage.blob.models.SourceModifiedAccessConditions
        :keyword comp: comp. Default value is "page". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword page_write: Required. You may specify one of the following options:


         * Update: Writes the bytes specified by the request body into the specified range. The Range
         and Content-Length headers must match to perform the update.
         * Clear: Clears the specified range and releases the space used in storage for that range. To
         clear a range, set the Content-Length header to zero, and the Range header to a value that
         indicates the range to clear, up to maximum blob size. Default value is "update". Note that
         overriding this default value may result in unsupported behavior.
        :paramtype page_write: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    def get_page_ranges(self, snapshot: str | None = None, timeout: int | None = None, range: str | None = None, request_id_parameter: str | None = None, marker: str | None = None, maxresults: int | None = None, lease_access_conditions: _models.LeaseAccessConditions | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, **kwargs: Any) -> _models.PageList:
        '''The Get Page Ranges operation returns the list of valid page ranges for a page blob or snapshot
        of a page blob.

        :param snapshot: The snapshot parameter is an opaque DateTime value that, when present,
         specifies the blob snapshot to retrieve. For more information on working with blob snapshots,
         see :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/creating-a-snapshot-of-a-blob">Creating
         a Snapshot of a Blob.</a>`. Default value is None.
        :type snapshot: str
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param range: Return only the bytes of the blob in the specified range. Default value is None.
        :type range: str
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
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
        :param lease_access_conditions: Parameter group. Default value is None.
        :type lease_access_conditions: ~azure.storage.blob.models.LeaseAccessConditions
        :param modified_access_conditions: Parameter group. Default value is None.
        :type modified_access_conditions: ~azure.storage.blob.models.ModifiedAccessConditions
        :keyword comp: comp. Default value is "pagelist". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PageList or the result of cls(response)
        :rtype: ~azure.storage.blob.models.PageList
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    def get_page_ranges_diff(self, snapshot: str | None = None, timeout: int | None = None, prevsnapshot: str | None = None, prev_snapshot_url: str | None = None, range: str | None = None, request_id_parameter: str | None = None, marker: str | None = None, maxresults: int | None = None, lease_access_conditions: _models.LeaseAccessConditions | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, **kwargs: Any) -> _models.PageList:
        '''The Get Page Ranges Diff operation returns the list of valid page ranges for a page blob that
        were changed between target blob and previous snapshot.

        :param snapshot: The snapshot parameter is an opaque DateTime value that, when present,
         specifies the blob snapshot to retrieve. For more information on working with blob snapshots,
         see :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/creating-a-snapshot-of-a-blob">Creating
         a Snapshot of a Blob.</a>`. Default value is None.
        :type snapshot: str
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param prevsnapshot: Optional in version 2015-07-08 and newer. The prevsnapshot parameter is a
         DateTime value that specifies that the response will contain only pages that were changed
         between target blob and previous snapshot. Changed pages include both updated and cleared
         pages. The target blob may be a snapshot, as long as the snapshot specified by prevsnapshot is
         the older of the two. Note that incremental snapshots are currently supported only for blobs
         created on or after January 1, 2016. Default value is None.
        :type prevsnapshot: str
        :param prev_snapshot_url: Optional. This header is only supported in service versions
         2019-04-19 and after and specifies the URL of a previous snapshot of the target blob. The
         response will only contain pages that were changed between the target blob and its previous
         snapshot. Default value is None.
        :type prev_snapshot_url: str
        :param range: Return only the bytes of the blob in the specified range. Default value is None.
        :type range: str
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
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
        :param lease_access_conditions: Parameter group. Default value is None.
        :type lease_access_conditions: ~azure.storage.blob.models.LeaseAccessConditions
        :param modified_access_conditions: Parameter group. Default value is None.
        :type modified_access_conditions: ~azure.storage.blob.models.ModifiedAccessConditions
        :keyword comp: comp. Default value is "pagelist". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PageList or the result of cls(response)
        :rtype: ~azure.storage.blob.models.PageList
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    def resize(self, blob_content_length: int, timeout: int | None = None, request_id_parameter: str | None = None, lease_access_conditions: _models.LeaseAccessConditions | None = None, cpk_info: _models.CpkInfo | None = None, cpk_scope_info: _models.CpkScopeInfo | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, **kwargs: Any) -> None:
        '''Resize the Blob.

        :param blob_content_length: This header specifies the maximum size for the page blob, up to 1
         TB. The page blob size must be aligned to a 512-byte boundary. Required.
        :type blob_content_length: int
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param lease_access_conditions: Parameter group. Default value is None.
        :type lease_access_conditions: ~azure.storage.blob.models.LeaseAccessConditions
        :param cpk_info: Parameter group. Default value is None.
        :type cpk_info: ~azure.storage.blob.models.CpkInfo
        :param cpk_scope_info: Parameter group. Default value is None.
        :type cpk_scope_info: ~azure.storage.blob.models.CpkScopeInfo
        :param modified_access_conditions: Parameter group. Default value is None.
        :type modified_access_conditions: ~azure.storage.blob.models.ModifiedAccessConditions
        :keyword comp: comp. Default value is "properties". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    def update_sequence_number(self, sequence_number_action: str | _models.SequenceNumberActionType, timeout: int | None = None, blob_sequence_number: int = 0, request_id_parameter: str | None = None, lease_access_conditions: _models.LeaseAccessConditions | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, **kwargs: Any) -> None:
        '''Update the sequence number of the blob.

        :param sequence_number_action: Required if the x-ms-blob-sequence-number header is set for the
         request. This property applies to page blobs only. This property indicates how the service
         should modify the blob\'s sequence number. Known values are: "max", "update", and "increment".
         Required.
        :type sequence_number_action: str or ~azure.storage.blob.models.SequenceNumberActionType
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param blob_sequence_number: Set for page blobs only. The sequence number is a user-controlled
         value that you can use to track requests. The value of the sequence number must be between 0
         and 2^63 - 1. Default value is 0.
        :type blob_sequence_number: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param lease_access_conditions: Parameter group. Default value is None.
        :type lease_access_conditions: ~azure.storage.blob.models.LeaseAccessConditions
        :param modified_access_conditions: Parameter group. Default value is None.
        :type modified_access_conditions: ~azure.storage.blob.models.ModifiedAccessConditions
        :keyword comp: comp. Default value is "properties". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    def copy_incremental(self, copy_source: str, timeout: int | None = None, request_id_parameter: str | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, **kwargs: Any) -> None:
        '''The Copy Incremental operation copies a snapshot of the source page blob to a destination page
        blob. The snapshot is copied such that only the differential changes between the previously
        copied snapshot are transferred to the destination. The copied snapshots are complete copies of
        the original snapshot and can be read or copied from as usual. This API is supported since REST
        version 2016-05-31.

        :param copy_source: Specifies the name of the source page blob snapshot. This value is a URL of
         up to 2 KB in length that specifies a page blob snapshot. The value should be URL-encoded as it
         would appear in a request URI. The source blob must either be public or must be authenticated
         via a shared access signature. Required.
        :type copy_source: str
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param modified_access_conditions: Parameter group. Default value is None.
        :type modified_access_conditions: ~azure.storage.blob.models.ModifiedAccessConditions
        :keyword comp: comp. Default value is "incrementalcopy". Note that overriding this default
         value may result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
