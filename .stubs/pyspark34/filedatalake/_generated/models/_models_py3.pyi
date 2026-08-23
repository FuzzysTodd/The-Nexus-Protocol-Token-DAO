import datetime
from .. import _serialization, models as _models
from _typeshed import Incomplete
from typing import Any, List, Literal

class AclFailedEntry(_serialization.Model):
    """AclFailedEntry.

    :ivar name:
    :vartype name: str
    :ivar type:
    :vartype type: str
    :ivar error_message:
    :vartype error_message: str
    """
    name: Incomplete
    type: Incomplete
    error_message: Incomplete
    def __init__(self, *, name: str | None = None, type: str | None = None, error_message: str | None = None, **kwargs: Any) -> None:
        """
        :keyword name:
        :paramtype name: str
        :keyword type:
        :paramtype type: str
        :keyword error_message:
        :paramtype error_message: str
        """

class BlobHierarchyListSegment(_serialization.Model):
    """BlobHierarchyListSegment.

    All required parameters must be populated in order to send to Azure.

    :ivar blob_prefixes:
    :vartype blob_prefixes: list[~azure.storage.filedatalake.models.BlobPrefix]
    :ivar blob_items: Required.
    :vartype blob_items: list[~azure.storage.filedatalake.models.BlobItemInternal]
    """
    blob_prefixes: Incomplete
    blob_items: Incomplete
    def __init__(self, *, blob_items: List['_models.BlobItemInternal'], blob_prefixes: List['_models.BlobPrefix'] | None = None, **kwargs: Any) -> None:
        """
        :keyword blob_prefixes:
        :paramtype blob_prefixes: list[~azure.storage.filedatalake.models.BlobPrefix]
        :keyword blob_items: Required.
        :paramtype blob_items: list[~azure.storage.filedatalake.models.BlobItemInternal]
        """

class BlobItemInternal(_serialization.Model):
    """An Azure Storage blob.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Required.
    :vartype name: str
    :ivar deleted: Required.
    :vartype deleted: bool
    :ivar snapshot: Required.
    :vartype snapshot: str
    :ivar version_id:
    :vartype version_id: str
    :ivar is_current_version:
    :vartype is_current_version: bool
    :ivar properties: Properties of a blob. Required.
    :vartype properties: ~azure.storage.filedatalake.models.BlobPropertiesInternal
    :ivar deletion_id:
    :vartype deletion_id: str
    """
    name: Incomplete
    deleted: Incomplete
    snapshot: Incomplete
    version_id: Incomplete
    is_current_version: Incomplete
    properties: Incomplete
    deletion_id: Incomplete
    def __init__(self, *, name: str, deleted: bool, snapshot: str, properties: _models.BlobPropertiesInternal, version_id: str | None = None, is_current_version: bool | None = None, deletion_id: str | None = None, **kwargs: Any) -> None:
        """
        :keyword name: Required.
        :paramtype name: str
        :keyword deleted: Required.
        :paramtype deleted: bool
        :keyword snapshot: Required.
        :paramtype snapshot: str
        :keyword version_id:
        :paramtype version_id: str
        :keyword is_current_version:
        :paramtype is_current_version: bool
        :keyword properties: Properties of a blob. Required.
        :paramtype properties: ~azure.storage.filedatalake.models.BlobPropertiesInternal
        :keyword deletion_id:
        :paramtype deletion_id: str
        """

class BlobPrefix(_serialization.Model):
    """BlobPrefix.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Required.
    :vartype name: str
    """
    name: Incomplete
    def __init__(self, *, name: str, **kwargs: Any) -> None:
        """
        :keyword name: Required.
        :paramtype name: str
        """

