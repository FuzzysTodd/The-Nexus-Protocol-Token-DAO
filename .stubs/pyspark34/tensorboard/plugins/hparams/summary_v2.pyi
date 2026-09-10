import abc
from _typeshed import Incomplete
from tensorboard.compat.proto import summary_pb2 as summary_pb2
from tensorboard.plugins.hparams import api_pb2 as api_pb2, metadata as metadata, plugin_data_pb2 as plugin_data_pb2

def hparams(hparams, trial_id: Incomplete | None = None, start_time_secs: Incomplete | None = None):
    """Write hyperparameter values for a single trial.

    Args:
      hparams: A `dict` mapping hyperparameters to the values used in this
        trial. Keys should be the names of `HParam` objects used in an
        experiment, or the `HParam` objects themselves. Values should be
        Python `bool`, `int`, `float`, or `string` values, depending on
        the type of the hyperparameter. The corresponding numpy types,
        like `np.float32`, are also permitted.
      trial_id: An optional `str` ID for the set of hyperparameter values
        used in this trial. Defaults to a hash of the hyperparameters.
      start_time_secs: The time that this trial started training, as
        seconds since epoch. Defaults to the current time.

    Returns:
      A tensor whose value is `True` on success, or `False` if no summary
      was written because no default summary writer was available.
    """
def hparams_pb(hparams, trial_id: Incomplete | None = None, start_time_secs: Incomplete | None = None):
    """Create a summary encoding hyperparameter values for a single trial.

    Args:
      hparams: A `dict` mapping hyperparameters to the values used in this
        trial. Keys should be the names of `HParam` objects used in an
        experiment, or the `HParam` objects themselves. Values should be
        Python `bool`, `int`, `float`, or `string` values, depending on
        the type of the hyperparameter.
      trial_id: An optional `str` ID for the set of hyperparameter values
        used in this trial. Defaults to a hash of the hyperparameters.
      start_time_secs: The time that this trial started training, as
        seconds since epoch. Defaults to the current time.

    Returns:
      A TensorBoard `summary_pb2.Summary` message.
    """
def hparams_config(hparams, metrics, time_created_secs: Incomplete | None = None):
    """Write a top-level experiment configuration.

    This configuration describes the hyperparameters and metrics that will
    be tracked in the experiment, but does not record any actual values of
    those hyperparameters and metrics. It can be created before any models
    are actually trained.

    Args:
      hparams: A list of `HParam` values.
      metrics: A list of `Metric` values.
      time_created_secs: The time that this experiment was created, as
        seconds since epoch. Defaults to the current time.

    Returns:
      A tensor whose value is `True` on success, or `False` if no summary
      was written because no default summary writer was available.
    """
def hparams_config_pb(hparams, metrics, time_created_secs: Incomplete | None = None):
    """Create a top-level experiment configuration.

    This configuration describes the hyperparameters and metrics that will
    be tracked in the experiment, but does not record any actual values of
    those hyperparameters and metrics. It can be created before any models
    are actually trained.

    Args:
      hparams: A list of `HParam` values.
      metrics: A list of `Metric` values.
      time_created_secs: The time that this experiment was created, as
        seconds since epoch. Defaults to the current time.

    Returns:
      A TensorBoard `summary_pb2.Summary` message.
    """

class HParam:
    """A hyperparameter in an experiment.

    This class describes a hyperparameter in the abstract. It ranges
    over a domain of values, but is not bound to any particular value.
    """
    def __init__(self, name, domain: Incomplete | None = None, display_name: Incomplete | None = None, description: Incomplete | None = None) -> None:
        """Create a hyperparameter object.

        Args:
          name: A string ID for this hyperparameter, which should be unique
            within an experiment.
          domain: An optional `Domain` object describing the values that
            this hyperparameter can take on.
          display_name: An optional human-readable display name (`str`).
          description: An optional Markdown string describing this
            hyperparameter.

        Raises:
          ValueError: If `domain` is not a `Domain`.
        """
    @property
    def name(self): ...
    @property
    def domain(self): ...
    @property
    def display_name(self): ...
    @property
    def description(self): ...

