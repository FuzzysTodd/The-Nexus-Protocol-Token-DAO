from _typeshed import Incomplete

def try_compile(compiler, code: Incomplete | None = None, flags=[], ext: Incomplete | None = None):
    """Returns True if the compiler is able to compile the given code"""
def has_flag(compiler, flag, ext: Incomplete | None = None):
    """Returns True if the compiler supports the given flag"""
def get_cxx_std_flag(compiler):
    """Detects compiler flag for c++14, c++11, or None if not detected"""
def get_c_std_flag(compiler):
    """Detects compiler flag to enable C99"""
def try_add_flag(args, compiler, flag, ext: Incomplete | None = None) -> None:
    """Appends flag to the list of arguments if supported by the compiler"""
def set_c_flags_hook(build_ext, ext) -> None:
    """Sets basic compiler flags for compiling C99 code"""
def set_cxx_flags_hook(build_ext, ext) -> None:
    """Sets basic compiler flags for compiling C++11 code"""
def set_cxx_flags_clib_hook(build_clib, build_info) -> None: ...
