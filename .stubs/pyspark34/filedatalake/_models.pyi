from ._shared.models import DictMixin as DictMixin
from _typeshed import Incomplete
from azure.core import CaseInsensitiveEnumMeta
from azure.storage.blob import AccessPolicy as BlobAccessPolicy, AccountSasPermissions as BlobAccountSasPermissions, ArrowDialect as BlobArrowDialect, ContainerEncryptionScope as BlobContainerEncryptionScope, ContentSettings as BlobContentSettings, CustomerProvidedEncryptionKey as BlobCustomerProvidedEncryptionKey, DelimitedJsonDialect as BlobDelimitedJSON, DelimitedTextDialect as BlobDelimitedTextDialect, LeaseProperties as BlobLeaseProperties, ResourceTypes as BlobResourceTypes, UserDelegationKey as BlobUserDelegationKey
from azure.storage.blob._generated.models import CorsRule as GenCorsRule, Logging as GenLogging, Metrics as GenMetrics, RetentionPolicy as GenRetentionPolicy, StaticWebsite as GenStaticWebsite
from azure.storage.blob._models import ContainerPropertiesPaged
from enum import Enum

class FileSystemProperties(DictMixin):
    '''File System properties class.

    :ivar str name:
        Name of the filesystem.
    :ivar ~datetime.datetime last_modified:
        A datetime object representing the last time the file system was modified.
    :ivar str etag:
        The ETag contains a value that you can use to perform operations
        conditionally.
    :ivar ~azure.storage.filedatalake.LeaseProperties lease:
        Stores all the lease information for the file system.
    :ivar str public_access: Specifies whether data in the file system may be accessed
        publicly and the level of access.
    :ivar bool has_immutability_policy:
        Represents whether the file system has an immutability policy.
    :ivar bool has_legal_hold:
        Represents whether the file system has a legal hold.
    :ivar dict metadata: A dict with name-value pairs to associate with the
        file system as metadata.
    :ivar ~azure.storage.filedatalake.EncryptionScopeOptions encryption_scope:
        The default encryption scope configuration for the file system.
    :ivar bool deleted:
        Whether this file system was deleted.
    :ivar str deleted_version:
        The version of a deleted file system.

    Returned ``FileSystemProperties`` instances expose these values through a
    dictionary interface, for example: ``file_system_props["last_modified"]``.
    Additionally, the file system name is available as ``file_system_props["name"]``.
    '''
    name: Incomplete
    last_modified: Incomplete
    etag: Incomplete
    lease: Incomplete
    public_access: Incomplete
    has_immutability_policy: Incomplete
    has_legal_hold: Incomplete
    metadata: Incomplete
    deleted: Incomplete
    deleted_version: Incomplete
    encryption_scope: Incomplete
    def __init__(self, **kwargs) -> None: ...

class FileSystemPropertiesPaged(ContainerPropertiesPaged):
    '''An Iterable of File System properties.

    :ivar str service_endpoint: The service URL.
    :ivar str prefix: A file system name prefix being used to filter the list.
    :ivar str marker: The continuation token of the current page of results.
    :ivar int results_per_page: The maximum number of results retrieved per API call.
    :ivar str continuation_token: The continuation token to retrieve the next page of results.
    :ivar str location_mode: The location mode being used to list results. The available
        options include "primary" and "secondary".
    :ivar current_page: The current page of listed results.
    :vartype current_page: list(~azure.storage.filedatalake.FileSystemProperties)

    :param callable command: Function to retrieve the next page of items.
    :param str prefix: Filters the results to return only file systems whose names
        begin with the specified prefix.
    :param int results_per_page: The maximum number of file system names to retrieve per
        call.
    :param str continuation_token: An opaque continuation token.
    '''
    def __init__(self, *args, **kwargs) -> None: ...

