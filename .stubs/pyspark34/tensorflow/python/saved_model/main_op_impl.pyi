from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import control_flow_ops as control_flow_ops, lookup_ops as lookup_ops, variables as variables
from tensorflow.python.util import deprecation as deprecation
from tensorflow.python.util.tf_export import tf_export as tf_export

def main_op():
    """Returns a main op to init variables and tables.

  Returns the main op including the group of ops that initializes all
  variables, initializes local variables and initialize all tables.

  Returns:
    The set of ops to be run as part of the main op upon the load operation.
  """
def main_op_with_restore(restore_op_name):
    """Returns a main op to init variables, tables and restore the graph.

  Returns the main op including the group of ops that initializes all
  variables, initialize local variables, initialize all tables and the restore
  op name.

  Args:
    restore_op_name: Name of the op to use to restore the graph.

  Returns:
    The set of ops to be run as part of the main op upon the load operation.
  """
