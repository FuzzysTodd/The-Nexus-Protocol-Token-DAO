from _typeshed import Incomplete
from openpyxl.descriptors.excel import Relation as Relation
from openpyxl.descriptors.serialisable import Serialisable as Serialisable

class Drawing(Serialisable):
    tagname: str
    id: Incomplete
    def __init__(self, id: Incomplete | None = None) -> None: ...
