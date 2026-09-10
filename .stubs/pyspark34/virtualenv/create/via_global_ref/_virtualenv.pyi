from _typeshed import Incomplete

VIRTUALENV_PATCH_FILE: Incomplete

def patch_dist(dist):
    """
    Distutils allows user to configure some arguments via a configuration file:
    https://docs.python.org/3/install/index.html#distutils-configuration-files.

    Some of this arguments though don't make sense in context of the virtual environment files, let's fix them up.
    """

class _Finder:
    """A meta path finder that allows patching the imported distutils modules."""
    fullname: Incomplete
    lock: Incomplete
    def find_spec(self, fullname, path, target: Incomplete | None = None): ...
    @staticmethod
    def exec_module(old, module) -> None: ...
    @staticmethod
    def load_module(old, name): ...
