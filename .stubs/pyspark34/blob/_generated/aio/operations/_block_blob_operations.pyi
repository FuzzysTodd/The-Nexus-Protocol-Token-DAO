import datetime
from ... import models as _models
from ...operations._block_blob_operations import build_commit_block_list_request as build_commit_block_list_request, build_get_block_list_request as build_get_block_list_request, build_put_blob_from_url_request as build_put_blob_from_url_request, build_stage_block_from_url_request as build_stage_block_from_url_request, build_stage_block_request as build_stage_block_request, build_upload_request as build_upload_request
from _typeshed import Incomplete
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from typing import Any, Callable, Dict, IO, TypeVar

T = TypeVar('T')
ClsType = Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any] | None

class BlockBlobOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.storage.blob.aio.AzureBlobStorage`'s
        :attr:`block_blob` attribute.
    """
    models: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    async def upload(self, content_length: int, body: IO, timeout: int | None = None, transactional_content_md5: bytes | None = None, metadata: Dict[str, str] | None = None, tier: str | _models.AccessTierOptional | None = None, request_id_parameter: str | None = None, blob_tags_string: str | None = None, immutability_policy_expiry: datetime.datetime | None = None, immutability_policy_mode: str | _models.BlobImmutabilityPolicyMode | None = None, legal_hold: bool | None = None, transactional_content_crc64: bytes | None = None, blob_http_headers: _models.BlobHTTPHeaders | None = None, lease_access_conditions: _models.LeaseAccessConditions | None = None, cpk_info: _models.CpkInfo | None = None, cpk_scope_info: _models.CpkScopeInfo | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, **kwargs: Any) -> None:
        '''The Upload Block Blob operation updates the content of an existing block blob. Updating an
        existing block blob overwrites any existing metadata on the blob. Partial updates are not
        supported with Put Blob; the content of the existing blob is overwritten with the content of
        the new blob. To perform a partial update of the content of a block blob, use the Put Block
        List operation.

        :param content_length: The length of the request. Required.
        :type content_length: int
        :param body: Initial data. Required.
        :type body: IO
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param transactional_content_md5: Specify the transactional md5 for the body, to be validated
         by the service. Default value is None.
        :type transactional_content_md5: bytes
        :param metadata: Optional. Specifies a user-defined name-value pair associated with the blob.
         If no name-value pairs are specified, the operation will copy the metadata from the source blob
         or file to the destination blob. If one or more name-value pairs are specified, the destination
         blob is created with the specified metadata, and metadata is not copied from the source blob or
         file. Note that beginning with version 2009-09-19, metadata names must adhere to the naming
         rules for C# identifiers. See Naming and Referencing Containers, Blobs, and Metadata for more
         information. Default value is None.
        :type metadata: dict[str, str]
        :param tier: Optional. Indicates the tier to be set on the blob. Known values are: "P4", "P6",
         "P10", "P15", "P20", "P30", "P40", "P50", "P60", "P70", "P80", "Hot", "Cool", "Archive", and
         "Cold". Default value is None.
        :type tier: str or ~azure.storage.blob.models.AccessTierOptional
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
        :param transactional_content_crc64: Specify the transactional crc64 for the body, to be
         validated by the service. Default value is None.
        :type transactional_content_crc64: bytes
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
         blob. Default value is "BlockBlob". Note that overriding this default value may result in
         unsupported behavior.
        :paramtype blob_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    async def put_blob_from_url(self, content_length: int, copy_source: str, timeout: int | None = None, transactional_content_md5: bytes | None = None, metadata: Dict[str, str] | None = None, tier: str | _models.AccessTierOptional | None = None, request_id_parameter: str | None = None, source_content_md5: bytes | None = None, blob_tags_string: str | None = None, copy_source_blob_properties: bool | None = None, copy_source_authorization: str | None = None, copy_source_tags: str | _models.BlobCopySourceTags | None = None, blob_http_headers: _models.BlobHTTPHeaders | None = None, lease_access_conditions: _models.LeaseAccessConditions | None = None, cpk_info: _models.CpkInfo | None = None, cpk_scope_info: _models.CpkScopeInfo | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, source_modified_access_conditions: _models.SourceModifiedAccessConditions | None = None, **kwargs: Any) -> None:
        '''The Put Blob from URL operation creates a new Block Blob where the contents of the blob are
        read from a given URL.  This API is supported beginning with the 2020-04-08 version. Partial
        updates are not supported with Put Blob from URL; the content of an existing blob is
        overwritten with the content of the new blob.  To perform partial updates to a block blob’s
        contents using a source URL, use the Put Block from URL API in conjunction with Put Block List.

        :param content_length: The length of the request. Required.
        :type content_length: int
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
        :param transactional_content_md5: Specify the transactional md5 for the body, to be validated
         by the service. Default value is None.
        :type transactional_content_md5: bytes
        :param metadata: Optional. Specifies a user-defined name-value pair associated with the blob.
         If no name-value pairs are specified, the operation will copy the metadata from the source blob
         or file to the destination blob. If one or more name-value pairs are specified, the destination
         blob is created with the specified metadata, and metadata is not copied from the source blob or
         file. Note that beginning with version 2009-09-19, metadata names must adhere to the naming
         rules for C# identifiers. See Naming and Referencing Containers, Blobs, and Metadata for more
         information. Default value is None.
        :type metadata: dict[str, str]
        :param tier: Optional. Indicates the tier to be set on the blob. Known values are: "P4", "P6",
         "P10", "P15", "P20", "P30", "P40", "P50", "P60", "P70", "P80", "Hot", "Cool", "Archive", and
         "Cold". Default value is None.
        :type tier: str or ~azure.storage.blob.models.AccessTierOptional
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param source_content_md5: Specify the md5 calculated for the range of bytes that must be read
         from the copy source. Default value is None.
        :type source_content_md5: bytes
        :param blob_tags_string: Optional.  Used to set blob tags in various blob operations. Default
         value is None.
        :type blob_tags_string: str
        :param copy_source_blob_properties: Optional, default is true.  Indicates if properties from
         the source blob should be copied. Default value is None.
        :type copy_source_blob_properties: bool
        :param copy_source_authorization: Only Bearer type is supported. Credentials should be a valid
         OAuth access token to copy source. Default value is None.
        :type copy_source_authorization: str
        :param copy_source_tags: Optional, default \'replace\'.  Indicates if source tags should be
         copied or replaced with the tags specified by x-ms-tags. Known values are: "REPLACE" and
         "COPY". Default value is None.
        :type copy_source_tags: str or ~azure.storage.blob.models.BlobCopySourceTags
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
        :param source_modified_access_conditions: Parameter group. Default value is None.
        :type source_modified_access_conditions:
         ~azure.storage.blob.models.SourceModifiedAccessConditions
        :keyword blob_type: Specifies the type of blob to create: block blob, page blob, or append
         blob. Default value is "BlockBlob". Note that overriding this default value may result in
         unsupported behavior.
        :paramtype blob_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    async def stage_block(self, block_id: str, content_length: int, body: IO, transactional_content_md5: bytes | None = None, transactional_content_crc64: bytes | None = None, timeout: int | None = None, request_id_parameter: str | None = None, lease_access_conditions: _models.LeaseAccessConditions | None = None, cpk_info: _models.CpkInfo | None = None, cpk_scope_info: _models.CpkScopeInfo | None = None, **kwargs: Any) -> None:
        '''The Stage Block operation creates a new block to be committed as part of a blob.

        :param block_id: A valid Base64 string value that identifies the block. Prior to encoding, the
         string must be less than or equal to 64 bytes in size. For a given blob, the length of the
         value specified for the blockid parameter must be the same size for each block. Required.
        :type block_id: str
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
        :keyword comp: comp. Default value is "block". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    async def stage_block_from_url(self, block_id: str, content_length: int, source_url: str, source_range: str | None = None, source_content_md5: bytes | None = None, source_contentcrc64: bytes | None = None, timeout: int | None = None, request_id_parameter: str | None = None, copy_source_authorization: str | None = None, cpk_info: _models.CpkInfo | None = None, cpk_scope_info: _models.CpkScopeInfo | None = None, lease_access_conditions: _models.LeaseAccessConditions | None = None, source_modified_access_conditions: _models.SourceModifiedAccessConditions | None = None, **kwargs: Any) -> None:
        '''The Stage Block operation creates a new block to be committed as part of a blob where the
        contents are read from a URL.

        :param block_id: A valid Base64 string value that identifies the block. Prior to encoding, the
         string must be less than or equal to 64 bytes in size. For a given blob, the length of the
         value specified for the blockid parameter must be the same size for each block. Required.
        :type block_id: str
        :param content_length: The length of the request. Required.
        :type content_length: int
        :param source_url: Specify a URL to the copy source. Required.
        :type source_url: str
        :param source_range: Bytes of source data in the specified range. Default value is None.
        :type source_range: str
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
        :param source_modified_access_conditions: Parameter group. Default value is None.
        :type source_modified_access_conditions:
         ~azure.storage.blob.models.SourceModifiedAccessConditions
        :keyword comp: comp. Default value is "block". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    async def commit_block_list(self, blocks: _models.BlockLookupList, timeout: int | None = None, transactional_content_md5: bytes | None = None, transactional_content_crc64: bytes | None = None, metadata: Dict[str, str] | None = None, tier: str | _models.AccessTierOptional | None = None, request_id_parameter: str | None = None, blob_tags_string: str | None = None, immutability_policy_expiry: datetime.datetime | None = None, immutability_policy_mode: str | _models.BlobImmutabilityPolicyMode | None = None, legal_hold: bool | None = None, blob_http_headers: _models.BlobHTTPHeaders | None = None, lease_access_conditions: _models.LeaseAccessConditions | None = None, cpk_info: _models.CpkInfo | None = None, cpk_scope_info: _models.CpkScopeInfo | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, **kwargs: Any) -> None:
        '''The Commit Block List operation writes a blob by specifying the list of block IDs that make up
        the blob. In order to be written as part of a blob, a block must have been successfully written
        to the server in a prior Put Block operation. You can call Put Block List to update a blob by
        uploading only those blocks that have changed, then committing the new and existing blocks
        together. You can do this by specifying whether to commit a block from the committed block list
        or from the uncommitted block list, or to commit the most recently uploaded version of the
        block, whichever list it may belong to.

        :param blocks: Blob Blocks. Required.
        :type blocks: ~azure.storage.blob.models.BlockLookupList
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param transactional_content_md5: Specify the transactional md5 for the body, to be validated
         by the service. Default value is None.
        :type transactional_content_md5: bytes
        :param transactional_content_crc64: Specify the transactional crc64 for the body, to be
         validated by the service. Default value is None.
        :type transactional_content_crc64: bytes
        :param metadata: Optional. Specifies a user-defined name-value pair associated with the blob.
         If no name-value pairs are specified, the operation will copy the metadata from the source blob
         or file to the destination blob. If one or more name-value pairs are specified, the destination
         blob is created with the specified metadata, and metadata is not copied from the source blob or
         file. Note that beginning with version 2009-09-19, metadata names must adhere to the naming
         rules for C# identifiers. See Naming and Referencing Containers, Blobs, and Metadata for more
         information. Default value is None.
        :type metadata: dict[str, str]
        :param tier: Optional. Indicates the tier to be set on the blob. Known values are: "P4", "P6",
         "P10", "P15", "P20", "P30", "P40", "P50", "P60", "P70", "P80", "Hot", "Cool", "Archive", and
         "Cold". Default value is None.
        :type tier: str or ~azure.storage.blob.models.AccessTierOptional
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
        :keyword comp: comp. Default value is "blocklist". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    async def get_block_list(self, snapshot: str | None = None, list_type: str | _models.BlockListType = 'committed', timeout: int | None = None, request_id_parameter: str | None = None, lease_access_conditions: _models.LeaseAccessConditions | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, **kwargs: Any) -> _models.BlockList:
        '''The Get Block List operation retrieves the list of blocks that have been uploaded as part of a
        block blob.

        :param snapshot: The snapshot parameter is an opaque DateTime value that, when present,
         specifies the blob snapshot to retrieve. For more information on working with blob snapshots,
         see :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/creating-a-snapshot-of-a-blob">Creating
         a Snapshot of a Blob.</a>`. Default value is None.
        :type snapshot: str
        :param list_type: Specifies whether to return the list of committed blocks, the list of
         uncommitted blocks, or both lists together. Known values are: "committed", "uncommitted", and
         "all". Default value is "committed".
        :type list_type: str or ~azure.storage.blob.models.BlockListType
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
        :param modified_access_conditions: Parameter group. Default value is None.
        :type modified_access_conditions: ~azure.storage.blob.models.ModifiedAccessConditions
        :keyword comp: comp. Default value is "blocklist". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: BlockList or the result of cls(response)
        :rtype: ~azure.storage.blob.models.BlockList
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
