from imp import *
from _imp import acquire_lock as acquire_lock, release_lock as release_lock
from _typeshed import Incomplete

SEARCH_ERROR: int
PY_SOURCE: int
PY_COMPILED: int
C_EXTENSION: int
PY_RESOURCE: int
PKG_DIRECTORY: int
C_BUILTIN: int
PY_FROZEN: int
PY_CODERESOURCE: int
IMP_HOOK: int

def get_suffixes(): ...
def find_module(name, path: Incomplete | None = None): ...
def load_dynamic(name, path, file: Incomplete | None = None): ...
