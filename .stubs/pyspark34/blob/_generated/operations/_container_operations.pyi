import datetime
from .. import models as _models
from .._serialization import Serializer as Serializer
from _typeshed import Incomplete
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from typing import Any, Callable, Dict, IO, Iterator, List, TypeVar

T = TypeVar('T')
ClsType = Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any] | None

def build_create_request(url: str, *, timeout: int | None = None, metadata: Dict[str, str] | None = None, access: str | _models.PublicAccessType | None = None, request_id_parameter: str | None = None, default_encryption_scope: str | None = None, prevent_encryption_scope_override: bool | None = None, **kwargs: Any) -> HttpRequest: ...
def build_get_properties_request(url: str, *, timeout: int | None = None, lease_id: str | None = None, request_id_parameter: str | None = None, **kwargs: Any) -> HttpRequest: ...
def build_delete_request(url: str, *, timeout: int | None = None, lease_id: str | None = None, if_modified_since: datetime.datetime | None = None, if_unmodified_since: datetime.datetime | None = None, request_id_parameter: str | None = None, **kwargs: Any) -> HttpRequest: ...
def build_set_metadata_request(url: str, *, timeout: int | None = None, lease_id: str | None = None, metadata: Dict[str, str] | None = None, if_modified_since: datetime.datetime | None = None, request_id_parameter: str | None = None, **kwargs: Any) -> HttpRequest: ...
def build_get_access_policy_request(url: str, *, timeout: int | None = None, lease_id: str | None = None, request_id_parameter: str | None = None, **kwargs: Any) -> HttpRequest: ...
def build_set_access_policy_request(url: str, *, timeout: int | None = None, lease_id: str | None = None, access: str | _models.PublicAccessType | None = None, if_modified_since: datetime.datetime | None = None, if_unmodified_since: datetime.datetime | None = None, request_id_parameter: str | None = None, content: Any = None, **kwargs: Any) -> HttpRequest: ...
def build_restore_request(url: str, *, timeout: int | None = None, request_id_parameter: str | None = None, deleted_container_name: str | None = None, deleted_container_version: str | None = None, **kwargs: Any) -> HttpRequest: ...
def build_rename_request(url: str, *, source_container_name: str, timeout: int | None = None, request_id_parameter: str | None = None, source_lease_id: str | None = None, **kwargs: Any) -> HttpRequest: ...
def build_submit_batch_request(url: str, *, content_length: int, content: IO, timeout: int | None = None, request_id_parameter: str | None = None, **kwargs: Any) -> HttpRequest: ...
def build_filter_blobs_request(url: str, *, timeout: int | None = None, request_id_parameter: str | None = None, where: str | None = None, marker: str | None = None, maxresults: int | None = None, include: List[str | _models.FilterBlobsIncludeItem] | None = None, **kwargs: Any) -> HttpRequest: ...
def build_acquire_lease_request(url: str, *, timeout: int | None = None, duration: int | None = None, proposed_lease_id: str | None = None, if_modified_since: datetime.datetime | None = None, if_unmodified_since: datetime.datetime | None = None, request_id_parameter: str | None = None, **kwargs: Any) -> HttpRequest: ...
def build_release_lease_request(url: str, *, lease_id: str, timeout: int | None = None, if_modified_since: datetime.datetime | None = None, if_unmodified_since: datetime.datetime | None = None, request_id_parameter: str | None = None, **kwargs: Any) -> HttpRequest: ...
def build_renew_lease_request(url: str, *, lease_id: str, timeout: int | None = None, if_modified_since: datetime.datetime | None = None, if_unmodified_since: datetime.datetime | None = None, request_id_parameter: str | None = None, **kwargs: Any) -> HttpRequest: ...
def build_break_lease_request(url: str, *, timeout: int | None = None, break_period: int | None = None, if_modified_since: datetime.datetime | None = None, if_unmodified_since: datetime.datetime | None = None, request_id_parameter: str | None = None, **kwargs: Any) -> HttpRequest: ...
def build_change_lease_request(url: str, *, lease_id: str, proposed_lease_id: str, timeout: int | None = None, if_modified_since: datetime.datetime | None = None, if_unmodified_since: datetime.datetime | None = None, request_id_parameter: str | None = None, **kwargs: Any) -> HttpRequest: ...
def build_list_blob_flat_segment_request(url: str, *, prefix: str | None = None, marker: str | None = None, maxresults: int | None = None, include: List[str | _models.ListBlobsIncludeItem] | None = None, timeout: int | None = None, request_id_parameter: str | None = None, **kwargs: Any) -> HttpRequest: ...
def build_list_blob_hierarchy_segment_request(url: str, *, delimiter: str, prefix: str | None = None, marker: str | None = None, maxresults: int | None = None, include: List[str | _models.ListBlobsIncludeItem] | None = None, timeout: int | None = None, request_id_parameter: str | None = None, **kwargs: Any) -> HttpRequest: ...
def build_get_account_info_request(url: str, **kwargs: Any) -> HttpRequest: ...

class ContainerOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.storage.blob.AzureBlobStorage`'s
        :attr:`container` attribute.
    """
    models: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def create(self, timeout: int | None = None, metadata: Dict[str, str] | None = None, access: str | _models.PublicAccessType | None = None, request_id_parameter: str | None = None, container_cpk_scope_info: _models.ContainerCpkScopeInfo | None = None, **kwargs: Any) -> None:
        '''creates a new container under the specified account. If the container with the same name
        already exists, the operation fails.

        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param metadata: Optional. Specifies a user-defined name-value pair associated with the blob.
         If no name-value pairs are specified, the operation will copy the metadata from the source blob
         or file to the destination blob. If one or more name-value pairs are specified, the destination
         blob is created with the specified metadata, and metadata is not copied from the source blob or
         file. Note that beginning with version 2009-09-19, metadata names must adhere to the naming
         rules for C# identifiers. See Naming and Referencing Containers, Blobs, and Metadata for more
         information. Default value is None.
        :type metadata: dict[str, str]
        :param access: Specifies whether data in the container may be accessed publicly and the level
         of access. Known values are: "container" and "blob". Default value is None.
        :type access: str or ~azure.storage.blob.models.PublicAccessType
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param container_cpk_scope_info: Parameter group. Default value is None.
        :type container_cpk_scope_info: ~azure.storage.blob.models.ContainerCpkScopeInfo
        :keyword restype: restype. Default value is "container". Note that overriding this default
         value may result in unsupported behavior.
        :paramtype restype: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    def get_properties(self, timeout: int | None = None, request_id_parameter: str | None = None, lease_access_conditions: _models.LeaseAccessConditions | None = None, **kwargs: Any) -> None:
        '''returns all user-defined metadata and system properties for the specified container. The data
        returned does not include the container\'s list of blobs.

        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param lease_access_conditions: Parameter group. Default value is None.
        :type lease_access_conditions: ~azure.storage.blob.models.LeaseAccessConditions
        :keyword restype: restype. Default value is "container". Note that overriding this default
         value may result in unsupported behavior.
        :paramtype restype: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    def delete(self, timeout: int | None = None, request_id_parameter: str | None = None, lease_access_conditions: _models.LeaseAccessConditions | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, **kwargs: Any) -> None:
        '''operation marks the specified container for deletion. The container and any blobs contained
        within it are later deleted during garbage collection.

        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param lease_access_conditions: Parameter group. Default value is None.
        :type lease_access_conditions: ~azure.storage.blob.models.LeaseAccessConditions
        :param modified_access_conditions: Parameter group. Default value is None.
        :type modified_access_conditions: ~azure.storage.blob.models.ModifiedAccessConditions
        :keyword restype: restype. Default value is "container". Note that overriding this default
         value may result in unsupported behavior.
        :paramtype restype: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    def set_metadata(self, timeout: int | None = None, metadata: Dict[str, str] | None = None, request_id_parameter: str | None = None, lease_access_conditions: _models.LeaseAccessConditions | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, **kwargs: Any) -> None:
        '''operation sets one or more user-defined name-value pairs for the specified container.

        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param metadata: Optional. Specifies a user-defined name-value pair associated with the blob.
         If no name-value pairs are specified, the operation will copy the metadata from the source blob
         or file to the destination blob. If one or more name-value pairs are specified, the destination
         blob is created with the specified metadata, and metadata is not copied from the source blob or
         file. Note that beginning with version 2009-09-19, metadata names must adhere to the naming
         rules for C# identifiers. See Naming and Referencing Containers, Blobs, and Metadata for more
         information. Default value is None.
        :type metadata: dict[str, str]
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param lease_access_conditions: Parameter group. Default value is None.
        :type lease_access_conditions: ~azure.storage.blob.models.LeaseAccessConditions
        :param modified_access_conditions: Parameter group. Default value is None.
        :type modified_access_conditions: ~azure.storage.blob.models.ModifiedAccessConditions
        :keyword restype: restype. Default value is "container". Note that overriding this default
         value may result in unsupported behavior.
        :paramtype restype: str
        :keyword comp: comp. Default value is "metadata". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    def get_access_policy(self, timeout: int | None = None, request_id_parameter: str | None = None, lease_access_conditions: _models.LeaseAccessConditions | None = None, **kwargs: Any) -> List[_models.SignedIdentifier]:
        '''gets the permissions for the specified container. The permissions indicate whether container
        data may be accessed publicly.

        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param lease_access_conditions: Parameter group. Default value is None.
        :type lease_access_conditions: ~azure.storage.blob.models.LeaseAccessConditions
        :keyword restype: restype. Default value is "container". Note that overriding this default
         value may result in unsupported behavior.
        :paramtype restype: str
        :keyword comp: comp. Default value is "acl". Note that overriding this default value may result
         in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of SignedIdentifier or the result of cls(response)
        :rtype: list[~azure.storage.blob.models.SignedIdentifier]
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    def set_access_policy(self, timeout: int | None = None, access: str | _models.PublicAccessType | None = None, request_id_parameter: str | None = None, lease_access_conditions: _models.LeaseAccessConditions | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, container_acl: List[_models.SignedIdentifier] | None = None, **kwargs: Any) -> None:
        '''sets the permissions for the specified container. The permissions indicate whether blobs in a
        container may be accessed publicly.

        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param access: Specifies whether data in the container may be accessed publicly and the level
         of access. Known values are: "container" and "blob". Default value is None.
        :type access: str or ~azure.storage.blob.models.PublicAccessType
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param lease_access_conditions: Parameter group. Default value is None.
        :type lease_access_conditions: ~azure.storage.blob.models.LeaseAccessConditions
        :param modified_access_conditions: Parameter group. Default value is None.
        :type modified_access_conditions: ~azure.storage.blob.models.ModifiedAccessConditions
        :param container_acl: the acls for the container. Default value is None.
        :type container_acl: list[~azure.storage.blob.models.SignedIdentifier]
        :keyword restype: restype. Default value is "container". Note that overriding this default
         value may result in unsupported behavior.
        :paramtype restype: str
        :keyword comp: comp. Default value is "acl". Note that overriding this default value may result
         in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    def restore(self, timeout: int | None = None, request_id_parameter: str | None = None, deleted_container_name: str | None = None, deleted_container_version: str | None = None, **kwargs: Any) -> None:
        '''Restores a previously-deleted container.

        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param deleted_container_name: Optional.  Version 2019-12-12 and later.  Specifies the name of
         the deleted container to restore. Default value is None.
        :type deleted_container_name: str
        :param deleted_container_version: Optional.  Version 2019-12-12 and later.  Specifies the
         version of the deleted container to restore. Default value is None.
        :type deleted_container_version: str
        :keyword restype: restype. Default value is "container". Note that overriding this default
         value may result in unsupported behavior.
        :paramtype restype: str
        :keyword comp: comp. Default value is "undelete". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    def rename(self, source_container_name: str, timeout: int | None = None, request_id_parameter: str | None = None, source_lease_id: str | None = None, **kwargs: Any) -> None:
        '''Renames an existing container.

        :param source_container_name: Required.  Specifies the name of the container to rename.
         Required.
        :type source_container_name: str
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param source_lease_id: A lease ID for the source path. If specified, the source path must have
         an active lease and the lease ID must match. Default value is None.
        :type source_lease_id: str
        :keyword restype: restype. Default value is "container". Note that overriding this default
         value may result in unsupported behavior.
        :paramtype restype: str
        :keyword comp: comp. Default value is "rename". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    def submit_batch(self, content_length: int, body: IO, timeout: int | None = None, request_id_parameter: str | None = None, **kwargs: Any) -> Iterator[bytes]:
        '''The Batch operation allows multiple API calls to be embedded into a single HTTP request.

        :param content_length: The length of the request. Required.
        :type content_length: int
        :param body: Initial data. Required.
        :type body: IO
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :keyword restype: restype. Default value is "container". Note that overriding this default
         value may result in unsupported behavior.
        :paramtype restype: str
        :keyword comp: comp. Default value is "batch". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Iterator of the response bytes or the result of cls(response)
        :rtype: Iterator[bytes]
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    def filter_blobs(self, timeout: int | None = None, request_id_parameter: str | None = None, where: str | None = None, marker: str | None = None, maxresults: int | None = None, include: List[str | _models.FilterBlobsIncludeItem] | None = None, **kwargs: Any) -> _models.FilterBlobSegment:
        '''The Filter Blobs operation enables callers to list blobs in a container whose tags match a
        given search expression.  Filter blobs searches within the given container.

        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param where: Filters the results to return only to return only blobs whose tags match the
         specified expression. Default value is None.
        :type where: str
        :param marker: A string value that identifies the portion of the list of containers to be
         returned with the next listing operation. The operation returns the NextMarker value within the
         response body if the listing operation did not return all containers remaining to be listed
         with the current page. The NextMarker value can be used as the value for the marker parameter
         in a subsequent call to request the next page of list items. The marker value is opaque to the
         client. Default value is None.
        :type marker: str
        :param maxresults: Specifies the maximum number of containers to return. If the request does
         not specify maxresults, or specifies a value greater than 5000, the server will return up to
         5000 items. Note that if the listing operation crosses a partition boundary, then the service
         will return a continuation token for retrieving the remainder of the results. For this reason,
         it is possible that the service will return fewer results than specified by maxresults, or than
         the default of 5000. Default value is None.
        :type maxresults: int
        :param include: Include this parameter to specify one or more datasets to include in the
         response. Default value is None.
        :type include: list[str or ~azure.storage.blob.models.FilterBlobsIncludeItem]
        :keyword restype: restype. Default value is "container". Note that overriding this default
         value may result in unsupported behavior.
        :paramtype restype: str
        :keyword comp: comp. Default value is "blobs". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: FilterBlobSegment or the result of cls(response)
        :rtype: ~azure.storage.blob.models.FilterBlobSegment
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    def acquire_lease(self, timeout: int | None = None, duration: int | None = None, proposed_lease_id: str | None = None, request_id_parameter: str | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, **kwargs: Any) -> None:
        '''[Update] establishes and manages a lock on a container for delete operations. The lock duration
        can be 15 to 60 seconds, or can be infinite.

        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param duration: Specifies the duration of the lease, in seconds, or negative one (-1) for a
         lease that never expires. A non-infinite lease can be between 15 and 60 seconds. A lease
         duration cannot be changed using renew or change. Default value is None.
        :type duration: int
        :param proposed_lease_id: Proposed lease ID, in a GUID string format. The Blob service returns
         400 (Invalid request) if the proposed lease ID is not in the correct format. See Guid
         Constructor (String) for a list of valid GUID string formats. Default value is None.
        :type proposed_lease_id: str
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param modified_access_conditions: Parameter group. Default value is None.
        :type modified_access_conditions: ~azure.storage.blob.models.ModifiedAccessConditions
        :keyword comp: comp. Default value is "lease". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword restype: restype. Default value is "container". Note that overriding this default
         value may result in unsupported behavior.
        :paramtype restype: str
        :keyword action: Describes what lease action to take. Default value is "acquire". Note that
         overriding this default value may result in unsupported behavior.
        :paramtype action: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    def release_lease(self, lease_id: str, timeout: int | None = None, request_id_parameter: str | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, **kwargs: Any) -> None:
        '''[Update] establishes and manages a lock on a container for delete operations. The lock duration
        can be 15 to 60 seconds, or can be infinite.

        :param lease_id: Specifies the current lease ID on the resource. Required.
        :type lease_id: str
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param modified_access_conditions: Parameter group. Default value is None.
        :type modified_access_conditions: ~azure.storage.blob.models.ModifiedAccessConditions
        :keyword comp: comp. Default value is "lease". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword restype: restype. Default value is "container". Note that overriding this default
         value may result in unsupported behavior.
        :paramtype restype: str
        :keyword action: Describes what lease action to take. Default value is "release". Note that
         overriding this default value may result in unsupported behavior.
        :paramtype action: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    def renew_lease(self, lease_id: str, timeout: int | None = None, request_id_parameter: str | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, **kwargs: Any) -> None:
        '''[Update] establishes and manages a lock on a container for delete operations. The lock duration
        can be 15 to 60 seconds, or can be infinite.

        :param lease_id: Specifies the current lease ID on the resource. Required.
        :type lease_id: str
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param modified_access_conditions: Parameter group. Default value is None.
        :type modified_access_conditions: ~azure.storage.blob.models.ModifiedAccessConditions
        :keyword comp: comp. Default value is "lease". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword restype: restype. Default value is "container". Note that overriding this default
         value may result in unsupported behavior.
        :paramtype restype: str
        :keyword action: Describes what lease action to take. Default value is "renew". Note that
         overriding this default value may result in unsupported behavior.
        :paramtype action: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    def break_lease(self, timeout: int | None = None, break_period: int | None = None, request_id_parameter: str | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, **kwargs: Any) -> None:
        '''[Update] establishes and manages a lock on a container for delete operations. The lock duration
        can be 15 to 60 seconds, or can be infinite.

        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param break_period: For a break operation, proposed duration the lease should continue before
         it is broken, in seconds, between 0 and 60. This break period is only used if it is shorter
         than the time remaining on the lease. If longer, the time remaining on the lease is used. A new
         lease will not be available before the break period has expired, but the lease may be held for
         longer than the break period. If this header does not appear with a break operation, a
         fixed-duration lease breaks after the remaining lease period elapses, and an infinite lease
         breaks immediately. Default value is None.
        :type break_period: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param modified_access_conditions: Parameter group. Default value is None.
        :type modified_access_conditions: ~azure.storage.blob.models.ModifiedAccessConditions
        :keyword comp: comp. Default value is "lease". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword restype: restype. Default value is "container". Note that overriding this default
         value may result in unsupported behavior.
        :paramtype restype: str
        :keyword action: Describes what lease action to take. Default value is "break". Note that
         overriding this default value may result in unsupported behavior.
        :paramtype action: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    def change_lease(self, lease_id: str, proposed_lease_id: str, timeout: int | None = None, request_id_parameter: str | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, **kwargs: Any) -> None:
        '''[Update] establishes and manages a lock on a container for delete operations. The lock duration
        can be 15 to 60 seconds, or can be infinite.

        :param lease_id: Specifies the current lease ID on the resource. Required.
        :type lease_id: str
        :param proposed_lease_id: Proposed lease ID, in a GUID string format. The Blob service returns
         400 (Invalid request) if the proposed lease ID is not in the correct format. See Guid
         Constructor (String) for a list of valid GUID string formats. Required.
        :type proposed_lease_id: str
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param modified_access_conditions: Parameter group. Default value is None.
        :type modified_access_conditions: ~azure.storage.blob.models.ModifiedAccessConditions
        :keyword comp: comp. Default value is "lease". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword restype: restype. Default value is "container". Note that overriding this default
         value may result in unsupported behavior.
        :paramtype restype: str
        :keyword action: Describes what lease action to take. Default value is "change". Note that
         overriding this default value may result in unsupported behavior.
        :paramtype action: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    def list_blob_flat_segment(self, prefix: str | None = None, marker: str | None = None, maxresults: int | None = None, include: List[str | _models.ListBlobsIncludeItem] | None = None, timeout: int | None = None, request_id_parameter: str | None = None, **kwargs: Any) -> _models.ListBlobsFlatSegmentResponse:
        '''[Update] The List Blobs operation returns a list of the blobs under the specified container.

        :param prefix: Filters the results to return only containers whose name begins with the
         specified prefix. Default value is None.
        :type prefix: str
        :param marker: A string value that identifies the portion of the list of containers to be
         returned with the next listing operation. The operation returns the NextMarker value within the
         response body if the listing operation did not return all containers remaining to be listed
         with the current page. The NextMarker value can be used as the value for the marker parameter
         in a subsequent call to request the next page of list items. The marker value is opaque to the
         client. Default value is None.
        :type marker: str
        :param maxresults: Specifies the maximum number of containers to return. If the request does
         not specify maxresults, or specifies a value greater than 5000, the server will return up to
         5000 items. Note that if the listing operation crosses a partition boundary, then the service
         will return a continuation token for retrieving the remainder of the results. For this reason,
         it is possible that the service will return fewer results than specified by maxresults, or than
         the default of 5000. Default value is None.
        :type maxresults: int
        :param include: Include this parameter to specify one or more datasets to include in the
         response. Default value is None.
        :type include: list[str or ~azure.storage.blob.models.ListBlobsIncludeItem]
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :keyword restype: restype. Default value is "container". Note that overriding this default
         value may result in unsupported behavior.
        :paramtype restype: str
        :keyword comp: comp. Default value is "list". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ListBlobsFlatSegmentResponse or the result of cls(response)
        :rtype: ~azure.storage.blob.models.ListBlobsFlatSegmentResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    def list_blob_hierarchy_segment(self, delimiter: str, prefix: str | None = None, marker: str | None = None, maxresults: int | None = None, include: List[str | _models.ListBlobsIncludeItem] | None = None, timeout: int | None = None, request_id_parameter: str | None = None, **kwargs: Any) -> _models.ListBlobsHierarchySegmentResponse:
        '''[Update] The List Blobs operation returns a list of the blobs under the specified container.

        :param delimiter: When the request includes this parameter, the operation returns a BlobPrefix
         element in the response body that acts as a placeholder for all blobs whose names begin with
         the same substring up to the appearance of the delimiter character. The delimiter may be a
         single character or a string. Required.
        :type delimiter: str
        :param prefix: Filters the results to return only containers whose name begins with the
         specified prefix. Default value is None.
        :type prefix: str
        :param marker: A string value that identifies the portion of the list of containers to be
         returned with the next listing operation. The operation returns the NextMarker value within the
         response body if the listing operation did not return all containers remaining to be listed
         with the current page. The NextMarker value can be used as the value for the marker parameter
         in a subsequent call to request the next page of list items. The marker value is opaque to the
         client. Default value is None.
        :type marker: str
        :param maxresults: Specifies the maximum number of containers to return. If the request does
         not specify maxresults, or specifies a value greater than 5000, the server will return up to
         5000 items. Note that if the listing operation crosses a partition boundary, then the service
         will return a continuation token for retrieving the remainder of the results. For this reason,
         it is possible that the service will return fewer results than specified by maxresults, or than
         the default of 5000. Default value is None.
        :type maxresults: int
        :param include: Include this parameter to specify one or more datasets to include in the
         response. Default value is None.
        :type include: list[str or ~azure.storage.blob.models.ListBlobsIncludeItem]
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :keyword restype: restype. Default value is "container". Note that overriding this default
         value may result in unsupported behavior.
        :paramtype restype: str
        :keyword comp: comp. Default value is "list". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ListBlobsHierarchySegmentResponse or the result of cls(response)
        :rtype: ~azure.storage.blob.models.ListBlobsHierarchySegmentResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
    def get_account_info(self, **kwargs: Any) -> None:
        '''Returns the sku name and account kind.

        :keyword restype: restype. Default value is "account". Note that overriding this default value
         may result in unsupported behavior.
        :paramtype restype: str
        :keyword comp: comp. Default value is "properties". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        '''
