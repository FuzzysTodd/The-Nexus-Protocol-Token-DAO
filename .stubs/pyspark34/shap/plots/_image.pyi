import numpy as np
from . import colors as colors
from .._explanation import Explanation as Explanation
from ..utils import ordinal_str as ordinal_str
from ..utils._legacy import kmeans as kmeans
from matplotlib.colors import Colormap as Colormap

have_ipython: bool

def image(shap_values: None, pixel_values: np.ndarray | None = None, labels: None | None = None, true_labels: list | None = None, width: int | None = 20, aspect: float | None = 0.2, hspace: float | None = 0.2, labelpad: float | None = None, cmap: None | None = ..., show: bool | None = True):
    """Plots SHAP values for image inputs.

    Parameters
    ----------
    shap_values : [numpy.array]
        List of arrays of SHAP values. Each array has the shape
        (# samples x width x height x channels), and the
        length of the list is equal to the number of model outputs that are being
        explained.

    pixel_values : numpy.array
        Matrix of pixel values (# samples x width x height x channels) for each image.
        It should be the same
        shape as each array in the ``shap_values`` list of arrays.

    labels : list or np.ndarray
        List or ``np.ndarray`` (# samples x top_k classes) of names for each of the
        model outputs that are being explained.

    true_labels: list
        List of a true image labels to plot.

    width : float
        The width of the produced matplotlib plot.

    labelpad : float
        How much padding to use around the model output labels.

    show : bool
        Whether ``matplotlib.pyplot.show()`` is called before returning.
        Setting this to ``False`` allows the plot
        to be customized further after it has been created.

    Examples
    --------

    See `image plot examples <https://shap.readthedocs.io/en/latest/example_notebooks/api_examples/plots/image.html>`_.

    """
def image_to_text(shap_values) -> None:
    """ Plots SHAP values for image inputs with test outputs.

    Parameters
    ----------
    shap_values : [numpy.array]
        List of arrays of SHAP values. Each array has the shap (# width x height x channels x num output tokens). One array
        for each sample

    """
