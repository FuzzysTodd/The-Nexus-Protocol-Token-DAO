import dataclasses
import enum
import torch
import torch._C._onnx as _C_onnx
from _typeshed import Incomplete
from torch import _C
from torch.onnx import _experimental, utils as utils
from torch.onnx._globals import GLOBALS as GLOBALS
from torch.onnx._internal import onnx_proto_utils as onnx_proto_utils
from torch.types import Number as Number
from typing import Any, Dict, List, Mapping, Sequence, Set, Tuple

class OnnxBackend(enum.Enum):
    """Enum class for ONNX backend used for export verification."""
    REFERENCE: str
    ONNX_RUNTIME_CPU: str
    ONNX_RUNTIME_CUDA: str

@dataclasses.dataclass
class VerificationOptions:
    """Options for ONNX export verification.

    Attributes:
        flatten: If True, unpack nested list/tuple/dict inputs into a flattened list of
            Tensors for ONNX. Set this to False if nested structures are to be preserved
            for ONNX, which is usually the case with exporting ScriptModules. Default True.
        ignore_none: Whether to ignore None type in torch output, which is usually the
            case with tracing. Set this to False, if torch output should keep None type,
            which is usually the case with exporting ScriptModules. Default to True.
        check_shape: Whether to check the shapes between PyTorch and ONNX Runtime outputs
            are exactly the same. Set this to False to allow output shape broadcasting.
            Default to True.
        check_dtype: Whether to check the dtypes between PyTorch and ONNX Runtime outputs
            are consistent. Default to True.
        backend: ONNX backend for verification. Default to OnnxBackend.ONNX_RUNTIME_CPU.
        rtol: relative tolerance in comparison between ONNX and PyTorch outputs.
        atol: absolute tolerance in comparison between ONNX and PyTorch outputs.
        remained_onnx_input_idx: If provided, only the specified inputs will be passed
            to the ONNX model. Supply a list when there are unused inputs in the model.
            Since unused inputs will be removed in the exported ONNX model, supplying
            all inputs will cause an error on unexpected inputs. This parameter tells
            the verifier which inputs to pass into the ONNX model.
        acceptable_error_percentage: acceptable percentage of element mismatches in comparison.
            It should be a float of value between 0.0 and 1.0.
    """
    flatten: bool = ...
    ignore_none: bool = ...
    check_shape: bool = ...
    check_dtype: bool = ...
    backend: OnnxBackend = ...
    rtol: float = ...
    atol: float = ...
    remained_onnx_input_idx: Sequence[int] | None = ...
    acceptable_error_percentage: float | None = ...
    def __init__(self, flatten, ignore_none, check_shape, check_dtype, backend, rtol, atol, remained_onnx_input_idx, acceptable_error_percentage) -> None: ...

class _GraphDiff:
    """A class to represent the difference between two graphs."""
    graph_a: Incomplete
    graph_b: Incomplete
    def __init__(self, graph_a: _C.Graph, graph_b: _C.Graph) -> None:
        """Construct a _GraphDiff object.

        Args:
            graph_a (_C.Graph): First graph to compare.
            graph_b (_C.Graph): Second graph to compare.
        """
    def diff_report(self) -> str:
        """Return a string representation of the graph difference.

        The report shows the first pair of nodes that diverges. It also shows the source
        location of the pair of nodes.

        Returns:
            graph_diff_report (str): A string representation of the graph difference.
        """

def check_export_model_diff(model: torch.nn.Module | torch.jit.ScriptModule, test_input_groups: Sequence[Tuple[Tuple[Any, ...], Mapping[str, Any]]], export_options: _experimental.ExportOptions | None = None) -> str:
    """Verify exported model discrepancy between different groups of inputs.

    A graph is exported for each group of inputs. The exported graphs are then compared
    to each other, and discrepancies of first pair of nodes are reported. This function
    first checks the jit graph. If no discrepancies were found, it then checks the onnx
    graph.

    Unless otherwise specified, the jit/ONNX graph is expected to be the same, regardless
    of the inputs used for exporting. A discrepancy implies the graph exported is
    not accurate when run on other groups of inputs, which will typically results in
    runtime errors or mismatching output.

    Args:
        model (torch.nn.Module or torch.jit.ScriptModule): The model to be exported.
        test_input_groups (Sequence[Tuple[Tuple[Any, ...], Mapping[str, Any]]]): A sequence
            of input groups to be used to export the model. Each input group is a pair of
            (args, kwargs).
        export_options (_experimental.ExportOptions, optional): An _experimental.ExportOptions
            object that controls the export behavior.

    Returns:
        str: A string containing the diff of the exported models.
    """
