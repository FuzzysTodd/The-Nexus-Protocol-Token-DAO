import datetime
from _typeshed import Incomplete
from openpyxl.descriptors import Alias as Alias, DateTime as DateTime
from openpyxl.descriptors.nested import NestedText as NestedText
from openpyxl.descriptors.serialisable import Serialisable as Serialisable
from openpyxl.xml.constants import COREPROPS_NS as COREPROPS_NS, DCORE_NS as DCORE_NS, DCTERMS_NS as DCTERMS_NS, XSI_NS as XSI_NS
from openpyxl.xml.functions import Element as Element, QName as QName

class NestedDateTime(DateTime, NestedText):
    expected_type = datetime.datetime
    def to_tree(self, tagname: Incomplete | None = None, value: Incomplete | None = None, namespace: Incomplete | None = None): ...

class QualifiedDateTime(NestedDateTime):
    """In certain situations Excel will complain if the additional type
    attribute isn't set"""
    def to_tree(self, tagname: Incomplete | None = None, value: Incomplete | None = None, namespace: Incomplete | None = None): ...

class DocumentProperties(Serialisable):
    """High-level properties of the document.
    Defined in ECMA-376 Par2 Annex D
    """
    tagname: str
    namespace = COREPROPS_NS
    category: Incomplete
    contentStatus: Incomplete
    keywords: Incomplete
    lastModifiedBy: Incomplete
    lastPrinted: Incomplete
    revision: Incomplete
    version: Incomplete
    last_modified_by: Incomplete
    subject: Incomplete
    title: Incomplete
    creator: Incomplete
    description: Incomplete
    identifier: Incomplete
    language: Incomplete
    created: Incomplete
    modified: Incomplete
    __elements__: Incomplete
    def __init__(self, category: Incomplete | None = None, contentStatus: Incomplete | None = None, keywords: Incomplete | None = None, lastModifiedBy: Incomplete | None = None, lastPrinted: Incomplete | None = None, revision: Incomplete | None = None, version: Incomplete | None = None, created: Incomplete | None = None, creator: str = 'openpyxl', description: Incomplete | None = None, identifier: Incomplete | None = None, language: Incomplete | None = None, modified: Incomplete | None = None, subject: Incomplete | None = None, title: Incomplete | None = None) -> None: ...