class Domain(metaclass=abc.ABCMeta):
    """The domain of a hyperparameter.

    Domains are restricted to values of the simple types `float`, `int`,
    `str`, and `bool`.
    """
    @property
    @abc.abstractmethod
    def dtype(self):
        """Data type of this domain: `float`, `int`, `str`, or `bool`."""
    @abc.abstractmethod
    def sample_uniform(self, rng=...):
        """Sample a value from this domain uniformly at random.

        Args:
          rng: A `random.Random` interface; defaults to the `random` module
            itself.

        Raises:
          IndexError: If the domain is empty.
        """
    @abc.abstractmethod
    def update_hparam_info(self, hparam_info):
        """Update an `HParamInfo` proto to include this domain.

        This should update the `type` field on the proto and exactly one of
        the `domain` variants on the proto.

        Args:
          hparam_info: An `api_pb2.HParamInfo` proto to modify.
        """

class IntInterval(Domain):
    """A domain that takes on all integer values in a closed interval."""
    def __init__(self, min_value: Incomplete | None = None, max_value: Incomplete | None = None) -> None:
        """Create an `IntInterval`.

        Args:
          min_value: The lower bound (inclusive) of the interval.
          max_value: The upper bound (inclusive) of the interval.

        Raises:
          TypeError: If `min_value` or `max_value` is not an `int`.
          ValueError: If `min_value > max_value`.
        """
    @property
    def dtype(self): ...
    @property
    def min_value(self): ...
    @property
    def max_value(self): ...
    def sample_uniform(self, rng=...): ...
    def update_hparam_info(self, hparam_info) -> None: ...

class RealInterval(Domain):
    """A domain that takes on all real values in a closed interval."""
    def __init__(self, min_value: Incomplete | None = None, max_value: Incomplete | None = None) -> None:
        """Create a `RealInterval`.

        Args:
          min_value: The lower bound (inclusive) of the interval.
          max_value: The upper bound (inclusive) of the interval.

        Raises:
          TypeError: If `min_value` or `max_value` is not an `float`.
          ValueError: If `min_value > max_value`.
        """
    @property
    def dtype(self): ...
    @property
    def min_value(self): ...
    @property
    def max_value(self): ...
    def sample_uniform(self, rng=...): ...
    def update_hparam_info(self, hparam_info) -> None: ...

class Discrete(Domain):
    """A domain that takes on a fixed set of values.

    These values may be of any (single) domain type.
    """
    def __init__(self, values, dtype: Incomplete | None = None) -> None:
        """Construct a discrete domain.

        Args:
          values: A iterable of the values in this domain.
          dtype: The Python data type of values in this domain: one of
            `int`, `float`, `bool`, or `str`. If `values` is non-empty,
            `dtype` may be `None`, in which case it will be inferred as the
            type of the first element of `values`.

        Raises:
          ValueError: If `values` is empty but no `dtype` is specified.
          ValueError: If `dtype` or its inferred value is not `int`,
            `float`, `bool`, or `str`.
          TypeError: If an element of `values` is not an instance of
            `dtype`.
        """
    @property
    def dtype(self): ...
    @property
    def values(self): ...
    def sample_uniform(self, rng=...): ...
    def update_hparam_info(self, hparam_info) -> None: ...

class Metric:
    """A metric in an experiment.

    A metric is a real-valued function of a model. Each metric is
    associated with a TensorBoard scalar summary, which logs the
    metric's value as the model trains.
    """
    TRAINING: Incomplete
    VALIDATION: Incomplete
    def __init__(self, tag, group: Incomplete | None = None, display_name: Incomplete | None = None, description: Incomplete | None = None, dataset_type: Incomplete | None = None) -> None:
        '''

        Args:
          tag: The tag name of the scalar summary that corresponds to this
            metric (as a `str`).
          group: An optional string listing the subdirectory under the
            session\'s log directory containing summaries for this metric.
            For instance, if summaries for training runs are written to
            events files in `ROOT_LOGDIR/SESSION_ID/train`, then `group`
            should be `"train"`. Defaults to the empty string: i.e.,
            summaries are expected to be written to the session logdir.
          display_name: An optional human-readable display name.
          description: An optional Markdown string with a human-readable
            description of this metric, to appear in TensorBoard.
          dataset_type: Either `Metric.TRAINING` or `Metric.VALIDATION`, or
            `None`.
        '''
    def as_proto(self): ...
