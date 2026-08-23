from _typeshed import Incomplete

NODES_TYPE_CONTAINING_SUBGRAPH: Incomplete

def parse_arguments(argv: Incomplete | None = None): ...
def run_profile(onnx_model_path, use_gpu, provider, basic_optimization, thread_num, all_inputs): ...
def load_profile_json(profile_file): ...
def parse_kernel_results(sess_time, threshold: int = 0):
    """Parse profile data and output nodes in two sections - nodes in the original order, and top expensive nodes.

    Args:
        sess_time (List[Dict]): profile data
        kernel_time_only (bool, optional): Only include items for kernel time. Defaults to False.
        threshold (int, optional): Minimum ratio of duration among all. Defaults to 0.

    Returns:
        List[str]: lines of string for output.
    """
def parse_node_results(sess_time, kernel_time_only: bool = False, threshold: int = 0):
    """Parse profile data and output nodes in two sections - nodes in the original order, and top expensive nodes.

    Args:
        sess_time (List[Dict]): profile data
        kernel_time_only (bool, optional): Only include items for kernel time. Defaults to False.
        threshold (int, optional): Minimum ratio of duration among all. Defaults to 0.

    Returns:
        List[str]: lines of string for output.
    """
def group_node_results(sess_time, kernel_time_only, use_gpu):
    """Group results by operator name.

    Args:
        sess_time (List[Dict]): profile data
        kernel_time_only (bool): Only include items for kernel time.
        use_gpu (bool): GPU is used in profiling or not.

    Returns:
        List[str]: lines of string for output.
    """
def get_dim_from_type_proto(dim): ...
def get_shape_from_type_proto(type_proto): ...
def create_dummy_inputs(onnx_model, batch_size, sequence_length, samples):
    """Create dummy inputs for ONNX model.

    Args:
        onnx_model (OnnxModel): ONNX model
        batch_size (int): batch size
        sequence_length (int): sequence length
        samples (int): number of samples

    Returns:
        List[Dict]: list of inputs
    """
def create_bert_inputs(onnx_model, batch_size, sequence_length, samples, input_ids_name: Incomplete | None = None, segment_ids_name: Incomplete | None = None, input_mask_name: Incomplete | None = None):
    """Create dummy inputs for BERT model.

    Args:
        onnx_model (OnnxModel): ONNX model
        batch_size (int): batch size
        sequence_length (int): sequence length
        samples (int): number of samples
        input_ids_name (str, optional): Name of graph input for input IDs. Defaults to None.
        segment_ids_name (str, optional): Name of graph input for segment IDs. Defaults to None.
        input_mask_name (str, optional): Name of graph input for attention mask. Defaults to None.

    Returns:
        List[Dict]: list of inputs
    """
def create_gpt2_inputs(onnx_model, batch_size, sequence_length, past_sequence_length, samples):
    """Create dummy inputs for GPT-2 model.

    Args:
        onnx_model (OnnxModel): ONNX model
        batch_size (int): batch size
        sequence_length (int): sequence length
        past_sequence_length (int): past sequence length
        samples (int): number of samples

    Raises:
        RuntimeError: symbolic is not supported. Use the tool convert_to_onnx.py to export ONNX model instead.

    Returns:
        List[Dict]: list of inputs
    """
def create_longformer_inputs(onnx_model, batch_size, sequence_length, global_length, samples):
    """Create dummy inputs for Longformer model.

    Args:
        onnx_model (OnnxModel): ONNX model
        batch_size (int): batch size
        sequence_length (int): sequence length
        global_length (int): number of global tokens
        samples (int): number of samples

    Raises:
        RuntimeError: symbolic is not supported. Use the tool convert_longformer_to_onnx.py to export ONNX model instead.

    Returns:
        List[Dict]: list of inputs
    """
def process_results(profile_file, args): ...
def run(args): ...
