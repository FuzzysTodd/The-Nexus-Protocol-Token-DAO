from _typeshed import Incomplete

log: Incomplete

def model_to_graph_def(model, **kwargs):
    """
    Convert a Caffe2 model to a Tensorflow graph. This function extracts
    'param_init_net' and 'net' from the model and passes it to nets_to_graph()
    for further processing.

    Args:
        model (cnn.CNNModelHelper, model_helper.ModelHelper): The model to
            extract the nets (instances of core.Net) from.

    Returns:
        Call to nets_to_graph_def() with extracted 'param_init_net', 'net' and
            **kwargs. See _operators_to_graph_def for detailed **kwargs.
    """
def nets_to_graph_def(nets, shapes: Incomplete | None = None, **kwargs):
    """
    Convert a set of Caffe2 nets to a Tensorflow graph.

    Args:
        nets: List of core.Nets. core.Net is a wrapper around a NetDef protobuf.
            The corresponding protobuf can be extracted using .Proto().
        shapes: Dictionary mapping blob names to their shapes/dimensions.

    Returns:
        Call to protos_to_graph_def() with the extracted NetDef protobufs and
            **kwargs. See _operators_to_graph_def for detailed **kwargs.
    """
def protos_to_graph_def(net_defs, shapes: Incomplete | None = None, **kwargs):
    """
    Convert a set of Caffe2 net definitions to a Tensorflow graph.

    Args:
        net_defs: List of caffe2_pb2.NetDef protobufs representing computation
            graphs.
        shapes: Dictionary mapping blob names to their shapes/dimensions.

    Returns:
        Call to _operators_to_graph_def() with the extracted operators from the
            NetDefs and **kwargs. See _operators_to_graph_def for detailed
            **kwargs.
    """
