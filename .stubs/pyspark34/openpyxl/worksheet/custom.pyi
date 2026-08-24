from _typeshed import Incomplete
from openpyxl.descriptors import Sequence as Sequence, String as String
from openpyxl.descriptors.serialisable import Serialisable as Serialisable

class CustomProperty(Serialisable):
    tagname: str
    name: Incomplete
    def __init__(self, name: Incomplete | None = None) -> None: ...

class CustomProperties(Serialisable):
    tagname: str
    customPr: Incomplete
    __elements__: Incomplete
    def __init__(self, customPr=()) -> None: ...
