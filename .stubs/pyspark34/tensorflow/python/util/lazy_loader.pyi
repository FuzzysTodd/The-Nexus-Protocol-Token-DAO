import types
from _typeshed import Incomplete

class LazyLoader(types.ModuleType):
    """Lazily import a module, mainly to avoid pulling in large dependencies.

  `contrib`, and `ffmpeg` are examples of modules that are large and not always
  needed, and this allows them to only be loaded when they are used.
  """
    def __init__(self, local_name, parent_module_globals, name, warning: Incomplete | None = None) -> None: ...
    def __getattr__(self, item): ...
    def __dir__(self): ...
