from tensorboard import plugin_util as plugin_util
from tensorboard.backend import http_util as http_util
from tensorboard.data import provider as provider
from tensorboard.plugins import base_plugin as base_plugin
from tensorboard.plugins.text import metadata as metadata

TAGS_ROUTE: str
TEXT_ROUTE: str

def reduce_to_2d(arr):
    """Given a np.ndarray with nDims > 2, reduce it to 2d.

    It does this by selecting the zeroth coordinate for every dimension except
    the last two.

    Args:
      arr: a numpy ndarray of dimension at least 2.

    Returns:
      A two-dimensional subarray from the input array.

    Raises:
      ValueError: If the argument is not a numpy ndarray, or the dimensionality
        is too low.
    """
def reduce_and_jsonify(text_ndarr):
    """Take a numpy.ndarray containing strings, and convert it into a
    json-compatible list, also squashing it to two dimensions if necessary.

    If the ndarray contains a single scalar string, then that ndarray is
    converted to a list. If it contains an array of strings,
    that array is converted to a list.  If the array contains dimensionality
    greater than 2, all but two of the dimensions are removed, and a squashed
    boolean is set to true.  Returned is a list, the shape of the original
    array, and a boolean indicating squashsing has occured.

    Args:
        text_arr: A numpy.ndarray containing strings.

    Returns:
        a tuple containing:
            The JSON-compatible list
            The shape of the array (before being squashed)
            A boolean indicating if the array was squashed
    """
def create_event(wall_time, step, string_ndarray):
    """Convert a text event into a JSON-compatible response with rank <= 2"""

class TextV2Plugin(base_plugin.TBPlugin):
    """Angular Text Plugin For TensorBoard"""
    plugin_name: str
    def __init__(self, context) -> None:
        """Instantiates Angular TextPlugin via TensorBoard core.

        Args:
          context: A base_plugin.TBContext instance.
        """
    def frontend_metadata(self): ...
    def is_active(self):
        """Determines whether this plugin is active.

        This plugin is only active if TensorBoard sampled any text summaries.

        Returns:
          Whether this plugin is active.
        """
    def index_impl(self, ctx, experiment): ...
    def text_impl(self, ctx, run, tag, experiment): ...
    def text_route(self, request): ...
    def tags_route(self, request): ...
    def get_plugin_apps(self): ...
