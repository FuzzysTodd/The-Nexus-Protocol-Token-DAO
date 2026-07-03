from _typeshed import Incomplete
from collections.abc import Generator

def approximate_mode(class_counts, n_draws, rng):
    """Computes approximate mode of multivariate hypergeometric.
    This is an approximation to the mode of the multivariate
    hypergeometric given by class_counts and n_draws.
    It shouldn't be off by more than one.
    It is the mostly likely outcome of drawing n_draws many
    samples from the population given by class_counts.
    Args
    ----------
    class_counts : ndarray of int
        Population per class.
    n_draws : int
        Number of draws (samples to draw) from the overall population.
    rng : random state
        Used to break ties.
    Returns
    -------
    sampled_classes : ndarray of int
        Number of samples drawn from each class.
        np.sum(sampled_classes) == n_draws

    """
def stratified_shuffle_split_generate_indices(y, n_train, n_test, rng, n_splits: int = 10) -> Generator[Incomplete, None, None]:
    """

    Provides train/test indices to split data in train/test sets.
    It's reference is taken from StratifiedShuffleSplit implementation
    of scikit-learn library.

    Args
    ----------

    n_train : int,
        represents the absolute number of train samples.

    n_test : int,
        represents the absolute number of test samples.

    random_state : int or RandomState instance, default=None
        Controls the randomness of the training and testing indices produced.
        Pass an int for reproducible output across multiple function calls.

    n_splits : int, default=10
        Number of re-shuffling & splitting iterations.
    """
