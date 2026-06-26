from _typeshed import Incomplete
from openpyxl.descriptors import Bool as Bool, Integer as Integer, String as String
from openpyxl.descriptors.excel import Base64Binary as Base64Binary
from openpyxl.descriptors.serialisable import Serialisable as Serialisable
from openpyxl.worksheet.protection import _Protected, hash_password as hash_password

class ChartsheetProtection(Serialisable, _Protected):
    tagname: str
    algorithmName: Incomplete
    hashValue: Incomplete
    saltValue: Incomplete
    spinCount: Incomplete
    content: Incomplete
    objects: Incomplete
    __attrs__: Incomplete
    password: Incomplete
    def __init__(self, content: Incomplete | None = None, objects: Incomplete | None = None, hashValue: Incomplete | None = None, spinCount: Incomplete | None = None, saltValue: Incomplete | None = None, algorithmName: Incomplete | None = None, password: Incomplete | None = None) -> None: ...
