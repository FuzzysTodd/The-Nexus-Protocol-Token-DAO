import numpy as np
from onnx import TensorProto
from onnx_model import OnnxModel
from typing import Dict, Tuple

def fake_input_ids_data(input_ids: TensorProto, batch_size: int, sequence_length: int, dictionary_size: int) -> np.ndarray:
    """Create input tensor based on the graph input of input_ids

    Args:
        input_ids (TensorProto): graph input of the input_ids input tensor
        batch_size (int): batch size
        sequence_length (int): sequence length
        dictionary_size (int): vocabulary size of dictionary

    Returns:
        np.ndarray: the input tensor created
    """
def fake_segment_ids_data(segment_ids: TensorProto, batch_size: int, sequence_length: int) -> np.ndarray:
    """Create input tensor based on the graph input of segment_ids

    Args:
        segment_ids (TensorProto): graph input of the token_type_ids input tensor
        batch_size (int): batch size
        sequence_length (int): sequence length

    Returns:
        np.ndarray: the input tensor created
    """
def get_random_length(max_sequence_length: int, average_sequence_length: int): ...
def fake_input_mask_data(input_mask: TensorProto, batch_size: int, sequence_length: int, average_sequence_length: int, random_sequence_length: bool, mask_type: int = 2) -> np.ndarray:
    """Create input tensor based on the graph input of segment_ids.

    Args:
        input_mask (TensorProto): graph input of the attention mask input tensor
        batch_size (int): batch size
        sequence_length (int): sequence length
        average_sequence_length (int): average sequence length excluding paddings
        random_sequence_length (bool): whether use uniform random number for sequence length
        mask_type (int): mask type - 1: mask index (sequence length excluding paddings). Shape is (batch_size).
                                     2: 2D attention mask. Shape is (batch_size, sequence_length).
                                     3: key len, cumulated lengths of query and key. Shape is (3 * batch_size + 2).

    Returns:
        np.ndarray: the input tensor created
    """
def output_test_data(directory: str, inputs: Dict[str, np.ndarray]):
    """Output input tensors of test data to a directory

    Args:
        directory (str): path of a directory
        inputs (Dict[str, np.ndarray]): map from input name to value
    """
def fake_test_data(batch_size: int, sequence_length: int, test_cases: int, dictionary_size: int, verbose: bool, random_seed: int, input_ids: TensorProto, segment_ids: TensorProto, input_mask: TensorProto, average_sequence_length: int, random_sequence_length: bool, mask_type: int):
    """Create given number of input data for testing

    Args:
        batch_size (int): batch size
        sequence_length (int): sequence length
        test_cases (int): number of test cases
        dictionary_size (int): vocabulary size of dictionary for input_ids
        verbose (bool): print more information or not
        random_seed (int): random seed
        input_ids (TensorProto): graph input of input IDs
        segment_ids (TensorProto): graph input of token type IDs
        input_mask (TensorProto): graph input of attention mask
        average_sequence_length (int): average sequence length excluding paddings
        random_sequence_length (bool): whether use uniform random number for sequence length
        mask_type (int): mask type 1 is mask index; 2 is 2D mask; 3 is key len, cumulated lengths of query and key

    Returns:
        List[Dict[str,numpy.ndarray]]: list of test cases, where each test case is a dictionary
                                       with input name as key and a tensor as value
    """
def generate_test_data(batch_size: int, sequence_length: int, test_cases: int, seed: int, verbose: bool, input_ids: TensorProto, segment_ids: TensorProto, input_mask: TensorProto, average_sequence_length: int, random_sequence_length: bool, mask_type: int):
    """Create given number of input data for testing

    Args:
        batch_size (int): batch size
        sequence_length (int): sequence length
        test_cases (int): number of test cases
        seed (int): random seed
        verbose (bool): print more information or not
        input_ids (TensorProto): graph input of input IDs
        segment_ids (TensorProto): graph input of token type IDs
        input_mask (TensorProto): graph input of attention mask
        average_sequence_length (int): average sequence length excluding paddings
        random_sequence_length (bool): whether use uniform random number for sequence length
        mask_type (int): mask type 1 is mask index; 2 is 2D mask; 3 is key len, cumulated lengths of query and key

    Returns:
        List[Dict[str,numpy.ndarray]]: list of test cases, where each test case is a dictionary
                                       with input name as key and a tensor as value
    """
def get_graph_input_from_embed_node(onnx_model, embed_node, input_index): ...
def find_bert_inputs(onnx_model: OnnxModel, input_ids_name: str | None = None, segment_ids_name: str | None = None, input_mask_name: str | None = None) -> Tuple[np.ndarray | None, np.ndarray | None, np.ndarray | None]:
    """Find graph inputs for BERT model.
    First, we will deduce inputs from EmbedLayerNormalization node.
    If not found, we will guess the meaning of graph inputs based on naming.

    Args:
        onnx_model (OnnxModel): onnx model object
        input_ids_name (str, optional): Name of graph input for input IDs. Defaults to None.
        segment_ids_name (str, optional): Name of graph input for segment IDs. Defaults to None.
        input_mask_name (str, optional): Name of graph input for attention mask. Defaults to None.

    Raises:
        ValueError: Graph does not have input named of input_ids_name or segment_ids_name or input_mask_name
        ValueError: Expected graph input number does not match with specified input_ids_name, segment_ids_name
                    and input_mask_name

    Returns:
        Tuple[Optional[np.ndarray], Optional[np.ndarray], Optional[np.ndarray]]: input tensors of input_ids,
                                                                                 segment_ids and input_mask
    """
def get_bert_inputs(onnx_file: str, input_ids_name: str | None = None, segment_ids_name: str | None = None, input_mask_name: str | None = None) -> Tuple[np.ndarray | None, np.ndarray | None, np.ndarray | None]:
    """Find graph inputs for BERT model.
    First, we will deduce inputs from EmbedLayerNormalization node.
    If not found, we will guess the meaning of graph inputs based on naming.

    Args:
        onnx_file (str): onnx model path
        input_ids_name (str, optional): Name of graph input for input IDs. Defaults to None.
        segment_ids_name (str, optional): Name of graph input for segment IDs. Defaults to None.
        input_mask_name (str, optional): Name of graph input for attention mask. Defaults to None.

    Returns:
        Tuple[Optional[np.ndarray], Optional[np.ndarray], Optional[np.ndarray]]: input tensors of input_ids,
                                                                                 segment_ids and input_mask
    """
def parse_arguments(): ...
def create_and_save_test_data(model: str, output_dir: str, batch_size: int, sequence_length: int, test_cases: int, seed: int, verbose: bool, input_ids_name: str | None, segment_ids_name: str | None, input_mask_name: str | None, only_input_tensors: bool, average_sequence_length: int, random_sequence_length: bool, mask_type: int):
    """Create test data for a model, and save test data to a directory.

    Args:
        model (str): path of ONNX bert model
        output_dir (str): output directory
        batch_size (int): batch size
        sequence_length (int): sequence length
        test_cases (int): number of test cases
        seed (int): random seed
        verbose (bool): whether print more information
        input_ids_name (str): graph input name of input_ids
        segment_ids_name (str): graph input name of segment_ids
        input_mask_name (str): graph input name of input_mask
        only_input_tensors (bool): only save input tensors,
        average_sequence_length (int): average sequence length excluding paddings
        random_sequence_length (bool): whether use uniform random number for sequence length
        mask_type(int): mask type
    """
def main() -> None: ...
