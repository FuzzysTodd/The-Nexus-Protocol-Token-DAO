from .utils._exceptions import DimensionError as DimensionError
from .utils._general import OpChain as OpChain
from _typeshed import Incomplete

op_chain_root: Incomplete

class MetaExplanation(type):
    """ This metaclass exposes the Explanation object's methods for creating template op chains.
    """
    def __getitem__(cls, item): ...
    @property
    def abs(cls):
        """ Element-wise absolute value op.
        """
    @property
    def identity(cls):
        """ A no-op.
        """
    @property
    def argsort(cls):
        """ Numpy style argsort.
        """
    @property
    def sum(cls):
        """ Numpy style sum.
        """
    @property
    def max(cls):
        """ Numpy style max.
        """
    @property
    def min(cls):
        """ Numpy style min.
        """
    @property
    def mean(cls):
        """ Numpy style mean.
        """
    @property
    def sample(cls):
        """ Numpy style sample.
        """
    @property
    def hclust(cls):
        """ Hierarchical clustering op.
        """

class Explanation(metaclass=MetaExplanation):
    """ A slicable set of parallel arrays representing a SHAP explanation.
    """
    op_history: Incomplete
    compute_time: Incomplete
    output_dims: Incomplete
    def __init__(self, values, base_values: Incomplete | None = None, data: Incomplete | None = None, display_data: Incomplete | None = None, instance_names: Incomplete | None = None, feature_names: Incomplete | None = None, output_names: Incomplete | None = None, output_indexes: Incomplete | None = None, lower_bounds: Incomplete | None = None, upper_bounds: Incomplete | None = None, error_std: Incomplete | None = None, main_effects: Incomplete | None = None, hierarchical_values: Incomplete | None = None, clustering: Incomplete | None = None, compute_time: Incomplete | None = None) -> None: ...
    @property
    def shape(self):
        """ Compute the shape over potentially complex data nesting.
        """
    @property
    def values(self):
        """ Pass-through from the underlying slicer object.
        """
    @values.setter
    def values(self, new_values) -> None: ...
    @property
    def base_values(self):
        """ Pass-through from the underlying slicer object.
        """
    @base_values.setter
    def base_values(self, new_base_values) -> None: ...
    @property
    def data(self):
        """ Pass-through from the underlying slicer object.
        """
    @data.setter
    def data(self, new_data) -> None: ...
    @property
    def display_data(self):
        """ Pass-through from the underlying slicer object.
        """
    @display_data.setter
    def display_data(self, new_display_data) -> None: ...
    @property
    def instance_names(self):
        """ Pass-through from the underlying slicer object.
        """
    @property
    def output_names(self):
        """ Pass-through from the underlying slicer object.
        """
    @output_names.setter
    def output_names(self, new_output_names) -> None: ...
    @property
    def output_indexes(self):
        """ Pass-through from the underlying slicer object.
        """
    @property
    def feature_names(self):
        """ Pass-through from the underlying slicer object.
        """
    @feature_names.setter
    def feature_names(self, new_feature_names) -> None: ...
    @property
    def lower_bounds(self):
        """ Pass-through from the underlying slicer object.
        """
    @property
    def upper_bounds(self):
        """ Pass-through from the underlying slicer object.
        """
    @property
    def error_std(self):
        """ Pass-through from the underlying slicer object.
        """
    @property
    def main_effects(self):
        """ Pass-through from the underlying slicer object.
        """
    @main_effects.setter
    def main_effects(self, new_main_effects) -> None: ...
    @property
    def hierarchical_values(self):
        """ Pass-through from the underlying slicer object.
        """
    @hierarchical_values.setter
    def hierarchical_values(self, new_hierarchical_values) -> None: ...
    @property
    def clustering(self):
        """ Pass-through from the underlying slicer object.
        """
    @clustering.setter
    def clustering(self, new_clustering) -> None: ...
    def cohorts(self, cohorts):
        """ Split this explanation into several cohorts.

        Parameters
        ----------
        cohorts : int or array
            If this is an integer then we auto build that many cohorts using a decision tree. If this is
            an array then we treat that as an array of cohort names/ids for each instance.
        """
    def __getitem__(self, item):
        """ This adds support for OpChain indexing.
        """
    def __len__(self) -> int: ...
    def __copy__(self): ...
    def __add__(self, other): ...
    def __radd__(self, other): ...
    def __sub__(self, other): ...
    def __rsub__(self, other): ...
    def __mul__(self, other): ...
    def __rmul__(self, other): ...
    def __truediv__(self, other): ...
    def mean(self, axis):
        """ Numpy-style mean function.
        """
    def max(self, axis):
        """ Numpy-style mean function.
        """
    def min(self, axis):
        """ Numpy-style mean function.
        """
    def sum(self, axis: Incomplete | None = None, grouping: Incomplete | None = None):
        """ Numpy-style mean function.
        """
    def hstack(self, other):
        """ Stack two explanations column-wise.
        """
    @property
    def abs(self): ...
    @property
    def identity(self): ...
    @property
    def argsort(self): ...
    @property
    def flip(self): ...
    def hclust(self, metric: str = 'sqeuclidean', axis: int = 0):
        ''' Computes an optimal leaf ordering sort order using hclustering.

        hclust(metric="sqeuclidean")

        Parameters
        ----------
        metric : string
            A metric supported by scipy clustering.

        axis : int
            The axis to cluster along.
        '''
    def sample(self, max_samples, replace: bool = False, random_state: int = 0):
        """ Randomly samples the instances (rows) of the Explanation object.

        Parameters
        ----------
        max_samples : int
            The number of rows to sample. Note that if replace=False then less than
            fewer than max_samples will be drawn if explanation.shape[0] < max_samples.

        replace : bool
            Sample with or without replacement.
        """
    def percentile(self, q, axis: Incomplete | None = None): ...

def group_features(shap_values, feature_map): ...
def compute_output_dims(values, base_values, data, output_names):
    """ Uses the passed data to infer which dimensions correspond to the model's output.
    """
def is_1d(val): ...

class Op: ...

class Percentile(Op):
    percentile: Incomplete
    def __init__(self, percentile) -> None: ...
    def add_repr(self, s, verbose: bool = False): ...

class Cohorts:
    cohorts: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def __getitem__(self, item): ...
    def __getattr__(self, name): ...
    def __call__(self, *args, **kwargs): ...

def list_wrap(x):
    """ A helper to patch things since slicer doesn't handle arrays of arrays (it does handle lists of arrays)
    """
