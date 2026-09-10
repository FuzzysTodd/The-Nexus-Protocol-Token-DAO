from ._generated.models import AccessPolicy as GenAccessPolicy, ArrowField as ArrowField, CorsRule as GeneratedCorsRule, Logging as GeneratedLogging, Metrics as GeneratedMetrics, RetentionPolicy as GeneratedRetentionPolicy, StaticWebsite as GeneratedStaticWebsite
from ._shared import decode_base64_to_bytes as decode_base64_to_bytes
from ._shared.models import DictMixin as DictMixin, get_enum_value as get_enum_value
from ._shared.response_handlers import process_storage_error as process_storage_error, return_context_and_deserialized as return_context_and_deserialized
from _typeshed import Incomplete
from azure.core import CaseInsensitiveEnumMeta
from azure.core.paging import PageIterator
from datetime import datetime
from enum import Enum
from typing import Dict, List

def parse_page_list(page_list): ...

class BlobType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    BLOCKBLOB: str
    PAGEBLOB: str
    APPENDBLOB: str

class BlockState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Block blob block types."""
    COMMITTED: str
    LATEST: str
    UNCOMMITTED: str

class StandardBlobTier(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """
    Specifies the blob tier to set the blob to. This is only applicable for
    block blobs on standard storage accounts.
    """
    ARCHIVE: str
    COOL: str
    COLD: str
    HOT: str

class PremiumPageBlobTier(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """
    Specifies the page blob tier to set the blob to. This is only applicable to page
    blobs on premium storage accounts. Please take a look at:
    https://docs.microsoft.com/en-us/azure/storage/storage-premium-storage#scalability-and-performance-targets
    for detailed information on the corresponding IOPS and throughput per PageBlobTier.
    """
    P4: str
    P6: str
    P10: str
    P15: str
    P20: str
    P30: str
    P40: str
    P50: str
    P60: str

class QuickQueryDialect(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies the quick query input/output dialect."""
    DELIMITEDTEXT: str
    DELIMITEDJSON: str
    PARQUET: str

