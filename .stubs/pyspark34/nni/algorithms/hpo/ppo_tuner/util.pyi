from _typeshed import Incomplete

def set_global_seeds(i) -> None:
    """set global seeds"""
def batch_to_seq(h, nbatch, nsteps, flat: bool = False):
    """convert from batch to sequence"""
def seq_to_batch(h, flat: bool = False):
    """convert from sequence to batch"""
def lstm(xs, ms, s, scope, nh, init_scale: float = 1.0):
    """lstm cell"""
def lstm_model(nlstm: int = 128, layer_norm: bool = False):
    """
    Builds LSTM (Long-Short Term Memory) network to be used in a policy.
    Note that the resulting function returns not only the output of the LSTM
    (i.e. hidden state of lstm for each step in the sequence), but also a dictionary
    with auxiliary tensors to be set as policy attributes.

    Specifically,
        S is a placeholder to feed current state (LSTM state has to be managed outside policy)
        M is a placeholder for the mask (used to mask out observations after the end of the episode, but can be used for other purposes too)
        initial_state is a numpy array containing initial lstm state (usually zeros)
        state is the output LSTM state (to be fed into S at the next call)


    An example of usage of lstm-based policy can be found here: common/tests/test_doc_examples.py/test_lstm_example

    Parameters
    ----------
    nlstm : int
        LSTM hidden state size
    layer_norm : bool
        if True, layer-normalized version of LSTM is used

    Returns
    -------
    function that builds LSTM with a given input tensor / placeholder
    """
def ortho_init(scale: float = 1.0):
    """init approach"""
def fc(x, scope, nh, *, init_scale: float = 1.0, init_bias: float = 0.0):
    """fully connected op"""
def adjust_shape(placeholder, data):
    """
    adjust shape of the data to the shape of the placeholder if possible.
    If shape is incompatible, AssertionError is thrown

    Parameters
    ----------
    placeholder
        tensorflow input placeholder
    data
        input data to be (potentially) reshaped to be fed into placeholder

    Returns
    -------
    reshaped data
    """
def get_session(config: Incomplete | None = None):
    """Get default session or create one with a given config"""
def make_session(config: Incomplete | None = None, num_cpu: Incomplete | None = None, make_default: bool = False, graph: Incomplete | None = None):
    """Returns a session that will use <num_cpu> CPU's only"""

ALREADY_INITIALIZED: Incomplete

def initialize() -> None:
    """Initialize all the uninitialized variables in the global scope."""
def observation_placeholder(ob_space, batch_size: Incomplete | None = None, name: str = 'Ob'):
    """
    Create placeholder to feed observations into of the size appropriate to the observation space

    Parameters
    ----------
    ob_space : gym.Space
        observation space
    batch_size : int
        size of the batch to be fed into input. Can be left None in most cases.
    name : str
        name of the placeholder

    Returns
    -------
    tensorflow placeholder tensor
    """
def explained_variance(ypred, y):
    """
    Computes fraction of variance that ypred explains about y.
    Returns 1 - Var[y-ypred] / Var[y]

    interpretation:
        ev=0  =>  might as well have predicted zero
        ev=1  =>  perfect prediction
        ev<0  =>  worse than just predicting zero

    """
