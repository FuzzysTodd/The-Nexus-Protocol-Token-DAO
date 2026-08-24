from ._clean_simple import clean_dimensions as clean_dimensions, clean_init_score_and_X as clean_init_score_and_X, typify_classification as typify_classification
from ._clean_x import preclean_X as preclean_X
from ._compressed_dataset import bin_native_by_dimension as bin_native_by_dimension
from ._native import Native as Native
from ._preprocessor import construct_bins as construct_bins
from ._rank_interactions import rank_interactions as rank_interactions
from _typeshed import Incomplete

def measure_interactions(X, y, interactions: Incomplete | None = None, init_score: Incomplete | None = None, sample_weight: Incomplete | None = None, feature_names: Incomplete | None = None, feature_types: Incomplete | None = None, max_interaction_bins: int = 32, min_samples_leaf: int = 2, objective: Incomplete | None = None):
    '''Run the FAST algorithm and return the ranked interactions and their strengths as a dictionary.

    Args:
        X: Array of training samples
        y: Array of training targets
        interactions: Interactions to evaluate
            Either a list of tuples of feature indices, or an integer for the max number of pairs returned.
            None evaluates all pairwise interactions
        init_score: Either a model that can generate scores or per-sample initialization score.
            If samples scores it should be the same length as X and y.
        sample_weight: Optional array of weights per sample. Should be the same length as X and y
        feature_names: List of feature names
        feature_types: List of feature types, for example "continuous" or "nominal"
        max_interaction_bins: Max number of bins per interaction terms
        min_samples_leaf: Minimum number of samples for tree splits used when calculating gain
        objective: None (rmse or log_loss), "rmse" (regression default), "log_loss" (classification default),
            "poisson_deviance", "tweedie_deviance:variance_power=1.5", "gamma_deviance",
            "pseudo_huber:delta=1.0", "rmse_log" (rmse with a log link function)
    Returns:
        List containing a tuple of feature indices for the terms and interaction strengths,
            e.g. [((1, 2), 0.134), ((3, 7), 0.0842)].  Ordered by decreasing interaction strengths.
    '''
