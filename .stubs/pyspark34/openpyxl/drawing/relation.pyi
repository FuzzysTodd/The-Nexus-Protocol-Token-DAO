from _typeshed import Incomplete
from openpyxl.descriptors.excel import Relation as Relation
from openpyxl.descriptors.serialisable import Serialisable as Serialisable
from openpyxl.xml.constants import CHART_NS as CHART_NS

class ChartRelation(Serialisable):
    tagname: str
    namespace = CHART_NS
    id: Incomplete
    def __init__(self, id) -> None: ...
