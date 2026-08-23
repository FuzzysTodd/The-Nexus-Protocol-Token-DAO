from ._deserialize import deserialize_blob_properties as deserialize_blob_properties, deserialize_blob_stream as deserialize_blob_stream, deserialize_pipeline_response_into_cls as deserialize_pipeline_response_into_cls, get_page_ranges_result as get_page_ranges_result, parse_tags as parse_tags
from ._download import StorageStreamDownloader as StorageStreamDownloader
from ._encryption import StorageEncryptionMixin as StorageEncryptionMixin, modify_user_agent_for_encryption as modify_user_agent_for_encryption
from ._generated import AzureBlobStorage as AzureBlobStorage
from ._generated.models import AppendPositionAccessConditions as AppendPositionAccessConditions, BlobHTTPHeaders as BlobHTTPHeaders, BlockList as BlockList, BlockLookupList as BlockLookupList, CpkInfo as CpkInfo, DeleteSnapshotsOptionType as DeleteSnapshotsOptionType, QueryRequest as QueryRequest, SequenceNumberAccessConditions as SequenceNumberAccessConditions
from ._lease import BlobLeaseClient as BlobLeaseClient
from ._models import BlobBlock as BlobBlock, BlobProperties as BlobProperties, BlobQueryError as BlobQueryError, BlobType as BlobType, ContentSettings as ContentSettings, DelimitedJsonDialect as DelimitedJsonDialect, DelimitedTextDialect as DelimitedTextDialect, ImmutabilityPolicy as ImmutabilityPolicy, PageRange as PageRange, PageRangePaged as PageRangePaged, PremiumPageBlobTier as PremiumPageBlobTier, QuickQueryDialect as QuickQueryDialect, SequenceNumberAction as SequenceNumberAction, StandardBlobTier as StandardBlobTier
from ._quick_query_helper import BlobQueryReader as BlobQueryReader
from ._serialize import get_access_conditions as get_access_conditions, get_api_version as get_api_version, get_cpk_scope_info as get_cpk_scope_info, get_modify_conditions as get_modify_conditions, get_source_conditions as get_source_conditions, get_version_id as get_version_id, serialize_blob_tags as serialize_blob_tags, serialize_blob_tags_header as serialize_blob_tags_header, serialize_query_format as serialize_query_format
from ._shared import encode_base64 as encode_base64
from ._shared.base_client import StorageAccountHostsMixin as StorageAccountHostsMixin, TransportWrapper as TransportWrapper, parse_connection_str as parse_connection_str, parse_query as parse_query
from ._shared.request_handlers import add_metadata_headers as add_metadata_headers, get_length as get_length, read_length as read_length, validate_and_format_range_headers as validate_and_format_range_headers
from ._shared.response_handlers import process_storage_error as process_storage_error, return_headers_and_deserialized as return_headers_and_deserialized, return_response_headers as return_response_headers
from ._shared.uploads import IterStreamer as IterStreamer
from ._shared.uploads_async import AsyncIterStreamer as AsyncIterStreamer
from ._upload_helpers import upload_append_blob as upload_append_blob, upload_block_blob as upload_block_blob, upload_page_blob as upload_page_blob
from _typeshed import Incomplete
from azure.core.credentials import AzureNamedKeyCredential as AzureNamedKeyCredential, AzureSasCredential as AzureSasCredential, TokenCredential as TokenCredential
from azure.core.paging import ItemPaged
from datetime import datetime
from typing import Any, AnyStr, Dict, IO, Iterable, List, Tuple, overload
from typing_extensions import Self

