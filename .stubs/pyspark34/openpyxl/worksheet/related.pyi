from _typeshed import Incomplete
from openpyxl.descriptors.excel import Relation as Relation
from openpyxl.descriptors.serialisable import Serialisable as Serialisable

class Related(Serialisable):
    id: Incomplete
    def __init__(self, id: Incomplete | None = None) -> None: ...
    def to_tree(self, tagname, idx: Incomplete | None = None): ...