class BlobPropertiesInternal(_serialization.Model):
    """Properties of a blob.

    All required parameters must be populated in order to send to Azure.

    :ivar creation_time:
    :vartype creation_time: ~datetime.datetime
    :ivar last_modified: Required.
    :vartype last_modified: ~datetime.datetime
    :ivar etag: Required.
    :vartype etag: str
    :ivar content_length: Size in bytes.
    :vartype content_length: int
    :ivar content_type:
    :vartype content_type: str
    :ivar content_encoding:
    :vartype content_encoding: str
    :ivar content_language:
    :vartype content_language: str
    :ivar content_md5:
    :vartype content_md5: bytes
    :ivar content_disposition:
    :vartype content_disposition: str
    :ivar cache_control:
    :vartype cache_control: str
    :ivar blob_sequence_number:
    :vartype blob_sequence_number: int
    :ivar copy_id:
    :vartype copy_id: str
    :ivar copy_source:
    :vartype copy_source: str
    :ivar copy_progress:
    :vartype copy_progress: str
    :ivar copy_completion_time:
    :vartype copy_completion_time: ~datetime.datetime
    :ivar copy_status_description:
    :vartype copy_status_description: str
    :ivar server_encrypted:
    :vartype server_encrypted: bool
    :ivar incremental_copy:
    :vartype incremental_copy: bool
    :ivar destination_snapshot:
    :vartype destination_snapshot: str
    :ivar deleted_time:
    :vartype deleted_time: ~datetime.datetime
    :ivar remaining_retention_days:
    :vartype remaining_retention_days: int
    :ivar access_tier_inferred:
    :vartype access_tier_inferred: bool
    :ivar customer_provided_key_sha256:
    :vartype customer_provided_key_sha256: str
    :ivar encryption_scope: The name of the encryption scope under which the blob is encrypted.
    :vartype encryption_scope: str
    :ivar access_tier_change_time:
    :vartype access_tier_change_time: ~datetime.datetime
    :ivar tag_count:
    :vartype tag_count: int
    :ivar expires_on:
    :vartype expires_on: ~datetime.datetime
    :ivar is_sealed:
    :vartype is_sealed: bool
    :ivar last_accessed_on:
    :vartype last_accessed_on: ~datetime.datetime
    :ivar delete_time:
    :vartype delete_time: ~datetime.datetime
    """
    creation_time: Incomplete
    last_modified: Incomplete
    etag: Incomplete
    content_length: Incomplete
    content_type: Incomplete
    content_encoding: Incomplete
    content_language: Incomplete
    content_md5: Incomplete
    content_disposition: Incomplete
    cache_control: Incomplete
    blob_sequence_number: Incomplete
    copy_id: Incomplete
    copy_source: Incomplete
    copy_progress: Incomplete
    copy_completion_time: Incomplete
    copy_status_description: Incomplete
    server_encrypted: Incomplete
    incremental_copy: Incomplete
    destination_snapshot: Incomplete
    deleted_time: Incomplete
    remaining_retention_days: Incomplete
    access_tier_inferred: Incomplete
    customer_provided_key_sha256: Incomplete
    encryption_scope: Incomplete
    access_tier_change_time: Incomplete
    tag_count: Incomplete
    expires_on: Incomplete
    is_sealed: Incomplete
    last_accessed_on: Incomplete
    delete_time: Incomplete
    def __init__(self, *, last_modified: datetime.datetime, etag: str, creation_time: datetime.datetime | None = None, content_length: int | None = None, content_type: str | None = None, content_encoding: str | None = None, content_language: str | None = None, content_md5: bytes | None = None, content_disposition: str | None = None, cache_control: str | None = None, blob_sequence_number: int | None = None, copy_id: str | None = None, copy_source: str | None = None, copy_progress: str | None = None, copy_completion_time: datetime.datetime | None = None, copy_status_description: str | None = None, server_encrypted: bool | None = None, incremental_copy: bool | None = None, destination_snapshot: str | None = None, deleted_time: datetime.datetime | None = None, remaining_retention_days: int | None = None, access_tier_inferred: bool | None = None, customer_provided_key_sha256: str | None = None, encryption_scope: str | None = None, access_tier_change_time: datetime.datetime | None = None, tag_count: int | None = None, expires_on: datetime.datetime | None = None, is_sealed: bool | None = None, last_accessed_on: datetime.datetime | None = None, delete_time: datetime.datetime | None = None, **kwargs: Any) -> None:
        """
        :keyword creation_time:
        :paramtype creation_time: ~datetime.datetime
        :keyword last_modified: Required.
        :paramtype last_modified: ~datetime.datetime
        :keyword etag: Required.
        :paramtype etag: str
        :keyword content_length: Size in bytes.
        :paramtype content_length: int
        :keyword content_type:
        :paramtype content_type: str
        :keyword content_encoding:
        :paramtype content_encoding: str
        :keyword content_language:
        :paramtype content_language: str
        :keyword content_md5:
        :paramtype content_md5: bytes
        :keyword content_disposition:
        :paramtype content_disposition: str
        :keyword cache_control:
        :paramtype cache_control: str
        :keyword blob_sequence_number:
        :paramtype blob_sequence_number: int
        :keyword copy_id:
        :paramtype copy_id: str
        :keyword copy_source:
        :paramtype copy_source: str
        :keyword copy_progress:
        :paramtype copy_progress: str
        :keyword copy_completion_time:
        :paramtype copy_completion_time: ~datetime.datetime
        :keyword copy_status_description:
        :paramtype copy_status_description: str
        :keyword server_encrypted:
        :paramtype server_encrypted: bool
        :keyword incremental_copy:
        :paramtype incremental_copy: bool
        :keyword destination_snapshot:
        :paramtype destination_snapshot: str
        :keyword deleted_time:
        :paramtype deleted_time: ~datetime.datetime
        :keyword remaining_retention_days:
        :paramtype remaining_retention_days: int
        :keyword access_tier_inferred:
        :paramtype access_tier_inferred: bool
        :keyword customer_provided_key_sha256:
        :paramtype customer_provided_key_sha256: str
        :keyword encryption_scope: The name of the encryption scope under which the blob is encrypted.
        :paramtype encryption_scope: str
        :keyword access_tier_change_time:
        :paramtype access_tier_change_time: ~datetime.datetime
        :keyword tag_count:
        :paramtype tag_count: int
        :keyword expires_on:
        :paramtype expires_on: ~datetime.datetime
        :keyword is_sealed:
        :paramtype is_sealed: bool
        :keyword last_accessed_on:
        :paramtype last_accessed_on: ~datetime.datetime
        :keyword delete_time:
        :paramtype delete_time: ~datetime.datetime
        """

