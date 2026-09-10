from _typeshed import Incomplete

def attr_value_proto(dtype, shape, s):
    """Creates a dict of objects matching
    https://github.com/tensorflow/tensorboard/blob/master/tensorboard/compat/proto/attr_value.proto
    specifically designed for a NodeDef. The values have been
    reverse engineered from standard TensorBoard logged data.
    """
def tensor_shape_proto(outputsize):
    """Creates an object matching
    https://github.com/tensorflow/tensorboard/blob/master/tensorboard/compat/proto/tensor_shape.proto
    """
def node_proto(name, op: str = 'UnSpecified', input: Incomplete | None = None, dtype: Incomplete | None = None, shape: tuple | None = None, outputsize: Incomplete | None = None, attributes: str = ''):
    """Creates an object matching
    https://github.com/tensorflow/tensorboard/blob/master/tensorboard/compat/proto/node_def.proto
    """
