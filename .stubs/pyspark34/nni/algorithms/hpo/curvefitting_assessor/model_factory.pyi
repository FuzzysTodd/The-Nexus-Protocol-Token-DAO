from .curvefunctions import *
from _typeshed import Incomplete

NUM_OF_FUNCTIONS: int
NUM_OF_SIMULATION_TIME: int
NUM_OF_INSTANCE: int
STEP_SIZE: float
LEAST_FITTED_FUNCTION: int
logger: Incomplete

class CurveModel:
    """Build a Curve Model to predict the performance

    Algorithm: https://github.com/Microsoft/nni/blob/master/src/sdk/pynni/nni/curvefitting_assessor/README.md

    Parameters
    ----------
    target_pos : int
        The point we need to predict
    """
    target_pos: Incomplete
    trial_history: Incomplete
    point_num: int
    effective_model: Incomplete
    effective_model_num: int
    weight_samples: Incomplete
    def __init__(self, target_pos) -> None: ...
    def fit_theta(self) -> None:
        """use least squares to fit all default curves parameter seperately

        Returns
        -------
        None
        """
    def filter_curve(self) -> None:
        """filter the poor performing curve

        Returns
        -------
        None
        """
    def predict_y(self, model, pos):
        """return the predict y of 'model' when epoch = pos

        Parameters
        ----------
        model : string
            name of the curve function model
        pos : int
            the epoch number of the position you want to predict

        Returns
        -------
        int
            The expected matrix at pos
        """
    def f_comb(self, pos, sample):
        """return the value of the f_comb when epoch = pos

        Parameters
        ----------
        pos : int
            the epoch number of the position you want to predict
        sample : list
            sample is a (1 * NUM_OF_FUNCTIONS) matrix, representing{w1, w2, ... wk}

        Returns
        -------
        int
            The expected matrix at pos with all the active function's prediction
        """
    def normalize_weight(self, samples):
        """normalize weight

        Parameters
        ----------
        samples : list
            a collection of sample, it's a (NUM_OF_INSTANCE * NUM_OF_FUNCTIONS) matrix,
            representing{{w11, w12, ..., w1k}, {w21, w22, ... w2k}, ...{wk1, wk2,..., wkk}}

        Returns
        -------
        list
            samples after normalize weight
        """
    def sigma_sq(self, sample):
        """returns the value of sigma square, given the weight's sample

        Parameters
        ----------
        sample : list
            sample is a (1 * NUM_OF_FUNCTIONS) matrix, representing{w1, w2, ... wk}

        Returns
        -------
        float
            the value of sigma square, given the weight's sample
        """
    def normal_distribution(self, pos, sample):
        """returns the value of normal distribution, given the weight's sample and target position

        Parameters
        ----------
        pos : int
            the epoch number of the position you want to predict
        sample : list
            sample is a (1 * NUM_OF_FUNCTIONS) matrix, representing{w1, w2, ... wk}

        Returns
        -------
        float
            the value of normal distribution
        """
    def likelihood(self, samples):
        """likelihood

        Parameters
        ----------
        sample : list
            sample is a (1 * NUM_OF_FUNCTIONS) matrix, representing{w1, w2, ... wk}

        Returns
        -------
        float
            likelihood
        """
    def prior(self, samples):
        """priori distribution

        Parameters
        ----------
        samples : list
            a collection of sample, it's a (NUM_OF_INSTANCE * NUM_OF_FUNCTIONS) matrix,
            representing{{w11, w12, ..., w1k}, {w21, w22, ... w2k}, ...{wk1, wk2,..., wkk}}

        Returns
        -------
        float
            priori distribution
        """
    def target_distribution(self, samples):
        """posterior probability

        Parameters
        ----------
        samples : list
            a collection of sample, it's a (NUM_OF_INSTANCE * NUM_OF_FUNCTIONS) matrix,
            representing{{w11, w12, ..., w1k}, {w21, w22, ... w2k}, ...{wk1, wk2,..., wkk}}

        Returns
        -------
        float
            posterior probability
        """
    def mcmc_sampling(self) -> None:
        """Adjust the weight of each function using mcmc sampling.
        The initial value of each weight is evenly distribute.
        Brief introduction:
        (1)Definition of sample:
            Sample is a (1 * NUM_OF_FUNCTIONS) matrix, representing{w1, w2, ... wk}
        (2)Definition of samples:
            Samples is a collection of sample, it's a (NUM_OF_INSTANCE * NUM_OF_FUNCTIONS) matrix,
            representing{{w11, w12, ..., w1k}, {w21, w22, ... w2k}, ...{wk1, wk2,..., wkk}}
        (3)Definition of model:
            Model is the function we chose right now. Such as: 'wap', 'weibull'.
        (4)Definition of pos:
            Pos is the position we want to predict, corresponds to the value of epoch.

        Returns
        -------
        None
        """
    def predict(self, trial_history):
        """predict the value of target position

        Parameters
        ----------
        trial_history : list
            The history performance matrix of each trial.

        Returns
        -------
        float
            expected final result performance of this hyperparameter config
        """