class DirectoryProperties(DictMixin):
    """
    :ivar str name: name of the directory
    :ivar str owner: The owner of the file or directory.
    :ivar str group: The owning group of the file or directory.
    :ivar str permissions: The permissions that are set for user, group, and other on the file or directory.
        Each individual permission is in [r,w,x,-]{3} format.
    :ivar str etag: The ETag contains a value that you can use to perform operations
        conditionally.
    :ivar bool deleted: if the current directory marked as deleted
    :ivar dict metadata: Name-value pairs associated with the directory as metadata.
    :ivar str encryption_scope:
        A predefined encryption scope used to encrypt the data on the service. An encryption
        scope can be created using the Management API and referenced here by name. If a default
        encryption scope has been defined at the file system, this value will override it if the
        file system level scope is configured to allow overrides. Otherwise an error will be raised.
    :ivar ~azure.storage.filedatalake.LeaseProperties lease:
        Stores all the lease information for the directory.
    :ivar ~datetime.datetime last_modified:
        A datetime object representing the last time the directory was modified.
    :ivar ~datetime.datetime creation_time:
        Indicates when the directory was created, in UTC.
    :ivar int remaining_retention_days: The number of days that the directory will be retained
        before being permanently deleted by the service.
    :var ~azure.storage.filedatalake.ContentSettings content_settings:
    """
    name: Incomplete
    etag: Incomplete
    deleted: bool
    metadata: Incomplete
    lease: Incomplete
    last_modified: Incomplete
    creation_time: Incomplete
    deleted_time: Incomplete
    remaining_retention_days: Incomplete
    encryption_scope: Incomplete
    owner: Incomplete
    group: Incomplete
    permissions: Incomplete
    def __init__(self, **kwargs) -> None: ...

class FileProperties(DictMixin):
    """
    :ivar str name: name of the file
    :ivar str owner: The owner of the file or directory.
    :ivar str group: The owning group of the file or directory.
    :ivar str permissions: The permissions that are set for user, group, and other on the file or directory.
        Each individual permission is in [r,w,x,-]{3} format.
    :ivar str etag: The ETag contains a value that you can use to perform operations
        conditionally.
    :ivar bool deleted: if the current file marked as deleted
    :ivar dict metadata: Name-value pairs associated with the file as metadata.
    :ivar str encryption_scope:
        A predefined encryption scope used to encrypt the data on the service. An encryption
        scope can be created using the Management API and referenced here by name. If a default
        encryption scope has been defined at the file system, this value will override it if the
        file system level scope is configured to allow overrides. Otherwise an error will be raised.
    :ivar ~azure.storage.filedatalake.LeaseProperties lease:
        Stores all the lease information for the file.
    :ivar ~datetime.datetime last_modified:
        A datetime object representing the last time the file was modified.
    :ivar ~datetime.datetime creation_time:
        Indicates when the file was created, in UTC.
    :ivar int size: size of the file
    :ivar int remaining_retention_days: The number of days that the file will be retained
        before being permanently deleted by the service.
    :ivar str encryption_context: Specifies the encryption context to set on the file.
    :var ~azure.storage.filedatalake.ContentSettings content_settings:
    """
    name: Incomplete
    etag: Incomplete
    deleted: bool
    metadata: Incomplete
    lease: Incomplete
    last_modified: Incomplete
    creation_time: Incomplete
    size: Incomplete
    deleted_time: Incomplete
    expiry_time: Incomplete
    remaining_retention_days: Incomplete
    content_settings: Incomplete
    encryption_scope: Incomplete
    encryption_context: Incomplete
    owner: Incomplete
    group: Incomplete
    permissions: Incomplete
    def __init__(self, **kwargs) -> None: ...

class PathProperties(DictMixin):
    """Path properties listed by get_paths api.

    :ivar str name: The full path for a file or directory.
    :ivar str owner: The owner of the file or directory.
    :ivar str group: The owning group of the file or directory.
    :ivar str permissions: The permissions that are set for user, group, and other on the file or directory.
        Each individual permission is in [r,w,x,-]{3} format.
    :ivar datetime last_modified:  A datetime object representing the last time the directory/file was modified.
    :ivar bool is_directory: Is the path a directory or not.
    :ivar str etag: The ETag contains a value that you can use to perform operations
        conditionally.
    :ivar int content_length: The size of file if the path is a file.
    :ivar datetime creation_time: The creation time of the file/directory.
    :ivar datetime expiry_time: The expiry time of the file/directory.
    :ivar str encryption_scope:
        A predefined encryption scope used to encrypt the data on the service. An encryption
        scope can be created using the Management API and referenced here by name. If a default
        encryption scope has been defined at the file system, this value will override it if the
        file system level scope is configured to allow overrides. Otherwise an error will be raised.
    :ivar str encryption_context: Specifies the encryption context to set on the file.
    """
    name: Incomplete
    owner: Incomplete
    group: Incomplete
    permissions: Incomplete
    last_modified: Incomplete
    is_directory: Incomplete
    etag: Incomplete
    content_length: Incomplete
    creation_time: Incomplete
    expiry_time: Incomplete
    encryption_scope: Incomplete
    encryption_context: Incomplete
    def __init__(self, **kwargs) -> None: ...

