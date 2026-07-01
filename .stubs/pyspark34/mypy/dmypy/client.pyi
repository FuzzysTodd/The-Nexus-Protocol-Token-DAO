import argparse
from _typeshed import Incomplete
from mypy.dmypy_os import alive as alive, kill as kill
from mypy.dmypy_util import DEFAULT_STATUS_FILE as DEFAULT_STATUS_FILE, receive as receive
from mypy.ipc import IPCClient as IPCClient, IPCException as IPCException
from mypy.util import check_python_version as check_python_version, get_terminal_width as get_terminal_width, should_force_color as should_force_color
from mypy.version import __version__ as __version__
from typing import Any, Callable, Mapping, NoReturn

class AugmentedHelpFormatter(argparse.RawDescriptionHelpFormatter):
    def __init__(self, prog: str) -> None: ...

parser: Incomplete
subparsers: Incomplete
start_parser: Incomplete
p: Incomplete
restart_parser: Incomplete
status_parser: Incomplete
stop_parser: Incomplete
kill_parser: Incomplete
check_parser: Incomplete
run_parser: Incomplete
recheck_parser: Incomplete
suggest_parser: Incomplete
inspect_parser: Incomplete
hang_parser: Incomplete
daemon_parser: Incomplete
help_parser: Incomplete

class BadStatus(Exception):
    """Exception raised when there is something wrong with the status file.

    For example:
    - No status file found
    - Status file malformed
    - Process whose pid is in the status file does not exist
    """

def main(argv: list[str]) -> None:
    """The code is top-down."""
def fail(msg: str) -> NoReturn: ...
ActionFunction = Callable[[argparse.Namespace], None]

def action(subparser: argparse.ArgumentParser) -> Callable[[ActionFunction], ActionFunction]:
    """Decorator to tie an action function to a subparser."""
def do_start(args: argparse.Namespace) -> None:
    """Start daemon (it must not already be running).

    This is where mypy flags are set from the command line.

    Setting flags is a bit awkward; you have to use e.g.:

      dmypy start -- --strict

    since we don't want to duplicate mypy's huge list of flags.
    """
def do_restart(args: argparse.Namespace) -> None:
    """Restart daemon (it may or may not be running; but not hanging).

    We first try to stop it politely if it's running.  This also sets
    mypy flags from the command line (see do_start()).
    """
def restart_server(args: argparse.Namespace, allow_sources: bool = False) -> None:
    """Restart daemon (it may or may not be running; but not hanging)."""
def start_server(args: argparse.Namespace, allow_sources: bool = False) -> None:
    """Start the server from command arguments and wait for it."""
def wait_for_server(status_file: str, timeout: float = 5.0) -> None:
    """Wait until the server is up.

    Exit if it doesn't happen within the timeout.
    """
def do_run(args: argparse.Namespace) -> None:
    """Do a check, starting (or restarting) the daemon as necessary

    Restarts the daemon if the running daemon reports that it is
    required (due to a configuration change, for example).

    Setting flags is a bit awkward; you have to use e.g.:

      dmypy run -- --strict a.py b.py ...

    since we don't want to duplicate mypy's huge list of flags.
    (The -- is only necessary if flags are specified.)
    """
def do_status(args: argparse.Namespace) -> None:
    """Print daemon status.

    This verifies that it is responsive to requests.
    """
def do_stop(args: argparse.Namespace) -> None:
    """Stop daemon via a 'stop' request."""
def do_kill(args: argparse.Namespace) -> None:
    """Kill daemon process with SIGKILL."""
def do_check(args: argparse.Namespace) -> None:
    """Ask the daemon to check a list of files."""
def do_recheck(args: argparse.Namespace) -> None:
    """Ask the daemon to recheck the previous list of files, with optional modifications.

    If at least one of --remove or --update is given, the server will
    update the list of files to check accordingly and assume that any other files
    are unchanged.  If none of these flags are given, the server will call stat()
    on each file last checked to determine its status.

    Files given in --update ought to exist.  Files given in --remove need not exist;
    if they don't they will be ignored.
    The lists may be empty but oughtn't contain duplicates or overlap.

    NOTE: The list of files is lost when the daemon is restarted.
    """
def do_suggest(args: argparse.Namespace) -> None:
    """Ask the daemon for a suggested signature.

    This just prints whatever the daemon reports as output.
    For now it may be closer to a list of call sites.
    """
def do_inspect(args: argparse.Namespace) -> None:
    """Ask daemon to print the type of an expression."""
def check_output(response: dict[str, Any], verbose: bool, junit_xml: str | None, perf_stats_file: str | None) -> None:
    """Print the output from a check or recheck command.

    Call sys.exit() unless the status code is zero.
    """
def show_stats(response: Mapping[str, object]) -> None: ...
def do_hang(args: argparse.Namespace) -> None:
    """Hang for 100 seconds, as a debug hack."""
def do_daemon(args: argparse.Namespace) -> None:
    """Serve requests in the foreground."""
def do_help(args: argparse.Namespace) -> None:
    """Print full help (same as dmypy --help)."""
def request(status_file: str, command: str, *, timeout: int | None = None, **kwds: object) -> dict[str, Any]:
    """Send a request to the daemon.

    Return the JSON dict with the response.

    Raise BadStatus if there is something wrong with the status file
    or if the process whose pid is in the status file has died.

    Return {'error': <message>} if an IPC operation or receive()
    raised OSError.  This covers cases such as connection refused or
    closed prematurely as well as invalid JSON received.
    """
def get_status(status_file: str) -> tuple[int, str]:
    """Read status file and check if the process is alive.

    Return (pid, connection_name) on success.

    Raise BadStatus if something's wrong.
    """
def check_status(data: dict[str, Any]) -> tuple[int, str]:
    """Check if the process is alive.

    Return (pid, connection_name) on success.

    Raise BadStatus if something's wrong.
    """
def read_status(status_file: str) -> dict[str, object]:
    """Read status file.

    Raise BadStatus if the status file doesn't exist or contains
    invalid JSON or the JSON is not a dict.
    """
def is_running(status_file: str) -> bool:
    """Check if the server is running cleanly"""
def console_entry() -> None: ...
