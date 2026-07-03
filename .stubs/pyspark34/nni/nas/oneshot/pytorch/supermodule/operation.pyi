import torch
import torch.nn as nn
from ._operation_utils import int_or_int_dict, scalar_or_scalar_dict
from .base import BaseSuperNetModule
from _typeshed import Incomplete
from nni.nas.nn.pytorch.choice import ValueChoiceX
from typing import Any, Type, TypeVar

__all__ = ['MixedOperationSamplingPolicy', 'MixedOperation', 'MixedLinear', 'MixedConv2d', 'MixedBatchNorm2d', 'MixedLayerNorm', 'MixedMultiHeadAttention', 'NATIVE_MIXED_OPERATIONS']

T = TypeVar('T')

class MixedOperationSamplingPolicy:
    """
    Algo-related part for mixed Operation.

    :class:`MixedOperation` delegates its resample and export to this policy (or its subclass),
    so that one Operation can be easily combined with different kinds of sampling.

    One SamplingStrategy corresponds to one mixed operation.
    """
    def __init__(self, operation: MixedOperation, memo: dict[str, Any], mutate_kwargs: dict[str, Any]) -> None:
        """At init, the sampling policy can prepare basic parameters,
        and store them in operation if they need back propagation.

        This init is called in :meth:`BaseSuperNetModule.mutate`, after the mixed operation is created.
        So similar to :meth:`BaseSuperNetModule.mutate`,
        memo should also be managed (read and written) by the policy itself.
        """
    def resample(self, operation: MixedOperation, memo: dict[str, Any]) -> dict[str, Any]:
        """The handler of :meth:`MixedOperation.resample`."""
    def export(self, operation: MixedOperation, memo: dict[str, Any]) -> dict[str, Any]:
        """The handler of :meth:`MixedOperation.export`."""
    def export_probs(self, operation: MixedOperation, memo: dict[str, Any]) -> dict[str, Any]:
        """The handler of :meth:`MixedOperation.export_probs`."""
    def forward_argument(self, operation: MixedOperation, name: str) -> Any:
        """Computing the argument with ``name`` used in operation's forward.
        Usually a value, or a distribution of value.
        """

class MixedOperation(BaseSuperNetModule):
    """This is the base class for all mixed operations.
    It's what you should inherit to support a new operation with ValueChoice.

    It contains commonly used utilities that will ease the effort to write customized mixed oeprations,
    i.e., operations with ValueChoice in its arguments.
    To customize, please write your own mixed operation, and add the hook into ``mutation_hooks`` parameter when using the strategy.

    By design, for a mixed operation to work in a specific algorithm,
    at least two classes are needed.

    1. One class needs to inherit this class, to control operation-related behavior,
       such as how to initialize the operation such that the sampled operation can be its sub-operation.
    2. The other one needs to inherit :class:`MixedOperationSamplingPolicy`,
       which controls algo-related behavior, such as sampling.

    The two classes are linked with ``sampling_policy`` attribute in :class:`MixedOperation`,
    whose type is set via ``mixed_op_sampling`` in ``mutate_kwargs`` when
    :meth:`MixedOperation.mutate` is called.

    With this design, one mixed-operation (e.g., MixedConv2d) can work in multiple algorithms
    (e.g., both DARTS and ENAS), saving the engineering effort to rewrite all operations for
    each specific algo.

    This class should also define a ``bound_type``, to control the matching type in mutate,
    an ``argument_list``, to control which arguments can be dynamically used in ``forward``.
    This list will also be used in mutate for sanity check.
    """
    bound_type: Type[nn.Module]
    argument_list: list[str]
    sampling_policy: MixedOperationSamplingPolicy
    def super_init_argument(self, name: str, value_choice: ValueChoiceX) -> Any:
        """Get the initialization argument when constructing super-kernel, i.e., calling ``super().__init__()``.
        This is often related to specific operator, rather than algo.

        For example::

            def super_init_argument(self, name, value_choice):
                return max(value_choice.candidates)
        """
    def __post_init__(self) -> None:
        """Can be used to validate, or to do extra processing after calling ``__init__``."""
    def forward_with_args(self, *args, **kwargs) -> None:
        """To control real fprop. The accepted arguments are ``argument_list``,
        appended by forward arguments in the ``bound_type``."""
    mutable_arguments: Incomplete
    init_arguments: Incomplete
    def __init__(self, module_kwargs: dict[str, Any]) -> None: ...
    def resample(self, memo):
        """Delegates to :meth:`MixedOperationSamplingPolicy.resample`."""
    def export_probs(self, memo):
        """Delegates to :meth:`MixedOperationSamplingPolicy.export_probs`."""
    def export(self, memo):
        """Delegates to :meth:`MixedOperationSamplingPolicy.export`."""
    def search_space_spec(self): ...
    @classmethod
    def mutate(cls, module, name, memo, mutate_kwargs):
        """Find value choice in module's arguments and replace the whole module"""
    def forward_argument(self, name: str) -> Any:
        """Get the argument used in forward.
        This if often related to algo. We redirect this to sampling policy.
        """
    def forward(self, *args, **kwargs):
        """First get sampled arguments, then forward with the sampled arguments (by calling ``forward_with_args``)."""
    def slice_param(self, **kwargs) -> None:
        """Slice the params and buffers for subnet forward and state dict.
        When there is a `mapping=True` in kwargs, the return result will be wrapped in dict.
        """

