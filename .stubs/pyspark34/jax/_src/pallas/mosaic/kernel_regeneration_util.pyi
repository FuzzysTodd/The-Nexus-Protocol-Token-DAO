from jaxlib.mlir import ir
from typing import Any

def encode_kernel_regeneration_metadata(metadata: dict[str, Any]) -> dict[str, bytes]:
    """Serializes the given kernel regeneration metadata.

  This function hides the serialization details from the end user.

  Args:
    metadata: dictionary with user-defined data to be serialized in the backend
      config.

  Returns:
    A dict that can be directly passed to pallas_call as a 'mosaic_params'
    argument.

  Raises:
    TypeError: when the input metadata is not serializable in json format.
  """
def extract_kernel_regeneration_metadata(op: ir.Operation) -> dict[str, Any]:
    """Extract kernel regeneration metadata from the given Operation.

  This function hides the serialization details from the end user.

  Args:
    op: the tpu custom_call mlir Operation that contains the kernel metadata.

  Returns:
    The decoded metadata in the form of a dict. This corresponds to the dict
    in input to the 'encode' function.
  """
