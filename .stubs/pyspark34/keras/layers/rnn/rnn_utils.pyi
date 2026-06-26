from keras.utils import control_flow_util as control_flow_util

def standardize_args(inputs, initial_state, constants, num_constants):
    """Standardizes `__call__` to a single list of tensor inputs.

    When running a model loaded from a file, the input tensors
    `initial_state` and `constants` can be passed to `RNN.__call__()` as part
    of `inputs` instead of by the dedicated keyword arguments. This method
    makes sure the arguments are separated and that `initial_state` and
    `constants` are lists of tensors (or None).

    Args:
      inputs: Tensor or list/tuple of tensors. which may include constants
        and initial states. In that case `num_constant` must be specified.
      initial_state: Tensor or list of tensors or None, initial states.
      constants: Tensor or list of tensors or None, constant tensors.
      num_constants: Expected number of constants (if constants are passed as
        part of the `inputs` list.

    Returns:
      inputs: Single tensor or tuple of tensors.
      initial_state: List of tensors or None.
      constants: List of tensors or None.
    """
def is_multiple_state(state_size):
    """Check whether the state_size contains multiple states."""
def generate_zero_filled_state_for_cell(cell, inputs, batch_size, dtype): ...
def generate_zero_filled_state(batch_size_tensor, state_size, dtype):
    """Generate a zero filled tensor with shape [batch_size, state_size]."""
def caching_device(rnn_cell):
    """Returns the caching device for the RNN variable.

    This is useful for distributed training, when variable is not located as
    same device as the training worker. By enabling the device cache, this
    allows worker to read the variable once and cache locally, rather than read
    it every time step from remote when it is needed.

    Note that this is assuming the variable that cell needs for each time step
    is having the same value in the forward path, and only gets updated in the
    backprop. It is true for all the default cells (SimpleRNN, GRU, LSTM). If
    the cell body relies on any variable that gets updated every time step, then
    caching device will cause it to read the stall value.

    Args:
      rnn_cell: the rnn cell instance.
    """
def config_for_enable_caching_device(rnn_cell):
    """Return the dict config for RNN cell wrt to enable_caching_device field.

    Since enable_caching_device is a internal implementation detail for speed up
    the RNN variable read when running on the multi remote worker setting, we
    don't want this config to be serialized constantly in the JSON. We will only
    serialize this field when a none default value is used to create the cell.
    Args:
      rnn_cell: the RNN cell for serialize.

    Returns:
      A dict which contains the JSON config for enable_caching_device value or
      empty dict if the enable_caching_device value is same as the default
      value.
    """
