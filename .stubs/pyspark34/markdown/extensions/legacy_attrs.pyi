from _typeshed import Incomplete
from markdown.extensions import Extension as Extension
from markdown.treeprocessors import Treeprocessor as Treeprocessor, isString as isString

ATTR_RE: Incomplete

class LegacyAttrs(Treeprocessor):
    def run(self, doc) -> None:
        """Find and set values of attributes ({@key=value}). """
    def handleAttributes(self, el, txt):
        """ Set attributes and return text without definitions. """

class LegacyAttrExtension(Extension):
    def extendMarkdown(self, md) -> None: ...

def makeExtension(**kwargs): ...
