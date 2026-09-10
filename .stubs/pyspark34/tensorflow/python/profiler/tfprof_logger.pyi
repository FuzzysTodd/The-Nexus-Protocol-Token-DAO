from _typeshed import Incomplete
from tensorflow.core.profiler import tfprof_log_pb2 as tfprof_log_pb2
from tensorflow.python.eager import context as context
from tensorflow.python.framework import ops as ops, tensor_shape as tensor_shape
from tensorflow.python.platform import gfile as gfile
from tensorflow.python.profiler.internal import flops_registry as flops_registry
from tensorflow.python.util.tf_export import tf_export as tf_export

TRAINABLE_VARIABLES: str
REGISTERED_FLOP_STATS: str

def merge_default_with_oplog(graph, op_log: Incomplete | None = None, run_meta: Incomplete | None = None, add_trace: bool = True, add_trainable_var: bool = True):
    """Merge the tfprof default extra info with caller's op_log.

  Args:
    graph: tf.Graph. If None and eager execution is not enabled, use
        default graph.
    op_log: OpLogProto proto.
    run_meta: RunMetadata proto used to complete shape information.
    add_trace: Whether to add op trace information.
    add_trainable_var: Whether to assign tf.compat.v1.trainable_variables() op
      type '_trainable_variables'.
  Returns:
    tmp_op_log: Merged OpLogProto proto.
  """
def write_op_log(graph, log_dir, op_log: Incomplete | None = None, run_meta: Incomplete | None = None, add_trace: bool = True) -> None:
    '''Log provided \'op_log\', and add additional model information below.

    The API also assigns ops in tf.compat.v1.trainable_variables() an op type
    called \'_trainable_variables\'.
    The API also logs \'flops\' statistics for ops with op.RegisterStatistics()
    defined. flops calculation depends on Tensor shapes defined in \'graph\',
    which might not be complete. \'run_meta\', if provided, completes the shape
    information with best effort.

  Args:
    graph: tf.Graph. If None and eager execution is not enabled, use
        default graph.
    log_dir: directory to write the log file.
    op_log: (Optional) OpLogProto proto to be written. If not provided, an new
        one is created.
    run_meta: (Optional) RunMetadata proto that helps flops computation using
        run time shape information.
    add_trace: Whether to add python code trace information.
        Used to support "code" view.
  '''
