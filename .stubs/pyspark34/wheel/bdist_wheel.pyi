from .macosx_libfile import calculate_macosx_platform_tag as calculate_macosx_platform_tag
from .metadata import pkginfo_to_metadata as pkginfo_to_metadata
from .util import log as log
from .vendored.packaging import tags as tags
from .wheelfile import WheelFile as WheelFile
from _typeshed import Incomplete
from setuptools import Command

def safe_name(name):
    """Convert an arbitrary string to a standard distribution name
    Any runs of non-alphanumeric/. characters are replaced with a single '-'.
    """
def safe_version(version):
    """
    Convert an arbitrary string to a standard version string
    """

setuptools_major_version: Incomplete
PY_LIMITED_API_PATTERN: str

def python_tag(): ...
def get_platform(archive_root):
    """Return our platform name 'win32', 'linux_x86_64'"""
def get_flag(var, fallback, expected: bool = True, warn: bool = True):
    """Use a fallback value for determining SOABI flags if the needed config
    var is unset or unavailable."""
def get_abi_tag():
    """Return the ABI tag based on SOABI (if available) or emulate SOABI (PyPy2)."""
def safer_name(name): ...
def safer_version(version): ...
def remove_readonly(func, path, excinfo) -> None: ...
def remove_readonly_exc(func, path, exc) -> None: ...

class bdist_wheel(Command):
    description: str
    supported_compressions: Incomplete
    user_options: Incomplete
    boolean_options: Incomplete
    bdist_dir: Incomplete
    data_dir: Incomplete
    plat_name: Incomplete
    plat_tag: Incomplete
    format: str
    keep_temp: bool
    dist_dir: Incomplete
    egginfo_dir: Incomplete
    root_is_pure: Incomplete
    skip_build: Incomplete
    relative: bool
    owner: Incomplete
    group: Incomplete
    universal: bool
    compression: str
    python_tag: Incomplete
    build_number: Incomplete
    py_limited_api: bool
    plat_name_supplied: bool
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    @property
    def wheel_dist_name(self):
        """Return distribution full name with - replaced with _"""
    def get_tag(self): ...
    install_libbase: Incomplete
    def run(self) -> None: ...
    def write_wheelfile(self, wheelfile_base, generator=...) -> None: ...
    @property
    def license_paths(self): ...
    def egg2dist(self, egginfo_path, distinfo_path):
        """Convert an .egg-info directory into a .dist-info directory"""
