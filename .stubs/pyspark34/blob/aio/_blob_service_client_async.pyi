from .._blob_service_client import BlobServiceClient as BlobServiceClientBase
from .._deserialize import service_properties_deserialize as service_properties_deserialize, service_stats_deserialize as service_stats_deserialize
from .._encryption import StorageEncryptionMixin as StorageEncryptionMixin
from .._generated.aio import AzureBlobStorage as AzureBlobStorage
from .._generated.models import KeyInfo as KeyInfo, StorageServiceProperties as StorageServiceProperties
from .._models import BlobAnalyticsLogging as BlobAnalyticsLogging, BlobProperties as BlobProperties, ContainerProperties as ContainerProperties, CorsRule as CorsRule, Metrics as Metrics, PublicAccess as PublicAccess, RetentionPolicy as RetentionPolicy, StaticWebsite as StaticWebsite
from .._serialize import get_api_version as get_api_version
from .._shared.base_client_async import AsyncStorageAccountHostsMixin as AsyncStorageAccountHostsMixin, AsyncTransportWrapper as AsyncTransportWrapper
from .._shared.models import LocationMode as LocationMode, UserDelegationKey as UserDelegationKey
from .._shared.policies_async import ExponentialRetry as ExponentialRetry
from .._shared.response_handlers import parse_to_internal_user_delegation_key as parse_to_internal_user_delegation_key, process_storage_error as process_storage_error, return_response_headers as return_response_headers
from ._blob_client_async import BlobClient as BlobClient
from ._container_client_async import ContainerClient as ContainerClient
from ._lease_async import BlobLeaseClient as BlobLeaseClient
from ._models import ContainerPropertiesPaged as ContainerPropertiesPaged, FilteredBlobPaged as FilteredBlobPaged
from azure.core.async_paging import AsyncItemPaged
from azure.core.credentials import AzureNamedKeyCredential as AzureNamedKeyCredential, AzureSasCredential as AzureSasCredential
from azure.core.credentials_async import AsyncTokenCredential as AsyncTokenCredential
from datetime import datetime
from typing import Any, Dict, List

