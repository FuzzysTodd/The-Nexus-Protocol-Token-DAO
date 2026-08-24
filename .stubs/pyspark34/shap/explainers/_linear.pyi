from .. import links as links, maskers as maskers
from ..utils import safe_isinstance as safe_isinstance
from ..utils._exceptions import DimensionError as DimensionError, InvalidFeaturePerturbationError as InvalidFeaturePerturbationError, InvalidModelError as InvalidModelError
from ._explainer import Explainer as Explainer
from _typeshed import Incomplete

class Linear(Explainer):
    ''' Computes SHAP values for a linear model, optionally accounting for inter-feature correlations.

    This computes the SHAP values for a linear model and can account for the correlations among
    the input features. Assuming features are independent leads to interventional SHAP values which
    for a linear model are coef[i] * (x[i] - X.mean(0)[i]) for the ith feature. If instead we account
    for correlations then we prevent any problems arising from collinearity and share credit among
    correlated features. Accounting for correlations can be computationally challenging, but
    LinearExplainer uses sampling to estimate a transform that can then be applied to explain
    any prediction of the model.

    Parameters
    ----------
    model : (coef, intercept) or sklearn.linear_model.*
        User supplied linear model either as either a parameter pair or sklearn object.

    data : (mean, cov), numpy.array, pandas.DataFrame, iml.DenseData or scipy.csr_matrix
        The background dataset to use for computing conditional expectations. Note that only the
        mean and covariance of the dataset are used. This means passing a raw data matrix is just
        a convenient alternative to passing the mean and covariance directly.
    nsamples : int
        Number of samples to use when estimating the transformation matrix used to account for
        feature correlations.
    feature_perturbation : "interventional" (default) or "correlation_dependent"
        There are two ways we might want to compute SHAP values, either the full conditional SHAP
        values or the interventional SHAP values. For interventional SHAP values we break any
        dependence structure between features in the model and so uncover how the model would behave if we
        intervened and changed some of the inputs. For the full conditional SHAP values we respect
        the correlations among the input features, so if the model depends on one input but that
        input is correlated with another input, then both get some credit for the model\'s behavior. The
        interventional option stays "true to the model" meaning it will only give credit to features that are
        actually used by the model, while the correlation option stays "true to the data" in the sense that
        it only considers how the model would behave when respecting the correlations in the input data.
        For sparse case only interventional option is supported.

    Examples
    --------
    See `Linear explainer examples <https://shap.readthedocs.io/en/latest/api_examples/explainers/Linear.html>`_
    '''
    feature_perturbation: Incomplete
    nsamples: Incomplete
    mean: Incomplete
    cov: Incomplete
    expected_value: Incomplete
    M: Incomplete
    valid_inds: Incomplete
    coef: Incomplete
    mean_transformed: Incomplete
    x_transform: Incomplete
    def __init__(self, model, masker, link=..., nsamples: int = 1000, feature_perturbation: Incomplete | None = None, **kwargs) -> None: ...
    @staticmethod
    def supports_model_with_masker(model, masker):
        """ Determines if we can parse the given model.
        """
    def explain_row(self, *row_args, max_evals, main_effects, error_bounds, batch_size, outputs, silent):
        """ Explains a single row and returns the tuple (row_values, row_expected_values, row_mask_shapes).
        """
    def shap_values(self, X):
        """ Estimate the SHAP values for a set of samples.

        Parameters
        ----------
        X : numpy.array, pandas.DataFrame or scipy.csr_matrix
            A matrix of samples (# samples x # features) on which to explain the model's output.

        Returns
        -------
        array or list
            For models with a single output this returns a matrix of SHAP values
            (# samples x # features). Each row sums to the difference between the model output for that
            sample and the expected value of the model output (which is stored as expected_value
            attribute of the explainer).
        """

def duplicate_components(C): ...
