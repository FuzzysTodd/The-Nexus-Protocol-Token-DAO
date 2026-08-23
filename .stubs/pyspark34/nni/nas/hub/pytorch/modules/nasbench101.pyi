import torch.nn as nn
from _typeshed import Incomplete
from nni.nas.execution.common import Model
from nni.nas.mutable import Mutator
from nni.nas.nn.pytorch.mutation_utils import Mutable
from typing import Callable, Dict, List

__all__ = ['NasBench101Cell', 'NasBench101Mutator']

class _NasBench101CellFixed(nn.Module):
    """
    The fixed version of NAS-Bench-101 Cell, used in python-version execution engine.
    """
    connection_matrix: Incomplete
    hidden_features: Incomplete
    num_nodes: Incomplete
    in_features: Incomplete
    out_features: Incomplete
    projections: Incomplete
    ops: Incomplete
    def __init__(self, operations: List[Callable[[int], nn.Module]], adjacency_list: List[List[int]], in_features: int, out_features: int, num_nodes: int, projection: Callable[[int, int], nn.Module]) -> None: ...
    @staticmethod
    def build_connection_matrix(adjacency_list, num_nodes): ...
    def forward(self, inputs): ...

class NasBench101Cell(Mutable):
    '''
    Cell structure that is proposed in NAS-Bench-101.

    Proposed by `NAS-Bench-101: Towards Reproducible Neural Architecture Search <http://proceedings.mlr.press/v97/ying19a/ying19a.pdf>`__.

    This cell is usually used in evaluation of NAS algorithms because there is a "comprehensive analysis" of this search space
    available, which includes a full architecture-dataset that "maps 423k unique architectures to metrics
    including run time and accuracy". You can also use the space in your own space design, in which scenario it should be possible
    to leverage results in the benchmark to narrow the huge space down to a few efficient architectures.

    The space of this cell architecture consists of all possible directed acyclic graphs on no more than ``max_num_nodes`` nodes,
    where each possible node (other than IN and OUT) has one of ``op_candidates``, representing the corresponding operation.
    Edges connecting the nodes can be no more than ``max_num_edges``.
    To align with the paper settings, two vertices specially labeled as operation IN and OUT, are also counted into
    ``max_num_nodes`` in our implementaion, the default value of ``max_num_nodes`` is 7 and ``max_num_edges`` is 9.

    Input of this cell should be of shape :math:`[N, C_{in}, *]`, while output should be :math:`[N, C_{out}, *]`. The shape
    of each hidden nodes will be first automatically computed, depending on the cell structure. Each of the ``op_candidates``
    should be a callable that accepts computed ``num_features`` and returns a ``Module``. For example,

    .. code-block:: python

        def conv_bn_relu(num_features):
            return nn.Sequential(
                nn.Conv2d(num_features, num_features, 1),
                nn.BatchNorm2d(num_features),
                nn.ReLU()
            )

    The output of each node is the sum of its input node feed into its operation, except for the last node (output node),
    which is the concatenation of its input *hidden* nodes, adding the *IN* node (if IN and OUT are connected).

    When input tensor is added with any other tensor, there could be shape mismatch. Therefore, a projection transformation
    is needed to transform the input tensor. In paper, this is simply a Conv1x1 followed by BN and ReLU. The ``projection``
    parameters accepts ``in_features`` and ``out_features``, returns a ``Module``. This parameter has no default value,
    as we hold no assumption that users are dealing with images. An example for this parameter is,

    .. code-block:: python

        def projection_fn(in_features, out_features):
            return nn.Conv2d(in_features, out_features, 1)

    Parameters
    ----------
    op_candidates : list of callable
        Operation candidates. Each should be a function accepts number of feature, returning nn.Module.
    in_features : int
        Input dimension of cell.
    out_features : int
        Output dimension of cell.
    projection : callable
        Projection module that is used to preprocess the input tensor of the whole cell.
        A callable that accept input feature and output feature, returning nn.Module.
    max_num_nodes : int
        Maximum number of nodes in the cell, input and output included. At least 2. Default: 7.
    max_num_edges : int
        Maximum number of edges in the cell. Default: 9.
    label : str
        Identifier of the cell. Cell sharing the same label will semantically share the same choice.

    Warnings
    --------
    :class:`NasBench101Cell` is not supported in :ref:`graph-based execution engine <graph-based-execution-engine>`.
    '''
    @classmethod
    def create_fixed_module(cls, op_candidates: Dict[str, Callable[[int], nn.Module]] | List[Callable[[int], nn.Module]], in_features: int, out_features: int, projection: Callable[[int, int], nn.Module], max_num_nodes: int = 7, max_num_edges: int = 9, label: str | None = None): ...
    num_nodes: Incomplete
    max_num_nodes: Incomplete
    max_num_edges: Incomplete
    hidden_features: Incomplete
    projections: Incomplete
    ops: Incomplete
    inputs: Incomplete
    def __init__(self, op_candidates: Dict[str, Callable[[int], nn.Module]] | List[Callable[[int], nn.Module]], in_features: int, out_features: int, projection: Callable[[int, int], nn.Module], max_num_nodes: int = 7, max_num_edges: int = 9, label: str | None = None) -> None: ...
    @property
    def label(self): ...
    def forward(self, x):
        """
        The forward of input choice is simply selecting first on all choices.
        It shouldn't be called directly by users in most cases.
        """

class NasBench101Mutator(Mutator):
    def __init__(self, label: str) -> None: ...
    @staticmethod
    def candidates(node): ...
    @staticmethod
    def number_of_chosen(node): ...
    def mutate(self, model: Model): ...
    def dry_run(self, model): ...
