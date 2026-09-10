from _typeshed import Incomplete
from openpyxl.descriptors import Alias as Alias, Bool as Bool, Integer as Integer, String as String
from openpyxl.descriptors.excel import Base64Binary as Base64Binary
from openpyxl.descriptors.serialisable import Serialisable as Serialisable
from openpyxl.utils.protection import hash_password as hash_password

class _Protected:
    def set_password(self, value: str = '', already_hashed: bool = False) -> None:
        """Set a password on this sheet."""
    @property
    def password(self):
        """Return the password value, regardless of hash."""
    @password.setter
    def password(self, value) -> None:
        """Set a password directly, forcing a hash step."""

class SheetProtection(Serialisable, _Protected):
    """
    Information about protection of various aspects of a sheet. True values
    mean that protection for the object or action is active This is the
    **default** when protection is active, ie. users cannot do something
    """
    tagname: str
    sheet: Incomplete
    enabled: Incomplete
    objects: Incomplete
    scenarios: Incomplete
    formatCells: Incomplete
    formatColumns: Incomplete
    formatRows: Incomplete
    insertColumns: Incomplete
    insertRows: Incomplete
    insertHyperlinks: Incomplete
    deleteColumns: Incomplete
    deleteRows: Incomplete
    selectLockedCells: Incomplete
    selectUnlockedCells: Incomplete
    sort: Incomplete
    autoFilter: Incomplete
    pivotTables: Incomplete
    saltValue: Incomplete
    spinCount: Incomplete
    algorithmName: Incomplete
    hashValue: Incomplete
    __attrs__: Incomplete
    password: Incomplete
    def __init__(self, sheet: bool = False, objects: bool = False, scenarios: bool = False, formatCells: bool = True, formatRows: bool = True, formatColumns: bool = True, insertColumns: bool = True, insertRows: bool = True, insertHyperlinks: bool = True, deleteColumns: bool = True, deleteRows: bool = True, selectLockedCells: bool = False, selectUnlockedCells: bool = False, sort: bool = True, autoFilter: bool = True, pivotTables: bool = True, password: Incomplete | None = None, algorithmName: Incomplete | None = None, saltValue: Incomplete | None = None, spinCount: Incomplete | None = None, hashValue: Incomplete | None = None) -> None: ...
    def set_password(self, value: str = '', already_hashed: bool = False) -> None: ...
    def enable(self) -> None: ...
    def disable(self) -> None: ...
    def __bool__(self) -> bool: ...
