from _typeshed import Incomplete
from tensorboard.plugins.hparams import api_pb2 as api_pb2, metadata as metadata, plugin_data_pb2 as plugin_data_pb2

def experiment_pb(hparam_infos, metric_infos, user: str = '', description: str = '', time_created_secs: Incomplete | None = None):
    """Creates a summary that defines a hyperparameter-tuning experiment.

    Args:
      hparam_infos: Array of api_pb2.HParamInfo messages. Describes the
          hyperparameters used in the experiment.
      metric_infos: Array of api_pb2.MetricInfo messages. Describes the metrics
          used in the experiment. See the documentation at the top of this file
          for how to populate this.
      user: String. An id for the user running the experiment
      description: String. A description for the experiment. May contain markdown.
      time_created_secs: float. The time the experiment is created in seconds
      since the UNIX epoch. If None uses the current time.

    Returns:
      A summary protobuffer containing the experiment definition.
    """
def session_start_pb(hparams, model_uri: str = '', monitor_url: str = '', group_name: str = '', start_time_secs: Incomplete | None = None):
    """Constructs a SessionStartInfo protobuffer.

    Creates a summary that contains a training session metadata information.
    One such summary per training session should be created. Each should have
    a different run.

    Args:
      hparams: A dictionary with string keys. Describes the hyperparameter values
               used in the session, mapping each hyperparameter name to its value.
               Supported value types are  `bool`, `int`, `float`, `str`, `list`,
               `tuple`.
               The type of value must correspond to the type of hyperparameter
               (defined in the corresponding api_pb2.HParamInfo member of the
               Experiment protobuf) as follows:

                +-----------------+---------------------------------+
                |Hyperparameter   | Allowed (Python) value types    |
                |type             |                                 |
                +-----------------+---------------------------------+
                |DATA_TYPE_BOOL   | bool                            |
                |DATA_TYPE_FLOAT64| int, float                      |
                |DATA_TYPE_STRING | str, tuple, list   |
                +-----------------+---------------------------------+

               Tuple and list instances will be converted to their string
               representation.
      model_uri: See the comment for the field with the same name of
                 plugin_data_pb2.SessionStartInfo.
      monitor_url: See the comment for the field with the same name of
                   plugin_data_pb2.SessionStartInfo.
      group_name:  See the comment for the field with the same name of
                   plugin_data_pb2.SessionStartInfo.
      start_time_secs: float. The time to use as the session start time.
                       Represented as seconds since the UNIX epoch. If None uses
                       the current time.
    Returns:
      The summary protobuffer mentioned above.
    """
def session_end_pb(status, end_time_secs: Incomplete | None = None):
    """Constructs a SessionEndInfo protobuffer.

    Creates a summary that contains status information for a completed
    training session. Should be exported after the training session is completed.
    One such summary per training session should be created. Each should have
    a different run.

    Args:
      status: A tensorboard.hparams.Status enumeration value denoting the
          status of the session.
      end_time_secs: float. The time to use as the session end time. Represented
          as seconds since the unix epoch. If None uses the current time.

    Returns:
      The summary protobuffer mentioned above.
    """
