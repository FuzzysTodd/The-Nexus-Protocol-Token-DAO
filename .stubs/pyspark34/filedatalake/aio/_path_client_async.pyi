from .._deserialize import process_storage_error as process_storage_error
from .._generated.aio import AzureDataLakeStorageRESTAPI as AzureDataLakeStorageRESTAPI
from .._models import AccessControlChangeCounters as AccessControlChangeCounters, AccessControlChangeFailure as AccessControlChangeFailure, AccessControlChangeResult as AccessControlChangeResult, AccessControlChanges as AccessControlChanges, ContentSettings as ContentSettings, DirectoryProperties as DirectoryProperties, FileProperties as FileProperties
from .._path_client import PathClient as PathClientBase
from .._serialize import get_api_version as get_api_version
from .._shared.base_client_async import AsyncStorageAccountHostsMixin as AsyncStorageAccountHostsMixin
from .._shared.policies_async import ExponentialRetry as ExponentialRetry
from ._data_lake_lease_async import DataLakeLeaseClient as DataLakeLeaseClient
from azure.core.credentials import AzureNamedKeyCredential as AzureNamedKeyCredential, AzureSasCredential as AzureSasCredential
from azure.core.credentials_async import AsyncTokenCredential as AsyncTokenCredential
from datetime import datetime
from typing import Any, Dict

