from _typeshed import Incomplete
from onnx import ModelProto as ModelProto, NodeProto as NodeProto, TensorProto

logger: Incomplete

class OnnxModel:
    def __init__(self, model) -> None: ...
    model: Incomplete
    shape_infer_helper: Incomplete
    enable_shape_infer: bool
    all_graphs: Incomplete
    def initialize(self, model) -> None: ...
    def disable_shape_inference(self) -> None: ...
    def infer_runtime_shape(self, dynamic_axis_mapping={}, update: bool = False): ...
    def input_name_to_nodes(self): ...
    def output_name_to_node(self): ...
    def nodes(self): ...
    def graph(self): ...
    def graphs(self): ...
    def get_graphs_input_names(self): ...
    def get_graphs_output_names(self): ...
    def get_graph_by_node(self, node): ...
    def get_graph_by_name(self, graph_name): ...
    def get_topological_insert_id(self, graph, outputs): ...
    def remove_node(self, node) -> None: ...
    def remove_nodes(self, nodes_to_remove) -> None: ...
    def add_node(self, node, graph_name: Incomplete | None = None) -> None: ...
    def add_nodes(self, nodes_to_add, node_name_to_graph_name: Incomplete | None = None) -> None: ...
    def add_initializer(self, tensor, graph_name: Incomplete | None = None) -> None: ...
    def add_input(self, input, graph_name: Incomplete | None = None) -> None: ...
    @staticmethod
    def replace_node_input(node, old_input_name, new_input_name) -> None: ...
    def replace_input_of_all_nodes(self, old_input_name, new_input_name) -> None: ...
    @staticmethod
    def replace_node_output(node, old_output_name, new_output_name) -> None: ...
    def replace_output_of_all_nodes(self, old_output_name, new_output_name) -> None: ...
    def get_initializer(self, name): ...
    def get_nodes_by_op_type(self, op_type): ...
    def get_children(self, node, input_name_to_nodes: Incomplete | None = None): ...
    def get_parents(self, node, output_name_to_node: Incomplete | None = None): ...
    def get_parent(self, node, i, output_name_to_node: Incomplete | None = None): ...
    def match_first_parent(self, node, parent_op_type, output_name_to_node, exclude=[]):
        """
        Find parent node based on constraints on op_type.

        Args:
            node (str): current node name.
            parent_op_type (str): constraint of parent node op_type.
            output_name_to_node (dict): dictionary with output name as key, and node as value.
            exclude (list): list of nodes that are excluded (not allowed to match as parent).

        Returns:
            parent: The matched parent node. None if not found.
            index: The input index of matched parent node. None if not found.
        """
    def match_parent(self, node, parent_op_type, input_index: Incomplete | None = None, output_name_to_node: Incomplete | None = None, exclude=[], return_indice: Incomplete | None = None):
        """
        Find parent node based on constraints on op_type and index.
        When input_index is None, we will find the first parent node based on constraints,
        and return_indice will be appended the corresponding input index.

        Args:
            node (str): current node name.
            parent_op_type (str): constraint of parent node op_type.
            input_index (int or None): only check the parent given input index of current node.
            output_name_to_node (dict): dictionary with output name as key, and node as value.
            exclude (list): list of nodes that are excluded (not allowed to match as parent).
            return_indice (list): a list to append the input index when input_index is None.

        Returns:
            parent: The matched parent node.
        """
    def match_parent_paths(self, node, paths, output_name_to_node): ...
    def match_parent_path(self, node, parent_op_types, parent_input_index: Incomplete | None = None, output_name_to_node: Incomplete | None = None, return_indice: Incomplete | None = None):
        """
        Find a sequence of input edges based on constraints on parent op_type and index.
        When input_index is None, we will find the first parent node based on constraints,
        and return_indice will be appended the corresponding input index.

        Args:
            node (str): current node name.
            parent_op_types (str): constraint of parent node op_type of each input edge.
            parent_input_index (list): constraint of input index of each input edge. None means no constraint.
            output_name_to_node (dict): dictionary with output name as key, and node as value.
            return_indice (list): a list to append the input index
                                  When there is no constraint on input index of an edge.

        Returns:
            parents: a list of matched parent node.
        """
    def find_first_child_by_type(self, node, child_type, input_name_to_nodes: Incomplete | None = None, recursive: bool = True): ...
    def find_first_parent_by_type(self, node, parent_type, output_name_to_node: Incomplete | None = None, recursive: bool = True): ...
    def get_constant_value(self, output_name): ...
    def get_constant_input(self, node): ...
    def find_constant_input(self, node, expected_value, delta: float = 1e-06): ...
    def is_constant_with_specified_dimension(self, output_name, dimensions, description): ...
    def has_constant_input(self, node, expected_value, delta: float = 1e-06): ...
    def get_children_subgraph_nodes(self, root_node, stop_nodes, input_name_to_nodes: Incomplete | None = None): ...
    def tensor_shape_to_list(self, tensor_type):
        """Convert tensor shape to list"""
    def get_dtype(self, input_or_output: str):
        """Try get data type given a name (could be initializer, graph input or output)."""
    @staticmethod
    def get_node_attribute(node: NodeProto, attribute_name: str): ...
    def remove_cascaded_cast_nodes(self) -> None:
        """Remove Cast node that are followed by another Cast node like  --> Cast --> Cast -->
        Note that this shall be used carefully since it might introduce semantic change.
        For example, float -> int -> float could get different value than the original float value.
        So, it is recommended to used only in post-processing of mixed precision conversion.
        """
    def remove_useless_cast_nodes(self):
        """Remove cast nodes that are not needed: input and output has same data type."""
    def convert_model_float32_to_float16(self, cast_input_output: bool = True) -> None: ...
    def convert_float_to_float16(self, use_symbolic_shape_infer: bool = True, **kwargs) -> None:
        """Convert a model to half (default) or mixed precision.
           To use mixed precision, user need specify which graph inputs, outputs, operator type
           or list of nodes shall keep in float32.

           Note that the conversion might not proceed without type information for the whole graph.

           By default, we use symbolic shape inference to get type information. The benefit of symbolic shape inference
           is that it could handle fused operators in com.microsoft domain. Those operators cannot be handled in onnx shape
           inference so symbolic shape inference is recommended for optimized model.

           When symbolic shape inference is used (even if it failed), ONNX shape inference will be disabled.

           Note that onnx shape inference will fail for model larger than 2GB. For large model, you have to eanble
           symbolic shape inference. If your model is not optimized, you can also use model path to call
           convert_float_to_float16 in float16.py (see https://github.com/microsoft/onnxruntime/pull/15067) to
           avoid the 2GB limit.

        Args:
            use_symbolic_shape_infer (bool, optional): use symbolic shape inference instead of onnx shape inference.
                                                       Defaults to True.
            keep_io_types (Union[bool, List[str]], optional): boolean or a list of float32 input/output names.
                                                              If True, model inputs/outputs should be left as float32.
                                                              Defaults to True.
            op_block_list (List[str], optional): List of operator types to leave as float32.
                                                 Defaults to None, which will use `float16.DEFAULT_OP_BLOCK_LIST`.
            node_block_list (List[str], optional): List of node names to leave as float32. Defaults to None.
            force_fp16_initializers(bool): force converting all float initializers to float16.
                                           Default to false.
            min_positive_val (float, optional): minimal positive value. Defaults to 1e-7.
            max_finite_val (float, optional): maximal finite value. Defaults to 1e4.
            force_fp16_inputs(Dict[str, List[int]]): Force the conversion of the inputs of some operators to float16, even if
                                                     this script's preference it to keep them in float32.
        """
    def create_node_name(self, op_type, name_prefix: Incomplete | None = None):
        """Create a unique node name that starts with a prefix (default is operator type).
           The name will not be duplicated with any name that generated or existed in current graphs.
        Args:
            op_type (str): operator type
            name_prefix (str, optional): prefix of node name. Defaults to None.

        Returns:
            str: node name
        """
    def find_graph_input(self, input_name): ...
    def find_graph_output(self, output_name): ...
    def get_parent_subgraph_nodes(self, node, stop_nodes, output_name_to_node: Incomplete | None = None): ...
    def get_graph_inputs(self, current_node, recursive: bool = False):
        """
        Find graph inputs that linked to current node.
        """
    @staticmethod
    def input_index(node_output, child_node): ...
    def remove_unused_constant(self) -> None: ...
    def prune_graph(self, outputs: Incomplete | None = None, allow_remove_graph_inputs: bool = True) -> None:
        """
        Prune graph to keep only required outputs. It removes unnecessary nodes that are not linked
        (directly or indirectly) to any required output.

        There is also an option to remove graph inputs that are not used to generate any required output.

        Args:
            outputs (list): a list of graph outputs to retain. If it is None, all graph outputs will be kept.
            allow_remove_graph_inputs (bool): allow remove graph inputs.
        """
    def update_graph(self, verbose: bool = False, allow_remove_graph_inputs: bool = False) -> None: ...
    def is_safe_to_fuse_nodes(self, nodes_to_remove, keep_outputs, input_name_to_nodes, output_name_to_node): ...
    @staticmethod
    def graph_topological_sort(graph, is_deterministic: bool = False): ...
    def topological_sort(self, is_deterministic: bool = False) -> None: ...
    @staticmethod
    def save(model, output_path, save_as_external_data: bool = False, all_tensors_to_one_file: bool = True, size_threshold: int = 1024, convert_attribute: bool = False) -> None: ...
    def save_model_to_file(self, output_path, use_external_data_format: bool = False, all_tensors_to_one_file: bool = True) -> None: ...
    def get_graph_inputs_excluding_initializers(self):
        """
        Returns real graph inputs (excluding initializers from older onnx model).
        """
    def get_opset_version(self):
        """Get opset version of onnx domain

        Raises:
            RuntimeError: ONNX model has no opset for default domain.

        Returns:
            int: opset version of onnx domain.
        """
    def get_operator_statistics(self, include_domain: bool = False):
        """
        Returns node count of operators.
        """
    @staticmethod
    def has_same_value(tensor1: TensorProto, tensor2: TensorProto, require_raw_data: bool = False) -> bool:
        """Returns True when two tensors have same value.
           Note that name can be different.

        Args:
            tensor1 (TensorProto): initializer 1
            tensor2 (TensorProto): initializer 2
            require_raw_data (bool): ignore tensors without raw_data
                Note: Flag can speed up runtime significantly

        Returns:
            bool: True when two intializers has same value.
        """
    def remove_duplicated_initializer(self, require_raw_data: bool = False):
        """Remove initializers with duplicated values, and only keep the first one.
        It could help reduce size of models (like ALBert) with shared weights.
        If require_raw_data passed, method will only compare raw_data initializers to speed runtime
        Note: this function does not process subgraph.
        """
    def add_prefix_to_names(self, prefix: str):
        """Add prefix to initializer or intermediate outputs in graph. Main graph inputs and outputs are excluded.
        It could help avoid conflicting in name of node_args when merging two graphs.
        Note: this function does not process subgraph.
        """
    def clean_shape_infer(self) -> None: ...
    def use_float16(self):
        """Check whether the model uses float16"""
