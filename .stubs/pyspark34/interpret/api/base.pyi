import abc
from _typeshed import Incomplete

class ExplainerMixin(abc.ABC, metaclass=abc.ABCMeta):
    '''An object that computes explanations.
        This is a contract required for InterpretML.

    Attributes:
        available_explanations: A list of strings subsetting the following
            - "perf", "data", "local", "global".
        explainer_type: A string that is one of the following
            - "blackbox", "model", "specific", "data", "perf".
    '''
    @property
    @abc.abstractmethod
    def available_explanations(self): ...
    @property
    @abc.abstractmethod
    def explainer_type(self): ...

class ExplanationMixin(abc.ABC, metaclass=abc.ABCMeta):
    '''The result of calling explain_* from an Explainer. Responsible for providing data and/or visualization.
        This is a contract required for InterpretML.

    Attributes:
        explanation_type: A string that is one of the
            explainer\'s available explanations.
            Should be one of "perf", "data", "local", "global".
        name: A string that denotes the name of the explanation
            for display purposes.
        selector: An optional dataframe that describes the data.
            Each row of the dataframe corresponds with a respective data item.
    '''
    @property
    @abc.abstractmethod
    def explanation_type(self): ...
    @abc.abstractmethod
    def data(self, key: Incomplete | None = None):
        """Provides specific explanation data.

        Args:
            key: A number/string that references a specific data item.
        Returns:
            A serializable dictionary.
        """
    @abc.abstractmethod
    def visualize(self, key: Incomplete | None = None):
        """Provides interactive visualizations.

        Args:
            key: Either a scalar or list
                that indexes the internal object for sub-plotting.
                If an overall visualization is requested, pass None.

        Returns:
            A Plotly figure, html as string, or a Dash component.
        """
    name: str
    selector: Incomplete
