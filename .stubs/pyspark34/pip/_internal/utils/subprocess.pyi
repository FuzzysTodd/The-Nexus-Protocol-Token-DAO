from pip._internal.cli.spinners import SpinnerInterface as SpinnerInterface, open_spinner as open_spinner
from pip._internal.exceptions import InstallationSubprocessError as InstallationSubprocessError
from pip._internal.utils.logging import VERBOSE as VERBOSE, subprocess_logger as subprocess_logger
from pip._internal.utils.misc import HiddenText as HiddenText
from pip._vendor.rich.markup import escape as escape
from typing import Any, Callable, Iterable, List, Literal, Mapping

CommandArgs = List[str | HiddenText]

def make_command(*args: str | HiddenText | CommandArgs) -> CommandArgs:
    """
    Create a CommandArgs object.
    """
def format_command_args(args: List[str] | CommandArgs) -> str:
    """
    Format command arguments for display.
    """
def reveal_command_args(args: List[str] | CommandArgs) -> List[str]:
    """
    Return the arguments in their raw, unredacted form.
    """
def call_subprocess(cmd: List[str] | CommandArgs, show_stdout: bool = False, cwd: str | None = None, on_returncode: Literal['raise', 'warn', 'ignore'] = 'raise', extra_ok_returncodes: Iterable[int] | None = None, extra_environ: Mapping[str, Any] | None = None, unset_environ: Iterable[str] | None = None, spinner: SpinnerInterface | None = None, log_failed_cmd: bool | None = True, stdout_only: bool | None = False, *, command_desc: str) -> str:
    """
    Args:
      show_stdout: if true, use INFO to log the subprocess's stderr and
        stdout streams.  Otherwise, use DEBUG.  Defaults to False.
      extra_ok_returncodes: an iterable of integer return codes that are
        acceptable, in addition to 0. Defaults to None, which means [].
      unset_environ: an iterable of environment variable names to unset
        prior to calling subprocess.Popen().
      log_failed_cmd: if false, failed commands are not logged, only raised.
      stdout_only: if true, return only stdout, else return both. When true,
        logging of both stdout and stderr occurs when the subprocess has
        terminated, else logging occurs as subprocess output is produced.
    """
def runner_with_spinner_message(message: str) -> Callable[..., None]:
    """Provide a subprocess_runner that shows a spinner message.

    Intended for use with for BuildBackendHookCaller. Thus, the runner has
    an API that matches what's expected by BuildBackendHookCaller.subprocess_runner.
    """
