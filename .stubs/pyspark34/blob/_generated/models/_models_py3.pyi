import datetime
from .. import _serialization, models as _models
from _typeshed import Incomplete
from collections.abc import MutableMapping
from typing import Any, Dict, List

JSON = MutableMapping[str, Any]

class AccessPolicy(_serialization.Model):
    """An Access policy.

    :ivar start: the date-time the policy is active.
    :vartype start: str
    :ivar expiry: the date-time the policy expires.
    :vartype expiry: str
    :ivar permission: the permissions for the acl policy.
    :vartype permission: str
    """
    start: Incomplete
    expiry: Incomplete
    permission: Incomplete
    def __init__(self, *, start: str | None = None, expiry: str | None = None, permission: str | None = None, **kwargs: Any) -> None:
        """
        :keyword start: the date-time the policy is active.
        :paramtype start: str
        :keyword expiry: the date-time the policy expires.
        :paramtype expiry: str
        :keyword permission: the permissions for the acl policy.
        :paramtype permission: str
        """

class AppendPositionAccessConditions(_serialization.Model):
    """Parameter group.

    :ivar max_size: Optional conditional header. The max length in bytes permitted for the append
     blob. If the Append Block operation would cause the blob to exceed that limit or if the blob
     size is already greater than the value specified in this header, the request will fail with
     MaxBlobSizeConditionNotMet error (HTTP status code 412 - Precondition Failed).
    :vartype max_size: int
    :ivar append_position: Optional conditional header, used only for the Append Block operation. A
     number indicating the byte offset to compare. Append Block will succeed only if the append
     position is equal to this number. If it is not, the request will fail with the
     AppendPositionConditionNotMet error (HTTP status code 412 - Precondition Failed).
    :vartype append_position: int
    """
    max_size: Incomplete
    append_position: Incomplete
    def __init__(self, *, max_size: int | None = None, append_position: int | None = None, **kwargs: Any) -> None:
        """
        :keyword max_size: Optional conditional header. The max length in bytes permitted for the
         append blob. If the Append Block operation would cause the blob to exceed that limit or if the
         blob size is already greater than the value specified in this header, the request will fail
         with MaxBlobSizeConditionNotMet error (HTTP status code 412 - Precondition Failed).
        :paramtype max_size: int
        :keyword append_position: Optional conditional header, used only for the Append Block
         operation. A number indicating the byte offset to compare. Append Block will succeed only if
         the append position is equal to this number. If it is not, the request will fail with the
         AppendPositionConditionNotMet error (HTTP status code 412 - Precondition Failed).
        :paramtype append_position: int
        """

class ArrowConfiguration(_serialization.Model):
    """Groups the settings used for formatting the response if the response should be Arrow formatted.

    All required parameters must be populated in order to send to Azure.

    :ivar schema: Required.
    :vartype schema: list[~azure.storage.blob.models.ArrowField]
    """
    schema: Incomplete
    def __init__(self, *, schema: List['_models.ArrowField'], **kwargs: Any) -> None:
        """
        :keyword schema: Required.
        :paramtype schema: list[~azure.storage.blob.models.ArrowField]
        """

class ArrowField(_serialization.Model):
    """Groups settings regarding specific field of an arrow schema.

    All required parameters must be populated in order to send to Azure.

    :ivar type: Required.
    :vartype type: str
    :ivar name:
    :vartype name: str
    :ivar precision:
    :vartype precision: int
    :ivar scale:
    :vartype scale: int
    """
    type: Incomplete
    name: Incomplete
    precision: Incomplete
    scale: Incomplete
    def __init__(self, *, type: str, name: str | None = None, precision: int | None = None, scale: int | None = None, **kwargs: Any) -> None:
        """
        :keyword type: Required.
        :paramtype type: str
        :keyword name:
        :paramtype name: str
        :keyword precision:
        :paramtype precision: int
        :keyword scale:
        :paramtype scale: int
        """

class BlobFlatListSegment(_serialization.Model):
    """BlobFlatListSegment.

    All required parameters must be populated in order to send to Azure.

    :ivar blob_items: Required.
    :vartype blob_items: list[~azure.storage.blob.models.BlobItemInternal]
    """
    blob_items: Incomplete
    def __init__(self, *, blob_items: List['_models.BlobItemInternal'], **kwargs: Any) -> None:
        """
        :keyword blob_items: Required.
        :paramtype blob_items: list[~azure.storage.blob.models.BlobItemInternal]
        """

class BlobHierarchyListSegment(_serialization.Model):
    """BlobHierarchyListSegment.

    All required parameters must be populated in order to send to Azure.

    :ivar blob_prefixes:
    :vartype blob_prefixes: list[~azure.storage.blob.models.BlobPrefix]
    :ivar blob_items: Required.
    :vartype blob_items: list[~azure.storage.blob.models.BlobItemInternal]
    """
    blob_prefixes: Incomplete
    blob_items: Incomplete
    def __init__(self, *, blob_items: List['_models.BlobItemInternal'], blob_prefixes: List['_models.BlobPrefix'] | None = None, **kwargs: Any) -> None:
        """
        :keyword blob_prefixes:
        :paramtype blob_prefixes: list[~azure.storage.blob.models.BlobPrefix]
        :keyword blob_items: Required.
        :paramtype blob_items: list[~azure.storage.blob.models.BlobItemInternal]
        """

class BlobHTTPHeaders(_serialization.Model):
    """Parameter group.

    :ivar blob_cache_control: Optional. Sets the blob's cache control. If specified, this property
     is stored with the blob and returned with a read request.
    :vartype blob_cache_control: str
    :ivar blob_content_type: Optional. Sets the blob's content type. If specified, this property is
     stored with the blob and returned with a read request.
    :vartype blob_content_type: str
    :ivar blob_content_md5: Optional. An MD5 hash of the blob content. Note that this hash is not
     validated, as the hashes for the individual blocks were validated when each was uploaded.
    :vartype blob_content_md5: bytes
    :ivar blob_content_encoding: Optional. Sets the blob's content encoding. If specified, this
     property is stored with the blob and returned with a read request.
    :vartype blob_content_encoding: str
    :ivar blob_content_language: Optional. Set the blob's content language. If specified, this
     property is stored with the blob and returned with a read request.
    :vartype blob_content_language: str
    :ivar blob_content_disposition: Optional. Sets the blob's Content-Disposition header.
    :vartype blob_content_disposition: str
    """
    blob_cache_control: Incomplete
    blob_content_type: Incomplete
    blob_content_md5: Incomplete
    blob_content_encoding: Incomplete
    blob_content_language: Incomplete
    blob_content_disposition: Incomplete
    def __init__(self, *, blob_cache_control: str | None = None, blob_content_type: str | None = None, blob_content_md5: bytes | None = None, blob_content_encoding: str | None = None, blob_content_language: str | None = None, blob_content_disposition: str | None = None, **kwargs: Any) -> None:
        """
        :keyword blob_cache_control: Optional. Sets the blob's cache control. If specified, this
         property is stored with the blob and returned with a read request.
        :paramtype blob_cache_control: str
        :keyword blob_content_type: Optional. Sets the blob's content type. If specified, this property
         is stored with the blob and returned with a read request.
        :paramtype blob_content_type: str
        :keyword blob_content_md5: Optional. An MD5 hash of the blob content. Note that this hash is
         not validated, as the hashes for the individual blocks were validated when each was uploaded.
        :paramtype blob_content_md5: bytes
        :keyword blob_content_encoding: Optional. Sets the blob's content encoding. If specified, this
         property is stored with the blob and returned with a read request.
        :paramtype blob_content_encoding: str
        :keyword blob_content_language: Optional. Set the blob's content language. If specified, this
         property is stored with the blob and returned with a read request.
        :paramtype blob_content_language: str
        :keyword blob_content_disposition: Optional. Sets the blob's Content-Disposition header.
        :paramtype blob_content_disposition: str
        """

