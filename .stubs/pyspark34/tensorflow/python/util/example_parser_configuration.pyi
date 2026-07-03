from tensorflow.core.example import example_parser_configuration_pb2 as example_parser_configuration_pb2
from tensorflow.python.framework import tensor_shape as tensor_shape, tensor_util as tensor_util

def extract_example_parser_configuration(parse_example_op, sess):
    """Returns an ExampleParserConfig proto.

  Args:
    parse_example_op: A ParseExample or ParseExampleV2 `Operation`
    sess: A tf.compat.v1.Session needed to obtain some configuration values.
  Returns:
    A ExampleParserConfig proto.

  Raises:
    ValueError: If attributes are inconsistent.
  """
