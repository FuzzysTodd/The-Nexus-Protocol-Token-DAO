import abc
from ..api.base import ExplainerMixin as ExplainerMixin
from ..api.templates import FeatureValueExplanation as FeatureValueExplanation
from ..utils._clean_x import preclean_X as preclean_X
from ..utils._explanation import gen_global_selector as gen_global_selector, gen_name_from_class as gen_name_from_class
from ..utils._unify_data import unify_data as unify_data
from ..utils._unify_predict import determine_classes as determine_classes, unify_predict_fn as unify_predict_fn
from _typeshed import Incomplete
from abc import ABC, abstractmethod

class SamplerMixin(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def sample(self, data, feature_names, feature_types): ...

class MorrisSampler(SamplerMixin):
    N: Incomplete
    num_levels: Incomplete
    kwargs: Incomplete
    def __init__(self, N: int = 1000, num_levels: int = 4, **kwargs) -> None: ...
    def sample(self, data, feature_names, feature_types): ...

class MorrisSensitivity(ExplainerMixin):
    '''Method of Morris for analyzing blackbox systems.
    If using this please cite the package owners as can be found here: https://github.com/SALib/SALib

    Morris, Max D. "Factorial sampling plans for preliminary computational experiments."
    Technometrics 33.2 (1991): 161-174.
    '''
    available_explanations: Incomplete
    explainer_type: str
    mu_: Incomplete
    mu_star_: Incomplete
    sigma_: Incomplete
    mu_star_conf_: Incomplete
    convergence_index_: Incomplete
    unique_val_counts_: Incomplete
    def __init__(self, model, data, feature_names: Incomplete | None = None, feature_types: Incomplete | None = None, sampler: Incomplete | None = None, **kwargs) -> None:
        """Initializes class.

        Args:
            model: model or prediction function of model (predict_proba for classification or predict for regression)
            data: Data used to initialize LIME with.
            feature_names: List of feature names.
            feature_types: List of feature types.
            sampler: A SamplerMixin derrived class that can generate samples from data
            **kwargs: Kwargs that will be sent to SALib.analyze.morris.analyze
        """
    def explain_global(self, name: Incomplete | None = None):
        """Provides approximate global explanation for blackbox model.

        Args:
            name: User-defined explanation name.

        Returns:
            An explanation object, visualizes dependence plots.
        """

class MorrisExplanation(FeatureValueExplanation):
    """Visualizations specific to Method of Morris."""
    explanation_type: Incomplete
    def __init__(self, explanation_type, internal_obj, feature_names: Incomplete | None = None, feature_types: Incomplete | None = None, name: Incomplete | None = None, selector: Incomplete | None = None) -> None:
        """Initializes class.

        Args:
            explanation_type:  Type of explanation.
            internal_obj: A jsonable object that backs the explanation.
            feature_names: List of feature names.
            feature_types: List of feature types.
            name: User-defined name of explanation.
            selector: A dataframe whose indices correspond to explanation entries.
        """
    def visualize(self, key: Incomplete | None = None):
        """Provides interactive visualizations.

        Args:
            key: Either a scalar or list
                that indexes the internal object for sub-plotting.
                If an overall visualization is requested, pass None.

        Returns:
            HTML as a string.
        """
