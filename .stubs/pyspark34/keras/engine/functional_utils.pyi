from keras import backend as backend
from keras.engine import keras_tensor as keras_tensor

def is_input_keras_tensor(tensor):
    """Check if tensor is directly generated from `tf.keras.Input`.

    This check is useful when constructing the functional model, since we will
    need to clone Nodes and KerasTensors if the model is building from non input
    tensor.

    Args:
      tensor: A `KerasTensor` as inputs to the functional model.

    Returns:
      bool. Whether the tensor is directly generated from `tf.keras.Input`.

    Raises:
      ValueError: if the tensor is not a KerasTensor instance.
    """
def find_nodes_by_inputs_and_outputs(inputs, outputs):
    '''Fetch all Nodes in the graph defined by "inputs" and "outputs".

    This method is used to find and then clone Nodes when creating a new
    sub-model from an existing functional model.

    Args:
      inputs: A nested structure of KerasTensor to use as model inputs.
      outputs: A nested structure of KerasTensor to use as model outputs.

    Returns:
      A list of Nodes that are connected to the inputs and outputs.

    Raises:
      ValueError: when inputs and outputs are disconnected or in case of
        unexpected objects in the inputs/outputs.
    '''
def clone_graph_nodes(inputs, outputs):
    """Clone the `Node` between the inputs and output tensors.

    This function is used to create a new functional model from any intermediate
    keras tensors. The clone of the nodes mimic the behavior of reconstructing
    the functional graph network by re-executing all the __call__ methods. The
    cloned nodes will be appended to the layers.

    Note that a new tf.keras.Inputs will be created for any items in the
    `inputs`

    Args:
      inputs: A nested structure of keras_tensors.
      outputs: A nested structure of keras_tensors.

    Returns:
      A pair of inputs and outputs, with cloned keras_tensors. They can be used
      to create a new functional model.
    """
def clone_keras_tensors(args, keras_tensor_mapping):
    """Clone the keras tensors from the inputs.

    For any KerasTensor instance in the `args`, a new copy of KerasTensor will
    be created if it has not been cloned yet (by checking the
    `keras_tensor_mapping`). For any other types, the instance will be
    unchanged. This function is useful for cloning the Nodes since KerasTensor
    can't be reused across the models.

    Args:
      args: A nested structure of objects, which could contain KerasTensor.
      keras_tensor_mapping: A dict contains the ID of original KerasTensor, and
        the cloned KerasTensor instance. The dict will be updated with newly
        copied KerasTensor instances within this method.
    Returns:
      Same structure as inputs, with KerasTensor cloned.
    """
