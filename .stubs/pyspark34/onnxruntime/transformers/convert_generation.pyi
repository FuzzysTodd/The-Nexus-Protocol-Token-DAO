import argparse
import onnx
import torch
from _typeshed import Incomplete
from benchmark_helper import Precision
from enum import Enum
from onnx import GraphProto as GraphProto, ModelProto as ModelProto, TensorProto
from onnxruntime import GraphOptimizationLevel as GraphOptimizationLevel, InferenceSession as InferenceSession, SessionOptions as SessionOptions, get_available_providers as get_available_providers
from transformers import GPT2LMHeadModel, T5ForConditionalGeneration
from typing import Any, Dict, List

logger: Incomplete

class GenerationType(Enum):
    BEAMSEARCH: str
    GREEDYSEARCH: str
    SAMPLING: str

def parse_arguments(argv: List[str] | None = None) -> argparse.Namespace:
    """Parse arguments

    Args:
        argv (Optional[List[str]], optional): _description_. Defaults to None.

    Returns:
        argparse.Namespace: Parsed arguments.
    """
def gpt2_to_onnx(args: argparse.Namespace):
    """Convert GPT-2 model to onnx

    Args:
        args (argparse.Namespace): arguments parsed from command line
    """
def t5_to_onnx(args: argparse.Namespace):
    """Convert T5 model to onnx

    Args:
        args (argparse.Namespace): arguments parsed from command line
    """
def shape_inference(onnx_path: str, use_external_data_format: bool = True):
    """Shape inference on an onnx file, which will be overwritten.

    Args:
        onnx_path (str): Path of onnx model
        use_external_data_format(bool): output tensors to external data or not.
    """
def pad_weights_of_logits_matmul(onnx_path: str, use_external_data_format: bool = True) -> bool:
    """Pad the logits MatMul weight in the provided decoder model, which will be overwritten.

    Args:
        onnx_path (str): Path of onnx model
        use_external_data_format(bool): output tensors to external data or not.
    """
def create_ort_session(model_path: str, use_gpu: bool, use_sln_strict_mode: bool) -> InferenceSession:
    """Create OnnxRuntime session.

    Args:
        model_path (str): onnx model path
        use_gpu (bool): use GPU or not
        use_sln_strict_mode (bool): use strict mode for skip layer normalization or not

    Raises:
        RuntimeError: CUDAExecutionProvider is not available when --use_gpu is specified.

    Returns:
        onnxruntime.InferenceSession: The created session.
    """
def verify_gpt2_subgraph(graph: onnx.GraphProto, precision: Precision):
    """Verify GPT-2 subgraph

    Args:
        graph (onnx.GraphProto): onnx graph of GPT-2
        precision (Precision): Precision (FLOAT16 or FLOAT32) of the model.

    Raises:
        ValueError: Number of inputs not expected.
        ValueError: Input name is not expected.
        ValueError: Input data type is not expected.
        ValueError: Number of outputs not expected.
        ValueError: Output name is not expected.
        ValueError: Output data type is not expected.
    """
def verify_t5_decoder_subgraph(graph: onnx.GraphProto, precision: Precision):
    """Verify T5 decoder subgraph

    Args:
        graph (onnx.GraphProto): onnx graph of T5 decoder
        precision (Precision): Precision (FLOAT16 or FLOAT32) of the model.

    Raises:
        ValueError: Number of inputs not expected.
        ValueError: Input name is not expected.
        ValueError: Input data type is not expected.
        ValueError: Number of outputs not expected.
        ValueError: Output name is not expected.
        ValueError: Output data type is not expected.
    """
def verify_t5_encoder_decoder_init_subgraph(graph: onnx.GraphProto, precision: Precision):
    """Verify T5 decoder subgraph

    Args:
        graph (onnx.GraphProto): onnx graph of T5 decoder
        precision (Precision): Precision (FLOAT16 or FLOAT32) of the model.

    Raises:
        ValueError: Number of inputs not expected.
        ValueError: Input name is not expected.
        ValueError: Input data type is not expected.
        ValueError: Number of outputs not expected.
        ValueError: Output name is not expected.
        ValueError: Output data type is not expected.
    """
def remove_shared_initializers(graph1: GraphProto, graph2: GraphProto, shared_prefix: str = 'shared_', min_elements: int = 1024, require_raw_data: bool = False):
    """Remove initializers with same value from two graphs.

    Args:
        graph1 (GraphProto): the first graph to process
        graph2 (GraphProto): the second graph to process
        shared_prefix (str): add prefix to the shared initializers among two graphs
        min_elements (int, optional): minimal number of elements for initializers to be considered. Defaults to 1024.
        require_raw_data (bool, optional): Only remove tensors with raw_data field to speed up method
    """
def get_shared_initializers(encoder_model: ModelProto, decoder_model: ModelProto, require_raw_data: bool = False): ...
def move_initializers(graph: GraphProto, min_elements: int = 1024) -> List[TensorProto]:
    """Remove initializers of a graph, when they have number of elements larger than a threshold.

    Args:
        graph (GraphProto): the graph.
        min_elements (int, optional): minimal number of elements for initializers to be considered. Defaults to 1024.

    Returns:
        List[TensorProto]: initializers that are removed from the graph.
    """
