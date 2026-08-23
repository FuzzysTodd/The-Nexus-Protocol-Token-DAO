from . import Extension as Extension
from ..preprocessors import Preprocessor as Preprocessor
from ..util import parseBoolValue as parseBoolValue
from .attr_list import AttrListExtension as AttrListExtension, get_attrs as get_attrs
from .codehilite import CodeHilite as CodeHilite, CodeHiliteExtension as CodeHiliteExtension, parse_hl_lines as parse_hl_lines
from _typeshed import Incomplete

class FencedCodeExtension(Extension):
    config: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def extendMarkdown(self, md) -> None:
        """ Add `FencedBlockPreprocessor` to the Markdown instance. """

class FencedBlockPreprocessor(Preprocessor):
    FENCED_BLOCK_RE: Incomplete
    config: Incomplete
    checked_for_deps: bool
    codehilite_conf: Incomplete
    use_attr_list: bool
    bool_options: Incomplete
    def __init__(self, md, config) -> None: ...
    def run(self, lines):
        """ Match and store Fenced Code Blocks in the `HtmlStash`. """
    def handle_attrs(self, attrs):
        """ Return tuple: (id, [list, of, classes], {configs}) """

def makeExtension(**kwargs): ...
