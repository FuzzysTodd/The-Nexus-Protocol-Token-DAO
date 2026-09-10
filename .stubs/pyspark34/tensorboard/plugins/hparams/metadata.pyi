from _typeshed import Incomplete
from tensorboard.compat.proto import summary_pb2 as summary_pb2, types_pb2 as types_pb2
from tensorboard.plugins.hparams import error as error, plugin_data_pb2 as plugin_data_pb2
from tensorboard.util import tensor_util as tensor_util

PLUGIN_NAME: str
PLUGIN_DATA_VERSION: int
NULL_TENSOR: Incomplete
EXPERIMENT_TAG: str
SESSION_START_INFO_TAG: str
SESSION_END_INFO_TAG: str

def create_summary_metadata(hparams_plugin_data_pb):
    """Returns a summary metadata for the HParams plugin.

    Returns a summary_pb2.SummaryMetadata holding a copy of the given
    HParamsPluginData message in its plugin_data.content field.
    Sets the version field of the hparams_plugin_data_pb copy to
    PLUGIN_DATA_VERSION.

    Args:
      hparams_plugin_data_pb: the HParamsPluginData protobuffer to use.
    """
def parse_experiment_plugin_data(content):
    """Returns the experiment from HParam's
    SummaryMetadata.plugin_data.content.

    Raises HParamsError if the content doesn't have 'experiment' set or
    this file is incompatible with the version of the metadata stored.

    Args:
      content: The SummaryMetadata.plugin_data.content to use.
    """
def parse_session_start_info_plugin_data(content):
    """Returns session_start_info from the plugin_data.content.

    Raises HParamsError if the content doesn't have 'session_start_info' set or
    this file is incompatible with the version of the metadata stored.

    Args:
      content: The SummaryMetadata.plugin_data.content to use.
    """
def parse_session_end_info_plugin_data(content):
    """Returns session_end_info from the plugin_data.content.

    Raises HParamsError if the content doesn't have 'session_end_info' set or
    this file is incompatible with the version of the metadata stored.

    Args:
      content: The SummaryMetadata.plugin_data.content to use.
    """
