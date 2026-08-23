import enum
from .lib import apikey as apikey
from .lib.gitlib import GitRepo as GitRepo
from .lib.runid import generate_id as generate_id
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import Any, Callable, Dict, ItemsView, Iterable, Sequence, Tuple
from wandb import util as util
from wandb.apis.internal import Api as Api
from wandb.errors import UsageError as UsageError
from wandb.proto import wandb_settings_pb2 as wandb_settings_pb2
from wandb.sdk.internal.system.env_probe_helpers import is_aws_lambda as is_aws_lambda
from wandb.sdk.lib import filesystem as filesystem
from wandb.sdk.lib._settings_toposort_generated import SETTINGS_TOPOLOGICALLY_SORTED as SETTINGS_TOPOLOGICALLY_SORTED

class SettingsPreprocessingError(UsageError):
    """Raised when the value supplied to a wandb.Settings() setting does not pass preprocessing."""
class SettingsValidationError(UsageError):
    """Raised when the value supplied to a wandb.Settings() setting does not pass validation."""
class SettingsUnexpectedArgsError(UsageError):
    """Raised when unexpected arguments are passed to wandb.Settings()."""

def is_instance_recursive(obj: Any, type_hint: Any) -> bool: ...

class Source(enum.IntEnum):
    OVERRIDE: int
    BASE: int
    ORG: int
    ENTITY: int
    PROJECT: int
    USER: int
    SYSTEM: int
    WORKSPACE: int
    ENV: int
    SETUP: int
    LOGIN: int
    INIT: int
    SETTINGS: int
    ARGS: int
    RUN: int

ConsoleValue: Incomplete

@dataclass()
class SettingsData:
    """Settings for the W&B SDK."""
    allow_val_change: bool
    anonymous: str
    api_key: str
    azure_account_url_to_access_key: Dict[str, str]
    base_url: str
    code_dir: str
    colab_url: str
    config_paths: Sequence[str]
    console: str
    deployment: str
    disable_code: bool
    disable_git: bool
    disable_hints: bool
    disable_job_creation: bool
    disabled: bool
    docker: str
    email: str
    entity: str
    files_dir: str
    force: bool
    git_commit: str
    git_remote: str
    git_remote_url: str
    git_root: str
    heartbeat_seconds: int
    host: str
    ignore_globs: Tuple[str]
    init_timeout: float
    is_local: bool
    job_name: str
    job_source: str
    label_disable: bool
    launch: bool
    launch_config_path: str
    log_dir: str
    log_internal: str
    log_symlink_internal: str
    log_symlink_user: str
    log_user: str
    login_timeout: float
    mode: str
    notebook_name: str
    problem: str
    program: str
    program_abspath: str
    program_relpath: str
    project: str
    project_url: str
    quiet: bool
    reinit: bool
    relogin: bool
    resume: str | bool
    resume_fname: str
    resumed: bool
    root_dir: str
    run_group: str
    run_id: str
    run_job_type: str
    run_mode: str
    run_name: str
    run_notes: str
    run_tags: Tuple[str]
    run_url: str
    sagemaker_disable: bool
    save_code: bool
    settings_system: str
    settings_workspace: str
    show_colors: bool
    show_emoji: bool
    show_errors: bool
    show_info: bool
    show_warnings: bool
    silent: bool
    start_method: str
    strict: bool
    summary_errors: int
    summary_timeout: int
    summary_warnings: int
    sweep_id: str
    sweep_param_path: str
    sweep_url: str
    symlink: bool
    sync_dir: str
    sync_file: str
    sync_symlink_latest: str
    system_sample: int
    system_sample_seconds: int
    table_raise_on_max_row_limit_exceeded: bool
    timespec: str
    tmp_dir: str
    username: str
    wandb_dir: str
    def __init__(self, _args, _aws_lambda, _async_upload_concurrency_limit, _cli_only_mode, _colab, _cuda, _disable_meta, _disable_service, _disable_setproctitle, _disable_stats, _disable_viewer, _disable_machine_info, _except_exit, _executable, _extra_http_headers, _file_stream_retry_max, _file_stream_retry_wait_min_seconds, _file_stream_retry_wait_max_seconds, _file_stream_timeout_seconds, _file_uploader_retry_max, _file_uploader_retry_wait_min_seconds, _file_uploader_retry_wait_max_seconds, _file_uploader_timeout_seconds, _flow_control_custom, _flow_control_disabled, _graphql_retry_max, _graphql_retry_wait_min_seconds, _graphql_retry_wait_max_seconds, _graphql_timeout_seconds, _internal_check_process, _internal_queue_timeout, _ipython, _jupyter, _jupyter_name, _jupyter_path, _jupyter_root, _kaggle, _live_policy_rate_limit, _live_policy_wait_time, _log_level, _network_buffer, _noop, _notebook, _offline, _sync, _os, _platform, _proxies, _python, _runqueue_item_id, _require_nexus, _save_requirements, _service_transport, _service_wait, _start_datetime, _start_time, _stats_pid, _stats_sample_rate_seconds, _stats_samples_to_average, _stats_join_assets, _stats_neuron_monitor_config_path, _stats_open_metrics_endpoints, _stats_open_metrics_filters, _stats_disk_paths, _stats_buffer_size, _tmp_code_dir, _tracelog, _unsaved_keys, _windows, allow_val_change, anonymous, api_key, azure_account_url_to_access_key, base_url, code_dir, colab_url, config_paths, console, deployment, disable_code, disable_git, disable_hints, disable_job_creation, disabled, docker, email, entity, files_dir, force, git_commit, git_remote, git_remote_url, git_root, heartbeat_seconds, host, ignore_globs, init_timeout, is_local, job_name, job_source, label_disable, launch, launch_config_path, log_dir, log_internal, log_symlink_internal, log_symlink_user, log_user, login_timeout, mode, notebook_name, problem, program, program_abspath, program_relpath, project, project_url, quiet, reinit, relogin, resume, resume_fname, resumed, root_dir, run_group, run_id, run_job_type, run_mode, run_name, run_notes, run_tags, run_url, sagemaker_disable, save_code, settings_system, settings_workspace, show_colors, show_emoji, show_errors, show_info, show_warnings, silent, start_method, strict, summary_errors, summary_timeout, summary_warnings, sweep_id, sweep_param_path, sweep_url, symlink, sync_dir, sync_file, sync_symlink_latest, system_sample, system_sample_seconds, table_raise_on_max_row_limit_exceeded, timespec, tmp_dir, username, wandb_dir) -> None: ...

