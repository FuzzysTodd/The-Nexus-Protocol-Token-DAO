from _typeshed import Incomplete
from openpyxl.descriptors import Integer as Integer, Sequence as Sequence, String as String
from openpyxl.descriptors.serialisable import Serialisable as Serialisable

class FunctionGroup(Serialisable):
    tagname: str
    name: Incomplete
    def __init__(self, name: Incomplete | None = None) -> None: ...

class FunctionGroupList(Serialisable):
    tagname: str
    builtInGroupCount: Incomplete
    functionGroup: Incomplete
    __elements__: Incomplete
    def __init__(self, builtInGroupCount: int = 16, functionGroup=()) -> None: ...
