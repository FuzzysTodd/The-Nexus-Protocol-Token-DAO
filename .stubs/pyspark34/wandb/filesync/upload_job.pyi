from _typeshed import Incomplete
from wandb.filesync import dir_watcher as dir_watcher, stats as stats, step_upload as step_upload
from wandb.sdk.internal import file_stream as file_stream, internal_api as internal_api
from wandb.sdk.lib.paths import LogicalPath as LogicalPath

logger: Incomplete

class UploadJob:
    silent: Incomplete
    save_name: Incomplete
    save_path: Incomplete
    artifact_id: Incomplete
    md5: Incomplete
    copied: Incomplete
    save_fn: Incomplete
    digest: Incomplete
    def __init__(self, stats: stats.Stats, api: internal_api.Api, file_stream: file_stream.FileStreamApi, silent: bool, save_name: LogicalPath, path: dir_watcher.PathStr, artifact_id: str | None, md5: str | None, copied: bool, save_fn: step_upload.SaveFn | None, digest: str | None) -> None:
        """A file uploader.

        Arguments:
            push_function: function(save_name, actual_path) which actually uploads
                the file.
            save_name: string logical location of the file relative to the run
                directory.
            path: actual string path of the file to upload on the filesystem.
        """
    def run(self) -> None: ...
    def push(self) -> None: ...
    def progress(self, total_bytes: int) -> None: ...

class UploadJobAsync:
    """Roughly an async equivalent of UploadJob.

    Important differences:
    - `run` is a coroutine
    - If `run()` fails, it falls back to the synchronous UploadJob
    """
    silent: Incomplete
    def __init__(self, stats: stats.Stats, api: internal_api.Api, file_stream: file_stream.FileStreamApi, silent: bool, request: step_upload.RequestUpload, save_fn_async: step_upload.SaveFnAsync) -> None: ...
    async def run(self) -> None: ...