class BlobItemInternal(_serialization.Model):
    """An Azure Storage blob.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Required.
    :vartype name: ~azure.storage.blob.models.BlobName
    :ivar deleted: Required.
    :vartype deleted: bool
    :ivar snapshot: Required.
    :vartype snapshot: str
    :ivar version_id:
    :vartype version_id: str
    :ivar is_current_version:
    :vartype is_current_version: bool
    :ivar properties: Properties of a blob. Required.
    :vartype properties: ~azure.storage.blob.models.BlobPropertiesInternal
    :ivar metadata:
    :vartype metadata: ~azure.storage.blob.models.BlobMetadata
    :ivar blob_tags: Blob tags.
    :vartype blob_tags: ~azure.storage.blob.models.BlobTags
    :ivar has_versions_only:
    :vartype has_versions_only: bool
    :ivar object_replication_metadata: Dictionary of :code:`<string>`.
    :vartype object_replication_metadata: dict[str, str]
    """
    name: Incomplete
    deleted: Incomplete
    snapshot: Incomplete
    version_id: Incomplete
    is_current_version: Incomplete
    properties: Incomplete
    metadata: Incomplete
    blob_tags: Incomplete
    has_versions_only: Incomplete
    object_replication_metadata: Incomplete
    def __init__(self, *, name: _models.BlobName, deleted: bool, snapshot: str, properties: _models.BlobPropertiesInternal, version_id: str | None = None, is_current_version: bool | None = None, metadata: _models.BlobMetadata | None = None, blob_tags: _models.BlobTags | None = None, has_versions_only: bool | None = None, object_replication_metadata: Dict[str, str] | None = None, **kwargs: Any) -> None:
        """
        :keyword name: Required.
        :paramtype name: ~azure.storage.blob.models.BlobName
        :keyword deleted: Required.
        :paramtype deleted: bool
        :keyword snapshot: Required.
        :paramtype snapshot: str
        :keyword version_id:
        :paramtype version_id: str
        :keyword is_current_version:
        :paramtype is_current_version: bool
        :keyword properties: Properties of a blob. Required.
        :paramtype properties: ~azure.storage.blob.models.BlobPropertiesInternal
        :keyword metadata:
        :paramtype metadata: ~azure.storage.blob.models.BlobMetadata
        :keyword blob_tags: Blob tags.
        :paramtype blob_tags: ~azure.storage.blob.models.BlobTags
        :keyword has_versions_only:
        :paramtype has_versions_only: bool
        :keyword object_replication_metadata: Dictionary of :code:`<string>`.
        :paramtype object_replication_metadata: dict[str, str]
        """

class BlobMetadata(_serialization.Model):
    """BlobMetadata.

    :ivar additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :vartype additional_properties: dict[str, str]
    :ivar encrypted:
    :vartype encrypted: str
    """
    additional_properties: Incomplete
    encrypted: Incomplete
    def __init__(self, *, additional_properties: Dict[str, str] | None = None, encrypted: str | None = None, **kwargs: Any) -> None:
        """
        :keyword additional_properties: Unmatched properties from the message are deserialized to this
         collection.
        :paramtype additional_properties: dict[str, str]
        :keyword encrypted:
        :paramtype encrypted: str
        """

class BlobName(_serialization.Model):
    """BlobName.

    :ivar encoded: Indicates if the blob name is encoded.
    :vartype encoded: bool
    :ivar content: The name of the blob.
    :vartype content: str
    """
    encoded: Incomplete
    content: Incomplete
    def __init__(self, *, encoded: bool | None = None, content: str | None = None, **kwargs: Any) -> None:
        """
        :keyword encoded: Indicates if the blob name is encoded.
        :paramtype encoded: bool
        :keyword content: The name of the blob.
        :paramtype content: str
        """

class BlobPrefix(_serialization.Model):
    """BlobPrefix.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Required.
    :vartype name: ~azure.storage.blob.models.BlobName
    """
    name: Incomplete
    def __init__(self, *, name: _models.BlobName, **kwargs: Any) -> None:
        """
        :keyword name: Required.
        :paramtype name: ~azure.storage.blob.models.BlobName
        """

class BlobPropertiesInternal(_serialization.Model):
    '''Properties of a blob.

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
    :ivar blob_type: Known values are: "BlockBlob", "PageBlob", and "AppendBlob".
    :vartype blob_type: str or ~azure.storage.blob.models.BlobType
    :ivar lease_status: Known values are: "locked" and "unlocked".
    :vartype lease_status: str or ~azure.storage.blob.models.LeaseStatusType
    :ivar lease_state: Known values are: "available", "leased", "expired", "breaking", and
     "broken".
    :vartype lease_state: str or ~azure.storage.blob.models.LeaseStateType
    :ivar lease_duration: Known values are: "infinite" and "fixed".
    :vartype lease_duration: str or ~azure.storage.blob.models.LeaseDurationType
    :ivar copy_id:
    :vartype copy_id: str
    :ivar copy_status: Known values are: "pending", "success", "aborted", and "failed".
    :vartype copy_status: str or ~azure.storage.blob.models.CopyStatusType
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
    :ivar access_tier: Known values are: "P4", "P6", "P10", "P15", "P20", "P30", "P40", "P50",
     "P60", "P70", "P80", "Hot", "Cool", "Archive", "Premium", and "Cold".
    :vartype access_tier: str or ~azure.storage.blob.models.AccessTier
    :ivar access_tier_inferred:
    :vartype access_tier_inferred: bool
    :ivar archive_status: Known values are: "rehydrate-pending-to-hot",
     "rehydrate-pending-to-cool", and "rehydrate-pending-to-cold".
    :vartype archive_status: str or ~azure.storage.blob.models.ArchiveStatus
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
    :ivar rehydrate_priority: If an object is in rehydrate pending state then this header is
     returned with priority of rehydrate. Valid values are High and Standard. Known values are:
     "High" and "Standard".
    :vartype rehydrate_priority: str or ~azure.storage.blob.models.RehydratePriority
    :ivar last_accessed_on:
    :vartype last_accessed_on: ~datetime.datetime
    :ivar immutability_policy_expires_on:
    :vartype immutability_policy_expires_on: ~datetime.datetime
    :ivar immutability_policy_mode: Known values are: "Mutable", "Unlocked", and "Locked".
    :vartype immutability_policy_mode: str or ~azure.storage.blob.models.BlobImmutabilityPolicyMode
    :ivar legal_hold:
    :vartype legal_hold: bool
    '''
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
    blob_type: Incomplete
    lease_status: Incomplete
    lease_state: Incomplete
    lease_duration: Incomplete
    copy_id: Incomplete
    copy_status: Incomplete
    copy_source: Incomplete
    copy_progress: Incomplete
    copy_completion_time: Incomplete
    copy_status_description: Incomplete
    server_encrypted: Incomplete
    incremental_copy: Incomplete
    destination_snapshot: Incomplete
    deleted_time: Incomplete
    remaining_retention_days: Incomplete
    access_tier: Incomplete
    access_tier_inferred: Incomplete
    archive_status: Incomplete
    customer_provided_key_sha256: Incomplete
    encryption_scope: Incomplete
    access_tier_change_time: Incomplete
    tag_count: Incomplete
    expires_on: Incomplete
    is_sealed: Incomplete
    rehydrate_priority: Incomplete
    last_accessed_on: Incomplete
    immutability_policy_expires_on: Incomplete
    immutability_policy_mode: Incomplete
    legal_hold: Incomplete
    def __init__(self, *, last_modified: datetime.datetime, etag: str, creation_time: datetime.datetime | None = None, content_length: int | None = None, content_type: str | None = None, content_encoding: str | None = None, content_language: str | None = None, content_md5: bytes | None = None, content_disposition: str | None = None, cache_control: str | None = None, blob_sequence_number: int | None = None, blob_type: str | _models.BlobType | None = None, lease_status: str | _models.LeaseStatusType | None = None, lease_state: str | _models.LeaseStateType | None = None, lease_duration: str | _models.LeaseDurationType | None = None, copy_id: str | None = None, copy_status: str | _models.CopyStatusType | None = None, copy_source: str | None = None, copy_progress: str | None = None, copy_completion_time: datetime.datetime | None = None, copy_status_description: str | None = None, server_encrypted: bool | None = None, incremental_copy: bool | None = None, destination_snapshot: str | None = None, deleted_time: datetime.datetime | None = None, remaining_retention_days: int | None = None, access_tier: str | _models.AccessTier | None = None, access_tier_inferred: bool | None = None, archive_status: str | _models.ArchiveStatus | None = None, customer_provided_key_sha256: str | None = None, encryption_scope: str | None = None, access_tier_change_time: datetime.datetime | None = None, tag_count: int | None = None, expires_on: datetime.datetime | None = None, is_sealed: bool | None = None, rehydrate_priority: str | _models.RehydratePriority | None = None, last_accessed_on: datetime.datetime | None = None, immutability_policy_expires_on: datetime.datetime | None = None, immutability_policy_mode: str | _models.BlobImmutabilityPolicyMode | None = None, legal_hold: bool | None = None, **kwargs: Any) -> None:
        '''
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
        :keyword blob_type: Known values are: "BlockBlob", "PageBlob", and "AppendBlob".
        :paramtype blob_type: str or ~azure.storage.blob.models.BlobType
        :keyword lease_status: Known values are: "locked" and "unlocked".
        :paramtype lease_status: str or ~azure.storage.blob.models.LeaseStatusType
        :keyword lease_state: Known values are: "available", "leased", "expired", "breaking", and
         "broken".
        :paramtype lease_state: str or ~azure.storage.blob.models.LeaseStateType
        :keyword lease_duration: Known values are: "infinite" and "fixed".
        :paramtype lease_duration: str or ~azure.storage.blob.models.LeaseDurationType
        :keyword copy_id:
        :paramtype copy_id: str
        :keyword copy_status: Known values are: "pending", "success", "aborted", and "failed".
        :paramtype copy_status: str or ~azure.storage.blob.models.CopyStatusType
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
        :keyword access_tier: Known values are: "P4", "P6", "P10", "P15", "P20", "P30", "P40", "P50",
         "P60", "P70", "P80", "Hot", "Cool", "Archive", "Premium", and "Cold".
        :paramtype access_tier: str or ~azure.storage.blob.models.AccessTier
        :keyword access_tier_inferred:
        :paramtype access_tier_inferred: bool
        :keyword archive_status: Known values are: "rehydrate-pending-to-hot",
         "rehydrate-pending-to-cool", and "rehydrate-pending-to-cold".
        :paramtype archive_status: str or ~azure.storage.blob.models.ArchiveStatus
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
        :keyword rehydrate_priority: If an object is in rehydrate pending state then this header is
         returned with priority of rehydrate. Valid values are High and Standard. Known values are:
         "High" and "Standard".
        :paramtype rehydrate_priority: str or ~azure.storage.blob.models.RehydratePriority
        :keyword last_accessed_on:
        :paramtype last_accessed_on: ~datetime.datetime
        :keyword immutability_policy_expires_on:
        :paramtype immutability_policy_expires_on: ~datetime.datetime
        :keyword immutability_policy_mode: Known values are: "Mutable", "Unlocked", and "Locked".
        :paramtype immutability_policy_mode: str or
         ~azure.storage.blob.models.BlobImmutabilityPolicyMode
        :keyword legal_hold:
        :paramtype legal_hold: bool
        '''

