from _typeshed import Incomplete
from tensorflow.python.framework import dtypes as dtypes
from tensorflow.python.util import object_identity as object_identity

READ_ONLY_RESOURCE_INPUTS_ATTR: str
RESOURCE_READ_OPS: Incomplete
COLLECTIVE_MANAGER_IDS: str

def register_read_only_resource_op(op_type) -> None:
    """Declares that `op_type` does not update its touched resource."""
def get_read_only_resource_input_indices_graph(func_graph):
    """Returns sorted list of read-only resource indices in func_graph.inputs."""
def get_read_write_resource_inputs(op):
    """Returns a tuple of resource reads, writes in op.inputs.

  Args:
    op: Operation

  Returns:
    A 2-tuple of ObjectIdentitySets, the first entry containing read-only
    resource handles and the second containing read-write resource handles in
    `op.inputs`.
  """
