from _typeshed import Incomplete

class Logger:
    """A Logfile class with different policies for file creation"""
    home_dir: Incomplete
    logfname: Incomplete
    loghead: Incomplete
    logmode: Incomplete
    logfile: Incomplete
    log_raw_input: bool
    log_output: bool
    timestamp: bool
    log_active: bool
    def __init__(self, home_dir, logfname: str = 'Logger.log', loghead: str = '', logmode: str = 'over') -> None: ...
    def logstart(self, logfname: Incomplete | None = None, loghead: Incomplete | None = None, logmode: Incomplete | None = None, log_output: bool = False, timestamp: bool = False, log_raw_input: bool = False) -> None:
        """Generate a new log-file with a default header.

        Raises RuntimeError if the log has already been started"""
    log_active_out: Incomplete
    def switch_log(self, val) -> None:
        """Switch logging on/off. val should be ONLY a boolean."""
    def logstate(self) -> None:
        """Print a status message about the logger."""
    def log(self, line_mod, line_ori) -> None:
        """Write the sources to a log.

        Inputs:

        - line_mod: possibly modified input, such as the transformations made
          by input prefilters or input handlers of various kinds. This should
          always be valid Python.

        - line_ori: unmodified input line from the user. This is not
          necessarily valid Python.
        """
    def log_write(self, data, kind: str = 'input') -> None:
        """Write data to the log file, if active"""
    def logstop(self) -> None:
        """Fully stop logging and close log file.

        In order to start logging again, a new logstart() call needs to be
        made, possibly (though not necessarily) with a new filename, mode and
        other options."""
    close_log = logstop
