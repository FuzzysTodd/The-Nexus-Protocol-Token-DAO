from _typeshed import Incomplete
from distutils.command.build_ext import build_ext as _build_ext

basestring = str

class build_ext(_build_ext):
    user_options: Incomplete
    boolean_options: Incomplete
    cython_cplus: int
    cython_create_listing: int
    cython_line_directives: int
    cython_include_dirs: Incomplete
    cython_directives: Incomplete
    cython_c_in_temp: int
    cython_gen_pxi: int
    cython_gdb: bool
    cython_compile_time_env: Incomplete
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def get_extension_attr(self, extension, option_name, default: bool = False): ...
    def build_extension(self, ext) -> None: ...
new_build_ext = build_ext
