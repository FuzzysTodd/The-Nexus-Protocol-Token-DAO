import adlfs
from _typeshed import Incomplete
from azure.core.pipeline import PipelineRequest as PipelineRequest, PipelineResponse as PipelineResponse
from azure.core.pipeline.policies import AsyncHTTPPolicy, SansIOHTTPPolicy as SansIOHTTPPolicy
from azure.storage.blob._shared import models as _models
from fsspec_wrapper.utils import token_service as token_service
from typing import Any, TypeVar

logger: Incomplete

def make_credential(token): ...
AsyncHTTPResponseType = TypeVar('AsyncHTTPResponseType')
HTTPRequestType = TypeVar('HTTPRequestType')

class _SansIOAsyncHTTPPolicyRunnerPandas(AsyncHTTPPolicy[HTTPRequestType, AsyncHTTPResponseType]):
    """Async implementation of the SansIO policy.

    Modifies the request and sends to the next policy in the chain.
    OneLake proxy API is sending a 302 or 307 response if the request
    is coming from a different region. Until proxy API is updated to
    handle the redirection, we are overriding the send method to
    redirect the request if the URL found response is received.
    We can remove this once OneLake proxy API handles the redirection.

    :param policy: A SansIO policy.
    :type policy: ~azure.core.pipeline.policies.SansIOHTTPPolicy
    """
    def __init__(self, policy: SansIOHTTPPolicy) -> None: ...
    async def send(self, request: PipelineRequest) -> PipelineResponse:
        """Modifies the request and sends to the next policy in the chain.

        Redirects the request if 302 or 307 response is received, this can
        be removed once OneLake proxy API handles the redirection.

        :param request: The PipelineRequest object.
        :type request: ~azure.core.pipeline.PipelineRequest
        :return: The PipelineResponse object.
        :rtype: ~azure.core.pipeline.PipelineResponse
        """

async def delete(self, snapshot: str | None = None, version_id: str | None = None, timeout: int | None = None, delete_snapshots: str | _models.DeleteSnapshotsOptionType | None = None, request_id_parameter: str | None = None, blob_delete_type: str | None = 'Permanent', lease_access_conditions: _models.LeaseAccessConditions | None = None, modified_access_conditions: _models.ModifiedAccessConditions | None = None, **kwargs: Any) -> None:
    '''If the storage account\'s soft delete feature is disabled then, when a blob is deleted, it is
    permanently removed from the storage account. If the storage account\'s soft delete feature is
    enabled, then, when a blob is deleted, it is marked for deletion and becomes inaccessible
    immediately. However, the blob service retains the blob or snapshot for the number of days
    specified by the DeleteRetentionPolicy section of [Storage service properties]
    (Set-Blob-Service-Properties.md). After the specified number of days has passed, the blob\'s
    data is permanently removed from the storage account. Note that you continue to be charged for
    the soft-deleted blob\'s storage until it is permanently removed. Use the List Blobs API and
    specify the "include=deleted" query parameter to discover which blobs and snapshots have been
    soft deleted. You can then use the Undelete Blob API to restore a soft-deleted blob. All other
    operations on a soft-deleted blob or snapshot causes the service to return an HTTP status code
    of 404 (ResourceNotFound).
    :param snapshot: The snapshot parameter is an opaque DateTime value that, when present,
     specifies the blob snapshot to retrieve. For more information on working with blob snapshots,
     see :code:`<a
     href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/creating-a-snapshot-of-a-blob">Creating
     a Snapshot of a Blob.</a>`.
    :type snapshot: str
    :param version_id: The version id parameter is an opaque DateTime value that, when present,
     specifies the version of the blob to operate on. It\'s for service version 2019-10-10 and newer.
    :type version_id: str
    :param timeout: The timeout parameter is expressed in seconds. For more information, see
     :code:`<a
     href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
     Timeouts for Blob Service Operations.</a>`.
    :type timeout: int
    :param delete_snapshots: Required if the blob has associated snapshots. Specify one of the
     following two options: include: Delete the base blob and all of its snapshots. only: Delete
     only the blob\'s snapshots and not the blob itself.
    :type delete_snapshots: str or ~azure.storage.blob.models.DeleteSnapshotsOptionType
    :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
     limit that is recorded in the analytics logs when storage analytics logging is enabled.
    :type request_id_parameter: str
    :param blob_delete_type: Optional.  Only possible value is \'permanent\', which specifies to
     permanently delete a blob if blob soft delete is enabled.
    :type blob_delete_type: str
    :param lease_access_conditions: Parameter group.
    :type lease_access_conditions: ~azure.storage.blob.models.LeaseAccessConditions
    :param modified_access_conditions: Parameter group.
    :type modified_access_conditions: ~azure.storage.blob.models.ModifiedAccessConditions
    :keyword callable cls: A custom type or function that will be passed the direct response
    :return: None, or the result of cls(response)
    :rtype: None
    :raises: ~azure.core.exceptions.HttpResponseError
    '''

class OnelakeFileSystem(adlfs.AzureBlobFileSystem):
    """
    Access OneLake File System if it were a file system using Multiprotocol Access

    args and kwargs are passed to ``adlfs.AzureBlobFileSystem``.
    """
    original_kwargs: Incomplete
    account_name: Incomplete
    account_host: Incomplete
    credential: Incomplete
    connection_verify: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    service_client: Incomplete
    account_url: Incomplete
    sas_token: Incomplete
    def do_connect(self) -> None:
        """Connect to the BlobServiceClient, using user-specified connection details.
        Tries credentials first, then connection string and finally account key

        Raises
        ------
        ValueError if none of the connection details are available
        """
    container_client: Incomplete
    def connect_client(self) -> None:
        """Connect to the Asynchronous BlobServiceClient, using user-specified connection details.
        Tries credentials first, then connection string and finally account key

        Raises
        ------
        ValueError if none of the connection details are available
        """
