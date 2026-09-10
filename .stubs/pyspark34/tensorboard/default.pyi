from _typeshed import Incomplete
from tensorboard.backend import experimental_plugin as experimental_plugin
from tensorboard.plugins.audio import audio_plugin as audio_plugin
from tensorboard.plugins.core import core_plugin as core_plugin
from tensorboard.plugins.custom_scalar import custom_scalars_plugin as custom_scalars_plugin
from tensorboard.plugins.debugger_v2 import debugger_v2_plugin as debugger_v2_plugin
from tensorboard.plugins.distribution import distributions_plugin as distributions_plugin
from tensorboard.plugins.graph import graphs_plugin as graphs_plugin
from tensorboard.plugins.histogram import histograms_plugin as histograms_plugin
from tensorboard.plugins.hparams import hparams_plugin as hparams_plugin
from tensorboard.plugins.image import images_plugin as images_plugin
from tensorboard.plugins.mesh import mesh_plugin as mesh_plugin
from tensorboard.plugins.metrics import metrics_plugin as metrics_plugin
from tensorboard.plugins.npmi import npmi_plugin as npmi_plugin
from tensorboard.plugins.pr_curve import pr_curves_plugin as pr_curves_plugin
from tensorboard.plugins.profile_redirect import profile_redirect_plugin as profile_redirect_plugin
from tensorboard.plugins.scalar import scalars_plugin as scalars_plugin
from tensorboard.plugins.text import text_plugin as text_plugin
from tensorboard.plugins.text_v2 import text_v2_plugin as text_v2_plugin
from tensorboard.plugins.wit_redirect import wit_redirect_plugin as wit_redirect_plugin

logger: Incomplete

class ExperimentalTextV2Plugin(text_v2_plugin.TextV2Plugin, experimental_plugin.ExperimentalPlugin):
    """Angular Text Plugin marked as experimental."""
class ExperimentalNpmiPlugin(npmi_plugin.NpmiPlugin, experimental_plugin.ExperimentalPlugin):
    """Angular nPMI Plugin marked as experimental."""

def get_plugins():
    """Returns a list specifying all known TensorBoard plugins.

    This includes both first-party, statically bundled plugins and
    dynamic plugins.

    This list can be passed to the `tensorboard.program.TensorBoard` API.

    Returns:
      The list of default first-party plugins.
    """
def get_static_plugins():
    """Returns a list specifying TensorBoard's default first-party plugins.

    Plugins are specified in this list either via a TBLoader instance to load the
    plugin, or the TBPlugin class itself which will be loaded using a BasicLoader.

    This list can be passed to the `tensorboard.program.TensorBoard` API.

    Returns:
      The list of default first-party plugins.

    :rtype: list[Type[base_plugin.TBLoader] | Type[base_plugin.TBPlugin]]
    """
def get_dynamic_plugins():
    """Returns a list specifying TensorBoard's dynamically loaded plugins.

    A dynamic TensorBoard plugin is specified using entry_points [1] and it is
    the robust way to integrate plugins into TensorBoard.

    This list can be passed to the `tensorboard.program.TensorBoard` API.

    Returns:
      The list of dynamic plugins.

    :rtype: list[Type[base_plugin.TBLoader] | Type[base_plugin.TBPlugin]]

    [1]: https://packaging.python.org/specifications/entry-points/
    """
