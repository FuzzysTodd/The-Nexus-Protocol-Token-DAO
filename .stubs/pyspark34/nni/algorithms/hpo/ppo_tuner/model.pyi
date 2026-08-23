from .util import get_session as get_session, initialize as initialize
from _typeshed import Incomplete

class Model:
    """
    We use this object to :
        __init__:
            - Creates the step_model
            - Creates the train_model

        train():
            - Make the training part (feedforward and retropropagation of gradients)

        save/load():
            - Save load the model
    """
    sess: Incomplete
    A: Incomplete
    ADV: Incomplete
    R: Incomplete
    OLDNEGLOGPAC: Incomplete
    OLDVPRED: Incomplete
    LR: Incomplete
    CLIPRANGE: Incomplete
    trainer: Incomplete
    grads: Incomplete
    var: Incomplete
    loss_names: Incomplete
    stats_list: Incomplete
    train_model: Incomplete
    act_model: Incomplete
    step: Incomplete
    value: Incomplete
    initial_state: Incomplete
    def __init__(self, *, policy, nbatch_act, nbatch_train, nsteps, ent_coef, vf_coef, max_grad_norm, microbatch_size: Incomplete | None = None, np_mask: Incomplete | None = None) -> None: ...
    def train(self, lr, cliprange, obs, returns, masks, actions, values, neglogpacs, states: Incomplete | None = None):
        """
        Train the model.
        Here we calculate advantage A(s,a) = R + yV(s') - V(s)

        Returns
        -------
        obj
            = R + yV(s')
        """
