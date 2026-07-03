from _typeshed import Incomplete
from tensorflow.core.framework import summary_pb2 as summary_pb2
from tensorflow.python.eager import monitoring as monitoring
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, func_graph as func_graph, function as function, graph_io as graph_io, ops as ops, tensor_util as tensor_util
from tensorflow.python.lib.io import file_io as file_io
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, control_flow_util as control_flow_util, gen_math_ops as gen_math_ops, init_ops as init_ops, linalg_ops as linalg_ops, logging_ops as logging_ops, math_ops as math_ops, nn_impl as nn_impl, state_ops as state_ops, string_ops as string_ops, variable_scope as variable_scope
from tensorflow.python.platform import analytics as analytics, gfile as gfile, remote_utils as remote_utils
from tensorflow.python.summary import summary_iterator as summary_iterator
from tensorflow.python.tpu import tensor_tracer_flags as tensor_tracer_flags, tensor_tracer_report as tensor_tracer_report, tpu as tpu
from tensorflow.python.tpu.ops import tpu_ops as tpu_ops
from tensorflow.python.training import training_util as training_util

TENSOR_TRACER_SUMMARY_COLLECTION: str
tt_gauge: Incomplete

def set_parameters(tensor_tracer_params: Incomplete | None = None) -> None:
    """Enables tensor tracer and sets its parameters.

  Example usage:
    tensor_tracer_parameters = {'trace_dir': '/usr/tmp/trace_dir',
                                'trace_mode': 'norm',
                                'report_file': '/usr/tmp/trace_dir/report.all'}
    tensor_tracer.set_parameters(tensor_tracer_parameters)

  This sets up the parameters for tensor tracer. A call to tensor tracer as
  below is necessary to enable debugging on CPUs and GPUs. On TPUs below can be
  skipped as this call is hooked into tpu.rewrite.
    tt = tensor_tracer.TensorTracer()
    loss = tt.trace_cpu(tf.get_default_graph(), tensor_fetches=loss)

  Args:
    tensor_tracer_params: Tensor tracer parameter dictionary. Below gives
    examples of these parameters: See tensor_tracer_report.py for all
      parameters.
        - enable: If set, tensor tracer will be enabled. Calling
          enable_tensor_tracer automatically adds this parameters.
        - trace_mode: The trace_mode to be used by tensor tracer. These include:
          - summary: Collects multiple statistics for traced tensors, and writes
            them a summary file that can be visualized using tensorboard. This
            mode currently only works for TPUEstimator. It can be also be used
            for other models, but outfeed must be handled by the user.
          - norm: Collects norm of each traced tensor and writes them into a
            text file pointed by 'trace_dir' flag. (Default mode).
          - nan-inf: Checks the existince of NaNs and Infs in the tensor, and
            writes a boolean value to a text file pointed by 'trace_dir' flag.
            Note that 'norm' mode can also capture this information with more
            numerical info.
          - max-abs: Collects the absolute max for each traced tensors and
            writes it into a text file pointed by 'trace_dir' flag.
          - full-tensor: Writes the full tensor content of the traced tensors
            into a text file pointed by 'trace_dir' flag.
          - part-tensor: Writes a part of the tensor content of the traced
            tensors into a text file pointed by 'trace_dir' flag.
          - full_tensor_summary: Writes the full tensors as binary event files.
            The outputs can be read using: trace =
              tensor_tracer.read_tensor_tracer_event_file(event_file_path)

        - report_file: Path to the metadata file that is written during graph
          construction. If not set, metadata will be printed to stdout during
          graph construction.
        - trace_dir: Path where the execution traces will be written during the
          graph execution. If not set, trace will be printed to stderr.
        - trace_level: Tensor tracer aims to trace everything it can. This
          introduces some overhead on graph execution and graph compilation
          times. Using trace_level parameter, it is possible to trace operation
          based on their priorities. For example, - trace_level=7 is the highest
          trace_level, in which every op is traced. - trace_level=6 will skip
          constant operations such as tf.constant. - trace_level=5 will skip
          less important ops such as tf.identities. - The default trace_level=3,
          that will skip concat ops, or random number generators. - To reduce
          the graph compile time overhead, trace_level can be set to 0, that
          will skip additions, and substractions, and multiplications as well.
        - excluded_opnames: If set, any matching op name will not be traced.
          excluded_opnames can be set as a regular expression. E.g,
          excluded_opnames=.* will exclude everything.
        - excluded_optypes: If set, any matching op type will not be traced.
          excluded_optypes can be set as a regular expression. E.g,
          excluded_optypes=.* will exclude everything. excluded_optypes=MatMul
          will exclude all MatMul ops from tracing.
        - included_opnames: If set, any matching op name will be forced to be
          traced. included_opnames can be set as a regular expression. E.g,
          '--included_opnames=some_op --excluded_opname=*.' will only trace
          some_op.
        - included_optypes: If set, any matching op type will be forced to be
          traced. included_optypes can be set as a regular expression. E.g,
          '--included_optypes=some_op_type --excluded_optypes=*.' will trace
          only the ops with type 'some_op_type'
        - flush_summaries: If summary mode is used, flush_summaries=1 will
          flush summaries using outside compilation. Note that, if used with
          low level APIs, flush_summaries=1 is necessary to obtain results.
        Advanced Flags:
        - trace_scalar: Scalar values are not traced by default. If this flag is
          set, scalar values will also be traced.
        - op_range: In the form of '%d:%d' that limits the tracing to the ops
          within this limit. --op_range='5:10' will trace only the ops that have
            topological order between 5-10.
        - submode: 'brief' or 'detailed'. If the trace mode is not compact,
          brief mode will print only the id of each traced tensor to save some
          space. 'detailed' mode prints the full tensor name.
        - use_fingerprint_subdirectory: The trace directory will be chosen as
          using the fingerprint of the trace metadata under the provided
          trace_dir.
  """
