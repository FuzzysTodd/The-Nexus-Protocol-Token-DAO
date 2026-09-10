import concurrent.futures
import queue
from _typeshed import Incomplete
from typing import Awaitable, Callable, MutableSet, NamedTuple, TypedDict
from wandb.errors.term import termerror as termerror
from wandb.filesync import stats as stats, upload_job as upload_job
from wandb.sdk.internal import file_stream as file_stream, internal_api as internal_api, progress as progress
from wandb.sdk.internal.settings_static import SettingsStatic as SettingsStatic
from wandb.sdk.lib.paths import LogicalPath as LogicalPath

class ArtifactStatus(TypedDict):
    finalize: bool
    pending_count: int
    commit_requested: bool
    pre_commit_callbacks: MutableSet['PreCommitFn']
    result_futures: MutableSet['concurrent.futures.Future[None]']
PreCommitFn = Callable[[], None]
OnRequestFinishFn = Callable[[], None]
SaveFn: Incomplete
SaveFnAsync: Incomplete
logger: Incomplete

class RequestUpload(NamedTuple):
    path: str
    save_name: LogicalPath
    artifact_id: str | None
    md5: str | None
    copied: bool
    save_fn: SaveFn | None
    save_fn_async: SaveFnAsync | None
    digest: str | None

class RequestCommitArtifact(NamedTuple):
    artifact_id: str
    finalize: bool
    before_commit: PreCommitFn
    result_future: concurrent.futures.Future[None]

class RequestFinish(NamedTuple):
    callback: OnRequestFinishFn | None

class EventJobDone(NamedTuple):
    job: RequestUpload
    exc: BaseException | None
Event = RequestUpload | RequestCommitArtifact | RequestFinish | EventJobDone

class AsyncExecutor:
    """Runs async file uploads in a background thread."""
    loop: Incomplete
    loop_thread: Incomplete
    concurrency_limiter: Incomplete
    def __init__(self, pool: concurrent.futures.ThreadPoolExecutor, concurrency_limit: int | None) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def submit(self, coro: Awaitable[None]) -> None: ...

class StepUpload:
    silent: Incomplete
    def __init__(self, api: internal_api.Api, stats: stats.Stats, event_queue: queue.Queue[Event], max_threads: int, file_stream: file_stream.FileStreamApi, settings: SettingsStatic | None = None) -> None: ...
    def start(self) -> None: ...
    def is_alive(self) -> bool: ...
