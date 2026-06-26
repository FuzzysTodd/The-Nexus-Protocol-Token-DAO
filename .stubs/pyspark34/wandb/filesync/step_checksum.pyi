import concurrent.futures
import queue
import tempfile
from typing import NamedTuple
from wandb.filesync import stats as stats, step_upload as step_upload
from wandb.sdk.artifacts.artifact_manifest import ArtifactManifest as ArtifactManifest
from wandb.sdk.artifacts.artifact_saver import SaveFn as SaveFn, SaveFnAsync as SaveFnAsync
from wandb.sdk.internal import internal_api as internal_api
from wandb.sdk.lib import filesystem as filesystem, runid as runid
from wandb.sdk.lib.paths import LogicalPath as LogicalPath

class RequestUpload(NamedTuple):
    path: str
    save_name: LogicalPath
    copy: bool

class RequestStoreManifestFiles(NamedTuple):
    manifest: ArtifactManifest
    artifact_id: str
    save_fn: SaveFn
    save_fn_async: SaveFnAsync

class RequestCommitArtifact(NamedTuple):
    artifact_id: str
    finalize: bool
    before_commit: step_upload.PreCommitFn
    result_future: concurrent.futures.Future[None]

class RequestFinish(NamedTuple):
    callback: step_upload.OnRequestFinishFn | None
Event = RequestUpload | RequestStoreManifestFiles | RequestCommitArtifact | RequestFinish

class StepChecksum:
    def __init__(self, api: internal_api.Api, tempdir: tempfile.TemporaryDirectory, request_queue: queue.Queue[Event], output_queue: queue.Queue[step_upload.Event], stats: stats.Stats) -> None: ...
    def start(self) -> None: ...
    def is_alive(self) -> bool: ...
    def finish(self) -> None: ...
