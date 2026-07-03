import torch
from _typeshed import Incomplete
from enum import Enum
from torch.autograd.graph import save_on_cpu as save_on_cpu
from typing import Any, Iterator, Tuple

class CheckpointImpl(Enum):
    REENTRANT: Incomplete
    NO_REENTRANT: Incomplete

class ActivationWrapper(torch.nn.Module):
    """
    Base class for Activation Checkpoint and Activation Offload.
    Not meant to be instantiated directly.
    """
    def __init__(self, mod) -> None: ...
    def forward(self, *args, **kwargs) -> None: ...
    def __getattr__(self, name: str) -> Any:
        """Forward missing attributes to wrapped module."""
    def __getitem__(self, key: int) -> Any:
        """Forward indexing calls in case the module is a nn.Sequential."""
    def named_parameters(self, *args, **kwargs) -> Iterator[Tuple[str, torch.nn.Parameter]]:
        """
        Overrides :meth:`named_parameters()` to intercept parameter names and
        remove all occurrences of ``_CHECKPOINT_PREFIX``.
        """

class OffloadWrapper(ActivationWrapper):
    def __init__(self, mod) -> None: ...
    def forward(self, *args, **kwargs): ...

class CheckpointWrapper(ActivationWrapper):
    """
    An ``nn.Module`` that wraps another ``nn.Module`` with checkpointing. Note that this
    module is not meant to be used directly, but instead it is to be used
    through the ``checkpoint_wrapper`` function.
    """
    checkpoint_impl: Incomplete
    checkpoint_fn: Incomplete
    def __init__(self, mod: torch.nn.Module, checkpoint_impl: CheckpointImpl = ..., checkpoint_fn: Incomplete | None = None, *checkpoint_fn_args, **checkpoint_fn_kwargs) -> None: ...
    def forward(self, *args, **kwargs): ...

def offload_wrapper(module: torch.nn.Module) -> torch.nn.Module:
    """
    A convenience wrapper for activation offloading to CPU. If the module is wrapped
    with this function, all subsequent calls to the module will automatically
    offload intermediate activations to the CPU. Wrappers with activation
    offload can be composed with ones that do recomputation-based
    checkpoint to trade off increased compute versus increased CPU
    memory usage and additional H2D transfers.
    Usage::
        offloaded_module = offload_wrapper(module)
        outputs = checkpointed_module(inputs)
    Args:
        module (nn.Module):
            The module to be wrapped
    Returns:
        (nn.Module):
            Wrapped module
    """
def checkpoint_wrapper(module: torch.nn.Module, checkpoint_impl: CheckpointImpl = ..., checkpoint_fn: Incomplete | None = None, *checkpoint_fn_args, **checkpoint_fn_kwargs) -> torch.nn.Module:
    """
    A convenience wrapper for activation checkpointing. If the module is wrapped
    with this function, all subsequent calls to the module will automatically
    perform checkpointing without the user having to explicitly call ``checkpoint``
    function.
    Usage::
        checkpointed_module = checkpoint_wrapper(module)
        outputs = checkpointed_module(inputs)
    Args:
        module (nn.Module):
            The module to be wrapped
        checkpoint_impl (Optional[CheckpointImpl]):
            The checkpointing implementation to use. Note that this will only
            be passed into the ``torch.utils.checkpoint.checkpoint``
            implementation, and is ignored if a custom ``checkpoint_fn`` is
            specified. Note that for implementations using reentrant checkpoint
            from ``torch.utils.checkpoint``, keyword arguments will only be
            supported if ``checkpoint_impl`` is passed as ``CheckpointImpl.REENTRANT`.
        checkpoint_fn (Optional[Callable]):
            Functional checkpoint implementation to use. If this is specified,
            it will be used over the default ``torch.utils.checkpoint.checkpoint``
            implementation and the `checkpoint_impl` argument will be ignored.
        *checkpoint_fn_args: (Sequence[Any]): Arguments to pass into `checkpoint_fn`.
        **checkpoint_fn_kwargs: (Dict[str, Any]): Keyword arguments to pass into `checkpoint_fn`.

    Returns:
        (nn.Module):
            Wrapped module
    """
def apply_activation_checkpointing(model, checkpoint_wrapper_fn=..., check_fn=...):
    """
    Applies :func:`checkpoint_wrapper` to modules within `model` based on a user-defined
    configuration. For each module within `model`, the `check_fn` is used to decide
    whether `module` should be wrapped with :func:`checkpoint_wrapper` or not.

    Note::
        This function modifies `model` in place and replaces appropriate layers with
        their checkpoint-wrapped modules.
    Note::
        This function will not wrap the overall root module. If this is needed, please directly use
        :func:`checkpoint_wrapper` or :func:`offload_wrapper`.
    Usage::
        model = nn.Sequential(
            nn.Linear(10, 10), nn.Linear(10, 10), nn.Linear(10, 10)
        )
        check_fn = lambda l: isinstance(l, nn.Linear)
        # checkpoint activations
        apply_activation_checkpointing(model, checkpoint_wrapper_fn=checkpoint_wrapper, check_fn=check_fn)
        # Or offload activations to CPU
        apply_activation_checkpointing(model, checkpoint_wrapper_fn=offload_wrapper, check_fn=check_fn)
    Args:
        model (nn.Module):
            The model whose submodules should be wrapped with activation checkpointing.
        checkpoint_wrapper_fn (Optional[Callable[nn.Module]])
            A ``Callable`` which will wrap modules
        check_fn (Optional[Callable[nn.Module, nn.Module]])
            A lambda function which will be passed each child submoule of ``model`` and returns
            ``True`` or ``False`` depending on whether the submodule should be wrapped.
    Returns: None (`model` is modified inplace)
    """