class MixedLinear(MixedOperation, nn.Linear):
    """Mixed linear operation.

    Supported arguments are:

    - ``in_features``
    - ``out_features``

    Prefix of weight and bias will be sliced.
    """
    bound_type: Incomplete
    argument_list: Incomplete
    def super_init_argument(self, name: str, value_choice: ValueChoiceX): ...
    def slice_param(self, in_features: int_or_int_dict, out_features: int_or_int_dict, **kwargs) -> Any: ...
    def forward_with_args(self, in_features: int_or_int_dict, out_features: int_or_int_dict, inputs: torch.Tensor) -> torch.Tensor: ...

class MixedConv2d(MixedOperation, nn.Conv2d):
    '''Mixed conv2d op.

    Supported arguments are:

    - ``in_channels``
    - ``out_channels``
    - ``groups``
    - ``stride`` (only supported in path sampling)
    - ``kernel_size``
    - ``padding``
    - ``dilation`` (only supported in path sampling)

    ``padding`` will be the "max" padding in differentiable mode.

    Mutable ``groups`` is NOT supported in most cases of differentiable mode.
    However, we do support one special case when the group number is proportional to ``in_channels`` and ``out_channels``.
    This is often the case of depth-wise convolutions.

    For channels, prefix will be sliced.
    For kernels, we take the small kernel from the center and round it to floor (left top). For example ::

        max_kernel = 5*5, sampled_kernel = 3*3, then we take [1: 4]
        max_kernel = 5*5, sampled_kernel = 2*2, then we take [1: 3]
        □ □ □ □ □   □ □ □ □ □
        □ ■ ■ ■ □   □ ■ ■ □ □
        □ ■ ■ ■ □   □ ■ ■ □ □
        □ ■ ■ ■ □   □ □ □ □ □
        □ □ □ □ □   □ □ □ □ □
    '''
    bound_type: Incomplete
    argument_list: Incomplete
    def super_init_argument(self, name: str, value_choice: ValueChoiceX): ...
    def slice_param(self, in_channels: int_or_int_dict, out_channels: int_or_int_dict, kernel_size: scalar_or_scalar_dict[_int_or_tuple], groups: int_or_int_dict, **kwargs) -> Any: ...
    def forward_with_args(self, in_channels: int_or_int_dict, out_channels: int_or_int_dict, kernel_size: scalar_or_scalar_dict[_int_or_tuple], stride: _int_or_tuple, padding: scalar_or_scalar_dict[_int_or_tuple], dilation: int, groups: int_or_int_dict, inputs: torch.Tensor) -> torch.Tensor: ...

class MixedBatchNorm2d(MixedOperation, nn.BatchNorm2d):
    """
    Mixed BatchNorm2d operation.

    Supported arguments are:

    - ``num_features``
    - ``eps`` (only supported in path sampling)
    - ``momentum`` (only supported in path sampling)

    For path-sampling, prefix of ``weight``, ``bias``, ``running_mean`` and ``running_var``
    are sliced. For weighted cases, the maximum ``num_features`` is used directly.

    Momentum is required to be float.
    PyTorch BatchNorm supports a case where momentum can be none, which is not supported here.
    """
    bound_type: Incomplete
    argument_list: Incomplete
    def super_init_argument(self, name: str, value_choice: ValueChoiceX): ...
    def slice_param(self, num_features: int_or_int_dict, **kwargs) -> Any: ...
    def forward_with_args(self, num_features: int_or_int_dict, eps: float, momentum: float, inputs: torch.Tensor) -> torch.Tensor: ...

class MixedLayerNorm(MixedOperation, nn.LayerNorm):
    """
    Mixed LayerNorm operation.

    Supported arguments are:

    - ``normalized_shape``
    - ``eps`` (only supported in path sampling)

    For path-sampling, prefix of ``weight`` and ``bias`` are sliced.
    For weighted cases, the maximum ``normalized_shape`` is used directly.

    eps is required to be float.
    """
    bound_type: Incomplete
    argument_list: Incomplete
    def super_init_argument(self, name: str, value_choice: ValueChoiceX): ...
    def slice_param(self, normalized_shape, **kwargs) -> Any: ...
    def forward_with_args(self, normalized_shape, eps: float, inputs: torch.Tensor) -> torch.Tensor: ...

class MixedMultiHeadAttention(MixedOperation, nn.MultiheadAttention):
    """
    Mixed multi-head attention.

    Supported arguments are:

    - ``embed_dim``
    - ``num_heads`` (only supported in path sampling)
    - ``kdim``
    - ``vdim``
    - ``dropout`` (only supported in path sampling)

    At init, it constructs the largest possible Q, K, V dimension.
    At forward, it slices the prefix to weight matrices according to the sampled value.
    For ``in_proj_bias`` and ``in_proj_weight``, three parts will be sliced and concatenated together:
    ``[0, embed_dim)``, ``[max_embed_dim, max_embed_dim + embed_dim)``,
    ``[max_embed_dim * 2, max_embed_dim * 2 + embed_dim)``.

    Warnings
    ----------
    All candidates of ``embed_dim`` should be divisible by all candidates of ``num_heads``.
    """
    bound_type: Incomplete
    argument_list: Incomplete
    q_proj_weight: Incomplete
    k_proj_weight: Incomplete
    v_proj_weight: Incomplete
    def __post_init__(self) -> None: ...
    def super_init_argument(self, name: str, value_choice: ValueChoiceX): ...
    def slice_param(self, embed_dim, kdim, vdim, **kwargs): ...
    def forward_with_args(self, embed_dim: int_or_int_dict, num_heads: int, kdim: int_or_int_dict | None, vdim: int_or_int_dict | None, dropout: float, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor, key_padding_mask: torch.Tensor | None = None, need_weights: bool = True, attn_mask: torch.Tensor | None = None) -> tuple[torch.Tensor, torch.Tensor | None]: ...

NATIVE_MIXED_OPERATIONS: list[Type[MixedOperation]]