def kwargs_of(node): ...
def shape_of(vi): ...
def update_decoder_subgraph_past_present_share_buffer(subg: GraphProto): ...
def update_decoder_subgraph_use_decoder_masked_attention(subg: GraphProto, is_beam_search: bool, switch_attention: bool) -> bool:
    """Update the Attention nodes to DecoderMaskedSelfAttention.

    Args:
        subg (GraphProto): GraphProto of the decoder subgraph
        is_beam_search (bool): Boolean specifying if the sampling algo is BeamSearch
        switch_attention (bool): Boolean specifying if `Attention` is to be switched with `DecoderMaskedSelfAttention`
    """
def find_past_seq_len_usage(subg: GraphProto):
    """Correct graph which originally use dim of past_seq_len from input_ids's shape which is fixed to max_seq_len after
       shared past/present buffer

    Args:
        subg (GraphProto): GraphProto of the decoder subgraph
    return:
        tensor_names_to_rename : set of tensor names which is equal to past_sequence_length
        nodes_to_remove : list of node to remove
    """
def update_decoder_subgraph_share_buffer_and_use_decoder_masked_mha(subg: GraphProto): ...
def pack_qkv_for_decoder_masked_mha(model_proto: ModelProto): ...
def update_input_shapes_for_gpt2_decoder_model(decoder_onnx_path: str, use_external_data_format: bool = True):
    '''Update the input shapes for the inputs "input_ids" and "position_ids" and make the sequence length dim value 1 for each of them.
       The decoder model will be over-written.

    Args:
        decoder_onnx_path (str): Path of GPT-2 decoder onnx model
        use_external_data_format(bool): output tensors to external data or not.
    '''
def generate_gpt2_init_decoder(decoder_onnx_path: str, init_decoder_onnx_path: str, use_external_data_format: bool = True) -> bool:
    """Generates the initial decoder GPT2 subgraph and saves it for downstream use.
       The initial decoder model will be saved to init_decoder_onnx_path.

    Args:
        decoder_onnx_path (str): Path of GPT-2 decoder onnx model
        init_decoder_onnx_path (str): Path of GPT-2 init decoder onnx model
        use_external_data_format(bool): output tensors to external data or not.
    """
def make_dim_proto_numeric_t5(model, config) -> None:
    """Make dim_proto numeric.

    Args:
        model: T5 encoder and decoder model.
        config: T5 config.
    """
def convert_generation_model(args: argparse.Namespace, generation_type: GenerationType = ...):
    """Convert model according to command line arguments.

    Args:
        args (argparse.Namespace): arguments parsed from command line
    """
def test_torch_performance(args: argparse.Namespace, model: GPT2LMHeadModel | T5ForConditionalGeneration, input_ids: torch.Tensor, attention_mask: torch.Tensor, eos_token_id: int, pad_token_id: int, bad_words_ids: List[List[int]]) -> Dict[str, Any]:
    """Test PyTorch performance of text generation.

    Args:
        args (argparse.Namespace): arguments parsed from command line
        model (Union[GPT2LMHeadModel, T5ForConditionalGeneration]): PyTorch model
        input_ids (torch.Tensor): input_ids
        attention_mask (torch.Tensor): Attention mask
        eos_token_id (int): EOS token ID
        pad_token_id (int): Padding token ID
        bad_words_ids (List[List[int]]): Words shall not be generated.

    Raises:
        RuntimeError: PyTorch with CUDA is not available for --use_gpu

    Returns:
        Dict[str, Any]: A dictionary with string with metric name, and value can be integer or string.
    """
def create_attention_mask(input_ids, pad_token_id): ...
def test_gpt_model(args: argparse.Namespace, sentences: List[str] | None = None, is_greedy: bool = False):
    """Test GPT-2 model

    Args:
        args (argparse.Namespace): arguments parsed from command line
        sentences (Optional[List[str]], optional): input text. Defaults to None.

    Returns:
        Union[Dict[str, Any], None]: A dictionary with string with metric name, and value can be integer or string.
    """
def test_t5_model(args: argparse.Namespace, sentences: List[str] | None = None):
    """Test T5 or MT5 model

    Args:
        args (argparse.Namespace): arguments parsed from command line
        sentences (Optional[List[str]], optional): input text. Defaults to None.

    Returns:
        Union[Dict[str, Any], None]: A dictionary with string with metric name, and value can be integer or string.
    """
def main(argv: List[str] | None = None, sentences: List[str] | None = None):
    """Main entry function

    Args:
        argv (Optional[List[str]], optional): _description_. Defaults to None.
        sentences (Optional[List[str]], optional): input text. Defaults to None.

    Raises:
        ValueError: Path does not exist: --encoder_decoder_init_onnx
        ValueError: Path does not exist: --decoder_onnx
        ValueError: --decoder_onnx and --encoder_decoder_init_onnx are not used together for T5

    Returns:
        Union[Dict[str, Any], None]: A dictionary with string with metric name, and value can be integer or string.
    """
