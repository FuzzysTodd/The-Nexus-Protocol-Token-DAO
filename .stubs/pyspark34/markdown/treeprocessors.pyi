from . import inlinepatterns as inlinepatterns, util as util
from _typeshed import Incomplete

def build_treeprocessors(md, **kwargs):
    """ Build the default  `treeprocessors` for Markdown. """
def isString(s):
    """ Check if it's string """

class Treeprocessor(util.Processor):
    """
    `Treeprocessor`s are run on the `ElementTree` object before serialization.

    Each `Treeprocessor` implements a `run` method that takes a pointer to an
    `ElementTree`, modifies it as necessary and returns an `ElementTree`
    object.

    `Treeprocessors` must extend `markdown.Treeprocessor`.

    """
    def run(self, root) -> None:
        """
        Subclasses of `Treeprocessor` should implement a `run` method, which
        takes a root `ElementTree`. This method can return another `ElementTree`
        object, and the existing root `ElementTree `will be replaced, or it can
        modify the current tree and return `None`.
        """

class InlineProcessor(Treeprocessor):
    """
    A `Treeprocessor` that traverses a tree, applying inline patterns.
    """
    md: Incomplete
    inlinePatterns: Incomplete
    ancestors: Incomplete
    def __init__(self, md) -> None: ...
    stashed_nodes: Incomplete
    parent_map: Incomplete
    def run(self, tree, ancestors: Incomplete | None = None):
        '''Apply inline patterns to a parsed Markdown tree.

        Iterate over `ElementTree`, find elements with inline tag, apply inline
        patterns and append newly created Elements to tree.  If you don\'t
        want to process your data with inline patterns, instead of normal
        string, use subclass `AtomicString`:

            node.text = markdown.AtomicString("This will not be processed.")

        Arguments:

        * `tree`: `ElementTree` object, representing Markdown tree.
        * `ancestors`: List of parent tag names that precede the tree node (if needed).

        Returns: `ElementTree` object with applied inline patterns.

        '''

class PrettifyTreeprocessor(Treeprocessor):
    """ Add line breaks to the html document. """
    def run(self, root) -> None:
        """ Add line breaks to `ElementTree` root object. """

class UnescapeTreeprocessor(Treeprocessor):
    """ Restore escaped chars """
    RE: Incomplete
    def unescape(self, text): ...
    def run(self, root) -> None:
        """ Loop over all elements and unescape all text. """
