from _typeshed import Incomplete
from collections.abc import Generator
from pkg_resources import Environment
from setuptools import Command
from setuptools.package_index import PackageIndex
from setuptools.warnings import SetuptoolsDeprecationWarning

__all__ = ['easy_install', 'PthDistributions', 'extract_wininst_cfg', 'get_exe_prefixes']

class easy_install(Command):
    """Manage a download/build/install process"""
    description: str
    command_consumes_arguments: bool
    user_options: Incomplete
    boolean_options: Incomplete
    negative_opt: Incomplete
    create_index = PackageIndex
    user: int
    zip_ok: Incomplete
    install_dir: Incomplete
    index_url: Incomplete
    find_links: Incomplete
    build_directory: Incomplete
    args: Incomplete
    optimize: Incomplete
    upgrade: Incomplete
    editable: Incomplete
    root: Incomplete
    version: Incomplete
    install_purelib: Incomplete
    install_platlib: Incomplete
    install_headers: Incomplete
    install_lib: Incomplete
    install_scripts: Incomplete
    install_data: Incomplete
    install_base: Incomplete
    install_platbase: Incomplete
    install_userbase: Incomplete
    install_usersite: Incomplete
    no_find_links: Incomplete
    package_index: Incomplete
    pth_file: Incomplete
    site_dirs: Incomplete
    installed_projects: Incomplete
    verbose: Incomplete
    def initialize_options(self) -> None: ...
    def delete_blockers(self, blockers) -> None: ...
    config_vars: Incomplete
    script_dir: Incomplete
    all_site_dirs: Incomplete
    shadow_path: Incomplete
    local_index: Incomplete
    outputs: Incomplete
    def finalize_options(self) -> None: ...
    def expand_basedirs(self) -> None:
        """Calls `os.path.expanduser` on install_base, install_platbase and
        root."""
    def expand_dirs(self) -> None:
        """Calls `os.path.expanduser` on install dirs."""
    def run(self, show_deprecation: bool = True) -> None: ...
    def pseudo_tempname(self):
        """Return a pseudo-tempname base in the install directory.
        This code is intentionally naive; if a malicious party can write to
        the target directory you're already in deep doodoo.
        """
    def warn_deprecated_options(self) -> None: ...
    def check_site_dir(self) -> None:
        """Verify that self.install_dir is .pth-capable dir, if needed"""
    def cant_write_to_target(self) -> None: ...
    def check_pth_processing(self):
        """Empirically verify whether .pth files are supported in inst. dir"""
    def install_egg_scripts(self, dist) -> None:
        """Write all the scripts for `dist`, unless scripts are excluded"""
    def add_output(self, path) -> None: ...
    def not_editable(self, spec) -> None: ...
    def check_editable(self, spec) -> None: ...
    def easy_install(self, spec, deps: bool = False): ...
    def install_item(self, spec, download, tmpdir, deps, install_needed: bool = False): ...
    def select_scheme(self, name) -> None: ...
    def process_distribution(self, requirement, dist, deps: bool = True, *info) -> None: ...
    def should_unzip(self, dist): ...
    def maybe_move(self, spec, dist_filename, setup_base): ...
    def install_wrapper_scripts(self, dist) -> None: ...
    def install_script(self, dist, script_name, script_text, dev_path: Incomplete | None = None) -> None:
        """Generate a legacy script wrapper and install it"""
    def write_script(self, script_name, contents, mode: str = 't', blockers=()) -> None:
        """Write an executable file to the scripts directory"""
    def install_eggs(self, spec, dist_filename, tmpdir): ...
    def egg_distribution(self, egg_path): ...
    def install_egg(self, egg_path, tmpdir): ...
    def install_exe(self, dist_filename, tmpdir): ...
    def exe_to_egg(self, dist_filename, egg_tmp):
        """Extract a bdist_wininst to the directories an egg would use"""
    def install_wheel(self, wheel_path, tmpdir): ...
    def installation_report(self, req, dist, what: str = 'Installed'):
        """Helpful installation message for display to package users"""
    def report_editable(self, spec, setup_script): ...
    def run_setup(self, setup_script, setup_base, args) -> None: ...
    def build_and_install(self, setup_script, setup_base): ...
    def update_pth(self, dist) -> None: ...
    def unpack_progress(self, src, dst): ...
    def unpack_and_compile(self, egg_path, destination): ...
    def byte_compile(self, to_compile) -> None: ...
    def create_home_path(self) -> None:
        """Create directories under ~."""
    INSTALL_SCHEMES: Incomplete
    DEFAULT_SCHEME: Incomplete

def extract_wininst_cfg(dist_filename):
    """Extract configuration data from a bdist_wininst .exe

    Returns a configparser.RawConfigParser, or None
    """
def get_exe_prefixes(exe_filename):
    """Get exe->egg path translations for a given .exe file"""

class PthDistributions(Environment):
    """A .pth file with Distribution paths in it"""
    filename: Incomplete
    sitedirs: Incomplete
    basedir: Incomplete
    def __init__(self, filename, sitedirs=()) -> None: ...
    dirty: bool
    def save(self) -> None:
        """Write changed .pth file back to disk"""
    def add(self, dist) -> None:
        """Add `dist` to the distribution map"""
    def remove(self, dist) -> None:
        """Remove `dist` from the distribution map"""
    def make_relative(self, path): ...

class RewritePthDistributions(PthDistributions):
    prelude: Incomplete
    postlude: Incomplete
PthDistributions = RewritePthDistributions

class CommandSpec(list):
    """
    A command spec for a #! header, specified as a list of arguments akin to
    those passed to Popen.
    """
    options: Incomplete
    split_args: Incomplete
    @classmethod
    def best(cls):
        """
        Choose the best CommandSpec class based on environmental conditions.
        """
    @classmethod
    def from_param(cls, param):
        """
        Construct a CommandSpec from a parameter to build_scripts, which may
        be None.
        """
    @classmethod
    def from_environment(cls): ...
    @classmethod
    def from_string(cls, string):
        """
        Construct a command spec from a simple string representing a command
        line parseable by shlex.split.
        """
    def install_options(self, script_text) -> None: ...
    def as_header(self): ...

class WindowsCommandSpec(CommandSpec):
    split_args: Incomplete

class ScriptWriter:
    """
    Encapsulates behavior around writing entry point scripts for console and
    gui apps.
    """
    template: Incomplete
    command_spec_class = CommandSpec
    @classmethod
    def get_args(cls, dist, header: Incomplete | None = None) -> Generator[Incomplete, None, None]:
        """
        Yield write_script() argument tuples for a distribution's
        console_scripts and gui_scripts entry points.
        """
    @classmethod
    def best(cls):
        """
        Select the best ScriptWriter for this environment.
        """
    @classmethod
    def get_header(cls, script_text: str = '', executable: Incomplete | None = None):
        """Create a #! line, getting options (if any) from script_text"""

class WindowsScriptWriter(ScriptWriter):
    command_spec_class = WindowsCommandSpec
    @classmethod
    def best(cls):
        """
        Select the best ScriptWriter suitable for Windows
        """

class WindowsExecutableLauncherWriter(WindowsScriptWriter): ...
class EasyInstallDeprecationWarning(SetuptoolsDeprecationWarning): ...