class LeaseProperties(BlobLeaseProperties):
    """DataLake Lease Properties.

    :ivar str status:
        The lease status of the file. Possible values: locked|unlocked
    :ivar str state:
        Lease state of the file. Possible values: available|leased|expired|breaking|broken
    :ivar str duration:
        When a file is leased, specifies whether the lease is of infinite or fixed duration.
    """

class ContentSettings(BlobContentSettings):
    """The content settings of a file or directory.

    :ivar str content_type:
        The content type specified for the file or directory. If no content type was
        specified, the default content type is application/octet-stream.
    :ivar str content_encoding:
        If the content_encoding has previously been set
        for the file, that value is stored.
    :ivar str content_language:
        If the content_language has previously been set
        for the file, that value is stored.
    :ivar str content_disposition:
        content_disposition conveys additional information about how to
        process the response payload, and also can be used to attach
        additional metadata. If content_disposition has previously been set
        for the file, that value is stored.
    :ivar str cache_control:
        If the cache_control has previously been set for
        the file, that value is stored.
    :ivar bytearray content_md5:
        If the content_md5 has been set for the file, this response
        header is stored so that the client can check for message content
        integrity.
    :keyword str content_type:
        The content type specified for the file or directory. If no content type was
        specified, the default content type is application/octet-stream.
    :keyword str content_encoding:
        If the content_encoding has previously been set
        for the file, that value is stored.
    :keyword str content_language:
        If the content_language has previously been set
        for the file, that value is stored.
    :keyword str content_disposition:
        content_disposition conveys additional information about how to
        process the response payload, and also can be used to attach
        additional metadata. If content_disposition has previously been set
        for the file, that value is stored.
    :keyword str cache_control:
        If the cache_control has previously been set for
        the file, that value is stored.
    :keyword bytearray content_md5:
        If the content_md5 has been set for the file, this response
        header is stored so that the client can check for message content
        integrity.
    """
    def __init__(self, **kwargs) -> None: ...

class AccountSasPermissions(BlobAccountSasPermissions):
    def __init__(self, read: bool = False, write: bool = False, delete: bool = False, list: bool = False, create: bool = False) -> None: ...

class FileSystemSasPermissions:
    """FileSystemSasPermissions class to be used with the
    :func:`~azure.storage.filedatalake.generate_file_system_sas` function.

    :param bool read:
        Read the content, properties, metadata etc.
    :param bool write:
        Create or write content, properties, metadata. Lease the file system.
    :param bool delete:
        Delete the file system.
    :param bool list:
        List paths in the file system.
    :keyword bool add:
        Append data to a file in the directory.
    :keyword bool create:
        Write a new file, snapshot a file, or copy a file to a new file.
    :keyword bool move:
        Move any file in the directory to a new location.
        Note the move operation can optionally be restricted to the child file or directory owner or
        the parent directory owner if the saoid parameter is included in the token and the sticky bit is set
        on the parent directory.
    :keyword bool execute:
        Get the status (system defined properties) and ACL of any file in the directory.
        If the caller is the owner, set access control on any file in the directory.
    :keyword bool manage_ownership:
        Allows the user to set owner, owning group, or act as the owner when renaming or deleting a file or directory
        within a folder that has the sticky bit set.
    :keyword bool manage_access_control:
         Allows the user to set permissions and POSIX ACLs on files and directories.
    """
    read: Incomplete
    add: Incomplete
    create: Incomplete
    write: Incomplete
    delete: Incomplete
    list: Incomplete
    move: Incomplete
    execute: Incomplete
    manage_ownership: Incomplete
    manage_access_control: Incomplete
    def __init__(self, read: bool = False, write: bool = False, delete: bool = False, list: bool = False, **kwargs) -> None: ...
    @classmethod
    def from_string(cls, permission):
        '''Create a FileSystemSasPermissions from a string.

        To specify read, write, or delete permissions you need only to
        include the first letter of the word in the string. E.g. For read and
        write permissions, you would provide a string "rw".

        :param str permission: The string which dictates the read, add, create,
            write, or delete permissions.
        :return: A FileSystemSasPermissions object
        :rtype: ~azure.storage.filedatalake.FileSystemSasPermissions
        '''

