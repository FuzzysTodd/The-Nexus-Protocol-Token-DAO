from _typeshed import Incomplete

PY_SOURCE: int
PY_COMPILED: int
C_EXTENSION: int
C_BUILTIN: int
PY_FROZEN: int

def find_spec(module, paths): ...
def find_module(module, paths: Incomplete | None = None):
    """Just like 'imp.find_module()', but with package support"""
def get_frozen_object(module, paths: Incomplete | None = None): ...
def get_module(module, paths, info): ...