class BlobTag(_serialization.Model):
    """BlobTag.

    All required parameters must be populated in order to send to Azure.

    :ivar key: Required.
    :vartype key: str
    :ivar value: Required.
    :vartype value: str
    """
    key: Incomplete
    value: Incomplete
    def __init__(self, *, key: str, value: str, **kwargs: Any) -> None:
        """
        :keyword key: Required.
        :paramtype key: str
        :keyword value: Required.
        :paramtype value: str
        """

class BlobTags(_serialization.Model):
    """Blob tags.

    All required parameters must be populated in order to send to Azure.

    :ivar blob_tag_set: Required.
    :vartype blob_tag_set: list[~azure.storage.blob.models.BlobTag]
    """
    blob_tag_set: Incomplete
    def __init__(self, *, blob_tag_set: List['_models.BlobTag'], **kwargs: Any) -> None:
        """
        :keyword blob_tag_set: Required.
        :paramtype blob_tag_set: list[~azure.storage.blob.models.BlobTag]
        """

class Block(_serialization.Model):
    """Represents a single block in a block blob.  It describes the block's ID and size.

    All required parameters must be populated in order to send to Azure.

    :ivar name: The base64 encoded block ID. Required.
    :vartype name: str
    :ivar size: The block size in bytes. Required.
    :vartype size: int
    """
    name: Incomplete
    size: Incomplete
    def __init__(self, *, name: str, size: int, **kwargs: Any) -> None:
        """
        :keyword name: The base64 encoded block ID. Required.
        :paramtype name: str
        :keyword size: The block size in bytes. Required.
        :paramtype size: int
        """

class BlockList(_serialization.Model):
    """BlockList.

    :ivar committed_blocks:
    :vartype committed_blocks: list[~azure.storage.blob.models.Block]
    :ivar uncommitted_blocks:
    :vartype uncommitted_blocks: list[~azure.storage.blob.models.Block]
    """
    committed_blocks: Incomplete
    uncommitted_blocks: Incomplete
    def __init__(self, *, committed_blocks: List['_models.Block'] | None = None, uncommitted_blocks: List['_models.Block'] | None = None, **kwargs: Any) -> None:
        """
        :keyword committed_blocks:
        :paramtype committed_blocks: list[~azure.storage.blob.models.Block]
        :keyword uncommitted_blocks:
        :paramtype uncommitted_blocks: list[~azure.storage.blob.models.Block]
        """

class BlockLookupList(_serialization.Model):
    """BlockLookupList.

    :ivar committed:
    :vartype committed: list[str]
    :ivar uncommitted:
    :vartype uncommitted: list[str]
    :ivar latest:
    :vartype latest: list[str]
    """
    committed: Incomplete
    uncommitted: Incomplete
    latest: Incomplete
    def __init__(self, *, committed: List[str] | None = None, uncommitted: List[str] | None = None, latest: List[str] | None = None, **kwargs: Any) -> None:
        """
        :keyword committed:
        :paramtype committed: list[str]
        :keyword uncommitted:
        :paramtype uncommitted: list[str]
        :keyword latest:
        :paramtype latest: list[str]
        """

class ClearRange(_serialization.Model):
    """ClearRange.

    All required parameters must be populated in order to send to Azure.

    :ivar start: Required.
    :vartype start: int
    :ivar end: Required.
    :vartype end: int
    """
    start: Incomplete
    end: Incomplete
    def __init__(self, *, start: int, end: int, **kwargs: Any) -> None:
        """
        :keyword start: Required.
        :paramtype start: int
        :keyword end: Required.
        :paramtype end: int
        """

class ContainerCpkScopeInfo(_serialization.Model):
    """Parameter group.

    :ivar default_encryption_scope: Optional.  Version 2019-07-07 and later.  Specifies the default
     encryption scope to set on the container and use for all future writes.
    :vartype default_encryption_scope: str
    :ivar prevent_encryption_scope_override: Optional.  Version 2019-07-07 and newer.  If true,
     prevents any request from specifying a different encryption scope than the scope set on the
     container.
    :vartype prevent_encryption_scope_override: bool
    """
    default_encryption_scope: Incomplete
    prevent_encryption_scope_override: Incomplete
    def __init__(self, *, default_encryption_scope: str | None = None, prevent_encryption_scope_override: bool | None = None, **kwargs: Any) -> None:
        """
        :keyword default_encryption_scope: Optional.  Version 2019-07-07 and later.  Specifies the
         default encryption scope to set on the container and use for all future writes.
        :paramtype default_encryption_scope: str
        :keyword prevent_encryption_scope_override: Optional.  Version 2019-07-07 and newer.  If true,
         prevents any request from specifying a different encryption scope than the scope set on the
         container.
        :paramtype prevent_encryption_scope_override: bool
        """

