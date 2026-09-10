from mlflow.utils import rest_utils as rest_utils
from mlflow.utils.file_utils import read_chunk as read_chunk

def put_adls_file_creation(sas_url, headers) -> None:
    """
    Performs an ADLS Azure file create `Put` operation
    (https://docs.microsoft.com/en-us/rest/api/storageservices/datalakestoragegen2/path/create)

    :param sas_url: A shared access signature URL referring to the Azure ADLS server
                    to which the file creation command should be issued.
    :param headers: Additional headers to include in the Put request body
    """
def patch_adls_file_upload(sas_url, local_file, start_byte, size, position, headers, is_single) -> None:
    """
    Performs an ADLS Azure file create `Patch` operation
    (https://docs.microsoft.com/en-us/rest/api/storageservices/datalakestoragegen2/path/update)

    :param sas_url: A shared access signature URL referring to the Azure ADLS server
                    to which the file update command should be issued.
    :param local_file: The local file to upload
    :param start_byte: The starting byte of the local file to upload
    :param size: The number of bytes to upload
    :param position: Positional offset of the data in the Patch request
    :param headers: Additional headers to include in the Patch request body
    :param is_single: Whether this is the only patch operation for this file
    """
def patch_adls_flush(sas_url, position, headers) -> None:
    """
    Performs an ADLS Azure file flush `Patch` operation
    (https://docs.microsoft.com/en-us/rest/api/storageservices/datalakestoragegen2/path/update)

    :param sas_url: A shared access signature URL referring to the Azure ADLS server
                    to which the file update command should be issued.
    :param position: The final size of the file to flush.
    :param headers: Additional headers to include in the Patch request body.
    """
def put_block(sas_url, block_id, data, headers) -> None:
    """
    Performs an Azure `Put Block` operation
    (https://docs.microsoft.com/en-us/rest/api/storageservices/put-block)

    :param sas_url: A shared access signature URL referring to the Azure Block Blob
                    to which the specified data should be staged.
    :param block_id: A base64-encoded string identifying the block.
    :param data: Data to include in the Put Block request body.
    :param headers: Additional headers to include in the Put Block request body
                    (the `x-ms-blob-type` header is always included automatically).
    """
def put_block_list(sas_url, block_list, headers) -> None:
    """
    Performs an Azure `Put Block List` operation
    (https://docs.microsoft.com/en-us/rest/api/storageservices/put-block-list)

    :param sas_url: A shared access signature URL referring to the Azure Block Blob
                    to which the specified data should be staged.
    :param block_list: A list of uncommitted base64-encoded string block IDs to commit. For
                       more information, see
                       https://docs.microsoft.com/en-us/rest/api/storageservices/put-block-list.
    :param headers: Headers to include in the Put Block request body.
    """
