from _typeshed import Incomplete

def set_font_settings_for_testing() -> None: ...
def set_reproducibility_for_testing() -> None: ...
def setup() -> None: ...
def subprocess_run_helper(func, *args, timeout, extra_env: Incomplete | None = None):
    """
    Run a function in a sub-process.

    Parameters
    ----------
    func : function
        The function to be run.  It must be in a module that is importable.
    *args : str
        Any additional command line arguments to be passed in
        the first argument to ``subprocess.run``.
    extra_env : dict[str, str]
        Any additional environment variables to be set for the subprocess.
    """
