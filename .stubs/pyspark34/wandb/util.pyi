import importlib
import json
import queue
import random
import types
from _typeshed import Incomplete
from datetime import timedelta
from types import ModuleType
from typing import Any, Callable, Dict, Generator, IO, Iterable, List, Mapping, Sequence, TextIO, Tuple, TypeVar
from wandb.errors import AuthenticationError as AuthenticationError, CommError as CommError, UsageError as UsageError, term as term
from wandb.sdk.artifacts.artifact import Artifact as Artifact
from wandb.sdk.lib import filesystem as filesystem, runid as runid
from wandb.sdk.lib.json_util import dump as dump, dumps as dumps
from wandb.sdk.lib.paths import FilePathStr as FilePathStr, StrPath as StrPath

CheckRetryFnType = Callable[[Exception], bool | timedelta]
T = TypeVar('T')
logger: Incomplete
MAX_LINE_BYTES: Incomplete
IS_GIT: Incomplete
RE_WINFNAMES: Incomplete
DOCKER_IMAGE_NAME_SEPARATOR: str
RE_DOCKER_IMAGE_NAME_SEPARATOR_START: Incomplete
RE_DOCKER_IMAGE_NAME_SEPARATOR_END: Incomplete
RE_DOCKER_IMAGE_NAME_SEPARATOR_REPEAT: Incomplete
RE_DOCKER_IMAGE_NAME_CHARS: Incomplete
SENTRY_ENV: str
PLATFORM_WINDOWS: str
PLATFORM_LINUX: str
PLATFORM_BSD: str
PLATFORM_DARWIN: str
PLATFORM_UNKNOWN: str
LAUNCH_JOB_ARTIFACT_SLOT_NAME: str

def get_platform_name() -> str: ...

POW_10_BYTES: Incomplete
POW_2_BYTES: Incomplete

def vendor_setup() -> Callable:
    """Create a function that restores user paths after vendor imports.

    This enables us to use the vendor directory for packages we don't depend on. Call
    the returned function after imports are complete. If you don't you may modify the
    user's path which is never good.

    Usage:

    ```python
    reset_path = vendor_setup()
    # do any vendor imports...
    reset_path()
    ```
    """
def vendor_import(name: str) -> Any: ...

class LazyModuleState:
    module: Incomplete
    load_started: bool
    lock: Incomplete
    def __init__(self, module: types.ModuleType) -> None: ...
    def load(self) -> None: ...

class LazyModule(types.ModuleType):
    def __getattribute__(self, name: str) -> Any: ...
    def __setattr__(self, name: str, value: Any) -> None: ...
    def __delattr__(self, name: str) -> None: ...

def import_module_lazy(name: str) -> types.ModuleType:
    """Import a module lazily, only when it is used.

    Inspired by importlib.util.LazyLoader, but improved so that the module loading is
    thread-safe. Circular dependency between modules can lead to a deadlock if the two
    modules are loaded from different threads.

    :param (str) name: Dot-separated module path. E.g., 'scipy.stats'.
    """
def get_module(name: str, required: str | bool | None = None, lazy: bool = True) -> Any:
    """Return module or None. Absolute import is required.

    :param (str) name: Dot-separated module path. E.g., 'scipy.stats'.
    :param (str) required: A string to raise a ValueError if missing
    :param (bool) lazy: If True, return a lazy loader for the module.
    :return: (module|None) If import succeeds, the module will be returned.
    """
def get_optional_module(name) -> importlib.ModuleInterface | None: ...

np: Incomplete
pd_available: bool
pandas_spec: Incomplete
VALUE_BYTES_LIMIT: int

def app_url(api_url: str) -> str:
    """Return the frontend app url without a trailing slash."""
def get_full_typename(o: Any) -> Any:
    """Determine types based on type names.

    Avoids needing to to import (and therefore depend on) PyTorch, TensorFlow, etc.
    """
