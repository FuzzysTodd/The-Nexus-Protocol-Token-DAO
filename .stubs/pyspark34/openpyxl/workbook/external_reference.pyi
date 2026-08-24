from _typeshed import Incomplete
from openpyxl.descriptors import Sequence as Sequence
from openpyxl.descriptors.excel import Relation as Relation
from openpyxl.descriptors.serialisable import Serialisable as Serialisable

class ExternalReference(Serialisable):
    tagname: str
    id: Incomplete
    def __init__(self, id) -> None: ...
