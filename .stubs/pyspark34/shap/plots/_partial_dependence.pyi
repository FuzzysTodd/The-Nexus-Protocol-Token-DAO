from .. import Explanation as Explanation
from ..plots.colors import blue_rgb as blue_rgb, light_blue_rgb as light_blue_rgb, red_blue_transparent as red_blue_transparent, red_rgb as red_rgb
from ..utils import convert_name as convert_name
from _typeshed import Incomplete

def compute_bounds(xmin, xmax, xv):
    ''' Handles any setting of xmax and xmin.

    Note that we handle None, float, or "percentile(float)" formats.
    '''
def partial_dependence(ind, model, data, xmin: str = 'percentile(0)', xmax: str = 'percentile(100)', npoints: Incomplete | None = None, feature_names: Incomplete | None = None, hist: bool = True, model_expected_value: bool = False, feature_expected_value: bool = False, shap_values: Incomplete | None = None, ylabel: Incomplete | None = None, ice: bool = True, ace_opacity: int = 1, pd_opacity: int = 1, pd_linewidth: int = 2, ace_linewidth: str = 'auto', ax: Incomplete | None = None, show: bool = True):
    """ A basic partial dependence plot function.
    """
