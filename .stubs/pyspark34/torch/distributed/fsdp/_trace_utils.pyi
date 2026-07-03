import torch
import torch.nn as nn
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import Any, Dict, List, NamedTuple, Tuple

@dataclass
class TracingConfig:
    """
    This represents a symbolic tracing configuration.

    Args:
        tracer (torch.fx.Tracer): An instance of :class:`torch.fx.Tracer` to
            use for symbolic tracing. The default value is the native
            :class:`torch.fx.Tracer` constructed with default arguments.
            However, the user may want to pass a different value such as the
            ``HFTracer`` for models in the HuggingFace Transformers_ library.
            .. _Transformers: https://huggingface.co/docs/transformers/index
        concrete_args (Optional[Dict[str, Any]]): Concrete arguments that
            should not be treated as ``torch.fx.Proxy`` when tracing the
            module ``forward()``. Passing ``concrete_args`` allows partially
            specializing the forward, e.g. to remove control flow or data
            structures. This ``concrete_args`` here is the same argument used
            in :meth:`~torch.fx.Tracer.trace`.
    """
    tracer: torch.fx.Tracer = ...
    concrete_args: Dict[str, Any] | None = ...
    def __init__(self, tracer, concrete_args) -> None: ...

class _ParamUsageInfo(NamedTuple):
    """
    This is used for ``_ExecutionInfo.module_to_param_usage_infos`` to record
    execution information. The ``dict`` maps modules to a list of these
    ``_ParamUsageInfo`` instances, where each instance represents a group of
    parameters used together.

    Specifically, for each module key in the ``dict``, each instance of this
    class represents either:
    (1) the module and some sublist of its ``named_parameters()`` used
    together in execution (see ``_patched_create_proxy()``), or
    (2) a submodule and all of ``submodule.named_parameters()`` (see
    ``_patched_call_module()``).

    Type (1) corresponds to directly using parameters in ops without calling
    ``forward()``, and type (2) corresponds to calling ``forward()``. The
    mapped-to lists in the ``dict`` follow the execution order.
    """
    module: nn.Module
    named_params: List[Tuple[str, nn.Parameter]]

class _ExecutionInfo:
    """
    This represents the execution order information from the forward pass.

    Attributes:
        curr_module (nn.Module): Current module being traced.
        module_forward_order (List[nn.Module]): The modules in (pre-)forward
            order, i.e. the order in which their ``forward()`` methods are
            called. Each call to a module's ``forward()`` corresponds to one
            element in the list.
        module_to_param_usage_infos (Dict[nn.Module, List[_ParamUsageInfo]]):
            Maps a module to a list of module execution infos. See
            :class:`_ParamUsageInfo` for details.
        param_forward_order (List[nn.Parameter]): The parameters in forward
            execution order, where only a parameter's first participation is
            included.
        visited_params (Set[nn.Parameter]): The parameters visited so far
            during the trace. This is only used during tracing for fast
            membership check. Invariant: The parameters in
            ``param_forward_order`` are exactly those in ``visited_params``.
    """
    curr_module: Incomplete
    module_forward_order: Incomplete
    module_to_param_usage_infos: Incomplete
    param_forward_order: Incomplete
    visited_params: Incomplete
    def __init__(self, root_module: nn.Module) -> None: ...

class _ExecOrderTracer:
    exec_info: Incomplete
    def __init__(self) -> None: ...
    def patch_tracer(self, tracer: torch.fx.Tracer, root_module: nn.Module): ...
