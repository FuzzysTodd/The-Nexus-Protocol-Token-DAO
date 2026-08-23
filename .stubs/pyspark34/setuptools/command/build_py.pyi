import distutils.command.build_py as orig
from ..extern.more_itertools import unique_everseen as unique_everseen
from ..warnings import SetuptoolsDeprecationWarning as SetuptoolsDeprecationWarning
from _typeshed import Incomplete
from typing import Dict, List

def make_writable(target) -> None: ...

class build_py(orig.build_py):
    """Enhanced 'build_py' command that includes data files with packages

    The data files are specified via a 'package_data' argument to 'setup()'.
    See 'setuptools.dist.Distribution' for more details.

    Also, this version of the 'build_py' command allows you to specify both
    'py_modules' and 'packages' in the same setup operation.
    """
    editable_mode: bool
    existing_egg_info_dir: str | None
    package_data: Incomplete
    exclude_package_data: Incomplete
    def finalize_options(self) -> None: ...
    def copy_file(self, infile, outfile, preserve_mode: int = 1, preserve_times: int = 1, link: Incomplete | None = None, level: int = 1): ...
    def run(self) -> None:
        """Build modules, packages, and copy data files to build directory"""
    data_files: Incomplete
    def __getattr__(self, attr):
        """lazily compute data files"""
    def build_module(self, module, module_file, package): ...
    def get_data_files_without_manifest(self):
        """
        Generate list of ``(package,src_dir,build_dir,filenames)`` tuples,
        but without triggering any attempt to analyze or build the manifest.
        """
    def find_data_files(self, package, src_dir):
        """Return filenames for package's data files in 'src_dir'"""
    def get_outputs(self, include_bytecode: int = 1) -> List[str]:
        """See :class:`setuptools.commands.build.SubCommand`"""
    def get_output_mapping(self) -> Dict[str, str]:
        """See :class:`setuptools.commands.build.SubCommand`"""
    def build_package_data(self) -> None:
        """Copy data files into build directory"""
    manifest_files: Incomplete
    def analyze_manifest(self) -> None: ...
    def get_data_files(self) -> None: ...
    def check_package(self, package, package_dir):
        """Check namespace packages' __init__ for declare_namespace"""
    packages_checked: Incomplete
    def initialize_options(self) -> None: ...
    def get_package_dir(self, package): ...
    def exclude_data_files(self, package, src_dir, files):
        """Filter filenames for package's data files in 'src_dir'"""

def assert_relative(path): ...

class _IncludePackageDataAbuse:
    """Inform users that package or module is included as 'data file'"""
    class _Warning(SetuptoolsDeprecationWarning): ...
    def __init__(self) -> None: ...
    def is_module(self, file): ...
    def importable_subpackage(self, parent, file): ...
    def warn(self, importable) -> None: ...
