from .distri import CategoricalPdType as CategoricalPdType
from .util import adjust_shape as adjust_shape, fc as fc, lstm_model as lstm_model, observation_placeholder as observation_placeholder
from _typeshed import Incomplete

class PolicyWithValue:
    """
    Encapsulates fields and methods for RL policy and value function estimation with shared parameters
    """
    X: Incomplete
    state: Incomplete
    initial_state: Incomplete
    np_mask: Incomplete
    pdtype: Incomplete
    act_latent: Incomplete
    nh: Incomplete
    action: Incomplete
    neglogp: Incomplete
    sess: Incomplete
    vf: Incomplete
    def __init__(self, env, observations, latent, estimate_q: bool = False, vf_latent: Incomplete | None = None, sess: Incomplete | None = None, np_mask: Incomplete | None = None, is_act_model: bool = False, **tensors) -> None:
        """
        Parameters
        ----------
        env : obj
            RL environment
        observations : tensorflow placeholder
            Tensorflow placeholder in which the observations will be fed
        latent : tensor
            Latent state from which policy distribution parameters should be inferred
        vf_latent : tensor
            Latent state from which value function should be inferred (if None, then latent is used)
        sess : tensorflow session
            Tensorflow session to run calculations in (if None, default session is used)
        **tensors
            Tensorflow tensors for additional attributes such as state or mask
        """
    def step(self, step, observation, **extra_feed):
        """
        Compute next action(s) given the observation(s)

        Parameters
        ----------
        observation : np array
            Observation data (either single or a batch)
        **extra_feed
            Additional data such as state or mask (names of the arguments should match the ones in constructor, see __init__)

        Returns
        -------
        (action, value estimate, next state, negative log likelihood of the action under current policy parameters) tuple
        """
    def value(self, ob, *args, **kwargs):
        """
        Compute value estimate(s) given the observation(s)

        Parameters
        ----------
        observation : np array
            Observation data (either single or a batch)
        **extra_feed
            Additional data such as state or mask (names of the arguments should match the ones in constructor, see __init__)

        Returns
        -------
        Value estimate
        """

def build_lstm_policy(model_config, value_network: Incomplete | None = None, estimate_q: bool = False, **policy_kwargs):
    """
    Build lstm policy and value network, they share the same lstm network.
    the parameters all use their default values.

    Parameter
    ---------
    model_config : obj
        Configurations of the model
    value_network : obj
        The network for value function
    estimate_q : bool
        Whether to estimate ``q``
    **policy_kwargs
        The kwargs for policy network, i.e., lstm model

    Returns
    -------
    func
        The policy network
    """
