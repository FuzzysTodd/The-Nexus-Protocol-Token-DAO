from tensorboard.compat.proto.graph_pb2 import GraphDef as GraphDef
from tensorboard.compat.tensorflow_stub import dtypes as dtypes

def keras_model_to_graph_def(keras_layer):
    """Returns a GraphDef representation of the Keras model in a dict form.

    Note that it only supports models that implemented to_json().

    Args:
      keras_layer: A dict from Keras model.to_json().

    Returns:
      A GraphDef representation of the layers in the model.
    """
