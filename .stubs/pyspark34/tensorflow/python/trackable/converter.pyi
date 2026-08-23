from _typeshed import Incomplete
from tensorflow.python.eager.polymorphic_function import saved_model_utils as saved_model_utils
from tensorflow.python.framework import dtypes as dtypes, tensor_util as tensor_util
from tensorflow.python.ops import resource_variable_ops as resource_variable_ops
from tensorflow.python.trackable import base as base, data_structures as data_structures

def convert_to_trackable(obj, parent: Incomplete | None = None):
    """Converts `obj` to `Trackable`."""
