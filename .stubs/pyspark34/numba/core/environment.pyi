from numba import _dynfunc

class Environment(_dynfunc.Environment):
    """Stores globals and constant pyobjects for runtime.

    It is often needed to convert b/w nopython objects and pyobjects.
    """
    @classmethod
    def from_fndesc(cls, fndesc): ...
    def can_cache(self): ...
    def __reduce__(self): ...
    def __del__(self) -> None: ...

def lookup_environment(env_name):
    """Returns the Environment object for the given name;
    or None if not found
    """