def op_priority(op_type):
    """Returns the priority of the op.

  If the priority of the op is k, it will be traced if trace_level>=k.
  Args:
    op_type: String name of the operation type.
  Returns:
    Integer value corresponding the priority of the op.
  """
def read_tensor_tracer_event_file(event_file):
    """Reads the event file written by tensor tracer.

  This can be used to read the full tensors written into binary event files by
  by TensorTracer with trace_mode=full_tensor_summary.

  Example usage:
    result_dict_list = tensor_tracer.read_tensor_tracer_event_file(
      event_file_path)
    for result_dict in result_dict_list:
      for step, tensor_dict in result_dict.items():
        for tensor_name, full_tensor_content in tensor_dict.items():
          logging.info(tensor_name, full_tensor_content)

  Args:
    event_file: Path to the event file that contains only tensor tracer events.
  Returns:
    A list of event dictionaries, each of which with the form:
    {step_number: {tensor_name: tensor_content}}. This is a list instead of
    a single event dictionary because it is possible that an event file may
    have multiple event traces, each of them covering the same step ranges.
  Raises:
    ValueError: If an unexpected trace is found.
  """
def trace_tensor(tensor, tracepoint_name: Incomplete | None = None):
    """Programmatic interface to trace a tensor with Tensor Tracer.

  Tensor Tracer, by default, traces all tensors in the execution. This function
  can be used to limit traced tensors. If this function is called for a subset
  of the tensors, only those will be traced.

  For example, Tensor Traacer will only trace c below.
    c = tf.MatMul(a, b)
    tensor_tracer.trace_tensor(c)
    d = tf.add(c, 1)
  Args:
     tensor: the tensor object for which the tracing is requested.
     tracepoint_name: an optional tensor tracepoint name string. A tracepoint
       name is an Tensor Tracer internal name for the tensor. It is useful when
       comparing equivalent traces from different models that have different
       tensor namings. Equivalent tensors (with different names) can be mapped
       to each other by assigning a common tracepoint_name.

  Returns:
    The provided tensor.
  """
def keras_layer_tracepoint(layer, checkpoint_name):
    """An interface for adding the tensor outputs of a keras layer.

  Encapsulates trace_tensor.

  Args:
     layer: A keras layer.
     checkpoint_name: a string name for the checkpoint. This name has to be a
     unique name if used within model comparison. The tensors that have the same
     checkpoint identifier is compared in model comparison.

  Returns:
    The provided layer.
  """

