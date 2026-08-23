import subprocess
import threading
import unittest
from _typeshed import Incomplete
from gevent._compat import perf_counter as perf_counter
from gevent._config import validate_bool as validate_bool
from gevent.monkey import get_original as get_original

BUFFER_OUTPUT: bool
QUIET: Incomplete

class Popen(subprocess.Popen):
    """
    Depending on when we're imported and if the process has been monkey-patched,
    this could use cooperative or native Popen.
    """
    timer: Incomplete
    def __enter__(self): ...
    def __exit__(self, *args) -> None: ...

def log(message, *args, **kwargs) -> None:
    """
    Log a *message*

    :keyword str color: One of the values from _colorscheme
    """
def debug(message, *args, **kwargs) -> None:
    """
    Log the *message* only if we're not in quiet mode.
    """
def killpg(pid): ...
def kill_processtree(pid) -> None: ...
def kill(popen) -> None: ...

IGNORED_GEVENT_ENV_KEYS: Incomplete
IGNORED_GEVENT_ENV_ITEMS: Incomplete

def getname(command, env: Incomplete | None = None, setenv: Incomplete | None = None): ...
def start(command, quiet: bool = False, **kwargs): ...

class RunResult:
    """
    The results of running an external command.

    If the command was successful, this has a boolean
    value of True; otherwise, a boolean value of false.

    The integer value of this object is the command's exit code.

    """
    command: Incomplete
    run_kwargs: Incomplete
    code: Incomplete
    output: Incomplete
    error: Incomplete
    name: Incomplete
    run_count: Incomplete
    skipped_count: Incomplete
    run_duration: Incomplete
    def __init__(self, command, run_kwargs, code, output: str = None, error: str = None, name: Incomplete | None = None, run_count: int = 0, skipped_count: int = 0, run_duration: float = 0) -> None: ...
    @property
    def output_lines(self): ...
    def __bool__(self) -> bool: ...
    __nonzero__ = __bool__
    def __int__(self) -> int: ...

output_lock: Incomplete

def run(command, **kwargs):
    """
    Execute *command*, returning a `RunResult`.

    This blocks until *command* finishes or until it times out.
    """

class NoSetupPyFound(Exception):
    """Raised by find_setup_py_above"""

def find_setup_py_above(a_file):
    """Return the directory containing setup.py somewhere above *a_file*"""
def search_for_setup_py(a_file: Incomplete | None = None, a_module_name: Incomplete | None = None, a_class: Incomplete | None = None, climb_cwd: bool = True): ...
def find_stdlib_tests():
    """
    Return a sequence of directories that could contain
    stdlib tests for the running version of Python.

    The most specific tests are at the end of the sequence.

    No checks are performed on existence of the directories.
    """
def absolute_pythonpath():
    """
    Return the PYTHONPATH environment variable (if set) with each
    entry being an absolute path. If not set, returns None.
    """

class ExampleMixin:
    """
    Something that uses the ``examples/`` directory
    from the root of the gevent distribution.

    The `cwd` property is set to the root of the gevent distribution.
    """
    example_args: Incomplete
    before_delay: int
    after_delay: float
    example: Incomplete
    start_kwargs: Incomplete
    def find_setup_py(self):
        """Return the directory containing setup.py"""
    @property
    def cwd(self): ...
    @property
    def setenv(self):
        """
        Returns a dictionary of environment variables to set for the
        child in addition to (or replacing) the ones already in the
        environment.

        Since the child is run in `cwd`, relative paths in ``PYTHONPATH``
        need to be converted to absolute paths.
        """
    def start_example(self): ...
    def run_example(self): ...

class TestServer(ExampleMixin, unittest.TestCase):
    popen: Incomplete
    def running_server(self): ...
    def test(self) -> None: ...
    def before(self) -> None: ...
    def after(self) -> None: ...

class alarm(threading.Thread):
    daemon: bool
    timeout: Incomplete
    def __init__(self, timeout) -> None: ...
    def run(self) -> None: ...
