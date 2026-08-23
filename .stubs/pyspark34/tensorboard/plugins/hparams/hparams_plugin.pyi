from _typeshed import Incomplete
from tensorboard import plugin_util as plugin_util
from tensorboard.backend import http_util as http_util
from tensorboard.plugins import base_plugin as base_plugin
from tensorboard.plugins.hparams import api_pb2 as api_pb2, backend_context as backend_context, download_data as download_data, error as error, get_experiment as get_experiment, list_metric_evals as list_metric_evals, list_session_groups as list_session_groups, metadata as metadata
from tensorboard.util import tb_logging as tb_logging

logger: Incomplete

class HParamsPlugin(base_plugin.TBPlugin):
    """HParams Plugin for TensorBoard.

    It supports both GETs and POSTs. See 'http_api.md' for more details.
    """
    plugin_name: Incomplete
    def __init__(self, context) -> None:
        """Instantiates HParams plugin via TensorBoard core.

        Args:
          context: A base_plugin.TBContext instance.
        """
    def get_plugin_apps(self):
        """See base class."""
    def is_active(self): ...
    def frontend_metadata(self): ...
    def download_data_route(self, request): ...
    def get_experiment_route(self, request): ...
    def list_session_groups_route(self, request): ...
    def list_metric_evals_route(self, request): ...
