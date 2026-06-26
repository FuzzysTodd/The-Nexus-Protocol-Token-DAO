from .exceptions import LimeError as LimeError
from _typeshed import Incomplete

def id_generator(size: int = 15, random_state: Incomplete | None = None):
    """Helper function to generate random div ids. This is useful for embedding
    HTML into ipython notebooks."""

class DomainMapper:
    """Class for mapping features to the specific domain.

    The idea is that there would be a subclass for each domain (text, tables,
    images, etc), so that we can have a general Explanation class, and separate
    out the specifics of visualizing features in here.
    """
    def __init__(self) -> None: ...
    def map_exp_ids(self, exp, **kwargs):
        """Maps the feature ids to concrete names.

        Default behaviour is the identity function. Subclasses can implement
        this as they see fit.

        Args:
            exp: list of tuples [(id, weight), (id,weight)]
            kwargs: optional keyword arguments

        Returns:
            exp: list of tuples [(name, weight), (name, weight)...]
        """
    def visualize_instance_html(self, exp, label, div_name, exp_object_name, **kwargs):
        """Produces html for visualizing the instance.

        Default behaviour does nothing. Subclasses can implement this as they
        see fit.

        Args:
             exp: list of tuples [(id, weight), (id,weight)]
             label: label id (integer)
             div_name: name of div object to be used for rendering(in js)
             exp_object_name: name of js explanation object
             kwargs: optional keyword arguments

        Returns:
             js code for visualizing the instance
        """

class Explanation:
    """Object returned by explainers."""
    random_state: Incomplete
    mode: Incomplete
    domain_mapper: Incomplete
    local_exp: Incomplete
    intercept: Incomplete
    score: Incomplete
    local_pred: Incomplete
    class_names: Incomplete
    top_labels: Incomplete
    predict_proba: Incomplete
    predicted_value: Incomplete
    min_value: float
    max_value: float
    dummy_label: int
    def __init__(self, domain_mapper, mode: str = 'classification', class_names: Incomplete | None = None, random_state: Incomplete | None = None) -> None:
        '''

        Initializer.

        Args:
            domain_mapper: must inherit from DomainMapper class
            type: "classification" or "regression"
            class_names: list of class names (only used for classification)
            random_state: an integer or numpy.RandomState that will be used to
                generate random numbers. If None, the random state will be
                initialized using the internal numpy seed.
        '''
    def available_labels(self):
        """
        Returns the list of classification labels for which we have any explanations.
        """
    def as_list(self, label: int = 1, **kwargs):
        """Returns the explanation as a list.

        Args:
            label: desired label. If you ask for a label for which an
                explanation wasn't computed, will throw an exception.
                Will be ignored for regression explanations.
            kwargs: keyword arguments, passed to domain_mapper

        Returns:
            list of tuples (representation, weight), where representation is
            given by domain_mapper. Weight is a float.
        """
    def as_map(self):
        """Returns the map of explanations.

        Returns:
            Map from label to list of tuples (feature_id, weight).
        """
    def as_pyplot_figure(self, label: int = 1, **kwargs):
        """Returns the explanation as a pyplot figure.

        Will throw an error if you don't have matplotlib installed
        Args:
            label: desired label. If you ask for a label for which an
                   explanation wasn't computed, will throw an exception.
                   Will be ignored for regression explanations.
            kwargs: keyword arguments, passed to domain_mapper

        Returns:
            pyplot figure (barchart).
        """
    def show_in_notebook(self, labels: Incomplete | None = None, predict_proba: bool = True, show_predicted_value: bool = True, **kwargs) -> None:
        """Shows html explanation in ipython notebook.

        See as_html() for parameters.
        This will throw an error if you don't have IPython installed"""
    def save_to_file(self, file_path, labels: Incomplete | None = None, predict_proba: bool = True, show_predicted_value: bool = True, **kwargs) -> None:
        """Saves html explanation to file. .

        Params:
            file_path: file to save explanations to

        See as_html() for additional parameters.

        """
    def as_html(self, labels: Incomplete | None = None, predict_proba: bool = True, show_predicted_value: bool = True, **kwargs):
        """Returns the explanation as an html page.

        Args:
            labels: desired labels to show explanations for (as barcharts).
                If you ask for a label for which an explanation wasn't
                computed, will throw an exception. If None, will show
                explanations for all available labels. (only used for classification)
            predict_proba: if true, add  barchart with prediction probabilities
                for the top classes. (only used for classification)
            show_predicted_value: if true, add  barchart with expected value
                (only used for regression)
            kwargs: keyword arguments, passed to domain_mapper

        Returns:
            code for an html page, including javascript includes.
        """
