import logging
import onnx
import onnxruntime as ort
import pathlib

def iterate_graph_per_node_func(graph, per_node_func, **func_args) -> None:
    """
    Iterate the graph including subgraphs calling the per_node_func for each node.
    :param graph: Graph to iterate
    :param per_node_func: Function to call for each node. Signature is fn(node: onnx:NodeProto, **kwargs)
    :param func_args: The keyword args to pass through.
    """
def iterate_graph_per_graph_func(graph, per_graph_func, **func_args) -> None:
    """
    Iterate the graph including subgraphs calling the per_graph_func for each Graph.
    :param graph: Graph to iterate
    :param per_graph_func: Function to call for each graph. Signature is fn(graph: onnx:GraphProto, **kwargs)
    :param func_args: The keyword args to pass through.
    """
def get_opsets_imported(model: onnx.ModelProto):
    """
    Get the opsets imported by the model
    :param model: Model to check.
    :return: Map of domain to opset.
    """
def update_onnx_opset(model_path: pathlib.Path, opset: int, out_path: pathlib.Path | None = None, logger: logging.Logger | None = None):
    """
    Helper to update the opset of a model using onnx version_converter. Target opset must be greater than current opset.
    :param model_path: Path to model to update
    :param opset: Opset to update model to
    :param out_path: Optional output path for updated model to be saved to.
    :param logger: Optional logger for diagnostic output
    :returns: Updated onnx.ModelProto
    """
def optimize_model(model_path: pathlib.Path, output_path: pathlib.Path, level: ort.GraphOptimizationLevel = ..., log_level: int = 3):
    """
    Optimize an ONNX model using ONNX Runtime to the specified level
    :param model_path: Path to ONNX model
    :param output_path: Path to save optimized model to.
    :param level: onnxruntime.GraphOptimizationLevel to use. Default is ORT_ENABLE_BASIC.
    :param log_level: Log level. Defaults to Error (3) so we don't get output about unused initializers being removed.
                      Warning (2) or Info (1) may be desirable in some scenarios.
    """
def remove_invalid_dim_values(graph: onnx.GraphProto):
    """
    Iterate the graph and subgraphs, unsetting any dim_value entries that have a value of less than 1.
    These are typically erroneously inserted by a converter to represent a dynamic dimension.
    :param graph: GraphProto to update
    """
def make_dim_param_fixed(graph: onnx.GraphProto, param_name: str, value: int):
    """
    Iterate all values in the graph, replacing dim_param in a tensor shape with the provided value.
    :param graph: GraphProto to update
    :param param_name: dim_param to set
    :param value: value to use
    """
def make_input_shape_fixed(graph: onnx.GraphProto, input_name: str, fixed_shape: [int]):
    """
    Update the named graph input to set shape to the provided value. This can be used to set unknown dims as well
    as to replace dim values.
    If setting the input shape replaces a dim_param, update any other values in the graph that use the dim_param.
    :param graph: Graph to update
    :param input_name: Name of graph input to update.
    :param fixed_shape: Shape to use.
    """
def fix_output_shapes(model: onnx.ModelProto):
    """
    Update the output shapesof a model where the input shape/s were made fixed, if possible.
    This is mainly to make the model usage clearer if the output shapes can be inferred from the new input shapes.
    :param model: Model that had input shapes fixed.
    """
def get_producer_consumer_maps(graph: onnx.GraphProto):
    """
    Get maps for connections between the node that produces each value and the nodes that consume the value.
    Processing includes subgraphs. As the map key is a Node instance from the Graph there should be no ambiguity.
    :param graph: Graph to process.
    :return: Tuple with two maps.
             First is node_to_producers map of a node to set of all nodes producing input it consumes.
             Second is node_to_consumers map of a node to set of all nodes consuming output it creates.
             e.g. NodeA and NodeB provide inputs to NodeC. NodeC provides input to NodeD
             node_to_consumers[NodeA] = set([NodeC])
             node_to_consumers[NodeB] = set([NodeC])
             node_to_producers[NodeC] = set([NodeA, NodeB])
             node_to_consumers[NodeC] = set([NodeD])
             node_to_producers[NodeD] = set([NodeC])
    """
def is_fixed_size_tensor(value: onnx.ValueInfoProto):
    """
    Check if value is a tensor with a fixed shape.
    :param value: onnx.ValueInfoProto to check
    :return: True if value is a tensor, with a shape, where all dimensions have fixed values.
    """
def get_optimization_level(level):
    """Convert string to GraphOptimizationLevel."""
