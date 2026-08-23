from _typeshed import Incomplete
from distutils.command import build_ext as _build_ext

__revision__: str
basestring = str
extension_name_re: Incomplete
show_compilers = _build_ext.show_compilers

class Optimization:
    flags: Incomplete
    state: Incomplete
    config_vars: Incomplete
    def __init__(self) -> None: ...
    def disable_optimization(self) -> None:
        """disable optimization for the C or C++ compiler"""
    def restore_state(self) -> None:
        """restore the original state"""

optimization: Incomplete

class old_build_ext(_build_ext.build_ext):
    description: str
    sep_by: Incomplete
    user_options: Incomplete
    boolean_options: Incomplete
    help_options: Incomplete
    cython_cplus: int
    cython_create_listing: int
    cython_line_directives: int
    cython_include_dirs: Incomplete
    cython_directives: Incomplete
    cython_c_in_temp: int
    cython_gen_pxi: int
    cython_gdb: bool
    no_c_in_traceback: int
    cython_compile_time_env: Incomplete
    def initialize_options(self) -> None: ...
    def __getattr__(self, name): ...
    def __setattr__(self, name, value): ...
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...
    def check_extensions_list(self, extensions) -> None: ...
    def cython_sources(self, sources, extension):
        """
        Walk the list of source files in 'sources', looking for Cython
        source files (.pyx and .py).  Run Cython on all that are
        found, and return a modified 'sources' list with Cython source
        files replaced by the generated C (or C++) files.
        """
