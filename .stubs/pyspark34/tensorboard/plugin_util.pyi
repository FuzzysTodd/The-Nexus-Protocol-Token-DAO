import threading
from _typeshed import Incomplete
from tensorboard._vendor.bleach.sanitizer import Cleaner as Cleaner
from tensorboard.util import tb_logging as tb_logging

logger: Incomplete

class _MarkdownStore(threading.local):
    markdown: Incomplete
    def __init__(self) -> None: ...

class _CleanerStore(threading.local):
    cleaner: Incomplete
    def __init__(self) -> None: ...

def safe_html(unsafe_string):
    """Return the input as a str, sanitized for insertion into the DOM.

    Arguments:
      unsafe_string: A Unicode string or UTF-8--encoded bytestring
        possibly containing unsafe HTML markup.

    Returns:
      A string containing safe HTML.
    """
def markdown_to_safe_html(markdown_string):
    """Convert Markdown to HTML that's safe to splice into the DOM.

    Arguments:
      markdown_string: A Unicode string or UTF-8--encoded bytestring
        containing Markdown source. Markdown tables are supported.

    Returns:
      A string containing safe HTML.
    """
def markdowns_to_safe_html(markdown_strings, combine):
    """Convert multiple Markdown documents to one safe HTML document.

    One could also achieve this by calling `markdown_to_safe_html`
    multiple times and combining the results. Compared to that approach,
    this function may be faster, because HTML sanitization (which can be
    expensive) is performed only once rather than once per input. It may
    also be less precise: if one of the input documents has unsafe HTML
    that is sanitized away, that sanitization might affect other
    documents, even if those documents are safe.

    Args:
      markdown_strings: List of Markdown source strings to convert, as
        Unicode strings or UTF-8--encoded bytestrings. Markdown tables
        are supported.
      combine: Callback function that takes a list of unsafe HTML
        strings of the same shape as `markdown_strings` and combines
        them into a single unsafe HTML string, which will be sanitized
        and returned.

    Returns:
      A string containing safe HTML.
    """
def context(environ):
    """Get a TensorBoard `RequestContext` from a WSGI environment.

    Returns:
      A `RequestContext` value.
    """
def experiment_id(environ):
    """Determine the experiment ID associated with a WSGI request.

    Each request to TensorBoard has an associated experiment ID, which is
    always a string and may be empty. This experiment ID should be passed
    to data providers.

    Args:
      environ: A WSGI environment `dict`. For a Werkzeug request, this is
        `request.environ`.

    Returns:
      A experiment ID, as a possibly-empty `str`.
    """

class _MetadataVersionChecker:
    """TensorBoard-internal utility for warning when data is too new.

    Specify a maximum known `version` number as stored in summary
    metadata, and automatically reject and warn on data from newer
    versions. This keeps a (single) bit of internal state to handle
    logging a warning to the user at most once.

    This should only be used by plugins bundled with TensorBoard, since
    it may instruct users to upgrade their copy of TensorBoard.
    """
    def __init__(self, data_kind, latest_known_version) -> None:
        '''Initialize a `_MetadataVersionChecker`.

        Args:
          data_kind: A human-readable description of the kind of data
            being read, like "scalar" or "histogram" or "PR curve".
          latest_known_version: Highest tolerated value of `version`,
            like `0`.
        '''
    def ok(self, version, run, tag):
        """Test whether `version` is permitted, else complain."""
