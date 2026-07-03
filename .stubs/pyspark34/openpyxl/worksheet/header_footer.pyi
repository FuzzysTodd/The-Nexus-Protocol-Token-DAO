from _typeshed import Incomplete
from openpyxl.descriptors import Alias as Alias, Bool as Bool, Integer as Integer, MatchPattern as MatchPattern, Strict as Strict, String as String, Typed as Typed
from openpyxl.descriptors.serialisable import Serialisable as Serialisable
from openpyxl.utils.escape import escape as escape, unescape as unescape
from openpyxl.xml.functions import Element as Element

FONT_PATTERN: str
COLOR_PATTERN: str
SIZE_REGEX: str
FORMAT_REGEX: Incomplete

class _HeaderFooterPart(Strict):
    '''
    Individual left/center/right header/footer part

    Do not use directly.

    Header & Footer ampersand codes:

    * &A   Inserts the worksheet name
    * &B   Toggles bold
    * &D or &[Date]   Inserts the current date
    * &E   Toggles double-underline
    * &F or &[File]   Inserts the workbook name
    * &I   Toggles italic
    * &N or &[Pages]   Inserts the total page count
    * &S   Toggles strikethrough
    * &T   Inserts the current time
    * &[Tab]   Inserts the worksheet name
    * &U   Toggles underline
    * &X   Toggles superscript
    * &Y   Toggles subscript
    * &P or &[Page]   Inserts the current page number
    * &P+n   Inserts the page number incremented by n
    * &P-n   Inserts the page number decremented by n
    * &[Path]   Inserts the workbook path
    * &&   Escapes the ampersand character
    * &"fontname"   Selects the named font
    * &nn   Selects the specified 2-digit font point size

    Colours are in RGB Hex
    '''
    text: Incomplete
    font: Incomplete
    size: Incomplete
    RGB: str
    color: Incomplete
    def __init__(self, text: Incomplete | None = None, font: Incomplete | None = None, size: Incomplete | None = None, color: Incomplete | None = None) -> None: ...
    def __bool__(self) -> bool: ...
    @classmethod
    def from_str(cls, text):
        """
        Convert from miniformat to object
        """

class HeaderFooterItem(Strict):
    """
    Header or footer item

    """
    left: Incomplete
    center: Incomplete
    centre: Incomplete
    right: Incomplete
    def __init__(self, left: Incomplete | None = None, right: Incomplete | None = None, center: Incomplete | None = None) -> None: ...
    def __bool__(self) -> bool: ...
    def to_tree(self, tagname):
        """
        Return as XML node
        """
    @classmethod
    def from_tree(cls, node): ...

class HeaderFooter(Serialisable):
    tagname: str
    differentOddEven: Incomplete
    differentFirst: Incomplete
    scaleWithDoc: Incomplete
    alignWithMargins: Incomplete
    oddHeader: Incomplete
    oddFooter: Incomplete
    evenHeader: Incomplete
    evenFooter: Incomplete
    firstHeader: Incomplete
    firstFooter: Incomplete
    __elements__: Incomplete
    def __init__(self, differentOddEven: Incomplete | None = None, differentFirst: Incomplete | None = None, scaleWithDoc: Incomplete | None = None, alignWithMargins: Incomplete | None = None, oddHeader: Incomplete | None = None, oddFooter: Incomplete | None = None, evenHeader: Incomplete | None = None, evenFooter: Incomplete | None = None, firstHeader: Incomplete | None = None, firstFooter: Incomplete | None = None) -> None: ...
    def __bool__(self) -> bool: ...
