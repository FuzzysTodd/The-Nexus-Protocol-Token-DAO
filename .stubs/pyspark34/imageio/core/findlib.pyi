from _typeshed import Incomplete

LOCALDIR: Incomplete
SYSTEM_LIBS_ONLY: bool

def looks_lib(fname):
    """Returns True if the given filename looks like a dynamic library.
    Based on extension, but cross-platform and more flexible.
    """
def generate_candidate_libs(lib_names, lib_dirs: Incomplete | None = None):
    """Generate a list of candidate filenames of what might be the dynamic
    library corresponding with the given list of names.
    Returns (lib_dirs, lib_paths)
    """
def load_lib(exact_lib_names, lib_names, lib_dirs: Incomplete | None = None):
    """load_lib(exact_lib_names, lib_names, lib_dirs=None)

    Load a dynamic library.

    This function first tries to load the library from the given exact
    names. When that fails, it tries to find the library in common
    locations. It searches for files that start with one of the names
    given in lib_names (case insensitive). The search is performed in
    the given lib_dirs and a set of common library dirs.

    Returns ``(ctypes_library, library_path)``
    """
