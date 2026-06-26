from _typeshed import Incomplete
from tensorflow.python.framework import dtypes as dtypes

OP_TYPES_ALLOWLIST: Incomplete
TENSOR_TYPES_ALLOWLIST: Incomplete

def obtain_capture_by_value_ops(dataset):
    """Given an input dataset, finds all allowlisted ops used for construction.

  Allowlisted ops are stateful ops which are known to be safe to capture by
  value.

  Args:
    dataset: Dataset to find allowlisted stateful ops for.

  Returns:
    A list of variant_tensor producing dataset ops used to construct this
    dataset.
  """
def obtain_all_variant_tensor_ops(dataset):
    """Given an input dataset, finds all dataset ops used for construction.

  A series of transformations would have created this dataset with each
  transformation including zero or more Dataset ops, each producing a dataset
  variant tensor. This method outputs all of them.

  Args:
    dataset: Dataset to find variant tensors for.

  Returns:
    A list of variant_tensor producing dataset ops used to construct this
    dataset.
  """
