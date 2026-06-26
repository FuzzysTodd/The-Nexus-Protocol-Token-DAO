from . import constants as constants, syssettings as syssettings
from .learnability import Solver as Solver
from .utils import EMA as EMA
from _typeshed import Incomplete

def get_optim_f_stop(maxiter, maxtime, dftol_stop, freltol_stop, minibatch: bool = True):
    """
    Check stopping conditions.
    """
def get_init(data_train, init_type: str = 'on', rng=..., prev_score: Incomplete | None = None):
    """
    Initialize the 'x' variable with different settings
    """
def get_checkpoint(S, stop_conds, rng: Incomplete | None = None, get_state: bool = True):
    """
    Save the necessary information into a dictionary
    """
def train_sk_dense(ty, X, y, classification): ...
