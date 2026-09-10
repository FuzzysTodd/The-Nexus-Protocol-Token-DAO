import torch.nn as nn
from typing import Any, Tuple

__all__ = ['Mutable', 'generate_new_label', 'get_fixed_value', 'get_fixed_dict']

class Mutable(nn.Module):
    """
    This is just an implementation trick for now.

    In future, this could be the base class for all PyTorch mutables including layer choice, input choice, etc.
    This is not considered as an interface, but rather as a base class consisting of commonly used class/instance methods.
    For API developers, it's not recommended to use ``isinstance(module, Mutable)`` to check for mutable modules either,
    before the design is finalized.
    """
    def __new__(cls, *args, **kwargs): ...
    @classmethod
    def create_fixed_module(cls, *args, **kwargs) -> nn.Module | Any:
        """
        Try to create a fixed module from fixed dict.
        If the code is running in a trial, this method would succeed, and a concrete module instead of a mutable will be created.
        Raises no context error if the creation failed.
        """

def generate_new_label(label: str | None): ...
def get_fixed_value(label: str | None) -> Any: ...
def get_fixed_dict(label_prefix: str | None) -> Tuple[str, Any]: ...
