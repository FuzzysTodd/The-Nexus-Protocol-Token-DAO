from .. import DeepExplainer as DeepExplainer, GradientExplainer as GradientExplainer, KernelExplainer as KernelExplainer, LinearExplainer as LinearExplainer, SamplingExplainer as SamplingExplainer, TreeExplainer as TreeExplainer, kmeans as kmeans
from ..explainers import other as other
from .models import KerasWrap as KerasWrap

def linear_shap_corr(model, data):
    """ Linear SHAP (corr 1000)
    """
def linear_shap_ind(model, data):
    """ Linear SHAP (ind)
    """
def coef(model, data):
    """ Coefficients
    """
def random(model, data):
    """ Random
    color = #777777
    linestyle = solid
    """
def kernel_shap_1000_meanref(model, data):
    """ Kernel SHAP 1000 mean ref.
    color = red_blue_circle(0.5)
    linestyle = solid
    """
def sampling_shap_1000(model, data):
    """ IME 1000
    color = red_blue_circle(0.5)
    linestyle = dashed
    """
def tree_shap_tree_path_dependent(model, data):
    """ TreeExplainer
    color = red_blue_circle(0)
    linestyle = solid
    """
def tree_shap_independent_200(model, data):
    """ TreeExplainer (independent)
    color = red_blue_circle(0)
    linestyle = dashed
    """
def mean_abs_tree_shap(model, data):
    """ mean(|TreeExplainer|)
    color = red_blue_circle(0.25)
    linestyle = solid
    """
def saabas(model, data):
    """ Saabas
    color = red_blue_circle(0)
    linestyle = dotted
    """
def tree_gain(model, data):
    """ Gain/Gini Importance
    color = red_blue_circle(0.25)
    linestyle = dotted
    """
def lime_tabular_regression_1000(model, data):
    """ LIME Tabular 1000
    color = red_blue_circle(0.75)
    """
def lime_tabular_classification_1000(model, data):
    """ LIME Tabular 1000
    color = red_blue_circle(0.75)
    """
def maple(model, data):
    """ MAPLE
    color = red_blue_circle(0.6)
    """
def tree_maple(model, data):
    """ Tree MAPLE
    color = red_blue_circle(0.6)
    linestyle = dashed
    """
def deep_shap(model, data):
    """ Deep SHAP (DeepLIFT)
    """
def expected_gradients(model, data):
    """ Expected Gradients
    """
