from .._explainer import Explainer as Explainer
from _typeshed import Incomplete

class LimeTabular(Explainer):
    ''' Simply wrap of lime.lime_tabular.LimeTabularExplainer into the common shap interface.

    Parameters
    ----------
    model : function or iml.Model
        User supplied function that takes a matrix of samples (# samples x # features) and
        computes the output of the model for those samples. The output can be a vector
        (# samples) or a matrix (# samples x # model outputs).

    data : numpy.array
        The background dataset.

    mode : "classification" or "regression"
        Control the mode of LIME tabular.
    '''
    model: Incomplete
    mode: Incomplete
    data: Incomplete
    explainer: Incomplete
    out_dim: int
    flat_out: bool
    def __init__(self, model, data, mode: str = 'classification') -> None: ...
    def attributions(self, X, nsamples: int = 5000, num_features: Incomplete | None = None): ...
