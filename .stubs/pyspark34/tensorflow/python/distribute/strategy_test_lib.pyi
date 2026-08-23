from tensorflow.core.protobuf import config_pb2 as config_pb2
from tensorflow.core.util import event_pb2 as event_pb2
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.distribute import distribute_lib as distribute_lib, distribute_utils as distribute_utils, reduce_util as reduce_util, tpu_strategy as tpu_strategy
from tensorflow.python.eager import backprop as backprop, context as context, def_function as def_function, test as test
from tensorflow.python.framework import dtypes as dtypes, errors as errors, ops as ops, test_util as test_util
from tensorflow.python.lib.io import tf_record as tf_record
from tensorflow.python.ops import array_ops as array_ops, gradients_impl as gradients_impl, init_ops as init_ops, init_ops_v2 as init_ops_v2, math_ops as math_ops, variable_scope as variable_scope, variables as variables
from tensorflow.python.platform import gfile as gfile
from tensorflow.python.training import optimizer as optimizer, training_util as training_util
from tensorflow.python.util import nest as nest, tf_inspect as tf_inspect

class _TestException(Exception): ...

def create_variable_like_keras_layer(name, shape, dtype):
    """Utitlity for create variables that works like variable in keras layer."""
def is_optimizer_v2_instance(optimizer_obj): ...
def is_mirrored_strategy(strategy: distribute_lib.Strategy) -> bool: ...
def is_multi_worker_mirrored_strategy(strategy: distribute_lib.Strategy) -> bool: ...
def is_tpu_strategy(strategy: distribute_lib.Strategy) -> bool: ...

class DistributionTestBase(test.TestCase):
    """Some tests that should work with any DistributionStrategy."""
class OneDeviceDistributionTestBase(test.TestCase):
    """Some tests that should work with any one-device DistributionStrategy."""
class TwoDeviceDistributionTestBase(test.TestCase):
    """Some tests that should work with any two-device DistributionStrategy."""
class RemoteSingleWorkerMirroredStrategyBase(DistributionTestBase):
    """Tests for a Remote single worker."""