def get_h5_typename(o: Any) -> Any: ...
def is_uri(string: str) -> bool: ...
def local_file_uri_to_path(uri: str) -> str:
    """Convert URI to local filesystem path.

    No-op if the uri does not have the expected scheme.
    """
def get_local_path_or_none(path_or_uri: str) -> str | None:
    """Return path if local, None otherwise.

    Return None if the argument is a local path (not a scheme or file:///). Otherwise
    return `path_or_uri`.
    """
def make_tarfile(output_filename: str, source_dir: str, archive_name: str, custom_filter: Callable | None = None) -> None: ...
def is_tf_tensor(obj: Any) -> bool: ...
def is_tf_tensor_typename(typename: str) -> bool: ...
def is_tf_eager_tensor_typename(typename: str) -> bool: ...
def is_pytorch_tensor(obj: Any) -> bool: ...
def is_pytorch_tensor_typename(typename: str) -> bool: ...
def is_jax_tensor_typename(typename: str) -> bool: ...
def get_jax_tensor(obj: Any) -> Any | None: ...
def is_fastai_tensor_typename(typename: str) -> bool: ...
def is_pandas_data_frame_typename(typename: str) -> bool: ...
def is_matplotlib_typename(typename: str) -> bool: ...
def is_plotly_typename(typename: str) -> bool: ...
def is_plotly_figure_typename(typename: str) -> bool: ...
def is_numpy_array(obj: Any) -> bool: ...
def is_pandas_data_frame(obj: Any) -> bool: ...
def ensure_matplotlib_figure(obj: Any) -> Any:
    """Extract the current figure from a matplotlib object.

    Return the object itself if it's a figure.
    Raises ValueError if the object can't be converted.
    """
def matplotlib_to_plotly(obj: Any) -> Any: ...
def matplotlib_contains_images(obj: Any) -> bool: ...
def json_friendly(obj: Any) -> Tuple[Any, bool] | Tuple[None | str | float, bool]:
    """Convert an object into something that's more becoming of JSON."""
def json_friendly_val(val: Any) -> Any:
    """Make any value (including dict, slice, sequence, dataclass) JSON friendly."""
def alias_is_version_index(alias: str) -> bool: ...
def convert_plots(obj: Any) -> Any: ...
def maybe_compress_history(obj: Any) -> Tuple[Any, bool]: ...
def maybe_compress_summary(obj: Any, h5_typename: str) -> Tuple[Any, bool]: ...
def launch_browser(attempt_launch_browser: bool = True) -> bool:
    """Decide if we should launch a browser."""
def generate_id(length: int = 8) -> str: ...
def parse_tfjob_config() -> Any:
    """Attempt to parse TFJob config, returning False if it can't find it."""

class WandBJSONEncoder(json.JSONEncoder):
    """A JSON Encoder that handles some extra types."""
    def default(self, obj: Any) -> Any: ...

class WandBJSONEncoderOld(json.JSONEncoder):
    """A JSON Encoder that handles some extra types."""
    def default(self, obj: Any) -> Any: ...

class WandBHistoryJSONEncoder(json.JSONEncoder):
    """A JSON Encoder that handles some extra types.

    This encoder turns numpy like objects with a size > 32 into histograms.
    """
    def default(self, obj: Any) -> Any: ...

class JSONEncoderUncompressed(json.JSONEncoder):
    """A JSON Encoder that handles some extra types.

    This encoder turns numpy like objects with a size > 32 into histograms.
    """
    def default(self, obj: Any) -> Any: ...

def json_dump_safer(obj: Any, fp: IO[str], **kwargs: Any) -> None:
    """Convert obj to json, with some extra encodable types."""
def json_dumps_safer(obj: Any, **kwargs: Any) -> str:
    """Convert obj to json, with some extra encodable types."""
def json_dump_uncompressed(obj: Any, fp: IO[str], **kwargs: Any) -> None:
    """Convert obj to json, with some extra encodable types."""
