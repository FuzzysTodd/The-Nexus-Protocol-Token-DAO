def match_blob_version(blob, version_id: str | None): ...
async def filter_blobs(blobs, target_path, delimiter: str = '/', version_id: str | None = None, versions: bool = False):
    """
    Filters out blobs that do not come from target_path

    Parameters
    ----------
    blobs:  A list of candidate blobs to be returned from Azure

    target_path: Actual prefix of the blob folder

    delimiter: str
            Delimiter used to separate containers and files

    version_id: Spefic blob version ID to be returned
    """
async def get_blob_metadata(container_client, path, version_id: str | None = None): ...
async def close_service_client(fs) -> None:
    """
    Implements asynchronous closure of service client for
    AzureBlobFile objects
    """
async def close_container_client(file_obj) -> None:
    """
    Implements asynchronous closure of container client for
    AzureBlobFile objects
    """
async def close_credential(file_obj) -> None:
    """
    Implements asynchronous closure of credentials for
    AzureBlobFile objects
    """
