from tensorflow.core.framework import attr_value_pb2 as attr_value_pb2
from tensorflow.python import pywrap_tensorflow as pywrap_tensorflow

def process_inputs(op_name, producer_version, keywords):
    """Helper method to speed up `_apply_op_helper` in op_def_library."""
