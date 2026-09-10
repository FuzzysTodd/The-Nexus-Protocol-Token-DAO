import torch
import torch.nn as nn
from .base import BaseSuperNetModule
from .operation import MixedOperation, MixedOperationSamplingPolicy
from _typeshed import Incomplete
from nni.common.hpo_utils import ParameterSpec
from nni.nas.nn.pytorch import ChoiceOf
from nni.nas.nn.pytorch.cell import CellOpFactory
from typing import Any

__all__ = ['PathSamplingLayer', 'PathSamplingInput', 'PathSamplingRepeat', 'PathSamplingCell', 'MixedOpPathSamplingPolicy']

class PathSamplingLayer(BaseSuperNetModule):
    """
    Mixed layer, in which fprop is decided by exactly one inner layer or sum of multiple (sampled) layers.
    If multiple modules are selected, the result will be summed and returned.

    Attributes
    ----------
    _sampled : int or list of str
        Sampled module indices.
    label : str
        Name of the choice.
    """
    op_names: Incomplete
    label: Incomplete
    def __init__(self, paths: list[tuple[str, nn.Module]], label: str) -> None: ...
    def resample(self, memo):
        """Random choose one path if label is not found in memo."""
    def export(self, memo):
        """Random choose one name if label isn't found in memo."""
    def search_space_spec(self): ...
    @classmethod
    def mutate(cls, module, name, memo, mutate_kwargs): ...
    def reduction(self, items: list[Any], sampled: list[Any]):
        """Override this to implement customized reduction."""
    def forward(self, *args, **kwargs): ...

class PathSamplingInput(BaseSuperNetModule):
    """
    Mixed input. Take a list of tensor as input, select some of them and return the sum.

    Attributes
    ----------
    _sampled : int or list of int
        Sampled input indices.
    """
    n_candidates: Incomplete
    n_chosen: Incomplete
    reduction_type: Incomplete
    label: Incomplete
    def __init__(self, n_candidates: int, n_chosen: int, reduction_type: str, label: str) -> None: ...
    def resample(self, memo):
        """Random choose one path / multiple paths if label is not found in memo.
        If one path is selected, only one integer will be in ``self._sampled``.
        If multiple paths are selected, a list will be in ``self._sampled``.
        """
    def export(self, memo):
        """Random choose one name if label isn't found in memo."""
    def search_space_spec(self): ...
    @classmethod
    def mutate(cls, module, name, memo, mutate_kwargs): ...
    def reduction(self, items: list[Any], sampled: list[Any]) -> Any:
        """Override this to implement customized reduction."""
    def forward(self, input_tensors): ...

class MixedOpPathSamplingPolicy(MixedOperationSamplingPolicy):
    '''Implements the path sampling in mixed operation.

    One mixed operation can have multiple value choices in its arguments.
    Each value choice can be further decomposed into "leaf value choices".
    We sample the leaf nodes, and composits them into the values on arguments.
    '''
    def __init__(self, operation: MixedOperation, memo: dict[str, Any], mutate_kwargs: dict[str, Any]) -> None: ...
    def resample(self, operation: MixedOperation, memo: dict[str, Any]) -> dict[str, Any]:
        """Random sample for each leaf value choice."""
    def export(self, operation: MixedOperation, memo: dict[str, Any]) -> dict[str, Any]:
        """Export is also random for each leaf value choice."""
    def forward_argument(self, operation: MixedOperation, name: str) -> Any: ...

class PathSamplingRepeat(BaseSuperNetModule):
    """
    Implementaion of Repeat in a path-sampling supernet.
    Samples one / some of the prefixes of the repeated blocks.

    Attributes
    ----------
    _sampled : int or list of int
        Sampled depth.
    """
    blocks: Incomplete
    depth: Incomplete
    def __init__(self, blocks: list[nn.Module], depth: ChoiceOf[int]) -> None: ...
    def resample(self, memo):
        """Since depth is based on ValueChoice, we only need to randomly sample every leaf value choices."""
    def export(self, memo):
        """Random choose one if every choice not in memo."""
    def search_space_spec(self): ...
    @classmethod
    def mutate(cls, module, name, memo, mutate_kwargs): ...
    def reduction(self, items: list[Any], sampled: list[Any]):
        """Override this to implement customized reduction."""
    def forward(self, x): ...

class PathSamplingCell(BaseSuperNetModule):
    """The implementation of super-net cell follows `DARTS <https://github.com/quark0/darts>`__.

    When ``factory_used`` is true, it reconstructs the cell for every possible combination of operation and input index,
    because for different input index, the cell factory could instantiate different operations (e.g., with different stride).
    On export, we first have best (operation, input) pairs, the select the best ``num_ops_per_node``.

    ``loose_end`` is not supported yet, because it will cause more problems (e.g., shape mismatch).
    We assumes ``loose_end`` to be ``all`` regardless of its configuration.

    A supernet cell can't slim its own weight to fit into a sub network, which is also a known issue.
    """
    num_nodes: Incomplete
    num_ops_per_node: Incomplete
    num_predecessors: Incomplete
    preprocessor: Incomplete
    ops: Incomplete
    postprocessor: Incomplete
    concat_dim: Incomplete
    op_names: Incomplete
    output_node_indices: Incomplete
    label: Incomplete
    def __init__(self, op_factory: list[CellOpFactory] | dict[str, CellOpFactory], num_nodes: int, num_ops_per_node: int, num_predecessors: int, preprocessor: Any, postprocessor: Any, concat_dim: int, memo: dict, mutate_kwargs: dict, label: str) -> None: ...
    def search_space_spec(self) -> dict[str, ParameterSpec]: ...
    def resample(self, memo):
        """Random choose one path if label is not found in memo."""
    def export(self, memo):
        """Randomly choose one to export."""
    def forward(self, *inputs: list[torch.Tensor] | torch.Tensor) -> tuple[torch.Tensor, ...] | torch.Tensor: ...
    @classmethod
    def mutate(cls, module, name, memo, mutate_kwargs):
        """
        Mutate only handles cells of specific configurations (e.g., with loose end).
        Fallback to the default mutate if the cell is not handled here.
        """
