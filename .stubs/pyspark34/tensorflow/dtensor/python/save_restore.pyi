from tensorflow.dtensor.python import api as api, d_variable as d_variable, gen_dtensor_ops as gen_dtensor_ops, layout as layout_lib, mesh_util as mesh_util
from tensorflow.python.eager import context as context
from tensorflow.python.framework import errors_impl as errors_impl, ops as ops
from tensorflow.python.ops import io_ops as io_ops, variables as tf_variables
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Dict, List, Union

def sharded_save(mesh: layout_lib.Mesh, file_prefix: Union[str, ops.Tensor], tensor_names: Union[List[str], ops.Tensor], shape_and_slices: Union[List[str], ops.Tensor], tensors: List[Union[ops.Tensor, tf_variables.Variable]]):
    '''Saves given named tensor slices in a sharded, multi-client safe fashion.

  The method makes sure the checkpoint directory state is correct in a sharded
  mutli-client saving. Namely, we place a barrier after SaveV2 to make sure
  every client has done writing the files. And another one after
  MergeV2Checkpoints to make sure all Metadata is properly merged.

  Upon existing, the checkpoint is completed and the all directory operations
  are done.

  Args:
    mesh: The Mesh that contains the Tensors to save.
    file_prefix: The prefix of checkpoint.
    tensor_names: a list of tensor names used in save op.
    shape_and_slices: a list of shape and slice specification used in save op.
      The only supported value is "" as we don\'t support distributed saving with
      slices yet.
    tensors: a list of tensors used in save op. The order should match
      tensor_names.

  Returns:
    A MergeV2Checkpoints op that merged all Metadata.
  '''
def enable_save_as_bf16(variables: List[tf_variables.Variable]):
    """Allows float32 DVariables to be checkpointed and restored as bfloat16.

  The method only affects the DVariable part inside the model and leaves
  non-DTensor Variables/Tensors untouched.

  Args:
    variables: A list of tf.Variable to be enabled with bfloat16 save/restore.
      Only has effect on DTensor Variables as they go through d_variables with
      DTensor Specific logis.
  """
def name_based_restore(mesh: layout_lib.Mesh, checkpoint_prefix: str, name_tensor_dict: Dict[str, Union[ops.Tensor, tf_variables.Variable]]):
    """Restores from checkpoint_prefix to name based DTensors.

  It is required to have already-initialized DTensor variables that have same
  shape/dtype for the tensors being restored.

  Also, we currently only support a named based restore on a single mesh.

  Args:
    mesh: The single mesh that all Tensors would be restored to.
    checkpoint_prefix : The prefix of checkpoint to be restored.
    name_tensor_dict: A ordered dictionary of tensor_names to a DTensor. The
      DTensor shape/dtype must match the tensors being saved/restored for now.

  Returns:
    A dictionary of name to its restored DTensor value.
  """
def name_based_save(mesh: layout_lib.Mesh, checkpoint_prefix: Union[str, ops.Tensor], name_tensor_dict: Dict[str, Union[ops.Tensor, tf_variables.Variable]]):
    """Saves name based Tensor into a Checkpoint.

  The function prepares the input dictionary to the format of a `sharded_save`,
  so that it can take advantage of DTensor SPMD based distributed save.

  Same as restore, the function only supports saving on the single mesh.

  Args:
    mesh: The single mesh that all Tensors would be restored to.
    checkpoint_prefix : The prefix of checkpoint to be restored.
    name_tensor_dict: A ordered dictionary of tensor_names to a DTensor. The
      DTensor shape/dtype must match the tensors being saved/restored for now.
  """
