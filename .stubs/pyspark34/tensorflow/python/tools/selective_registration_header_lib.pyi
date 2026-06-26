from _typeshed import Incomplete
from tensorflow.core.framework import graph_pb2 as graph_pb2
from tensorflow.python.platform import gfile as gfile, tf_logging as tf_logging

OPS_WITHOUT_KERNEL_ALLOWLIST: Incomplete
FLEX_PREFIX: bytes
FLEX_PREFIX_LENGTH: Incomplete

def get_ops_from_nodedef(node_def):
    """Gets the op and kernel needed from the given NodeDef.

  Args:
    node_def: TF NodeDef to get op/kernel information.

  Returns:
    A tuple of (op_name, kernel_name). If the op is not in the allowlist of ops
    without kernel and there is no kernel found, then return None.
  """
def get_ops_and_kernels(proto_fileformat, proto_files, default_ops_str):
    """Gets the ops and kernels needed from the model files."""
def get_header_from_ops_and_kernels(ops_and_kernels, include_all_ops_and_kernels):
    """Returns a header for use with tensorflow SELECTIVE_REGISTRATION.

  Args:
    ops_and_kernels: a set of (op_name, kernel_class_name) pairs to include.
    include_all_ops_and_kernels: if True, ops_and_kernels is ignored and all op
      kernels are included.

  Returns:
    the string of the header that should be written as ops_to_register.h.
  """
def get_header(graphs, proto_fileformat: str = 'rawproto', default_ops: str = 'NoOp:NoOp,_Recv:RecvOp,_Send:SendOp'):
    '''Computes a header for use with tensorflow SELECTIVE_REGISTRATION.

  Args:
    graphs: a list of paths to GraphDef files to include.
    proto_fileformat: optional format of proto file, either \'textproto\',
      \'rawproto\' (default) or ops_list. The ops_list is the file contain the
      list of ops in JSON format, Ex: "[["Transpose", "TransposeCpuOp"]]".
    default_ops: optional comma-separated string of operator:kernel pairs to
      always include implementation for. Pass \'all\' to have all operators and
      kernels included. Default: \'NoOp:NoOp,_Recv:RecvOp,_Send:SendOp\'.

  Returns:
    the string of the header that should be written as ops_to_register.h.
  '''
