from _typeshed import Incomplete
from tensorflow.core.framework import graph_pb2 as graph_pb2
from tensorflow.core.protobuf import config_pb2 as config_pb2

def OptimizeGraph(config_proto, metagraph, verbose: bool = True, graph_id: bytes = b'graph_to_optimize', cluster: Incomplete | None = None, strip_default_attributes: bool = False):
    """Optimize the provided metagraph.

  For best results, the signature_def field in `metagraph` should be populated
  with information about input (feed) and output (fetch) tensors.

  Args:
    config_proto: a ConfigProto protobuf.
    metagraph: a MetagraphDef protobuf.
    verbose: whether to log optimization results.
    graph_id: a string identifying this graph.
    cluster: a grappler cluster object representing hardware resources
        available to run this graph.
    strip_default_attributes: whether graph node attributes having default
        values should be removed after all the optimization passes. This
        option is useful if the resulting graph will be executed by an older
        process that might not know some of the recently added attributes.
  """
