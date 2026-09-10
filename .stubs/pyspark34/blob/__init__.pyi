from ._blob_client import BlobClient as BlobClient
from ._blob_service_client import BlobServiceClient as BlobServiceClient
from ._container_client import ContainerClient as ContainerClient
from ._download import StorageStreamDownloader as StorageStreamDownloader
from ._generated.models import RehydratePriority as RehydratePriority
from ._lease import BlobLeaseClient as BlobLeaseClient
from ._list_blobs_helper import BlobPrefix as BlobPrefix
from ._models import AccessPolicy as AccessPolicy, ArrowDialect as ArrowDialect, ArrowType as ArrowType, BlobAnalyticsLogging as BlobAnalyticsLogging, BlobBlock as BlobBlock, BlobImmutabilityPolicyMode as BlobImmutabilityPolicyMode, BlobProperties as BlobProperties, BlobQueryError as BlobQueryError, BlobSasPermissions as BlobSasPermissions, BlobType as BlobType, BlockState as BlockState, ContainerEncryptionScope as ContainerEncryptionScope, ContainerProperties as ContainerProperties, ContainerSasPermissions as ContainerSasPermissions, ContentSettings as ContentSettings, CopyProperties as CopyProperties, CorsRule as CorsRule, CustomerProvidedEncryptionKey as CustomerProvidedEncryptionKey, DelimitedJsonDialect as DelimitedJsonDialect, DelimitedTextDialect as DelimitedTextDialect, FilteredBlob as FilteredBlob, ImmutabilityPolicy as ImmutabilityPolicy, LeaseProperties as LeaseProperties, Metrics as Metrics, ObjectReplicationPolicy as ObjectReplicationPolicy, ObjectReplicationRule as ObjectReplicationRule, PageRange as PageRange, PremiumPageBlobTier as PremiumPageBlobTier, PublicAccess as PublicAccess, QuickQueryDialect as QuickQueryDialect, RetentionPolicy as RetentionPolicy, SequenceNumberAction as SequenceNumberAction, StandardBlobTier as StandardBlobTier, StaticWebsite as StaticWebsite
from ._quick_query_helper import BlobQueryReader as BlobQueryReader
from ._shared.models import AccountSasPermissions as AccountSasPermissions, LocationMode as LocationMode, ResourceTypes as ResourceTypes, StorageErrorCode as StorageErrorCode, UserDelegationKey as UserDelegationKey
from ._shared.policies import ExponentialRetry as ExponentialRetry, LinearRetry as LinearRetry
from ._shared.response_handlers import PartialBatchErrorException as PartialBatchErrorException
from ._shared_access_signature import generate_account_sas as generate_account_sas, generate_blob_sas as generate_blob_sas, generate_container_sas as generate_container_sas
from ._version import VERSION
from typing import Any, AnyStr, Dict, IO, Iterable

__all__ = ['upload_blob_to_url', 'download_blob_from_url', 'BlobServiceClient', 'ContainerClient', 'BlobClient', 'BlobType', 'BlobLeaseClient', 'StorageErrorCode', 'UserDelegationKey', 'ExponentialRetry', 'LinearRetry', 'LocationMode', 'BlockState', 'StandardBlobTier', 'PremiumPageBlobTier', 'SequenceNumberAction', 'BlobImmutabilityPolicyMode', 'ImmutabilityPolicy', 'PublicAccess', 'BlobAnalyticsLogging', 'Metrics', 'RetentionPolicy', 'StaticWebsite', 'CorsRule', 'ContainerProperties', 'BlobProperties', 'BlobPrefix', 'FilteredBlob', 'LeaseProperties', 'ContentSettings', 'CopyProperties', 'BlobBlock', 'PageRange', 'AccessPolicy', 'QuickQueryDialect', 'ContainerSasPermissions', 'BlobSasPermissions', 'ResourceTypes', 'AccountSasPermissions', 'StorageStreamDownloader', 'CustomerProvidedEncryptionKey', 'RehydratePriority', 'generate_account_sas', 'generate_container_sas', 'generate_blob_sas', 'PartialBatchErrorException', 'ContainerEncryptionScope', 'BlobQueryError', 'DelimitedJsonDialect', 'DelimitedTextDialect', 'ArrowDialect', 'ArrowType', 'BlobQueryReader', 'ObjectReplicationPolicy', 'ObjectReplicationRule']

__version__ = VERSION

