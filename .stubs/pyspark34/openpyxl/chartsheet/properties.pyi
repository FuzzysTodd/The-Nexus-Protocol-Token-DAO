from _typeshed import Incomplete
from openpyxl.descriptors import Bool as Bool, String as String, Typed as Typed
from openpyxl.descriptors.serialisable import Serialisable as Serialisable
from openpyxl.styles import Color as Color

class ChartsheetProperties(Serialisable):
    tagname: str
    published: Incomplete
    codeName: Incomplete
    tabColor: Incomplete
    __elements__: Incomplete
    def __init__(self, published: Incomplete | None = None, codeName: Incomplete | None = None, tabColor: Incomplete | None = None) -> None: ...
