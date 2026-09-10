from _typeshed import Incomplete
from azure.core import CaseInsensitiveEnumMeta
from enum import Enum

def get_enum_value(value): ...

class StorageErrorCode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    ACCOUNT_ALREADY_EXISTS: str
    ACCOUNT_BEING_CREATED: str
    ACCOUNT_IS_DISABLED: str
    AUTHENTICATION_FAILED: str
    AUTHORIZATION_FAILURE: str
    NO_AUTHENTICATION_INFORMATION: str
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
    BLOB_NOT_FOUND: str
    BLOB_OVERWRITTEN: str
    BLOB_TIER_INADEQUATE_FOR_CONTENT_LENGTH: str
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
    INCREMENTAL_COPY_OF_ERALIER_VERSION_SNAPSHOT_NOT_ALLOWED: str
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
    SNAPHOT_OPERATION_RATE_EXCEEDED: str
    SNAPSHOTS_PRESENT: str
    SOURCE_CONDITION_NOT_MET: str
    SYSTEM_IN_USE: str
    TARGET_CONDITION_NOT_MET: str
    UNAUTHORIZED_BLOB_OVERWRITE: str
    BLOB_BEING_REHYDRATED: str
    BLOB_ARCHIVED: str
    BLOB_NOT_ARCHIVED: str
    INVALID_MARKER: str
    MESSAGE_NOT_FOUND: str
    MESSAGE_TOO_LARGE: str
    POP_RECEIPT_MISMATCH: str
    QUEUE_ALREADY_EXISTS: str
    QUEUE_BEING_DELETED: str
    QUEUE_DISABLED: str
    QUEUE_NOT_EMPTY: str
    QUEUE_NOT_FOUND: str
    CANNOT_DELETE_FILE_OR_DIRECTORY: str
    CLIENT_CACHE_FLUSH_DELAY: str
    DELETE_PENDING: str
    DIRECTORY_NOT_EMPTY: str
    FILE_LOCK_CONFLICT: str
    INVALID_FILE_OR_DIRECTORY_PATH_NAME: str
    PARENT_NOT_FOUND: str
    READ_ONLY_ATTRIBUTE: str
    SHARE_ALREADY_EXISTS: str
    SHARE_BEING_DELETED: str
    SHARE_DISABLED: str
    SHARE_NOT_FOUND: str
    SHARING_VIOLATION: str
    SHARE_SNAPSHOT_IN_PROGRESS: str
    SHARE_SNAPSHOT_COUNT_EXCEEDED: str
    SHARE_SNAPSHOT_OPERATION_NOT_SUPPORTED: str
    SHARE_HAS_SNAPSHOTS: str
    CONTAINER_QUOTA_DOWNGRADE_NOT_ALLOWED: str
    CONTENT_LENGTH_MUST_BE_ZERO: str
    PATH_ALREADY_EXISTS: str
    INVALID_FLUSH_POSITION: str
    INVALID_PROPERTY_NAME: str
    INVALID_SOURCE_URI: str
    UNSUPPORTED_REST_VERSION: str
    FILE_SYSTEM_NOT_FOUND: str
    PATH_NOT_FOUND: str
    RENAME_DESTINATION_PARENT_PATH_NOT_FOUND: str
    SOURCE_PATH_NOT_FOUND: str
    DESTINATION_PATH_IS_BEING_DELETED: str
    FILE_SYSTEM_ALREADY_EXISTS: str
    FILE_SYSTEM_BEING_DELETED: str
    INVALID_DESTINATION_PATH: str
    INVALID_RENAME_SOURCE_PATH: str
    INVALID_SOURCE_OR_DESTINATION_RESOURCE_TYPE: str
    LEASE_IS_ALREADY_BROKEN: str
    LEASE_NAME_MISMATCH: str
    PATH_CONFLICT: str
    SOURCE_PATH_IS_BEING_DELETED: str

class DictMixin:
    def __setitem__(self, key, item) -> None: ...
    def __getitem__(self, key): ...
    def __len__(self) -> int: ...
    def __delitem__(self, key) -> None: ...
    def __eq__(self, other):
        """Compare objects by comparing all attributes."""
    def __ne__(self, other):
        """Compare objects by comparing all attributes."""
    def has_key(self, k): ...
    def update(self, *args, **kwargs): ...
    def keys(self): ...
    def values(self): ...
    def items(self): ...
    def get(self, key, default: Incomplete | None = None): ...

class LocationMode:
    """
    Specifies the location the request should be sent to. This mode only applies
    for RA-GRS accounts which allow secondary read access. All other account types
    must use PRIMARY.
    """
    PRIMARY: str
    SECONDARY: str