class SequenceNumberAction(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Sequence number actions."""
    INCREMENT: str
    MAX: str
    UPDATE: str

class PublicAccess(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """
    Specifies whether data in the container may be accessed publicly and the level of access.
    """
    OFF: str
    BLOB: str
    CONTAINER: str

class BlobImmutabilityPolicyMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    '''
    Specifies the immutability policy mode to set on the blob.
    "Mutable" can only be returned by service, don\'t set to "Mutable".
    '''
    UNLOCKED: str
    LOCKED: str
    MUTABLE: str

class BlobAnalyticsLogging(GeneratedLogging):
    """Azure Analytics Logging settings.

    :keyword str version:
        The version of Storage Analytics to configure. The default value is 1.0.
    :keyword bool delete:
        Indicates whether all delete requests should be logged. The default value is `False`.
    :keyword bool read:
        Indicates whether all read requests should be logged. The default value is `False`.
    :keyword bool write:
        Indicates whether all write requests should be logged. The default value is `False`.
    :keyword ~azure.storage.blob.RetentionPolicy retention_policy:
        Determines how long the associated data should persist. If not specified the retention
        policy will be disabled by default.
    """
    version: Incomplete
    delete: Incomplete
    read: Incomplete
    write: Incomplete
    retention_policy: Incomplete
    def __init__(self, **kwargs) -> None: ...

class Metrics(GeneratedMetrics):
    """A summary of request statistics grouped by API in hour or minute aggregates
    for blobs.

    :keyword str version:
        The version of Storage Analytics to configure. The default value is 1.0.
    :keyword bool enabled:
        Indicates whether metrics are enabled for the Blob service.
        The default value is `False`.
    :keyword bool include_apis:
        Indicates whether metrics should generate summary statistics for called API operations.
    :keyword ~azure.storage.blob.RetentionPolicy retention_policy:
        Determines how long the associated data should persist. If not specified the retention
        policy will be disabled by default.
    """
    version: Incomplete
    enabled: Incomplete
    include_apis: Incomplete
    retention_policy: Incomplete
    def __init__(self, **kwargs) -> None: ...

class RetentionPolicy(GeneratedRetentionPolicy):
    """The retention policy which determines how long the associated data should
    persist.

    :param bool enabled:
        Indicates whether a retention policy is enabled for the storage service.
        The default value is False.
    :param int days:
        Indicates the number of days that metrics or logging or
        soft-deleted data should be retained. All data older than this value will
        be deleted. If enabled=True, the number of days must be specified.
    """
    def __init__(self, enabled: bool = False, days: Incomplete | None = None) -> None: ...

class StaticWebsite(GeneratedStaticWebsite):
    """The properties that enable an account to host a static website.

    :keyword bool enabled:
        Indicates whether this account is hosting a static website.
        The default value is `False`.
    :keyword str index_document:
        The default name of the index page under each directory.
    :keyword str error_document404_path:
        The absolute path of the custom 404 page.
    :keyword str default_index_document_path:
        Absolute path of the default index page.
    """
    enabled: Incomplete
    index_document: Incomplete
    error_document404_path: Incomplete
    default_index_document_path: Incomplete
    def __init__(self, **kwargs) -> None: ...

class CorsRule(GeneratedCorsRule):
    '''CORS is an HTTP feature that enables a web application running under one
    domain to access resources in another domain. Web browsers implement a
    security restriction known as same-origin policy that prevents a web page
    from calling APIs in a different domain; CORS provides a secure way to
    allow one domain (the origin domain) to call APIs in another domain.

    :param list(str) allowed_origins:
        A list of origin domains that will be allowed via CORS, or "*" to allow
        all domains. The list of must contain at least one entry. Limited to 64
        origin domains. Each allowed origin can have up to 256 characters.
    :param list(str) allowed_methods:
        A list of HTTP methods that are allowed to be executed by the origin.
        The list of must contain at least one entry. For Azure Storage,
        permitted methods are DELETE, GET, HEAD, MERGE, POST, OPTIONS or PUT.
    :keyword list(str) allowed_headers:
        Defaults to an empty list. A list of headers allowed to be part of
        the cross-origin request. Limited to 64 defined headers and 2 prefixed
        headers. Each header can be up to 256 characters.
    :keyword list(str) exposed_headers:
        Defaults to an empty list. A list of response headers to expose to CORS
        clients. Limited to 64 defined headers and two prefixed headers. Each
        header can be up to 256 characters.
    :keyword int max_age_in_seconds:
        The number of seconds that the client/browser should cache a
        preflight response.
    '''
    allowed_origins: Incomplete
    allowed_methods: Incomplete
    allowed_headers: Incomplete
    exposed_headers: Incomplete
    max_age_in_seconds: Incomplete
    def __init__(self, allowed_origins, allowed_methods, **kwargs) -> None: ...

class ContainerProperties(DictMixin):
    '''Blob container\'s properties class.

    Returned ``ContainerProperties`` instances expose these values through a
    dictionary interface, for example: ``container_props["last_modified"]``.
    Additionally, the container name is available as ``container_props["name"]``.

    :ivar str name:
        Name of the container.
    :ivar ~datetime.datetime last_modified:
        A datetime object representing the last time the container was modified.
    :ivar str etag:
        The ETag contains a value that you can use to perform operations
        conditionally.
    :ivar ~azure.storage.blob.LeaseProperties lease:
        Stores all the lease information for the container.
    :ivar str public_access: Specifies whether data in the container may be accessed
        publicly and the level of access.
    :ivar bool has_immutability_policy:
        Represents whether the container has an immutability policy.
    :ivar bool has_legal_hold:
        Represents whether the container has a legal hold.
    :ivar bool immutable_storage_with_versioning_enabled:
        Represents whether immutable storage with versioning enabled on the container.

        .. versionadded:: 12.10.0
            This was introduced in API version \'2020-10-02\'.

    :ivar dict metadata: A dict with name-value pairs to associate with the
        container as metadata.
    :ivar ~azure.storage.blob.ContainerEncryptionScope encryption_scope:
        The default encryption scope configuration for the container.
    :ivar bool deleted:
        Whether this container was deleted.
    :ivar str version:
        The version of a deleted container.
    '''
    name: Incomplete
    last_modified: Incomplete
    etag: Incomplete
    lease: Incomplete
    public_access: Incomplete
    has_immutability_policy: Incomplete
    deleted: Incomplete
    version: Incomplete
    has_legal_hold: Incomplete
    metadata: Incomplete
    encryption_scope: Incomplete
    immutable_storage_with_versioning_enabled: Incomplete
    def __init__(self, **kwargs) -> None: ...

class ContainerPropertiesPaged(PageIterator):
    '''An Iterable of Container properties.

    :ivar str service_endpoint: The service URL.
    :ivar str prefix: A container name prefix being used to filter the list.
    :ivar str marker: The continuation token of the current page of results.
    :ivar int results_per_page: The maximum number of results retrieved per API call.
    :ivar str continuation_token: The continuation token to retrieve the next page of results.
    :ivar str location_mode: The location mode being used to list results. The available
        options include "primary" and "secondary".
    :ivar current_page: The current page of listed results.
    :vartype current_page: list(~azure.storage.blob.ContainerProperties)

    :param callable command: Function to retrieve the next page of items.
    :param str prefix: Filters the results to return only containers whose names
        begin with the specified prefix.
    :param int results_per_page: The maximum number of container names to retrieve per
        call.
    :param str continuation_token: An opaque continuation token.
    '''
    service_endpoint: Incomplete
    prefix: Incomplete
    marker: Incomplete
    results_per_page: Incomplete
    location_mode: Incomplete
    current_page: Incomplete
    def __init__(self, command, prefix: Incomplete | None = None, results_per_page: Incomplete | None = None, continuation_token: Incomplete | None = None) -> None: ...

class ImmutabilityPolicy(DictMixin):
    '''Optional parameters for setting the immutability policy of a blob, blob snapshot or blob version.

    .. versionadded:: 12.10.0
        This was introduced in API version \'2020-10-02\'.

    :keyword ~datetime.datetime expiry_time:
        Specifies the date time when the blobs immutability policy is set to expire.
    :keyword str or ~azure.storage.blob.BlobImmutabilityPolicyMode policy_mode:
        Specifies the immutability policy mode to set on the blob.
        Possible values to set include: "Locked", "Unlocked".
        "Mutable" can only be returned by service, don\'t set to "Mutable".
    '''
    expiry_time: Incomplete
    policy_mode: Incomplete
    def __init__(self, **kwargs) -> None: ...

class FilteredBlob(DictMixin):
    """Blob info from a Filter Blobs API call.

    :ivar name: Blob name
    :type name: str
    :ivar container_name: Container name.
    :type container_name: str
    :ivar tags: Key value pairs of blob tags.
    :type tags: Dict[str, str]
    """
    name: Incomplete
    container_name: Incomplete
    tags: Incomplete
    def __init__(self, **kwargs) -> None: ...

class LeaseProperties(DictMixin):
    """Blob Lease Properties.

    :ivar str status:
        The lease status of the blob. Possible values: locked|unlocked
    :ivar str state:
        Lease state of the blob. Possible values: available|leased|expired|breaking|broken
    :ivar str duration:
        When a blob is leased, specifies whether the lease is of infinite or fixed duration.
    """
    status: Incomplete
    state: Incomplete
    duration: Incomplete
    def __init__(self, **kwargs) -> None: ...

class ContentSettings(DictMixin):
    """The content settings of a blob.

    :param str content_type:
        The content type specified for the blob. If no content type was
        specified, the default content type is application/octet-stream.
    :param str content_encoding:
        If the content_encoding has previously been set
        for the blob, that value is stored.
    :param str content_language:
        If the content_language has previously been set
        for the blob, that value is stored.
    :param str content_disposition:
        content_disposition conveys additional information about how to
        process the response payload, and also can be used to attach
        additional metadata. If content_disposition has previously been set
        for the blob, that value is stored.
    :param str cache_control:
        If the cache_control has previously been set for
        the blob, that value is stored.
    :param bytearray content_md5:
        If the content_md5 has been set for the blob, this response
        header is stored so that the client can check for message content
        integrity.
    """
    content_type: Incomplete
    content_encoding: Incomplete
    content_language: Incomplete
    content_md5: Incomplete
    content_disposition: Incomplete
    cache_control: Incomplete
    def __init__(self, content_type: Incomplete | None = None, content_encoding: Incomplete | None = None, content_language: Incomplete | None = None, content_disposition: Incomplete | None = None, cache_control: Incomplete | None = None, content_md5: Incomplete | None = None, **kwargs) -> None: ...

class CopyProperties(DictMixin):
    """Blob Copy Properties.

    These properties will be `None` if this blob has never been the destination
    in a Copy Blob operation, or if this blob has been modified after a concluded
    Copy Blob operation, for example, using Set Blob Properties, Upload Blob, or Commit Block List.

    :ivar str id:
        String identifier for the last attempted Copy Blob operation where this blob
        was the destination blob.
    :ivar str source:
        URL up to 2 KB in length that specifies the source blob used in the last attempted
        Copy Blob operation where this blob was the destination blob.
    :ivar str status:
        State of the copy operation identified by Copy ID, with these values:
            success:
                Copy completed successfully.
            pending:
                Copy is in progress. Check copy_status_description if intermittent,
                non-fatal errors impede copy progress but don't cause failure.
            aborted:
                Copy was ended by Abort Copy Blob.
            failed:
                Copy failed. See copy_status_description for failure details.
    :ivar str progress:
        Contains the number of bytes copied and the total bytes in the source in the last
        attempted Copy Blob operation where this blob was the destination blob. Can show
        between 0 and Content-Length bytes copied.
    :ivar ~datetime.datetime completion_time:
        Conclusion time of the last attempted Copy Blob operation where this blob was the
        destination blob. This value can specify the time of a completed, aborted, or
        failed copy attempt.
    :ivar str status_description:
        Only appears when x-ms-copy-status is failed or pending. Describes cause of fatal
        or non-fatal copy operation failure.
    :ivar bool incremental_copy:
        Copies the snapshot of the source page blob to a destination page blob.
        The snapshot is copied such that only the differential changes between
        the previously copied snapshot are transferred to the destination
    :ivar ~datetime.datetime destination_snapshot:
        Included if the blob is incremental copy blob or incremental copy snapshot,
        if x-ms-copy-status is success. Snapshot time of the last successful
        incremental copy snapshot for this blob.
    """
    id: Incomplete
    source: Incomplete
    status: Incomplete
    progress: Incomplete
    completion_time: Incomplete
    status_description: Incomplete
    incremental_copy: Incomplete
    destination_snapshot: Incomplete
    def __init__(self, **kwargs) -> None: ...

class BlobBlock(DictMixin):
    """BlockBlob Block class.

    :param str block_id:
        Block id.
    :param str state:
        Block state. Possible values: committed|uncommitted
    :ivar int size:
        Block size in bytes.
    """
    id: Incomplete
    state: Incomplete
    size: Incomplete
    def __init__(self, block_id, state=...) -> None: ...

class PageRange(DictMixin):
    """Page Range for page blob.

    :param int start:
        Start of page range in bytes.
    :param int end:
        End of page range in bytes.
    :ivar bool cleared:
        Whether the range has been cleared.
    """
    start: Incomplete
    end: Incomplete
    cleared: Incomplete
    def __init__(self, start: Incomplete | None = None, end: Incomplete | None = None, *, cleared: bool = False) -> None: ...

class PageRangePaged(PageIterator):
    results_per_page: Incomplete
    location_mode: Incomplete
    current_page: Incomplete
    def __init__(self, command, results_per_page: Incomplete | None = None, continuation_token: Incomplete | None = None) -> None: ...

class AccessPolicy(GenAccessPolicy):
    """Access Policy class used by the set and get access policy methods in each service.

    A stored access policy can specify the start time, expiry time, and
    permissions for the Shared Access Signatures with which it's associated.
    Depending on how you want to control access to your resource, you can
    specify all of these parameters within the stored access policy, and omit
    them from the URL for the Shared Access Signature. Doing so permits you to
    modify the associated signature's behavior at any time, as well as to revoke
    it. Or you can specify one or more of the access policy parameters within
    the stored access policy, and the others on the URL. Finally, you can
    specify all of the parameters on the URL. In this case, you can use the
    stored access policy to revoke the signature, but not to modify its behavior.

    Together the Shared Access Signature and the stored access policy must
    include all fields required to authenticate the signature. If any required
    fields are missing, the request will fail. Likewise, if a field is specified
    both in the Shared Access Signature URL and in the stored access policy, the
    request will fail with status code 400 (Bad Request).

    :param permission:
        The permissions associated with the shared access signature. The
        user is restricted to operations allowed by the permissions.
        Required unless an id is given referencing a stored access policy
        which contains this field. This field must be omitted if it has been
        specified in an associated stored access policy.
    :type permission: str or ~azure.storage.blob.ContainerSasPermissions
    :param expiry:
        The time at which the shared access signature becomes invalid.
        Required unless an id is given referencing a stored access policy
        which contains this field. This field must be omitted if it has
        been specified in an associated stored access policy. Azure will always
        convert values to UTC. If a date is passed in without timezone info, it
        is assumed to be UTC.
    :type expiry: ~datetime.datetime or str
    :param start:
        The time at which the shared access signature becomes valid. If
        omitted, start time for this call is assumed to be the time when the
        storage service receives the request. Azure will always convert values
        to UTC. If a date is passed in without timezone info, it is assumed to
        be UTC.
    :type start: ~datetime.datetime or str
    """
    start: Incomplete
    expiry: Incomplete
    permission: Incomplete
    def __init__(self, permission: Incomplete | None = None, expiry: Incomplete | None = None, start: Incomplete | None = None) -> None: ...

class ContainerSasPermissions:
    """ContainerSasPermissions class to be used with the
    :func:`~azure.storage.blob.generate_container_sas` function and
    for the AccessPolicies used with
    :func:`~azure.storage.blob.ContainerClient.set_container_access_policy`.

    :param bool read:
        Read the content, properties, metadata or block list of any blob in the
        container. Use any blob in the container as the source of a copy operation.
    :param bool write:
        For any blob in the container, create or write content, properties,
        metadata, or block list. Snapshot or lease the blob. Resize the blob
        (page blob only). Use the blob as the destination of a copy operation
        within the same account. Note: You cannot grant permissions to read or
        write container properties or metadata, nor to lease a container, with
        a container SAS. Use an account SAS instead.
    :param bool delete:
        Delete any blob in the container. Note: You cannot grant permissions to
        delete a container with a container SAS. Use an account SAS instead.
    :param bool delete_previous_version:
        Delete the previous blob version for the versioning enabled storage account.
    :param bool list:
        List blobs in the container.
    :param bool tag:
        Set or get tags on the blobs in the container.
    :keyword bool add:
        Add a block to an append blob.
    :keyword bool create:
        Write a new blob, snapshot a blob, or copy a blob to a new blob.
    :keyword bool permanent_delete:
        To enable permanent delete on the blob is permitted.
    :keyword bool filter_by_tags:
        To enable finding blobs by tags.
    :keyword bool move:
        Move a blob or a directory and its contents to a new location.
    :keyword bool execute:
        Get the system properties and, if the hierarchical namespace is enabled for the storage account,
        get the POSIX ACL of a blob.
    :keyword bool set_immutability_policy:
        To enable operations related to set/delete immutability policy.
        To get immutability policy, you just need read permission.
    """
    read: Incomplete
    add: Incomplete
    create: Incomplete
    write: Incomplete
    delete: Incomplete
    delete_previous_version: Incomplete
    permanent_delete: Incomplete
    list: Incomplete
    tag: Incomplete
    filter_by_tags: Incomplete
    move: Incomplete
    execute: Incomplete
    set_immutability_policy: Incomplete
    def __init__(self, read: bool = False, write: bool = False, delete: bool = False, list: bool = False, delete_previous_version: bool = False, tag: bool = False, **kwargs) -> None: ...
    @classmethod
    def from_string(cls, permission):
        '''Create a ContainerSasPermissions from a string.

        To specify read, write, delete, or list permissions you need only to
        include the first letter of the word in the string. E.g. For read and
        write permissions, you would provide a string "rw".

        :param str permission: The string which dictates the read, write, delete,
            and list permissions.
        :return: A ContainerSasPermissions object
        :rtype: ~azure.storage.blob.ContainerSasPermissions
        '''

class BlobSasPermissions:
    """BlobSasPermissions class to be used with the
    :func:`~azure.storage.blob.generate_blob_sas` function.

    :param bool read:
        Read the content, properties, metadata and block list. Use the blob as
        the source of a copy operation.
    :param bool add:
        Add a block to an append blob.
    :param bool create:
        Write a new blob, snapshot a blob, or copy a blob to a new blob.
    :param bool write:
        Create or write content, properties, metadata, or block list. Snapshot
        or lease the blob. Resize the blob (page blob only). Use the blob as the
        destination of a copy operation within the same account.
    :param bool delete:
        Delete the blob.
    :param bool delete_previous_version:
        Delete the previous blob version for the versioning enabled storage account.
    :param bool tag:
        Set or get tags on the blob.
    :keyword bool permanent_delete:
        To enable permanent delete on the blob is permitted.
    :keyword bool move:
        Move a blob or a directory and its contents to a new location.
    :keyword bool execute:
        Get the system properties and, if the hierarchical namespace is enabled for the storage account,
        get the POSIX ACL of a blob.
    :keyword bool set_immutability_policy:
        To enable operations related to set/delete immutability policy.
        To get immutability policy, you just need read permission.
    """
    read: Incomplete
    add: Incomplete
    create: Incomplete
    write: Incomplete
    delete: Incomplete
    delete_previous_version: Incomplete
    permanent_delete: Incomplete
    tag: Incomplete
    move: Incomplete
    execute: Incomplete
    set_immutability_policy: Incomplete
    def __init__(self, read: bool = False, add: bool = False, create: bool = False, write: bool = False, delete: bool = False, delete_previous_version: bool = False, tag: bool = False, **kwargs) -> None: ...
    @classmethod
    def from_string(cls, permission):
        '''Create a BlobSasPermissions from a string.

        To specify read, add, create, write, or delete permissions you need only to
        include the first letter of the word in the string. E.g. For read and
        write permissions, you would provide a string "rw".

        :param str permission: The string which dictates the read, add, create,
            write, or delete permissions.
        :return: A BlobSasPermissions object
        :rtype: ~azure.storage.blob.BlobSasPermissions
        '''

class CustomerProvidedEncryptionKey:
    """
    All data in Azure Storage is encrypted at-rest using an account-level encryption key.
    In versions 2018-06-17 and newer, you can manage the key used to encrypt blob contents
    and application metadata per-blob by providing an AES-256 encryption key in requests to the storage service.

    When you use a customer-provided key, Azure Storage does not manage or persist your key.
    When writing data to a blob, the provided key is used to encrypt your data before writing it to disk.
    A SHA-256 hash of the encryption key is written alongside the blob contents,
    and is used to verify that all subsequent operations against the blob use the same encryption key.
    This hash cannot be used to retrieve the encryption key or decrypt the contents of the blob.
    When reading a blob, the provided key is used to decrypt your data after reading it from disk.
    In both cases, the provided encryption key is securely discarded
    as soon as the encryption or decryption process completes.

    :param str key_value:
        Base64-encoded AES-256 encryption key value.
    :param str key_hash:
        Base64-encoded SHA256 of the encryption key.
    :ivar str algorithm:
        Specifies the algorithm to use when encrypting data using the given key. Must be AES256.
    """
    key_value: Incomplete
    key_hash: Incomplete
    algorithm: str
    def __init__(self, key_value, key_hash) -> None: ...

class ContainerEncryptionScope:
    """The default encryption scope configuration for a container.

    This scope is used implicitly for all future writes within the container,
    but can be overridden per blob operation.

    .. versionadded:: 12.2.0

    :param str default_encryption_scope:
        Specifies the default encryption scope to set on the container and use for
        all future writes.
    :param bool prevent_encryption_scope_override:
        If true, prevents any request from specifying a different encryption scope than the scope
        set on the container. Default value is false.
    """
    default_encryption_scope: Incomplete
    prevent_encryption_scope_override: Incomplete
    def __init__(self, default_encryption_scope, **kwargs) -> None: ...

class DelimitedJsonDialect(DictMixin):
    """Defines the input or output JSON serialization for a blob data query.

    :keyword str delimiter: The line separator character, default value is '
'
    """
    delimiter: Incomplete
    def __init__(self, **kwargs) -> None: ...

class DelimitedTextDialect(DictMixin):
    '''Defines the input or output delimited (CSV) serialization for a blob query request.

    :keyword str delimiter:
        Column separator, defaults to \',\'.
    :keyword str quotechar:
        Field quote, defaults to \'"\'.
    :keyword str lineterminator:
        Record separator, defaults to \'\\\\n\'.
    :keyword str escapechar:
        Escape char, defaults to empty.
    :keyword bool has_header:
        Whether the blob data includes headers in the first line. The default value is False, meaning that the
        data will be returned inclusive of the first line. If set to True, the data will be returned exclusive
        of the first line.
    '''
    delimiter: Incomplete
    quotechar: Incomplete
    lineterminator: Incomplete
    escapechar: Incomplete
    has_header: Incomplete
    def __init__(self, **kwargs) -> None: ...

class ArrowDialect(ArrowField):
    """field of an arrow schema.

    All required parameters must be populated in order to send to Azure.

    :param ~azure.storage.blob.ArrowType type: Arrow field type.
    :keyword str name: The name of the field.
    :keyword int precision: The precision of the field.
    :keyword int scale: The scale of the field.
    """
    def __init__(self, type, **kwargs) -> None: ...

class ArrowType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    INT64: str
    BOOL: str
    TIMESTAMP_MS: str
    STRING: str
    DOUBLE: str
    DECIMAL: str

class ObjectReplicationPolicy(DictMixin):
    """Policy id and rule ids applied to a blob.

    :ivar str policy_id:
        Policy id for the blob. A replication policy gets created (policy id) when creating a source/destination pair.
    :ivar list(~azure.storage.blob.ObjectReplicationRule) rules:
        Within each policy there may be multiple replication rules.
        e.g. rule 1= src/container/.pdf to dst/container2/; rule2 = src/container1/.jpg to dst/container3
    """
    policy_id: Incomplete
    rules: Incomplete
    def __init__(self, **kwargs) -> None: ...

class BlobProperties(DictMixin):
    """Blob Properties."""
    name: str
    container: str
    snapshot: str | None
    blob_type: BlobType
    metadata: Dict[str, str]
    last_modified: datetime
    etag: str
    size: int
    content_range: str | None
    append_blob_committed_block_count: int | None
    is_append_blob_sealed: bool | None
    page_blob_sequence_number: int | None
    server_encrypted: bool
    copy: CopyProperties
    content_settings: ContentSettings
    lease: LeaseProperties
    blob_tier: StandardBlobTier | None
    rehydrate_priority: str | None
    blob_tier_change_time: datetime | None
    blob_tier_inferred: bool | None
    deleted: bool | None
    deleted_time: datetime | None
    remaining_retention_days: int | None
    creation_time: datetime
    archive_status: str | None
    encryption_key_sha256: str | None
    encryption_scope: str | None
    request_server_encrypted: bool | None
    object_replication_source_properties: List[ObjectReplicationPolicy] | None
    object_replication_destination_policy: str | None
    last_accessed_on: datetime | None
    tag_count: int | None
    tags: Dict[str, str] | None
    has_versions_only: bool | None
    immutability_policy: ImmutabilityPolicy
    has_legal_hold: bool | None
    version_id: Incomplete
    is_current_version: Incomplete
    encrypted_metadata: Incomplete
    def __init__(self, **kwargs) -> None: ...

class ObjectReplicationRule(DictMixin):
    '''Policy id and rule ids applied to a blob.

    :ivar str rule_id:
        Rule id.
    :ivar str status:
        The status of the rule. It could be "Complete" or "Failed"
    '''
    rule_id: Incomplete
    status: Incomplete
    def __init__(self, **kwargs) -> None: ...

class BlobQueryError:
    """The error happened during quick query operation.

    :ivar str error:
        The name of the error.
    :ivar bool is_fatal:
        If true, this error prevents further query processing. More result data may be returned,
        but there is no guarantee that all of the original data will be processed.
        If false, this error does not prevent further query processing.
    :ivar str description:
        A description of the error.
    :ivar int position:
        The blob offset at which the error occurred.
    """
    error: Incomplete
    is_fatal: Incomplete
    description: Incomplete
    position: Incomplete
    def __init__(self, error: Incomplete | None = None, is_fatal: bool = False, description: Incomplete | None = None, position: Incomplete | None = None) -> None: ...
