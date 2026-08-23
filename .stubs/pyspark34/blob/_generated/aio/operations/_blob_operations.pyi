import datetime
from ... import models as _models
from ...operations._blob_operations import build_abort_copy_from_url_request as build_abort_copy_from_url_request, build_acquire_lease_request as build_acquire_lease_request, build_break_lease_request as build_break_lease_request, build_change_lease_request as build_change_lease_request, build_copy_from_url_request as build_copy_from_url_request, build_create_snapshot_request as build_create_snapshot_request, build_delete_immutability_policy_request as build_delete_immutability_policy_request, build_delete_request as build_delete_request, build_download_request as build_download_request, build_get_account_info_request as build_get_account_info_request, build_get_properties_request as build_get_properties_request, build_get_tags_request as build_get_tags_request, build_query_request as build_query_request, build_release_lease_request as build_release_lease_request, build_renew_lease_request as build_renew_lease_request, build_set_expiry_request as build_set_expiry_request, build_set_http_headers_request as build_set_http_headers_request, build_set_immutability_policy_request as build_set_immutability_policy_request, build_set_legal_hold_request as build_set_legal_hold_request, build_set_metadata_request as build_set_metadata_request, build_set_tags_request as build_set_tags_request, build_set_tier_request as build_set_tier_request, build_start_copy_from_url_request as build_start_copy_from_url_request, build_undelete_request as build_undelete_request
from _typeshed import Incomplete
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from typing import Any, AsyncIterator, Callable, Dict, Literal, TypeVar

T = TypeVar('T')
ClsType = Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any] | None

class BlobOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.storage.blob.aio.AzureBlobStorage`'s
        :attr:`blob` attribute.
    """
    models: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    async def download(self, snapshot: str | None = None, version_id: str | None = None, timeout: int | None = None, range: str | None = None, range_get_content_md5: bool | None = None, range_get_content_crc64: bool | None = None, request_id_parameter: str | None = None, lease_access_conditions: _models.LeaseAccessConditions | None = None, cpk_info: _models.CpkInfo | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, **kwargs: Any) -> AsyncIterator[bytes]:
        '''The Download operation reads or downloads a blob from the system, including its metadata and
        properties. You can also call Download to read a snapshot.

        :param snapshot: The snapshot parameter is an opaque DateTime value that, when present,
         specifies the blob snapshot to retrieve. For more information on working with blob snapshots,
         see :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/creating-a-snapshot-of-a-blob">Creating
         a Snapshot of a Blob.</a>`. Default value is None.
        :type snapshot: str
        :param version_id: The version id parameter is an opaque DateTime value that, when present,
         specifies the version of the blob to operate on. It\'s for service version 2019-10-10 and newer.
         Default value is None.
        :type version_id: str
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param range: Return only the bytes of the blob in the specified range. Default value is None.
        :type range: str
        :param range_get_content_md5: When set to true and specified together with the Range, the
         service returns the MD5 hash for the range, as long as the range is less than or equal to 4 MB
         in size. Default value is None.
        :type range_get_content_md5: bool
        :param range_get_content_crc64: When set to true and specified together with the Range, the
         service returns the CRC64 hash for the range, as long as the range is less than or equal to 4
         MB in size. Default value is None.
        :type range_get_content_crc64: bool
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param lease_access_conditions: Parameter group. Default value is None.
        :type lease_access_conditions: ~azure.storage.blob.models.LeaseAccessConditions
        :param cpk_info: Parameter group. Default value is None.
        :type cpk_info: ~azure.storage.blob.models.CpkInfo
        :param modified_access_conditions: Parameter group. Default value is None.
        :type modified_access_conditions: ~azure.storage.blob.models.ModifiedAccessConditions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Async iterator of the response bytes or the result of cls(response)
        :rtype: AsyncIterator[bytes]
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    async def get_properties(self, snapshot: str | None = None, version_id: str | None = None, timeout: int | None = None, request_id_parameter: str | None = None, lease_access_conditions: _models.LeaseAccessConditions | None = None, cpk_info: _models.CpkInfo | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, **kwargs: Any) -> None:
        '''The Get Properties operation returns all user-defined metadata, standard HTTP properties, and
        system properties for the blob. It does not return the content of the blob.

        :param snapshot: The snapshot parameter is an opaque DateTime value that, when present,
         specifies the blob snapshot to retrieve. For more information on working with blob snapshots,
         see :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/creating-a-snapshot-of-a-blob">Creating
         a Snapshot of a Blob.</a>`. Default value is None.
        :type snapshot: str
        :param version_id: The version id parameter is an opaque DateTime value that, when present,
         specifies the version of the blob to operate on. It\'s for service version 2019-10-10 and newer.
         Default value is None.
        :type version_id: str
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
        :param modified_access_conditions: Parameter group. Default value is None.
        :type modified_access_conditions: ~azure.storage.blob.models.ModifiedAccessConditions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    async def delete(self, snapshot: str | None = None, version_id: str | None = None, timeout: int | None = None, delete_snapshots: str | _models.DeleteSnapshotsOptionType | None = None, request_id_parameter: str | None = None, blob_delete_type: Literal['Permanent'] = 'Permanent', lease_access_conditions: _models.LeaseAccessConditions | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, **kwargs: Any) -> None:
        '''If the storage account\'s soft delete feature is disabled then, when a blob is deleted, it is
        permanently removed from the storage account. If the storage account\'s soft delete feature is
        enabled, then, when a blob is deleted, it is marked for deletion and becomes inaccessible
        immediately. However, the blob service retains the blob or snapshot for the number of days
        specified by the DeleteRetentionPolicy section of [Storage service properties]
        (Set-Blob-Service-Properties.md). After the specified number of days has passed, the blob\'s
        data is permanently removed from the storage account. Note that you continue to be charged for
        the soft-deleted blob\'s storage until it is permanently removed. Use the List Blobs API and
        specify the "include=deleted" query parameter to discover which blobs and snapshots have been
        soft deleted. You can then use the Undelete Blob API to restore a soft-deleted blob. All other
        operations on a soft-deleted blob or snapshot causes the service to return an HTTP status code
        of 404 (ResourceNotFound).

        :param snapshot: The snapshot parameter is an opaque DateTime value that, when present,
         specifies the blob snapshot to retrieve. For more information on working with blob snapshots,
         see :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/creating-a-snapshot-of-a-blob">Creating
         a Snapshot of a Blob.</a>`. Default value is None.
        :type snapshot: str
        :param version_id: The version id parameter is an opaque DateTime value that, when present,
         specifies the version of the blob to operate on. It\'s for service version 2019-10-10 and newer.
         Default value is None.
        :type version_id: str
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param delete_snapshots: Required if the blob has associated snapshots. Specify one of the
         following two options: include: Delete the base blob and all of its snapshots. only: Delete
         only the blob\'s snapshots and not the blob itself. Known values are: "include" and "only".
         Default value is None.
        :type delete_snapshots: str or ~azure.storage.blob.models.DeleteSnapshotsOptionType
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param blob_delete_type: Optional.  Only possible value is \'permanent\', which specifies to
         permanently delete a blob if blob soft delete is enabled. Known values are "Permanent" and
         None. Default value is "Permanent".
        :type blob_delete_type: str
        :param lease_access_conditions: Parameter group. Default value is None.
        :type lease_access_conditions: ~azure.storage.blob.models.LeaseAccessConditions
        :param modified_access_conditions: Parameter group. Default value is None.
        :type modified_access_conditions: ~azure.storage.blob.models.ModifiedAccessConditions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    async def undelete(self, timeout: int | None = None, request_id_parameter: str | None = None, **kwargs: Any) -> None:
        '''Undelete a blob that was previously soft deleted.

        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :keyword comp: comp. Default value is "undelete". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    async def set_expiry(self, expiry_options: str | _models.BlobExpiryOptions, timeout: int | None = None, request_id_parameter: str | None = None, expires_on: str | None = None, **kwargs: Any) -> None:
        '''Sets the time a blob will expire and be deleted.

        :param expiry_options: Required. Indicates mode of the expiry time. Known values are:
         "NeverExpire", "RelativeToCreation", "RelativeToNow", and "Absolute". Required.
        :type expiry_options: str or ~azure.storage.blob.models.BlobExpiryOptions
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param expires_on: The time to set the blob to expiry. Default value is None.
        :type expires_on: str
        :keyword comp: comp. Default value is "expiry". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    async def set_http_headers(self, timeout: int | None = None, request_id_parameter: str | None = None, blob_http_headers: _models.BlobHTTPHeaders | None = None, lease_access_conditions: _models.LeaseAccessConditions | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, **kwargs: Any) -> None:
        '''The Set HTTP Headers operation sets system properties on the blob.

        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param blob_http_headers: Parameter group. Default value is None.
        :type blob_http_headers: ~azure.storage.blob.models.BlobHTTPHeaders
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
    async def set_immutability_policy(self, timeout: int | None = None, request_id_parameter: str | None = None, immutability_policy_expiry: datetime.datetime | None = None, immutability_policy_mode: str | _models.BlobImmutabilityPolicyMode | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, **kwargs: Any) -> None:
        '''The Set Immutability Policy operation sets the immutability policy on the blob.

        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param immutability_policy_expiry: Specifies the date time when the blobs immutability policy
         is set to expire. Default value is None.
        :type immutability_policy_expiry: ~datetime.datetime
        :param immutability_policy_mode: Specifies the immutability policy mode to set on the blob.
         Known values are: "Mutable", "Unlocked", and "Locked". Default value is None.
        :type immutability_policy_mode: str or ~azure.storage.blob.models.BlobImmutabilityPolicyMode
        :param modified_access_conditions: Parameter group. Default value is None.
        :type modified_access_conditions: ~azure.storage.blob.models.ModifiedAccessConditions
        :keyword comp: comp. Default value is "immutabilityPolicies". Note that overriding this default
         value may result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    async def delete_immutability_policy(self, timeout: int | None = None, request_id_parameter: str | None = None, **kwargs: Any) -> None:
        '''The Delete Immutability Policy operation deletes the immutability policy on the blob.

        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :keyword comp: comp. Default value is "immutabilityPolicies". Note that overriding this default
         value may result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    async def set_legal_hold(self, legal_hold: bool, timeout: int | None = None, request_id_parameter: str | None = None, **kwargs: Any) -> None:
        '''The Set Legal Hold operation sets a legal hold on the blob.

        :param legal_hold: Specified if a legal hold should be set on the blob. Required.
        :type legal_hold: bool
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :keyword comp: comp. Default value is "legalhold". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    async def set_metadata(self, timeout: int | None = None, metadata: Dict[str, str] | None = None, request_id_parameter: str | None = None, lease_access_conditions: _models.LeaseAccessConditions | None = None, cpk_info: _models.CpkInfo | None = None, cpk_scope_info: _models.CpkScopeInfo | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, **kwargs: Any) -> None:
        '''The Set Blob Metadata operation sets user-defined metadata for the specified blob as one or
        more name-value pairs.

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
        :param lease_access_conditions: Parameter group. Default value is None.
        :type lease_access_conditions: ~azure.storage.blob.models.LeaseAccessConditions
        :param cpk_info: Parameter group. Default value is None.
        :type cpk_info: ~azure.storage.blob.models.CpkInfo
        :param cpk_scope_info: Parameter group. Default value is None.
        :type cpk_scope_info: ~azure.storage.blob.models.CpkScopeInfo
        :param modified_access_conditions: Parameter group. Default value is None.
        :type modified_access_conditions: ~azure.storage.blob.models.ModifiedAccessConditions
        :keyword comp: comp. Default value is "metadata". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    async def acquire_lease(self, timeout: int | None = None, duration: int | None = None, proposed_lease_id: str | None = None, request_id_parameter: str | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, **kwargs: Any) -> None:
        '''[Update] The Lease Blob operation establishes and manages a lock on a blob for write and delete
        operations.

        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param duration: Specifies the duration of the lease, in seconds, or negative one (-1) for a
         lease that never expires. A non-infinite lease can be between 15 and 60 seconds. A lease
         duration cannot be changed using renew or change. Default value is None.
        :type duration: int
        :param proposed_lease_id: Proposed lease ID, in a GUID string format. The Blob service returns
         400 (Invalid request) if the proposed lease ID is not in the correct format. See Guid
         Constructor (String) for a list of valid GUID string formats. Default value is None.
        :type proposed_lease_id: str
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param modified_access_conditions: Parameter group. Default value is None.
        :type modified_access_conditions: ~azure.storage.blob.models.ModifiedAccessConditions
        :keyword comp: comp. Default value is "lease". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword action: Describes what lease action to take. Default value is "acquire". Note that
         overriding this default value may result in unsupported behavior.
        :paramtype action: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    async def release_lease(self, lease_id: str, timeout: int | None = None, request_id_parameter: str | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, **kwargs: Any) -> None:
        '''[Update] The Lease Blob operation establishes and manages a lock on a blob for write and delete
        operations.

        :param lease_id: Specifies the current lease ID on the resource. Required.
        :type lease_id: str
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
        :keyword comp: comp. Default value is "lease". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword action: Describes what lease action to take. Default value is "release". Note that
         overriding this default value may result in unsupported behavior.
        :paramtype action: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    async def renew_lease(self, lease_id: str, timeout: int | None = None, request_id_parameter: str | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, **kwargs: Any) -> None:
        '''[Update] The Lease Blob operation establishes and manages a lock on a blob for write and delete
        operations.

        :param lease_id: Specifies the current lease ID on the resource. Required.
        :type lease_id: str
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
        :keyword comp: comp. Default value is "lease". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword action: Describes what lease action to take. Default value is "renew". Note that
         overriding this default value may result in unsupported behavior.
        :paramtype action: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    async def change_lease(self, lease_id: str, proposed_lease_id: str, timeout: int | None = None, request_id_parameter: str | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, **kwargs: Any) -> None:
        '''[Update] The Lease Blob operation establishes and manages a lock on a blob for write and delete
        operations.

        :param lease_id: Specifies the current lease ID on the resource. Required.
        :type lease_id: str
        :param proposed_lease_id: Proposed lease ID, in a GUID string format. The Blob service returns
         400 (Invalid request) if the proposed lease ID is not in the correct format. See Guid
         Constructor (String) for a list of valid GUID string formats. Required.
        :type proposed_lease_id: str
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
        :keyword comp: comp. Default value is "lease". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword action: Describes what lease action to take. Default value is "change". Note that
         overriding this default value may result in unsupported behavior.
        :paramtype action: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    async def break_lease(self, timeout: int | None = None, break_period: int | None = None, request_id_parameter: str | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, **kwargs: Any) -> None:
        '''[Update] The Lease Blob operation establishes and manages a lock on a blob for write and delete
        operations.

        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param break_period: For a break operation, proposed duration the lease should continue before
         it is broken, in seconds, between 0 and 60. This break period is only used if it is shorter
         than the time remaining on the lease. If longer, the time remaining on the lease is used. A new
         lease will not be available before the break period has expired, but the lease may be held for
         longer than the break period. If this header does not appear with a break operation, a
         fixed-duration lease breaks after the remaining lease period elapses, and an infinite lease
         breaks immediately. Default value is None.
        :type break_period: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param modified_access_conditions: Parameter group. Default value is None.
        :type modified_access_conditions: ~azure.storage.blob.models.ModifiedAccessConditions
        :keyword comp: comp. Default value is "lease". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword action: Describes what lease action to take. Default value is "break". Note that
         overriding this default value may result in unsupported behavior.
        :paramtype action: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    async def create_snapshot(self, timeout: int | None = None, metadata: Dict[str, str] | None = None, request_id_parameter: str | None = None, cpk_info: _models.CpkInfo | None = None, cpk_scope_info: _models.CpkScopeInfo | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, lease_access_conditions: _models.LeaseAccessConditions | None = None, **kwargs: Any) -> None:
        '''The Create Snapshot operation creates a read-only snapshot of a blob.

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
        :param cpk_info: Parameter group. Default value is None.
        :type cpk_info: ~azure.storage.blob.models.CpkInfo
        :param cpk_scope_info: Parameter group. Default value is None.
        :type cpk_scope_info: ~azure.storage.blob.models.CpkScopeInfo
        :param modified_access_conditions: Parameter group. Default value is None.
        :type modified_access_conditions: ~azure.storage.blob.models.ModifiedAccessConditions
        :param lease_access_conditions: Parameter group. Default value is None.
        :type lease_access_conditions: ~azure.storage.blob.models.LeaseAccessConditions
        :keyword comp: comp. Default value is "snapshot". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    async def start_copy_from_url(self, copy_source: str, timeout: int | None = None, metadata: Dict[str, str] | None = None, tier: str | _models.AccessTierOptional | None = None, rehydrate_priority: str | _models.RehydratePriority | None = None, request_id_parameter: str | None = None, blob_tags_string: str | None = None, seal_blob: bool | None = None, immutability_policy_expiry: datetime.datetime | None = None, immutability_policy_mode: str | _models.BlobImmutabilityPolicyMode | None = None, legal_hold: bool | None = None, source_modified_access_conditions: _models.SourceModifiedAccessConditions | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, lease_access_conditions: _models.LeaseAccessConditions | None = None, **kwargs: Any) -> None:
        '''The Start Copy From URL operation copies a blob or an internet resource to a new blob.

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
        :param rehydrate_priority: Optional: Indicates the priority with which to rehydrate an archived
         blob. Known values are: "High" and "Standard". Default value is None.
        :type rehydrate_priority: str or ~azure.storage.blob.models.RehydratePriority
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param blob_tags_string: Optional.  Used to set blob tags in various blob operations. Default
         value is None.
        :type blob_tags_string: str
        :param seal_blob: Overrides the sealed state of the destination blob.  Service version
         2019-12-12 and newer. Default value is None.
        :type seal_blob: bool
        :param immutability_policy_expiry: Specifies the date time when the blobs immutability policy
         is set to expire. Default value is None.
        :type immutability_policy_expiry: ~datetime.datetime
        :param immutability_policy_mode: Specifies the immutability policy mode to set on the blob.
         Known values are: "Mutable", "Unlocked", and "Locked". Default value is None.
        :type immutability_policy_mode: str or ~azure.storage.blob.models.BlobImmutabilityPolicyMode
        :param legal_hold: Specified if a legal hold should be set on the blob. Default value is None.
        :type legal_hold: bool
        :param source_modified_access_conditions: Parameter group. Default value is None.
        :type source_modified_access_conditions:
         ~azure.storage.blob.models.SourceModifiedAccessConditions
        :param modified_access_conditions: Parameter group. Default value is None.
        :type modified_access_conditions: ~azure.storage.blob.models.ModifiedAccessConditions
        :param lease_access_conditions: Parameter group. Default value is None.
        :type lease_access_conditions: ~azure.storage.blob.models.LeaseAccessConditions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    async def copy_from_url(self, copy_source: str, timeout: int | None = None, metadata: Dict[str, str] | None = None, tier: str | _models.AccessTierOptional | None = None, request_id_parameter: str | None = None, source_content_md5: bytes | None = None, blob_tags_string: str | None = None, immutability_policy_expiry: datetime.datetime | None = None, immutability_policy_mode: str | _models.BlobImmutabilityPolicyMode | None = None, legal_hold: bool | None = None, copy_source_authorization: str | None = None, copy_source_tags: str | _models.BlobCopySourceTags | None = None, source_modified_access_conditions: _models.SourceModifiedAccessConditions | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, lease_access_conditions: _models.LeaseAccessConditions | None = None, cpk_scope_info: _models.CpkScopeInfo | None = None, **kwargs: Any) -> None:
        '''The Copy From URL operation copies a blob or an internet resource to a new blob. It will not
        return a response until the copy is complete.

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
        :param immutability_policy_expiry: Specifies the date time when the blobs immutability policy
         is set to expire. Default value is None.
        :type immutability_policy_expiry: ~datetime.datetime
        :param immutability_policy_mode: Specifies the immutability policy mode to set on the blob.
         Known values are: "Mutable", "Unlocked", and "Locked". Default value is None.
        :type immutability_policy_mode: str or ~azure.storage.blob.models.BlobImmutabilityPolicyMode
        :param legal_hold: Specified if a legal hold should be set on the blob. Default value is None.
        :type legal_hold: bool
        :param copy_source_authorization: Only Bearer type is supported. Credentials should be a valid
         OAuth access token to copy source. Default value is None.
        :type copy_source_authorization: str
        :param copy_source_tags: Optional, default \'replace\'.  Indicates if source tags should be
         copied or replaced with the tags specified by x-ms-tags. Known values are: "REPLACE" and
         "COPY". Default value is None.
        :type copy_source_tags: str or ~azure.storage.blob.models.BlobCopySourceTags
        :param source_modified_access_conditions: Parameter group. Default value is None.
        :type source_modified_access_conditions:
         ~azure.storage.blob.models.SourceModifiedAccessConditions
        :param modified_access_conditions: Parameter group. Default value is None.
        :type modified_access_conditions: ~azure.storage.blob.models.ModifiedAccessConditions
        :param lease_access_conditions: Parameter group. Default value is None.
        :type lease_access_conditions: ~azure.storage.blob.models.LeaseAccessConditions
        :param cpk_scope_info: Parameter group. Default value is None.
        :type cpk_scope_info: ~azure.storage.blob.models.CpkScopeInfo
        :keyword x_ms_requires_sync: This header indicates that this is a synchronous Copy Blob From
         URL instead of a Asynchronous Copy Blob. Default value is "true". Note that overriding this
         default value may result in unsupported behavior.
        :paramtype x_ms_requires_sync: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    async def abort_copy_from_url(self, copy_id: str, timeout: int | None = None, request_id_parameter: str | None = None, lease_access_conditions: _models.LeaseAccessConditions | None = None, **kwargs: Any) -> None:
        '''The Abort Copy From URL operation aborts a pending Copy From URL operation, and leaves a
        destination blob with zero length and full metadata.

        :param copy_id: The copy identifier provided in the x-ms-copy-id header of the original Copy
         Blob operation. Required.
        :type copy_id: str
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
        :keyword comp: comp. Default value is "copy". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword copy_action_abort_constant: Copy action. Default value is "abort". Note that
         overriding this default value may result in unsupported behavior.
        :paramtype copy_action_abort_constant: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    async def set_tier(self, tier: str | _models.AccessTierRequired, snapshot: str | None = None, version_id: str | None = None, timeout: int | None = None, rehydrate_priority: str | _models.RehydratePriority | None = None, request_id_parameter: str | None = None, lease_access_conditions: _models.LeaseAccessConditions | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, **kwargs: Any) -> None:
        '''The Set Tier operation sets the tier on a blob. The operation is allowed on a page blob in a
        premium storage account and on a block blob in a blob storage account (locally redundant
        storage only). A premium page blob\'s tier determines the allowed size, IOPS, and bandwidth of
        the blob. A block blob\'s tier determines Hot/Cool/Archive storage type. This operation does not
        update the blob\'s ETag.

        :param tier: Indicates the tier to be set on the blob. Known values are: "P4", "P6", "P10",
         "P15", "P20", "P30", "P40", "P50", "P60", "P70", "P80", "Hot", "Cool", "Archive", and "Cold".
         Required.
        :type tier: str or ~azure.storage.blob.models.AccessTierRequired
        :param snapshot: The snapshot parameter is an opaque DateTime value that, when present,
         specifies the blob snapshot to retrieve. For more information on working with blob snapshots,
         see :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/creating-a-snapshot-of-a-blob">Creating
         a Snapshot of a Blob.</a>`. Default value is None.
        :type snapshot: str
        :param version_id: The version id parameter is an opaque DateTime value that, when present,
         specifies the version of the blob to operate on. It\'s for service version 2019-10-10 and newer.
         Default value is None.
        :type version_id: str
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param rehydrate_priority: Optional: Indicates the priority with which to rehydrate an archived
         blob. Known values are: "High" and "Standard". Default value is None.
        :type rehydrate_priority: str or ~azure.storage.blob.models.RehydratePriority
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param lease_access_conditions: Parameter group. Default value is None.
        :type lease_access_conditions: ~azure.storage.blob.models.LeaseAccessConditions
        :param modified_access_conditions: Parameter group. Default value is None.
        :type modified_access_conditions: ~azure.storage.blob.models.ModifiedAccessConditions
        :keyword comp: comp. Default value is "tier". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    async def get_account_info(self, **kwargs: Any) -> None:
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
    async def query(self, snapshot: str | None = None, timeout: int | None = None, request_id_parameter: str | None = None, lease_access_conditions: _models.LeaseAccessConditions | None = None, cpk_info: _models.CpkInfo | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, query_request: _models.QueryRequest | None = None, **kwargs: Any) -> AsyncIterator[bytes]:
        '''The Query operation enables users to select/project on blob data by providing simple query
        expressions.

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
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param lease_access_conditions: Parameter group. Default value is None.
        :type lease_access_conditions: ~azure.storage.blob.models.LeaseAccessConditions
        :param cpk_info: Parameter group. Default value is None.
        :type cpk_info: ~azure.storage.blob.models.CpkInfo
        :param modified_access_conditions: Parameter group. Default value is None.
        :type modified_access_conditions: ~azure.storage.blob.models.ModifiedAccessConditions
        :param query_request: the query request. Default value is None.
        :type query_request: ~azure.storage.blob.models.QueryRequest
        :keyword comp: comp. Default value is "query". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Async iterator of the response bytes or the result of cls(response)
        :rtype: AsyncIterator[bytes]
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    async def get_tags(self, timeout: int | None = None, request_id_parameter: str | None = None, snapshot: str | None = None, version_id: str | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, lease_access_conditions: _models.LeaseAccessConditions | None = None, **kwargs: Any) -> _models.BlobTags:
        '''The Get Tags operation enables users to get the tags associated with a blob.

        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param snapshot: The snapshot parameter is an opaque DateTime value that, when present,
         specifies the blob snapshot to retrieve. For more information on working with blob snapshots,
         see :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/creating-a-snapshot-of-a-blob">Creating
         a Snapshot of a Blob.</a>`. Default value is None.
        :type snapshot: str
        :param version_id: The version id parameter is an opaque DateTime value that, when present,
         specifies the version of the blob to operate on. It\'s for service version 2019-10-10 and newer.
         Default value is None.
        :type version_id: str
        :param modified_access_conditions: Parameter group. Default value is None.
        :type modified_access_conditions: ~azure.storage.blob.models.ModifiedAccessConditions
        :param lease_access_conditions: Parameter group. Default value is None.
        :type lease_access_conditions: ~azure.storage.blob.models.LeaseAccessConditions
        :keyword comp: comp. Default value is "tags". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: BlobTags or the result of cls(response)
        :rtype: ~azure.storage.blob.models.BlobTags
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    async def set_tags(self, timeout: int | None = None, version_id: str | None = None, transactional_content_md5: bytes | None = None, transactional_content_crc64: bytes | None = None, request_id_parameter: str | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, lease_access_conditions: _models.LeaseAccessConditions | None = None, tags: _models.BlobTags | None = None, **kwargs: Any) -> None:
        '''The Set Tags operation enables users to set tags on a blob.

        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param version_id: The version id parameter is an opaque DateTime value that, when present,
         specifies the version of the blob to operate on. It\'s for service version 2019-10-10 and newer.
         Default value is None.
        :type version_id: str
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
        :param modified_access_conditions: Parameter group. Default value is None.
        :type modified_access_conditions: ~azure.storage.blob.models.ModifiedAccessConditions
        :param lease_access_conditions: Parameter group. Default value is None.
        :type lease_access_conditions: ~azure.storage.blob.models.LeaseAccessConditions
        :param tags: Blob tags. Default value is None.
        :type tags: ~azure.storage.blob.models.BlobTags
        :keyword comp: comp. Default value is "tags". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
