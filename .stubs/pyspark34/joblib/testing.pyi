from _typeshed import Incomplete

raises: Incomplete
warns: Incomplete
SkipTest: Incomplete
skipif: Incomplete
fixture: Incomplete
parametrize: Incomplete
timeout: Incomplete
xfail: Incomplete
param: Incomplete

def warnings_to_stdout() -> None:
    """ Redirect all warnings to stdout.
    """
def check_subprocess_call(cmd, timeout: int = 5, stdout_regex: Incomplete | None = None, stderr_regex: Incomplete | None = None) -> None:
    """Runs a command in a subprocess with timeout in seconds.

    A SIGTERM is sent after `timeout` and if it does not terminate, a
    SIGKILL is sent after `2 * timeout`.

    Also checks returncode is zero, stdout if stdout_regex is set, and
    stderr if stderr_regex is set.
    """