class ContainerItem(_serialization.Model):
    """An Azure Storage container.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Required.
    :vartype name: str
    :ivar deleted:
    :vartype deleted: bool
    :ivar version:
    :vartype version: str
    :ivar properties: Properties of a container. Required.
    :vartype properties: ~azure.storage.blob.models.ContainerProperties
    :ivar metadata: Dictionary of :code:`<string>`.
    :vartype metadata: dict[str, str]
    """
    name: Incomplete
    deleted: Incomplete
    version: Incomplete
    properties: Incomplete
    metadata: Incomplete
    def __init__(self, *, name: str, properties: _models.ContainerProperties, deleted: bool | None = None, version: str | None = None, metadata: Dict[str, str] | None = None, **kwargs: Any) -> None:
        """
        :keyword name: Required.
        :paramtype name: str
        :keyword deleted:
        :paramtype deleted: bool
        :keyword version:
        :paramtype version: str
        :keyword properties: Properties of a container. Required.
        :paramtype properties: ~azure.storage.blob.models.ContainerProperties
        :keyword metadata: Dictionary of :code:`<string>`.
        :paramtype metadata: dict[str, str]
        """

class ContainerProperties(_serialization.Model):
    '''Properties of a container.

    All required parameters must be populated in order to send to Azure.

    :ivar last_modified: Required.
    :vartype last_modified: ~datetime.datetime
    :ivar etag: Required.
    :vartype etag: str
    :ivar lease_status: Known values are: "locked" and "unlocked".
    :vartype lease_status: str or ~azure.storage.blob.models.LeaseStatusType
    :ivar lease_state: Known values are: "available", "leased", "expired", "breaking", and
     "broken".
    :vartype lease_state: str or ~azure.storage.blob.models.LeaseStateType
    :ivar lease_duration: Known values are: "infinite" and "fixed".
    :vartype lease_duration: str or ~azure.storage.blob.models.LeaseDurationType
    :ivar public_access: Known values are: "container" and "blob".
    :vartype public_access: str or ~azure.storage.blob.models.PublicAccessType
    :ivar has_immutability_policy:
    :vartype has_immutability_policy: bool
    :ivar has_legal_hold:
    :vartype has_legal_hold: bool
    :ivar default_encryption_scope:
    :vartype default_encryption_scope: str
    :ivar prevent_encryption_scope_override:
    :vartype prevent_encryption_scope_override: bool
    :ivar deleted_time:
    :vartype deleted_time: ~datetime.datetime
    :ivar remaining_retention_days:
    :vartype remaining_retention_days: int
    :ivar is_immutable_storage_with_versioning_enabled: Indicates if version level worm is enabled
     on this container.
    :vartype is_immutable_storage_with_versioning_enabled: bool
    '''
    last_modified: Incomplete
    etag: Incomplete
    lease_status: Incomplete
    lease_state: Incomplete
    lease_duration: Incomplete
    public_access: Incomplete
    has_immutability_policy: Incomplete
    has_legal_hold: Incomplete
    default_encryption_scope: Incomplete
    prevent_encryption_scope_override: Incomplete
    deleted_time: Incomplete
    remaining_retention_days: Incomplete
    is_immutable_storage_with_versioning_enabled: Incomplete
    def __init__(self, *, last_modified: datetime.datetime, etag: str, lease_status: str | _models.LeaseStatusType | None = None, lease_state: str | _models.LeaseStateType | None = None, lease_duration: str | _models.LeaseDurationType | None = None, public_access: str | _models.PublicAccessType | None = None, has_immutability_policy: bool | None = None, has_legal_hold: bool | None = None, default_encryption_scope: str | None = None, prevent_encryption_scope_override: bool | None = None, deleted_time: datetime.datetime | None = None, remaining_retention_days: int | None = None, is_immutable_storage_with_versioning_enabled: bool | None = None, **kwargs: Any) -> None:
        '''
        :keyword last_modified: Required.
        :paramtype last_modified: ~datetime.datetime
        :keyword etag: Required.
        :paramtype etag: str
        :keyword lease_status: Known values are: "locked" and "unlocked".
        :paramtype lease_status: str or ~azure.storage.blob.models.LeaseStatusType
        :keyword lease_state: Known values are: "available", "leased", "expired", "breaking", and
         "broken".
        :paramtype lease_state: str or ~azure.storage.blob.models.LeaseStateType
        :keyword lease_duration: Known values are: "infinite" and "fixed".
        :paramtype lease_duration: str or ~azure.storage.blob.models.LeaseDurationType
        :keyword public_access: Known values are: "container" and "blob".
        :paramtype public_access: str or ~azure.storage.blob.models.PublicAccessType
        :keyword has_immutability_policy:
        :paramtype has_immutability_policy: bool
        :keyword has_legal_hold:
        :paramtype has_legal_hold: bool
        :keyword default_encryption_scope:
        :paramtype default_encryption_scope: str
        :keyword prevent_encryption_scope_override:
        :paramtype prevent_encryption_scope_override: bool
        :keyword deleted_time:
        :paramtype deleted_time: ~datetime.datetime
        :keyword remaining_retention_days:
        :paramtype remaining_retention_days: int
        :keyword is_immutable_storage_with_versioning_enabled: Indicates if version level worm is
         enabled on this container.
        :paramtype is_immutable_storage_with_versioning_enabled: bool
        '''

