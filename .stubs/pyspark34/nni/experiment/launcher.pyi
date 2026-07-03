from . import rest as rest
from ..tools.nnictl.config_utils import Config as Config, Experiments as Experiments
from ..tools.nnictl.nnictl_utils import update_experiment as update_experiment
from .config import ExperimentConfig as ExperimentConfig
from .config.utils import load_experiment_config as load_experiment_config
from .experiment import RunMode as RunMode
from _typeshed import Incomplete
from dataclasses import dataclass
from subprocess import Popen
from typing_extensions import Literal

@dataclass(init=False)
class NniManagerArgs:
    port: int
    experiment_id: str
    action: Literal['create', 'resume', 'view']
    mode: str
    experiments_directory: str
    log_level: str
    foreground: bool = ...
    url_prefix: str | None = ...
    tuner_command_channel: str | None = ...
    python_interpreter: str
    def __init__(self, action: Literal['create', 'resume', 'view'], exp_id: str, config: ExperimentConfig, port: int, debug: bool, foreground: bool, url_prefix: str | None, tuner_command_channel: str | None) -> None: ...
    def to_command_line_args(self) -> list[str]: ...

def start_experiment(action: Literal['create', 'resume', 'view'], exp_id: str, config: ExperimentConfig, port: int, debug: bool, run_mode: RunMode, url_prefix: str | None, tuner_command_channel: str | None = None, tags: list[str] = []) -> Popen: ...
def get_stopped_experiment_config(exp_id, exp_dir: Incomplete | None = None): ...
def get_stopped_experiment_config_json(exp_id, exp_dir: Incomplete | None = None): ...
