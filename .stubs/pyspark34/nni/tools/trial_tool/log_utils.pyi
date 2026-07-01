import threading
from .commands import CommandType as CommandType
from .rest_utils import rest_post as rest_post
from .url_utils import gen_send_stdout_url as gen_send_stdout_url
from _typeshed import Incomplete
from enum import Enum
from logging import StreamHandler

class LogType(Enum):
    Trace: str
    Debug: str
    Info: str
    Warning: str
    Error: str
    Fatal: str

class StdOutputType(Enum):
    Stdout: Incomplete
    Stderr: str

def nni_log(log_type, log_message) -> None:
    """Log message into stdout"""

class NNIRestLogHanlder(StreamHandler):
    host: Incomplete
    port: Incomplete
    tag: Incomplete
    std_output_type: Incomplete
    trial_id: Incomplete
    channel: Incomplete
    orig_stdout: Incomplete
    orig_stderr: Incomplete
    def __init__(self, host, port, tag, trial_id, channel, std_output_type=...) -> None: ...
    def emit(self, record) -> None: ...

class RemoteLogger:
    """
    NNI remote logger
    """
    logger: Incomplete
    log_level: Incomplete
    pipeReader: Incomplete
    handler: Incomplete
    orig_stdout: Incomplete
    log_collection: Incomplete
    def __init__(self, syslog_host, syslog_port, tag, std_output_type, log_collection, trial_id: Incomplete | None = None, channel: Incomplete | None = None, log_level=...) -> None:
        """
        constructor
        """
    def get_pipelog_reader(self):
        """
        Get pipe for remote logger
        """
    def flush(self) -> None:
        """
        Add flush in handler
        """
    def write(self, buf) -> None:
        """
        Write buffer data into logger/stdout
        """
    def close(self) -> None:
        """
        Close handlers and resources
        """

class PipeLogReader(threading.Thread):
    """
    The reader thread reads log data from pipe
    """
    queue: Incomplete
    logger: Incomplete
    daemon: bool
    log_level: Incomplete
    pipeReader: Incomplete
    orig_stdout: Incomplete
    process_exit: bool
    log_collection: Incomplete
    log_pattern: Incomplete
    pip_log_reader_thread: Incomplete
    def __init__(self, logger, log_collection, log_level=...) -> None:
        """Setup the object with a logger and a loglevel
        and start the thread
        """
    def fileno(self):
        """Return the write file descriptor of the pipe
        """
    def run(self) -> None:
        """Run the thread, logging everything.
           If the log_collection is 'none', the log content will not be enqueued
        """
    def close(self) -> None:
        """Close the write end of the pipe.
        """
    @property
    def is_read_completed(self):
        """Return if read is completed
        """
    def set_process_exit(self): ...