def verify(model: _ModelType, input_args: _InputArgsType, input_kwargs: _InputKwargsType | None = None, do_constant_folding: bool = True, dynamic_axes: Mapping[str, Mapping[int, str] | Mapping[str, Sequence[int]]] | None = None, input_names: Sequence[str] | None = None, output_names: Sequence[str] | None = None, training: _C_onnx.TrainingMode = ..., opset_version: int | None = None, keep_initializers_as_inputs: bool = True, verbose: bool = False, fixed_batch_size: bool = False, use_external_data: bool = False, additional_test_inputs: Sequence[_InputArgsType] | None = None, options: VerificationOptions | None = None):
    """Verify model export to ONNX against original PyTorch model.

    Args:
        model (torch.nn.Module or torch.jit.ScriptModule): See :func:`torch.onnx.export`.
        input_args (tuple): See :func:`torch.onnx.export`.
        input_kwargs (dict): See :func:`torch.onnx.export`.
        do_constant_folding (bool, optional): See :func:`torch.onnx.export`.
        dynamic_axes (dict, optional): See :func:`torch.onnx.export`.
        input_names (list, optional): See :func:`torch.onnx.export`.
        output_names (list, optional): See :func:`torch.onnx.export`.
        training (torch.onnx.TrainingMode): See :func:`torch.onnx.export`.
        opset_version (int, optional): See :func:`torch.onnx.export`.
        keep_initializers_as_inputs (bool, optional): See :func:`torch.onnx.export`.
        verbose (bool, optional): See :func:`torch.onnx.export`.
        fixed_batch_size (bool, optional): Legacy argument, used only by rnn test cases.
        use_external_data (bool, optional): Explicitly specify whether to export the
            model with external data.
        additional_test_inputs (list, optional): List of tuples. Each tuple is a group of
            input arguments to test. Currently only *args are supported.
        options (_VerificationOptions, optional): A _VerificationOptions object that
            controls the verification behavior.

    Raises:
        AssertionError: if outputs from ONNX model and PyTorch model are not
            equal up to specified precision.
        ValueError: if arguments provided are invalid.
    """
def verify_aten_graph(graph: torch.Graph, input_args: Tuple[Any, ...], export_options: _experimental.ExportOptions, params_dict: Dict[str, Any] | None = None, verification_options: VerificationOptions | None = None) -> Tuple[AssertionError | None, torch.Graph, _OutputsType, _OutputsType]: ...

class GraphInfoPrettyPrinter:
    graph_info: GraphInfo | None
    upper_printer: GraphInfoPrettyPrinter | None
    lower_printer: GraphInfoPrettyPrinter | None
    graph_str_lambdas: Mapping[int, str]
    connector_str_lambdas: Mapping[int, str]
    children_str_lambdas: Mapping[int, str]
    def __init__(self, graph_info: GraphInfo | None) -> None: ...
    def pretty_print(self) -> None: ...

class OnnxTestCaseRepro:
    repro_dir: Incomplete
    def __init__(self, repro_dir) -> None: ...
    @classmethod
    def create_test_case_repro(cls, proto: bytes, inputs, outputs, dir: str, name: str | None = None):
        '''Create a repro under "{dir}/test_{name}" for an ONNX test case.

        The test case contains the model and the inputs/outputs data. The directory
        structure is as follows:

        dir
        ├── test_<name>
        │   ├── model.onnx
        │   └── test_data_set_0
        │       ├── input_0.pb
        │       ├── input_1.pb
        │       ├── output_0.pb
        │       └── output_1.pb

        Args:
            proto: ONNX model proto.
            inputs: Inputs to the model.
            outputs: Outputs of the model.
            dir: Directory to save the repro.
            name: Name of the test case. If not specified, a name based on current time
                will be generated.
        Returns:
            Path to the repro.
        '''
    def validate(self, options: VerificationOptions):
        """Run the ONNX test case with options.backend, and compare with the expected outputs.

        Args:
            options: Options for validation.

        Raise:
            AssertionError: if outputs from options.backend and expected outputs are not
                equal up to specified precision.
        """

