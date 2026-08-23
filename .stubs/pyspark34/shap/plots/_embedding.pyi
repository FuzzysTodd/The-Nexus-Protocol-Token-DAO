from . import colors as colors
from ..utils import convert_name as convert_name
from ._labels import labels as labels
from _typeshed import Incomplete

def embedding(ind, shap_values, feature_names: Incomplete | None = None, method: str = 'pca', alpha: float = 1.0, show: bool = True) -> None:
    ''' Use the SHAP values as an embedding which we project to 2D for visualization.

    Parameters
    ----------
    ind : int or string
        If this is an int it is the index of the feature to use to color the embedding.
        If this is a string it is either the name of the feature, or it can have the
        form "rank(int)" to specify the feature with that rank (ordered by mean absolute
        SHAP value over all the samples), or "sum()" to mean the sum of all the SHAP values,
        which is the model\'s output (minus it\'s expected value).

    shap_values : numpy.array
        Matrix of SHAP values (# samples x # features).

    feature_names : None or list
        The names of the features in the shap_values array.

    method : "pca" or numpy.array
        How to reduce the dimensions of the shap_values to 2D. If "pca" then the 2D
        PCA projection of shap_values is used. If a numpy array then is should be
        (# samples x 2) and represent the embedding of that values.

    alpha : float
        The transparency of the data points (between 0 and 1). This can be useful to the
        show density of the data points when using a large dataset.
    '''
