from _typeshed import Incomplete
from tensorflow.lite.python import schema_util as schema_util
from tensorflow.python.platform import gfile as gfile

def convert_bytearray_to_object(model_bytearray):
    """Converts a tflite model from a bytearray to an object for parsing."""
def read_model(input_tflite_file):
    """Reads a tflite model as a python object.

  Args:
    input_tflite_file: Full path name to the input tflite file

  Raises:
    RuntimeError: If input_tflite_file path is invalid.
    IOError: If input_tflite_file cannot be opened.

  Returns:
    A python object corresponding to the input tflite file.
  """
def read_model_with_mutable_tensors(input_tflite_file):
    """Reads a tflite model as a python object with mutable tensors.

  Similar to read_model() with the addition that the returned object has
  mutable tensors (read_model() returns an object with immutable tensors).

  Args:
    input_tflite_file: Full path name to the input tflite file

  Raises:
    RuntimeError: If input_tflite_file path is invalid.
    IOError: If input_tflite_file cannot be opened.

  Returns:
    A mutable python object corresponding to the input tflite file.
  """
def convert_object_to_bytearray(model_object):
    """Converts a tflite model from an object to a immutable bytearray."""
def write_model(model_object, output_tflite_file) -> None:
    """Writes the tflite model, a python object, into the output file.

  Args:
    model_object: A tflite model as a python object
    output_tflite_file: Full path name to the output tflite file.

  Raises:
    IOError: If output_tflite_file path is invalid or cannot be opened.
  """
def strip_strings(model) -> None:
    '''Strips all nonessential strings from the model to reduce model size.

  We remove the following strings:
  (find strings by searching ":string" in the tensorflow lite flatbuffer schema)
  1. Model description
  2. SubGraph name
  3. Tensor names
  We retain OperatorCode custom_code and Metadata name.

  Args:
    model: The model from which to remove nonessential strings.
  '''
def type_to_name(tensor_type):
    """Converts a numerical enum to a readable tensor type."""
def randomize_weights(model, random_seed: int = 0, buffers_to_skip: Incomplete | None = None) -> None:
    """Randomize weights in a model.

  Args:
    model: The model in which to randomize weights.
    random_seed: The input to the random number generator (default value is 0).
    buffers_to_skip: The list of buffer indices to skip. The weights in these
                     buffers are left unmodified.
  """
def rename_custom_ops(model, map_custom_op_renames) -> None:
    """Rename custom ops so they use the same naming style as builtin ops.

  Args:
    model: The input tflite model.
    map_custom_op_renames: A mapping from old to new custom op names.
  """
def opcode_to_name(model, op_code):
    """Converts a TFLite op_code to the human readable name.

  Args:
    model: The input tflite model.
    op_code: The op_code to resolve to a readable name.

  Returns:
    A string containing the human readable op name, or None if not resolvable.
  """
def xxd_output_to_bytes(input_cc_file):
    """Converts xxd output C++ source file to bytes (immutable).

  Args:
    input_cc_file: Full path name to th C++ source file dumped by xxd

  Raises:
    RuntimeError: If input_cc_file path is invalid.
    IOError: If input_cc_file cannot be opened.

  Returns:
    A bytearray corresponding to the input cc file array.
  """
def xxd_output_to_object(input_cc_file):
    """Converts xxd output C++ source file to object.

  Args:
    input_cc_file: Full path name to th C++ source file dumped by xxd

  Raises:
    RuntimeError: If input_cc_file path is invalid.
    IOError: If input_cc_file cannot be opened.

  Returns:
    A python object corresponding to the input tflite file.
  """
def count_resource_variables(model):
    """Calculates the number of unique resource variables in a model.

  Args:
    model: the input tflite model, either as bytearray or object.

  Returns:
    An integer number representing the number of unique resource variables.
  """
