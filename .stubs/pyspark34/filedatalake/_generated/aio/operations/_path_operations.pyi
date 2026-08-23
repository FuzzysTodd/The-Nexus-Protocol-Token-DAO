from ... import models as _models
from ...operations._path_operations import build_append_data_request as build_append_data_request, build_create_request as build_create_request, build_delete_request as build_delete_request, build_flush_data_request as build_flush_data_request, build_get_properties_request as build_get_properties_request, build_lease_request as build_lease_request, build_read_request as build_read_request, build_set_access_control_recursive_request as build_set_access_control_recursive_request, build_set_access_control_request as build_set_access_control_request, build_set_expiry_request as build_set_expiry_request, build_undelete_request as build_undelete_request, build_update_request as build_update_request
from _typeshed import Incomplete
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from typing import Any, AsyncIterator, Callable, Dict, IO, TypeVar

T = TypeVar('T')
ClsType = Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any] | None

class PathOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.storage.filedatalake.aio.AzureDataLakeStorageRESTAPI`'s
        :attr:`path` attribute.
    """
    models: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    async def create(self, request_id_parameter: str | None = None, timeout: int | None = None, resource: str | _models.PathResourceType | None = None, continuation: str | None = None, mode: str | _models.PathRenameMode | None = None, rename_source: str | None = None, source_lease_id: str | None = None, properties: str | None = None, permissions: str | None = None, umask: str | None = None, owner: str | None = None, group: str | None = None, acl: str | None = None, proposed_lease_id: str | None = None, lease_duration: int | None = None, expiry_options: str | _models.PathExpiryOptions | None = None, expires_on: str | None = None, encryption_context: str | None = None, path_http_headers: _models.PathHTTPHeaders | None = None, lease_access_conditions: _models.LeaseAccessConditions | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, source_modified_access_conditions: _models.SourceModifiedAccessConditions | None = None, cpk_info: _models.CpkInfo | None = None, **kwargs: Any) -> None:
        '''Create File | Create Directory | Rename File | Rename Directory.

        Create or rename a file or directory.    By default, the destination is overwritten and if the
        destination already exists and has a lease the lease is broken.  This operation supports
        conditional HTTP requests.  For more information, see `Specifying Conditional Headers for Blob
        Service Operations
        <https://docs.microsoft.com/en-us/rest/api/storageservices/specifying-conditional-headers-for-blob-service-operations>`_.
        To fail if the destination already exists, use a conditional request with If-None-Match: "*".

        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param resource: Required only for Create File and Create Directory. The value must be "file"
         or "directory". Known values are: "directory" and "file". Default value is None.
        :type resource: str or ~azure.storage.filedatalake.models.PathResourceType
        :param continuation: Optional.  When deleting a directory, the number of paths that are deleted
         with each invocation is limited.  If the number of paths to be deleted exceeds this limit, a
         continuation token is returned in this response header.  When a continuation token is returned
         in the response, it must be specified in a subsequent invocation of the delete operation to
         continue deleting the directory. Default value is None.
        :type continuation: str
        :param mode: Optional. Valid only when namespace is enabled. This parameter determines the
         behavior of the rename operation. The value must be "legacy" or "posix", and the default value
         will be "posix". Known values are: "legacy" and "posix". Default value is None.
        :type mode: str or ~azure.storage.filedatalake.models.PathRenameMode
        :param rename_source: An optional file or directory to be renamed.  The value must have the
         following format: "/{filesystem}/{path}".  If "x-ms-properties" is specified, the properties
         will overwrite the existing properties; otherwise, the existing properties will be preserved.
         This value must be a URL percent-encoded string. Note that the string may only contain ASCII
         characters in the ISO-8859-1 character set. Default value is None.
        :type rename_source: str
        :param source_lease_id: A lease ID for the source path. If specified, the source path must have
         an active lease and the lease ID must match. Default value is None.
        :type source_lease_id: str
        :param properties: Optional. User-defined properties to be stored with the filesystem, in the
         format of a comma-separated list of name and value pairs "n1=v1, n2=v2, ...", where each value
         is a base64 encoded string. Note that the string may only contain ASCII characters in the
         ISO-8859-1 character set.  If the filesystem exists, any properties not included in the list
         will be removed.  All properties are removed if the header is omitted.  To merge new and
         existing properties, first get all existing properties and the current E-Tag, then make a
         conditional request with the E-Tag and include values for all properties. Default value is
         None.
        :type properties: str
        :param permissions: Optional and only valid if Hierarchical Namespace is enabled for the
         account. Sets POSIX access permissions for the file owner, the file owning group, and others.
         Each class may be granted read, write, or execute permission.  The sticky bit is also
         supported.  Both symbolic (rwxrw-rw-) and 4-digit octal notation (e.g. 0766) are supported.
         Default value is None.
        :type permissions: str
        :param umask: Optional and only valid if Hierarchical Namespace is enabled for the account.
         When creating a file or directory and the parent folder does not have a default ACL, the umask
         restricts the permissions of the file or directory to be created.  The resulting permission is
         given by p bitwise and not u, where p is the permission and u is the umask.  For example, if p
         is 0777 and u is 0057, then the resulting permission is 0720.  The default permission is 0777
         for a directory and 0666 for a file.  The default umask is 0027.  The umask must be specified
         in 4-digit octal notation (e.g. 0766). Default value is None.
        :type umask: str
        :param owner: Optional. The owner of the blob or directory. Default value is None.
        :type owner: str
        :param group: Optional. The owning group of the blob or directory. Default value is None.
        :type group: str
        :param acl: Sets POSIX access control rights on files and directories. The value is a
         comma-separated list of access control entries. Each access control entry (ACE) consists of a
         scope, a type, a user or group identifier, and permissions in the format
         "[scope:][type]:[id]:[permissions]". Default value is None.
        :type acl: str
        :param proposed_lease_id: Proposed lease ID, in a GUID string format. The Blob service returns
         400 (Invalid request) if the proposed lease ID is not in the correct format. See Guid
         Constructor (String) for a list of valid GUID string formats. Default value is None.
        :type proposed_lease_id: str
        :param lease_duration: The lease duration is required to acquire a lease, and specifies the
         duration of the lease in seconds.  The lease duration must be between 15 and 60 seconds or -1
         for infinite lease. Default value is None.
        :type lease_duration: int
        :param expiry_options: Required. Indicates mode of the expiry time. Known values are:
         "NeverExpire", "RelativeToCreation", "RelativeToNow", and "Absolute". Default value is None.
        :type expiry_options: str or ~azure.storage.filedatalake.models.PathExpiryOptions
        :param expires_on: The time to set the blob to expiry. Default value is None.
        :type expires_on: str
        :param encryption_context: Specifies the encryption context to set on the file. Default value
         is None.
        :type encryption_context: str
        :param path_http_headers: Parameter group. Default value is None.
        :type path_http_headers: ~azure.storage.filedatalake.models.PathHTTPHeaders
        :param lease_access_conditions: Parameter group. Default value is None.
        :type lease_access_conditions: ~azure.storage.filedatalake.models.LeaseAccessConditions
        :param modified_access_conditions: Parameter group. Default value is None.
        :type modified_access_conditions: ~azure.storage.filedatalake.models.ModifiedAccessConditions
        :param source_modified_access_conditions: Parameter group. Default value is None.
        :type source_modified_access_conditions:
         ~azure.storage.filedatalake.models.SourceModifiedAccessConditions
        :param cpk_info: Parameter group. Default value is None.
        :type cpk_info: ~azure.storage.filedatalake.models.CpkInfo
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    async def update(self, action: str | _models.PathUpdateAction, mode: str | _models.PathSetAccessControlRecursiveMode, body: IO, request_id_parameter: str | None = None, timeout: int | None = None, max_records: int | None = None, continuation: str | None = None, force_flag: bool | None = None, position: int | None = None, retain_uncommitted_data: bool | None = None, close: bool | None = None, content_length: int | None = None, properties: str | None = None, owner: str | None = None, group: str | None = None, permissions: str | None = None, acl: str | None = None, path_http_headers: _models.PathHTTPHeaders | None = None, lease_access_conditions: _models.LeaseAccessConditions | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, **kwargs: Any) -> _models.SetAccessControlRecursiveResponse | None:
        '''Append Data | Flush Data | Set Properties | Set Access Control.

        Uploads data to be appended to a file, flushes (writes) previously uploaded data to a file,
        sets properties for a file or directory, or sets access control for a file or directory. Data
        can only be appended to a file. Concurrent writes to the same file using multiple clients are
        not supported. This operation supports conditional HTTP requests. For more information, see
        `Specifying Conditional Headers for Blob Service Operations
        <https://docs.microsoft.com/en-us/rest/api/storageservices/specifying-conditional-headers-for-blob-service-operations>`_.

        :param action: The action must be "append" to upload data to be appended to a file, "flush" to
         flush previously uploaded data to a file, "setProperties" to set the properties of a file or
         directory, "setAccessControl" to set the owner, group, permissions, or access control list for
         a file or directory, or  "setAccessControlRecursive" to set the access control list for a
         directory recursively. Note that Hierarchical Namespace must be enabled for the account in
         order to use access control.  Also note that the Access Control List (ACL) includes permissions
         for the owner, owning group, and others, so the x-ms-permissions and x-ms-acl request headers
         are mutually exclusive. Known values are: "append", "flush", "setProperties",
         "setAccessControl", and "setAccessControlRecursive". Required.
        :type action: str or ~azure.storage.filedatalake.models.PathUpdateAction
        :param mode: Mode "set" sets POSIX access control rights on files and directories, "modify"
         modifies one or more POSIX access control rights  that pre-exist on files and directories,
         "remove" removes one or more POSIX access control rights  that were present earlier on files
         and directories. Known values are: "set", "modify", and "remove". Required.
        :type mode: str or ~azure.storage.filedatalake.models.PathSetAccessControlRecursiveMode
        :param body: Initial data. Required.
        :type body: IO
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param max_records: Optional. Valid for "SetAccessControlRecursive" operation. It specifies the
         maximum number of files or directories on which the acl change will be applied. If omitted or
         greater than 2,000, the request will process up to 2,000 items. Default value is None.
        :type max_records: int
        :param continuation: Optional. The number of paths processed with each invocation is limited.
         If the number of paths to be processed exceeds this limit, a continuation token is returned in
         the response header x-ms-continuation. When a continuation token is  returned in the response,
         it must be percent-encoded and specified in a subsequent invocation of
         setAccessControlRecursive operation. Default value is None.
        :type continuation: str
        :param force_flag: Optional. Valid for "SetAccessControlRecursive" operation. If set to false,
         the operation will terminate quickly on encountering user errors (4XX). If true, the operation
         will ignore user errors and proceed with the operation on other sub-entities of the directory.
         Continuation token will only be returned when forceFlag is true in case of user errors. If not
         set the default value is false for this. Default value is None.
        :type force_flag: bool
        :param position: This parameter allows the caller to upload data in parallel and control the
         order in which it is appended to the file.  It is required when uploading data to be appended
         to the file and when flushing previously uploaded data to the file.  The value must be the
         position where the data is to be appended.  Uploaded data is not immediately flushed, or
         written, to the file.  To flush, the previously uploaded data must be contiguous, the position
         parameter must be specified and equal to the length of the file after all data has been
         written, and there must not be a request entity body included with the request. Default value
         is None.
        :type position: int
        :param retain_uncommitted_data: Valid only for flush operations.  If "true", uncommitted data
         is retained after the flush operation completes; otherwise, the uncommitted data is deleted
         after the flush operation.  The default is false.  Data at offsets less than the specified
         position are written to the file when flush succeeds, but this optional parameter allows data
         after the flush position to be retained for a future flush operation. Default value is None.
        :type retain_uncommitted_data: bool
        :param close: Azure Storage Events allow applications to receive notifications when files
         change. When Azure Storage Events are enabled, a file changed event is raised. This event has a
         property indicating whether this is the final change to distinguish the difference between an
         intermediate flush to a file stream and the final close of a file stream. The close query
         parameter is valid only when the action is "flush" and change notifications are enabled. If the
         value of close is "true" and the flush operation completes successfully, the service raises a
         file change notification with a property indicating that this is the final update (the file
         stream has been closed). If "false" a change notification is raised indicating the file has
         changed. The default is false. This query parameter is set to true by the Hadoop ABFS driver to
         indicate that the file stream has been closed.". Default value is None.
        :type close: bool
        :param content_length: Required for "Append Data" and "Flush Data".  Must be 0 for "Flush
         Data".  Must be the length of the request content in bytes for "Append Data". Default value is
         None.
        :type content_length: int
        :param properties: Optional. User-defined properties to be stored with the filesystem, in the
         format of a comma-separated list of name and value pairs "n1=v1, n2=v2, ...", where each value
         is a base64 encoded string. Note that the string may only contain ASCII characters in the
         ISO-8859-1 character set.  If the filesystem exists, any properties not included in the list
         will be removed.  All properties are removed if the header is omitted.  To merge new and
         existing properties, first get all existing properties and the current E-Tag, then make a
         conditional request with the E-Tag and include values for all properties. Default value is
         None.
        :type properties: str
        :param owner: Optional. The owner of the blob or directory. Default value is None.
        :type owner: str
        :param group: Optional. The owning group of the blob or directory. Default value is None.
        :type group: str
        :param permissions: Optional and only valid if Hierarchical Namespace is enabled for the
         account. Sets POSIX access permissions for the file owner, the file owning group, and others.
         Each class may be granted read, write, or execute permission.  The sticky bit is also
         supported.  Both symbolic (rwxrw-rw-) and 4-digit octal notation (e.g. 0766) are supported.
         Default value is None.
        :type permissions: str
        :param acl: Sets POSIX access control rights on files and directories. The value is a
         comma-separated list of access control entries. Each access control entry (ACE) consists of a
         scope, a type, a user or group identifier, and permissions in the format
         "[scope:][type]:[id]:[permissions]". Default value is None.
        :type acl: str
        :param path_http_headers: Parameter group. Default value is None.
        :type path_http_headers: ~azure.storage.filedatalake.models.PathHTTPHeaders
        :param lease_access_conditions: Parameter group. Default value is None.
        :type lease_access_conditions: ~azure.storage.filedatalake.models.LeaseAccessConditions
        :param modified_access_conditions: Parameter group. Default value is None.
        :type modified_access_conditions: ~azure.storage.filedatalake.models.ModifiedAccessConditions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SetAccessControlRecursiveResponse or None or the result of cls(response)
        :rtype: ~azure.storage.filedatalake.models.SetAccessControlRecursiveResponse or None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    async def lease(self, x_ms_lease_action: str | _models.PathLeaseAction, request_id_parameter: str | None = None, timeout: int | None = None, x_ms_lease_break_period: int | None = None, proposed_lease_id: str | None = None, lease_access_conditions: _models.LeaseAccessConditions | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, **kwargs: Any) -> None:
        '''Lease Path.

        Create and manage a lease to restrict write and delete access to the path. This operation
        supports conditional HTTP requests.  For more information, see `Specifying Conditional Headers
        for Blob Service Operations
        <https://docs.microsoft.com/en-us/rest/api/storageservices/specifying-conditional-headers-for-blob-service-operations>`_.

        :param x_ms_lease_action: There are five lease actions: "acquire", "break", "change", "renew",
         and "release". Use "acquire" and specify the "x-ms-proposed-lease-id" and "x-ms-lease-duration"
         to acquire a new lease. Use "break" to break an existing lease. When a lease is broken, the
         lease break period is allowed to elapse, during which time no lease operation except break and
         release can be performed on the file. When a lease is successfully broken, the response
         indicates the interval in seconds until a new lease can be acquired. Use "change" and specify
         the current lease ID in "x-ms-lease-id" and the new lease ID in "x-ms-proposed-lease-id" to
         change the lease ID of an active lease. Use "renew" and specify the "x-ms-lease-id" to renew an
         existing lease. Use "release" and specify the "x-ms-lease-id" to release a lease. Known values
         are: "acquire", "break", "change", "renew", and "release". Required.
        :type x_ms_lease_action: str or ~azure.storage.filedatalake.models.PathLeaseAction
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param x_ms_lease_break_period: The lease break period duration is optional to break a lease,
         and  specifies the break period of the lease in seconds.  The lease break  duration must be
         between 0 and 60 seconds. Default value is None.
        :type x_ms_lease_break_period: int
        :param proposed_lease_id: Proposed lease ID, in a GUID string format. The Blob service returns
         400 (Invalid request) if the proposed lease ID is not in the correct format. See Guid
         Constructor (String) for a list of valid GUID string formats. Default value is None.
        :type proposed_lease_id: str
        :param lease_access_conditions: Parameter group. Default value is None.
        :type lease_access_conditions: ~azure.storage.filedatalake.models.LeaseAccessConditions
        :param modified_access_conditions: Parameter group. Default value is None.
        :type modified_access_conditions: ~azure.storage.filedatalake.models.ModifiedAccessConditions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    async def read(self, request_id_parameter: str | None = None, timeout: int | None = None, range: str | None = None, x_ms_range_get_content_md5: bool | None = None, lease_access_conditions: _models.LeaseAccessConditions | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, cpk_info: _models.CpkInfo | None = None, **kwargs: Any) -> AsyncIterator[bytes]:
        '''Read File.

        Read the contents of a file.  For read operations, range requests are supported. This operation
        supports conditional HTTP requests.  For more information, see `Specifying Conditional Headers
        for Blob Service Operations
        <https://docs.microsoft.com/en-us/rest/api/storageservices/specifying-conditional-headers-for-blob-service-operations>`_.

        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param range: The HTTP Range request header specifies one or more byte ranges of the resource
         to be retrieved. Default value is None.
        :type range: str
        :param x_ms_range_get_content_md5: Optional. When this header is set to "true" and specified
         together with the Range header, the service returns the MD5 hash for the range, as long as the
         range is less than or equal to 4MB in size. If this header is specified without the Range
         header, the service returns status code 400 (Bad Request). If this header is set to true when
         the range exceeds 4 MB in size, the service returns status code 400 (Bad Request). Default
         value is None.
        :type x_ms_range_get_content_md5: bool
        :param lease_access_conditions: Parameter group. Default value is None.
        :type lease_access_conditions: ~azure.storage.filedatalake.models.LeaseAccessConditions
        :param modified_access_conditions: Parameter group. Default value is None.
        :type modified_access_conditions: ~azure.storage.filedatalake.models.ModifiedAccessConditions
        :param cpk_info: Parameter group. Default value is None.
        :type cpk_info: ~azure.storage.filedatalake.models.CpkInfo
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Async iterator of the response bytes or the result of cls(response)
        :rtype: AsyncIterator[bytes]
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    async def get_properties(self, request_id_parameter: str | None = None, timeout: int | None = None, action: str | _models.PathGetPropertiesAction | None = None, upn: bool | None = None, lease_access_conditions: _models.LeaseAccessConditions | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, **kwargs: Any) -> None:
        '''Get Properties | Get Status | Get Access Control List.

        Get Properties returns all system and user defined properties for a path. Get Status returns
        all system defined properties for a path. Get Access Control List returns the access control
        list for a path. This operation supports conditional HTTP requests.  For more information, see
        `Specifying Conditional Headers for Blob Service Operations
        <https://docs.microsoft.com/en-us/rest/api/storageservices/specifying-conditional-headers-for-blob-service-operations>`_.

        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param action: Optional. If the value is "getStatus" only the system defined properties for the
         path are returned. If the value is "getAccessControl" the access control list is returned in
         the response headers (Hierarchical Namespace must be enabled for the account), otherwise the
         properties are returned. Known values are: "getAccessControl" and "getStatus". Default value is
         None.
        :type action: str or ~azure.storage.filedatalake.models.PathGetPropertiesAction
        :param upn: Optional. Valid only when Hierarchical Namespace is enabled for the account. If
         "true", the user identity values returned in the x-ms-owner, x-ms-group, and x-ms-acl response
         headers will be transformed from Azure Active Directory Object IDs to User Principal Names.  If
         "false", the values will be returned as Azure Active Directory Object IDs. The default value is
         false. Note that group and application Object IDs are not translated because they do not have
         unique friendly names. Default value is None.
        :type upn: bool
        :param lease_access_conditions: Parameter group. Default value is None.
        :type lease_access_conditions: ~azure.storage.filedatalake.models.LeaseAccessConditions
        :param modified_access_conditions: Parameter group. Default value is None.
        :type modified_access_conditions: ~azure.storage.filedatalake.models.ModifiedAccessConditions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    async def delete(self, request_id_parameter: str | None = None, timeout: int | None = None, recursive: bool | None = None, continuation: str | None = None, lease_access_conditions: _models.LeaseAccessConditions | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, **kwargs: Any) -> None:
        '''Delete File | Delete Directory.

        Delete the file or directory. This operation supports conditional HTTP requests.  For more
        information, see `Specifying Conditional Headers for Blob Service Operations
        <https://docs.microsoft.com/en-us/rest/api/storageservices/specifying-conditional-headers-for-blob-service-operations>`_.

        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param recursive: Required. Default value is None.
        :type recursive: bool
        :param continuation: Optional.  When deleting a directory, the number of paths that are deleted
         with each invocation is limited.  If the number of paths to be deleted exceeds this limit, a
         continuation token is returned in this response header.  When a continuation token is returned
         in the response, it must be specified in a subsequent invocation of the delete operation to
         continue deleting the directory. Default value is None.
        :type continuation: str
        :param lease_access_conditions: Parameter group. Default value is None.
        :type lease_access_conditions: ~azure.storage.filedatalake.models.LeaseAccessConditions
        :param modified_access_conditions: Parameter group. Default value is None.
        :type modified_access_conditions: ~azure.storage.filedatalake.models.ModifiedAccessConditions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    async def set_access_control(self, timeout: int | None = None, owner: str | None = None, group: str | None = None, permissions: str | None = None, acl: str | None = None, request_id_parameter: str | None = None, lease_access_conditions: _models.LeaseAccessConditions | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, **kwargs: Any) -> None:
        '''Set the owner, group, permissions, or access control list for a path.

        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param owner: Optional. The owner of the blob or directory. Default value is None.
        :type owner: str
        :param group: Optional. The owning group of the blob or directory. Default value is None.
        :type group: str
        :param permissions: Optional and only valid if Hierarchical Namespace is enabled for the
         account. Sets POSIX access permissions for the file owner, the file owning group, and others.
         Each class may be granted read, write, or execute permission.  The sticky bit is also
         supported.  Both symbolic (rwxrw-rw-) and 4-digit octal notation (e.g. 0766) are supported.
         Default value is None.
        :type permissions: str
        :param acl: Sets POSIX access control rights on files and directories. The value is a
         comma-separated list of access control entries. Each access control entry (ACE) consists of a
         scope, a type, a user or group identifier, and permissions in the format
         "[scope:][type]:[id]:[permissions]". Default value is None.
        :type acl: str
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param lease_access_conditions: Parameter group. Default value is None.
        :type lease_access_conditions: ~azure.storage.filedatalake.models.LeaseAccessConditions
        :param modified_access_conditions: Parameter group. Default value is None.
        :type modified_access_conditions: ~azure.storage.filedatalake.models.ModifiedAccessConditions
        :keyword action: action. Default value is "setAccessControl". Note that overriding this default
         value may result in unsupported behavior.
        :paramtype action: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    async def set_access_control_recursive(self, mode: str | _models.PathSetAccessControlRecursiveMode, timeout: int | None = None, continuation: str | None = None, force_flag: bool | None = None, max_records: int | None = None, acl: str | None = None, request_id_parameter: str | None = None, **kwargs: Any) -> _models.SetAccessControlRecursiveResponse:
        '''Set the access control list for a path and sub-paths.

        :param mode: Mode "set" sets POSIX access control rights on files and directories, "modify"
         modifies one or more POSIX access control rights  that pre-exist on files and directories,
         "remove" removes one or more POSIX access control rights  that were present earlier on files
         and directories. Known values are: "set", "modify", and "remove". Required.
        :type mode: str or ~azure.storage.filedatalake.models.PathSetAccessControlRecursiveMode
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param continuation: Optional.  When deleting a directory, the number of paths that are deleted
         with each invocation is limited.  If the number of paths to be deleted exceeds this limit, a
         continuation token is returned in this response header.  When a continuation token is returned
         in the response, it must be specified in a subsequent invocation of the delete operation to
         continue deleting the directory. Default value is None.
        :type continuation: str
        :param force_flag: Optional. Valid for "SetAccessControlRecursive" operation. If set to false,
         the operation will terminate quickly on encountering user errors (4XX). If true, the operation
         will ignore user errors and proceed with the operation on other sub-entities of the directory.
         Continuation token will only be returned when forceFlag is true in case of user errors. If not
         set the default value is false for this. Default value is None.
        :type force_flag: bool
        :param max_records: Optional. It specifies the maximum number of files or directories on which
         the acl change will be applied. If omitted or greater than 2,000, the request will process up
         to 2,000 items. Default value is None.
        :type max_records: int
        :param acl: Sets POSIX access control rights on files and directories. The value is a
         comma-separated list of access control entries. Each access control entry (ACE) consists of a
         scope, a type, a user or group identifier, and permissions in the format
         "[scope:][type]:[id]:[permissions]". Default value is None.
        :type acl: str
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :keyword action: action. Default value is "setAccessControlRecursive". Note that overriding
         this default value may result in unsupported behavior.
        :paramtype action: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SetAccessControlRecursiveResponse or the result of cls(response)
        :rtype: ~azure.storage.filedatalake.models.SetAccessControlRecursiveResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    async def flush_data(self, timeout: int | None = None, position: int | None = None, retain_uncommitted_data: bool | None = None, close: bool | None = None, content_length: int | None = None, lease_action: str | _models.LeaseAction | None = None, lease_duration: int | None = None, proposed_lease_id: str | None = None, request_id_parameter: str | None = None, path_http_headers: _models.PathHTTPHeaders | None = None, lease_access_conditions: _models.LeaseAccessConditions | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, cpk_info: _models.CpkInfo | None = None, **kwargs: Any) -> None:
        '''Set the owner, group, permissions, or access control list for a path.

        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param position: This parameter allows the caller to upload data in parallel and control the
         order in which it is appended to the file.  It is required when uploading data to be appended
         to the file and when flushing previously uploaded data to the file.  The value must be the
         position where the data is to be appended.  Uploaded data is not immediately flushed, or
         written, to the file.  To flush, the previously uploaded data must be contiguous, the position
         parameter must be specified and equal to the length of the file after all data has been
         written, and there must not be a request entity body included with the request. Default value
         is None.
        :type position: int
        :param retain_uncommitted_data: Valid only for flush operations.  If "true", uncommitted data
         is retained after the flush operation completes; otherwise, the uncommitted data is deleted
         after the flush operation.  The default is false.  Data at offsets less than the specified
         position are written to the file when flush succeeds, but this optional parameter allows data
         after the flush position to be retained for a future flush operation. Default value is None.
        :type retain_uncommitted_data: bool
        :param close: Azure Storage Events allow applications to receive notifications when files
         change. When Azure Storage Events are enabled, a file changed event is raised. This event has a
         property indicating whether this is the final change to distinguish the difference between an
         intermediate flush to a file stream and the final close of a file stream. The close query
         parameter is valid only when the action is "flush" and change notifications are enabled. If the
         value of close is "true" and the flush operation completes successfully, the service raises a
         file change notification with a property indicating that this is the final update (the file
         stream has been closed). If "false" a change notification is raised indicating the file has
         changed. The default is false. This query parameter is set to true by the Hadoop ABFS driver to
         indicate that the file stream has been closed.". Default value is None.
        :type close: bool
        :param content_length: Required for "Append Data" and "Flush Data".  Must be 0 for "Flush
         Data".  Must be the length of the request content in bytes for "Append Data". Default value is
         None.
        :type content_length: int
        :param lease_action: Optional. If "acquire" it will acquire the lease. If "auto-renew" it will
         renew the lease. If "release" it will release the lease only on flush. If "acquire-release" it
         will acquire & complete the operation & release the lease once operation is done. Known values
         are: "acquire", "auto-renew", "release", and "acquire-release". Default value is None.
        :type lease_action: str or ~azure.storage.filedatalake.models.LeaseAction
        :param lease_duration: The lease duration is required to acquire a lease, and specifies the
         duration of the lease in seconds.  The lease duration must be between 15 and 60 seconds or -1
         for infinite lease. Default value is None.
        :type lease_duration: int
        :param proposed_lease_id: Proposed lease ID, in a GUID string format. The Blob service returns
         400 (Invalid request) if the proposed lease ID is not in the correct format. See Guid
         Constructor (String) for a list of valid GUID string formats. Default value is None.
        :type proposed_lease_id: str
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param path_http_headers: Parameter group. Default value is None.
        :type path_http_headers: ~azure.storage.filedatalake.models.PathHTTPHeaders
        :param lease_access_conditions: Parameter group. Default value is None.
        :type lease_access_conditions: ~azure.storage.filedatalake.models.LeaseAccessConditions
        :param modified_access_conditions: Parameter group. Default value is None.
        :type modified_access_conditions: ~azure.storage.filedatalake.models.ModifiedAccessConditions
        :param cpk_info: Parameter group. Default value is None.
        :type cpk_info: ~azure.storage.filedatalake.models.CpkInfo
        :keyword action: action. Default value is "flush". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype action: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    async def append_data(self, body: IO, position: int | None = None, timeout: int | None = None, content_length: int | None = None, transactional_content_crc64: bytes | None = None, lease_action: str | _models.LeaseAction | None = None, lease_duration: int | None = None, proposed_lease_id: str | None = None, request_id_parameter: str | None = None, flush: bool | None = None, path_http_headers: _models.PathHTTPHeaders | None = None, lease_access_conditions: _models.LeaseAccessConditions | None = None, cpk_info: _models.CpkInfo | None = None, **kwargs: Any) -> None:
        '''Append data to the file.

        :param body: Initial data. Required.
        :type body: IO
        :param position: This parameter allows the caller to upload data in parallel and control the
         order in which it is appended to the file.  It is required when uploading data to be appended
         to the file and when flushing previously uploaded data to the file.  The value must be the
         position where the data is to be appended.  Uploaded data is not immediately flushed, or
         written, to the file.  To flush, the previously uploaded data must be contiguous, the position
         parameter must be specified and equal to the length of the file after all data has been
         written, and there must not be a request entity body included with the request. Default value
         is None.
        :type position: int
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param content_length: Required for "Append Data" and "Flush Data".  Must be 0 for "Flush
         Data".  Must be the length of the request content in bytes for "Append Data". Default value is
         None.
        :type content_length: int
        :param transactional_content_crc64: Specify the transactional crc64 for the body, to be
         validated by the service. Default value is None.
        :type transactional_content_crc64: bytes
        :param lease_action: Optional. If "acquire" it will acquire the lease. If "auto-renew" it will
         renew the lease. If "release" it will release the lease only on flush. If "acquire-release" it
         will acquire & complete the operation & release the lease once operation is done. Known values
         are: "acquire", "auto-renew", "release", and "acquire-release". Default value is None.
        :type lease_action: str or ~azure.storage.filedatalake.models.LeaseAction
        :param lease_duration: The lease duration is required to acquire a lease, and specifies the
         duration of the lease in seconds.  The lease duration must be between 15 and 60 seconds or -1
         for infinite lease. Default value is None.
        :type lease_duration: int
        :param proposed_lease_id: Proposed lease ID, in a GUID string format. The Blob service returns
         400 (Invalid request) if the proposed lease ID is not in the correct format. See Guid
         Constructor (String) for a list of valid GUID string formats. Default value is None.
        :type proposed_lease_id: str
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param flush: If file should be flushed after the append. Default value is None.
        :type flush: bool
        :param path_http_headers: Parameter group. Default value is None.
        :type path_http_headers: ~azure.storage.filedatalake.models.PathHTTPHeaders
        :param lease_access_conditions: Parameter group. Default value is None.
        :type lease_access_conditions: ~azure.storage.filedatalake.models.LeaseAccessConditions
        :param cpk_info: Parameter group. Default value is None.
        :type cpk_info: ~azure.storage.filedatalake.models.CpkInfo
        :keyword action: action. Default value is "append". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype action: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    async def set_expiry(self, expiry_options: str | _models.PathExpiryOptions, timeout: int | None = None, request_id_parameter: str | None = None, expires_on: str | None = None, **kwargs: Any) -> None:
        '''Sets the time a blob will expire and be deleted.

        :param expiry_options: Required. Indicates mode of the expiry time. Known values are:
         "NeverExpire", "RelativeToCreation", "RelativeToNow", and "Absolute". Required.
        :type expiry_options: str or ~azure.storage.filedatalake.models.PathExpiryOptions
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
    async def undelete(self, timeout: int | None = None, undelete_source: str | None = None, request_id_parameter: str | None = None, **kwargs: Any) -> None:
        '''Undelete a path that was previously soft deleted.

        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param undelete_source: Only for hierarchical namespace enabled accounts. Optional. The path of
         the soft deleted blob to undelete. Default value is None.
        :type undelete_source: str
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
