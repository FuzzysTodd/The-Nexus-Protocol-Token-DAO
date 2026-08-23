import torch
import torch.nn as nn
from .choice import ChosenInputs as ChosenInputs, InputChoice as InputChoice, LayerChoice as LayerChoice
from .layers import ModuleList as ModuleList
from .mutation_utils import generate_new_label as generate_new_label
from _typeshed import Incomplete
from typing import Callable, Dict, List, Tuple
from typing_extensions import Literal

class _ListIdentity(nn.Identity):
    def forward(self, x: List[torch.Tensor]) -> List[torch.Tensor]: ...

class _DefaultPostprocessor(nn.Module):
    def forward(self, this_cell: torch.Tensor, prev_cell: List[torch.Tensor]) -> torch.Tensor: ...

CellOpFactory: Incomplete

def create_cell_op_candidates(op_candidates, node_index, op_index, chosen) -> Tuple[Dict[str, nn.Module], bool]: ...
def preprocess_cell_inputs(num_predecessors: int, *inputs: List[torch.Tensor] | torch.Tensor) -> List[torch.Tensor]: ...

class Cell(nn.Module):
    '''
    Cell structure that is popularly used in NAS literature.

    Find the details in:

    * `Neural Architecture Search with Reinforcement Learning <https://arxiv.org/abs/1611.01578>`__.
    * `Learning Transferable Architectures for Scalable Image Recognition <https://arxiv.org/abs/1707.07012>`__.
    * `DARTS: Differentiable Architecture Search <https://arxiv.org/abs/1806.09055>`__

    `On Network Design Spaces for Visual Recognition <https://arxiv.org/abs/1905.13214>`__
    is a good summary of how this structure works in practice.

    A cell consists of multiple "nodes". Each node is a sum of multiple operators. Each operator is chosen from
    ``op_candidates``, and takes one input from previous nodes and predecessors. Predecessor means the input of cell.
    The output of cell is the concatenation of some of the nodes in the cell (by default all the nodes).

    Two examples of searched cells are illustrated in the figure below.
    In these two cells, ``op_candidates`` are series of convolutions and pooling operations.
    ``num_nodes_per_node`` is set to 2. ``num_nodes`` is set to 5. ``merge_op`` is ``loose_end``.
    Assuming nodes are enumerated from bottom to top, left to right,
    ``output_node_indices`` for the normal cell is ``[2, 3, 4, 5, 6]``.
    For the reduction cell, it\'s ``[4, 5, 6]``.
    Please take a look at this
    `review article <https://sh-tsang.medium.com/review-nasnet-neural-architecture-search-network-image-classification-23139ea0425d>`__
    if you are interested in details.

    .. image:: ../../../img/nasnet_cell.png
       :width: 900
       :align: center

    Here is a glossary table, which could help better understand the terms used above:

    .. list-table::
        :widths: 25 75
        :header-rows: 1

        * - Name
          - Brief Description
        * - Cell
          - A cell consists of ``num_nodes`` nodes.
        * - Node
          - A node is the **sum** of ``num_ops_per_node`` operators.
        * - Operator
          - Each operator is independently chosen from a list of user-specified candidate operators.
        * - Operator\'s input
          - Each operator has one input, chosen from previous nodes as well as predecessors.
        * - Predecessors
          - Input of cell. A cell can have multiple predecessors. Predecessors are sent to *preprocessor* for preprocessing.
        * - Cell\'s output
          - Output of cell. Usually concatenation of some nodes (possibly all nodes) in the cell. Cell\'s output,
            along with predecessors, are sent to *postprocessor* for postprocessing.
        * - Preprocessor
          - Extra preprocessing to predecessors. Usually used in shape alignment (e.g., predecessors have different shapes).
            By default, do nothing.
        * - Postprocessor
          - Extra postprocessing for cell\'s output. Usually used to chain cells with multiple Predecessors
            (e.g., the next cell wants to have the outputs of both this cell and previous cell as its input).
            By default, directly use this cell\'s output.

    .. tip::

        It\'s highly recommended to make the candidate operators have an output of the same shape as input.
        This is because, there can be dynamic connections within cell. If there\'s shape change within operations,
        the input shape of the subsequent operation becomes unknown.
        In addition, the final concatenation could have shape mismatch issues.

    Parameters
    ----------
    op_candidates : list of module or function, or dict
        A list of modules to choose from, or a function that accepts current index and optionally its input index, and returns a module.
        For example, (2, 3, 0) means the 3rd op in the 2nd node, accepts the 0th node as input.
        The index are enumerated for all nodes including predecessors from 0.
        When first created, the input index is ``None``, meaning unknown.
        Note that in graph execution engine, support of function in ``op_candidates`` is limited.
        Please also note that, to make :class:`Cell` work with one-shot strategy,
        ``op_candidates``, in case it\'s a callable, should not depend on the second input argument,
        i.e., ``op_index`` in current node.
    num_nodes : int
        Number of nodes in the cell.
    num_ops_per_node: int
        Number of operators in each node. The output of each node is the sum of all operators in the node. Default: 1.
    num_predecessors : int
        Number of inputs of the cell. The input to forward should be a list of tensors. Default: 1.
    merge_op : "all", or "loose_end"
        If "all", all the nodes (except predecessors) will be concatenated as the cell\'s output, in which case, ``output_node_indices``
        will be ``list(range(num_predecessors, num_predecessors + num_nodes))``.
        If "loose_end", only the nodes that have never been used as other nodes\' inputs will be concatenated to the output.
        Predecessors are not considered when calculating unused nodes.
        Details can be found in `NDS paper <https://arxiv.org/abs/1905.13214>`__. Default: all.
    preprocessor : callable
        Override this if some extra transformation on cell\'s input is intended.
        It should be a callable (``nn.Module`` is also acceptable) that takes a list of tensors which are predecessors,
        and outputs a list of tensors, with the same length as input.
        By default, it does nothing to the input.
    postprocessor : callable
        Override this if customization on the output of the cell is intended.
        It should be a callable that takes the output of this cell, and a list which are predecessors.
        Its return type should be either one tensor, or a tuple of tensors.
        The return value of postprocessor is the return value of the cell\'s forward.
        By default, it returns only the output of the current cell.
    concat_dim : int
        The result will be a concatenation of several nodes on this dim. Default: 1.
    label : str
        Identifier of the cell. Cell sharing the same label will semantically share the same choice.

    Examples
    --------
    Choose between conv2d and maxpool2d.
    The cell have 4 nodes, 1 op per node, and 2 predecessors.

    >>> cell = nn.Cell([nn.Conv2d(32, 32, 3, padding=1), nn.MaxPool2d(3, padding=1)], 4, 1, 2)

    In forward:

    >>> cell([input1, input2])

    The "list bracket" can be omitted:

    >>> cell(only_input)                    # only one input
    >>> cell(tensor1, tensor2, tensor3)     # multiple inputs

    Use ``merge_op`` to specify how to construct the output.
    The output will then have dynamic shape, depending on which input has been used in the cell.

    >>> cell = nn.Cell([nn.Conv2d(32, 32, 3), nn.MaxPool2d(3)], 4, 1, 2, merge_op=\'loose_end\')
    >>> cell_out_channels = len(cell.output_node_indices) * 32

    The op candidates can be callable that accepts node index in cell, op index in node, and input index.

    >>> cell = nn.Cell([
    ...     lambda node_index, op_index, input_index: nn.Conv2d(32, 32, 3, stride=2 if input_index < 1 else 1),
    ... ], 4, 1, 2)

    Predecessor example: ::

        class Preprocessor:
            def __init__(self):
                self.conv1 = nn.Conv2d(16, 32, 1)
                self.conv2 = nn.Conv2d(64, 32, 1)

            def forward(self, x):
                return [self.conv1(x[0]), self.conv2(x[1])]

        cell = nn.Cell([nn.Conv2d(32, 32, 3), nn.MaxPool2d(3)], 4, 1, 2, preprocessor=Preprocessor())
        cell([torch.randn(1, 16, 48, 48), torch.randn(1, 64, 48, 48)])  # the two inputs will be sent to conv1 and conv2 respectively

    Warnings
    --------
    :class:`Cell` is not supported in :ref:`graph-based execution engine <graph-based-execution-engine>`.

    Attributes
    ----------
    output_node_indices : list of int
        An attribute that contains indices of the nodes concatenated to the output (a list of integers).

        When the cell is first instantiated in the base model, or when ``merge_op`` is ``all``,
        ``output_node_indices`` must be ``range(num_predecessors, num_predecessors + num_nodes)``.

        When ``merge_op`` is ``loose_end``, ``output_node_indices`` is useful to compute the shape of this cell\'s output,
        because the output shape depends on the connection in the cell, and which nodes are "loose ends" depends on mutation.

    op_candidates_factory : CellOpFactory or None
        If the operations are created with a factory (callable), this is to be set with the factory.
        One-shot algorithms will use this to make each node a cartesian product of operations and inputs.
    '''
    preprocessor: Incomplete
    ops: Incomplete
    inputs: Incomplete
    postprocessor: Incomplete
    num_nodes: Incomplete
    num_ops_per_node: Incomplete
    num_predecessors: Incomplete
    merge_op: Incomplete
    output_node_indices: Incomplete
    concat_dim: Incomplete
    op_candidates_factory: Incomplete
    def __init__(self, op_candidates: Callable[[], List[nn.Module]] | List[nn.Module] | List[CellOpFactory] | Dict[str, nn.Module] | Dict[str, CellOpFactory], num_nodes: int, num_ops_per_node: int = 1, num_predecessors: int = 1, merge_op: Literal['all', 'loose_end'] = 'all', preprocessor: Callable[[List[torch.Tensor]], List[torch.Tensor]] | None = None, postprocessor: Callable[[torch.Tensor, List[torch.Tensor]], Tuple[torch.Tensor, ...] | torch.Tensor] | None = None, concat_dim: int = 1, *, label: str | None = None) -> None: ...
    @property
    def label(self): ...
    def forward(self, *inputs: List[torch.Tensor] | torch.Tensor) -> Tuple[torch.Tensor, ...] | torch.Tensor:
        """Forward propagation of cell.

        Parameters
        ----------
        inputs
            Can be a list of tensors, or several tensors.
            The length should be equal to ``num_predecessors``.

        Returns
        -------
        Tuple[torch.Tensor] | torch.Tensor
            The return type depends on the output of ``postprocessor``.
            By default, it's the output of ``merge_op``, which is a contenation (on ``concat_dim``)
            of some of (possibly all) the nodes' outputs in the cell.
        """
