from ..core import Command as Command
from ..errors import DistutilsSetupError as DistutilsSetupError
from ..sysconfig import customize_compiler as customize_compiler
from _typeshed import Incomplete

def show_compilers() -> None: ...

class build_clib(Command):
    description: str
    user_options: Incomplete
    boolean_options: Incomplete
    help_options: Incomplete
    build_clib: Incomplete
    build_temp: Incomplete
    libraries: Incomplete
    include_dirs: Incomplete
    define: Incomplete
    undef: Incomplete
    debug: Incomplete
    force: int
    compiler: Incomplete
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...
    def check_library_list(self, libraries) -> None:
        """Ensure that the list of libraries is valid.

        `library` is presumably provided as a command option 'libraries'.
        This method checks that it is a list of 2-tuples, where the tuples
        are (library_name, build_info_dict).

        Raise DistutilsSetupError if the structure is invalid anywhere;
        just returns otherwise.
        """
    def get_library_names(self): ...
    def get_source_files(self): ...
    def build_libraries(self, libraries) -> None: ...
