import concurrent.futures
from _typeshed import Incomplete
from typing import Tuple
from wandb.filesync import stats as stats, step_checksum as step_checksum, step_upload as step_upload
from wandb.sdk.artifacts.artifact_manifest import ArtifactManifest as ArtifactManifest
from wandb.sdk.artifacts.artifact_saver import SaveFn as SaveFn, SaveFnAsync as SaveFnAsync
from wandb.sdk.internal import file_stream as file_stream, internal_api as internal_api
from wandb.sdk.internal.settings_static import SettingsStatic as SettingsStatic
from wandb.sdk.lib.paths import LogicalPath as LogicalPath

TMP_DIR: Incomplete
logger: Incomplete

class FilePusher:
    """Parallel file upload class.

    This manages uploading multiple files in parallel. It will restart a given file's
    upload job if it receives a notification that that file has been modified. The
    finish() method will block until all events have been processed and all uploads are
    complete.
    """
    MAX_UPLOAD_JOBS: int
    def __init__(self, api: internal_api.Api, file_stream: file_stream.FileStreamApi, settings: SettingsStatic | None = None) -> None: ...
    def get_status(self) -> Tuple[bool, stats.Summary]: ...
    def print_status(self, prefix: bool = True) -> None: ...
    def file_counts_by_category(self) -> stats.FileCountsByCategory: ...
    def file_changed(self, save_name: LogicalPath, path: str, copy: bool = True):
        """Tell the file pusher that a file's changed and should be uploaded.

        Arguments:
            save_name: string logical location of the file relative to the run
                directory.
            path: actual string path of the file to upload on the filesystem.
        """
    def store_manifest_files(self, manifest: ArtifactManifest, artifact_id: str, save_fn: SaveFn, save_fn_async: SaveFnAsync) -> None: ...
    def commit_artifact(self, artifact_id: str, *, finalize: bool = True, before_commit: step_upload.PreCommitFn, result_future: concurrent.futures.Future[None]): ...
    def finish(self, callback: step_upload.OnRequestFinishFn | None = None): ...
    def join(self) -> None: ...
    def is_alive(self) -> bool: ...
