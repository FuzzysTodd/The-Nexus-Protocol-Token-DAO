from _typeshed import Incomplete
from tensorflow.python.platform import gfile as gfile
from tensorflow.python.tpu import tensor_tracer_pb2 as tensor_tracer_pb2

def topological_sort(g):
    """Performs topological sort on the given graph.

  Args:
     g: the graph.

  Returns:
     A pair where the first element indicates if the topological
     sort succeeded (True if there is no cycle found; False if a
     cycle is found) and the second element is either the sorted
     list of nodes or the cycle of nodes found.
  """

class TensorTracerConfig:
    """Tensor Tracer config object."""
    version: Incomplete
    device_type: Incomplete
    num_replicas: Incomplete
    num_replicas_per_host: Incomplete
    num_hosts: Incomplete
    def __init__(self) -> None: ...

class TensorTraceOrder:
    """Class that is responsible from storing the trace-id of the tensors."""
    graph_order: Incomplete
    traced_tensors: Incomplete
    def __init__(self, graph_order, traced_tensors) -> None: ...

def sort_tensors_and_ops(graph):
    """Returns a wrapper that has consistent tensor and op orders."""

class OpenReportFile:
    """Context manager for writing report file."""
    def __init__(self, tt_parameters) -> None: ...
    def __enter__(self): ...
    def __exit__(self, unused_type: type[BaseException] | None, unused_value: BaseException | None, unused_traceback: types.TracebackType | None) -> None: ...

def proto_fingerprint(message_proto): ...

class TTReportHandle:
    """Utility class responsible from creating a tensor tracer report."""
    instrument_records: Incomplete
    def __init__(self) -> None: ...
    def instrument(self, name, explanation) -> None: ...
    def instrument_op(self, op, explanation) -> None: ...
    def instrument_tensor(self, tensor, explanation) -> None: ...
    def create_report_proto(self, tt_config, tt_parameters, tensor_trace_order, tensor_trace_points, collected_signature_types):
        """Creates and returns a proto that stores tensor tracer configuration.

    Args:
      tt_config: TensorTracerConfig object holding information about the run
        environment (device, # cores, # hosts), and tensor tracer version
        information.
      tt_parameters: TTParameters objects storing the user provided parameters
        for tensor tracer.
      tensor_trace_order: TensorTraceOrder object storing a topological order of
        the graph.
      tensor_trace_points: Progromatically added trace_points/checkpoints.
      collected_signature_types: The signature types collected, e,g, norm,
        max, min, mean...
    Returns:
      TensorTracerReport proto.
    """
    def report_proto_path(self, trace_dir, summary_tag_name):
        """Returns the path where report proto should be written.

    Args:
      trace_dir: String denoting the trace directory.
      summary_tag_name: Name of the unique tag that relates to
                        the report.
    Returns:
      A string denoting the path to the report proto.
    """
    def write_report_proto(self, report_path, report_proto, tt_parameters) -> None:
        """Writes the given report proto under trace_dir."""
    def create_report(self, tt_config, tt_parameters, tensor_trace_order, tensor_trace_points) -> None:
        """Creates a report file and writes the trace information."""
