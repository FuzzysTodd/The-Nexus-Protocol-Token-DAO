from .._explainer import Explainer as Explainer
from _typeshed import Incomplete

class Maple(Explainer):
    """ Simply wraps MAPLE into the common SHAP interface.

    Parameters
    ----------
    model : function
        User supplied function that takes a matrix of samples (# samples x # features) and
        computes the output of the model for those samples. The output can be a vector
        (# samples) or a matrix (# samples x # model outputs).

    data : numpy.array
        The background dataset.
    """
    model: Incomplete
    data: Incomplete
    data_mean: Incomplete
    out_dim: int
    flat_out: bool
    explainer: Incomplete
    def __init__(self, model, data) -> None: ...
    def attributions(self, X, multiply_by_input: bool = False):
        """ Compute the MAPLE coef attributions.

        Parameters
        ----------
        multiply_by_input : bool
            If true, this multiplies the learned coefficients by the mean-centered input. This makes these
            values roughly comparable to SHAP values.
        """

class TreeMaple(Explainer):
    """ Simply tree MAPLE into the common SHAP interface.

    Parameters
    ----------
    model : function
        User supplied function that takes a matrix of samples (# samples x # features) and
        computes the output of the model for those samples. The output can be a vector
        (# samples) or a matrix (# samples x # model outputs).

    data : numpy.array
        The background dataset.
    """
    model: Incomplete
    data: Incomplete
    data_mean: Incomplete
    out_dim: int
    flat_out: bool
    explainer: Incomplete
    def __init__(self, model, data) -> None: ...
    def attributions(self, X, multiply_by_input: bool = False):
        """ Compute the MAPLE coef attributions.

        Parameters
        ----------
        multiply_by_input : bool
            If true, this multiplies the learned coeffients by the mean-centered input. This makes these
            values roughly comparable to SHAP values.
        """

class MAPLE:
    X_train: Incomplete
    MR_train: Incomplete
    X_val: Incomplete
    MR_val: Incomplete
    n_estimators: Incomplete
    max_features: Incomplete
    min_samples_leaf: Incomplete
    regularization: Incomplete
    num_features: Incomplete
    num_train: Incomplete
    fe: Incomplete
    train_leaf_ids: Incomplete
    feature_scores: Incomplete
    retain: Incomplete
    X: Incomplete
    def __init__(self, X_train, MR_train, X_val, MR_val, fe_type: str = 'rf', fe: Incomplete | None = None, n_estimators: int = 200, max_features: float = 0.5, min_samples_leaf: int = 10, regularization: float = 0.001) -> None: ...
    def training_point_weights(self, instance_leaf_ids): ...
    def explain(self, x): ...
    def predict(self, X): ...
    def predict_fe(self, X): ...
    def predict_silo(self, X): ...
