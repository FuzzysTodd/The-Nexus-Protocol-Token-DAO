from .._explanation import Explanation as Explanation
from ..utils import safe_isinstance as safe_isinstance
from ..utils._legacy import convert_to_instance as convert_to_instance, match_instance_to_data as match_instance_to_data
from ._kernel import Kernel as Kernel
from _typeshed import Incomplete

log: Incomplete

class Sampling(Kernel):
    ''' This is an extension of the Shapley sampling values explanation method (aka. IME)

    SamplingExplainer computes SHAP values under the assumption of feature independence and is an
    extension of the algorithm proposed in "An Efficient Explanation of Individual Classifications
    using Game Theory", Erik Strumbelj, Igor Kononenko, JMLR 2010. It is a good alternative to
    KernelExplainer when you want to use a large background set (as opposed to a single reference
    value for example).

    Parameters
    ----------
    model : function
        User supplied function that takes a matrix of samples (# samples x # features) and
        computes the output of the model for those samples. The output can be a vector
        (# samples) or a matrix (# samples x # model outputs).

    data : numpy.array or pandas.DataFrame
        The background dataset to use for integrating out features. To determine the impact
        of a feature, that feature is set to "missing" and the change in the model output
        is observed. Since most models aren\'t designed to handle arbitrary missing data at test
        time, we simulate "missing" by replacing the feature with the values it takes in the
        background dataset. So if the background dataset is a simple sample of all zeros, then
        we would approximate a feature being missing by setting it to zero. Unlike the
        KernelExplainer this data can be the whole training set, even if that is a large set. This
        is because SamplingExplainer only samples from this background dataset.
    '''
    def __init__(self, model, data, **kwargs) -> None: ...
    def __call__(self, X, y: Incomplete | None = None, nsamples: int = 2000): ...
    varyingInds: Incomplete
    M: Incomplete
    fx: Incomplete
    nsamples: Incomplete
    X_masked: Incomplete
    def explain(self, incoming_instance, **kwargs): ...
    def sampling_estimate(self, j, f, x, X, nsamples: int = 10): ...
