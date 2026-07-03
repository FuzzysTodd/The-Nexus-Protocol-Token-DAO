from _typeshed import Incomplete
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, math_ops as math_ops
from tensorflow.python.util import tf_should_use as tf_should_use
from typing import NamedTuple

class _Resource(NamedTuple):
    handle: Incomplete
    create: Incomplete
    is_initialized: Incomplete

def register_resource(handle, create_op, is_initialized_op, is_shared: bool = True) -> None:
    """Registers a resource into the appropriate collections.

  This makes the resource findable in either the shared or local resources
  collection.

  Args:
   handle: op which returns a handle for the resource.
   create_op: op which initializes the resource.
   is_initialized_op: op which returns a scalar boolean tensor of whether
    the resource has been initialized.
   is_shared: if True, the resource gets added to the shared resource
    collection; otherwise it gets added to the local resource collection.

  """
def shared_resources():
    """Returns resources visible to all tasks in the cluster."""
def local_resources():
    """Returns resources intended to be local to this session."""
def report_uninitialized_resources(resource_list: Incomplete | None = None, name: str = 'report_uninitialized_resources'):
    """Returns the names of all uninitialized resources in resource_list.

  If the returned tensor is empty then all resources have been initialized.

  Args:
   resource_list: resources to check. If None, will use shared_resources() +
    local_resources().
   name: name for the resource-checking op.

  Returns:
   Tensor containing names of the handles of all resources which have not
   yet been initialized.

  """
def initialize_resources(resource_list, name: str = 'init'):
    """Initializes the resources in the given list.

  Args:
   resource_list: list of resources to initialize.
   name: name of the initialization op.

  Returns:
   op responsible for initializing all resources.
  """