class ResourceTypes:
    """
    Specifies the resource types that are accessible with the account SAS.

    :param bool service:
        Access to service-level APIs (e.g., Get/Set Service Properties,
        Get Service Stats, List Containers/Queues/Shares)
    :param bool container:
        Access to container-level APIs (e.g., Create/Delete Container,
        Create/Delete Queue, Create/Delete Share,
        List Blobs/Files and Directories)
    :param bool object:
        Access to object-level APIs for blobs, queue messages, and
        files(e.g. Put Blob, Query Entity, Get Messages, Create File, etc.)
    """
    service: Incomplete
    container: Incomplete
    object: Incomplete
    def __init__(self, service: bool = False, container: bool = False, object: bool = False) -> None: ...
    @classmethod
    def from_string(cls, string):
        '''Create a ResourceTypes from a string.

        To specify service, container, or object you need only to
        include the first letter of the word in the string. E.g. service and container,
        you would provide a string "sc".

        :param str string: Specify service, container, or object in
            in the string with the first letter of the word.
        :return: A ResourceTypes object
        :rtype: ~azure.storage.blob.ResourceTypes
        '''

class AccountSasPermissions:
    """
    :class:`~ResourceTypes` class to be used with generate_account_sas
    function and for the AccessPolicies used with set_*_acl. There are two types of
    SAS which may be used to grant resource access. One is to grant access to a
    specific resource (resource-specific). Another is to grant access to the
    entire service for a specific account and allow certain operations based on
    perms found here.

    :param bool read:
        Valid for all signed resources types (Service, Container, and Object).
        Permits read permissions to the specified resource type.
    :param bool write:
        Valid for all signed resources types (Service, Container, and Object).
        Permits write permissions to the specified resource type.
    :param bool delete:
        Valid for Container and Object resource types, except for queue messages.
    :param bool delete_previous_version:
        Delete the previous blob version for the versioning enabled storage account.
    :param bool list:
        Valid for Service and Container resource types only.
    :param bool add:
        Valid for the following Object resource types only: queue messages, and append blobs.
    :param bool create:
        Valid for the following Object resource types only: blobs and files.
        Users can create new blobs or files, but may not overwrite existing
        blobs or files.
    :param bool update:
        Valid for the following Object resource types only: queue messages.
    :param bool process:
        Valid for the following Object resource type only: queue messages.
    :keyword bool tag:
        To enable set or get tags on the blobs in the container.
    :keyword bool filter_by_tags:
        To enable get blobs by tags, this should be used together with list permission.
    :keyword bool set_immutability_policy:
        To enable operations related to set/delete immutability policy.
        To get immutability policy, you just need read permission.
    :keyword bool permanent_delete:
        To enable permanent delete on the blob is permitted.
        Valid for Object resource type of Blob only.
    """
    read: Incomplete
    write: Incomplete
    delete: Incomplete
    delete_previous_version: Incomplete
    permanent_delete: Incomplete
    list: Incomplete
    add: Incomplete
    create: Incomplete
    update: Incomplete
    process: Incomplete
    tag: Incomplete
    filter_by_tags: Incomplete
    set_immutability_policy: Incomplete
    def __init__(self, read: bool = False, write: bool = False, delete: bool = False, list: bool = False, add: bool = False, create: bool = False, update: bool = False, process: bool = False, delete_previous_version: bool = False, **kwargs) -> None: ...
    @classmethod
    def from_string(cls, permission):
        '''Create AccountSasPermissions from a string.

        To specify read, write, delete, etc. permissions you need only to
        include the first letter of the word in the string. E.g. for read and write
        permissions you would provide a string "rw".

        :param str permission: Specify permissions in
            the string with the first letter of the word.
        :return: An AccountSasPermissions object
        :rtype: ~azure.storage.filedatalake.AccountSasPermissions
        '''

class Services:
    """Specifies the services accessible with the account SAS.

    :param bool blob:
        Access for the `~azure.storage.blob.BlobServiceClient`
    :param bool queue:
        Access for the `~azure.storage.queue.QueueServiceClient`
    :param bool fileshare:
        Access for the `~azure.storage.fileshare.ShareServiceClient`
    """
    blob: Incomplete
    queue: Incomplete
    fileshare: Incomplete
    def __init__(self, blob: bool = False, queue: bool = False, fileshare: bool = False) -> None: ...
    @classmethod
    def from_string(cls, string):
        '''Create Services from a string.

        To specify blob, queue, or file you need only to
        include the first letter of the word in the string. E.g. for blob and queue
        you would provide a string "bq".

        :param str string: Specify blob, queue, or file in
            in the string with the first letter of the word.
        :return: A Services object
        :rtype: ~azure.storage.blob.Services
        '''

class UserDelegationKey:
    """
    Represents a user delegation key, provided to the user by Azure Storage
    based on their Azure Active Directory access token.

    The fields are saved as simple strings since the user does not have to interact with this object;
    to generate an identify SAS, the user can simply pass it to the right API.

    :ivar str signed_oid:
        Object ID of this token.
    :ivar str signed_tid:
        Tenant ID of the tenant that issued this token.
    :ivar str signed_start:
        The datetime this token becomes valid.
    :ivar str signed_expiry:
        The datetime this token expires.
    :ivar str signed_service:
        What service this key is valid for.
    :ivar str signed_version:
        The version identifier of the REST service that created this token.
    :ivar str value:
        The user delegation key.
    """
    signed_oid: Incomplete
    signed_tid: Incomplete
    signed_start: Incomplete
    signed_expiry: Incomplete
    signed_service: Incomplete
    signed_version: Incomplete
    value: Incomplete
    def __init__(self) -> None: ...