class Property:
    """A class to represent attributes (individual settings) of the Settings object.

    - Encapsulates the logic of how to preprocess and validate values of settings
    throughout the lifetime of a class instance.
    - Allows for runtime modification of settings with hooks, e.g. in the case when
    a setting depends on another setting.
    - The update() method is used to update the value of a setting.
    - The `is_policy` attribute determines the source priority when updating the property value.
    E.g. if `is_policy` is True, the smallest `Source` value takes precedence.
    """
    name: Incomplete
    def __init__(self, name: str, value: Any | None = None, preprocessor: Callable | Sequence[Callable] | None = None, validator: Callable | Sequence[Callable] | None = None, hook: Callable | Sequence[Callable] | None = None, auto_hook: bool = False, is_policy: bool = False, frozen: bool = False, source: int = ..., **kwargs: Any) -> None: ...
    @property
    def value(self) -> Any:
        """Apply the runtime modifier(s) (if any) and return the value."""
    @property
    def is_policy(self) -> bool: ...
    @property
    def source(self) -> int: ...
    def update(self, value: Any, source: int = ...) -> None:
        """Update the value of the property."""
    def __setattr__(self, key: str, value: Any) -> None: ...

class Settings(SettingsData):
    """A class to represent modifiable settings."""
    def __init__(self, **kwargs: Any) -> None: ...
    def __copy__(self) -> Settings:
        """Ensure that a copy of the settings object is a truly deep copy.

        Note that the copied object will not be frozen  todo? why is this needed?
        """
    def __deepcopy__(self, memo: dict) -> Settings: ...
    def __getattribute__(self, name):
        """Expose `attribute.value` if `attribute` is a Property."""
    def __setattr__(self, key: str, value: Any) -> None: ...
    def __iter__(self) -> Iterable: ...
    def copy(self) -> Settings: ...
    def keys(self) -> Iterable[str]: ...
    def __getitem__(self, name):
        """Expose attribute.value if attribute is a Property."""
    def update(self, settings: Dict[str, Any] | Settings | None = None, source: int = ..., **kwargs: Any) -> None:
        """Update individual settings."""
    def items(self) -> ItemsView[str, Any]: ...
    def get(self, key: str, default: Any | None = None) -> Any: ...
    def freeze(self) -> None: ...
    def unfreeze(self) -> None: ...
    def is_frozen(self) -> bool: ...
    def to_dict(self) -> Dict[str, Any]:
        """Return a dict representation of the settings."""
    def to_proto(self) -> wandb_settings_pb2.Settings:
        """Generate a protobuf representation of the settings."""