class DirectorySasPermissions:
    """DirectorySasPermissions class to be used with the
    :func:`~azure.storage.filedatalake.generate_directory_sas` function.

    :param bool read:
        Read the content, properties, metadata etc.
    :param bool create:
        Create a new directory
    :param bool write:
        Create or write content, properties, metadata. Lease the directory.
    :param bool delete:
        Delete the directory.
    :keyword bool add:
        Append data to a file in the directory.
    :keyword bool list:
        List any files in the directory. Implies Execute.
    :keyword bool move:
        Move any file in the directory to a new location.
        Note the move operation can optionally be restricted to the child file or directory owner or
        the parent directory owner if the saoid parameter is included in the token and the sticky bit is set
        on the parent directory.
    :keyword bool execute:
        Get the status (system defined properties) and ACL of any file in the directory.
        If the caller is the owner, set access control on any file in the directory.
    :keyword bool manage_ownership:
        Allows the user to set owner, owning group, or act as the owner when renaming or deleting a file or directory
        within a folder that has the sticky bit set.
    :keyword bool manage_access_control:
         Allows the user to set permissions and POSIX ACLs on files and directories.
    """
    read: Incomplete
    add: Incomplete
    create: Incomplete
    write: Incomplete
    delete: Incomplete
    list: Incomplete
    move: Incomplete
    execute: Incomplete
    manage_ownership: Incomplete
    manage_access_control: Incomplete
    def __init__(self, read: bool = False, create: bool = False, write: bool = False, delete: bool = False, **kwargs) -> None: ...
    @classmethod
    def from_string(cls, permission):
        '''Create a DirectorySasPermissions from a string.

        To specify read, create, write, or delete permissions you need only to
        include the first letter of the word in the string. E.g. For read and
        write permissions, you would provide a string "rw".

        :param str permission: The string which dictates the read, add, create,
            write, or delete permissions.
        :return: A DirectorySasPermissions object
        :rtype: ~azure.storage.filedatalake.DirectorySasPermissions
        '''

class FileSasPermissions:
    """FileSasPermissions class to be used with the
    :func:`~azure.storage.filedatalake.generate_file_sas` function.

    :param bool read:
        Read the content, properties, metadata etc. Use the file as
        the source of a read operation.
    :param bool create:
        Write a new file.
    :param bool write:
        Create or write content, properties, metadata. Lease the file.
    :param bool delete:
        Delete the file.
    :keyword bool add:
        Append data to the file.
    :keyword bool move:
        Move any file in the directory to a new location.
        Note the move operation can optionally be restricted to the child file or directory owner or
        the parent directory owner if the saoid parameter is included in the token and the sticky bit is set
        on the parent directory.
    :keyword bool execute:
        Get the status (system defined properties) and ACL of any file in the directory.
        If the caller is the owner, set access control on any file in the directory.
    :keyword bool manage_ownership:
        Allows the user to set owner, owning group, or act as the owner when renaming or deleting a file or directory
        within a folder that has the sticky bit set.
    :keyword bool manage_access_control:
         Allows the user to set permissions and POSIX ACLs on files and directories.
    """
    read: Incomplete
    add: Incomplete
    create: Incomplete
    write: Incomplete
    delete: Incomplete
    move: Incomplete
    execute: Incomplete
    manage_ownership: Incomplete
    manage_access_control: Incomplete
    def __init__(self, read: bool = False, create: bool = False, write: bool = False, delete: bool = False, **kwargs) -> None: ...
    @classmethod
    def from_string(cls, permission):
        '''Create a FileSasPermissions from a string.

        To specify read, write, or delete permissions you need only to
        include the first letter of the word in the string. E.g. For read and
        write permissions, you would provide a string "rw".

        :param str permission: The string which dictates the read, add, create,
            write, or delete permissions.
        :return: A FileSasPermissions object
        :rtype: ~azure.storage.filedatalake.FileSasPermissions
        '''

