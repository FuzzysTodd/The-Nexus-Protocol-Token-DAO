import sentry_sdk
import sentry_sdk.tracing
import threading
import time
from _typeshed import Incomplete
from sentry_sdk._compat import PY311 as PY311, PY33 as PY33
from sentry_sdk._lru_cache import LRUCache as LRUCache
from sentry_sdk._types import ProfilerMode as ProfilerMode, SamplingContext as SamplingContext, TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.utils import capture_internal_exception as capture_internal_exception, filename_for_module as filename_for_module, is_valid_sample_rate as is_valid_sample_rate, logger as logger, nanosecond_time as nanosecond_time, set_in_app_in_frames as set_in_app_in_frames
from types import FrameType
from typing import Any, Callable, Dict, List, Sequence, Tuple
from typing_extensions import TypedDict

ThreadId = str

class ProcessedSample(TypedDict):
    elapsed_since_start_ns: str
    thread_id: ThreadId
    stack_id: int
ProcessedStack = List[int]

class ProcessedFrame(TypedDict):
    abs_path: str
    filename: str | None
    function: str
    lineno: int
    module: str | None

class ProcessedThreadMetadata(TypedDict):
    name: str

class ProcessedProfile(TypedDict):
    frames: List[ProcessedFrame]
    stacks: List[ProcessedStack]
    samples: List[ProcessedSample]
    thread_metadata: Dict[ThreadId, ProcessedThreadMetadata]

class ProfileContext(TypedDict):
    profile_id: str
FrameId = Tuple[str, int, str]
FrameIds = Tuple[FrameId, ...]
StackId = Tuple[int, int]
ExtractedStack = Tuple[StackId, FrameIds, List[ProcessedFrame]]
ExtractedSample = Sequence[Tuple[ThreadId, ExtractedStack]]
thread_sleep: Incomplete
thread_sleep = time.sleep

def is_gevent() -> bool: ...

DEFAULT_SAMPLING_FREQUENCY: int
PROFILE_MINIMUM_SAMPLES: int

def has_profiling_enabled(options: Dict[str, Any]) -> bool: ...
def setup_profiler(options: Dict[str, Any]) -> bool: ...
def teardown_profiler() -> None: ...

MAX_STACK_DEPTH: int

def extract_stack(raw_frame: FrameType | None, cache: LRUCache, cwd: str, max_stack_depth: int = ...) -> ExtractedStack:
    """
    Extracts the stack starting the specified frame. The extracted stack
    assumes the specified frame is the top of the stack, and works back
    to the bottom of the stack.

    In the event that the stack is more than `MAX_STACK_DEPTH` frames deep,
    only the first `MAX_STACK_DEPTH` frames will be returned.
    """
def frame_id(raw_frame: FrameType) -> FrameId: ...
def extract_frame(fid: FrameId, raw_frame: FrameType, cwd: str) -> ProcessedFrame: ...
def get_frame_name(frame: FrameType) -> str: ...

MAX_PROFILE_DURATION_NS: Incomplete

def get_current_thread_id(thread: threading.Thread | None = None) -> int | None:
    """
    Try to get the id of the current thread, with various fall backs.
    """

class Profile:
    scheduler: Incomplete
    hub: Incomplete
    event_id: Incomplete
    sampled: Incomplete
    active_thread_id: Incomplete
    start_ns: Incomplete
    stop_ns: int
    active: bool
    indexed_frames: Incomplete
    indexed_stacks: Incomplete
    frames: Incomplete
    stacks: Incomplete
    samples: Incomplete
    unique_samples: int
    def __init__(self, transaction: sentry_sdk.tracing.Transaction, hub: sentry_sdk.Hub | None = None, scheduler: Scheduler | None = None) -> None: ...
    def update_active_thread_id(self) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def __enter__(self) -> Profile: ...
    def __exit__(self, ty: Any | None, value: Any | None, tb: Any | None) -> None: ...
    def write(self, ts: int, sample: ExtractedSample) -> None: ...
    def process(self) -> ProcessedProfile: ...
    def to_json(self, event_opt: Dict[str, Any], options: Dict[str, Any]) -> Dict[str, Any]: ...
    def valid(self) -> bool: ...

class Scheduler:
    mode: ProfilerMode
    interval: Incomplete
    sampler: Incomplete
    new_profiles: Incomplete
    active_profiles: Incomplete
    def __init__(self, frequency: int) -> None: ...
    def __enter__(self) -> Scheduler: ...
    def __exit__(self, ty: Any | None, value: Any | None, tb: Any | None) -> None: ...
    def setup(self) -> None: ...
    def teardown(self) -> None: ...
    def ensure_running(self) -> None: ...
    def start_profiling(self, profile: Profile) -> None: ...
    def stop_profiling(self, profile: Profile) -> None: ...
    def make_sampler(self) -> Callable[..., None]: ...

class ThreadScheduler(Scheduler):
    """
    This scheduler is based on running a daemon thread that will call
    the sampler at a regular interval.
    """
    mode: ProfilerMode
    name: str
    running: bool
    thread: Incomplete
    pid: Incomplete
    lock: Incomplete
    def __init__(self, frequency: int) -> None: ...
    def setup(self) -> None: ...
    def teardown(self) -> None: ...
    def ensure_running(self) -> None: ...
    def run(self) -> None: ...

class GeventScheduler(Scheduler):
    """
    This scheduler is based on the thread scheduler but adapted to work with
    gevent. When using gevent, it may monkey patch the threading modules
    (`threading` and `_thread`). This results in the use of greenlets instead
    of native threads.

    This is an issue because the sampler CANNOT run in a greenlet because
    1. Other greenlets doing sync work will prevent the sampler from running
    2. The greenlet runs in the same thread as other greenlets so when taking
       a sample, other greenlets will have been evicted from the thread. This
       results in a sample containing only the sampler's code.
    """
    mode: ProfilerMode
    name: str
    running: bool
    thread: Incomplete
    pid: Incomplete
    lock: Incomplete
    def __init__(self, frequency: int) -> None: ...
    def setup(self) -> None: ...
    def teardown(self) -> None: ...
    def ensure_running(self) -> None: ...
    def run(self) -> None: ...