def json_dumps_safer_history(obj: Any, **kwargs: Any) -> str:
    """Convert obj to json, with some extra encodable types, including histograms."""
def make_json_if_not_number(v: int | float | str | Mapping | Sequence) -> int | float | str:
    """If v is not a basic type convert it to json."""
def make_safe_for_json(obj: Any) -> Any:
    """Replace invalid json floats with strings. Also converts to lists and dicts."""
def no_retry_4xx(e: Exception) -> bool: ...
def no_retry_auth(e: Any) -> bool: ...
def check_retry_conflict(e: Any) -> bool | None:
    """Check if the exception is a conflict type so it can be retried.

    Returns:
        True - Should retry this operation
        False - Should not retry this operation
        None - No decision, let someone else decide
    """
def check_retry_conflict_or_gone(e: Any) -> bool | None:
    """Check if the exception is a conflict or gone type, so it can be retried or not.

    Returns:
        True - Should retry this operation
        False - Should not retry this operation
        None - No decision, let someone else decide
    """
def make_check_retry_fn(fallback_retry_fn: CheckRetryFnType, check_fn: Callable[[Exception], bool | None], check_timedelta: timedelta | None = None) -> CheckRetryFnType:
    """Return a check_retry_fn which can be used by lib.Retry().

    Arguments:
        fallback_fn: Use this function if check_fn didn't decide if a retry should happen.
        check_fn: Function which returns bool if retry should happen or None if unsure.
        check_timedelta: Optional retry timeout if we check_fn matches the exception
    """
def find_runner(program: str) -> None | list | List[str]:
    """Return a command that will run program.

    Arguments:
        program: The string name of the program to try to run.

    Returns:
        commandline list of strings to run the program (eg. with subprocess.call()) or None
    """
def downsample(values: Sequence, target_length: int) -> list:
    """Downsample 1d values to target_length, including start and end.

    Algorithm just rounds index down.

    Values can be any sequence, including a generator.
    """
def has_num(dictionary: Mapping, key: Any) -> bool: ...
def get_log_file_path() -> str:
    """Log file path used in error messages.

    It would probably be better if this pointed to a log file in a
    run directory.
    """
def docker_image_regex(image: str) -> Any:
    """Regex match for valid docker image names."""
def image_from_docker_args(args: List[str]) -> str | None:
    """Scan docker run args and attempt to find the most likely docker image argument.

    It excludes any arguments that start with a dash, and the argument after it if it
    isn't a boolean switch. This can be improved, we currently fallback gracefully when
    this fails.
    """
def load_yaml(file: Any) -> Any: ...
def image_id_from_k8s() -> str | None:
    """Ping the k8s metadata service for the image id.

    Specify the KUBERNETES_NAMESPACE environment variable if your pods are not in the
    default namespace:

    - name: KUBERNETES_NAMESPACE valueFrom:
        fieldRef:
          fieldPath: metadata.namespace
    """
def async_call(target: Callable, timeout: int | float | None = None) -> Callable:
    """Wrap a method to run in the background with an optional timeout.

    Returns a new method that will call the original with any args, waiting for upto
    timeout seconds. This new method blocks on the original and returns the result or
    None if timeout was reached, along with the thread. You can check thread.is_alive()
    to determine if a timeout was reached. If an exception is thrown in the thread, we
    reraise it.
    """
def read_many_from_queue(q: queue.Queue, max_items: int, queue_timeout: int | float) -> list: ...
def stopwatch_now() -> float:
    """Get a time value for interval comparisons.

    When possible it is a monotonic clock to prevent backwards time issues.
    """
def class_colors(class_count: int) -> List[List[int]]: ...
def prompt_choices(choices: Sequence[str], input_timeout: int | float | None = None, jupyter: bool = False) -> str:
    """Allow a user to choose from a list of options."""
