from ._encryption import GCMBlobEncryptionStream as GCMBlobEncryptionStream, encrypt_blob as encrypt_blob, generate_blob_encryption_data as generate_blob_encryption_data, get_adjusted_upload_size as get_adjusted_upload_size, get_blob_encryptor_and_padder as get_blob_encryptor_and_padder
from ._generated.models import AppendPositionAccessConditions as AppendPositionAccessConditions, BlockLookupList as BlockLookupList, ModifiedAccessConditions as ModifiedAccessConditions
from ._shared.models import StorageErrorCode as StorageErrorCode
from ._shared.response_handlers import process_storage_error as process_storage_error, return_response_headers as return_response_headers
from ._shared.uploads import AppendBlobChunkUploader as AppendBlobChunkUploader, BlockBlobChunkUploader as BlockBlobChunkUploader, PageBlobChunkUploader as PageBlobChunkUploader, upload_data_chunks as upload_data_chunks, upload_substream_blocks as upload_substream_blocks
from _typeshed import Incomplete
from typing import TypeVar

BlobLeaseClient = TypeVar('BlobLeaseClient')

def upload_block_blob(client: Incomplete | None = None, data: Incomplete | None = None, stream: Incomplete | None = None, length: Incomplete | None = None, overwrite: Incomplete | None = None, headers: Incomplete | None = None, validate_content: Incomplete | None = None, max_concurrency: Incomplete | None = None, blob_settings: Incomplete | None = None, encryption_options: Incomplete | None = None, **kwargs): ...
def upload_page_blob(client: Incomplete | None = None, stream: Incomplete | None = None, length: Incomplete | None = None, overwrite: Incomplete | None = None, headers: Incomplete | None = None, validate_content: Incomplete | None = None, max_concurrency: Incomplete | None = None, blob_settings: Incomplete | None = None, encryption_options: Incomplete | None = None, **kwargs): ...
def upload_append_blob(client: Incomplete | None = None, stream: Incomplete | None = None, length: Incomplete | None = None, overwrite: Incomplete | None = None, headers: Incomplete | None = None, validate_content: Incomplete | None = None, max_concurrency: Incomplete | None = None, blob_settings: Incomplete | None = None, encryption_options: Incomplete | None = None, **kwargs): ...
