from . import Extension as Extension
from ..treeprocessors import Treeprocessor as Treeprocessor
from _typeshed import Incomplete

def get_attrs(str):
    """ Parse attribute list and return a list of attribute tuples. """
def isheader(elem): ...

class AttrListTreeprocessor(Treeprocessor):
    BASE_RE: str
    HEADER_RE: Incomplete
    BLOCK_RE: Incomplete
    INLINE_RE: Incomplete
    NAME_RE: Incomplete
    def run(self, doc) -> None: ...
    def assign_attrs(self, elem, attrs) -> None:
        """ Assign `attrs` to element. """
    def sanitize_name(self, name):
        '''
        Sanitize name as \'an XML Name, minus the ":"\'.
        See https://www.w3.org/TR/REC-xml-names/#NT-NCName
        '''

class AttrListExtension(Extension):
    def extendMarkdown(self, md) -> None: ...

def makeExtension(**kwargs): ...