class CorsRule(_serialization.Model):
    """CORS is an HTTP feature that enables a web application running under one domain to access
    resources in another domain. Web browsers implement a security restriction known as same-origin
    policy that prevents a web page from calling APIs in a different domain; CORS provides a secure
    way to allow one domain (the origin domain) to call APIs in another domain.

    All required parameters must be populated in order to send to Azure.

    :ivar allowed_origins: The origin domains that are permitted to make a request against the
     storage service via CORS. The origin domain is the domain from which the request originates.
     Note that the origin must be an exact case-sensitive match with the origin that the user age
     sends to the service. You can also use the wildcard character '*' to allow all origin domains
     to make requests via CORS. Required.
    :vartype allowed_origins: str
    :ivar allowed_methods: The methods (HTTP request verbs) that the origin domain may use for a
     CORS request. (comma separated). Required.
    :vartype allowed_methods: str
    :ivar allowed_headers: the request headers that the origin domain may specify on the CORS
     request. Required.
    :vartype allowed_headers: str
    :ivar exposed_headers: The response headers that may be sent in the response to the CORS
     request and exposed by the browser to the request issuer. Required.
    :vartype exposed_headers: str
    :ivar max_age_in_seconds: The maximum amount time that a browser should cache the preflight
     OPTIONS request. Required.
    :vartype max_age_in_seconds: int
    """
    allowed_origins: Incomplete
    allowed_methods: Incomplete
    allowed_headers: Incomplete
    exposed_headers: Incomplete
    max_age_in_seconds: Incomplete
    def __init__(self, *, allowed_origins: str, allowed_methods: str, allowed_headers: str, exposed_headers: str, max_age_in_seconds: int, **kwargs: Any) -> None:
        """
        :keyword allowed_origins: The origin domains that are permitted to make a request against the
         storage service via CORS. The origin domain is the domain from which the request originates.
         Note that the origin must be an exact case-sensitive match with the origin that the user age
         sends to the service. You can also use the wildcard character '*' to allow all origin domains
         to make requests via CORS. Required.
        :paramtype allowed_origins: str
        :keyword allowed_methods: The methods (HTTP request verbs) that the origin domain may use for a
         CORS request. (comma separated). Required.
        :paramtype allowed_methods: str
        :keyword allowed_headers: the request headers that the origin domain may specify on the CORS
         request. Required.
        :paramtype allowed_headers: str
        :keyword exposed_headers: The response headers that may be sent in the response to the CORS
         request and exposed by the browser to the request issuer. Required.
        :paramtype exposed_headers: str
        :keyword max_age_in_seconds: The maximum amount time that a browser should cache the preflight
         OPTIONS request. Required.
        :paramtype max_age_in_seconds: int
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
     provided. Known values are: "None" and "AES256".
    :vartype encryption_algorithm: str or ~azure.storage.blob.models.EncryptionAlgorithmType
    '''
    encryption_key: Incomplete
    encryption_key_sha256: Incomplete
    encryption_algorithm: Incomplete
    def __init__(self, *, encryption_key: str | None = None, encryption_key_sha256: str | None = None, encryption_algorithm: str | _models.EncryptionAlgorithmType | None = None, **kwargs: Any) -> None:
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
         header is provided. Known values are: "None" and "AES256".
        :paramtype encryption_algorithm: str or ~azure.storage.blob.models.EncryptionAlgorithmType
        '''

class CpkScopeInfo(_serialization.Model):
    """Parameter group.

    :ivar encryption_scope: Optional. Version 2019-07-07 and later.  Specifies the name of the
     encryption scope to use to encrypt the data provided in the request. If not specified,
     encryption is performed with the default account encryption scope.  For more information, see
     Encryption at Rest for Azure Storage Services.
    :vartype encryption_scope: str
    """
    encryption_scope: Incomplete
    def __init__(self, *, encryption_scope: str | None = None, **kwargs: Any) -> None:
        """
        :keyword encryption_scope: Optional. Version 2019-07-07 and later.  Specifies the name of the
         encryption scope to use to encrypt the data provided in the request. If not specified,
         encryption is performed with the default account encryption scope.  For more information, see
         Encryption at Rest for Azure Storage Services.
        :paramtype encryption_scope: str
        """

class DelimitedTextConfiguration(_serialization.Model):
    """Groups the settings used for interpreting the blob data if the blob is delimited text
    formatted.

    :ivar column_separator: The string used to separate columns.
    :vartype column_separator: str
    :ivar field_quote: The string used to quote a specific field.
    :vartype field_quote: str
    :ivar record_separator: The string used to separate records.
    :vartype record_separator: str
    :ivar escape_char: The string used as an escape character.
    :vartype escape_char: str
    :ivar headers_present: Represents whether the data has headers.
    :vartype headers_present: bool
    """
    column_separator: Incomplete
    field_quote: Incomplete
    record_separator: Incomplete
    escape_char: Incomplete
    headers_present: Incomplete
    def __init__(self, *, column_separator: str | None = None, field_quote: str | None = None, record_separator: str | None = None, escape_char: str | None = None, headers_present: bool | None = None, **kwargs: Any) -> None:
        """
        :keyword column_separator: The string used to separate columns.
        :paramtype column_separator: str
        :keyword field_quote: The string used to quote a specific field.
        :paramtype field_quote: str
        :keyword record_separator: The string used to separate records.
        :paramtype record_separator: str
        :keyword escape_char: The string used as an escape character.
        :paramtype escape_char: str
        :keyword headers_present: Represents whether the data has headers.
        :paramtype headers_present: bool
        """

class FilterBlobItem(_serialization.Model):
    """Blob info from a Filter Blobs API call.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Required.
    :vartype name: str
    :ivar container_name: Required.
    :vartype container_name: str
    :ivar tags: Blob tags.
    :vartype tags: ~azure.storage.blob.models.BlobTags
    :ivar version_id:
    :vartype version_id: str
    :ivar is_current_version:
    :vartype is_current_version: bool
    """
    name: Incomplete
    container_name: Incomplete
    tags: Incomplete
    version_id: Incomplete
    is_current_version: Incomplete
    def __init__(self, *, name: str, container_name: str, tags: _models.BlobTags | None = None, version_id: str | None = None, is_current_version: bool | None = None, **kwargs: Any) -> None:
        """
        :keyword name: Required.
        :paramtype name: str
        :keyword container_name: Required.
        :paramtype container_name: str
        :keyword tags: Blob tags.
        :paramtype tags: ~azure.storage.blob.models.BlobTags
        :keyword version_id:
        :paramtype version_id: str
        :keyword is_current_version:
        :paramtype is_current_version: bool
        """

class FilterBlobSegment(_serialization.Model):
    """The result of a Filter Blobs API call.

    All required parameters must be populated in order to send to Azure.

    :ivar service_endpoint: Required.
    :vartype service_endpoint: str
    :ivar where: Required.
    :vartype where: str
    :ivar blobs: Required.
    :vartype blobs: list[~azure.storage.blob.models.FilterBlobItem]
    :ivar next_marker:
    :vartype next_marker: str
    """
    service_endpoint: Incomplete
    where: Incomplete
    blobs: Incomplete
    next_marker: Incomplete
    def __init__(self, *, service_endpoint: str, where: str, blobs: List['_models.FilterBlobItem'], next_marker: str | None = None, **kwargs: Any) -> None:
        """
        :keyword service_endpoint: Required.
        :paramtype service_endpoint: str
        :keyword where: Required.
        :paramtype where: str
        :keyword blobs: Required.
        :paramtype blobs: list[~azure.storage.blob.models.FilterBlobItem]
        :keyword next_marker:
        :paramtype next_marker: str
        """

class GeoReplication(_serialization.Model):
    '''Geo-Replication information for the Secondary Storage Service.

    All required parameters must be populated in order to send to Azure.

    :ivar status: The status of the secondary location. Required. Known values are: "live",
     "bootstrap", and "unavailable".
    :vartype status: str or ~azure.storage.blob.models.GeoReplicationStatusType
    :ivar last_sync_time: A GMT date/time value, to the second. All primary writes preceding this
     value are guaranteed to be available for read operations at the secondary. Primary writes after
     this point in time may or may not be available for reads. Required.
    :vartype last_sync_time: ~datetime.datetime
    '''
    status: Incomplete
    last_sync_time: Incomplete
    def __init__(self, *, status: str | _models.GeoReplicationStatusType, last_sync_time: datetime.datetime, **kwargs: Any) -> None:
        '''
        :keyword status: The status of the secondary location. Required. Known values are: "live",
         "bootstrap", and "unavailable".
        :paramtype status: str or ~azure.storage.blob.models.GeoReplicationStatusType
        :keyword last_sync_time: A GMT date/time value, to the second. All primary writes preceding
         this value are guaranteed to be available for read operations at the secondary. Primary writes
         after this point in time may or may not be available for reads. Required.
        :paramtype last_sync_time: ~datetime.datetime
        '''

class JsonTextConfiguration(_serialization.Model):
    """json text configuration.

    :ivar record_separator: The string used to separate records.
    :vartype record_separator: str
    """
    record_separator: Incomplete
    def __init__(self, *, record_separator: str | None = None, **kwargs: Any) -> None:
        """
        :keyword record_separator: The string used to separate records.
        :paramtype record_separator: str
        """

class KeyInfo(_serialization.Model):
    """Key information.

    All required parameters must be populated in order to send to Azure.

    :ivar start: The date-time the key is active in ISO 8601 UTC time. Required.
    :vartype start: str
    :ivar expiry: The date-time the key expires in ISO 8601 UTC time. Required.
    :vartype expiry: str
    """
    start: Incomplete
    expiry: Incomplete
    def __init__(self, *, start: str, expiry: str, **kwargs: Any) -> None:
        """
        :keyword start: The date-time the key is active in ISO 8601 UTC time. Required.
        :paramtype start: str
        :keyword expiry: The date-time the key expires in ISO 8601 UTC time. Required.
        :paramtype expiry: str
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

