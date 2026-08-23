import logging
import onnx
import pathlib
from ..onnx_model_utils import get_opsets_imported as get_opsets_imported
from ..reduced_build_config_parser import parse_config as parse_config
from _typeshed import Incomplete

cpp_to_tensorproto_type: Incomplete
tensorproto_type_to_cpp: Incomplete

def check_graph(graph, opsets, required_ops, global_types, special_types, unsupported_ops, logger):
    """
    Check the graph and any subgraphs for usage of types or operators which we know are not supported.
    :param graph: Graph to process.
    :param opsets: Map of domain to opset version that the model imports.
    :param required_ops: Operators that are included in the pre-built package.
    :param global_types: Types globally enabled in the pre-built package.
    :param special_types: Types that are always enabled for a subset of operators and are _usually_ supported but are
                          not guaranteed to be. We would need to add a lot of infrastructure to know for sure so
                          currently we treat them as supported.
    :param unsupported_ops: Set of unsupported operators that were found.
    :param logger: Logger for diagnostic output.
    :return: Returns whether the graph uses unsupported operators or types.
    """
def get_default_config_path(): ...
def run_check_with_model(model_with_type_info: onnx.ModelProto, mobile_pkg_build_config: pathlib.Path, logger: logging.Logger):
    """
    Check if an ONNX model can be used with the ORT Mobile pre-built package.
    :param model_with_type_info: ONNX model that has had ONNX shape inferencing run on to add type/shape information.
    :param mobile_pkg_build_config: Configuration file used to build the ORT Mobile package.
    :param logger: Logger for output
    :return: True if supported
    """
def run_check(model_path: pathlib.Path, mobile_pkg_build_config: pathlib.Path, logger: logging.Logger):
    """
    Check if an ONNX model will be able to be used with the ORT Mobile pre-built package.
    :param model_path: Path to ONNX model.
    :param mobile_pkg_build_config: Configuration file used to build the ORT Mobile package.
    :param logger: Logger for output
    :return: True if supported
    """
def main() -> None: ...