class CpkInfo(_serialization.Model):
    '''Parameter group.

    :ivar encryption_key: Optional. Specifies the encryption key to use to encrypt the data
     provided in the request. If not specified, encryption is performed with the root account
     encryption key.  For more information, see Encryption at Rest for Azure Storage Services.
    :vartype encryption_key: str
    :ivar encryption_key_sha256: The SHA-256 hash of the provided encryption key. Must be provided
     if the x-ms-encryption-key header is provided.
    :vartype encryption_key_sha256: str
    :ivar encryption_algorithm: The algorithm used to produce the encryption key hash. Currently,
     the only accepted value is "AES256". Must be provided if the x-ms-encryption-key header is
     provided. Default value is "AES256".
    :vartype encryption_algorithm: str
    '''
    encryption_key: Incomplete
    encryption_key_sha256: Incomplete
    encryption_algorithm: Incomplete
    def __init__(self, *, encryption_key: str | None = None, encryption_key_sha256: str | None = None, encryption_algorithm: Literal['AES256'] | None = None, **kwargs: Any) -> None:
        '''
        :keyword encryption_key: Optional. Specifies the encryption key to use to encrypt the data
         provided in the request. If not specified, encryption is performed with the root account
         encryption key.  For more information, see Encryption at Rest for Azure Storage Services.
        :paramtype encryption_key: str
        :keyword encryption_key_sha256: The SHA-256 hash of the provided encryption key. Must be
         provided if the x-ms-encryption-key header is provided.
        :paramtype encryption_key_sha256: str
        :keyword encryption_algorithm: The algorithm used to produce the encryption key hash.
         Currently, the only accepted value is "AES256". Must be provided if the x-ms-encryption-key
         header is provided. Default value is "AES256".
        :paramtype encryption_algorithm: str
        '''

class FileSystem(_serialization.Model):
    """FileSystem.

    :ivar name:
    :vartype name: str
    :ivar last_modified:
    :vartype last_modified: str
    :ivar e_tag:
    :vartype e_tag: str
    """
    name: Incomplete
    last_modified: Incomplete
    e_tag: Incomplete
    def __init__(self, *, name: str | None = None, last_modified: str | None = None, e_tag: str | None = None, **kwargs: Any) -> None:
        """
        :keyword name:
        :paramtype name: str
        :keyword last_modified:
        :paramtype last_modified: str
        :keyword e_tag:
        :paramtype e_tag: str
        """

