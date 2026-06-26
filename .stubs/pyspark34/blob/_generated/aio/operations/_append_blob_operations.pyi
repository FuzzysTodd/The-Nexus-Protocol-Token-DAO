import datetime
from ... import models as _models
from ...operations._append_blob_operations import build_append_block_from_url_request as build_append_block_from_url_request, build_append_block_request as build_append_block_request, build_create_request as build_create_request, build_seal_request as build_seal_request
from _typeshed import Incomplete
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from typing import Any, Callable, Dict, IO, TypeVar

T = TypeVar('T')
ClsType = Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any] | None

class AppendBlobOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.storage.blob.aio.AzureBlobStorage`'s
        :attr:`append_blob` attribute.
    """
    models: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    async def create(self, content_length: int, timeout: int | None = None, metadata: Dict[str, str] | None = None, request_id_parameter: str | None = None, blob_tags_string: str | None = None, immutability_policy_expiry: datetime.datetime | None = None, immutability_policy_mode: str | _models.BlobImmutabilityPolicyMode | None = None, legal_hold: bool | None = None, blob_http_headers: _models.BlobHTTPHeaders | None = None, lease_access_conditions: _models.LeaseAccessConditions | None = None, cpk_info: _models.CpkInfo | None = None, cpk_scope_info: _models.CpkScopeInfo | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, **kwargs: Any) -> None:
        '''The Create Append Blob operation creates a new append blob.

        :param content_length: The length of the request. Required.
        :type content_length: int
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param metadata: Optional. Specifies a user-defined name-value pair associated with the blob.
         If no name-value pairs are specified, the operation will copy the metadata from the source blob
         or file to the destination blob. If one or more name-value pairs are specified, the destination
         blob is created with the specified metadata, and metadata is not copied from the source blob or
         file. Note that beginning with version 2009-09-19, metadata names must adhere to the naming
         rules for C# identifiers. See Naming and Referencing Containers, Blobs, and Metadata for more
         information. Default value is None.
        :type metadata: dict[str, str]
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
         blob. Default value is "AppendBlob". Note that overriding this default value may result in
         unsupported behavior.
        :paramtype blob_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    async def append_block(self, content_length: int, body: IO, timeout: int | None = None, transactional_content_md5: bytes | None = None, transactional_content_crc64: bytes | None = None, request_id_parameter: str | None = None, lease_access_conditions: _models.LeaseAccessConditions | None = None, append_position_access_conditions: _models.AppendPositionAccessConditions | None = None, cpk_info: _models.CpkInfo | None = None, cpk_scope_info: _models.CpkScopeInfo | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, **kwargs: Any) -> None:
        '''The Append Block operation commits a new block of data to the end of an existing append blob.
        The Append Block operation is permitted only if the blob was created with x-ms-blob-type set to
        AppendBlob. Append Block is supported only on version 2015-02-21 version or later.

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
        :param transactional_content_crc64: Specify the transactional crc64 for the body, to be
         validated by the service. Default value is None.
        :type transactional_content_crc64: bytes
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param lease_access_conditions: Parameter group. Default value is None.
        :type lease_access_conditions: ~azure.storage.blob.models.LeaseAccessConditions
        :param append_position_access_conditions: Parameter group. Default value is None.
        :type append_position_access_conditions:
         ~azure.storage.blob.models.AppendPositionAccessConditions
        :param cpk_info: Parameter group. Default value is None.
        :type cpk_info: ~azure.storage.blob.models.CpkInfo
        :param cpk_scope_info: Parameter group. Default value is None.
        :type cpk_scope_info: ~azure.storage.blob.models.CpkScopeInfo
        :param modified_access_conditions: Parameter group. Default value is None.
        :type modified_access_conditions: ~azure.storage.blob.models.ModifiedAccessConditions
        :keyword comp: comp. Default value is "appendblock". Note that overriding this default value
         may result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    async def append_block_from_url(self, source_url: str, content_length: int, source_range: str | None = None, source_content_md5: bytes | None = None, source_contentcrc64: bytes | None = None, timeout: int | None = None, transactional_content_md5: bytes | None = None, request_id_parameter: str | None = None, copy_source_authorization: str | None = None, cpk_info: _models.CpkInfo | None = None, cpk_scope_info: _models.CpkScopeInfo | None = None, lease_access_conditions: _models.LeaseAccessConditions | None = None, append_position_access_conditions: _models.AppendPositionAccessConditions | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, source_modified_access_conditions: _models.SourceModifiedAccessConditions | None = None, **kwargs: Any) -> None:
        '''The Append Block operation commits a new block of data to the end of an existing append blob
        where the contents are read from a source url. The Append Block operation is permitted only if
        the blob was created with x-ms-blob-type set to AppendBlob. Append Block is supported only on
        version 2015-02-21 version or later.

        :param source_url: Specify a URL to the copy source. Required.
        :type source_url: str
        :param content_length: The length of the request. Required.
        :type content_length: int
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
        :param transactional_content_md5: Specify the transactional md5 for the body, to be validated
         by the service. Default value is None.
        :type transactional_content_md5: bytes
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
        :param append_position_access_conditions: Parameter group. Default value is None.
        :type append_position_access_conditions:
         ~azure.storage.blob.models.AppendPositionAccessConditions
        :param modified_access_conditions: Parameter group. Default value is None.
        :type modified_access_conditions: ~azure.storage.blob.models.ModifiedAccessConditions
        :param source_modified_access_conditions: Parameter group. Default value is None.
        :type source_modified_access_conditions:
         ~azure.storage.blob.models.SourceModifiedAccessConditions
        :keyword comp: comp. Default value is "appendblock". Note that overriding this default value
         may result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    async def seal(self, timeout: int | None = None, request_id_parameter: str | None = None, lease_access_conditions: _models.LeaseAccessConditions | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, append_position_access_conditions: _models.AppendPositionAccessConditions | None = None, **kwargs: Any) -> None:
        '''The Seal operation seals the Append Blob to make it read-only. Seal is supported only on
        version 2019-12-12 version or later.

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
        :param append_position_access_conditions: Parameter group. Default value is None.
        :type append_position_access_conditions:
         ~azure.storage.blob.models.AppendPositionAccessConditions
        :keyword comp: comp. Default value is "seal". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
