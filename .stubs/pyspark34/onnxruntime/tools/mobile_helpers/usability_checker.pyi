import logging
import onnx
import pathlib
from ..onnx_model_utils import get_producer_consumer_maps as get_producer_consumer_maps, is_fixed_size_tensor as is_fixed_size_tensor, iterate_graph_per_graph_func as iterate_graph_per_graph_func, iterate_graph_per_node_func as iterate_graph_per_node_func, optimize_model as optimize_model
from _typeshed import Incomplete
from enum import IntEnum

class _SupportedOpsChecker:
    """
    Class to process the md file with list of supported ops and caveats for an execution provider.
    e.g. /tools/ci_build/github/android/nnapi_supported_ops.md
         /tools/ci_build/github/apple/coreml_supported_ops.md
    """
    def __init__(self, filename) -> None: ...
    def is_op_supported(self, node): ...
    def get_caveats(self): ...

class PartitioningInfo:
    class TryWithEP(IntEnum):
        NO: Incomplete
        MAYBE: Incomplete
        YES: int
    num_nodes: int
    num_supported_nodes: int
    num_partitions: int
    num_nodes_in_subgraphs: int
    supported_ops_checker: Incomplete
    supported_groups: Incomplete
    unsupported_ops: Incomplete
    nodes_unsupported_due_to_op: int
    nodes_unsupported_due_to_dynamic_input: int
    def __init__(self) -> None: ...
    def suitability(self): ...
    def dump_analysis(self, logger: logging.Logger, ep_name: str):
        """
        Analyze the partitioning information and log the analysis
        :param logger: Logger to use
        :param ep_name: Execution provider name to use in the log messages
        """

def check_partitioning(graph: onnx.GraphProto, supported_ops_checker: _SupportedOpsChecker, require_fixed_input_sizes: bool = False, value_info: dict | None = None):
    """
    Estimate the partitions the graph will be split into for nodes that is_node_supported_fn returns true for.

    The check on whether a node is supported is purely based on the operator type. Additional limitations
    (e.g. NNAPI EP only supports 2D Conv) are not checked, so partitions may not be 100% accurate. The limitations
    for operators in the partitions are printed so the user can manually check.
    :param graph: Graph to process
    :param supported_ops_checker: Checker with info on supported ops.
    :param require_fixed_input_sizes: If True, require that the inputs to a potentially supported node are
                                       fixed size tensors for it to be considered as supported.
                                       If True, onnx.shape_inference.infer_shapes should have been run on the model
                                       to populate the shape information.
    :param value_info: Map of value name to ValueInfoProto. Required if require_fixed_input_sizes is True to lookup
                       the shape of a value.
    :return PartitioningInfo instance with details
    """
def check_nnapi_partitions(model, value_info: dict | None = None): ...
def check_coreml_partitions(model, value_info: dict | None = None): ...
def check_shapes(graph: onnx.GraphProto, logger: logging.Logger | None = None):
    """
    Check the shapes of graph inputs, values and graph outputs to determine if they have static or dynamic sizes.
    NNAPI and CoreML do not support dynamically sized values.
    :param graph: Graph to check. If shape inferencing has been run the checks on values will be meaningful.
    :param logger: Optional logger for diagnostic information.
    :return: Tuple of List of inputs with dynamic shapes, Number of dynamic values found
    """
def checker(model_path, logger: logging.Logger): ...
def analyze_model(model_path: pathlib.Path, skip_optimize: bool = False, logger: logging.Logger | None = None):
    """
    Analyze the provided model to determine if it's likely to work well with the NNAPI or CoreML Execution Providers
    :param model_path: Model to analyze.
    :param skip_optimize: Skip optimizing to BASIC level before checking. When exporting to ORT format we will do this
                          optimization..
    :param logger: Logger for output
    :return: True if either the NNAPI or CoreML Execution Providers may work well with this model.
    """
def parse_args(): ...
def run_analyze_model() -> None: ...
