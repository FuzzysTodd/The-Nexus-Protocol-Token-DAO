from _typeshed import Incomplete

logger: Incomplete

def make_command_file(path_to_debug_info, prefix_code: str = '', no_import: bool = False, skip_interpreter: bool = False): ...

usage: str

def main(path_to_debug_info: Incomplete | None = None, gdb_argv: Incomplete | None = None, no_import: bool = False) -> None:
    """
    Start the Cython debugger. This tells gdb to import the Cython and Python
    extensions (libcython.py and libpython.py) and it enables gdb's pending
    breakpoints.

    path_to_debug_info is the path to the Cython build directory
    gdb_argv is the list of options to gdb
    no_import tells cygdb whether it should import debug information
    """