class BlobClient(StorageAccountHostsMixin, StorageEncryptionMixin):
    '''A client to interact with a specific blob, although that blob may not yet exist.

    For more optional configuration, please click
    `here <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob
    #optional-configuration>`_.

    :param str account_url:
        The URI to the storage account. In order to create a client given the full URI to the blob,
        use the :func:`from_blob_url` classmethod.
    :param container_name: The container name for the blob.
    :type container_name: str
    :param blob_name: The name of the blob with which to interact. If specified, this value will override
        a blob value specified in the blob URL.
    :type blob_name: str
    :param str snapshot:
        The optional blob snapshot on which to operate. This can be the snapshot ID string
        or the response returned from :func:`create_snapshot`.
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
    :keyword str version_id: The version id parameter is an opaque DateTime value that, when present,
        specifies the version of the blob to operate on.

    .. admonition:: Example:

        .. literalinclude:: ../samples/blob_samples_authentication.py
            :start-after: [START create_blob_client]
            :end-before: [END create_blob_client]
            :language: python
            :dedent: 8
            :caption: Creating the BlobClient from a URL to a public blob (no auth needed).

        .. literalinclude:: ../samples/blob_samples_authentication.py
            :start-after: [START create_blob_client_sas_url]
            :end-before: [END create_blob_client_sas_url]
            :language: python
            :dedent: 8
            :caption: Creating the BlobClient from a SAS URL to a blob.
    '''
    container_name: Incomplete
    blob_name: Incomplete
    snapshot: Incomplete
    version_id: Incomplete
    def __init__(self, account_url: str, container_name: str, blob_name: str, snapshot: str | Dict[str, Any] | None = None, credential: str | Dict[str, str] | AzureNamedKeyCredential | AzureSasCredential | TokenCredential | None = None, **kwargs: Any) -> None: ...
    @classmethod
    def from_blob_url(cls, blob_url: str, credential: str | Dict[str, str] | AzureNamedKeyCredential | AzureSasCredential | TokenCredential | None = None, snapshot: str | Dict[str, Any] | None = None, **kwargs: Any) -> Self:
        '''Create BlobClient from a blob url. This doesn\'t support customized blob url with \'/\' in blob name.

        :param str blob_url:
            The full endpoint URL to the Blob, including SAS token and snapshot if used. This could be
            either the primary endpoint, or the secondary endpoint depending on the current `location_mode`.
        :type blob_url: str
        :param credential:
            The credentials with which to authenticate. This is optional if the
            account URL already has a SAS token, or the connection string already has shared
            access key values. The value can be a SAS token string,
            an instance of a AzureSasCredential or AzureNamedKeyCredential from azure.core.credentials,
            an account shared access key, or an instance of a TokenCredentials class from azure.identity.
            If the resource URI already contains a SAS token, this will be ignored in favor of an explicit credential
            - except in the case of AzureSasCredential, where the conflicting SAS tokens will raise a ValueError.
            If using an instance of AzureNamedKeyCredential, "name" should be the storage account name, and "key"
            should be the storage account key.
        :type credential: Optional[Union[str, Dict[str, str], "AzureNamedKeyCredential", "AzureSasCredential", "TokenCredential"]]  # pylint: disable=line-too-long
        :param str snapshot:
            The optional blob snapshot on which to operate. This can be the snapshot ID string
            or the response returned from :func:`create_snapshot`. If specified, this will override
            the snapshot in the url.
        :keyword str version_id: The version id parameter is an opaque DateTime value that, when present,
            specifies the version of the blob to operate on.
        :returns: A Blob client.
        :rtype: ~azure.storage.blob.BlobClient
        '''
    @classmethod
    def from_connection_string(cls, conn_str: str, container_name: str, blob_name: str, snapshot: str | Dict[str, Any] | None = None, credential: str | Dict[str, str] | AzureNamedKeyCredential | AzureSasCredential | TokenCredential | None = None, **kwargs: Any) -> Self:
        '''Create BlobClient from a Connection String.

        :param str conn_str:
            A connection string to an Azure Storage account.
        :param container_name: The container name for the blob.
        :type container_name: str
        :param blob_name: The name of the blob with which to interact.
        :type blob_name: str
        :param str snapshot:
            The optional blob snapshot on which to operate. This can be the snapshot ID string
            or the response returned from :func:`create_snapshot`.
        :param credential:
            The credentials with which to authenticate. This is optional if the
            account URL already has a SAS token, or the connection string already has shared
            access key values. The value can be a SAS token string,
            an instance of a AzureSasCredential or AzureNamedKeyCredential from azure.core.credentials,
            an account shared access key, or an instance of a TokenCredentials class from azure.identity.
            Credentials provided here will take precedence over those in the connection string.
            If using an instance of AzureNamedKeyCredential, "name" should be the storage account name, and "key"
            should be the storage account key.
        :type credential: Optional[Union[str, Dict[str, str], "AzureNamedKeyCredential", "AzureSasCredential", "TokenCredential"]]  # pylint: disable=line-too-long
        :keyword str version_id: The version id parameter is an opaque DateTime value that, when present,
            specifies the version of the blob to operate on.
        :returns: A Blob client.
        :rtype: ~azure.storage.blob.BlobClient

        .. admonition:: Example:

            .. literalinclude:: ../samples/blob_samples_authentication.py
                :start-after: [START auth_from_connection_string_blob]
                :end-before: [END auth_from_connection_string_blob]
                :language: python
                :dedent: 8
                :caption: Creating the BlobClient from a connection string.
        '''
    def get_account_information(self, **kwargs: Any) -> Dict[str, str]:
        """Gets information related to the storage account in which the blob resides.

        The information can also be retrieved if the user has a SAS to a container or blob.
        The keys in the returned dictionary include 'sku_name' and 'account_kind'.

        :returns: A dict of account information (SKU and account type).
        :rtype: dict(str, str)
        """
    def upload_blob_from_url(self, source_url: str, **kwargs: Any) -> Dict[str, Any]:
        '''
        Creates a new Block Blob where the content of the blob is read from a given URL.
        The content of an existing blob is overwritten with the new blob.

        :param str source_url:
            A URL of up to 2 KB in length that specifies a file or blob.
            The value should be URL-encoded as it would appear in a request URI.
            If the source is in another account, the source must either be public
            or must be authenticated via a shared access signature. If the source
            is public, no authentication is required.
            Examples:
            https://myaccount.blob.core.windows.net/mycontainer/myblob

            https://myaccount.blob.core.windows.net/mycontainer/myblob?snapshot=<DateTime>

            https://otheraccount.blob.core.windows.net/mycontainer/myblob?sastoken
        :keyword bool overwrite: Whether the blob to be uploaded should overwrite the current data.
            If True, upload_blob will overwrite the existing data. If set to False, the
            operation will fail with ResourceExistsError.
        :keyword bool include_source_blob_properties:
            Indicates if properties from the source blob should be copied. Defaults to True.
        :keyword tags:
            Name-value pairs associated with the blob as tag. Tags are case-sensitive.
            The tag set may contain at most 10 tags.  Tag keys must be between 1 and 128 characters,
            and tag values must be between 0 and 256 characters.
            Valid tag key and value characters include: lowercase and uppercase letters, digits (0-9),
            space (` `), plus (+), minus (-), period (.), solidus (/), colon (:), equals (=), underscore (_)
        :paramtype tags: dict(str, str)
        :keyword bytearray source_content_md5:
            Specify the md5 that is used to verify the integrity of the source bytes.
        :keyword ~datetime.datetime source_if_modified_since:
            A DateTime value. Azure expects the date value passed in to be UTC.
            If timezone is included, any non-UTC datetimes will be converted to UTC.
            If a date is passed in without timezone info, it is assumed to be UTC.
            Specify this header to perform the operation only
            if the source resource has been modified since the specified time.
        :keyword ~datetime.datetime source_if_unmodified_since:
            A DateTime value. Azure expects the date value passed in to be UTC.
            If timezone is included, any non-UTC datetimes will be converted to UTC.
            If a date is passed in without timezone info, it is assumed to be UTC.
            Specify this header to perform the operation only if
            the source resource has not been modified since the specified date/time.
        :keyword str source_etag:
            The source ETag value, or the wildcard character (*). Used to check if the resource has changed,
            and act according to the condition specified by the `match_condition` parameter.
        :keyword ~azure.core.MatchConditions source_match_condition:
            The source match condition to use upon the etag.
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
            The destination ETag value, or the wildcard character (*). Used to check if the resource has changed,
            and act according to the condition specified by the `match_condition` parameter.
        :keyword ~azure.core.MatchConditions match_condition:
            The destination match condition to use upon the etag.
        :keyword destination_lease:
            The lease ID specified for this header must match the lease ID of the
            destination blob. If the request does not include the lease ID or it is not
            valid, the operation fails with status code 412 (Precondition Failed).
        :paramtype destination_lease: ~azure.storage.blob.BlobLeaseClient or str
        :keyword int timeout:
            Sets the server-side timeout for the operation in seconds. For more details see
            https://learn.microsoft.com/rest/api/storageservices/setting-timeouts-for-blob-service-operations.
            This value is not tracked or validated on the client. To configure client-side network timesouts
            see `here <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob
            #other-client--per-operation-configuration>`_.
        :keyword ~azure.storage.blob.ContentSettings content_settings:
            ContentSettings object used to set blob properties. Used to set content type, encoding,
            language, disposition, md5, and cache control.
        :keyword ~azure.storage.blob.CustomerProvidedEncryptionKey cpk:
            Encrypts the data on the service-side with the given key.
            Use of customer-provided keys must be done over HTTPS.
            As the encryption key itself is provided in the request,
            a secure connection must be established to transfer the key.
        :keyword str encryption_scope:
            A predefined encryption scope used to encrypt the data on the service. An encryption
            scope can be created using the Management API and referenced here by name. If a default
            encryption scope has been defined at the container, this value will override it if the
            container-level scope is configured to allow overrides. Otherwise an error will be raised.
        :keyword ~azure.storage.blob.StandardBlobTier standard_blob_tier:
            A standard blob tier value to set the blob to. For this version of the library,
            this is only applicable to block blobs on standard storage accounts.
        :keyword str source_authorization:
            Authenticate as a service principal using a client secret to access a source blob. Ensure "bearer " is
            the prefix of the source_authorization string.
        '''
    def upload_blob(self, data: bytes | str | Iterable[AnyStr] | IO[AnyStr], blob_type: str | BlobType = ..., length: int | None = None, metadata: Dict[str, str] | None = None, **kwargs) -> Dict[str, Any]:
        '''Creates a new blob from a data source with automatic chunking.

        :param data: The blob data to upload.
        :param ~azure.storage.blob.BlobType blob_type: The type of the blob. This can be
            either BlockBlob, PageBlob or AppendBlob. The default value is BlockBlob.
        :param int length:
            Number of bytes to read from the stream. This is optional, but
            should be supplied for optimal performance.
        :param metadata:
            Name-value pairs associated with the blob as metadata.
        :type metadata: dict(str, str)
        :keyword tags:
            Name-value pairs associated with the blob as tag. Tags are case-sensitive.
            The tag set may contain at most 10 tags.  Tag keys must be between 1 and 128 characters,
            and tag values must be between 0 and 256 characters.
            Valid tag key and value characters include: lowercase and uppercase letters, digits (0-9),
            space (` `), plus (+), minus (-), period (.), solidus (/), colon (:), equals (=), underscore (_)

            .. versionadded:: 12.4.0

        :paramtype tags: dict(str, str)
        :keyword bool overwrite: Whether the blob to be uploaded should overwrite the current data.
            If True, upload_blob will overwrite the existing data. If set to False, the
            operation will fail with ResourceExistsError. The exception to the above is with Append
            blob types: if set to False and the data already exists, an error will not be raised
            and the data will be appended to the existing blob. If set overwrite=True, then the existing
            append blob will be deleted, and a new one created. Defaults to False.
        :keyword ~azure.storage.blob.ContentSettings content_settings:
            ContentSettings object used to set blob properties. Used to set content type, encoding,
            language, disposition, md5, and cache control.
        :keyword bool validate_content:
            If true, calculates an MD5 hash for each chunk of the blob. The storage
            service checks the hash of the content that has arrived with the hash
            that was sent. This is primarily valuable for detecting bitflips on
            the wire if using http instead of https, as https (the default), will
            already validate. Note that this MD5 hash is not stored with the
            blob. Also note that if enabled, the memory-efficient upload algorithm
            will not be used because computing the MD5 hash requires buffering
            entire blocks, and doing so defeats the purpose of the memory-efficient algorithm.
        :keyword lease:
            Required if the blob has an active lease. If specified, upload_blob only succeeds if the
            blob\'s lease is active and matches this ID. Value can be a BlobLeaseClient object
            or the lease ID as a string.
        :paramtype lease: ~azure.storage.blob.BlobLeaseClient or str
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
        :keyword str if_tags_match_condition:
            Specify a SQL where clause on blob tags to operate only on blob with a matching value.
            eg. ``"\\"tagname\\"=\'my tag\'"``

            .. versionadded:: 12.4.0

        :keyword ~azure.storage.blob.PremiumPageBlobTier premium_page_blob_tier:
            A page blob tier value to set the blob to. The tier correlates to the size of the
            blob and number of allowed IOPS. This is only applicable to page blobs on
            premium storage accounts.
        :keyword ~azure.storage.blob.StandardBlobTier standard_blob_tier:
            A standard blob tier value to set the blob to. For this version of the library,
            this is only applicable to block blobs on standard storage accounts.
        :keyword ~azure.storage.blob.ImmutabilityPolicy immutability_policy:
            Specifies the immutability policy of a blob, blob snapshot or blob version.
            Currently this parameter of upload_blob() API is for BlockBlob only.

            .. versionadded:: 12.10.0
                This was introduced in API version \'2020-10-02\'.

        :keyword bool legal_hold:
            Specified if a legal hold should be set on the blob.
            Currently this parameter of upload_blob() API is for BlockBlob only.

            .. versionadded:: 12.10.0
                This was introduced in API version \'2020-10-02\'.

        :keyword int maxsize_condition:
            Optional conditional header. The max length in bytes permitted for
            the append blob. If the Append Block operation would cause the blob
            to exceed that limit or if the blob size is already greater than the
            value specified in this header, the request will fail with
            MaxBlobSizeConditionNotMet error (HTTP status code 412 - Precondition Failed).
        :keyword int max_concurrency:
            Maximum number of parallel connections to use when the blob size exceeds
            64MB.
        :keyword ~azure.storage.blob.CustomerProvidedEncryptionKey cpk:
            Encrypts the data on the service-side with the given key.
            Use of customer-provided keys must be done over HTTPS.
            As the encryption key itself is provided in the request,
            a secure connection must be established to transfer the key.
        :keyword str encryption_scope:
            A predefined encryption scope used to encrypt the data on the service. An encryption
            scope can be created using the Management API and referenced here by name. If a default
            encryption scope has been defined at the container, this value will override it if the
            container-level scope is configured to allow overrides. Otherwise an error will be raised.

            .. versionadded:: 12.2.0

        :keyword str encoding:
            Defaults to UTF-8.
        :keyword progress_hook:
            A callback to track the progress of a long running upload. The signature is
            function(current: int, total: Optional[int]) where current is the number of bytes transferred
            so far, and total is the size of the blob or None if the size is unknown.
        :paramtype progress_hook: Callable[[int, Optional[int]], None]
        :keyword int timeout:
            Sets the server-side timeout for the operation in seconds. For more details see
            https://learn.microsoft.com/rest/api/storageservices/setting-timeouts-for-blob-service-operations.
            This value is not tracked or validated on the client. To configure client-side network timesouts
            see `here <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob
            #other-client--per-operation-configuration>`_. This method may make multiple calls to the service and
            the timeout will apply to each call individually.
        :returns: Blob-updated property dict (Etag and last modified)
        :rtype: dict[str, Any]

        .. admonition:: Example:

            .. literalinclude:: ../samples/blob_samples_hello_world.py
                :start-after: [START upload_a_blob]
                :end-before: [END upload_a_blob]
                :language: python
                :dedent: 12
                :caption: Upload a blob to the container.
        '''
    @overload
    def download_blob(self, offset: int = None, length: int = None, *, encoding: str, **kwargs) -> StorageStreamDownloader[str]: ...
    @overload
    def download_blob(self, offset: int = None, length: int = None, *, encoding: None = None, **kwargs) -> StorageStreamDownloader[bytes]: ...
    def query_blob(self, query_expression: str, **kwargs: Any) -> BlobQueryReader:
        '''Enables users to select/project on blob/or blob snapshot data by providing simple query expressions.
        This operations returns a BlobQueryReader, users need to use readall() or readinto() to get query data.

        :param str query_expression:
            Required. a query statement. For more details see
            https://learn.microsoft.com/azure/storage/blobs/query-acceleration-sql-reference.
        :keyword Callable[~azure.storage.blob.BlobQueryError] on_error:
            A function to be called on any processing errors returned by the service.
        :keyword blob_format:
            Optional. Defines the serialization of the data currently stored in the blob. The default is to
            treat the blob data as CSV data formatted in the default dialect. This can be overridden with
            a custom DelimitedTextDialect, or DelimitedJsonDialect or "ParquetDialect" (passed as a string or enum).
            These dialects can be passed through their respective classes, the QuickQueryDialect enum or as a string
        :paramtype blob_format: ~azure.storage.blob.DelimitedTextDialect or ~azure.storage.blob.DelimitedJsonDialect
            or ~azure.storage.blob.QuickQueryDialect or str
        :keyword output_format:
            Optional. Defines the output serialization for the data stream. By default the data will be returned
            as it is represented in the blob (Parquet formats default to DelimitedTextDialect).
            By providing an output format, the blob data will be reformatted according to that profile.
            This value can be a DelimitedTextDialect or a DelimitedJsonDialect or ArrowDialect.
            These dialects can be passed through their respective classes, the QuickQueryDialect enum or as a string
        :paramtype output_format: ~azure.storage.blob.DelimitedTextDialect or ~azure.storage.blob.DelimitedJsonDialect
            or list[~azure.storage.blob.ArrowDialect] or ~azure.storage.blob.QuickQueryDialect or str
        :keyword lease:
            Required if the blob has an active lease. Value can be a BlobLeaseClient object
            or the lease ID as a string.
        :paramtype lease: ~azure.storage.blob.BlobLeaseClient or str
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
        :keyword str if_tags_match_condition:
            Specify a SQL where clause on blob tags to operate only on blob with a matching value.
            eg. ``"\\"tagname\\"=\'my tag\'"``

            .. versionadded:: 12.4.0

        :keyword ~azure.storage.blob.CustomerProvidedEncryptionKey cpk:
            Encrypts the data on the service-side with the given key.
            Use of customer-provided keys must be done over HTTPS.
            As the encryption key itself is provided in the request,
            a secure connection must be established to transfer the key.
        :keyword int timeout:
            Sets the server-side timeout for the operation in seconds. For more details see
            https://learn.microsoft.com/rest/api/storageservices/setting-timeouts-for-blob-service-operations.
            This value is not tracked or validated on the client. To configure client-side network timesouts
            see `here <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob
            #other-client--per-operation-configuration>`_.
        :returns: A streaming object (BlobQueryReader)
        :rtype: ~azure.storage.blob.BlobQueryReader

        .. admonition:: Example:

            .. literalinclude:: ../samples/blob_samples_query.py
                :start-after: [START query]
                :end-before: [END query]
                :language: python
                :dedent: 4
                :caption: select/project on blob/or blob snapshot data by providing simple query expressions.
        '''
    def delete_blob(self, delete_snapshots: str = None, **kwargs: Any) -> None:
        '''Marks the specified blob for deletion.

        The blob is later deleted during garbage collection.
        Note that in order to delete a blob, you must delete all of its
        snapshots. You can delete both at the same time with the delete_blob()
        operation.

        If a delete retention policy is enabled for the service, then this operation soft deletes the blob
        and retains the blob for a specified number of days.
        After the specified number of days, the blob\'s data is removed from the service during garbage collection.
        Soft deleted blob is accessible through :func:`~ContainerClient.list_blobs()` specifying `include=[\'deleted\']`
        option. Soft-deleted blob can be restored using :func:`undelete` operation.

        :param str delete_snapshots:
            Required if the blob has associated snapshots. Values include:
             - "only": Deletes only the blobs snapshots.
             - "include": Deletes the blob along with all snapshots.
        :keyword str version_id:
            The version id parameter is an opaque DateTime
            value that, when present, specifies the version of the blob to delete.

            .. versionadded:: 12.4.0
            This keyword argument was introduced in API version \'2019-12-12\'.

        :keyword lease:
            Required if the blob has an active lease. If specified, delete_blob only
            succeeds if the blob\'s lease is active and matches this ID. Value can be a
            BlobLeaseClient object or the lease ID as a string.
        :paramtype lease: ~azure.storage.blob.BlobLeaseClient or str
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
        :keyword str if_tags_match_condition:
            Specify a SQL where clause on blob tags to operate only on blob with a matching value.
            eg. ``"\\"tagname\\"=\'my tag\'"``

            .. versionadded:: 12.4.0

        :keyword int timeout:
            Sets the server-side timeout for the operation in seconds. For more details see
            https://learn.microsoft.com/rest/api/storageservices/setting-timeouts-for-blob-service-operations.
            This value is not tracked or validated on the client. To configure client-side network timesouts
            see `here <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob
            #other-client--per-operation-configuration>`_.
        :rtype: None

        .. admonition:: Example:

            .. literalinclude:: ../samples/blob_samples_hello_world.py
                :start-after: [START delete_blob]
                :end-before: [END delete_blob]
                :language: python
                :dedent: 12
                :caption: Delete a blob.
        '''
    def undelete_blob(self, **kwargs: Any) -> None:
        """Restores soft-deleted blobs or snapshots.

        Operation will only be successful if used within the specified number of days
        set in the delete retention policy.

        If blob versioning is enabled, the base blob cannot be restored using this
        method. Instead use :func:`start_copy_from_url` with the URL of the blob version
        you wish to promote to the current version.

        :keyword int timeout:
            Sets the server-side timeout for the operation in seconds. For more details see
            https://learn.microsoft.com/rest/api/storageservices/setting-timeouts-for-blob-service-operations.
            This value is not tracked or validated on the client. To configure client-side network timesouts
            see `here <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob
            #other-client--per-operation-configuration>`_.
        :rtype: None

        .. admonition:: Example:

            .. literalinclude:: ../samples/blob_samples_common.py
                :start-after: [START undelete_blob]
                :end-before: [END undelete_blob]
                :language: python
                :dedent: 8
                :caption: Undeleting a blob.
        """
    def exists(self, **kwargs: Any) -> bool:
        """
        Returns True if a blob exists with the defined parameters, and returns
        False otherwise.

        :keyword str version_id:
            The version id parameter is an opaque DateTime
            value that, when present, specifies the version of the blob to check if it exists.
        :keyword int timeout:
            Sets the server-side timeout for the operation in seconds. For more details see
            https://learn.microsoft.com/rest/api/storageservices/setting-timeouts-for-blob-service-operations.
            This value is not tracked or validated on the client. To configure client-side network timesouts
            see `here <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob
            #other-client--per-operation-configuration>`_.
        :returns: boolean
        :rtype: bool
        """
    def get_blob_properties(self, **kwargs: Any) -> BlobProperties:
        '''Returns all user-defined metadata, standard HTTP properties, and
        system properties for the blob. It does not return the content of the blob.

        :keyword lease:
            Required if the blob has an active lease. Value can be a BlobLeaseClient object
            or the lease ID as a string.
        :paramtype lease: ~azure.storage.blob.BlobLeaseClient or str
        :keyword str version_id:
            The version id parameter is an opaque DateTime
            value that, when present, specifies the version of the blob to get properties.

            .. versionadded:: 12.4.0
            This keyword argument was introduced in API version \'2019-12-12\'.

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
        :keyword str if_tags_match_condition:
            Specify a SQL where clause on blob tags to operate only on blob with a matching value.
            eg. ``"\\"tagname\\"=\'my tag\'"``

            .. versionadded:: 12.4.0

        :keyword ~azure.storage.blob.CustomerProvidedEncryptionKey cpk:
            Encrypts the data on the service-side with the given key.
            Use of customer-provided keys must be done over HTTPS.
            As the encryption key itself is provided in the request,
            a secure connection must be established to transfer the key.
        :keyword int timeout:
            Sets the server-side timeout for the operation in seconds. For more details see
            https://learn.microsoft.com/rest/api/storageservices/setting-timeouts-for-blob-service-operations.
            This value is not tracked or validated on the client. To configure client-side network timesouts
            see `here <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob
            #other-client--per-operation-configuration>`_.
        :returns: BlobProperties
        :rtype: ~azure.storage.blob.BlobProperties

        .. admonition:: Example:

            .. literalinclude:: ../samples/blob_samples_common.py
                :start-after: [START get_blob_properties]
                :end-before: [END get_blob_properties]
                :language: python
                :dedent: 8
                :caption: Getting the properties for a blob.
        '''
    def set_http_headers(self, content_settings: ContentSettings | None = None, **kwargs: Any) -> None:
        '''Sets system properties on the blob.

        If one property is set for the content_settings, all properties will be overridden.

        :param ~azure.storage.blob.ContentSettings content_settings:
            ContentSettings object used to set blob properties. Used to set content type, encoding,
            language, disposition, md5, and cache control.
        :keyword lease:
            Required if the blob has an active lease. Value can be a BlobLeaseClient object
            or the lease ID as a string.
        :paramtype lease: ~azure.storage.blob.BlobLeaseClient or str
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
        :keyword str if_tags_match_condition:
            Specify a SQL where clause on blob tags to operate only on blob with a matching value.
            eg. ``"\\"tagname\\"=\'my tag\'"``

            .. versionadded:: 12.4.0

        :keyword int timeout:
            Sets the server-side timeout for the operation in seconds. For more details see
            https://learn.microsoft.com/rest/api/storageservices/setting-timeouts-for-blob-service-operations.
            This value is not tracked or validated on the client. To configure client-side network timesouts
            see `here <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob
            #other-client--per-operation-configuration>`_.
        :returns: Blob-updated property dict (Etag and last modified)
        :rtype: Dict[str, Any]
        '''
    def set_blob_metadata(self, metadata: Dict[str, str] | None = None, **kwargs: Any) -> Dict[str, str | datetime]:
        '''Sets user-defined metadata for the blob as one or more name-value pairs.

        :param metadata:
            Dict containing name and value pairs. Each call to this operation
            replaces all existing metadata attached to the blob. To remove all
            metadata from the blob, call this operation with no metadata headers.
        :type metadata: dict(str, str)
        :keyword lease:
            Required if the blob has an active lease. Value can be a BlobLeaseClient object
            or the lease ID as a string.
        :paramtype lease: ~azure.storage.blob.BlobLeaseClient or str
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
        :keyword str if_tags_match_condition:
            Specify a SQL where clause on blob tags to operate only on blob with a matching value.
            eg. ``"\\"tagname\\"=\'my tag\'"``

            .. versionadded:: 12.4.0

        :keyword ~azure.storage.blob.CustomerProvidedEncryptionKey cpk:
            Encrypts the data on the service-side with the given key.
            Use of customer-provided keys must be done over HTTPS.
            As the encryption key itself is provided in the request,
            a secure connection must be established to transfer the key.
        :keyword str encryption_scope:
            A predefined encryption scope used to encrypt the data on the service. An encryption
            scope can be created using the Management API and referenced here by name. If a default
            encryption scope has been defined at the container, this value will override it if the
            container-level scope is configured to allow overrides. Otherwise an error will be raised.

            .. versionadded:: 12.2.0

        :keyword int timeout:
            Sets the server-side timeout for the operation in seconds. For more details see
            https://learn.microsoft.com/rest/api/storageservices/setting-timeouts-for-blob-service-operations.
            This value is not tracked or validated on the client. To configure client-side network timesouts
            see `here <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob
            #other-client--per-operation-configuration>`_.
        :returns: Blob-updated property dict (Etag and last modified)
        '''
    def set_immutability_policy(self, immutability_policy: ImmutabilityPolicy, **kwargs: Any) -> Dict[str, str]:
        """The Set Immutability Policy operation sets the immutability policy on the blob.

        .. versionadded:: 12.10.0
            This operation was introduced in API version '2020-10-02'.

        :param ~azure.storage.blob.ImmutabilityPolicy immutability_policy:
            Specifies the immutability policy of a blob, blob snapshot or blob version.

            .. versionadded:: 12.10.0
                This was introduced in API version '2020-10-02'.

        :keyword int timeout:
            Sets the server-side timeout for the operation in seconds. For more details see
            https://learn.microsoft.com/rest/api/storageservices/setting-timeouts-for-blob-service-operations.
            This value is not tracked or validated on the client. To configure client-side network timesouts
            see `here <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob
            #other-client--per-operation-configuration>`_.
        :returns: Key value pairs of blob tags.
        :rtype: Dict[str, str]
        """
    def delete_immutability_policy(self, **kwargs: Any) -> None:
        """The Delete Immutability Policy operation deletes the immutability policy on the blob.

        .. versionadded:: 12.10.0
            This operation was introduced in API version '2020-10-02'.

        :keyword int timeout:
            Sets the server-side timeout for the operation in seconds. For more details see
            https://learn.microsoft.com/rest/api/storageservices/setting-timeouts-for-blob-service-operations.
            This value is not tracked or validated on the client. To configure client-side network timesouts
            see `here <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob
            #other-client--per-operation-configuration>`_.
        :returns: Key value pairs of blob tags.
        :rtype: Dict[str, str]
        """
    def set_legal_hold(self, legal_hold: bool, **kwargs: Any) -> Dict[str, str | datetime | bool]:
        """The Set Legal Hold operation sets a legal hold on the blob.

        .. versionadded:: 12.10.0
            This operation was introduced in API version '2020-10-02'.

        :param bool legal_hold:
            Specified if a legal hold should be set on the blob.
        :keyword int timeout:
            Sets the server-side timeout for the operation in seconds. For more details see
            https://learn.microsoft.com/rest/api/storageservices/setting-timeouts-for-blob-service-operations.
            This value is not tracked or validated on the client. To configure client-side network timesouts
            see `here <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob
            #other-client--per-operation-configuration>`_.
        :returns: Key value pairs of blob tags.
        :rtype: Dict[str, Union[str, datetime, bool]]
        """
    def create_page_blob(self, size: int, content_settings: ContentSettings | None = None, metadata: Dict[str, str] | None = None, premium_page_blob_tier: str | PremiumPageBlobTier | None = None, **kwargs) -> Dict[str, str | datetime]:
        """Creates a new Page Blob of the specified size.

        :param int size:
            This specifies the maximum size for the page blob, up to 1 TB.
            The page blob size must be aligned to a 512-byte boundary.
        :param ~azure.storage.blob.ContentSettings content_settings:
            ContentSettings object used to set blob properties. Used to set content type, encoding,
            language, disposition, md5, and cache control.
        :param metadata:
            Name-value pairs associated with the blob as metadata.
        :type metadata: dict(str, str)
        :param ~azure.storage.blob.PremiumPageBlobTier premium_page_blob_tier:
            A page blob tier value to set the blob to. The tier correlates to the size of the
            blob and number of allowed IOPS. This is only applicable to page blobs on
            premium storage accounts.
        :keyword tags:
            Name-value pairs associated with the blob as tag. Tags are case-sensitive.
            The tag set may contain at most 10 tags.  Tag keys must be between 1 and 128 characters,
            and tag values must be between 0 and 256 characters.
            Valid tag key and value characters include: lowercase and uppercase letters, digits (0-9),
            space (` `), plus (+), minus (-), period (.), solidus (/), colon (:), equals (=), underscore (_)

            .. versionadded:: 12.4.0

        :paramtype tags: dict(str, str)
        :keyword int sequence_number:
            Only for Page blobs. The sequence number is a user-controlled value that you can use to
            track requests. The value of the sequence number must be between 0
            and 2^63 - 1.The default value is 0.
        :keyword lease:
            Required if the blob has an active lease. Value can be a BlobLeaseClient object
            or the lease ID as a string.
        :paramtype lease: ~azure.storage.blob.BlobLeaseClient or str
        :keyword ~azure.storage.blob.ImmutabilityPolicy immutability_policy:
            Specifies the immutability policy of a blob, blob snapshot or blob version.

            .. versionadded:: 12.10.0
                This was introduced in API version '2020-10-02'.

        :keyword bool legal_hold:
            Specified if a legal hold should be set on the blob.

            .. versionadded:: 12.10.0
                This was introduced in API version '2020-10-02'.

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
        :keyword ~azure.storage.blob.CustomerProvidedEncryptionKey cpk:
            Encrypts the data on the service-side with the given key.
            Use of customer-provided keys must be done over HTTPS.
            As the encryption key itself is provided in the request,
            a secure connection must be established to transfer the key.
        :keyword str encryption_scope:
            A predefined encryption scope used to encrypt the data on the service. An encryption
            scope can be created using the Management API and referenced here by name. If a default
            encryption scope has been defined at the container, this value will override it if the
            container-level scope is configured to allow overrides. Otherwise an error will be raised.

            .. versionadded:: 12.2.0

        :keyword int timeout:
            Sets the server-side timeout for the operation in seconds. For more details see
            https://learn.microsoft.com/rest/api/storageservices/setting-timeouts-for-blob-service-operations.
            This value is not tracked or validated on the client. To configure client-side network timesouts
            see `here <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob
            #other-client--per-operation-configuration>`_.
        :returns: Blob-updated property dict (Etag and last modified).
        :rtype: dict[str, Any]
        """
    def create_append_blob(self, content_settings: ContentSettings | None = None, metadata: Dict[str, str] | None = None, **kwargs: Any) -> Dict[str, str | datetime]:
        """Creates a new Append Blob. This operation creates a new 0-length append blob. The content
        of any existing blob is overwritten with the newly initialized append blob. To add content to
        the append blob, call the :func:`append_block` or :func:`append_block_from_url` method.

        :param ~azure.storage.blob.ContentSettings content_settings:
            ContentSettings object used to set blob properties. Used to set content type, encoding,
            language, disposition, md5, and cache control.
        :param metadata:
            Name-value pairs associated with the blob as metadata.
        :type metadata: dict(str, str)
        :keyword tags:
            Name-value pairs associated with the blob as tag. Tags are case-sensitive.
            The tag set may contain at most 10 tags.  Tag keys must be between 1 and 128 characters,
            and tag values must be between 0 and 256 characters.
            Valid tag key and value characters include: lowercase and uppercase letters, digits (0-9),
            space (` `), plus (+), minus (-), period (.), solidus (/), colon (:), equals (=), underscore (_)

            .. versionadded:: 12.4.0

        :paramtype tags: dict(str, str)
        :keyword lease:
            Required if the blob has an active lease. Value can be a BlobLeaseClient object
            or the lease ID as a string.
        :paramtype lease: ~azure.storage.blob.BlobLeaseClient or str
        :keyword ~azure.storage.blob.ImmutabilityPolicy immutability_policy:
            Specifies the immutability policy of a blob, blob snapshot or blob version.

            .. versionadded:: 12.10.0
                This was introduced in API version '2020-10-02'.

        :keyword bool legal_hold:
            Specified if a legal hold should be set on the blob.

            .. versionadded:: 12.10.0
                This was introduced in API version '2020-10-02'.

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
        :keyword ~azure.storage.blob.CustomerProvidedEncryptionKey cpk:
            Encrypts the data on the service-side with the given key.
            Use of customer-provided keys must be done over HTTPS.
            As the encryption key itself is provided in the request,
            a secure connection must be established to transfer the key.
        :keyword str encryption_scope:
            A predefined encryption scope used to encrypt the data on the service. An encryption
            scope can be created using the Management API and referenced here by name. If a default
            encryption scope has been defined at the container, this value will override it if the
            container-level scope is configured to allow overrides. Otherwise an error will be raised.

            .. versionadded:: 12.2.0

        :keyword int timeout:
            Sets the server-side timeout for the operation in seconds. For more details see
            https://learn.microsoft.com/rest/api/storageservices/setting-timeouts-for-blob-service-operations.
            This value is not tracked or validated on the client. To configure client-side network timesouts
            see `here <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob
            #other-client--per-operation-configuration>`_.
        :returns: Blob-updated property dict (Etag and last modified).
        :rtype: dict[str, Any]
        """
    def create_snapshot(self, metadata: Dict[str, str] | None = None, **kwargs: Any) -> Dict[str, str | datetime]:
        """Creates a snapshot of the blob.

        A snapshot is a read-only version of a blob that's taken at a point in time.
        It can be read, copied, or deleted, but not modified. Snapshots provide a way
        to back up a blob as it appears at a moment in time.

        A snapshot of a blob has the same name as the base blob from which the snapshot
        is taken, with a DateTime value appended to indicate the time at which the
        snapshot was taken.

        :param metadata:
            Name-value pairs associated with the blob as metadata.
        :type metadata: dict(str, str)
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
        :keyword str if_tags_match_condition:
            Specify a SQL where clause on blob tags to operate only on destination blob with a matching value.

            .. versionadded:: 12.4.0

        :keyword lease:
            Required if the blob has an active lease. Value can be a BlobLeaseClient object
            or the lease ID as a string.
        :paramtype lease: ~azure.storage.blob.BlobLeaseClient or str
        :keyword ~azure.storage.blob.CustomerProvidedEncryptionKey cpk:
            Encrypts the data on the service-side with the given key.
            Use of customer-provided keys must be done over HTTPS.
            As the encryption key itself is provided in the request,
            a secure connection must be established to transfer the key.
        :keyword str encryption_scope:
            A predefined encryption scope used to encrypt the data on the service. An encryption
            scope can be created using the Management API and referenced here by name. If a default
            encryption scope has been defined at the container, this value will override it if the
            container-level scope is configured to allow overrides. Otherwise an error will be raised.

            .. versionadded:: 12.2.0

        :keyword int timeout:
            Sets the server-side timeout for the operation in seconds. For more details see
            https://learn.microsoft.com/rest/api/storageservices/setting-timeouts-for-blob-service-operations.
            This value is not tracked or validated on the client. To configure client-side network timesouts
            see `here <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob
            #other-client--per-operation-configuration>`_.
        :returns: Blob-updated property dict (Snapshot ID, Etag, and last modified).
        :rtype: dict[str, Any]

        .. admonition:: Example:

            .. literalinclude:: ../samples/blob_samples_common.py
                :start-after: [START create_blob_snapshot]
                :end-before: [END create_blob_snapshot]
                :language: python
                :dedent: 8
                :caption: Create a snapshot of the blob.
        """
    def start_copy_from_url(self, source_url: str, metadata: Dict[str, str] | None = None, incremental_copy: bool = False, **kwargs: Any) -> Dict[str, str | datetime]:
        '''Copies a blob from the given URL.

        This operation returns a dictionary containing `copy_status` and `copy_id`,
        which can be used to check the status of or abort the copy operation.
        `copy_status` will be \'success\' if the copy completed synchronously or
        \'pending\' if the copy has been started asynchronously. For asynchronous copies,
        the status can be checked by polling the :func:`get_blob_properties` method and
        checking the copy status. Set `requires_sync` to True to force the copy to be synchronous.
        The Blob service copies blobs on a best-effort basis.

        The source blob for a copy operation may be a block blob, an append blob,
        or a page blob. If the destination blob already exists, it must be of the
        same blob type as the source blob. Any existing destination blob will be
        overwritten. The destination blob cannot be modified while a copy operation
        is in progress.

        When copying from a page blob, the Blob service creates a destination page
        blob of the source blob\'s length, initially containing all zeroes. Then
        the source page ranges are enumerated, and non-empty ranges are copied.

        For a block blob or an append blob, the Blob service creates a committed
        blob of zero length before returning from this operation. When copying
        from a block blob, all committed blocks and their block IDs are copied.
        Uncommitted blocks are not copied. At the end of the copy operation, the
        destination blob will have the same committed block count as the source.

        When copying from an append blob, all committed blocks are copied. At the
        end of the copy operation, the destination blob will have the same committed
        block count as the source.

        :param str source_url:
            A URL of up to 2 KB in length that specifies a file or blob.
            The value should be URL-encoded as it would appear in a request URI.
            If the source is in another account, the source must either be public
            or must be authenticated via a shared access signature. If the source
            is public, no authentication is required.
            Examples:
            https://myaccount.blob.core.windows.net/mycontainer/myblob

            https://myaccount.blob.core.windows.net/mycontainer/myblob?snapshot=<DateTime>

            https://otheraccount.blob.core.windows.net/mycontainer/myblob?sastoken
        :param metadata:
            Name-value pairs associated with the blob as metadata. If no name-value
            pairs are specified, the operation will copy the metadata from the
            source blob or file to the destination blob. If one or more name-value
            pairs are specified, the destination blob is created with the specified
            metadata, and metadata is not copied from the source blob or file.
        :type metadata: dict(str, str)
        :param bool incremental_copy:
            Copies the snapshot of the source page blob to a destination page blob.
            The snapshot is copied such that only the differential changes between
            the previously copied snapshot are transferred to the destination.
            The copied snapshots are complete copies of the original snapshot and
            can be read or copied from as usual. Defaults to False.
        :keyword tags:
            Name-value pairs associated with the blob as tag. Tags are case-sensitive.
            The tag set may contain at most 10 tags.  Tag keys must be between 1 and 128 characters,
            and tag values must be between 0 and 256 characters.
            Valid tag key and value characters include: lowercase and uppercase letters, digits (0-9),
            space (` `), plus (+), minus (-), period (.), solidus (/), colon (:), equals (=), underscore (_).

            The (case-sensitive) literal "COPY" can instead be passed to copy tags from the source blob.
            This option is only available when `incremental_copy=False` and `requires_sync=True`.

            .. versionadded:: 12.4.0

        :paramtype tags: dict(str, str) or Literal["COPY"]
        :keyword ~azure.storage.blob.ImmutabilityPolicy immutability_policy:
            Specifies the immutability policy of a blob, blob snapshot or blob version.

            .. versionadded:: 12.10.0
                This was introduced in API version \'2020-10-02\'.

        :keyword bool legal_hold:
            Specified if a legal hold should be set on the blob.

            .. versionadded:: 12.10.0
                This was introduced in API version \'2020-10-02\'.

        :keyword ~datetime.datetime source_if_modified_since:
            A DateTime value. Azure expects the date value passed in to be UTC.
            If timezone is included, any non-UTC datetimes will be converted to UTC.
            If a date is passed in without timezone info, it is assumed to be UTC.
            Specify this conditional header to copy the blob only if the source
            blob has been modified since the specified date/time.
        :keyword ~datetime.datetime source_if_unmodified_since:
            A DateTime value. Azure expects the date value passed in to be UTC.
            If timezone is included, any non-UTC datetimes will be converted to UTC.
            If a date is passed in without timezone info, it is assumed to be UTC.
            Specify this conditional header to copy the blob only if the source blob
            has not been modified since the specified date/time.
        :keyword str source_etag:
            The source ETag value, or the wildcard character (*). Used to check if the resource has changed,
            and act according to the condition specified by the `match_condition` parameter.
        :keyword ~azure.core.MatchConditions source_match_condition:
            The source match condition to use upon the etag.
        :keyword ~datetime.datetime if_modified_since:
            A DateTime value. Azure expects the date value passed in to be UTC.
            If timezone is included, any non-UTC datetimes will be converted to UTC.
            If a date is passed in without timezone info, it is assumed to be UTC.
            Specify this conditional header to copy the blob only
            if the destination blob has been modified since the specified date/time.
            If the destination blob has not been modified, the Blob service returns
            status code 412 (Precondition Failed).
        :keyword ~datetime.datetime if_unmodified_since:
            A DateTime value. Azure expects the date value passed in to be UTC.
            If timezone is included, any non-UTC datetimes will be converted to UTC.
            If a date is passed in without timezone info, it is assumed to be UTC.
            Specify this conditional header to copy the blob only
            if the destination blob has not been modified since the specified
            date/time. If the destination blob has been modified, the Blob service
            returns status code 412 (Precondition Failed).
        :keyword str etag:
            The destination ETag value, or the wildcard character (*). Used to check if the resource has changed,
            and act according to the condition specified by the `match_condition` parameter.
        :keyword ~azure.core.MatchConditions match_condition:
            The destination match condition to use upon the etag.
        :keyword destination_lease:
            The lease ID specified for this header must match the lease ID of the
            destination blob. If the request does not include the lease ID or it is not
            valid, the operation fails with status code 412 (Precondition Failed).
        :paramtype destination_lease: ~azure.storage.blob.BlobLeaseClient or str
        :keyword source_lease:
            Specify this to perform the Copy Blob operation only if
            the lease ID given matches the active lease ID of the source blob.
        :paramtype source_lease: ~azure.storage.blob.BlobLeaseClient or str
        :keyword int timeout:
            Sets the server-side timeout for the operation in seconds. For more details see
            https://learn.microsoft.com/rest/api/storageservices/setting-timeouts-for-blob-service-operations.
            This value is not tracked or validated on the client. To configure client-side network timesouts
            see `here <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob
            #other-client--per-operation-configuration>`_.
        :keyword ~azure.storage.blob.PremiumPageBlobTier premium_page_blob_tier:
            A page blob tier value to set the blob to. The tier correlates to the size of the
            blob and number of allowed IOPS. This is only applicable to page blobs on
            premium storage accounts.
        :keyword ~azure.storage.blob.StandardBlobTier standard_blob_tier:
            A standard blob tier value to set the blob to. For this version of the library,
            this is only applicable to block blobs on standard storage accounts.
        :keyword ~azure.storage.blob.RehydratePriority rehydrate_priority:
            Indicates the priority with which to rehydrate an archived blob
        :keyword bool seal_destination_blob:
            Seal the destination append blob. This operation is only for append blob.

            .. versionadded:: 12.4.0

        :keyword bool requires_sync:
            Enforces that the service will not return a response until the copy is complete.
        :keyword str source_authorization:
            Authenticate as a service principal using a client secret to access a source blob. Ensure "bearer " is
            the prefix of the source_authorization string. This option is only available when `incremental_copy` is
            set to False and `requires_sync` is set to True.

            .. versionadded:: 12.9.0

        :keyword str encryption_scope:
            A predefined encryption scope used to encrypt the data on the sync copied blob. An encryption
            scope can be created using the Management API and referenced here by name. If a default
            encryption scope has been defined at the container, this value will override it if the
            container-level scope is configured to allow overrides. Otherwise an error will be raised.

            .. versionadded:: 12.10.0

        :returns: A dictionary of copy properties (etag, last_modified, copy_id, copy_status).
        :rtype: dict[str, Union[str, ~datetime.datetime]]

        .. admonition:: Example:

            .. literalinclude:: ../samples/blob_samples_common.py
                :start-after: [START copy_blob_from_url]
                :end-before: [END copy_blob_from_url]
                :language: python
                :dedent: 12
                :caption: Copy a blob from a URL.
        '''
    def abort_copy(self, copy_id: str | Dict[str, Any] | BlobProperties, **kwargs: Any) -> None:
        """Abort an ongoing copy operation.

        This will leave a destination blob with zero length and full metadata.
        This will raise an error if the copy operation has already ended.

        :param copy_id:
            The copy operation to abort. This can be either an ID string, or an
            instance of BlobProperties.
        :type copy_id: str or ~azure.storage.blob.BlobProperties
        :rtype: None

        .. admonition:: Example:

            .. literalinclude:: ../samples/blob_samples_common.py
                :start-after: [START abort_copy_blob_from_url]
                :end-before: [END abort_copy_blob_from_url]
                :language: python
                :dedent: 12
                :caption: Abort copying a blob from URL.
        """
    def acquire_lease(self, lease_duration: int = -1, lease_id: str | None = None, **kwargs: Any) -> BlobLeaseClient:
        '''Requests a new lease.

        If the blob does not have an active lease, the Blob
        Service creates a lease on the blob and returns a new lease.

        :param int lease_duration:
            Specifies the duration of the lease, in seconds, or negative one
            (-1) for a lease that never expires. A non-infinite lease can be
            between 15 and 60 seconds. A lease duration cannot be changed
            using renew or change. Default is -1 (infinite lease).
        :param str lease_id:
            Proposed lease ID, in a GUID string format. The Blob Service
            returns 400 (Invalid request) if the proposed lease ID is not
            in the correct format.
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
        :keyword str if_tags_match_condition:
            Specify a SQL where clause on blob tags to operate only on blob with a matching value.
            eg. ``"\\"tagname\\"=\'my tag\'"``

            .. versionadded:: 12.4.0

        :keyword int timeout:
            Sets the server-side timeout for the operation in seconds. For more details see
            https://learn.microsoft.com/rest/api/storageservices/setting-timeouts-for-blob-service-operations.
            This value is not tracked or validated on the client. To configure client-side network timesouts
            see `here <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob
            #other-client--per-operation-configuration>`_.
        :returns: A BlobLeaseClient object.
        :rtype: ~azure.storage.blob.BlobLeaseClient

        .. admonition:: Example:

            .. literalinclude:: ../samples/blob_samples_common.py
                :start-after: [START acquire_lease_on_blob]
                :end-before: [END acquire_lease_on_blob]
                :language: python
                :dedent: 8
                :caption: Acquiring a lease on a blob.
        '''
    def set_standard_blob_tier(self, standard_blob_tier: str | StandardBlobTier, **kwargs: Any) -> None:
        '''This operation sets the tier on a block blob.

        A block blob\'s tier determines Hot/Cool/Archive storage type.
        This operation does not update the blob\'s ETag.

        :param standard_blob_tier:
            Indicates the tier to be set on the blob. Options include \'Hot\', \'Cool\',
            \'Archive\'. The hot tier is optimized for storing data that is accessed
            frequently. The cool storage tier is optimized for storing data that
            is infrequently accessed and stored for at least a month. The archive
            tier is optimized for storing data that is rarely accessed and stored
            for at least six months with flexible latency requirements.
        :type standard_blob_tier: str or ~azure.storage.blob.StandardBlobTier
        :keyword ~azure.storage.blob.RehydratePriority rehydrate_priority:
            Indicates the priority with which to rehydrate an archived blob
        :keyword str version_id:
            The version id parameter is an opaque DateTime
            value that, when present, specifies the version of the blob to download.

            .. versionadded:: 12.4.0
            This keyword argument was introduced in API version \'2019-12-12\'.
        :keyword str if_tags_match_condition:
            Specify a SQL where clause on blob tags to operate only on blob with a matching value.
            eg. ``"\\"tagname\\"=\'my tag\'"``

            .. versionadded:: 12.4.0
        :keyword int timeout:
            Sets the server-side timeout for the operation in seconds. For more details see
            https://learn.microsoft.com/rest/api/storageservices/setting-timeouts-for-blob-service-operations.
            This value is not tracked or validated on the client. To configure client-side network timesouts
            see `here <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob
            #other-client--per-operation-configuration>`_.
        :keyword lease:
            Required if the blob has an active lease. Value can be a BlobLeaseClient object
            or the lease ID as a string.
        :paramtype lease: ~azure.storage.blob.BlobLeaseClient or str
        :rtype: None
        '''
    def stage_block(self, block_id: str, data: Iterable[AnyStr] | IO[AnyStr], length: int | None = None, **kwargs) -> Dict[str, Any]:
        """Creates a new block to be committed as part of a blob.

        :param str block_id: A string value that identifies the block.
             The string should be less than or equal to 64 bytes in size.
             For a given blob, the block_id must be the same size for each block.
        :param data: The blob data.
        :param int length: Size of the block.
        :keyword bool validate_content:
            If true, calculates an MD5 hash for each chunk of the blob. The storage
            service checks the hash of the content that has arrived with the hash
            that was sent. This is primarily valuable for detecting bitflips on
            the wire if using http instead of https, as https (the default), will
            already validate. Note that this MD5 hash is not stored with the
            blob. Also note that if enabled, the memory-efficient upload algorithm
            will not be used because computing the MD5 hash requires buffering
            entire blocks, and doing so defeats the purpose of the memory-efficient algorithm.
        :keyword lease:
            Required if the blob has an active lease. Value can be a BlobLeaseClient object
            or the lease ID as a string.
        :paramtype lease: ~azure.storage.blob.BlobLeaseClient or str
        :keyword str encoding:
            Defaults to UTF-8.
        :keyword ~azure.storage.blob.CustomerProvidedEncryptionKey cpk:
            Encrypts the data on the service-side with the given key.
            Use of customer-provided keys must be done over HTTPS.
            As the encryption key itself is provided in the request,
            a secure connection must be established to transfer the key.
        :keyword str encryption_scope:
            A predefined encryption scope used to encrypt the data on the service. An encryption
            scope can be created using the Management API and referenced here by name. If a default
            encryption scope has been defined at the container, this value will override it if the
            container-level scope is configured to allow overrides. Otherwise an error will be raised.

            .. versionadded:: 12.2.0

        :keyword int timeout:
            Sets the server-side timeout for the operation in seconds. For more details see
            https://learn.microsoft.com/rest/api/storageservices/setting-timeouts-for-blob-service-operations.
            This value is not tracked or validated on the client. To configure client-side network timesouts
            see `here <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob
            #other-client--per-operation-configuration>`_.
        :returns: Blob property dict.
        :rtype: dict[str, Any]
        """
    def stage_block_from_url(self, block_id: str | int, source_url: str, source_offset: int | None = None, source_length: int | None = None, source_content_md5: bytes | bytearray | None = None, **kwargs) -> Dict[str, Any]:
        '''Creates a new block to be committed as part of a blob where
        the contents are read from a URL.

        :param str block_id: A string value that identifies the block.
             The string should be less than or equal to 64 bytes in size.
             For a given blob, the block_id must be the same size for each block.
        :param str source_url: The URL.
        :param int source_offset:
            Start of byte range to use for the block.
            Must be set if source length is provided.
        :param int source_length: The size of the block in bytes.
        :param bytearray source_content_md5:
            Specify the md5 calculated for the range of
            bytes that must be read from the copy source.
        :keyword lease:
            Required if the blob has an active lease. Value can be a BlobLeaseClient object
            or the lease ID as a string.
        :paramtype lease: ~azure.storage.blob.BlobLeaseClient or str
        :keyword ~azure.storage.blob.CustomerProvidedEncryptionKey cpk:
            Encrypts the data on the service-side with the given key.
            Use of customer-provided keys must be done over HTTPS.
            As the encryption key itself is provided in the request,
            a secure connection must be established to transfer the key.
        :keyword str encryption_scope:
            A predefined encryption scope used to encrypt the data on the service. An encryption
            scope can be created using the Management API and referenced here by name. If a default
            encryption scope has been defined at the container, this value will override it if the
            container-level scope is configured to allow overrides. Otherwise an error will be raised.

            .. versionadded:: 12.2.0

        :keyword int timeout:
            Sets the server-side timeout for the operation in seconds. For more details see
            https://learn.microsoft.com/rest/api/storageservices/setting-timeouts-for-blob-service-operations.
            This value is not tracked or validated on the client. To configure client-side network timesouts
            see `here <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob
            #other-client--per-operation-configuration>`_.
        :keyword str source_authorization:
            Authenticate as a service principal using a client secret to access a source blob. Ensure "bearer " is
            the prefix of the source_authorization string.
        :returns: Blob property dict.
        :rtype: dict[str, Any]
        '''
    def get_block_list(self, block_list_type: str | None = 'committed', **kwargs: Any) -> Tuple[List[BlobBlock], List[BlobBlock]]:
        """The Get Block List operation retrieves the list of blocks that have
        been uploaded as part of a block blob.

        :param str block_list_type:
            Specifies whether to return the list of committed
            blocks, the list of uncommitted blocks, or both lists together.
            Possible values include: 'committed', 'uncommitted', 'all'
        :keyword lease:
            Required if the blob has an active lease. Value can be a BlobLeaseClient object
            or the lease ID as a string.
        :paramtype lease: ~azure.storage.blob.BlobLeaseClient or str
        :keyword str if_tags_match_condition:
            Specify a SQL where clause on blob tags to operate only on destination blob with a matching value.

            .. versionadded:: 12.4.0

        :keyword int timeout:
            Sets the server-side timeout for the operation in seconds. For more details see
            https://learn.microsoft.com/rest/api/storageservices/setting-timeouts-for-blob-service-operations.
            This value is not tracked or validated on the client. To configure client-side network timesouts
            see `here <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob
            #other-client--per-operation-configuration>`_.
        :returns: A tuple of two lists - committed and uncommitted blocks
        :rtype: tuple(list(~azure.storage.blob.BlobBlock), list(~azure.storage.blob.BlobBlock))
        """
    def commit_block_list(self, block_list: List[BlobBlock], content_settings: ContentSettings | None = None, metadata: Dict[str, str] | None = None, **kwargs) -> Dict[str, str | datetime]:
        """The Commit Block List operation writes a blob by specifying the list of
        block IDs that make up the blob.

        :param list block_list:
            List of Blockblobs.
        :param ~azure.storage.blob.ContentSettings content_settings:
            ContentSettings object used to set blob properties. Used to set content type, encoding,
            language, disposition, md5, and cache control.
        :param metadata:
            Name-value pairs associated with the blob as metadata.
        :type metadata: dict[str, str]
        :keyword tags:
            Name-value pairs associated with the blob as tag. Tags are case-sensitive.
            The tag set may contain at most 10 tags.  Tag keys must be between 1 and 128 characters,
            and tag values must be between 0 and 256 characters.
            Valid tag key and value characters include: lowercase and uppercase letters, digits (0-9),
            space (` `), plus (+), minus (-), period (.), solidus (/), colon (:), equals (=), underscore (_)

            .. versionadded:: 12.4.0

        :paramtype tags: dict(str, str)
        :keyword lease:
            Required if the blob has an active lease. Value can be a BlobLeaseClient object
            or the lease ID as a string.
        :paramtype lease: ~azure.storage.blob.BlobLeaseClient or str
        :keyword ~azure.storage.blob.ImmutabilityPolicy immutability_policy:
            Specifies the immutability policy of a blob, blob snapshot or blob version.

            .. versionadded:: 12.10.0
                This was introduced in API version '2020-10-02'.

        :keyword bool legal_hold:
            Specified if a legal hold should be set on the blob.

            .. versionadded:: 12.10.0
                This was introduced in API version '2020-10-02'.

        :keyword bool validate_content:
            If true, calculates an MD5 hash of the page content. The storage
            service checks the hash of the content that has arrived
            with the hash that was sent. This is primarily valuable for detecting
            bitflips on the wire if using http instead of https, as https (the default),
            will already validate. Note that this MD5 hash is not stored with the
            blob.
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
        :keyword str if_tags_match_condition:
            Specify a SQL where clause on blob tags to operate only on destination blob with a matching value.

            .. versionadded:: 12.4.0

        :keyword ~azure.storage.blob.StandardBlobTier standard_blob_tier:
            A standard blob tier value to set the blob to. For this version of the library,
            this is only applicable to block blobs on standard storage accounts.
        :keyword ~azure.storage.blob.CustomerProvidedEncryptionKey cpk:
            Encrypts the data on the service-side with the given key.
            Use of customer-provided keys must be done over HTTPS.
            As the encryption key itself is provided in the request,
            a secure connection must be established to transfer the key.
        :keyword str encryption_scope:
            A predefined encryption scope used to encrypt the data on the service. An encryption
            scope can be created using the Management API and referenced here by name. If a default
            encryption scope has been defined at the container, this value will override it if the
            container-level scope is configured to allow overrides. Otherwise an error will be raised.

            .. versionadded:: 12.2.0

        :keyword int timeout:
            Sets the server-side timeout for the operation in seconds. For more details see
            https://learn.microsoft.com/rest/api/storageservices/setting-timeouts-for-blob-service-operations.
            This value is not tracked or validated on the client. To configure client-side network timesouts
            see `here <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob
            #other-client--per-operation-configuration>`_.
        :returns: Blob-updated property dict (Etag and last modified).
        :rtype: dict(str, Any)
        """
    def set_premium_page_blob_tier(self, premium_page_blob_tier: str | PremiumPageBlobTier, **kwargs: Any) -> None:
        '''Sets the page blob tiers on the blob. This API is only supported for page blobs on premium accounts.

        :param premium_page_blob_tier:
            A page blob tier value to set the blob to. The tier correlates to the size of the
            blob and number of allowed IOPS. This is only applicable to page blobs on
            premium storage accounts.
        :type premium_page_blob_tier: ~azure.storage.blob.PremiumPageBlobTier
        :keyword str if_tags_match_condition:
            Specify a SQL where clause on blob tags to operate only on blob with a matching value.
            eg. ``"\\"tagname\\"=\'my tag\'"``

            .. versionadded:: 12.4.0

        :keyword int timeout:
            Sets the server-side timeout for the operation in seconds. For more details see
            https://learn.microsoft.com/rest/api/storageservices/setting-timeouts-for-blob-service-operations.
            This value is not tracked or validated on the client. To configure client-side network timesouts
            see `here <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob
            #other-client--per-operation-configuration>`_.
        :keyword lease:
            Required if the blob has an active lease. Value can be a BlobLeaseClient object
            or the lease ID as a string.
        :paramtype lease: ~azure.storage.blob.BlobLeaseClient or str
        :rtype: None
        '''
    def set_blob_tags(self, tags: Dict[str, str] | None = None, **kwargs: Any) -> Dict[str, Any]:
        '''The Set Tags operation enables users to set tags on a blob or specific blob version, but not snapshot.
            Each call to this operation replaces all existing tags attached to the blob. To remove all
            tags from the blob, call this operation with no tags set.

        .. versionadded:: 12.4.0
            This operation was introduced in API version \'2019-12-12\'.

        :param tags:
            Name-value pairs associated with the blob as tag. Tags are case-sensitive.
            The tag set may contain at most 10 tags.  Tag keys must be between 1 and 128 characters,
            and tag values must be between 0 and 256 characters.
            Valid tag key and value characters include: lowercase and uppercase letters, digits (0-9),
            space (` `), plus (+), minus (-), period (.), solidus (/), colon (:), equals (=), underscore (_)
        :type tags: dict(str, str)
        :keyword str version_id:
            The version id parameter is an opaque DateTime
            value that, when present, specifies the version of the blob to add tags to.
        :keyword bool validate_content:
            If true, calculates an MD5 hash of the tags content. The storage
            service checks the hash of the content that has arrived
            with the hash that was sent. This is primarily valuable for detecting
            bitflips on the wire if using http instead of https, as https (the default),
            will already validate. Note that this MD5 hash is not stored with the
            blob.
        :keyword str if_tags_match_condition:
            Specify a SQL where clause on blob tags to operate only on destination blob with a matching value.
            eg. ``"\\"tagname\\"=\'my tag\'"``
        :keyword lease:
            Required if the blob has an active lease. Value can be a BlobLeaseClient object
            or the lease ID as a string.
        :paramtype lease: ~azure.storage.blob.BlobLeaseClient or str
        :keyword int timeout:
            Sets the server-side timeout for the operation in seconds. For more details see
            https://learn.microsoft.com/rest/api/storageservices/setting-timeouts-for-blob-service-operations.
            This value is not tracked or validated on the client. To configure client-side network timesouts
            see `here <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob
            #other-client--per-operation-configuration>`_.
        :returns: Blob-updated property dict (Etag and last modified)
        :rtype: Dict[str, Any]
        '''
    def get_blob_tags(self, **kwargs: Any) -> Dict[str, str]:
        '''The Get Tags operation enables users to get tags on a blob or specific blob version, or snapshot.

        .. versionadded:: 12.4.0
            This operation was introduced in API version \'2019-12-12\'.

        :keyword str version_id:
            The version id parameter is an opaque DateTime
            value that, when present, specifies the version of the blob to add tags to.
        :keyword str if_tags_match_condition:
            Specify a SQL where clause on blob tags to operate only on destination blob with a matching value.
            eg. ``"\\"tagname\\"=\'my tag\'"``
        :keyword lease:
            Required if the blob has an active lease. Value can be a BlobLeaseClient object
            or the lease ID as a string.
        :paramtype lease: ~azure.storage.blob.BlobLeaseClient or str
        :keyword int timeout:
            Sets the server-side timeout for the operation in seconds. For more details see
            https://learn.microsoft.com/rest/api/storageservices/setting-timeouts-for-blob-service-operations.
            This value is not tracked or validated on the client. To configure client-side network timesouts
            see `here <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob
            #other-client--per-operation-configuration>`_.
        :returns: Key value pairs of blob tags.
        :rtype: Dict[str, str]
        '''
    def get_page_ranges(self, offset: int | None = None, length: int | None = None, previous_snapshot_diff: str | Dict[str, Any] | None = None, **kwargs) -> Tuple[List[Dict[str, int]], List[Dict[str, int]]]:
        '''DEPRECATED: Returns the list of valid page ranges for a Page Blob or snapshot
        of a page blob.

        :param int offset:
            Start of byte range to use for getting valid page ranges.
            If no length is given, all bytes after the offset will be searched.
            Pages must be aligned with 512-byte boundaries, the start offset
            must be a modulus of 512 and the length must be a modulus of
            512.
        :param int length:
            Number of bytes to use for getting valid page ranges.
            If length is given, offset must be provided.
            This range will return valid page ranges from the offset start up to
            the specified length.
            Pages must be aligned with 512-byte boundaries, the start offset
            must be a modulus of 512 and the length must be a modulus of
            512.
        :param str previous_snapshot_diff:
            The snapshot diff parameter that contains an opaque DateTime value that
            specifies a previous blob snapshot to be compared
            against a more recent snapshot or the current blob.
        :keyword lease:
            Required if the blob has an active lease. Value can be a BlobLeaseClient object
            or the lease ID as a string.
        :paramtype lease: ~azure.storage.blob.BlobLeaseClient or str
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
        :keyword str if_tags_match_condition:
            Specify a SQL where clause on blob tags to operate only on blob with a matching value.
            eg. ``"\\"tagname\\"=\'my tag\'"``

            .. versionadded:: 12.4.0

        :keyword int timeout:
            Sets the server-side timeout for the operation in seconds. For more details see
            https://learn.microsoft.com/rest/api/storageservices/setting-timeouts-for-blob-service-operations.
            This value is not tracked or validated on the client. To configure client-side network timesouts
            see `here <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob
            #other-client--per-operation-configuration>`_.
        :returns:
            A tuple of two lists of page ranges as dictionaries with \'start\' and \'end\' keys.
            The first element are filled page ranges, the 2nd element is cleared page ranges.
        :rtype: tuple(list(dict(str, str), list(dict(str, str))
        '''
    def list_page_ranges(self, *, offset: int | None = None, length: int | None = None, previous_snapshot: str | Dict[str, Any] | None = None, **kwargs: Any) -> ItemPaged[PageRange]:
        '''Returns the list of valid page ranges for a Page Blob or snapshot
        of a page blob. If `previous_snapshot` is specified, the result will be
        a diff of changes between the target blob and the previous snapshot.

        :keyword int offset:
            Start of byte range to use for getting valid page ranges.
            If no length is given, all bytes after the offset will be searched.
            Pages must be aligned with 512-byte boundaries, the start offset
            must be a modulus of 512 and the length must be a modulus of
            512.
        :keyword int length:
            Number of bytes to use for getting valid page ranges.
            If length is given, offset must be provided.
            This range will return valid page ranges from the offset start up to
            the specified length.
            Pages must be aligned with 512-byte boundaries, the start offset
            must be a modulus of 512 and the length must be a modulus of
            512.
        :keyword previous_snapshot:
            A snapshot value that specifies that the response will contain only pages that were changed
            between target blob and previous snapshot. Changed pages include both updated and cleared
            pages. The target blob may be a snapshot, as long as the snapshot specified by `previous_snapshot`
            is the older of the two.
        :paramtype previous_snapshot: str or Dict[str, Any]
        :keyword lease:
            Required if the blob has an active lease. Value can be a BlobLeaseClient object
            or the lease ID as a string.
        :paramtype lease: ~azure.storage.blob.BlobLeaseClient or str
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
        :keyword str if_tags_match_condition:
            Specify a SQL where clause on blob tags to operate only on blob with a matching value.
            eg. ``"\\"tagname\\"=\'my tag\'"``

            .. versionadded:: 12.4.0

        :keyword int results_per_page:
            The maximum number of page ranges to retrieve per API call.
        :keyword int timeout:
            Sets the server-side timeout for the operation in seconds. For more details see
            https://learn.microsoft.com/rest/api/storageservices/setting-timeouts-for-blob-service-operations.
            This value is not tracked or validated on the client. To configure client-side network timesouts
            see `here <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob
            #other-client--per-operation-configuration>`_.
        :returns: An iterable (auto-paging) of PageRange.
        :rtype: ~azure.core.paging.ItemPaged[~azure.storage.blob.PageRange]
        '''
    def get_page_range_diff_for_managed_disk(self, previous_snapshot_url: str, offset: int | None = None, length: int | None = None, **kwargs) -> Tuple[List[Dict[str, int]], List[Dict[str, int]]]:
        """Returns the list of valid page ranges for a managed disk or snapshot.

        .. note::
            This operation is only available for managed disk accounts.

        .. versionadded:: 12.2.0
            This operation was introduced in API version '2019-07-07'.

        :param previous_snapshot_url:
            Specifies the URL of a previous snapshot of the managed disk.
            The response will only contain pages that were changed between the target blob and
            its previous snapshot.
        :param int offset:
            Start of byte range to use for getting valid page ranges.
            If no length is given, all bytes after the offset will be searched.
            Pages must be aligned with 512-byte boundaries, the start offset
            must be a modulus of 512 and the length must be a modulus of
            512.
        :param int length:
            Number of bytes to use for getting valid page ranges.
            If length is given, offset must be provided.
            This range will return valid page ranges from the offset start up to
            the specified length.
            Pages must be aligned with 512-byte boundaries, the start offset
            must be a modulus of 512 and the length must be a modulus of
            512.
        :keyword lease:
            Required if the blob has an active lease. Value can be a BlobLeaseClient object
            or the lease ID as a string.
        :paramtype lease: ~azure.storage.blob.BlobLeaseClient or str
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
        :returns:
            A tuple of two lists of page ranges as dictionaries with 'start' and 'end' keys.
            The first element are filled page ranges, the 2nd element is cleared page ranges.
        :rtype: tuple(list(dict(str, str), list(dict(str, str))
        """
    def set_sequence_number(self, sequence_number_action: str | SequenceNumberAction, sequence_number: str | None = None, **kwargs: Any) -> Dict[str, str | datetime]:
        '''Sets the blob sequence number.

        :param str sequence_number_action:
            This property indicates how the service should modify the blob\'s sequence
            number. See :class:`~azure.storage.blob.SequenceNumberAction` for more information.
        :param str sequence_number:
            This property sets the blob\'s sequence number. The sequence number is a
            user-controlled property that you can use to track requests and manage
            concurrency issues.
        :keyword lease:
            Required if the blob has an active lease. Value can be a BlobLeaseClient object
            or the lease ID as a string.
        :paramtype lease: ~azure.storage.blob.BlobLeaseClient or str
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
        :keyword str if_tags_match_condition:
            Specify a SQL where clause on blob tags to operate only on blob with a matching value.
            eg. ``"\\"tagname\\"=\'my tag\'"``

            .. versionadded:: 12.4.0

        :keyword int timeout:
            Sets the server-side timeout for the operation in seconds. For more details see
            https://learn.microsoft.com/rest/api/storageservices/setting-timeouts-for-blob-service-operations.
            This value is not tracked or validated on the client. To configure client-side network timesouts
            see `here <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob
            #other-client--per-operation-configuration>`_.
        :returns: Blob-updated property dict (Etag and last modified).
        :rtype: dict(str, Any)
        '''
    def resize_blob(self, size: int, **kwargs: Any) -> Dict[str, str | datetime]:
        '''Resizes a page blob to the specified size.

        If the specified value is less than the current size of the blob,
        then all pages above the specified value are cleared.

        :param int size:
            Size used to resize blob. Maximum size for a page blob is up to 1 TB.
            The page blob size must be aligned to a 512-byte boundary.
        :keyword lease:
            Required if the blob has an active lease. Value can be a BlobLeaseClient object
            or the lease ID as a string.
        :paramtype lease: ~azure.storage.blob.BlobLeaseClient or str
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
        :keyword str if_tags_match_condition:
            Specify a SQL where clause on blob tags to operate only on blob with a matching value.
            eg. ``"\\"tagname\\"=\'my tag\'"``

            .. versionadded:: 12.4.0

        :keyword ~azure.storage.blob.PremiumPageBlobTier premium_page_blob_tier:
            A page blob tier value to set the blob to. The tier correlates to the size of the
            blob and number of allowed IOPS. This is only applicable to page blobs on
            premium storage accounts.
        :keyword int timeout:
            Sets the server-side timeout for the operation in seconds. For more details see
            https://learn.microsoft.com/rest/api/storageservices/setting-timeouts-for-blob-service-operations.
            This value is not tracked or validated on the client. To configure client-side network timesouts
            see `here <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob
            #other-client--per-operation-configuration>`_.
        :returns: Blob-updated property dict (Etag and last modified).
        :rtype: dict(str, Any)
        '''
    def upload_page(self, page: bytes, offset: int, length: int, **kwargs) -> Dict[str, str | datetime]:
        '''The Upload Pages operation writes a range of pages to a page blob.

        :param bytes page:
            Content of the page.
        :param int offset:
            Start of byte range to use for writing to a section of the blob.
            Pages must be aligned with 512-byte boundaries, the start offset
            must be a modulus of 512 and the length  must be a modulus of
            512.
        :param int length:
            Number of bytes to use for writing to a section of the blob.
            Pages must be aligned with 512-byte boundaries, the start offset
            must be a modulus of 512 and the length must be a modulus of
            512.
        :keyword lease:
            Required if the blob has an active lease. Value can be a BlobLeaseClient object
            or the lease ID as a string.
        :paramtype lease: ~azure.storage.blob.BlobLeaseClient or str
        :keyword bool validate_content:
            If true, calculates an MD5 hash of the page content. The storage
            service checks the hash of the content that has arrived
            with the hash that was sent. This is primarily valuable for detecting
            bitflips on the wire if using http instead of https, as https (the default),
            will already validate. Note that this MD5 hash is not stored with the
            blob.
        :keyword int if_sequence_number_lte:
            If the blob\'s sequence number is less than or equal to
            the specified value, the request proceeds; otherwise it fails.
        :keyword int if_sequence_number_lt:
            If the blob\'s sequence number is less than the specified
            value, the request proceeds; otherwise it fails.
        :keyword int if_sequence_number_eq:
            If the blob\'s sequence number is equal to the specified
            value, the request proceeds; otherwise it fails.
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
        :keyword str if_tags_match_condition:
            Specify a SQL where clause on blob tags to operate only on blob with a matching value.
            eg. ``"\\"tagname\\"=\'my tag\'"``

            .. versionadded:: 12.4.0

        :keyword ~azure.storage.blob.CustomerProvidedEncryptionKey cpk:
            Encrypts the data on the service-side with the given key.
            Use of customer-provided keys must be done over HTTPS.
            As the encryption key itself is provided in the request,
            a secure connection must be established to transfer the key.
        :keyword str encryption_scope:
            A predefined encryption scope used to encrypt the data on the service. An encryption
            scope can be created using the Management API and referenced here by name. If a default
            encryption scope has been defined at the container, this value will override it if the
            container-level scope is configured to allow overrides. Otherwise an error will be raised.

            .. versionadded:: 12.2.0

        :keyword str encoding:
            Defaults to UTF-8.
        :keyword int timeout:
            Sets the server-side timeout for the operation in seconds. For more details see
            https://learn.microsoft.com/rest/api/storageservices/setting-timeouts-for-blob-service-operations.
            This value is not tracked or validated on the client. To configure client-side network timesouts
            see `here <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob
            #other-client--per-operation-configuration>`_.
        :returns: Blob-updated property dict (Etag and last modified).
        :rtype: dict(str, Any)
        '''
    def upload_pages_from_url(self, source_url: str, offset: int, length: int, source_offset: int, **kwargs) -> Dict[str, Any]:
        '''
        The Upload Pages operation writes a range of pages to a page blob where
        the contents are read from a URL.

        :param str source_url:
            The URL of the source data. It can point to any Azure Blob or File, that is either public or has a
            shared access signature attached.
        :param int offset:
            Start of byte range to use for writing to a section of the blob.
            Pages must be aligned with 512-byte boundaries, the start offset
            must be a modulus of 512 and the length  must be a modulus of
            512.
        :param int length:
            Number of bytes to use for writing to a section of the blob.
            Pages must be aligned with 512-byte boundaries, the start offset
            must be a modulus of 512 and the length must be a modulus of
            512.
        :param int source_offset:
            This indicates the start of the range of bytes(inclusive) that has to be taken from the copy source.
            The service will read the same number of bytes as the destination range (length-offset).
        :keyword bytes source_content_md5:
            If given, the service will calculate the MD5 hash of the block content and compare against this value.
        :keyword ~datetime.datetime source_if_modified_since:
            A DateTime value. Azure expects the date value passed in to be UTC.
            If timezone is included, any non-UTC datetimes will be converted to UTC.
            If a date is passed in without timezone info, it is assumed to be UTC.
            Specify this header to perform the operation only
            if the source resource has been modified since the specified time.
        :keyword ~datetime.datetime source_if_unmodified_since:
            A DateTime value. Azure expects the date value passed in to be UTC.
            If timezone is included, any non-UTC datetimes will be converted to UTC.
            If a date is passed in without timezone info, it is assumed to be UTC.
            Specify this header to perform the operation only if
            the source resource has not been modified since the specified date/time.
        :keyword str source_etag:
            The source ETag value, or the wildcard character (*). Used to check if the resource has changed,
            and act according to the condition specified by the `match_condition` parameter.
        :keyword ~azure.core.MatchConditions source_match_condition:
            The source match condition to use upon the etag.
        :keyword lease:
            Required if the blob has an active lease. Value can be a BlobLeaseClient object
            or the lease ID as a string.
        :paramtype lease: ~azure.storage.blob.BlobLeaseClient or str
        :keyword int if_sequence_number_lte:
            If the blob\'s sequence number is less than or equal to
            the specified value, the request proceeds; otherwise it fails.
        :keyword int if_sequence_number_lt:
            If the blob\'s sequence number is less than the specified
            value, the request proceeds; otherwise it fails.
        :keyword int if_sequence_number_eq:
            If the blob\'s sequence number is equal to the specified
            value, the request proceeds; otherwise it fails.
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
            The destination ETag value, or the wildcard character (*). Used to check if the resource has changed,
            and act according to the condition specified by the `match_condition` parameter.
        :keyword ~azure.core.MatchConditions match_condition:
            The destination match condition to use upon the etag.
        :keyword str if_tags_match_condition:
            Specify a SQL where clause on blob tags to operate only on blob with a matching value.
            eg. ``"\\"tagname\\"=\'my tag\'"``

            .. versionadded:: 12.4.0

        :keyword ~azure.storage.blob.CustomerProvidedEncryptionKey cpk:
            Encrypts the data on the service-side with the given key.
            Use of customer-provided keys must be done over HTTPS.
            As the encryption key itself is provided in the request,
            a secure connection must be established to transfer the key.
        :keyword str encryption_scope:
            A predefined encryption scope used to encrypt the data on the service. An encryption
            scope can be created using the Management API and referenced here by name. If a default
            encryption scope has been defined at the container, this value will override it if the
            container-level scope is configured to allow overrides. Otherwise an error will be raised.

            .. versionadded:: 12.2.0

        :keyword int timeout:
            Sets the server-side timeout for the operation in seconds. For more details see
            https://learn.microsoft.com/rest/api/storageservices/setting-timeouts-for-blob-service-operations.
            This value is not tracked or validated on the client. To configure client-side network timesouts
            see `here <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob
            #other-client--per-operation-configuration>`_.
        :keyword str source_authorization:
            Authenticate as a service principal using a client secret to access a source blob. Ensure "bearer " is
            the prefix of the source_authorization string.
        '''
    def clear_page(self, offset: int, length: int, **kwargs: Any) -> Dict[str, str | datetime]:
        '''Clears a range of pages.

        :param int offset:
            Start of byte range to use for writing to a section of the blob.
            Pages must be aligned with 512-byte boundaries, the start offset
            must be a modulus of 512 and the length must be a modulus of
            512.
        :param int length:
            Number of bytes to use for writing to a section of the blob.
            Pages must be aligned with 512-byte boundaries, the start offset
            must be a modulus of 512 and the length must be a modulus of
            512.
        :keyword lease:
            Required if the blob has an active lease. Value can be a BlobLeaseClient object
            or the lease ID as a string.
        :paramtype lease: ~azure.storage.blob.BlobLeaseClient or str
        :keyword int if_sequence_number_lte:
            If the blob\'s sequence number is less than or equal to
            the specified value, the request proceeds; otherwise it fails.
        :keyword int if_sequence_number_lt:
            If the blob\'s sequence number is less than the specified
            value, the request proceeds; otherwise it fails.
        :keyword int if_sequence_number_eq:
            If the blob\'s sequence number is equal to the specified
            value, the request proceeds; otherwise it fails.
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
        :keyword str if_tags_match_condition:
            Specify a SQL where clause on blob tags to operate only on blob with a matching value.
            eg. ``"\\"tagname\\"=\'my tag\'"``

            .. versionadded:: 12.4.0

        :keyword ~azure.storage.blob.CustomerProvidedEncryptionKey cpk:
            Encrypts the data on the service-side with the given key.
            Use of customer-provided keys must be done over HTTPS.
            As the encryption key itself is provided in the request,
            a secure connection must be established to transfer the key.
        :keyword int timeout:
            Sets the server-side timeout for the operation in seconds. For more details see
            https://learn.microsoft.com/rest/api/storageservices/setting-timeouts-for-blob-service-operations.
            This value is not tracked or validated on the client. To configure client-side network timesouts
            see `here <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob
            #other-client--per-operation-configuration>`_.
        :returns: Blob-updated property dict (Etag and last modified).
        :rtype: dict(str, Any)
        '''
    def append_block(self, data: bytes | str | Iterable[AnyStr] | IO[AnyStr], length: int | None = None, **kwargs) -> Dict[str, str | datetime | int]:
        '''Commits a new block of data to the end of the existing append blob.

        :param data:
            Content of the block. This can be bytes, text, an iterable or a file-like object.
        :type data: bytes or str or Iterable
        :param int length:
            Size of the block in bytes.
        :keyword bool validate_content:
            If true, calculates an MD5 hash of the block content. The storage
            service checks the hash of the content that has arrived
            with the hash that was sent. This is primarily valuable for detecting
            bitflips on the wire if using http instead of https, as https (the default),
            will already validate. Note that this MD5 hash is not stored with the
            blob.
        :keyword int maxsize_condition:
            Optional conditional header. The max length in bytes permitted for
            the append blob. If the Append Block operation would cause the blob
            to exceed that limit or if the blob size is already greater than the
            value specified in this header, the request will fail with
            MaxBlobSizeConditionNotMet error (HTTP status code 412 - Precondition Failed).
        :keyword int appendpos_condition:
            Optional conditional header, used only for the Append Block operation.
            A number indicating the byte offset to compare. Append Block will
            succeed only if the append position is equal to this number. If it
            is not, the request will fail with the AppendPositionConditionNotMet error
            (HTTP status code 412 - Precondition Failed).
        :keyword lease:
            Required if the blob has an active lease. Value can be a BlobLeaseClient object
            or the lease ID as a string.
        :paramtype lease: ~azure.storage.blob.BlobLeaseClient or str
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
        :keyword str if_tags_match_condition:
            Specify a SQL where clause on blob tags to operate only on blob with a matching value.
            eg. ``"\\"tagname\\"=\'my tag\'"``

            .. versionadded:: 12.4.0

        :keyword str encoding:
            Defaults to UTF-8.
        :keyword ~azure.storage.blob.CustomerProvidedEncryptionKey cpk:
            Encrypts the data on the service-side with the given key.
            Use of customer-provided keys must be done over HTTPS.
            As the encryption key itself is provided in the request,
            a secure connection must be established to transfer the key.
        :keyword str encryption_scope:
            A predefined encryption scope used to encrypt the data on the service. An encryption
            scope can be created using the Management API and referenced here by name. If a default
            encryption scope has been defined at the container, this value will override it if the
            container-level scope is configured to allow overrides. Otherwise an error will be raised.

            .. versionadded:: 12.2.0

        :keyword int timeout:
            Sets the server-side timeout for the operation in seconds. For more details see
            https://learn.microsoft.com/rest/api/storageservices/setting-timeouts-for-blob-service-operations.
            This value is not tracked or validated on the client. To configure client-side network timesouts
            see `here <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob
            #other-client--per-operation-configuration>`_.
        :returns: Blob-updated property dict (Etag, last modified, append offset, committed block count).
        :rtype: dict(str, Any)
        '''
    def append_block_from_url(self, copy_source_url: str, source_offset: int | None = None, source_length: int | None = None, **kwargs) -> Dict[str, str | datetime | int]:
        '''
        Creates a new block to be committed as part of a blob, where the contents are read from a source url.

        :param str copy_source_url:
            The URL of the source data. It can point to any Azure Blob or File, that is either public or has a
            shared access signature attached.
        :param int source_offset:
            This indicates the start of the range of bytes (inclusive) that has to be taken from the copy source.
        :param int source_length:
            This indicates the end of the range of bytes that has to be taken from the copy source.
        :keyword bytearray source_content_md5:
            If given, the service will calculate the MD5 hash of the block content and compare against this value.
        :keyword int maxsize_condition:
            Optional conditional header. The max length in bytes permitted for
            the append blob. If the Append Block operation would cause the blob
            to exceed that limit or if the blob size is already greater than the
            value specified in this header, the request will fail with
            MaxBlobSizeConditionNotMet error (HTTP status code 412 - Precondition Failed).
        :keyword int appendpos_condition:
            Optional conditional header, used only for the Append Block operation.
            A number indicating the byte offset to compare. Append Block will
            succeed only if the append position is equal to this number. If it
            is not, the request will fail with the
            AppendPositionConditionNotMet error
            (HTTP status code 412 - Precondition Failed).
        :keyword lease:
            Required if the blob has an active lease. Value can be a BlobLeaseClient object
            or the lease ID as a string.
        :paramtype lease: ~azure.storage.blob.BlobLeaseClient or str
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
            The destination ETag value, or the wildcard character (*). Used to check if the resource has changed,
            and act according to the condition specified by the `match_condition` parameter.
        :keyword ~azure.core.MatchConditions match_condition:
            The destination match condition to use upon the etag.
        :keyword str if_tags_match_condition:
            Specify a SQL where clause on blob tags to operate only on blob with a matching value.
            eg. ``"\\"tagname\\"=\'my tag\'"``

            .. versionadded:: 12.4.0

        :keyword ~datetime.datetime source_if_modified_since:
            A DateTime value. Azure expects the date value passed in to be UTC.
            If timezone is included, any non-UTC datetimes will be converted to UTC.
            If a date is passed in without timezone info, it is assumed to be UTC.
            Specify this header to perform the operation only
            if the source resource has been modified since the specified time.
        :keyword ~datetime.datetime source_if_unmodified_since:
            A DateTime value. Azure expects the date value passed in to be UTC.
            If timezone is included, any non-UTC datetimes will be converted to UTC.
            If a date is passed in without timezone info, it is assumed to be UTC.
            Specify this header to perform the operation only if
            the source resource has not been modified since the specified date/time.
        :keyword str source_etag:
            The source ETag value, or the wildcard character (*). Used to check if the resource has changed,
            and act according to the condition specified by the `match_condition` parameter.
        :keyword ~azure.core.MatchConditions source_match_condition:
            The source match condition to use upon the etag.
        :keyword ~azure.storage.blob.CustomerProvidedEncryptionKey cpk:
            Encrypts the data on the service-side with the given key.
            Use of customer-provided keys must be done over HTTPS.
            As the encryption key itself is provided in the request,
            a secure connection must be established to transfer the key.
        :keyword str encryption_scope:
            A predefined encryption scope used to encrypt the data on the service. An encryption
            scope can be created using the Management API and referenced here by name. If a default
            encryption scope has been defined at the container, this value will override it if the
            container-level scope is configured to allow overrides. Otherwise an error will be raised.

            .. versionadded:: 12.2.0

        :keyword int timeout:
            Sets the server-side timeout for the operation in seconds. For more details see
            https://learn.microsoft.com/rest/api/storageservices/setting-timeouts-for-blob-service-operations.
            This value is not tracked or validated on the client. To configure client-side network timesouts
            see `here <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob
            #other-client--per-operation-configuration>`_.
        :keyword str source_authorization:
            Authenticate as a service principal using a client secret to access a source blob. Ensure "bearer " is
            the prefix of the source_authorization string.
        '''
    def seal_append_blob(self, **kwargs) -> Dict[str, str | datetime | int]:
        """The Seal operation seals the Append Blob to make it read-only.

            .. versionadded:: 12.4.0

        :keyword int appendpos_condition:
            Optional conditional header, used only for the Append Block operation.
            A number indicating the byte offset to compare. Append Block will
            succeed only if the append position is equal to this number. If it
            is not, the request will fail with the AppendPositionConditionNotMet error
            (HTTP status code 412 - Precondition Failed).
        :keyword lease:
            Required if the blob has an active lease. Value can be a BlobLeaseClient object
            or the lease ID as a string.
        :paramtype lease: ~azure.storage.blob.BlobLeaseClient or str
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
        :returns: Blob-updated property dict (Etag, last modified, append offset, committed block count).
        :rtype: dict(str, Any)
        """
