from _typeshed import Incomplete
from collections import deque as deque
from onnx_model import OnnxModel
from pathlib import Path as Path
from typing import List

logger: Incomplete
CONSTANT_SHAPE_NAME_PREFIX: str
RESHAPE_INPUT_SHAPE_PREFIX: str

class BertOnnxModelShapeOptimizer(OnnxModel):
    """
    This optimizer will replace Shape output or the shape input of Reshape node by initializer. Currently, it requires
    model inputs to have static shape.
    """
    def __init__(self, onnx_model) -> None: ...
    def add_shape_initializer(self, shape):
        """
        Add an initializer for constant shape.
        """
    def get_shape_outputs(self):
        """
        Returns a list of output names of all Shape nodes.
        """
    def get_reshape_shape_inputs(self):
        """
        Returns a list of shape input names of Reshape nodes.
        """
    def add_shape_for_reshape_input(self):
        """
        For each Reshape node, create a Shape node for its first input.
        Returns the output names of these Shape nodes.
        """
    def add_extra_graph_output(self, extra_outputs):
        """
        Add a list of output names to graph output.
        """
    def use_static_input(self, inputs, batch_size: int = 1, max_seq_len: int = 128) -> None:
        """
        Update the model to use static axes instead of dynamic axes for graph inputs.
        """
    def create_dummy_inputs(self, input_ids, segment_ids, input_mask, batch_size, sequence_length, elem_type, dictionary_size: int = 8):
        """
        Create dummy data for model inputs. If the model has more than 3 inputs, please update this function accordingly before running the tool.
        """
    bert_inputs: Incomplete
    def shape_optimization(self, temp_model_path, input_ids, segment_ids, input_mask, output_names, batch_size, sequence_length, enable_shape_opt, enable_reshape_opt, verbose) -> None: ...
    def update_target_shape(self, shapes, shape_input, input_shape, verbose) -> None:
        """
        Update the target shape to use 0 to represent that dimension value does not change.
        For example, shape of source data is (2, 5, 8) and target shape is (2, 5, 4, 2), the target shape will be updated to (0, 0, 4, 2).
        """
    def validate_input(self, input: str): ...
    def validate_outputs(self, output_names: List[str]): ...
    def optimize(self, output_path: str, input_ids: str, segment_ids: str, input_mask: str, enable_shape_opt: bool, enable_reshape_opt: bool, output_names: List[str] | None = None, batch_size: int = 1, sequence_length: int = 128, verbose: bool = False): ...

def parse_arguments(): ...
def setup_logging(verbose) -> None: ...
def main() -> None: ...
