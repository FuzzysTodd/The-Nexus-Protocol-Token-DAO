import threading
from _typeshed import Incomplete
from dash.testing import wait as wait
from dash.testing.errors import DashAppLoadingError as DashAppLoadingError, NoAppFoundError as NoAppFoundError, ServerCloseError as ServerCloseError, TestingTimeoutError as TestingTimeoutError

logger: Incomplete

def import_app(app_file, application_name: str = 'app'):
    '''Import a dash application from a module. The import path is in dot
    notation to the module. The variable named app will be returned.

    :Example:

        >>> app = import_app("my_app.app")

    Will import the application in module `app` of the package `my_app`.

    :param app_file: Path to the app (dot-separated).
    :type app_file: str
    :param application_name: The name of the dash application instance.
    :raise: dash_tests.errors.NoAppFoundError
    :return: App from module.
    :rtype: dash.Dash
    '''

class BaseDashRunner:
    """Base context manager class for running applications."""
    port: int
    started: Incomplete
    keep_open: Incomplete
    stop_timeout: Incomplete
    def __init__(self, keep_open, stop_timeout) -> None: ...
    def start(self, *args, **kwargs) -> None: ...
    def stop(self) -> None: ...
    @staticmethod
    def accessible(url): ...
    def __call__(self, *args, **kwargs): ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, traceback: types.TracebackType | None) -> None: ...
    @property
    def url(self):
        """The default server url."""
    @property
    def is_windows(self): ...
    @property
    def tmp_app_path(self): ...

class KillerThread(threading.Thread):
    def __init__(self, **kwargs) -> None: ...
    def kill(self) -> None: ...

class ThreadedRunner(BaseDashRunner):
    """Runs a dash application in a thread.

    This is the default flavor to use in dash integration tests.
    """
    thread: Incomplete
    def __init__(self, keep_open: bool = False, stop_timeout: int = 3) -> None: ...
    def running_and_accessible(self, url): ...
    port: Incomplete
    started: Incomplete
    def start(self, app, start_timeout: int = 3, **kwargs):
        """Start the app server in threading flavor."""
    def stop(self) -> None: ...

class MultiProcessRunner(BaseDashRunner):
    proc: Incomplete
    def __init__(self, keep_open: bool = False, stop_timeout: int = 3) -> None: ...
    port: Incomplete
    started: bool
    def start(self, app, start_timeout: int = 3, **kwargs): ...
    def stop(self) -> None: ...

class ProcessRunner(BaseDashRunner):
    """Runs a dash application in a waitress-serve subprocess.

    This flavor is closer to production environment but slower.
    """
    proc: Incomplete
    def __init__(self, keep_open: bool = False, stop_timeout: int = 3) -> None: ...
    port: Incomplete
    started: bool
    def start(self, app_module: Incomplete | None = None, application_name: str = 'app', raw_command: Incomplete | None = None, port: int = 8050, start_timeout: int = 3):
        """Start the server with waitress-serve in process flavor."""
    def stop(self) -> None: ...

class RRunner(ProcessRunner):
    proc: Incomplete
    def __init__(self, keep_open: bool = False, stop_timeout: int = 3) -> None: ...
    started: bool
    def start(self, app, start_timeout: int = 2, cwd: Incomplete | None = None):
        """Start the server with subprocess and Rscript."""

class JuliaRunner(ProcessRunner):
    proc: Incomplete
    def __init__(self, keep_open: bool = False, stop_timeout: int = 3) -> None: ...
    started: bool
    def start(self, app, start_timeout: int = 30, cwd: Incomplete | None = None):
        """Start the server with subprocess and julia."""