def guess_data_type(shape: Sequence[int], risky: bool = False) -> str | None:
    """Infer the type of data based on the shape of the tensors.

    Arguments:
        shape (Sequence[int]): The shape of the data
        risky(bool): some guesses are more likely to be wrong.
    """
def download_file_from_url(dest_path: str, source_url: str, api_key: str | None = None) -> None: ...
def download_file_into_memory(source_url: str, api_key: str | None = None) -> bytes: ...
def isatty(ob: IO) -> bool: ...
def to_human_size(size: int, units: List[Tuple[str, Any]] | None = None) -> str: ...
def from_human_size(size: str, units: List[Tuple[str, Any]] | None = None) -> int: ...
def auto_project_name(program: str | None) -> str: ...
def to_forward_slash_path(path: str) -> str: ...
def to_native_slash_path(path: str) -> FilePathStr: ...
def check_and_warn_old(files: List[str]) -> bool: ...

class ImportMetaHook:
    modules: Incomplete
    on_import: Incomplete
    def __init__(self) -> None: ...
    def add(self, fullname: str, on_import: Callable) -> None: ...
    def install(self) -> None: ...
    def uninstall(self) -> None: ...
    def find_module(self, fullname: str, path: str | None = None) -> ImportMetaHook | None: ...
    def load_module(self, fullname: str) -> ModuleType: ...
    def get_modules(self) -> Tuple[str, ...]: ...
    def get_module(self, module: str) -> ModuleType: ...

def add_import_hook(fullname: str, on_import: Callable) -> None: ...
def host_from_path(path: str | None) -> str:
    """Return the host of the path."""
def uri_from_path(path: str | None) -> str:
    """Return the URI of the path."""
def is_unicode_safe(stream: TextIO) -> bool:
    """Return True if the stream supports UTF-8."""
def rand_alphanumeric(length: int = 8, rand: ModuleType | random.Random | None = None) -> str: ...
def fsync_open(path: StrPath, mode: str = 'w', encoding: str | None = None) -> Generator[IO[Any], None, None]:
    """Open a path for I/O and guarantee that the file is flushed and synced."""
def check_windows_valid_filename(path: int | str) -> bool: ...
def artifact_to_json(artifact: Artifact) -> Dict[str, Any]: ...
def check_dict_contains_nested_artifact(d: dict, nested: bool = False) -> bool: ...
def load_json_yaml_dict(config: str) -> Any: ...
def parse_artifact_string(v: str) -> Tuple[str, str | None, bool]: ...
def ensure_text(string: str | bytes, encoding: str = 'utf-8', errors: str = 'strict') -> str:
    """Coerce s to str."""
def make_artifact_name_safe(name: str) -> str:
    """Make an artifact name safe for use in artifacts."""
def make_docker_image_name_safe(name: str) -> str:
    """Make a docker image name safe for use in artifacts."""
def merge_dicts(source: Dict[str, Any], destination: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively merge two dictionaries."""
def coalesce(*arg: Any) -> Any:
    """Return the first non-none value in the list of arguments.

    Similar to ?? in C#.
    """
def cast_dictlike_to_dict(d: Dict[str, Any]) -> Dict[str, Any]: ...
def remove_keys_with_none_values(d: Dict[str, Any] | Any) -> Dict[str, Any] | Any: ...
def batched(n: int, iterable: Iterable[T]) -> Generator[List[T], None, None]: ...
def random_string(length: int = 12) -> str:
    """Generate a random string of a given length.

    :param length: Length of the string to generate.
    :return: Random string.
    """
def sample_with_exponential_decay_weights(xs: Iterable | Iterable[Iterable], ys: Iterable[Iterable], keys: Iterable | None = None, sample_size: int = 1500) -> Tuple[List, List, List | None]:
    """Sample from a list of lists with weights that decay exponentially.

    May be used with the wandb.plot.line_series function.
    """