class AccessPolicy(BlobAccessPolicy):
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
    :type permission: str or ~azure.storage.datalake.FileSystemSasPermissions
    :param expiry:
        The time at which the shared access signature becomes invalid.
        Required unless an id is given referencing a stored access policy
        which contains this field. This field must be omitted if it has
        been specified in an associated stored access policy. Azure will always
        convert values to UTC. If a date is passed in without timezone info, it
        is assumed to be UTC.
    :type expiry: ~datetime.datetime or str
    :keyword start:
        The time at which the shared access signature becomes valid. If
        omitted, start time for this call is assumed to be the time when the
        storage service receives the request. Azure will always convert values
        to UTC. If a date is passed in without timezone info, it is assumed to
        be UTC.
    :paramtype start: ~datetime.datetime or str
    """
    def __init__(self, permission: Incomplete | None = None, expiry: Incomplete | None = None, **kwargs) -> None: ...

class ResourceTypes(BlobResourceTypes):
    """
    Specifies the resource types that are accessible with the account SAS.

    :param bool service:
        Access to service-level APIs (e.g.List File Systems)
    :param bool file_system:
        Access to file_system-level APIs (e.g., Create/Delete file system,
        List Directories/Files)
    :param bool object:
        Access to object-level APIs for
        files(e.g. Create File, etc.)
    """
    def __init__(self, service: bool = False, file_system: bool = False, object: bool = False) -> None: ...

class UserDelegationKey(BlobUserDelegationKey):
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

class PublicAccess(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """
    Specifies whether data in the file system may be accessed publicly and the level of access.
    """
    FILE: str
    FILESYSTEM: str

class LocationMode:
    """
    Specifies the location the request should be sent to. This mode only applies
    for RA-GRS accounts which allow secondary read access. All other account types
    must use PRIMARY.
    """
    PRIMARY: str
    SECONDARY: str

class DelimitedJsonDialect(BlobDelimitedJSON):
    """Defines the input or output JSON serialization for a datalake query.

    :keyword str delimiter: The line separator character, default value is '
'
    """
class DelimitedTextDialect(BlobDelimitedTextDialect):
    '''Defines the input or output delimited (CSV) serialization for a datalake query request.

    :keyword str delimiter:
        Column separator, defaults to \',\'.
    :keyword str quotechar:
        Field quote, defaults to \'"\'.
    :keyword str lineterminator:
        Record separator, defaults to \'
\'.
    :keyword str escapechar:
        Escape char, defaults to empty.
    :keyword bool has_header:
        Whether the blob data includes headers in the first line. The default value is False, meaning that the
        data will be returned inclusive of the first line. If set to True, the data will be returned exclusive
        of the first line.
    '''
class ArrowDialect(BlobArrowDialect):
    """field of an arrow schema.

    All required parameters must be populated in order to send to Azure.

    :param str type: Required.
    :keyword str name: The name of the field.
    :keyword int precision: The precision of the field.
    :keyword int scale: The scale of the field.
    """
class CustomerProvidedEncryptionKey(BlobCustomerProvidedEncryptionKey):
    """
    All data in Azure Storage is encrypted at-rest using an account-level encryption key.
    In versions 2021-06-08 and newer, you can manage the key used to encrypt file contents
    and application metadata per-file by providing an AES-256 encryption key in requests to the storage service.

    When you use a customer-provided key, Azure Storage does not manage or persist your key.
    When writing data to a file, the provided key is used to encrypt your data before writing it to disk.
    A SHA-256 hash of the encryption key is written alongside the file contents,
    and is used to verify that all subsequent operations against the file use the same encryption key.
    This hash cannot be used to retrieve the encryption key or decrypt the contents of the file.
    When reading a file, the provided key is used to decrypt your data after reading it from disk.
    In both cases, the provided encryption key is securely discarded
    as soon as the encryption or decryption process completes.

    :param str key_value:
        Base64-encoded AES-256 encryption key value.
    :param str key_hash:
        Base64-encoded SHA256 of the encryption key.
    :ivar str algorithm:
        Specifies the algorithm to use when encrypting data using the given key. Must be AES256.
    """
class EncryptionScopeOptions(BlobContainerEncryptionScope):
    """The default encryption scope configuration for a file system.

    This scope is used implicitly for all future writes within the file system,
    but can be overridden per blob operation.

    .. versionadded:: 12.9.0

    :param str default_encryption_scope:
        Specifies the default encryption scope to set on the file system and use for
        all future writes.
    :param bool prevent_encryption_scope_override:
        If true, prevents any request from specifying a different encryption scope than the scope
        set on the file system. Default value is false.
    """

class QuickQueryDialect(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies the quick query input/output dialect."""
    DELIMITEDTEXT: str
    DELIMITEDJSON: str
    PARQUET: str

class ArrowType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    INT64: str
    BOOL: str
    TIMESTAMP_MS: str
    STRING: str
    DOUBLE: str
    DECIMAL: str

class DataLakeFileQueryError:
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

class AccessControlChangeCounters(DictMixin):
    """
    AccessControlChangeCounters contains counts of operations that change Access Control Lists recursively.

    :ivar int directories_successful:
        Number of directories where Access Control List has been updated successfully.
    :ivar int files_successful:
        Number of files where Access Control List has been updated successfully.
    :ivar int failure_count:
        Number of paths where Access Control List update has failed.
    """
    directories_successful: Incomplete
    files_successful: Incomplete
    failure_count: Incomplete
    def __init__(self, directories_successful, files_successful, failure_count) -> None: ...

