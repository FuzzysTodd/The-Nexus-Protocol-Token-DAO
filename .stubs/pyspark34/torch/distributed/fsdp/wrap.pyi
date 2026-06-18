import abc
import torch.nn as nn
from abc import ABC, abstractmethod
from typing import Any, Callable, Dict, Generator, Set, Type

__all__ = ['always_wrap_policy', 'lambda_auto_wrap_policy', 'transformer_auto_wrap_policy', 'size_based_auto_wrap_policy', 'enable_wrap', 'wrap', 'ModuleWrapPolicy']

def always_wrap_policy(*args, **kwargs) -> bool:
    """
    A simple recursive wrap policy that always returns ``True``. This means
    that every submodule is wrapped by the wrapper class in
    :func:`_recursive_wrap`.
    """

class _FSDPPolicy(ABC, metaclass=abc.ABCMeta):
    """
    This defines an abstract base class that represents an FSDP policy for
    constructing ``FlatParameter`` s.
    """
    def __init__(self) -> None: ...
    @property
    @abstractmethod
    def policy(self) -> Callable: ...

class ModuleWrapPolicy(_FSDPPolicy):
    """This is a wrapper around :func:`_module_wrap_policy`."""
    def __init__(self, module_classes: Set[Type[nn.Module]]) -> None: ...
    @property
    def policy(self): ...

def lambda_auto_wrap_policy(module: nn.Module, recurse: bool, nonwrapped_numel: int, lambda_fn: Callable) -> bool:
    """
    A convenient auto wrap policy to wrap submodules based on an arbitrary user
    function. If `lambda_fn(submodule) == True``, the submodule will be wrapped as
    a `wrapper_cls` unit.

    Return if a module should be wrapped during auto wrapping.

    The first three parameters are required by :func:`_recursive_wrap`.

    Args:
        module (nn.Module): Current module being considered.
        recurse (bool): If ``False``, then this function must decide whether
            ``module`` should be wrapped as an FSDP instance or not. If
            ``True``, then the function is still recursing down the module
            tree as a part of the DFS.
        nonwrapped_numel (int): Parameter numel not yet wrapped.

        lambda_fn (Callable[[nn.Module], bool]): If this returns ``True``, then
            this module will be wrapped.
    """
def transformer_auto_wrap_policy(module: nn.Module, recurse: bool, nonwrapped_numel: int, transformer_layer_cls: Set[Type[nn.Module]]) -> bool:
    """
    See :func:`_module_wrap_policy`, where ``transformer_layer_cls`` is the
    same as ``module_classes``. Note that shared parameters must be wrapped in
    the same FSDP instance, so this auto wrap policy can help wrap shared
    embeddings into the same FSDP instance for transformer models.
    """
def size_based_auto_wrap_policy(module: nn.Module, recurse: bool, nonwrapped_numel: int, min_num_params: int = ..., force_leaf_modules: Set[Type[nn.Module]] | None = None, exclude_wrap_modules: Set[Type[nn.Module]] | None = None) -> bool:
    """
    A size-based auto wrap policy.

    Args:
        module (nn.Module): Current module being considered.
        recurse (bool): If ``False``, then this function must decide whether
            ``module`` should be wrapped as an FSDP instance or not. If
            ``True``, then the function is still recursing down the module
            tree as a part of the DFS.
        nonwrapped_numel (int): Parameter numel not yet wrapped.

        min_num_params (int): Customizable policy input that controls the size
            threshold over which a module is ready to be wrapped. This is in
            units of numel.
        force_leaf_modules (Set[Type[nn.Module]]): Set of module types to keep
            as leaves, i.e. their children will never be wrapped.
        exclude_wrap_modules (Set[Type[nn.Module]]): Set of module types to be
            excluded in wrapping.

    Returns:
        Whether ``module`` should be wrapped.
    """
def enable_wrap(*, wrapper_cls: Any, **wrapper_kwargs: Any) -> Generator[None, None, None]:
    """
    Context manager to wrap modules using a wrapper.

    Useful for when you'd like to apply the same configuration arguments to all
    child modules that you wrap. A particularly important use case is wrapping
    large layers so that they get sharded (in-place) during initialization, to
    avoid running out of system memory. Large layers can indicate that they
    should be sharded via the ``wrap`` annotation and this context manager can
    provide the exact configuration for these nested instances.

    Usage::

        with enable_wrap(wrapper_cls, **params):
            # Wraps layer in FSDP by default if within context
            self.l1 = wrap(torch.nn.Linear(5, 5))

    Args:
        wrapper_cls:
            Class that `wrap` annotation will `wrap` modules with, such as
            `FullyShardedDataParallel`.
        **wrapper_kwargs:
            Configuration settings that will be passed to all ``wrap``
            instances inside the context
    """
def wrap(module: nn.Module, **wrap_overrides: Any) -> nn.Module:
    """
    Annotate that a module should be wrapped. Annotated modules will only be
    wrapped if inside of an :func:`enable_wrap` context manager. This allows
    a module to be initialized both with and without a wrapper without code
    change.

    The class that this function wraps the passed in ``nn.Module`` with is the
    passed in ``wrapper_cls`` argument into ``enable_wrap``. Both
    ``enable_wrap`` and ``wrap`` can take in kwargs specifying how to construct
    the ``wrapper_cls`` instance. In the case of duplicate kwargs in
    ``enable_wrap`` and ``wrap``, the argument passed into ``wrap`` will be
    respected.

    Usage::

        with enable_wrap(wrapper_cls=FSDP, **fsdp_config):
            # Wraps layer in FSDP by default if within context
            self.l1 = wrap(torch.nn.Linear(5, 5))

    Args:
        module (nn.Module): module to wrap (if in :func:`enable_wrap` context)
        **wrap_overrides: configuration overrides that will take priority over
            the values provided by the :func:`enable_wrap` context
    """

class _ConfigAutoWrap:
    """
    Helper class to wrap modules based on default config args via a context manager.
    See :func:`enable_wrap` for more information.
    """
    in_autowrap_context: bool
    wrapper_cls: Callable | None
    kwargs: Dict[str, Any]
    def __init__(self, **kwargs: Dict[str, Any]) -> None: ...
    @staticmethod
    def enable_autowrap_context(kwargs: Any) -> None: ...
    @staticmethod
    def disable_autowrap_context() -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: ...