def upload_blob_to_url(blob_url: str, data: Iterable[AnyStr] | IO[AnyStr], credential: Optional[str | Dict[str, str] | AzureNamedKeyCredential | AzureSasCredential | TokenCredential] = None, **kwargs) -> Dict[str, Any]:
    '''Upload data to a given URL

    The data will be uploaded as a block blob.

    :param str blob_url:
        The full URI to the blob. This can also include a SAS token.
    :param data:
        The data to upload. This can be bytes, text, an iterable or a file-like object.
    :type data: bytes or str or Iterable
    :param credential:
        The credentials with which to authenticate. This is optional if the
        blob URL already has a SAS token. The value can be a SAS token string,
        an instance of a AzureSasCredential or AzureNamedKeyCredential from azure.core.credentials,
        an account shared access key, or an instance of a TokenCredentials class from azure.identity.
        If the resource URI already contains a SAS token, this will be ignored in favor of an explicit credential
        - except in the case of AzureSasCredential, where the conflicting SAS tokens will raise a ValueError.
        If using an instance of AzureNamedKeyCredential, "name" should be the storage account name, and "key"
        should be the storage account key.
    :paramtype credential: Optional[Union[str, Dict[str, str], AzureNamedKeyCredential, AzureSasCredential, "TokenCredential"]] # pylint: disable=line-too-long
    :keyword bool overwrite:
        Whether the blob to be uploaded should overwrite the current data.
        If True, upload_blob_to_url will overwrite any existing data. If set to False, the
        operation will fail with a ResourceExistsError.
    :keyword int max_concurrency:
        The number of parallel connections with which to download.
    :keyword int length:
        Number of bytes to read from the stream. This is optional, but
        should be supplied for optimal performance.
    :keyword dict(str,str) metadata:
        Name-value pairs associated with the blob as metadata.
    :keyword bool validate_content:
        If true, calculates an MD5 hash for each chunk of the blob. The storage
        service checks the hash of the content that has arrived with the hash
        that was sent. This is primarily valuable for detecting bitflips on
        the wire if using http instead of https as https (the default) will
        already validate. Note that this MD5 hash is not stored with the
        blob. Also note that if enabled, the memory-efficient upload algorithm
        will not be used, because computing the MD5 hash requires buffering
        entire blocks, and doing so defeats the purpose of the memory-efficient algorithm.
    :keyword str encoding:
        Encoding to use if text is supplied as input. Defaults to UTF-8.
    :returns: Blob-updated property dict (Etag and last modified)
    :rtype: dict(str, Any)
    '''
def download_blob_from_url(blob_url: str, output: str, credential: Optional[str | Dict[str, str] | AzureNamedKeyCredential | AzureSasCredential | TokenCredential] = None, **kwargs) -> None:
    '''Download the contents of a blob to a local file or stream.

    :param str blob_url:
        The full URI to the blob. This can also include a SAS token.
    :param output:
        Where the data should be downloaded to. This could be either a file path to write to,
        or an open IO handle to write to.
    :type output: str or writable stream.
    :param credential:
        The credentials with which to authenticate. This is optional if the
        blob URL already has a SAS token or the blob is public. The value can be a SAS token string,
        an instance of a AzureSasCredential or AzureNamedKeyCredential from azure.core.credentials,
        an account shared access key, or an instance of a TokenCredentials class from azure.identity.
        If the resource URI already contains a SAS token, this will be ignored in favor of an explicit credential
        - except in the case of AzureSasCredential, where the conflicting SAS tokens will raise a ValueError.
        If using an instance of AzureNamedKeyCredential, "name" should be the storage account name, and "key"
        should be the storage account key.
    :paramtype credential: Optional[Union[str, Dict[str, str], AzureNamedKeyCredential, AzureSasCredential, "TokenCredential"]] # pylint: disable=line-too-long
    :keyword bool overwrite:
        Whether the local file should be overwritten if it already exists. The default value is
        `False` - in which case a ValueError will be raised if the file already exists. If set to
        `True`, an attempt will be made to write to the existing file. If a stream handle is passed
        in, this value is ignored.
    :keyword int max_concurrency:
        The number of parallel connections with which to download.
    :keyword int offset:
        Start of byte range to use for downloading a section of the blob.
        Must be set if length is provided.
    :keyword int length:
        Number of bytes to read from the stream. This is optional, but
        should be supplied for optimal performance.
    :keyword bool validate_content:
        If true, calculates an MD5 hash for each chunk of the blob. The storage
        service checks the hash of the content that has arrived with the hash
        that was sent. This is primarily valuable for detecting bitflips on
        the wire if using http instead of https as https (the default) will
        already validate. Note that this MD5 hash is not stored with the
        blob. Also note that if enabled, the memory-efficient upload algorithm
        will not be used, because computing the MD5 hash requires buffering
        entire blocks, and doing so defeats the purpose of the memory-efficient algorithm.
    :rtype: None
    '''
