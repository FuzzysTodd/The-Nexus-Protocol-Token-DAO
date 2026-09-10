from . import Extension as Extension
from ..treeprocessors import Treeprocessor as Treeprocessor, UnescapeTreeprocessor as UnescapeTreeprocessor
from ..util import AMP_SUBSTITUTE as AMP_SUBSTITUTE, AtomicString as AtomicString, HTML_PLACEHOLDER_RE as HTML_PLACEHOLDER_RE, code_escape as code_escape, parseBoolValue as parseBoolValue
from _typeshed import Incomplete
from collections.abc import Generator

def slugify(value, separator, unicode: bool = False):
    """ Slugify a string, to make it URL friendly. """
def slugify_unicode(value, separator):
    """ Slugify a string, to make it URL friendly while preserving Unicode characters. """

IDCOUNT_RE: Incomplete

def unique(id, ids):
    """ Ensure id is unique in set of ids. Append '_1', '_2'... if not """
def get_name(el):
    """Get title name."""
def stashedHTML2text(text, md, strip_entities: bool = True):
    """ Extract raw HTML from stash, reduce to plain text and swap with placeholder. """
def unescape(text):
    """ Unescape escaped text. """
def nest_toc_tokens(toc_list):
    """Given an unsorted list with errors and skips, return a nested one.
    [{'level': 1}, {'level': 2}]
    =>
    [{'level': 1, 'children': [{'level': 2, 'children': []}]}]

    A wrong list is also converted:
    [{'level': 2}, {'level': 1}]
    =>
    [{'level': 2, 'children': []}, {'level': 1, 'children': []}]
    """

class TocTreeprocessor(Treeprocessor):
    marker: Incomplete
    title: Incomplete
    base_level: Incomplete
    slugify: Incomplete
    sep: Incomplete
    toc_class: Incomplete
    use_anchors: Incomplete
    anchorlink_class: Incomplete
    use_permalinks: Incomplete
    permalink_class: Incomplete
    permalink_title: Incomplete
    header_rgx: Incomplete
    toc_top: int
    toc_bottom: Incomplete
    def __init__(self, md, config) -> None: ...
    def iterparent(self, node) -> Generator[Incomplete, Incomplete, None]:
        """ Iterator wrapper to get allowed parent and child all at once. """
    def replace_marker(self, root, elem) -> None:
        """ Replace marker with elem. """
    def set_level(self, elem) -> None:
        """ Adjust header level according to base level. """
    def add_anchor(self, c, elem_id) -> None: ...
    def add_permalink(self, c, elem_id) -> None: ...
    def build_toc_div(self, toc_list):
        """ Return a string div given a toc list. """
    def run(self, doc) -> None: ...

class TocExtension(Extension):
    TreeProcessorClass = TocTreeprocessor
    config: Incomplete
    def __init__(self, **kwargs) -> None: ...
    md: Incomplete
    def extendMarkdown(self, md) -> None: ...
    def reset(self) -> None: ...

def makeExtension(**kwargs): ...
