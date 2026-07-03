from _typeshed import Incomplete
from typing import NamedTuple

class VersionInfo(NamedTuple):
    major: Incomplete
    minor: Incomplete
    micro: Incomplete
    releaselevel: Incomplete
    serial: Incomplete

EXTENSIONS: Incomplete

class PythonInfo:
    """Contains information for a Python interpreter."""
    platform: Incomplete
    implementation: Incomplete
    pypy_version_info: Incomplete
    version_info: Incomplete
    architecture: Incomplete
    version_nodot: Incomplete
    version: Incomplete
    os: Incomplete
    prefix: Incomplete
    base_prefix: Incomplete
    real_prefix: Incomplete
    base_exec_prefix: Incomplete
    exec_prefix: Incomplete
    executable: Incomplete
    original_executable: Incomplete
    system_executable: Incomplete
    has_venv: Incomplete
    path: Incomplete
    file_system_encoding: Incomplete
    stdout_encoding: Incomplete
    sysconfig_scheme: str
    sysconfig_paths: Incomplete
    distutils_install: Incomplete
    sysconfig: Incomplete
    sysconfig_vars: Incomplete
    system_stdlib: Incomplete
    system_stdlib_platform: Incomplete
    max_size: Incomplete
    def __init__(self) -> None: ...
    def install_path(self, key): ...
    @property
    def version_str(self): ...
    @property
    def version_release_str(self): ...
    @property
    def python_name(self): ...
    @property
    def is_old_virtualenv(self): ...
    @property
    def is_venv(self): ...
    def sysconfig_path(self, key, config_var: Incomplete | None = None, sep=...): ...
    def creators(self, refresh: bool = False): ...
    @property
    def system_include(self): ...
    @property
    def system_prefix(self): ...
    @property
    def system_exec_prefix(self): ...
    def __unicode__(self): ...
    @property
    def spec(self): ...
    @classmethod
    def clear_cache(cls, app_data) -> None: ...
    def satisfies(self, spec, impl_must_match):
        """Check if a given specification can be satisfied by the this python interpreter instance."""
    @classmethod
    def current(cls, app_data: Incomplete | None = None):
        """
        This locates the current host interpreter information. This might be different than what we run into in case
        the host python has been upgraded from underneath us.
        """
    @classmethod
    def current_system(cls, app_data: Incomplete | None = None):
        """
        This locates the current host interpreter information. This might be different than what we run into in case
        the host python has been upgraded from underneath us.
        """
    @classmethod
    def from_exe(cls, exe, app_data: Incomplete | None = None, raise_on_error: bool = True, ignore_cache: bool = False, resolve_to_host: bool = True, env: Incomplete | None = None):
        """Given a path to an executable get the python information."""
    def discover_exe(self, app_data, prefix, exact: bool = True, env: Incomplete | None = None): ...
