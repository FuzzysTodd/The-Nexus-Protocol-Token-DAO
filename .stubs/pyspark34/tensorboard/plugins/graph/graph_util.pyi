from tensorboard.compat.proto import graph_pb2 as graph_pb2

def merge_graph_defs(graph_defs):
    '''Merges GraphDefs by adding unique prefix, `graph_{ind}`, to names.

    All GraphDefs are expected to be of TensorBoard\'s.

    When collecting graphs using the `tf.summary.trace` API, node names are not
    guranteed to be unique.  When non-unique names are not considered, it can
    lead to graph visualization showing them as one which creates inaccurate
    depiction of the flow of the graph (e.g., if there are A -> B -> C and D ->
    B -> E, you may see {A, D} -> B -> E).  To prevent such graph, we checked
    for uniquenss while merging but it resulted in
    https://github.com/tensorflow/tensorboard/issues/1929.

    To remedy these issues, we simply "apply name scope" on each graph by
    prefixing it with unique name (with a chance of collision) to create
    unconnected group of graphs.

    In case there is only one graph def passed, it returns the original
    graph_def. In case no graph defs are passed, it returns an empty GraphDef.

    Args:
      graph_defs: TensorBoard GraphDefs to merge.

    Returns:
      TensorBoard GraphDef that merges all graph_defs with unique prefixes.

    Raises:
      ValueError in case GraphDef versions mismatch.
    '''
