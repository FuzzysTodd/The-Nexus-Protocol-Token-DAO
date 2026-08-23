from _typeshed import Incomplete
from collections.abc import Generator
from jedi.cache import memoize_method as memoize_method, time_cache as time_cache
from jedi.inference.compiled.subprocess import CompiledSubprocess as CompiledSubprocess, InferenceStateSameProcess as InferenceStateSameProcess, InferenceStateSubprocess as InferenceStateSubprocess
from typing import NamedTuple

class _VersionInfo(NamedTuple):
    major: Incomplete
    minor: Incomplete
    micro: Incomplete

class InvalidPythonEnvironment(Exception):
    """
    If you see this exception, the Python executable or Virtualenv you have
    been trying to use is probably not a correct Python version.
    """

class _BaseEnvironment:
    def get_grammar(self): ...

class Environment(_BaseEnvironment):
    """
    This class is supposed to be created by internal Jedi architecture. You
    should not create it directly. Please use create_environment or the other
    functions instead. It is then returned by that function.
    """
    def __init__(self, executable, env_vars: Incomplete | None = None) -> None: ...
    def get_inference_state_subprocess(self, inference_state): ...
    def get_sys_path(self):
        """
        The sys path for this environment. Does not include potential
        modifications from e.g. appending to :data:`sys.path`.

        :returns: list of str
        """

class _SameEnvironmentMixin:
    path: Incomplete
    version_info: Incomplete
    def __init__(self) -> None: ...

class SameEnvironment(_SameEnvironmentMixin, Environment): ...

class InterpreterEnvironment(_SameEnvironmentMixin, _BaseEnvironment):
    def get_inference_state_subprocess(self, inference_state): ...
    def get_sys_path(self): ...

def get_default_environment():
    """
    Tries to return an active Virtualenv or conda environment.
    If there is no VIRTUAL_ENV variable or no CONDA_PREFIX variable set
    set it will return the latest Python version installed on the system. This
    makes it possible to use as many new Python features as possible when using
    autocompletion and other functionality.

    :returns: :class:`.Environment`
    """
def get_cached_default_environment(): ...
def find_virtualenvs(paths: Incomplete | None = None, *, safe: bool = True, use_environment_vars: bool = True) -> Generator[Incomplete, None, None]:
    """
    :param paths: A list of paths in your file system to be scanned for
        Virtualenvs. It will search in these paths and potentially execute the
        Python binaries.
    :param safe: Default True. In case this is False, it will allow this
        function to execute potential `python` environments. An attacker might
        be able to drop an executable in a path this function is searching by
        default. If the executable has not been installed by root, it will not
        be executed.
    :param use_environment_vars: Default True. If True, the VIRTUAL_ENV
        variable will be checked if it contains a valid VirtualEnv.
        CONDA_PREFIX will be checked to see if it contains a valid conda
        environment.

    :yields: :class:`.Environment`
    """
def find_system_environments(*, env_vars: Incomplete | None = None) -> Generator[Incomplete, None, None]:
    """
    Ignores virtualenvs and returns the Python versions that were installed on
    your system. This might return nothing, if you're running Python e.g. from
    a portable version.

    The environments are sorted from latest to oldest Python version.

    :yields: :class:`.Environment`
    """
def get_system_environment(version, *, env_vars: Incomplete | None = None):
    """
    Return the first Python environment found for a string of the form 'X.Y'
    where X and Y are the major and minor versions of Python.

    :raises: :exc:`.InvalidPythonEnvironment`
    :returns: :class:`.Environment`
    """
def create_environment(path, *, safe: bool = True, env_vars: Incomplete | None = None):
    """
    Make it possible to manually create an Environment object by specifying a
    Virtualenv path or an executable path and optional environment variables.

    :raises: :exc:`.InvalidPythonEnvironment`
    :returns: :class:`.Environment`
    """