class AccessControlChangeResult(DictMixin):
    """
    AccessControlChangeResult contains result of operations that change Access Control Lists recursively.

    :ivar ~azure.storage.filedatalake.AccessControlChangeCounters counters:
        Contains counts of paths changed from start of the operation.
    :ivar str continuation:
        Optional continuation token.
        Value is present when operation is split into multiple batches and can be used to resume progress.
    """
    counters: Incomplete
    continuation: Incomplete
    def __init__(self, counters, continuation) -> None: ...

class AccessControlChangeFailure(DictMixin):
    """
    Represents an entry that failed to update Access Control List.

    :ivar str name:
        Name of the entry.
    :ivar bool is_directory:
        Indicates whether the entry is a directory.
    :ivar str error_message:
        Indicates the reason why the entry failed to update.
    """
    name: Incomplete
    is_directory: Incomplete
    error_message: Incomplete
    def __init__(self, name, is_directory, error_message) -> None: ...

class AccessControlChanges(DictMixin):
    """
    AccessControlChanges contains batch and cumulative counts of operations
    that change Access Control Lists recursively.
    Additionally it exposes path entries that failed to update while these operations progress.

    :ivar ~azure.storage.filedatalake.AccessControlChangeCounters batch_counters:
        Contains counts of paths changed within single batch.
    :ivar ~azure.storage.filedatalake.AccessControlChangeCounters aggregate_counters:
        Contains counts of paths changed from start of the operation.
    :ivar list(~azure.storage.filedatalake.AccessControlChangeFailure) batch_failures:
        List of path entries that failed to update Access Control List within single batch.
    :ivar str continuation:
        An opaque continuation token that may be used to resume the operations in case of failures.
    """
    batch_counters: Incomplete
    aggregate_counters: Incomplete
    batch_failures: Incomplete
    continuation: Incomplete
    def __init__(self, batch_counters, aggregate_counters, batch_failures, continuation) -> None: ...

class DeletedPathProperties(DictMixin):
    """
    Properties populated for a deleted path.

    :ivar str name:
        The name of the file in the path.
    :ivar ~datetime.datetime deleted_time:
        A datetime object representing the time at which the path was deleted.
    :ivar int remaining_retention_days:
        The number of days that the path will be retained before being permanently deleted by the service.
    :ivar str deletion_id:
        The id associated with the deleted path.
    """
    name: Incomplete
    deleted_time: Incomplete
    remaining_retention_days: Incomplete
    deletion_id: Incomplete
    def __init__(self, **kwargs) -> None: ...

class AnalyticsLogging(GenLogging):
    """Azure Analytics Logging settings.

    :keyword str version:
        The version of Storage Analytics to configure. The default value is 1.0.
    :keyword bool delete:
        Indicates whether all delete requests should be logged. The default value is `False`.
    :keyword bool read:
        Indicates whether all read requests should be logged. The default value is `False`.
    :keyword bool write:
        Indicates whether all write requests should be logged. The default value is `False`.
    :keyword ~azure.storage.filedatalake.RetentionPolicy retention_policy:
        Determines how long the associated data should persist. If not specified the retention
        policy will be disabled by default.
    """
    version: Incomplete
    delete: Incomplete
    read: Incomplete
    write: Incomplete
    retention_policy: Incomplete
    def __init__(self, **kwargs) -> None: ...

class Metrics(GenMetrics):
    """A summary of request statistics grouped by API in hour or minute aggregates.

    :keyword str version:
        The version of Storage Analytics to configure. The default value is 1.0.
    :keyword bool enabled:
        Indicates whether metrics are enabled for the Datalake service.
        The default value is `False`.
    :keyword bool include_apis:
        Indicates whether metrics should generate summary statistics for called API operations.
    :keyword ~azure.storage.filedatalake.RetentionPolicy retention_policy:
        Determines how long the associated data should persist. If not specified the retention
        policy will be disabled by default.
    """
    version: Incomplete
    enabled: Incomplete
    include_apis: Incomplete
    retention_policy: Incomplete
    def __init__(self, **kwargs) -> None: ...

class RetentionPolicy(GenRetentionPolicy):
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

class StaticWebsite(GenStaticWebsite):
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

class CorsRule(GenCorsRule):
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