class ListBlobsFlatSegmentResponse(_serialization.Model):
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
    :ivar segment: Required.
    :vartype segment: ~azure.storage.blob.models.BlobFlatListSegment
    :ivar next_marker:
    :vartype next_marker: str
    """
    service_endpoint: Incomplete
    container_name: Incomplete
    prefix: Incomplete
    marker: Incomplete
    max_results: Incomplete
    segment: Incomplete
    next_marker: Incomplete
    def __init__(self, *, service_endpoint: str, container_name: str, segment: _models.BlobFlatListSegment, prefix: str | None = None, marker: str | None = None, max_results: int | None = None, next_marker: str | None = None, **kwargs: Any) -> None:
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
        :keyword segment: Required.
        :paramtype segment: ~azure.storage.blob.models.BlobFlatListSegment
        :keyword next_marker:
        :paramtype next_marker: str
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
    :vartype segment: ~azure.storage.blob.models.BlobHierarchyListSegment
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
        :paramtype segment: ~azure.storage.blob.models.BlobHierarchyListSegment
        :keyword next_marker:
        :paramtype next_marker: str
        """

class ListContainersSegmentResponse(_serialization.Model):
    """An enumeration of containers.

    All required parameters must be populated in order to send to Azure.

    :ivar service_endpoint: Required.
    :vartype service_endpoint: str
    :ivar prefix:
    :vartype prefix: str
    :ivar marker:
    :vartype marker: str
    :ivar max_results:
    :vartype max_results: int
    :ivar container_items: Required.
    :vartype container_items: list[~azure.storage.blob.models.ContainerItem]
    :ivar next_marker:
    :vartype next_marker: str
    """
    service_endpoint: Incomplete
    prefix: Incomplete
    marker: Incomplete
    max_results: Incomplete
    container_items: Incomplete
    next_marker: Incomplete
    def __init__(self, *, service_endpoint: str, container_items: List['_models.ContainerItem'], prefix: str | None = None, marker: str | None = None, max_results: int | None = None, next_marker: str | None = None, **kwargs: Any) -> None:
        """
        :keyword service_endpoint: Required.
        :paramtype service_endpoint: str
        :keyword prefix:
        :paramtype prefix: str
        :keyword marker:
        :paramtype marker: str
        :keyword max_results:
        :paramtype max_results: int
        :keyword container_items: Required.
        :paramtype container_items: list[~azure.storage.blob.models.ContainerItem]
        :keyword next_marker:
        :paramtype next_marker: str
        """

class Logging(_serialization.Model):
    """Azure Analytics Logging settings.

    All required parameters must be populated in order to send to Azure.

    :ivar version: The version of Storage Analytics to configure. Required.
    :vartype version: str
    :ivar delete: Indicates whether all delete requests should be logged. Required.
    :vartype delete: bool
    :ivar read: Indicates whether all read requests should be logged. Required.
    :vartype read: bool
    :ivar write: Indicates whether all write requests should be logged. Required.
    :vartype write: bool
    :ivar retention_policy: the retention policy which determines how long the associated data
     should persist. Required.
    :vartype retention_policy: ~azure.storage.blob.models.RetentionPolicy
    """
    version: Incomplete
    delete: Incomplete
    read: Incomplete
    write: Incomplete
    retention_policy: Incomplete
    def __init__(self, *, version: str, delete: bool, read: bool, write: bool, retention_policy: _models.RetentionPolicy, **kwargs: Any) -> None:
        """
        :keyword version: The version of Storage Analytics to configure. Required.
        :paramtype version: str
        :keyword delete: Indicates whether all delete requests should be logged. Required.
        :paramtype delete: bool
        :keyword read: Indicates whether all read requests should be logged. Required.
        :paramtype read: bool
        :keyword write: Indicates whether all write requests should be logged. Required.
        :paramtype write: bool
        :keyword retention_policy: the retention policy which determines how long the associated data
         should persist. Required.
        :paramtype retention_policy: ~azure.storage.blob.models.RetentionPolicy
        """

