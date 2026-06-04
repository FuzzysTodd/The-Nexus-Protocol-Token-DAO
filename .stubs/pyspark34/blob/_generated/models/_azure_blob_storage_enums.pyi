from azure.core import CaseInsensitiveEnumMeta
from enum import Enum

class AccessTier(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """AccessTier."""
    P4: str
    P6: str
    P10: str
    P15: str
    P20: str
    P30: str
    P40: str
    P50: str
    P60: str
    P70: str
    P80: str
    HOT: str
    COOL: str
    ARCHIVE: str
    PREMIUM: str
    COLD: str

class AccessTierOptional(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """AccessTierOptional."""
    P4: str
    P6: str
    P10: str
    P15: str
    P20: str
    P30: str
    P40: str
    P50: str
    P60: str
    P70: str
    P80: str
    HOT: str
    COOL: str
    ARCHIVE: str
    COLD: str

class AccessTierRequired(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """AccessTierRequired."""
    P4: str
    P6: str
    P10: str
    P15: str
    P20: str
    P30: str
    P40: str
    P50: str
    P60: str
    P70: str
    P80: str
    HOT: str
    COOL: str
    ARCHIVE: str
    COLD: str

class AccountKind(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """AccountKind."""
    STORAGE: str
    BLOB_STORAGE: str
    STORAGE_V2: str
    FILE_STORAGE: str
    BLOCK_BLOB_STORAGE: str

class ArchiveStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """ArchiveStatus."""
    REHYDRATE_PENDING_TO_HOT: str
    REHYDRATE_PENDING_TO_COOL: str
    REHYDRATE_PENDING_TO_COLD: str

class BlobCopySourceTags(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """BlobCopySourceTags."""
    REPLACE: str
    COPY: str

class BlobExpiryOptions(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """BlobExpiryOptions."""
    NEVER_EXPIRE: str
    RELATIVE_TO_CREATION: str
    RELATIVE_TO_NOW: str
    ABSOLUTE: str

class BlobImmutabilityPolicyMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """BlobImmutabilityPolicyMode."""
    MUTABLE: str
    UNLOCKED: str
    LOCKED: str

class BlobType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """BlobType."""
    BLOCK_BLOB: str
    PAGE_BLOB: str
    APPEND_BLOB: str

class BlockListType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """BlockListType."""
    COMMITTED: str
    UNCOMMITTED: str
    ALL: str

class CopyStatusType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """CopyStatusType."""
    PENDING: str
    SUCCESS: str
    ABORTED: str
    FAILED: str

class DeleteSnapshotsOptionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """DeleteSnapshotsOptionType."""
    INCLUDE: str
    ONLY: str

class EncryptionAlgorithmType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """EncryptionAlgorithmType."""
    NONE: str
    AES256: str

class FilterBlobsIncludeItem(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """FilterBlobsIncludeItem."""
    NONE: str
    VERSIONS: str

class GeoReplicationStatusType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The status of the secondary location."""
    LIVE: str
    BOOTSTRAP: str
    UNAVAILABLE: str

class LeaseDurationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """LeaseDurationType."""
    INFINITE: str
    FIXED: str

class LeaseStateType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """LeaseStateType."""
    AVAILABLE: str
    LEASED: str
    EXPIRED: str
    BREAKING: str
    BROKEN: str

class LeaseStatusType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """LeaseStatusType."""
    LOCKED: str
    UNLOCKED: str

class ListBlobsIncludeItem(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """ListBlobsIncludeItem."""
    COPY: str
    DELETED: str
    METADATA: str
    SNAPSHOTS: str
    UNCOMMITTEDBLOBS: str
    VERSIONS: str
    TAGS: str
    IMMUTABILITYPOLICY: str
    LEGALHOLD: str
    DELETEDWITHVERSIONS: str

class ListContainersIncludeType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """ListContainersIncludeType."""
    METADATA: str
    DELETED: str
    SYSTEM: str

class PremiumPageBlobAccessTier(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """PremiumPageBlobAccessTier."""
    P4: str
    P6: str
    P10: str
    P15: str
    P20: str
    P30: str
    P40: str
    P50: str
    P60: str
    P70: str
    P80: str

class PublicAccessType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """PublicAccessType."""
    CONTAINER: str
    BLOB: str

class QueryFormatType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The quick query format type."""
    DELIMITED: str
    JSON: str
    ARROW: str
    PARQUET: str

class RehydratePriority(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """If an object is in rehydrate pending state then this header is returned with priority of
    rehydrate. Valid values are High and Standard.
    """
    HIGH: str
    STANDARD: str

class SequenceNumberActionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """SequenceNumberActionType."""
    MAX: str
    UPDATE: str
    INCREMENT: str

class SkuName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """SkuName."""
    STANDARD_LRS: str
    STANDARD_GRS: str
    STANDARD_RAGRS: str
    STANDARD_ZRS: str
    PREMIUM_LRS: str

class StorageErrorCode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Error codes returned by the service."""
    ACCOUNT_ALREADY_EXISTS: str
    ACCOUNT_BEING_CREATED: str
    ACCOUNT_IS_DISABLED: str
    AUTHENTICATION_FAILED: str
    AUTHORIZATION_FAILURE: str
    CONDITION_HEADERS_NOT_SUPPORTED: str
    CONDITION_NOT_MET: str
    EMPTY_METADATA_KEY: str
    INSUFFICIENT_ACCOUNT_PERMISSIONS: str
    INTERNAL_ERROR: str
    INVALID_AUTHENTICATION_INFO: str
    INVALID_HEADER_VALUE: str
    INVALID_HTTP_VERB: str
    INVALID_INPUT: str
    INVALID_MD5: str
    INVALID_METADATA: str
    INVALID_QUERY_PARAMETER_VALUE: str
    INVALID_RANGE: str
    INVALID_RESOURCE_NAME: str
    INVALID_URI: str
    INVALID_XML_DOCUMENT: str
    INVALID_XML_NODE_VALUE: str
    MD5_MISMATCH: str
    METADATA_TOO_LARGE: str
    MISSING_CONTENT_LENGTH_HEADER: str
    MISSING_REQUIRED_QUERY_PARAMETER: str
    MISSING_REQUIRED_HEADER: str
    MISSING_REQUIRED_XML_NODE: str
    MULTIPLE_CONDITION_HEADERS_NOT_SUPPORTED: str
    OPERATION_TIMED_OUT: str
    OUT_OF_RANGE_INPUT: str
    OUT_OF_RANGE_QUERY_PARAMETER_VALUE: str
    REQUEST_BODY_TOO_LARGE: str
    RESOURCE_TYPE_MISMATCH: str
    REQUEST_URL_FAILED_TO_PARSE: str
    RESOURCE_ALREADY_EXISTS: str
    RESOURCE_NOT_FOUND: str
    SERVER_BUSY: str
    UNSUPPORTED_HEADER: str
    UNSUPPORTED_XML_NODE: str
    UNSUPPORTED_QUERY_PARAMETER: str
    UNSUPPORTED_HTTP_VERB: str
    APPEND_POSITION_CONDITION_NOT_MET: str
    BLOB_ALREADY_EXISTS: str
    BLOB_IMMUTABLE_DUE_TO_POLICY: str
    BLOB_NOT_FOUND: str
    BLOB_OVERWRITTEN: str
    BLOB_TIER_INADEQUATE_FOR_CONTENT_LENGTH: str
    BLOB_USES_CUSTOMER_SPECIFIED_ENCRYPTION: str
    BLOCK_COUNT_EXCEEDS_LIMIT: str
    BLOCK_LIST_TOO_LONG: str
    CANNOT_CHANGE_TO_LOWER_TIER: str
    CANNOT_VERIFY_COPY_SOURCE: str
    CONTAINER_ALREADY_EXISTS: str
    CONTAINER_BEING_DELETED: str
    CONTAINER_DISABLED: str
    CONTAINER_NOT_FOUND: str
    CONTENT_LENGTH_LARGER_THAN_TIER_LIMIT: str
    COPY_ACROSS_ACCOUNTS_NOT_SUPPORTED: str
    COPY_ID_MISMATCH: str
    FEATURE_VERSION_MISMATCH: str
    INCREMENTAL_COPY_BLOB_MISMATCH: str
    INCREMENTAL_COPY_OF_EARLIER_VERSION_SNAPSHOT_NOT_ALLOWED: str
    INCREMENTAL_COPY_SOURCE_MUST_BE_SNAPSHOT: str
    INFINITE_LEASE_DURATION_REQUIRED: str
    INVALID_BLOB_OR_BLOCK: str
    INVALID_BLOB_TIER: str
    INVALID_BLOB_TYPE: str
    INVALID_BLOCK_ID: str
    INVALID_BLOCK_LIST: str
    INVALID_OPERATION: str
    INVALID_PAGE_RANGE: str
    INVALID_SOURCE_BLOB_TYPE: str
    INVALID_SOURCE_BLOB_URL: str
    INVALID_VERSION_FOR_PAGE_BLOB_OPERATION: str
    LEASE_ALREADY_PRESENT: str
    LEASE_ALREADY_BROKEN: str
    LEASE_ID_MISMATCH_WITH_BLOB_OPERATION: str
    LEASE_ID_MISMATCH_WITH_CONTAINER_OPERATION: str
    LEASE_ID_MISMATCH_WITH_LEASE_OPERATION: str
    LEASE_ID_MISSING: str
    LEASE_IS_BREAKING_AND_CANNOT_BE_ACQUIRED: str
    LEASE_IS_BREAKING_AND_CANNOT_BE_CHANGED: str
    LEASE_IS_BROKEN_AND_CANNOT_BE_RENEWED: str
    LEASE_LOST: str
    LEASE_NOT_PRESENT_WITH_BLOB_OPERATION: str
    LEASE_NOT_PRESENT_WITH_CONTAINER_OPERATION: str
    LEASE_NOT_PRESENT_WITH_LEASE_OPERATION: str
    MAX_BLOB_SIZE_CONDITION_NOT_MET: str
    NO_AUTHENTICATION_INFORMATION: str
    NO_PENDING_COPY_OPERATION: str
    OPERATION_NOT_ALLOWED_ON_INCREMENTAL_COPY_BLOB: str
    PENDING_COPY_OPERATION: str
    PREVIOUS_SNAPSHOT_CANNOT_BE_NEWER: str
    PREVIOUS_SNAPSHOT_NOT_FOUND: str
    PREVIOUS_SNAPSHOT_OPERATION_NOT_SUPPORTED: str
    SEQUENCE_NUMBER_CONDITION_NOT_MET: str
    SEQUENCE_NUMBER_INCREMENT_TOO_LARGE: str
    SNAPSHOT_COUNT_EXCEEDED: str
    SNAPSHOT_OPERATION_RATE_EXCEEDED: str
    SNAPSHOTS_PRESENT: str
    SOURCE_CONDITION_NOT_MET: str
    SYSTEM_IN_USE: str
    TARGET_CONDITION_NOT_MET: str
    UNAUTHORIZED_BLOB_OVERWRITE: str
    BLOB_BEING_REHYDRATED: str
    BLOB_ARCHIVED: str
    BLOB_NOT_ARCHIVED: str
    AUTHORIZATION_SOURCE_IP_MISMATCH: str
    AUTHORIZATION_PROTOCOL_MISMATCH: str
    AUTHORIZATION_PERMISSION_MISMATCH: str
    AUTHORIZATION_SERVICE_MISMATCH: str
    AUTHORIZATION_RESOURCE_TYPE_MISMATCH: str
