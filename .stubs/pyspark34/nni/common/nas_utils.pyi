from .. import trial as trial
from _typeshed import Incomplete

def classic_mode(mutable_id, mutable_layer_id, funcs, funcs_args, fixed_inputs, optional_inputs, optional_input_size):
    """Execute the chosen function and inputs directly.
    In this mode, the trial code is only running the chosen subgraph (i.e., the chosen ops and inputs),
    without touching the full model graph."""
def enas_mode(mutable_id, mutable_layer_id, funcs, funcs_args, fixed_inputs, optional_inputs, optional_input_size, tf):
    """For enas mode, we build the full model graph in trial but only run a subgraph。
    This is implemented by masking inputs and branching ops.
    Specifically, based on the received subgraph (through nni.get_next_parameter),
    it can be known which inputs should be masked and which op should be executed."""
def oneshot_mode(mutable_id, mutable_layer_id, funcs, funcs_args, fixed_inputs, optional_inputs, optional_input_size, tf):
    """Similar to enas mode, oneshot mode also builds the full model graph.
    The difference is that oneshot mode does not receive subgraph.
    Instead, it uses dropout to randomly dropout inputs and ops."""
def darts_mode(mutable_id, mutable_layer_id, funcs, funcs_args, fixed_inputs, optional_inputs, optional_input_size, tf): ...
def reload_tensorflow_variables(tf, session) -> None:
    """In Enas mode, this function reload every signal varaible created in `enas_mode` function so
    the whole tensorflow graph will be changed into certain subgraph recerived from Tuner.
    ---------------
    session: the tensorflow session created by users
    tf: tensorflow module
    """
def darts_training(tf, session, loss, feed_dict) -> None: ...
def training_update(nas_mode, tf: Incomplete | None = None, session: Incomplete | None = None, loss: Incomplete | None = None, feed_dict: Incomplete | None = None) -> None: ...
def convert_nas_search_space(search_space):
    """
    Args:
        param search_space: raw search space
        return: the new search space, mutable_layers will be converted into choice
    """
def rewrite_nas_space(func): ...
