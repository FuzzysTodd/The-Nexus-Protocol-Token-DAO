from _typeshed import Incomplete
from typing import Any, Dict, List

string_types: Incomplete

def synchronized(lock): ...

class HookInfoNode:
    fullname: Incomplete
    hooks: Incomplete
    childs: Incomplete
    def __init__(self, fullname: str, hooks: List[Any] = [], childs: Dict[str, 'HookInfoNode'] = {}) -> None: ...

def register_generic_import_hook_submodule(hook: Any, name: str, overwrite: bool = True) -> bool: ...
def register_generic_import_hook(hook, name, hook_dict, overwrite) -> None: ...
def hooks_equal(existing_hook, hook): ...
def register_import_error_hook(hook, name, overwrite: bool = True) -> None:
    """
    :param hook: A function or string entrypoint to invoke when the specified module is imported
                 and an error occurs.
    :param name: The name of the module for which to fire the hook at import error detection time.
    :param overwrite: Specifies the desired behavior when a preexisting hook for the same
                      function / entrypoint already exists for the specified module. If `True`,
                      all preexisting hooks matching the specified function / entrypoint will be
                      removed and replaced with a single instance of the specified `hook`.
    """
def register_post_import_hook(hook, name, overwrite: bool = True) -> None:
    """
    :param hook: A function or string entrypoint to invoke when the specified module is imported.
    :param name: The name of the module for which to fire the hook at import time.
    :param overwrite: Specifies the desired behavior when a preexisting hook for the same
                      function / entrypoint already exists for the specified module. If `True`,
                      all preexisting hooks matching the specified function / entrypoint will be
                      removed and replaced with a single instance of the specified `hook`.
    """
def register_post_import_hook_sub_modules(hook, name, overwrite: bool = True) -> None:
    """
    :param hook: A function or string entrypoint to invoke when the specified module is imported.
    :param name: The name of the module for which to fire the hook at import time.
    :param overwrite: Specifies the desired behavior when a preexisting hook for the same
                      function / entrypoint already exists for the specified module. If `True`,
                      all preexisting hooks matching the specified function / entrypoint will be
                      removed and replaced with a single instance of the specified `hook`.
    """
def discover_post_import_hooks(group) -> None: ...
def collect_hooks(fullname: str) -> List[Any]: ...
def notify_module_loaded(module) -> None: ...
def notify_module_import_error(module_name) -> None: ...

class _ImportHookChainedLoader:
    loader: Incomplete
    def __init__(self, loader) -> None: ...
    def load_module(self, fullname): ...

class ImportHookFinder:
    in_progress: Incomplete
    def __init__(self) -> None: ...
    def find_module(self, fullname, path: Incomplete | None = None): ...
    def find_spec(self, fullname, path, target: Incomplete | None = None): ...

def when_imported(name, error_handler: bool = False): ...
