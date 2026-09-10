from _typeshed import Incomplete
from openpyxl.descriptors import Typed as Typed
from openpyxl.descriptors.nested import NestedText as NestedText
from openpyxl.descriptors.serialisable import Serialisable as Serialisable
from openpyxl.xml.constants import XPROPS_NS as XPROPS_NS

def get_version(): ...

class DigSigBlob(Serialisable):
    __elements__: Incomplete
    __attrs__: Incomplete

class VectorLpstr(Serialisable):
    __elements__: Incomplete
    __attrs__: Incomplete

class VectorVariant(Serialisable):
    __elements__: Incomplete
    __attrs__: Incomplete

class ExtendedProperties(Serialisable):
    """
    See 22.2

    Most of this is irrelevant
    """
    tagname: str
    Template: Incomplete
    Manager: Incomplete
    Company: Incomplete
    Pages: Incomplete
    Words: Incomplete
    Characters: Incomplete
    PresentationFormat: Incomplete
    Lines: Incomplete
    Paragraphs: Incomplete
    Slides: Incomplete
    Notes: Incomplete
    TotalTime: Incomplete
    HiddenSlides: Incomplete
    MMClips: Incomplete
    ScaleCrop: Incomplete
    HeadingPairs: Incomplete
    TitlesOfParts: Incomplete
    LinksUpToDate: Incomplete
    CharactersWithSpaces: Incomplete
    SharedDoc: Incomplete
    HyperlinkBase: Incomplete
    HLinks: Incomplete
    HyperlinksChanged: Incomplete
    DigSig: Incomplete
    Application: Incomplete
    AppVersion: Incomplete
    DocSecurity: Incomplete
    __elements__: Incomplete
    def __init__(self, Template: Incomplete | None = None, Manager: Incomplete | None = None, Company: Incomplete | None = None, Pages: Incomplete | None = None, Words: Incomplete | None = None, Characters: Incomplete | None = None, PresentationFormat: Incomplete | None = None, Lines: Incomplete | None = None, Paragraphs: Incomplete | None = None, Slides: Incomplete | None = None, Notes: Incomplete | None = None, TotalTime: Incomplete | None = None, HiddenSlides: Incomplete | None = None, MMClips: Incomplete | None = None, ScaleCrop: Incomplete | None = None, HeadingPairs: Incomplete | None = None, TitlesOfParts: Incomplete | None = None, LinksUpToDate: Incomplete | None = None, CharactersWithSpaces: Incomplete | None = None, SharedDoc: Incomplete | None = None, HyperlinkBase: Incomplete | None = None, HLinks: Incomplete | None = None, HyperlinksChanged: Incomplete | None = None, DigSig: Incomplete | None = None, Application: str = 'Microsoft Excel', AppVersion: Incomplete | None = None, DocSecurity: Incomplete | None = None) -> None: ...
    def to_tree(self): ...
