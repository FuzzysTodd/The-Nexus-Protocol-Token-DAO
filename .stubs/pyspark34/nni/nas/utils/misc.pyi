from _typeshed import Incomplete
from typing import Any

__all__ = ['NoContextError', 'ContextStack', 'ModelNamespace', 'original_state_dict_hooks', 'uid', 'import_', 'reset_uid', 'get_module_name', 'get_importable_name', 'get_current_context', 'STATE_DICT_PY_MAPPING', 'STATE_DICT_PY_MAPPING_PARTIAL']

def import_(target: str, allow_none: bool = False) -> Any: ...
def uid(namespace: str = 'default') -> int: ...
def reset_uid(namespace: str = 'default') -> None: ...
def get_module_name(cls_or_func): ...
def get_importable_name(cls, relocate_module: bool = False): ...

class NoContextError(Exception):
    """Exception raised when context is missing."""

class ContextStack:
    """
    This is to maintain a globally-accessible context environment that is visible to everywhere.

    Use ``with ContextStack(namespace, value):`` to initiate, and use ``get_current_context(namespace)`` to
    get the corresponding value in the namespace.

    Note that this is not multi-processing safe. Also, the values will get cleared for a new process.
    """
    key: Incomplete
    value: Incomplete
    def __init__(self, key: str, value: Any) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *args, **kwargs) -> None: ...
    @classmethod
    def push(cls, key: str, value: Any): ...
    @classmethod
    def pop(cls, key: str) -> Any: ...
    @classmethod
    def top(cls, key: str) -> Any: ...

class ModelNamespace:
    """
    To create an individual namespace for models:

    1. to enable automatic numbering;
    2. to trace general information (like creation of hyper-parameters) of model.

    A namespace is bounded to a key. Namespace bounded to different keys are completed isolated.
    Namespace can have sub-namespaces (with the same key). The numbering will be chained (e.g., ``model_1_4_2``).
    """
    key: Incomplete
    name_path: Incomplete
    parameter_specs: Incomplete
    def __init__(self, key: str = ...) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, *args, **kwargs) -> None: ...
    @staticmethod
    def current_context(key: str = ...) -> ModelNamespace:
        """Get the current context in key."""
    @staticmethod
    def next_label(key: str = ...) -> str:
        """Get the next label for API calls, with automatic numbering."""

def get_current_context(key: str) -> Any: ...

STATE_DICT_PY_MAPPING: str
STATE_DICT_PY_MAPPING_PARTIAL: str

def original_state_dict_hooks(model: Any):
    """
    Use this patch if you want to save/load state dict in the original state dict hierarchy.

    For example, when you already have a state dict for the base model / search space (which often
    happens when you have trained a supernet with one-shot strategies), the state dict isn't organized
    in the same way as when a sub-model is sampled from the search space. This patch will help
    the modules in the sub-model find the corresponding module in the base model.

    The code looks like,

    .. code-block:: python

        with original_state_dict_hooks(model):
            model.load_state_dict(state_dict_from_supernet, strict=False)  # supernet has extra keys

    Or vice-versa,

    .. code-block:: python

        with original_state_dict_hooks(model):
            supernet_style_state_dict = model.state_dict()
    """
