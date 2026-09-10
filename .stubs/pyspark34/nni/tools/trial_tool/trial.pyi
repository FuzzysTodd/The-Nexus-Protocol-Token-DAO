from .commands import CommandType as CommandType
from .log_utils import LogType as LogType, RemoteLogger as RemoteLogger, StdOutputType as StdOutputType, nni_log as nni_log
from _typeshed import Incomplete

trial_output_path_name: str

class Trial:
    process: Incomplete
    data: Incomplete
    args: Incomplete
    command_channel: Incomplete
    trial_syslogger_stdout: Incomplete
    id: Incomplete
    node_id: Incomplete
    name: Incomplete
    def __init__(self, args, data) -> None: ...
    trial_output_dir: Incomplete
    working_dir: Incomplete
    log_pipe_stdout: Incomplete
    def run(self) -> None: ...
    def save_parameter_file(self, command_data) -> None: ...
    def is_running(self): ...
    def kill(self, trial_id: Incomplete | None = None) -> None: ...
    def cleanup(self) -> None: ...
