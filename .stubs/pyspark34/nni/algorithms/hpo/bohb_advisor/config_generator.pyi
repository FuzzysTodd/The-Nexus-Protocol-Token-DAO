from _typeshed import Incomplete

logger: Incomplete

class CG_BOHB:
    top_n_percent: Incomplete
    configspace: Incomplete
    bw_factor: Incomplete
    min_bandwidth: Incomplete
    min_points_in_model: Incomplete
    num_samples: Incomplete
    random_fraction: Incomplete
    kde_vartypes: str
    vartypes: Incomplete
    cat_probs: Incomplete
    configs: Incomplete
    losses: Incomplete
    good_config_rankings: Incomplete
    kde_models: Incomplete
    def __init__(self, configspace, min_points_in_model: Incomplete | None = None, top_n_percent: int = 15, num_samples: int = 64, random_fraction=..., bandwidth_factor: int = 3, min_bandwidth: float = 0.001) -> None:
        """Fits for each given budget a kernel density estimator on the best N percent of the
        evaluated configurations on this budget.


        Parameters:
        -----------
        configspace: ConfigSpace
            Configuration space object
        top_n_percent: int
            Determines the percentile of configurations that will be used as training data
            for the kernel density estimator, e.g if set to 10 the 10% best configurations will be considered
            for training.
        min_points_in_model: int
            minimum number of datapoints needed to fit a model
        num_samples: int
            number of samples drawn to optimize EI via sampling
        random_fraction: float
            fraction of random configurations returned
        bandwidth_factor: float
            widens the bandwidth for contiuous parameters for proposed points to optimize EI
        min_bandwidth: float
            to keep diversity, even when all (good) samples have the same value for one of the parameters,
            a minimum bandwidth (Default: 1e-3) is used instead of zero.
        """
    def largest_budget_with_model(self): ...
    def sample_from_largest_budget(self, info_dict):
        '''We opted for a single multidimensional KDE compared to the
        hierarchy of one-dimensional KDEs used in TPE. The dimensional is
        seperated by budget. This function sample a configuration from
        largest budget. Firstly we sample "num_samples" configurations,
        then prefer one with the largest l(x)/g(x).

        Parameters:
        -----------
        info_dict: dict
            record the information of this configuration

        Returns
        -------
        dict:
            new configuration named sample
        dict:
            info_dict, record the information of this configuration
        '''
    def get_config(self, budget):
        """Function to sample a new configuration
        This function is called inside BOHB to query a new configuration

        Parameters:
        -----------
        budget: float
            the budget for which this configuration is scheduled

        Returns
        -------
        config
            return a valid configuration with parameters and budget
        """
    def impute_conditional_data(self, array): ...
    def new_result(self, loss, budget, parameters, update_model: bool = True) -> None:
        """
        Function to register finished runs. Every time a run has finished, this function should be called
        to register it with the loss.

        Parameters:
        -----------
        loss: float
            the loss of the parameters
        budget: float
            the budget of the parameters
        parameters: dict
            the parameters of this trial
        update_model: bool
            whether use this parameter to update BP model

        Returns
        -------
        None
        """
