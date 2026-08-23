from .logging import get_logger as get_logger
from _typeshed import Incomplete

logger: Incomplete

class _PatchedModuleObj:
    """Set all the modules components as attributes of the _PatchedModuleObj object."""
    def __init__(self, module, attrs: Incomplete | None = None) -> None: ...

class patch_submodule:
    '''
    Patch a submodule attribute of an object, by keeping all other submodules intact at all levels.

    Example::

        >>> import importlib
        >>> from datasets.load import dataset_module_factory
        >>> from datasets.streaming import patch_submodule, xjoin
        >>>
        >>> dataset_module = dataset_module_factory("snli")
        >>> snli_module = importlib.import_module(dataset_module.module_path)
        >>> patcher = patch_submodule(snli_module, "os.path.join", xjoin)
        >>> patcher.start()
        >>> assert snli_module.os.path.join is xjoin
    '''
    obj: Incomplete
    target: Incomplete
    new: Incomplete
    key: Incomplete
    original: Incomplete
    attrs: Incomplete
    def __init__(self, obj, target: str, new, attrs: Incomplete | None = None) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, *exc_info) -> None: ...
    def start(self) -> None:
        """Activate a patch."""
    def stop(self):
        """Stop an active patch."""
