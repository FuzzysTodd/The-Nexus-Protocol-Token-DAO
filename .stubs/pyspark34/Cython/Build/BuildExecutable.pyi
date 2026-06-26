from _typeshed import Incomplete

DEBUG: bool

def get_config_var(name, default: str = ''): ...

INCDIR: Incomplete
LIBDIR1: Incomplete
LIBDIR2: Incomplete
PYLIB: Incomplete
PYLIB_DYN: Incomplete
CC: Incomplete
CFLAGS: Incomplete
LINKCC: Incomplete
LINKFORSHARED: Incomplete
LIBS: Incomplete
SYSLIBS: Incomplete
EXE_EXT: Incomplete

def dump_config() -> None: ...
def runcmd(cmd, shell: bool = True) -> None: ...
def clink(basename) -> None: ...
def ccompile(basename) -> None: ...
def cycompile(input_file, options=()) -> None: ...
def exec_file(program_name, args=()) -> None: ...
def build(input_file, compiler_args=(), force: bool = False):
    """
    Build an executable program from a Cython module.

    Returns the name of the executable file.
    """
def build_and_run(args) -> None:
    """
    Build an executable program from a Cython module and run it.

    Arguments after the module name will be passed verbatimly to the program.
    """
