import torch
import torch.nn as nn
from .base import BaseSuperNetModule
from .operation import MixedOperation, MixedOperationSamplingPolicy
from .sampling import PathSamplingCell
from _typeshed import Incomplete
from collections.abc import Generator
from nni.nas.nn.pytorch import ChoiceOf
from typing import Any

__all__ = ['DifferentiableMixedLayer', 'DifferentiableMixedInput', 'DifferentiableMixedRepeat', 'DifferentiableMixedCell', 'MixedOpDifferentiablePolicy', 'GumbelSoftmax']

class GumbelSoftmax(nn.Softmax):
    """Wrapper of ``F.gumbel_softmax``. dim = -1 by default."""
    dim: int
    tau: int
    hard: bool
    def __init__(self, dim: int = -1) -> None: ...
    def forward(self, inputs: torch.Tensor) -> torch.Tensor: ...

class DifferentiableMixedLayer(BaseSuperNetModule):
    '''
    Mixed layer, in which fprop is decided by a weighted sum of several layers.
    Proposed in `DARTS: Differentiable Architecture Search <https://arxiv.org/abs/1806.09055>`__.

    The weight ``alpha`` is usually learnable, and optimized on validation dataset.

    Differentiable sampling layer requires all operators returning the same shape for one input,
    as all outputs will be weighted summed to get the final output.

    Parameters
    ----------
    paths : list[tuple[str, nn.Module]]
        Layers to choose from. Each is a tuple of name, and its module.
    alpha : Tensor
        Tensor that stores the "learnable" weights.
    softmax : nn.Module
        Customizable softmax function. Usually ``nn.Softmax(-1)``.
    label : str
        Name of the choice.

    Attributes
    ----------
    op_names : str
        Operator names.
    label : str
        Name of the choice.
    '''
    op_names: Incomplete
    label: Incomplete
    def __init__(self, paths: list[tuple[str, nn.Module]], alpha: torch.Tensor, softmax: nn.Module, label: str) -> None: ...
    def resample(self, memo):
        """Do nothing. Differentiable layer doesn't need resample."""
    def export(self, memo):
        """Choose the operator with the maximum logit."""
    def export_probs(self, memo): ...
    def search_space_spec(self): ...
    @classmethod
    def mutate(cls, module, name, memo, mutate_kwargs): ...
    def reduction(self, items: list[Any], weights: list[float]) -> Any:
        """Override this for customized reduction."""
    def forward(self, *args, **kwargs):
        """The forward of mixed layer accepts same arguments as its sub-layer."""
    def parameters(self, *args, **kwargs) -> Generator[Incomplete, None, None]:
        """Parameters excluding architecture parameters."""
    def named_parameters(self, *args, **kwargs) -> Generator[Incomplete, None, None]:
        """Named parameters excluding architecture parameters."""

class DifferentiableMixedInput(BaseSuperNetModule):
    '''
    Mixed input. Forward returns a weighted sum of candidates.
    Implementation is very similar to :class:`DifferentiableMixedLayer`.

    Parameters
    ----------
    n_candidates : int
        Expect number of input candidates.
    n_chosen : int
        Expect numebr of inputs finally chosen.
    alpha : Tensor
        Tensor that stores the "learnable" weights.
    softmax : nn.Module
        Customizable softmax function. Usually ``nn.Softmax(-1)``.
    label : str
        Name of the choice.

    Attributes
    ----------
    label : str
        Name of the choice.
    '''
    n_candidates: Incomplete
    n_chosen: int
    label: Incomplete
    def __init__(self, n_candidates: int, n_chosen: int | None, alpha: torch.Tensor, softmax: nn.Module, label: str) -> None: ...
    def resample(self, memo):
        """Do nothing. Differentiable layer doesn't need resample."""
    def export(self, memo):
        """Choose the operator with the top ``n_chosen`` logits."""
    def export_probs(self, memo): ...
    def search_space_spec(self): ...
    @classmethod
    def mutate(cls, module, name, memo, mutate_kwargs): ...
    def reduction(self, items: list[Any], weights: list[float]) -> Any:
        """Override this for customized reduction."""
    def forward(self, inputs):
        """Forward takes a list of input candidates."""
    def parameters(self, *args, **kwargs) -> Generator[Incomplete, None, None]:
        """Parameters excluding architecture parameters."""
    def named_parameters(self, *args, **kwargs) -> Generator[Incomplete, None, None]:
        """Named parameters excluding architecture parameters."""