class FileSystemList(_serialization.Model):
    """FileSystemList.

    :ivar filesystems:
    :vartype filesystems: list[~azure.storage.filedatalake.models.FileSystem]
    """
    filesystems: Incomplete
    def __init__(self, *, filesystems: List['_models.FileSystem'] | None = None, **kwargs: Any) -> None:
        """
        :keyword filesystems:
        :paramtype filesystems: list[~azure.storage.filedatalake.models.FileSystem]
        """

class LeaseAccessConditions(_serialization.Model):
    """Parameter group.

    :ivar lease_id: If specified, the operation only succeeds if the resource's lease is active and
     matches this ID.
    :vartype lease_id: str
    """
    lease_id: Incomplete
    def __init__(self, *, lease_id: str | None = None, **kwargs: Any) -> None:
        """
        :keyword lease_id: If specified, the operation only succeeds if the resource's lease is active
         and matches this ID.
        :paramtype lease_id: str
        """

class ListBlobsHierarchySegmentResponse(_serialization.Model):
    """An enumeration of blobs.

    All required parameters must be populated in order to send to Azure.

    :ivar service_endpoint: Required.
    :vartype service_endpoint: str
    :ivar container_name: Required.
    :vartype container_name: str
    :ivar prefix:
    :vartype prefix: str
    :ivar marker:
    :vartype marker: str
    :ivar max_results:
    :vartype max_results: int
    :ivar delimiter:
    :vartype delimiter: str
    :ivar segment: Required.
    :vartype segment: ~azure.storage.filedatalake.models.BlobHierarchyListSegment
    :ivar next_marker:
    :vartype next_marker: str
    """
    service_endpoint: Incomplete
    container_name: Incomplete
    prefix: Incomplete
    marker: Incomplete
    max_results: Incomplete
    delimiter: Incomplete
    segment: Incomplete
    next_marker: Incomplete
    def __init__(self, *, service_endpoint: str, container_name: str, segment: _models.BlobHierarchyListSegment, prefix: str | None = None, marker: str | None = None, max_results: int | None = None, delimiter: str | None = None, next_marker: str | None = None, **kwargs: Any) -> None:
        """
        :keyword service_endpoint: Required.
        :paramtype service_endpoint: str
        :keyword container_name: Required.
        :paramtype container_name: str
        :keyword prefix:
        :paramtype prefix: str
        :keyword marker:
        :paramtype marker: str
        :keyword max_results:
        :paramtype max_results: int
        :keyword delimiter:
        :paramtype delimiter: str
        :keyword segment: Required.
        :paramtype segment: ~azure.storage.filedatalake.models.BlobHierarchyListSegment
        :keyword next_marker:
        :paramtype next_marker: str
        """

class ModifiedAccessConditions(_serialization.Model):
    """Parameter group.

    :ivar if_modified_since: Specify this header value to operate only on a blob if it has been
     modified since the specified date/time.
    :vartype if_modified_since: ~datetime.datetime
    :ivar if_unmodified_since: Specify this header value to operate only on a blob if it has not
     been modified since the specified date/time.
    :vartype if_unmodified_since: ~datetime.datetime
    :ivar if_match: Specify an ETag value to operate only on blobs with a matching value.
    :vartype if_match: str
    :ivar if_none_match: Specify an ETag value to operate only on blobs without a matching value.
    :vartype if_none_match: str
    """
    if_modified_since: Incomplete
    if_unmodified_since: Incomplete
    if_match: Incomplete
    if_none_match: Incomplete
    def __init__(self, *, if_modified_since: datetime.datetime | None = None, if_unmodified_since: datetime.datetime | None = None, if_match: str | None = None, if_none_match: str | None = None, **kwargs: Any) -> None:
        """
        :keyword if_modified_since: Specify this header value to operate only on a blob if it has been
         modified since the specified date/time.
        :paramtype if_modified_since: ~datetime.datetime
        :keyword if_unmodified_since: Specify this header value to operate only on a blob if it has not
         been modified since the specified date/time.
        :paramtype if_unmodified_since: ~datetime.datetime
        :keyword if_match: Specify an ETag value to operate only on blobs with a matching value.
        :paramtype if_match: str
        :keyword if_none_match: Specify an ETag value to operate only on blobs without a matching
         value.
        :paramtype if_none_match: str
        """

