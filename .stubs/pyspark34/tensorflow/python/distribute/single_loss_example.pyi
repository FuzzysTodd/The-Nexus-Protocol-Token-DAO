from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.distribute import step_fn as step_fn, strategy_test_lib as strategy_test_lib
from tensorflow.python.framework import constant_op as constant_op, ops as ops
from tensorflow.python.layers import core as core, normalization as normalization
from tensorflow.python.ops import array_ops as array_ops, math_ops as math_ops

def single_loss_example(optimizer_fn, distribution, use_bias: bool = False, iterations_per_step: int = 1):
    """Build a very simple network to use in tests and examples."""
def minimize_loss_example(optimizer, use_bias: bool = False, use_callable_loss: bool = True):
    """Example of non-distribution-aware legacy code."""
def batchnorm_example(optimizer_fn, batch_per_epoch: int = 1, momentum: float = 0.9, renorm: bool = False, update_ops_in_replica_mode: bool = False):
    """Example of non-distribution-aware legacy code with batch normalization."""