class TensorTracer:
    '''A software construct for tracing tensor values in a TF graph.

  This utility is disabled by default. It is hooked into tpu.rewrite, so it can
  easily be enabled on TPUs by setting the TENSOR_TRACER_FLAGS env variable as
  below without a code change.
    export TENSOR_TRACER_FLAGS="--enable=1"

  Below is the use example to enable it on CPUs or GPUs, or for more advance use
  cases on TPUs.

    a = x + 1
    b = a * 2
    rs = tf.reduce_sum(b)
    tensor_tracer.set_parameters({\'trace_dir\': \'path/to/trace_dir\',
                             \'report_file: \'path/to/report/file\'})
    tt = tensor_tracer.TensorTracer()
    if on_tpu:
      rs = tt.trace_tpu(tf.get_default_graph(),
                          tensor_fetches=rs)
    else:
      rs = tt.trace_cpu(tf.get_default_graph(),
                          tensor_fetches=rs)
    session.run(rs)

  If it is enabled, it will trace the output tensor values of
  selected Ops in the graph. It has two outputs: (1) the traces and (2)
  a report. The traces are dumped to a specified directory during the graph
  execution, while the report is dumped during the graph construction.
  By passing options via the env variable, users can change:
     (1) the trace mode (e.g., detecting NaN/Inf, printing partial or
         full tensor values)
     (2) which Ops to be traced (via op.name or op.type)
     (3) output trace file path.

  '''
    @staticmethod
    def is_enabled():
        """Returns True if TensorTracer is enabled."""
    @staticmethod
    def check_device_type(device_type) -> None:
        """Checks if the given device type is valid."""
    @staticmethod
    def check_trace_mode(device_type, trace_mode) -> None:
        """Checks if the given trace mode work on the given device type.

    Args:
      device_type: Device type, TPU, GPU, CPU.
      trace_mode: Tensor tracer trace mode.
    Raises:
      ValueError: If the given trace mode is not supported for the device.
    """
    @staticmethod
    def loop_cond_op(op): ...
    @staticmethod
    def while_loop_op(op):
        """Returns true if op is one of the special ops of in a while loop.

    Args:
       op: A tf.Operation.

    Returns:
       True if the given op is one of [Switch, Merge, Enter, Exit,
       NextIteration, LoopCond], which are all building blocks for TF while
       loops.
    """
    @staticmethod
    def control_flow_op(op):
        """Returns true if op is one of the special ops of in a while loop.

    Args:
       op: A tf.Operation.

    Returns:
       True if the given op is one of [Switch, Merge, Enter, Exit,
       NextIteration, LoopCond], which are all building blocks for TF while
       loops.
    """
    @staticmethod
    def unsafe_op(op):
        """Returns True if this op is not safe to be traced."""
    @staticmethod
    def device_mismatch(device_type, op): ...
    @staticmethod
    def unsafe_scalar_trace(op):
        """Return true if scalar output tensor from Op is not safe to be traced."""
    @staticmethod
    def reason(op_idx, details):
        """Returns reason why the Op at op_idx is traced or not."""
    def __init__(self) -> None:
        """Initializes a TensorTracer.

    Sets the various member fields from the flags (if given) or the defaults.
    """
    def report_proto(self):
        """Getter for tensor_tracer.proto object for summary and full_tensor_summary modes.

    Returns:
      A tensor_tracer.proto object.
    Raises:
      ValueError if called before tracing happens, or when trace mode is not
      summary or full_tensor_summary.
    """
    def report_proto_path(self):
        """Getter for path where tensor_tracer.proto object should be written.

    Returns:
      A string path.
    """
    def merge_caches_on_tpu(self, local_tpu_cache_tensor):
        """Merges the given caches on tpu.

    Args:
      local_tpu_cache_tensor: A local tensor that needs to be merged
        by concanting data from other tpu cores.
    Returns:
      A merged tf.Tensor.
    """
    def aggregate_global_cache(self, global_tt_summary_cache):
        """Merges the given caches on tpu.

    Args:
      global_tt_summary_cache: The global tensor tracer summary cache tensor
        with shape (num_cores, num_traced_tensors, num_traced_signatures). First
        dimension corresponds to core_id, where global_tpu_cache_tensor[i]
        correspond to the local cache from core-i.
    Returns:
      An aggregated tf.Tensor.
    Raises:
      RuntimeError: if there is no aggregate function defined for a signature.
    """
    def host_call_deps_and_fn(self): ...
    def get_traced_op_names(self):
        """Returns the set of traced op names."""
    def trace_tpu(self, graph, tensor_fetches, op_fetches: Incomplete | None = None, num_replicas: Incomplete | None = None, num_replicas_per_host: Incomplete | None = None, num_hosts: Incomplete | None = None):
        """Traces the tensors generated by TPU Ops in a TF graph.

    Args:
      graph: the graph of Ops executed on the TPU.
      tensor_fetches: a (list,tuple,or a single object) of tensor fetches
        returned by model_fn given to session.run. Function must be provided
        with as least one tensor to fetch.
      op_fetches: A list of op fetches returned by model_fn given to
        session.run. op_fetches and tensor_fetches are used to determine the
        nodes that will be executed. Can be None.
      num_replicas: number of replicas used on the TPU.
      num_replicas_per_host: number of replicas per TPU host.
      num_hosts: total number of TPU hosts.

    Returns:
      tensor_fetches: an exact copy of tensor_fetches that has additional
                      dependencies.
    """
    def trace_cpu(self, graph, tensor_fetches, op_fetches: Incomplete | None = None):
        """Traces the tensors generated by CPU Ops in a TF graph.

    Args:
      graph: the graph of Ops executed on the CPU.
      tensor_fetches: a (list,tuple,or a single object) of tensor fetches
        returned by model_fn given to session.run. Function must be provided
        with as least one tensor to fetch.
      op_fetches: A list of op fetches returned by model_fn given to
        session.run. op_fetches and tensor_fetches are used to determine the
        nodes that will be executed. Can be None.

    Returns:
      tensor_fetches: an exact copy of tensor_fetches that has additional
                      dependencies.
    """
