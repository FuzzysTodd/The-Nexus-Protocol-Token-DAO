from _typeshed import Incomplete
from distutils.errors import CCompilerError as CCompilerError, DistutilsError as DistutilsError

HAS_CYTHON: bool
DEBUG: int

def pyx_to_dll(filename, ext: Incomplete | None = None, force_rebuild: int = 0, build_in_temp: bool = False, pyxbuild_dir: Incomplete | None = None, setup_args: Incomplete | None = None, reload_support: bool = False, inplace: bool = False):
    """Compile a PYX file to a DLL and return the name of the generated .so
       or .dll ."""