@dataclasses.dataclass
class GraphInfo:
    """GraphInfo contains validation information of a TorchScript graph and its converted ONNX graph."""
    graph: torch.Graph
    input_args: Tuple[Any, ...]
    params_dict: Dict[str, Any]
    export_options: _experimental.ExportOptions = ...
    mismatch_error: AssertionError | None = ...
    pt_outs: Sequence[_NumericType] | None = ...
    upper_graph_info: GraphInfo | None = ...
    lower_graph_info: GraphInfo | None = ...
    id: str = ...
    def clear(self) -> None:
        """Clear states and results of previous verification."""
    def pretty_print_tree(self) -> None:
        """Pretty print `GraphInfo` tree.

        Each node represents a subgraph, showing the number of nodes in the subgraph and
        a check mark if the subgraph has output mismatch between torch and ONNX.

        The id of the subgraph is shown under the node. The `GraphInfo` object for any
        subgraph can be retrieved by calling `graph_info.find_partition(id)`.

        Example::

            ==================================== Tree: =====================================
            5 X   __2 X    __1 ✓
            id:  |  id: 0 |  id: 00
                 |        |
                 |        |__1 X (aten::relu)
                 |           id: 01
                 |
                 |__3 X    __1 ✓
                    id: 1 |  id: 10
                          |
                          |__2 X     __1 X (aten::relu)
                             id: 11 |  id: 110
                                    |
                                    |__1 ✓
                                       id: 111
            =========================== Mismatch leaf subgraphs: ===========================
            ['01', '110']
            ============================= Mismatch node kinds: =============================
            {'aten::relu': 2}

        """
    def pretty_print_mismatch(self, graph: bool = False):
        """Pretty print details of the mismatch between torch and ONNX.

        Args:
            graph: If True, print the ATen JIT graph and ONNX graph.
        """
    def has_mismatch(self) -> bool:
        """Return True if the subgraph has output mismatch between torch and ONNX."""
    def essential_node_count(self) -> int:
        """Return the number of nodes in the subgraph excluding those in `_EXCLUDED_NODE_KINDS`."""
    def essential_node_kinds(self) -> Set[str]:
        """Return the set of node kinds in the subgraph excluding those in `_EXCLUDED_NODE_KINDS`."""
    def all_mismatch_leaf_graph_info(self) -> List['GraphInfo']:
        """Return a list of all leaf `GraphInfo` objects that have mismatch."""
    def find_partition(self, id: str) -> GraphInfo | None:
        """Find the `GraphInfo` object with the given id."""
    def export_repro(self, repro_dir: str | None = None, name: str | None = None) -> str:
        '''Export the subgraph to ONNX along with the input/output data for repro.

        The repro directory will contain the following files::

            dir
            ├── test_<name>
            │   ├── model.onnx
            │   └── test_data_set_0
            │       ├── input_0.pb
            │       ├── input_1.pb
            │       ├── output_0.pb
            │       └── output_1.pb

        Args:
            repro_dir: The directory to export the repro files to. Defaults to current
                working directory if None.
            name: An optional name for the test case folder: "test_{name}".

        Returns:
            The path to the exported repro directory.
        '''
    def verify_export(self, options: VerificationOptions) -> Tuple[AssertionError | None, torch.Graph, _OutputsType, _OutputsType]:
        """
        Verify the export from TorchScript IR graph to ONNX.

        Export the TorchScript IR graph to ONNX, with the inputs, parameters and export
        options recorded in this object. Then verify the exported ONNX graph against
        the original TorchScript IR graph under the provided verification options.

        Args:
            options: The verification options.

        Returns:
            error: The AssertionError raised during the verification. Returns None if no
            error is raised.
            onnx_graph: The exported ONNX graph in TorchScript IR format.
            onnx_outs: The outputs from running exported ONNX model under the onnx
            backend in `options`.
            pt_outs: The outputs from running the TorchScript IR graph.
        """
    def find_mismatch(self, options: VerificationOptions | None = None):
        """
        Find all mismatches between the TorchScript IR graph and the exported onnx model.

        Binary searches the model graph to find the minimal subgraph that exhibits the
        mismatch. A `GraphInfo` object is created for each subgraph, recording the test
        inputs and export options, as well as the validation results.

        Args:
            options: The verification options.
        """
    def __init__(self, graph, input_args, params_dict, export_options, id, _EXCLUDED_NODE_KINDS) -> None: ...