class BlobServiceClient(AsyncStorageAccountHostsMixin, BlobServiceClientBase, StorageEncryptionMixin):
    '''A client to interact with the Blob Service at the account level.

    This client provides operations to retrieve and configure the account properties
    as well as list, create and delete containers within the account.
    For operations relating to a specific container or blob, clients for those entities
    can also be retrieved using the `get_client` functions.

    :param str account_url:
        The URL to the blob storage account. Any other entities included
        in the URL path (e.g. container or blob) will be discarded. This URL can be optionally
        authenticated with a SAS token.
    :param credential:
        The credentials with which to authenticate. This is optional if the
        account URL already has a SAS token. The value can be a SAS token string,
        an instance of a AzureSasCredential or AzureNamedKeyCredential from azure.core.credentials,
        an account shared access key, or an instance of a TokenCredentials class from azure.identity.
        If the resource URI already contains a SAS token, this will be ignored in favor of an explicit credential
        - except in the case of AzureSasCredential, where the conflicting SAS tokens will raise a ValueError.
        If using an instance of AzureNamedKeyCredential, "name" should be the storage account name, and "key"
        should be the storage account key.
    :keyword str api_version:
        The Storage API version to use for requests. Default value is the most recent service version that is
        compatible with the current SDK. Setting to an older version may result in reduced feature compatibility.

        .. versionadded:: 12.2.0

    :keyword str secondary_hostname:
        The hostname of the secondary endpoint.
    :keyword int max_block_size: The maximum chunk size for uploading a block blob in chunks.
        Defaults to 4*1024*1024, or 4MB.
    :keyword int max_single_put_size: If the blob size is less than or equal max_single_put_size, then the blob will be
        uploaded with only one http PUT request. If the blob size is larger than max_single_put_size,
        the blob will be uploaded in chunks. Defaults to 64*1024*1024, or 64MB.
    :keyword int min_large_block_upload_threshold: The minimum chunk size required to use the memory efficient
        algorithm when uploading a block blob. Defaults to 4*1024*1024+1.
    :keyword bool use_byte_buffer: Use a byte buffer for block blob uploads. Defaults to False.
    :keyword int max_page_size: The maximum chunk size for uploading a page blob. Defaults to 4*1024*1024, or 4MB.
    :keyword int max_single_get_size: The maximum size for a blob to be downloaded in a single call,
        the exceeded part will be downloaded in chunks (could be parallel). Defaults to 32*1024*1024, or 32MB.
    :keyword int max_chunk_get_size: The maximum chunk size used for downloading a blob. Defaults to 4*1024*1024,
        or 4MB.

    .. admonition:: Example:

        .. literalinclude:: ../samples/blob_samples_authentication_async.py
            :start-after: [START create_blob_service_client]
            :end-before: [END create_blob_service_client]
            :language: python
            :dedent: 8
            :caption: Creating the BlobServiceClient with account url and credential.

        .. literalinclude:: ../samples/blob_samples_authentication_async.py
            :start-after: [START create_blob_service_client_oauth]
            :end-before: [END create_blob_service_client_oauth]
            :language: python
            :dedent: 8
            :caption: Creating the BlobServiceClient with Azure Identity credentials.
    '''
    def __init__(self, account_url: str, credential: str | Dict[str, str] | AzureNamedKeyCredential | AzureSasCredential | AsyncTokenCredential | None = None, **kwargs: Any) -> None: ...
    async def get_user_delegation_key(self, key_start_time: datetime, key_expiry_time: datetime, **kwargs: Any) -> UserDelegationKey:
        """
        Obtain a user delegation key for the purpose of signing SAS tokens.
        A token credential must be present on the service object for this request to succeed.

        :param ~datetime.datetime key_start_time:
            A DateTime value. Indicates when the key becomes valid.
        :param ~datetime.datetime key_expiry_time:
            A DateTime value. Indicates when the key stops being valid.
        :keyword int timeout:
            Sets the server-side timeout for the operation in seconds. For more details see
            https://learn.microsoft.com/rest/api/storageservices/setting-timeouts-for-blob-service-operations.
            This value is not tracked or validated on the client. To configure client-side network timesouts
            see `here <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob
            #other-client--per-operation-configuration>`_.
        :return: The user delegation key.
        :rtype: ~azure.storage.blob.UserDelegationKey
        """
    async def get_account_information(self, **kwargs: Any) -> Dict[str, str]:
        """Gets information related to the storage account.

        The information can also be retrieved if the user has a SAS to a container or blob.
        The keys in the returned dictionary include 'sku_name' and 'account_kind'.

        :returns: A dict of account information (SKU and account type).
        :rtype: dict(str, str)

        .. admonition:: Example:

            .. literalinclude:: ../samples/blob_samples_service_async.py
                :start-after: [START get_blob_service_account_info]
                :end-before: [END get_blob_service_account_info]
                :language: python
                :dedent: 12
                :caption: Getting account information for the blob service.
        """
    async def get_service_stats(self, **kwargs: Any) -> Dict[str, Any]:
        """Retrieves statistics related to replication for the Blob service.

        It is only available when read-access geo-redundant replication is enabled for
        the storage account.

        With geo-redundant replication, Azure Storage maintains your data durable
        in two locations. In both locations, Azure Storage constantly maintains
        multiple healthy replicas of your data. The location where you read,
        create, update, or delete data is the primary storage account location.
        The primary location exists in the region you choose at the time you
        create an account via the Azure Management Azure classic portal, for
        example, North Central US. The location to which your data is replicated
        is the secondary location. The secondary location is automatically
        determined based on the location of the primary; it is in a second data
        center that resides in the same region as the primary location. Read-only
        access is available from the secondary location, if read-access geo-redundant
        replication is enabled for your storage account.

        :keyword int timeout:
            Sets the server-side timeout for the operation in seconds. For more details see
            https://learn.microsoft.com/rest/api/storageservices/setting-timeouts-for-blob-service-operations.
            This value is not tracked or validated on the client. To configure client-side network timesouts
            see `here <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob
            #other-client--per-operation-configuration>`_.
        :return: The blob service stats.
        :rtype: Dict[str, Any]

        .. admonition:: Example:

            .. literalinclude:: ../samples/blob_samples_service_async.py
                :start-after: [START get_blob_service_stats]
                :end-before: [END get_blob_service_stats]
                :language: python
                :dedent: 12
                :caption: Getting service stats for the blob service.
        """
    async def get_service_properties(self, **kwargs: Any) -> Dict[str, Any]:
        """Gets the properties of a storage account's Blob service, including
        Azure Storage Analytics.

        :keyword int timeout:
            Sets the server-side timeout for the operation in seconds. For more details see
            https://learn.microsoft.com/rest/api/storageservices/setting-timeouts-for-blob-service-operations.
            This value is not tracked or validated on the client. To configure client-side network timesouts
            see `here <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob
            #other-client--per-operation-configuration>`_.
        :returns: An object containing blob service properties such as
            analytics logging, hour/minute metrics, cors rules, etc.
        :rtype: Dict[str, Any]

        .. admonition:: Example:

            .. literalinclude:: ../samples/blob_samples_service_async.py
                :start-after: [START get_blob_service_properties]
                :end-before: [END get_blob_service_properties]
                :language: python
                :dedent: 12
                :caption: Getting service properties for the blob service.
        """
    async def set_service_properties(self, analytics_logging: BlobAnalyticsLogging | None = None, hour_metrics: Metrics | None = None, minute_metrics: Metrics | None = None, cors: List[CorsRule] | None = None, target_version: str | None = None, delete_retention_policy: RetentionPolicy | None = None, static_website: StaticWebsite | None = None, **kwargs) -> None:
        """Sets the properties of a storage account's Blob service, including
        Azure Storage Analytics.

        If an element (e.g. analytics_logging) is left as None, the
        existing settings on the service for that functionality are preserved.

        :param analytics_logging:
            Groups the Azure Analytics Logging settings.
        :type analytics_logging: ~azure.storage.blob.BlobAnalyticsLogging
        :param hour_metrics:
            The hour metrics settings provide a summary of request
            statistics grouped by API in hourly aggregates for blobs.
        :type hour_metrics: ~azure.storage.blob.Metrics
        :param minute_metrics:
            The minute metrics settings provide request statistics
            for each minute for blobs.
        :type minute_metrics: ~azure.storage.blob.Metrics
        :param cors:
            You can include up to five CorsRule elements in the
            list. If an empty list is specified, all CORS rules will be deleted,
            and CORS will be disabled for the service.
        :type cors: list[~azure.storage.blob.CorsRule]
        :param str target_version:
            Indicates the default version to use for requests if an incoming
            request's version is not specified.
        :param delete_retention_policy:
            The delete retention policy specifies whether to retain deleted blobs.
            It also specifies the number of days and versions of blob to keep.
        :type delete_retention_policy: ~azure.storage.blob.RetentionPolicy
        :param static_website:
            Specifies whether the static website feature is enabled,
            and if yes, indicates the index document and 404 error document to use.
        :type static_website: ~azure.storage.blob.StaticWebsite
        :keyword int timeout:
            Sets the server-side timeout for the operation in seconds. For more details see
            https://learn.microsoft.com/rest/api/storageservices/setting-timeouts-for-blob-service-operations.
            This value is not tracked or validated on the client. To configure client-side network timesouts
            see `here <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob
            #other-client--per-operation-configuration>`_.
        :rtype: None

        .. admonition:: Example:

            .. literalinclude:: ../samples/blob_samples_service_async.py
                :start-after: [START set_blob_service_properties]
                :end-before: [END set_blob_service_properties]
                :language: python
                :dedent: 12
                :caption: Setting service properties for the blob service.
        """
    def list_containers(self, name_starts_with: str | None = None, include_metadata: bool | None = False, **kwargs) -> AsyncItemPaged[ContainerProperties]:
        """Returns a generator to list the containers under the specified account.

        The generator will lazily follow the continuation tokens returned by
        the service and stop when all containers have been returned.

        :param str name_starts_with:
            Filters the results to return only containers whose names
            begin with the specified prefix.
        :param bool include_metadata:
            Specifies that container metadata to be returned in the response.
            The default value is `False`.
        :keyword bool include_deleted:
            Specifies that deleted containers to be returned in the response. This is for container restore enabled
            account. The default value is `False`.
            .. versionadded:: 12.4.0
        :keyword bool include_system:
            Flag specifying that system containers should be included.
            .. versionadded:: 12.10.0
        :keyword int results_per_page:
            The maximum number of container names to retrieve per API
            call. If the request does not specify the server will return up to 5,000 items.
        :keyword int timeout:
            Sets the server-side timeout for the operation in seconds. For more details see
            https://learn.microsoft.com/rest/api/storageservices/setting-timeouts-for-blob-service-operations.
            This value is not tracked or validated on the client. To configure client-side network timesouts
            see `here <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob
            #other-client--per-operation-configuration>`_.
        :returns: An iterable (auto-paging) of ContainerProperties.
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.storage.blob.ContainerProperties]

        .. admonition:: Example:

            .. literalinclude:: ../samples/blob_samples_service_async.py
                :start-after: [START bsc_list_containers]
                :end-before: [END bsc_list_containers]
                :language: python
                :dedent: 16
                :caption: Listing the containers in the blob service.
        """
    def find_blobs_by_tags(self, filter_expression: str, **kwargs: Any) -> AsyncItemPaged[FilteredBlob]:
        '''The Filter Blobs operation enables callers to list blobs across all
        containers whose tags match a given search expression.  Filter blobs
        searches across all containers within a storage account but can be
        scoped within the expression to a single container.

        :param str filter_expression:
            The expression to find blobs whose tags matches the specified condition.
            eg. ""yourtagname"=\'firsttag\' and "yourtagname2"=\'secondtag\'"
            To specify a container, eg. "@container=\'containerName\' and "Name"=\'C\'"
        :keyword int results_per_page:
            The max result per page when paginating.
        :keyword int timeout:
            Sets the server-side timeout for the operation in seconds. For more details see
            https://learn.microsoft.com/rest/api/storageservices/setting-timeouts-for-blob-service-operations.
            This value is not tracked or validated on the client. To configure client-side network timesouts
            see `here <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob
            #other-client--per-operation-configuration>`_.
        :returns: An iterable (auto-paging) response of BlobProperties.
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.storage.blob.FilteredBlob]
        '''
    async def create_container(self, name: str, metadata: Dict[str, str] | None = None, public_access: PublicAccess | str | None = None, **kwargs) -> ContainerClient:
        """Creates a new container under the specified account.

        If the container with the same name already exists, a ResourceExistsError will
        be raised. This method returns a client with which to interact with the newly
        created container.

        :param str name: The name of the container to create.
        :param metadata:
            A dict with name-value pairs to associate with the
            container as metadata. Example: `{'Category':'test'}`
        :type metadata: dict(str, str)
        :param public_access:
            Possible values include: 'container', 'blob'.
        :type public_access: str or ~azure.storage.blob.PublicAccess
        :keyword container_encryption_scope:
            Specifies the default encryption scope to set on the container and use for
            all future writes.

            .. versionadded:: 12.2.0

        :paramtype container_encryption_scope: dict or ~azure.storage.blob.ContainerEncryptionScope
        :keyword int timeout:
            Sets the server-side timeout for the operation in seconds. For more details see
            https://learn.microsoft.com/rest/api/storageservices/setting-timeouts-for-blob-service-operations.
            This value is not tracked or validated on the client. To configure client-side network timesouts
            see `here <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob
            #other-client--per-operation-configuration>`_.
        :rtype: ~azure.storage.blob.aio.ContainerClient

        .. admonition:: Example:

            .. literalinclude:: ../samples/blob_samples_service_async.py
                :start-after: [START bsc_create_container]
                :end-before: [END bsc_create_container]
                :language: python
                :dedent: 16
                :caption: Creating a container in the blob service.
        """
    async def delete_container(self, container: ContainerProperties | str, lease: BlobLeaseClient | str | None = None, **kwargs) -> None:
        """Marks the specified container for deletion.

        The container and any blobs contained within it are later deleted during garbage collection.
        If the container is not found, a ResourceNotFoundError will be raised.

        :param container:
            The container to delete. This can either be the name of the container,
            or an instance of ContainerProperties.
        :type container: str or ~azure.storage.blob.ContainerProperties
        :param lease:
            If specified, delete_container only succeeds if the
            container's lease is active and matches this ID.
            Required if the container has an active lease.
        :paramtype lease: ~azure.storage.blob.aio.BlobLeaseClient or str
        :keyword ~datetime.datetime if_modified_since:
            A DateTime value. Azure expects the date value passed in to be UTC.
            If timezone is included, any non-UTC datetimes will be converted to UTC.
            If a date is passed in without timezone info, it is assumed to be UTC.
            Specify this header to perform the operation only
            if the resource has been modified since the specified time.
        :keyword ~datetime.datetime if_unmodified_since:
            A DateTime value. Azure expects the date value passed in to be UTC.
            If timezone is included, any non-UTC datetimes will be converted to UTC.
            If a date is passed in without timezone info, it is assumed to be UTC.
            Specify this header to perform the operation only if
            the resource has not been modified since the specified date/time.
        :keyword str etag:
            An ETag value, or the wildcard character (*). Used to check if the resource has changed,
            and act according to the condition specified by the `match_condition` parameter.
        :keyword ~azure.core.MatchConditions match_condition:
            The match condition to use upon the etag.
        :keyword int timeout:
            Sets the server-side timeout for the operation in seconds. For more details see
            https://learn.microsoft.com/rest/api/storageservices/setting-timeouts-for-blob-service-operations.
            This value is not tracked or validated on the client. To configure client-side network timesouts
            see `here <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob
            #other-client--per-operation-configuration>`_.
        :rtype: None

        .. admonition:: Example:

            .. literalinclude:: ../samples/blob_samples_service_async.py
                :start-after: [START bsc_delete_container]
                :end-before: [END bsc_delete_container]
                :language: python
                :dedent: 16
                :caption: Deleting a container in the blob service.
        """
    async def undelete_container(self, deleted_container_name: str, deleted_container_version: str, **kwargs: Any) -> ContainerClient:
        """Restores soft-deleted container.

        Operation will only be successful if used within the specified number of days
        set in the delete retention policy.

        .. versionadded:: 12.4.0
            This operation was introduced in API version '2019-12-12'.

        :param str deleted_container_name:
            Specifies the name of the deleted container to restore.
        :param str deleted_container_version:
            Specifies the version of the deleted container to restore.
        :keyword int timeout:
            Sets the server-side timeout for the operation in seconds. For more details see
            https://learn.microsoft.com/rest/api/storageservices/setting-timeouts-for-blob-service-operations.
            This value is not tracked or validated on the client. To configure client-side network timesouts
            see `here <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob
            #other-client--per-operation-configuration>`_.
        :returns: The recovered soft-deleted ContainerClient.
        :rtype: ~azure.storage.blob.aio.ContainerClient
        """
    def get_container_client(self, container: ContainerProperties | str) -> ContainerClient:
        """Get a client to interact with the specified container.

        The container need not already exist.

        :param container:
            The container. This can either be the name of the container,
            or an instance of ContainerProperties.
        :type container: str or ~azure.storage.blob.ContainerProperties
        :returns: A ContainerClient.
        :rtype: ~azure.storage.blob.aio.ContainerClient

        .. admonition:: Example:

            .. literalinclude:: ../samples/blob_samples_service_async.py
                :start-after: [START bsc_get_container_client]
                :end-before: [END bsc_get_container_client]
                :language: python
                :dedent: 12
                :caption: Getting the container client to interact with a specific container.
        """
    def get_blob_client(self, container: ContainerProperties | str, blob: BlobProperties | str, snapshot: Dict[str, Any] | str | None = None, *, version_id: str | None = None) -> BlobClient:
        """Get a client to interact with the specified blob.

        The blob need not already exist.

        :param container:
            The container that the blob is in. This can either be the name of the container,
            or an instance of ContainerProperties.
        :type container: str or ~azure.storage.blob.ContainerProperties
        :param blob:
            The blob with which to interact. This can either be the name of the blob,
            or an instance of BlobProperties.
        :type blob: str or ~azure.storage.blob.BlobProperties
        :param snapshot:
            The optional blob snapshot on which to operate. This can either be the ID of the snapshot,
            or a dictionary output returned by
            :func:`~azure.storage.blob.aio.BlobClient.create_snapshot()`.
        :type snapshot: str or dict(str, Any)
        :keyword str version_id: The version id parameter is an opaque DateTime value that, when present,
            specifies the version of the blob to operate on.
        :returns: A BlobClient.
        :rtype: ~azure.storage.blob.aio.BlobClient

        .. admonition:: Example:

            .. literalinclude:: ../samples/blob_samples_service_async.py
                :start-after: [START bsc_get_blob_client]
                :end-before: [END bsc_get_blob_client]
                :language: python
                :dedent: 16
                :caption: Getting the blob client to interact with a specific blob.
        """
