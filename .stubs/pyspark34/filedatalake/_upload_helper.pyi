from ._deserialize import process_storage_error as process_storage_error
from ._shared.response_handlers import return_response_headers as return_response_headers
from ._shared.uploads import DataLakeFileChunkUploader as DataLakeFileChunkUploader, upload_data_chunks as upload_data_chunks, upload_substream_blocks as upload_substream_blocks
from _typeshed import Incomplete

def upload_datalake_file(client: Incomplete | None = None, stream: Incomplete | None = None, length: Incomplete | None = None, overwrite: Incomplete | None = None, validate_content: Incomplete | None = None, max_concurrency: Incomplete | None = None, file_settings: Incomplete | None = None, **kwargs): ...
