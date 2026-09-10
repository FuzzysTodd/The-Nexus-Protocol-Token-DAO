import distutils.extension as _Extension
from _typeshed import Incomplete

__revision__: str

class Extension(_Extension.Extension):
    cython_include_dirs: Incomplete
    cython_directives: Incomplete
    cython_create_listing: Incomplete
    cython_line_directives: Incomplete
    cython_cplus: Incomplete
    cython_c_in_temp: Incomplete
    cython_gen_pxi: Incomplete
    cython_gdb: Incomplete
    no_c_in_traceback: Incomplete
    cython_compile_time_env: Incomplete
    def __init__(self, name, sources, include_dirs: Incomplete | None = None, define_macros: Incomplete | None = None, undef_macros: Incomplete | None = None, library_dirs: Incomplete | None = None, libraries: Incomplete | None = None, runtime_library_dirs: Incomplete | None = None, extra_objects: Incomplete | None = None, extra_compile_args: Incomplete | None = None, extra_link_args: Incomplete | None = None, export_symbols: Incomplete | None = None, depends: Incomplete | None = None, language: Incomplete | None = None, cython_include_dirs: Incomplete | None = None, cython_directives: Incomplete | None = None, cython_create_listing: bool = False, cython_line_directives: bool = False, cython_cplus: bool = False, cython_c_in_temp: bool = False, cython_gen_pxi: bool = False, cython_gdb: bool = False, no_c_in_traceback: bool = False, cython_compile_time_env: Incomplete | None = None, **kw) -> None: ...

read_setup_file: Incomplete
