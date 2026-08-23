from . import datasets as datasets, links as links, utils as utils
from ._explanation import Cohorts as Cohorts, Explanation as Explanation
from .actions._optimizer import ActionOptimizer as ActionOptimizer
from .explainers import other as other
from .explainers._explainer import Explainer as Explainer
from .plots._force import getjs as getjs
from .utils import approximate_interactions as approximate_interactions, sample as sample
from .utils._legacy import kmeans as kmeans

__version__: str

def unsupported(*args, **kwargs) -> None: ...

class UnsupportedModule:
    def __getattribute__(self, item) -> None: ...

have_matplotlib: bool
summary_plot = unsupported
decision_plot = unsupported
multioutput_decision_plot = unsupported
dependence_plot = unsupported
force_plot = unsupported
initjs = unsupported
save_html = unsupported
image_plot = unsupported
monitoring_plot = unsupported
embedding_plot = unsupported
partial_dependence_plot = unsupported
bar_plot = unsupported
waterfall_plot = unsupported
text_plot = unsupported
