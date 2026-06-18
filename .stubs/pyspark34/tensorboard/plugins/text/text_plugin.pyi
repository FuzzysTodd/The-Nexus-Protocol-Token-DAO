from _typeshed import Incomplete
from tensorboard import plugin_util as plugin_util
from tensorboard.backend import http_util as http_util
from tensorboard.data import provider as provider
from tensorboard.plugins import base_plugin as base_plugin
from tensorboard.plugins.text import metadata as metadata

TAGS_ROUTE: str
TEXT_ROUTE: str
WARNING_TEMPLATE: Incomplete

def make_table_row(contents, tag: str = 'td'):
    """Given an iterable of string contents, make a table row.

    Args:
      contents: An iterable yielding strings.
      tag: The tag to place contents in. Defaults to 'td', you might want 'th'.

    Returns:
      A string containing the content strings, organized into a table row.

    Example: make_table_row(['one', 'two', 'three']) == '''
    <tr>
    <td>one</td>
    <td>two</td>
    <td>three</td>
    </tr>'''
    """
def make_table(contents, headers: Incomplete | None = None):
    """Given a numpy ndarray of strings, concatenate them into a html table.

    Args:
      contents: A np.ndarray of strings. May be 1d or 2d. In the 1d case, the
        table is laid out vertically (i.e. row-major).
      headers: A np.ndarray or list of string header names for the table.

    Returns:
      A string containing all of the content strings, organized into a table.

    Raises:
      ValueError: If contents is not a np.ndarray.
      ValueError: If contents is not 1d or 2d.
      ValueError: If contents is empty.
      ValueError: If headers is present and not a list, tuple, or ndarray.
      ValueError: If headers is not 1d.
      ValueError: If number of elements in headers does not correspond to number
        of columns in contents.
    """
def reduce_to_2d(arr):
    """Given a np.npdarray with nDims > 2, reduce it to 2d.

    It does this by selecting the zeroth coordinate for every dimension greater
    than two.

    Args:
      arr: a numpy ndarray of dimension at least 2.

    Returns:
      A two-dimensional subarray from the input array.

    Raises:
      ValueError: If the argument is not a numpy ndarray, or the dimensionality
        is too low.
    """
def text_array_to_html(text_arr, enable_markdown):
    """Take a numpy.ndarray containing strings, and convert it into html.

    If the ndarray contains a single scalar string, that string is converted to
    html via our sanitized markdown parser. If it contains an array of strings,
    the strings are individually converted to html and then composed into a table
    using make_table. If the array contains dimensionality greater than 2,
    all but two of the dimensions are removed, and a warning message is prefixed
    to the table.

    Args:
      text_arr: A numpy.ndarray containing strings.
      enable_markdown: boolean, whether to enable Markdown

    Returns:
      The array converted to html.
    """
def process_event(wall_time, step, string_ndarray, enable_markdown):
    """Convert a text event into a JSON-compatible response."""

class TextPlugin(base_plugin.TBPlugin):
    """Text Plugin for TensorBoard."""
    plugin_name: Incomplete
    def __init__(self, context) -> None:
        """Instantiates TextPlugin via TensorBoard core.

        Args:
          context: A base_plugin.TBContext instance.
        """
    def is_active(self): ...
    def frontend_metadata(self): ...
    def index_impl(self, ctx, experiment): ...
    def tags_route(self, request): ...
    def text_impl(self, ctx, run, tag, experiment, enable_markdown): ...
    def text_route(self, request): ...
    def get_plugin_apps(self): ...
