from .._path import ensure_directory as ensure_directory
from _typeshed import Incomplete
from collections.abc import Generator
from setuptools import Command as Command
from setuptools.extension import Library as Library

def strip_module(filename): ...
def sorted_walk(dir) -> Generator[Incomplete, None, None]:
    """Do os.walk in a reproducible way,
    independent of indeterministic filesystem readdir order
    """
def write_stub(resource, pyfile) -> None: ...

class bdist_egg(Command):
    description: str
    user_options: Incomplete
    boolean_options: Incomplete
    bdist_dir: Incomplete
    plat_name: Incomplete
    keep_temp: int
    dist_dir: Incomplete
    skip_build: int
    egg_output: Incomplete
    exclude_source_files: Incomplete
    def initialize_options(self) -> None: ...
    egg_info: Incomplete
    def finalize_options(self) -> None: ...
    def do_install_data(self) -> None: ...
    def get_outputs(self): ...
    def call_command(self, cmdname, **kw):
        """Invoke reinitialized command `cmdname` with keyword args"""
    stubs: Incomplete
    def run(self) -> None: ...
    def zap_pyfiles(self) -> None: ...
    def zip_safe(self): ...
    def gen_header(self): ...
    def copy_metadata_to(self, target_dir) -> None:
        """Copy metadata (egg info) to the target_dir"""
    def get_ext_outputs(self):
        """Get a list of relative paths to C extensions in the output distro"""

NATIVE_EXTENSIONS: Incomplete

def walk_egg(egg_dir) -> Generator[Incomplete, None, None]:
    """Walk an unpacked egg's contents, skipping the metadata directory"""
def analyze_egg(egg_dir, stubs): ...
def write_safety_flag(egg_dir, safe) -> None: ...

safety_flags: Incomplete

def scan_module(egg_dir, base, name, stubs):
    """Check whether module possibly uses unsafe-for-zipfile stuff"""
def iter_symbols(code) -> Generator[Incomplete, None, None]:
    """Yield names and strings used by `code` and its nested code objects"""
def can_scan(): ...

INSTALL_DIRECTORY_ATTRS: Incomplete

def make_zipfile(zip_filename, base_dir, verbose: int = 0, dry_run: int = 0, compress: bool = True, mode: str = 'w'):
    '''Create a zip file from all the files under \'base_dir\'.  The output
    zip file will be named \'base_dir\' + ".zip".  Uses either the "zipfile"
    Python module (if available) or the InfoZIP "zip" utility (if installed
    and found on the default search path).  If neither tool is available,
    raises DistutilsExecError.  Returns the name of the output zip file.
    '''
