from _typeshed import Incomplete
from collections.abc import Generator
from setuptools import Command
from setuptools.command.install import install as InstallCommandBase
from setuptools.dist import Distribution

project_name: str
project_name_idx: Incomplete
collaborator_build: bool

def standard_or_nightly(standard, nightly): ...

REQUIRED_PACKAGES: Incomplete
FAKE_REQUIRED_PACKAGES: Incomplete
DOCLINES: Incomplete
project_name_no_gpu: Incomplete
CONSOLE_SCRIPTS: Incomplete

class BinaryDistribution(Distribution):
    def has_ext_modules(self): ...

class InstallCommand(InstallCommandBase):
    """Override the dir where the headers go."""
    install_headers: Incomplete
    install_lib: Incomplete
    def finalize_options(self): ...

class InstallHeaders(Command):
    """Override how headers are copied.

  The install_headers that comes with setuptools copies all files to
  the same directory. But we need the files to be in a specific directory
  hierarchy for -I <include_dir> to work correctly.
  """
    description: str
    user_options: Incomplete
    boolean_options: Incomplete
    install_dir: Incomplete
    force: int
    outfiles: Incomplete
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def mkdir_and_copy_file(self, header): ...
    def run(self) -> None: ...
    def get_inputs(self): ...
    def get_outputs(self): ...

def find_files(pattern, root) -> Generator[Incomplete, None, None]:
    """Return all the files matching pattern below root dir."""

so_lib_paths: Incomplete
matches: Incomplete
EXTENSION_NAME: str
headers: Incomplete
