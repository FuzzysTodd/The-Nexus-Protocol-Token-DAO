from .._explanation import Explanation as Explanation
from ..utils import safe_isinstance as safe_isinstance
from ..utils._legacy import DenseData as DenseData, IdentityLink as IdentityLink, SparseData as SparseData, convert_to_data as convert_to_data, convert_to_instance as convert_to_instance, convert_to_instance_with_index as convert_to_instance_with_index, convert_to_link as convert_to_link, convert_to_model as convert_to_model, match_instance_to_data as match_instance_to_data, match_model_to_data as match_model_to_data
from ._explainer import Explainer as Explainer
from _typeshed import Incomplete

log: Incomplete

class Kernel(Explainer):
    '''Uses the Kernel SHAP method to explain the output of any function.

    Kernel SHAP is a method that uses a special weighted linear regression
    to compute the importance of each feature. The computed importance values
    are Shapley values from game theory and also coefficients from a local linear
    regression.


    Parameters
    ----------
    model : function or iml.Model
        User supplied function that takes a matrix of samples (# samples x # features) and
        computes the output of the model for those samples. The output can be a vector
        (# samples) or a matrix (# samples x # model outputs).

    data : numpy.array or pandas.DataFrame or shap.common.DenseData or any scipy.sparse matrix
        The background dataset to use for integrating out features. To determine the impact
        of a feature, that feature is set to "missing" and the change in the model output
        is observed. Since most models aren\'t designed to handle arbitrary missing data at test
        time, we simulate "missing" by replacing the feature with the values it takes in the
        background dataset. So if the background dataset is a simple sample of all zeros, then
        we would approximate a feature being missing by setting it to zero. For small problems
        this background dataset can be the whole training set, but for larger problems consider
        using a single reference value or using the kmeans function to summarize the dataset.
        Note: for sparse case we accept any sparse matrix but convert to lil format for
        performance.

    feature_names : list
        The names of the features in the background dataset. If the background dataset is
        supplied as a pandas.DataFrame, then feature_names can be set to None (the default value)
        and the feature names will be taken as the column names of the dataframe.

    link : "identity" or "logit"
        A generalized linear model link to connect the feature importance values to the model
        output. Since the feature importance values, phi, sum up to the model output, it often makes
        sense to connect them to the output with a link function where link(output) = sum(phi).
        If the model output is a probability then the LogitLink link function makes the feature
        importance values have log-odds units.

    Examples
    --------
    See :ref:`Kernel Explainer Examples <kernel_explainer_examples>`
    '''
    data_feature_names: Incomplete
    link: Incomplete
    model: Incomplete
    keep_index: Incomplete
    keep_index_ordered: Incomplete
    data: Incomplete
    N: Incomplete
    P: Incomplete
    linkfv: Incomplete
    nsamplesAdded: int
    nsamplesRun: int
    fnull: Incomplete
    expected_value: Incomplete
    vector_out: bool
    D: int
    def __init__(self, model, data, feature_names: Incomplete | None = None, link=..., **kwargs) -> None: ...
    def __call__(self, X): ...
    def shap_values(self, X, **kwargs):
        ''' Estimate the SHAP values for a set of samples.

        Parameters
        ----------
        X : numpy.array or pandas.DataFrame or any scipy.sparse matrix
            A matrix of samples (# samples x # features) on which to explain the model\'s output.

        nsamples : "auto" or int
            Number of times to re-evaluate the model when explaining each prediction. More samples
            lead to lower variance estimates of the SHAP values. The "auto" setting uses
            `nsamples = 2 * X.shape[1] + 2048`.

        l1_reg : "num_features(int)", "auto" (default for now, but deprecated), "aic", "bic", or float
            The l1 regularization to use for feature selection (the estimation procedure is based on
            a debiased lasso). The auto option currently uses "aic" when less that 20% of the possible sample
            space is enumerated, otherwise it uses no regularization. THE BEHAVIOR OF "auto" WILL CHANGE
            in a future version to be based on num_features instead of AIC.
            The "aic" and "bic" options use the AIC and BIC rules for regularization.
            Using "num_features(int)" selects a fix number of top features. Passing a float directly sets the
            "alpha" parameter of the sklearn.linear_model.Lasso model used for feature selection.

        gc_collect : bool
           Run garbage collection after each explanation round. Sometime needed for memory intensive explanations (default False).

        Returns
        -------
        array or list
            For models with a single output this returns a matrix of SHAP values
            (# samples x # features). Each row sums to the difference between the model output for that
            sample and the expected value of the model output (which is stored as expected_value
            attribute of the explainer). For models with vector outputs this returns a list
            of such matrices, one for each output.
        '''
    varyingInds: Incomplete
    varyingFeatureGroups: Incomplete
    M: Incomplete
    fx: Incomplete
    l1_reg: Incomplete
    nsamples: Incomplete
    max_samples: Incomplete
    def explain(self, incoming_instance, **kwargs): ...
    @staticmethod
    def not_equal(i, j): ...
    def varying_groups(self, x): ...
    synth_data: Incomplete
    maskMatrix: Incomplete
    kernelWeights: Incomplete
    y: Incomplete
    ey: Incomplete
    lastMask: Incomplete
    synth_data_index: Incomplete
    def allocate(self) -> None: ...
    def addsample(self, x, m, w) -> None: ...
    def run(self) -> None: ...
    def solve(self, fraction_evaluated, dim): ...
