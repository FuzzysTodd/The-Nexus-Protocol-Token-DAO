from ..core import Command as Command
from ..errors import DistutilsOptionError as DistutilsOptionError
from _typeshed import Incomplete

PYTHON_SOURCE_EXTENSION: str

class install_lib(Command):
    description: str
    user_options: Incomplete
    boolean_options: Incomplete
    negative_opt: Incomplete
    install_dir: Incomplete
    build_dir: Incomplete
    force: int
    compile: Incomplete
    optimize: Incomplete
    skip_build: Incomplete
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...
    def build(self) -> None: ...
    def install(self): ...
    def byte_compile(self, files) -> None: ...
    def get_outputs(self):
        '''Return the list of files that would be installed if this command
        were actually run.  Not affected by the "dry-run" flag or whether
        modules have actually been built yet.
        '''
    def get_inputs(self):
        """Get the list of files that are input to this command, ie. the
        files that get installed as they are named in the build tree.
        The files in this list correspond one-to-one to the output
        filenames returned by 'get_outputs()'.
        """