class Metrics(_serialization.Model):
    """a summary of request statistics grouped by API in hour or minute aggregates for blobs.

    All required parameters must be populated in order to send to Azure.

    :ivar version: The version of Storage Analytics to configure.
    :vartype version: str
    :ivar enabled: Indicates whether metrics are enabled for the Blob service. Required.
    :vartype enabled: bool
    :ivar include_apis: Indicates whether metrics should generate summary statistics for called API
     operations.
    :vartype include_apis: bool
    :ivar retention_policy: the retention policy which determines how long the associated data
     should persist.
    :vartype retention_policy: ~azure.storage.blob.models.RetentionPolicy
    """
    version: Incomplete
    enabled: Incomplete
    include_apis: Incomplete
    retention_policy: Incomplete
    def __init__(self, *, enabled: bool, version: str | None = None, include_apis: bool | None = None, retention_policy: _models.RetentionPolicy | None = None, **kwargs: Any) -> None:
        """
        :keyword version: The version of Storage Analytics to configure.
        :paramtype version: str
        :keyword enabled: Indicates whether metrics are enabled for the Blob service. Required.
        :paramtype enabled: bool
        :keyword include_apis: Indicates whether metrics should generate summary statistics for called
         API operations.
        :paramtype include_apis: bool
        :keyword retention_policy: the retention policy which determines how long the associated data
         should persist.
        :paramtype retention_policy: ~azure.storage.blob.models.RetentionPolicy
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
    :ivar if_tags: Specify a SQL where clause on blob tags to operate only on blobs with a matching
     value.
    :vartype if_tags: str
    """
    if_modified_since: Incomplete
    if_unmodified_since: Incomplete
    if_match: Incomplete
    if_none_match: Incomplete
    if_tags: Incomplete
    def __init__(self, *, if_modified_since: datetime.datetime | None = None, if_unmodified_since: datetime.datetime | None = None, if_match: str | None = None, if_none_match: str | None = None, if_tags: str | None = None, **kwargs: Any) -> None:
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
        :keyword if_tags: Specify a SQL where clause on blob tags to operate only on blobs with a
         matching value.
        :paramtype if_tags: str
        """

class PageList(_serialization.Model):
    """the list of pages.

    :ivar page_range:
    :vartype page_range: list[~azure.storage.blob.models.PageRange]
    :ivar clear_range:
    :vartype clear_range: list[~azure.storage.blob.models.ClearRange]
    :ivar next_marker:
    :vartype next_marker: str
    """
    page_range: Incomplete
    clear_range: Incomplete
    next_marker: Incomplete
    def __init__(self, *, page_range: List['_models.PageRange'] | None = None, clear_range: List['_models.ClearRange'] | None = None, next_marker: str | None = None, **kwargs: Any) -> None:
        """
        :keyword page_range:
        :paramtype page_range: list[~azure.storage.blob.models.PageRange]
        :keyword clear_range:
        :paramtype clear_range: list[~azure.storage.blob.models.ClearRange]
        :keyword next_marker:
        :paramtype next_marker: str
        """

class PageRange(_serialization.Model):
    """PageRange.

    All required parameters must be populated in order to send to Azure.

    :ivar start: Required.
    :vartype start: int
    :ivar end: Required.
    :vartype end: int
    """
    start: Incomplete
    end: Incomplete
    def __init__(self, *, start: int, end: int, **kwargs: Any) -> None:
        """
        :keyword start: Required.
        :paramtype start: int
        :keyword end: Required.
        :paramtype end: int
        """

class QueryFormat(_serialization.Model):
    '''QueryFormat.

    All required parameters must be populated in order to send to Azure.

    :ivar type: The quick query format type. Required. Known values are: "delimited", "json",
     "arrow", and "parquet".
    :vartype type: str or ~azure.storage.blob.models.QueryFormatType
    :ivar delimited_text_configuration: Groups the settings used for interpreting the blob data if
     the blob is delimited text formatted.
    :vartype delimited_text_configuration: ~azure.storage.blob.models.DelimitedTextConfiguration
    :ivar json_text_configuration: json text configuration.
    :vartype json_text_configuration: ~azure.storage.blob.models.JsonTextConfiguration
    :ivar arrow_configuration: Groups the settings used for formatting the response if the response
     should be Arrow formatted.
    :vartype arrow_configuration: ~azure.storage.blob.models.ArrowConfiguration
    :ivar parquet_text_configuration: parquet configuration.
    :vartype parquet_text_configuration: JSON
    '''
    type: Incomplete
    delimited_text_configuration: Incomplete
    json_text_configuration: Incomplete
    arrow_configuration: Incomplete
    parquet_text_configuration: Incomplete
    def __init__(self, *, type: str | _models.QueryFormatType, delimited_text_configuration: _models.DelimitedTextConfiguration | None = None, json_text_configuration: _models.JsonTextConfiguration | None = None, arrow_configuration: _models.ArrowConfiguration | None = None, parquet_text_configuration: JSON | None = None, **kwargs: Any) -> None:
        '''
        :keyword type: The quick query format type. Required. Known values are: "delimited", "json",
         "arrow", and "parquet".
        :paramtype type: str or ~azure.storage.blob.models.QueryFormatType
        :keyword delimited_text_configuration: Groups the settings used for interpreting the blob data
         if the blob is delimited text formatted.
        :paramtype delimited_text_configuration: ~azure.storage.blob.models.DelimitedTextConfiguration
        :keyword json_text_configuration: json text configuration.
        :paramtype json_text_configuration: ~azure.storage.blob.models.JsonTextConfiguration
        :keyword arrow_configuration: Groups the settings used for formatting the response if the
         response should be Arrow formatted.
        :paramtype arrow_configuration: ~azure.storage.blob.models.ArrowConfiguration
        :keyword parquet_text_configuration: parquet configuration.
        :paramtype parquet_text_configuration: JSON
        '''

class QueryRequest(_serialization.Model):
    '''Groups the set of query request settings.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar query_type: Required. The type of the provided query expression. Required. Default value
     is "SQL".
    :vartype query_type: str
    :ivar expression: The query expression in SQL. The maximum size of the query expression is
     256KiB. Required.
    :vartype expression: str
    :ivar input_serialization:
    :vartype input_serialization: ~azure.storage.blob.models.QuerySerialization
    :ivar output_serialization:
    :vartype output_serialization: ~azure.storage.blob.models.QuerySerialization
    '''
    query_type: str
    expression: Incomplete
    input_serialization: Incomplete
    output_serialization: Incomplete
    def __init__(self, *, expression: str, input_serialization: _models.QuerySerialization | None = None, output_serialization: _models.QuerySerialization | None = None, **kwargs: Any) -> None:
        """
        :keyword expression: The query expression in SQL. The maximum size of the query expression is
         256KiB. Required.
        :paramtype expression: str
        :keyword input_serialization:
        :paramtype input_serialization: ~azure.storage.blob.models.QuerySerialization
        :keyword output_serialization:
        :paramtype output_serialization: ~azure.storage.blob.models.QuerySerialization
        """

class QuerySerialization(_serialization.Model):
    """QuerySerialization.

    All required parameters must be populated in order to send to Azure.

    :ivar format: Required.
    :vartype format: ~azure.storage.blob.models.QueryFormat
    """
    format: Incomplete
    def __init__(self, *, format: _models.QueryFormat, **kwargs: Any) -> None:
        """
        :keyword format: Required.
        :paramtype format: ~azure.storage.blob.models.QueryFormat
        """

class RetentionPolicy(_serialization.Model):
    """the retention policy which determines how long the associated data should persist.

    All required parameters must be populated in order to send to Azure.

    :ivar enabled: Indicates whether a retention policy is enabled for the storage service.
     Required.
    :vartype enabled: bool
    :ivar days: Indicates the number of days that metrics or logging or soft-deleted data should be
     retained. All data older than this value will be deleted.
    :vartype days: int
    :ivar allow_permanent_delete: Indicates whether permanent delete is allowed on this storage
     account.
    :vartype allow_permanent_delete: bool
    """
    enabled: Incomplete
    days: Incomplete
    allow_permanent_delete: Incomplete
    def __init__(self, *, enabled: bool, days: int | None = None, allow_permanent_delete: bool | None = None, **kwargs: Any) -> None:
        """
        :keyword enabled: Indicates whether a retention policy is enabled for the storage service.
         Required.
        :paramtype enabled: bool
        :keyword days: Indicates the number of days that metrics or logging or soft-deleted data should
         be retained. All data older than this value will be deleted.
        :paramtype days: int
        :keyword allow_permanent_delete: Indicates whether permanent delete is allowed on this storage
         account.
        :paramtype allow_permanent_delete: bool
        """

class SequenceNumberAccessConditions(_serialization.Model):
    """Parameter group.

    :ivar if_sequence_number_less_than_or_equal_to: Specify this header value to operate only on a
     blob if it has a sequence number less than or equal to the specified.
    :vartype if_sequence_number_less_than_or_equal_to: int
    :ivar if_sequence_number_less_than: Specify this header value to operate only on a blob if it
     has a sequence number less than the specified.
    :vartype if_sequence_number_less_than: int
    :ivar if_sequence_number_equal_to: Specify this header value to operate only on a blob if it
     has the specified sequence number.
    :vartype if_sequence_number_equal_to: int
    """
    if_sequence_number_less_than_or_equal_to: Incomplete
    if_sequence_number_less_than: Incomplete
    if_sequence_number_equal_to: Incomplete
    def __init__(self, *, if_sequence_number_less_than_or_equal_to: int | None = None, if_sequence_number_less_than: int | None = None, if_sequence_number_equal_to: int | None = None, **kwargs: Any) -> None:
        """
        :keyword if_sequence_number_less_than_or_equal_to: Specify this header value to operate only on
         a blob if it has a sequence number less than or equal to the specified.
        :paramtype if_sequence_number_less_than_or_equal_to: int
        :keyword if_sequence_number_less_than: Specify this header value to operate only on a blob if
         it has a sequence number less than the specified.
        :paramtype if_sequence_number_less_than: int
        :keyword if_sequence_number_equal_to: Specify this header value to operate only on a blob if it
         has the specified sequence number.
        :paramtype if_sequence_number_equal_to: int
        """

class SignedIdentifier(_serialization.Model):
    """signed identifier.

    All required parameters must be populated in order to send to Azure.

    :ivar id: a unique id. Required.
    :vartype id: str
    :ivar access_policy: An Access policy.
    :vartype access_policy: ~azure.storage.blob.models.AccessPolicy
    """
    id: Incomplete
    access_policy: Incomplete
    def __init__(self, *, id: str, access_policy: _models.AccessPolicy | None = None, **kwargs: Any) -> None:
        """
        :keyword id: a unique id. Required.
        :paramtype id: str
        :keyword access_policy: An Access policy.
        :paramtype access_policy: ~azure.storage.blob.models.AccessPolicy
        """

class SourceModifiedAccessConditions(_serialization.Model):
    """Parameter group.

    :ivar source_if_modified_since: Specify this header value to operate only on a blob if it has
     been modified since the specified date/time.
    :vartype source_if_modified_since: ~datetime.datetime
    :ivar source_if_unmodified_since: Specify this header value to operate only on a blob if it has
     not been modified since the specified date/time.
    :vartype source_if_unmodified_since: ~datetime.datetime
    :ivar source_if_match: Specify an ETag value to operate only on blobs with a matching value.
    :vartype source_if_match: str
    :ivar source_if_none_match: Specify an ETag value to operate only on blobs without a matching
     value.
    :vartype source_if_none_match: str
    :ivar source_if_tags: Specify a SQL where clause on blob tags to operate only on blobs with a
     matching value.
    :vartype source_if_tags: str
    """
    source_if_modified_since: Incomplete
    source_if_unmodified_since: Incomplete
    source_if_match: Incomplete
    source_if_none_match: Incomplete
    source_if_tags: Incomplete
    def __init__(self, *, source_if_modified_since: datetime.datetime | None = None, source_if_unmodified_since: datetime.datetime | None = None, source_if_match: str | None = None, source_if_none_match: str | None = None, source_if_tags: str | None = None, **kwargs: Any) -> None:
        """
        :keyword source_if_modified_since: Specify this header value to operate only on a blob if it
         has been modified since the specified date/time.
        :paramtype source_if_modified_since: ~datetime.datetime
        :keyword source_if_unmodified_since: Specify this header value to operate only on a blob if it
         has not been modified since the specified date/time.
        :paramtype source_if_unmodified_since: ~datetime.datetime
        :keyword source_if_match: Specify an ETag value to operate only on blobs with a matching value.
        :paramtype source_if_match: str
        :keyword source_if_none_match: Specify an ETag value to operate only on blobs without a
         matching value.
        :paramtype source_if_none_match: str
        :keyword source_if_tags: Specify a SQL where clause on blob tags to operate only on blobs with
         a matching value.
        :paramtype source_if_tags: str
        """

class StaticWebsite(_serialization.Model):
    """The properties that enable an account to host a static website.

    All required parameters must be populated in order to send to Azure.

    :ivar enabled: Indicates whether this account is hosting a static website. Required.
    :vartype enabled: bool
    :ivar index_document: The default name of the index page under each directory.
    :vartype index_document: str
    :ivar error_document404_path: The absolute path of the custom 404 page.
    :vartype error_document404_path: str
    :ivar default_index_document_path: Absolute path of the default index page.
    :vartype default_index_document_path: str
    """
    enabled: Incomplete
    index_document: Incomplete
    error_document404_path: Incomplete
    default_index_document_path: Incomplete
    def __init__(self, *, enabled: bool, index_document: str | None = None, error_document404_path: str | None = None, default_index_document_path: str | None = None, **kwargs: Any) -> None:
        """
        :keyword enabled: Indicates whether this account is hosting a static website. Required.
        :paramtype enabled: bool
        :keyword index_document: The default name of the index page under each directory.
        :paramtype index_document: str
        :keyword error_document404_path: The absolute path of the custom 404 page.
        :paramtype error_document404_path: str
        :keyword default_index_document_path: Absolute path of the default index page.
        :paramtype default_index_document_path: str
        """

class StorageError(_serialization.Model):
    """StorageError.

    :ivar message:
    :vartype message: str
    """
    message: Incomplete
    def __init__(self, *, message: str | None = None, **kwargs: Any) -> None:
        """
        :keyword message:
        :paramtype message: str
        """

class StorageServiceProperties(_serialization.Model):
    """Storage Service Properties.

    :ivar logging: Azure Analytics Logging settings.
    :vartype logging: ~azure.storage.blob.models.Logging
    :ivar hour_metrics: a summary of request statistics grouped by API in hour or minute aggregates
     for blobs.
    :vartype hour_metrics: ~azure.storage.blob.models.Metrics
    :ivar minute_metrics: a summary of request statistics grouped by API in hour or minute
     aggregates for blobs.
    :vartype minute_metrics: ~azure.storage.blob.models.Metrics
    :ivar cors: The set of CORS rules.
    :vartype cors: list[~azure.storage.blob.models.CorsRule]
    :ivar default_service_version: The default version to use for requests to the Blob service if
     an incoming request's version is not specified. Possible values include version 2008-10-27 and
     all more recent versions.
    :vartype default_service_version: str
    :ivar delete_retention_policy: the retention policy which determines how long the associated
     data should persist.
    :vartype delete_retention_policy: ~azure.storage.blob.models.RetentionPolicy
    :ivar static_website: The properties that enable an account to host a static website.
    :vartype static_website: ~azure.storage.blob.models.StaticWebsite
    """
    logging: Incomplete
    hour_metrics: Incomplete
    minute_metrics: Incomplete
    cors: Incomplete
    default_service_version: Incomplete
    delete_retention_policy: Incomplete
    static_website: Incomplete
    def __init__(self, *, logging: _models.Logging | None = None, hour_metrics: _models.Metrics | None = None, minute_metrics: _models.Metrics | None = None, cors: List['_models.CorsRule'] | None = None, default_service_version: str | None = None, delete_retention_policy: _models.RetentionPolicy | None = None, static_website: _models.StaticWebsite | None = None, **kwargs: Any) -> None:
        """
        :keyword logging: Azure Analytics Logging settings.
        :paramtype logging: ~azure.storage.blob.models.Logging
        :keyword hour_metrics: a summary of request statistics grouped by API in hour or minute
         aggregates for blobs.
        :paramtype hour_metrics: ~azure.storage.blob.models.Metrics
        :keyword minute_metrics: a summary of request statistics grouped by API in hour or minute
         aggregates for blobs.
        :paramtype minute_metrics: ~azure.storage.blob.models.Metrics
        :keyword cors: The set of CORS rules.
        :paramtype cors: list[~azure.storage.blob.models.CorsRule]
        :keyword default_service_version: The default version to use for requests to the Blob service
         if an incoming request's version is not specified. Possible values include version 2008-10-27
         and all more recent versions.
        :paramtype default_service_version: str
        :keyword delete_retention_policy: the retention policy which determines how long the associated
         data should persist.
        :paramtype delete_retention_policy: ~azure.storage.blob.models.RetentionPolicy
        :keyword static_website: The properties that enable an account to host a static website.
        :paramtype static_website: ~azure.storage.blob.models.StaticWebsite
        """

class StorageServiceStats(_serialization.Model):
    """Stats for the storage service.

    :ivar geo_replication: Geo-Replication information for the Secondary Storage Service.
    :vartype geo_replication: ~azure.storage.blob.models.GeoReplication
    """
    geo_replication: Incomplete
    def __init__(self, *, geo_replication: _models.GeoReplication | None = None, **kwargs: Any) -> None:
        """
        :keyword geo_replication: Geo-Replication information for the Secondary Storage Service.
        :paramtype geo_replication: ~azure.storage.blob.models.GeoReplication
        """

class UserDelegationKey(_serialization.Model):
    """A user delegation key.

    All required parameters must be populated in order to send to Azure.

    :ivar signed_oid: The Azure Active Directory object ID in GUID format. Required.
    :vartype signed_oid: str
    :ivar signed_tid: The Azure Active Directory tenant ID in GUID format. Required.
    :vartype signed_tid: str
    :ivar signed_start: The date-time the key is active. Required.
    :vartype signed_start: ~datetime.datetime
    :ivar signed_expiry: The date-time the key expires. Required.
    :vartype signed_expiry: ~datetime.datetime
    :ivar signed_service: Abbreviation of the Azure Storage service that accepts the key. Required.
    :vartype signed_service: str
    :ivar signed_version: The service version that created the key. Required.
    :vartype signed_version: str
    :ivar value: The key as a base64 string. Required.
    :vartype value: str
    """
    signed_oid: Incomplete
    signed_tid: Incomplete
    signed_start: Incomplete
    signed_expiry: Incomplete
    signed_service: Incomplete
    signed_version: Incomplete
    value: Incomplete
    def __init__(self, *, signed_oid: str, signed_tid: str, signed_start: datetime.datetime, signed_expiry: datetime.datetime, signed_service: str, signed_version: str, value: str, **kwargs: Any) -> None:
        """
        :keyword signed_oid: The Azure Active Directory object ID in GUID format. Required.
        :paramtype signed_oid: str
        :keyword signed_tid: The Azure Active Directory tenant ID in GUID format. Required.
        :paramtype signed_tid: str
        :keyword signed_start: The date-time the key is active. Required.
        :paramtype signed_start: ~datetime.datetime
        :keyword signed_expiry: The date-time the key expires. Required.
        :paramtype signed_expiry: ~datetime.datetime
        :keyword signed_service: Abbreviation of the Azure Storage service that accepts the key.
         Required.
        :paramtype signed_service: str
        :keyword signed_version: The service version that created the key. Required.
        :paramtype signed_version: str
        :keyword value: The key as a base64 string. Required.
        :paramtype value: str
        """