class MixedOpDifferentiablePolicy(MixedOperationSamplingPolicy):
    """Implementes the differentiable sampling in mixed operation.

    One mixed operation can have multiple value choices in its arguments.
    Thus the ``_arch_alpha`` here is a parameter dict, and ``named_parameters``
    filters out multiple parameters with ``_arch_alpha`` as its prefix.

    When this class is asked for ``forward_argument``, it returns a distribution,
    i.e., a dict from int to float based on its weights.

    All the parameters (``_arch_alpha``, ``parameters()``, ``_softmax``) are
    saved as attributes of ``operation``, rather than ``self``,
    because this class itself is not a ``nn.Module``, and saved parameters here
    won't be optimized.
    """
    def __init__(self, operation: MixedOperation, memo: dict[str, Any], mutate_kwargs: dict[str, Any]) -> None: ...
    @staticmethod
    def parameters(module, *args, **kwargs) -> Generator[Incomplete, None, None]: ...
    @staticmethod
    def named_parameters(module, *args, **kwargs) -> Generator[Incomplete, None, None]: ...
    def resample(self, operation: MixedOperation, memo: dict[str, Any]) -> dict[str, Any]:
        """Differentiable. Do nothing in resample."""
    def export(self, operation: MixedOperation, memo: dict[str, Any]) -> dict[str, Any]:
        """Export is argmax for each leaf value choice."""
    def export_probs(self, operation: MixedOperation, memo: dict[str, Any]):
        """Export the weight for every leaf value choice."""
    def forward_argument(self, operation: MixedOperation, name: str) -> dict[Any, float] | Any: ...

class DifferentiableMixedRepeat(BaseSuperNetModule):
    """
    Implementaion of Repeat in a differentiable supernet.
    Result is a weighted sum of possible prefixes, sliced by possible depths.

    If the output is not a single tensor, it will be summed at every independant dimension.
    See :func:`weighted_sum` for details.
    """
    blocks: Incomplete
    depth: Incomplete
    def __init__(self, blocks: list[nn.Module], depth: ChoiceOf[int], softmax: nn.Module, memo: dict[str, Any]) -> None: ...
    def resample(self, memo):
        """Do nothing."""
    def export(self, memo):
        """Choose argmax for each leaf value choice."""
    def export_probs(self, memo):
        """Export the weight for every leaf value choice."""
    def search_space_spec(self): ...
    @classmethod
    def mutate(cls, module, name, memo, mutate_kwargs): ...
    def parameters(self, *args, **kwargs) -> Generator[Incomplete, None, None]: ...
    def named_parameters(self, *args, **kwargs) -> Generator[Incomplete, None, None]: ...
    def reduction(self, items: list[Any], weights: list[float], depths: list[int]) -> Any:
        """Override this for customized reduction."""
    def forward(self, x): ...

class DifferentiableMixedCell(PathSamplingCell):
    """Implementation of Cell under differentiable context.

    Similar to PathSamplingCell, this cell only handles cells of specific kinds (e.g., with loose end).

    An architecture parameter is created on each edge of the full-connected graph.
    """
    def __init__(self, op_factory, num_nodes, num_ops_per_node, num_predecessors, preprocessor, postprocessor, concat_dim, memo, mutate_kwargs, label) -> None: ...
    def resample(self, memo):
        """Differentiable doesn't need to resample."""
    def export_probs(self, memo):
        """When export probability, we follow the structure in arch alpha."""
    def export(self, memo):
        """Tricky export.

        Reference: https://github.com/quark0/darts/blob/f276dd346a09ae3160f8e3aca5c7b193fda1da37/cnn/model_search.py#L135
        """
    def forward(self, *inputs: list[torch.Tensor] | torch.Tensor) -> tuple[torch.Tensor, ...] | torch.Tensor: ...
    def parameters(self, *args, **kwargs) -> Generator[Incomplete, None, None]: ...
    def named_parameters(self, *args, **kwargs) -> Generator[Incomplete, None, None]: ...