class Path(_serialization.Model):
    """Path.

    :ivar name:
    :vartype name: str
    :ivar is_directory:
    :vartype is_directory: bool
    :ivar last_modified:
    :vartype last_modified: str
    :ivar e_tag:
    :vartype e_tag: str
    :ivar content_length:
    :vartype content_length: int
    :ivar owner:
    :vartype owner: str
    :ivar group:
    :vartype group: str
    :ivar permissions:
    :vartype permissions: str
    :ivar encryption_scope: The name of the encryption scope under which the blob is encrypted.
    :vartype encryption_scope: str
    :ivar creation_time:
    :vartype creation_time: str
    :ivar expiry_time:
    :vartype expiry_time: str
    :ivar encryption_context:
    :vartype encryption_context: str
    """
    name: Incomplete
    is_directory: Incomplete
    last_modified: Incomplete
    e_tag: Incomplete
    content_length: Incomplete
    owner: Incomplete
    group: Incomplete
    permissions: Incomplete
    encryption_scope: Incomplete
    creation_time: Incomplete
    expiry_time: Incomplete
    encryption_context: Incomplete
    def __init__(self, *, name: str | None = None, is_directory: bool = False, last_modified: str | None = None, e_tag: str | None = None, content_length: int | None = None, owner: str | None = None, group: str | None = None, permissions: str | None = None, encryption_scope: str | None = None, creation_time: str | None = None, expiry_time: str | None = None, encryption_context: str | None = None, **kwargs: Any) -> None:
        """
        :keyword name:
        :paramtype name: str
        :keyword is_directory:
        :paramtype is_directory: bool
        :keyword last_modified:
        :paramtype last_modified: str
        :keyword e_tag:
        :paramtype e_tag: str
        :keyword content_length:
        :paramtype content_length: int
        :keyword owner:
        :paramtype owner: str
        :keyword group:
        :paramtype group: str
        :keyword permissions:
        :paramtype permissions: str
        :keyword encryption_scope: The name of the encryption scope under which the blob is encrypted.
        :paramtype encryption_scope: str
        :keyword creation_time:
        :paramtype creation_time: str
        :keyword expiry_time:
        :paramtype expiry_time: str
        :keyword encryption_context:
        :paramtype encryption_context: str
        """

class PathHTTPHeaders(_serialization.Model):
    """Parameter group.

    :ivar cache_control: Optional. Sets the blob's cache control. If specified, this property is
     stored with the blob and returned with a read request.
    :vartype cache_control: str
    :ivar content_encoding: Optional. Sets the blob's content encoding. If specified, this property
     is stored with the blob and returned with a read request.
    :vartype content_encoding: str
    :ivar content_language: Optional. Set the blob's content language. If specified, this property
     is stored with the blob and returned with a read request.
    :vartype content_language: str
    :ivar content_disposition: Optional. Sets the blob's Content-Disposition header.
    :vartype content_disposition: str
    :ivar content_type: Optional. Sets the blob's content type. If specified, this property is
     stored with the blob and returned with a read request.
    :vartype content_type: str
    :ivar content_md5: Specify the transactional md5 for the body, to be validated by the service.
    :vartype content_md5: bytes
    :ivar transactional_content_hash: Specify the transactional md5 for the body, to be validated
     by the service.
    :vartype transactional_content_hash: bytes
    """
    cache_control: Incomplete
    content_encoding: Incomplete
    content_language: Incomplete
    content_disposition: Incomplete
    content_type: Incomplete
    content_md5: Incomplete
    transactional_content_hash: Incomplete
    def __init__(self, *, cache_control: str | None = None, content_encoding: str | None = None, content_language: str | None = None, content_disposition: str | None = None, content_type: str | None = None, content_md5: bytes | None = None, transactional_content_hash: bytes | None = None, **kwargs: Any) -> None:
        """
        :keyword cache_control: Optional. Sets the blob's cache control. If specified, this property is
         stored with the blob and returned with a read request.
        :paramtype cache_control: str
        :keyword content_encoding: Optional. Sets the blob's content encoding. If specified, this
         property is stored with the blob and returned with a read request.
        :paramtype content_encoding: str
        :keyword content_language: Optional. Set the blob's content language. If specified, this
         property is stored with the blob and returned with a read request.
        :paramtype content_language: str
        :keyword content_disposition: Optional. Sets the blob's Content-Disposition header.
        :paramtype content_disposition: str
        :keyword content_type: Optional. Sets the blob's content type. If specified, this property is
         stored with the blob and returned with a read request.
        :paramtype content_type: str
        :keyword content_md5: Specify the transactional md5 for the body, to be validated by the
         service.
        :paramtype content_md5: bytes
        :keyword transactional_content_hash: Specify the transactional md5 for the body, to be
         validated by the service.
        :paramtype transactional_content_hash: bytes
        """

