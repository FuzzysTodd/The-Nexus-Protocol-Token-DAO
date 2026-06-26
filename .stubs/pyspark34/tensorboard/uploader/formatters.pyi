import abc
from tensorboard.uploader import util as util

class BaseExperimentFormatter(metaclass=abc.ABCMeta):
    """Abstract base class for formatting experiment information as a string."""
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def format_experiment(self, experiment, experiment_url):
        """Format the information about an experiment as a representing string.

        Args:
          experiment: An `experiment_pb2.Experiment` protobuf message for the
            experiment to be formatted.
          experiment_url: The URL at which the experiment can be accessed via
            TensorBoard.

        Returns:
          A string that represents the experiment.
        """

class ReadableFormatter(BaseExperimentFormatter):
    """A formatter implementation that outputs human-readable text."""
    def __init__(self) -> None: ...
    def format_experiment(self, experiment, experiment_url): ...

class JsonFormatter:
    """A formatter implementation: outputs experiment as JSON."""
    def __init__(self) -> None: ...
    def format_experiment(self, experiment, experiment_url): ...