def find_mismatch(model: torch.nn.Module | torch.jit.ScriptModule, input_args: Tuple[Any, ...], do_constant_folding: bool = True, training: _C_onnx.TrainingMode = ..., opset_version: int | None = None, keep_initializers_as_inputs: bool = True, verbose: bool = False, options: VerificationOptions | None = None) -> GraphInfo:
    '''Find all mismatches between the original model and the exported model.

    Experimental. The API is subject to change.

    This tool helps debug the mismatch between the original PyTorch model and exported
    ONNX model. It binary searches the model graph to find the minimal subgraph that
    exhibits the mismatch.

    Args:
        model: The model to be exported.
        input_args: The input arguments to the model.
        do_constant_folding: Same as `do_constant_folding` in :func:`torch.onnx.export`.
        training: Same as `training` in :func:`torch.onnx.export`.
        opset_version: Same as `opset_version` in :func:`torch.onnx.export`.
        keep_initializers_as_inputs: Same as `keep_initializers_as_inputs` in :func:`torch.onnx.export`.
        verbose: Same as `verbose` in :func:`torch.onnx.export`.
        options: The options for the mismatch verification.

    Returns:
        A GraphInfo object that contains the mismatch information.

    Example::

        >>> import torch
        >>> import torch.onnx.verification
        >>> torch.manual_seed(0)
        >>> opset_version = 15
        >>> # Define a custom symbolic function for aten::relu.
        >>> # The custom symbolic function is incorrect, which will result in mismatches.
        >>> def incorrect_relu_symbolic_function(g, self):
        ...     return self
        >>> torch.onnx.register_custom_op_symbolic(
        ...     "aten::relu",
        ...     incorrect_relu_symbolic_function,
        ...     opset_version=opset_version,
        ... )
        >>> class Model(torch.nn.Module):
        ...     def __init__(self):
        ...         super().__init__()
        ...         self.layers = torch.nn.Sequential(
        ...             torch.nn.Linear(3, 4),
        ...             torch.nn.ReLU(),
        ...             torch.nn.Linear(4, 5),
        ...             torch.nn.ReLU(),
        ...             torch.nn.Linear(5, 6),
        ...         )
        ...     def forward(self, x):
        ...         return self.layers(x)
        >>> # xdoctest: +REQUIRES(env:TORCH_DOCTEST_ONNX)
        >>> graph_info = torch.onnx.verification.find_mismatch(
        ...     Model(),
        ...     (torch.randn(2, 3),),
        ...     opset_version=opset_version,
        ... )
        ===================== Mismatch info for graph partition : ======================
        ================================ Mismatch error ================================
        Tensor-likes are not close!
        Mismatched elements: 12 / 12 (100.0%)
        Greatest absolute difference: 0.2328854203224182 at index (1, 2) (up to 1e-07 allowed)
        Greatest relative difference: 0.699536174352349 at index (1, 3) (up to 0.001 allowed)
        ==================================== Tree: =====================================
        5 X   __2 X    __1 ✓
        id:  |  id: 0 |  id: 00
             |        |
             |        |__1 X (aten::relu)
             |           id: 01
             |
             |__3 X    __1 ✓
                id: 1 |  id: 10
                      |
                      |__2 X     __1 X (aten::relu)
                         id: 11 |  id: 110
                                |
                                |__1 ✓
                                   id: 111
        =========================== Mismatch leaf subgraphs: ===========================
        [\'01\', \'110\']
        ============================= Mismatch node kinds: =============================
        {\'aten::relu\': 2}

    '''
