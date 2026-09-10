import asyncio
import queue
from typing import Callable, Dict, NamedTuple, Sequence, Tuple
from wandb.sdk.internal.internal_api import Api as Api, CreateArtifactFileSpecInput as CreateArtifactFileSpecInput, CreateArtifactFilesResponseFile as CreateArtifactFilesResponseFile

class RequestPrepare(NamedTuple):
    file_spec: CreateArtifactFileSpecInput
    response_channel: queue.Queue[ResponsePrepare] | Tuple['asyncio.AbstractEventLoop', 'asyncio.Future[ResponsePrepare]']

class RequestFinish(NamedTuple): ...

class ResponsePrepare(NamedTuple):
    birth_artifact_id: str
    upload_url: str | None
    upload_headers: Sequence[str]
    upload_id: str | None
    storage_path: str | None
    multipart_upload_urls: Dict[int, str] | None
Request = RequestPrepare | RequestFinish

def gather_batch(request_queue: queue.Queue[Request], batch_time: float, inter_event_time: float, max_batch_size: int, clock: Callable[[], float] = ...) -> Tuple[bool, Sequence[RequestPrepare]]: ...
def prepare_response(response: CreateArtifactFilesResponseFile) -> ResponsePrepare: ...

class StepPrepare:
    """A thread that batches requests to our file prepare API.

    Any number of threads may call prepare_async() in parallel. The PrepareBatcher thread
    will batch requests up and send them all to the backend at once.
    """
    def __init__(self, api: Api, batch_time: float, inter_event_time: float, max_batch_size: int, request_queue: queue.Queue[Request] | None = None) -> None: ...
    def prepare_async(self, file_spec: CreateArtifactFileSpecInput) -> asyncio.Future[ResponsePrepare]:
        """Request the backend to prepare a file for upload."""
    def prepare_sync(self, file_spec: CreateArtifactFileSpecInput) -> queue.Queue[ResponsePrepare]: ...
    def start(self) -> None: ...
    def finish(self) -> None: ...
    def is_alive(self) -> bool: ...
    def shutdown(self) -> None: ...