class PathList(_serialization.Model):
    """PathList.

    :ivar paths:
    :vartype paths: list[~azure.storage.filedatalake.models.Path]
    """
    paths: Incomplete
    def __init__(self, *, paths: List['_models.Path'] | None = None, **kwargs: Any) -> None:
        """
        :keyword paths:
        :paramtype paths: list[~azure.storage.filedatalake.models.Path]
        """

class SetAccessControlRecursiveResponse(_serialization.Model):
    """SetAccessControlRecursiveResponse.

    :ivar directories_successful:
    :vartype directories_successful: int
    :ivar files_successful:
    :vartype files_successful: int
    :ivar failure_count:
    :vartype failure_count: int
    :ivar failed_entries:
    :vartype failed_entries: list[~azure.storage.filedatalake.models.AclFailedEntry]
    """
    directories_successful: Incomplete
    files_successful: Incomplete
    failure_count: Incomplete
    failed_entries: Incomplete
    def __init__(self, *, directories_successful: int | None = None, files_successful: int | None = None, failure_count: int | None = None, failed_entries: List['_models.AclFailedEntry'] | None = None, **kwargs: Any) -> None:
        """
        :keyword directories_successful:
        :paramtype directories_successful: int
        :keyword files_successful:
        :paramtype files_successful: int
        :keyword failure_count:
        :paramtype failure_count: int
        :keyword failed_entries:
        :paramtype failed_entries: list[~azure.storage.filedatalake.models.AclFailedEntry]
        """

class SourceModifiedAccessConditions(_serialization.Model):
    """Parameter group.

    :ivar source_if_match: Specify an ETag value to operate only on blobs with a matching value.
    :vartype source_if_match: str
    :ivar source_if_none_match: Specify an ETag value to operate only on blobs without a matching
     value.
    :vartype source_if_none_match: str
    :ivar source_if_modified_since: Specify this header value to operate only on a blob if it has
     been modified since the specified date/time.
    :vartype source_if_modified_since: ~datetime.datetime
    :ivar source_if_unmodified_since: Specify this header value to operate only on a blob if it has
     not been modified since the specified date/time.
    :vartype source_if_unmodified_since: ~datetime.datetime
    """
    source_if_match: Incomplete
    source_if_none_match: Incomplete
    source_if_modified_since: Incomplete
    source_if_unmodified_since: Incomplete
    def __init__(self, *, source_if_match: str | None = None, source_if_none_match: str | None = None, source_if_modified_since: datetime.datetime | None = None, source_if_unmodified_since: datetime.datetime | None = None, **kwargs: Any) -> None:
        """
        :keyword source_if_match: Specify an ETag value to operate only on blobs with a matching value.
        :paramtype source_if_match: str
        :keyword source_if_none_match: Specify an ETag value to operate only on blobs without a
         matching value.
        :paramtype source_if_none_match: str
        :keyword source_if_modified_since: Specify this header value to operate only on a blob if it
         has been modified since the specified date/time.
        :paramtype source_if_modified_since: ~datetime.datetime
        :keyword source_if_unmodified_since: Specify this header value to operate only on a blob if it
         has not been modified since the specified date/time.
        :paramtype source_if_unmodified_since: ~datetime.datetime
        """

class StorageError(_serialization.Model):
    """StorageError.

    :ivar error: The service error response object.
    :vartype error: ~azure.storage.filedatalake.models.StorageErrorError
    """
    error: Incomplete
    def __init__(self, *, error: _models.StorageErrorError | None = None, **kwargs: Any) -> None:
        """
        :keyword error: The service error response object.
        :paramtype error: ~azure.storage.filedatalake.models.StorageErrorError
        """

class StorageErrorError(_serialization.Model):
    """The service error response object.

    :ivar code: The service error code.
    :vartype code: str
    :ivar message: The service error message.
    :vartype message: str
    """
    code: Incomplete
    message: Incomplete
    def __init__(self, *, code: str | None = None, message: str | None = None, **kwargs: Any) -> None:
        """
        :keyword code: The service error code.
        :paramtype code: str
        :keyword message: The service error message.
        :paramtype message: str
        """
