import lxml.etree as etree
from . import base as base
from .. import constants as constants
from ..constants import DataLossWarning as DataLossWarning
from _typeshed import Incomplete

fullTree: bool
tag_regexp: Incomplete
comment_type: Incomplete

class DocumentType:
    name: Incomplete
    publicId: Incomplete
    systemId: Incomplete
    def __init__(self, name, publicId, systemId) -> None: ...

class Document:
    def __init__(self) -> None: ...
    def appendChild(self, element) -> None: ...
    childNodes: Incomplete

def testSerializer(element): ...
def tostring(element):
    """Serialize an element and its child nodes to a string"""

class TreeBuilder(base.TreeBuilder):
    documentClass = Document
    doctypeClass = DocumentType
    elementClass: Incomplete
    commentClass: Incomplete
    fragmentClass = Document
    implementation = etree
    namespaceHTMLElements: Incomplete
    def __init__(self, namespaceHTMLElements, fullTree: bool = False) -> None: ...
    insertComment: Incomplete
    initial_comments: Incomplete
    doctype: Incomplete
    def reset(self) -> None: ...
    def testSerializer(self, element): ...
    def getDocument(self): ...
    def getFragment(self): ...
    def insertDoctype(self, token) -> None: ...
    def insertCommentInitial(self, data, parent: Incomplete | None = None) -> None: ...
    def insertCommentMain(self, data, parent: Incomplete | None = None) -> None: ...
    document: Incomplete
    def insertRoot(self, token) -> None: ...