class PathClient(AsyncStorageAccountHostsMixin, PathClientBase):
    '''A base client for interacting with a DataLake file/directory, even if the file/directory may not
    yet exist.

    :param str account_url:
        The URI to the storage account.
    :param str file_system_name:
        The file system for the directory or files.
    :param str file_path:
        The whole file path, so that to interact with a specific file.
        eg. "{directory}/{subdirectory}/{file}"
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
    '''
    def __init__(self, account_url: str, file_system_name: str, path_name: str, credential: str | Dict[str, str] | AzureNamedKeyCredential | AzureSasCredential | AsyncTokenCredential | None = None, **kwargs: Any) -> None: ...
    async def __aexit__(self, *args) -> None: ...
    async def close(self) -> None:
        """ This method is to close the sockets opened by the client.
        It need not be used when using with a context manager.
        """
    async def set_access_control(self, owner: str | None = None, group: str | None = None, permissions: str | None = None, acl: str | None = None, **kwargs) -> Dict[str, str | datetime]:
        '''
        Set the owner, group, permissions, or access control list for a path.

        :param owner:
            Optional. The owner of the file or directory.
        :type owner: str
        :param group:
            Optional. The owning group of the file or directory.
        :type group: str
        :param permissions:
            Optional and only valid if Hierarchical Namespace
            is enabled for the account. Sets POSIX access permissions for the file
            owner, the file owning group, and others. Each class may be granted
            read, write, or execute permission.  The sticky bit is also supported.
            Both symbolic (rwxrw-rw-) and 4-digit octal notation (e.g. 0766) are
            supported.
            permissions and acl are mutually exclusive.
        :type permissions: str
        :param acl:
            Sets POSIX access control rights on files and directories.
            The value is a comma-separated list of access control entries. Each
            access control entry (ACE) consists of a scope, a type, a user or
            group identifier, and permissions in the format
            "[scope:][type]:[id]:[permissions]".
            permissions and acl are mutually exclusive.
        :type acl: str
        :keyword lease:
            Required if the file/directory has an active lease. Value can be a LeaseClient object
            or the lease ID as a string.
        :paramtype lease: ~azure.storage.filedatalake.aio.DataLakeLeaseClient or str
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
            see `here <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-file-datalake
            #other-client--per-operation-configuration>`_.
        :keyword: response dict (Etag and last modified).
        '''
    async def get_access_control(self, upn: bool | None = None, **kwargs) -> Dict[str, Any]:
        '''
        Get the owner, group, permissions, or access control list for a path.

        :param upn:
            Optional. Valid only when Hierarchical Namespace is
            enabled for the account. If "true", the user identity values returned
            in the x-ms-owner, x-ms-group, and x-ms-acl response headers will be
            transformed from Azure Active Directory Object IDs to User Principal
            Names.  If "false", the values will be returned as Azure Active
            Directory Object IDs. The default value is false. Note that group and
            application Object IDs are not translated because they do not have
            unique friendly names.
        :type upn: bool
        :keyword lease:
            Required if the file/directory has an active lease. Value can be a LeaseClient object
            or the lease ID as a string.
        :paramtype lease: ~azure.storage.filedatalake.aio.DataLakeLeaseClient or str
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
            see `here <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-file-datalake
            #other-client--per-operation-configuration>`_.
        :keyword: response dict.
        '''
    async def set_access_control_recursive(self, acl: str, **kwargs: Any) -> AccessControlChangeResult:
        '''
        Sets the Access Control on a path and sub-paths.

        :param acl:
            Sets POSIX access control rights on files and directories.
            The value is a comma-separated list of access control entries. Each
            access control entry (ACE) consists of a scope, a type, a user or
            group identifier, and permissions in the format
            "[scope:][type]:[id]:[permissions]".
        :type acl: str
        :keyword func(~azure.storage.filedatalake.AccessControlChanges) progress_hook:
            Callback where the caller can track progress of the operation
            as well as collect paths that failed to change Access Control.
        :keyword str continuation_token:
            Optional continuation token that can be used to resume previously stopped operation.
        :keyword int batch_size:
            Optional. If data set size exceeds batch size then operation will be split into multiple
            requests so that progress can be tracked. Batch size should be between 1 and 2000.
            The default when unspecified is 2000.
        :keyword int max_batches:
            Optional. Defines maximum number of batches that single change Access Control operation can execute.
            If maximum is reached before all sub-paths are processed,
            then continuation token can be used to resume operation.
            Empty value indicates that maximum number of batches in unbound and operation continues till end.
        :keyword bool continue_on_failure:
            If set to False, the operation will terminate quickly on encountering user errors (4XX).
            If True, the operation will ignore user errors and proceed with the operation on other sub-entities of
            the directory.
            Continuation token will only be returned when continue_on_failure is True in case of user errors.
            If not set the default value is False for this.
        :keyword int timeout:
            Sets the server-side timeout for the operation in seconds. For more details see
            https://learn.microsoft.com/rest/api/storageservices/setting-timeouts-for-blob-service-operations.
            This value is not tracked or validated on the client. To configure client-side network timesouts
            see `here <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-file-datalake
            #other-client--per-operation-configuration>`_.
        :return: A summary of the recursive operations, including the count of successes and failures,
            as well as a continuation token in case the operation was terminated prematurely.
        :rtype: :~azure.storage.filedatalake.AccessControlChangeResult`
        :raises ~azure.core.exceptions.AzureError:
            User can restart the operation using continuation_token field of AzureError if the token is available.
        '''
    async def update_access_control_recursive(self, acl: str, **kwargs: Any) -> AccessControlChangeResult:
        '''
        Modifies the Access Control on a path and sub-paths.

        :param acl:
            Modifies POSIX access control rights on files and directories.
            The value is a comma-separated list of access control entries. Each
            access control entry (ACE) consists of a scope, a type, a user or
            group identifier, and permissions in the format
            "[scope:][type]:[id]:[permissions]".
        :type acl: str
        :keyword func(~azure.storage.filedatalake.AccessControlChanges) progress_hook:
            Callback where the caller can track progress of the operation
            as well as collect paths that failed to change Access Control.
        :keyword str continuation_token:
            Optional continuation token that can be used to resume previously stopped operation.
        :keyword int batch_size:
            Optional. If data set size exceeds batch size then operation will be split into multiple
            requests so that progress can be tracked. Batch size should be between 1 and 2000.
            The default when unspecified is 2000.
        :keyword int max_batches:
            Optional. Defines maximum number of batches that single,
            change Access Control operation can execute.
            If maximum is reached before all sub-paths are processed,
            then continuation token can be used to resume operation.
            Empty value indicates that maximum number of batches in unbound and operation continues till end.
        :keyword bool continue_on_failure:
            If set to False, the operation will terminate quickly on encountering user errors (4XX).
            If True, the operation will ignore user errors and proceed with the operation on other sub-entities of
            the directory.
            Continuation token will only be returned when continue_on_failure is True in case of user errors.
            If not set the default value is False for this.
        :keyword int timeout:
            Sets the server-side timeout for the operation in seconds. For more details see
            https://learn.microsoft.com/rest/api/storageservices/setting-timeouts-for-blob-service-operations.
            This value is not tracked or validated on the client. To configure client-side network timesouts
            see `here <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-file-datalake
            #other-client--per-operation-configuration>`_.
        :return: A summary of the recursive operations, including the count of successes and failures,
            as well as a continuation token in case the operation was terminated prematurely.
        :rtype: :~azure.storage.filedatalake.AccessControlChangeResult`
        :raises ~azure.core.exceptions.AzureError:
            User can restart the operation using continuation_token field of AzureError if the token is available.
        '''
    async def remove_access_control_recursive(self, acl: str, **kwargs: Any) -> AccessControlChangeResult:
        '''
        Removes the Access Control on a path and sub-paths.

        :param acl:
            Removes POSIX access control rights on files and directories.
            The value is a comma-separated list of access control entries. Each
            access control entry (ACE) consists of a scope, a type, and a user or
            group identifier in the format "[scope:][type]:[id]".
        :type acl: str
        :keyword func(~azure.storage.filedatalake.AccessControlChanges) progress_hook:
            Callback where the caller can track progress of the operation
            as well as collect paths that failed to change Access Control.
        :keyword str continuation_token:
            Optional continuation token that can be used to resume previously stopped operation.
        :keyword int batch_size:
            Optional. If data set size exceeds batch size then operation will be split into multiple
            requests so that progress can be tracked. Batch size should be between 1 and 2000.
            The default when unspecified is 2000.
        :keyword int max_batches:
            Optional. Defines maximum number of batches that single change Access Control operation can execute.
            If maximum is reached before all sub-paths are processed,
            then continuation token can be used to resume operation.
            Empty value indicates that maximum number of batches in unbound and operation continues till end.
        :keyword bool continue_on_failure:
            If set to False, the operation will terminate quickly on encountering user errors (4XX).
            If True, the operation will ignore user errors and proceed with the operation on other sub-entities of
            the directory.
            Continuation token will only be returned when continue_on_failure is True in case of user errors.
            If not set the default value is False for this.
        :keyword int timeout:
            Sets the server-side timeout for the operation in seconds. For more details see
            https://learn.microsoft.com/rest/api/storageservices/setting-timeouts-for-blob-service-operations.
            This value is not tracked or validated on the client. To configure client-side network timesouts
            see `here <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-file-datalake
            #other-client--per-operation-configuration>`_.
        :return: A summary of the recursive operations, including the count of successes and failures,
            as well as a continuation token in case the operation was terminated prematurely.
        :rtype: :~azure.storage.filedatalake.AccessControlChangeResult`
        :raises ~azure.core.exceptions.AzureError:
            User can restart the operation using continuation_token field of AzureError if the token is available.
        '''
    async def set_metadata(self, metadata: Dict[str, str], **kwargs) -> Dict[str, str | datetime]:
        """Sets one or more user-defined name-value pairs for the specified
        file system. Each call to this operation replaces all existing metadata
        attached to the file system. To remove all metadata from the file system,
        call this operation with no metadata dict.

        :param metadata:
            A dict containing name-value pairs to associate with the file system as
            metadata. Example: {'category':'test'}
        :type metadata: dict[str, str]
        :keyword lease:
            If specified, set_file_system_metadata only succeeds if the
            file system's lease is active and matches this ID.
        :paramtype lease: ~azure.storage.filedatalake.aio.DataLakeLeaseClient or str
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
        :keyword ~azure.storage.filedatalake.CustomerProvidedEncryptionKey cpk:
            Encrypts the data on the service-side with the given key.
            Use of customer-provided keys must be done over HTTPS.
        :keyword int timeout:
            Sets the server-side timeout for the operation in seconds. For more details see
            https://learn.microsoft.com/rest/api/storageservices/setting-timeouts-for-blob-service-operations.
            This value is not tracked or validated on the client. To configure client-side network timesouts
            see `here <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-file-datalake
            #other-client--per-operation-configuration>`_.
        :returns: file system-updated property dict (Etag and last modified).
        """
    async def set_http_headers(self, content_settings: ContentSettings | None = None, **kwargs) -> Dict[str, Any]:
        """Sets system properties on the file or directory.

        If one property is set for the content_settings, all properties will be overridden.

        :param ~azure.storage.filedatalake.ContentSettings content_settings:
            ContentSettings object used to set file/directory properties.
        :keyword lease:
            If specified, set_file_system_metadata only succeeds if the
            file system's lease is active and matches this ID.
        :paramtype lease: ~azure.storage.filedatalake.aio.DataLakeLeaseClient or str
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
            see `here <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-file-datalake
            #other-client--per-operation-configuration>`_.
        :returns: file/directory-updated property dict (Etag and last modified)
        :rtype: Dict[str, Any]
        """
    async def acquire_lease(self, lease_duration: int | None = -1, lease_id: str | None = None, **kwargs) -> DataLakeLeaseClient:
        """
        Requests a new lease. If the file or directory does not have an active lease,
        the DataLake service creates a lease on the file/directory and returns a new
        lease ID.

        :param int lease_duration:
            Specifies the duration of the lease, in seconds, or negative one
            (-1) for a lease that never expires. A non-infinite lease can be
            between 15 and 60 seconds. A lease duration cannot be changed
            using renew or change. Default is -1 (infinite lease).
        :param str lease_id:
            Proposed lease ID, in a GUID string format. The DataLake service returns
            400 (Invalid request) if the proposed lease ID is not in the correct format.
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
            see `here <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-file-datalake
            #other-client--per-operation-configuration>`_.
        :returns: A DataLakeLeaseClient object, that can be run in a context manager.
        :rtype: ~azure.storage.filedatalake.aio.DataLakeLeaseClient

        .. admonition:: Example:

            .. literalinclude:: ../samples/test_file_system_samples.py
                :start-after: [START acquire_lease_on_file_system]
                :end-before: [END acquire_lease_on_file_system]
                :language: python
                :dedent: 8
                :caption: Acquiring a lease on the file_system.
        """
