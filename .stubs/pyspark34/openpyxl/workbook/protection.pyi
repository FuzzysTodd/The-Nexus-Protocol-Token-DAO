from _typeshed import Incomplete
from openpyxl.descriptors import Alias as Alias, Bool as Bool, Float as Float, Integer as Integer, NoneSet as NoneSet, Set as Set, String as String, Typed as Typed
from openpyxl.descriptors.excel import Base64Binary as Base64Binary, ExtensionList as ExtensionList, Guid as Guid, HexBinary as HexBinary, Relation as Relation
from openpyxl.descriptors.serialisable import Serialisable as Serialisable
from openpyxl.utils.protection import hash_password as hash_password

class WorkbookProtection(Serialisable):
    tagname: str
    workbook_password: Incomplete
    workbookPasswordCharacterSet: Incomplete
    revision_password: Incomplete
    revisionsPasswordCharacterSet: Incomplete
    lockStructure: Incomplete
    lock_structure: Incomplete
    lockWindows: Incomplete
    lock_windows: Incomplete
    lockRevision: Incomplete
    lock_revision: Incomplete
    revisionsAlgorithmName: Incomplete
    revisionsHashValue: Incomplete
    revisionsSaltValue: Incomplete
    revisionsSpinCount: Incomplete
    workbookAlgorithmName: Incomplete
    workbookHashValue: Incomplete
    workbookSaltValue: Incomplete
    workbookSpinCount: Incomplete
    __attrs__: Incomplete
    def __init__(self, workbookPassword: Incomplete | None = None, workbookPasswordCharacterSet: Incomplete | None = None, revisionsPassword: Incomplete | None = None, revisionsPasswordCharacterSet: Incomplete | None = None, lockStructure: Incomplete | None = None, lockWindows: Incomplete | None = None, lockRevision: Incomplete | None = None, revisionsAlgorithmName: Incomplete | None = None, revisionsHashValue: Incomplete | None = None, revisionsSaltValue: Incomplete | None = None, revisionsSpinCount: Incomplete | None = None, workbookAlgorithmName: Incomplete | None = None, workbookHashValue: Incomplete | None = None, workbookSaltValue: Incomplete | None = None, workbookSpinCount: Incomplete | None = None) -> None: ...
    def set_workbook_password(self, value: str = '', already_hashed: bool = False) -> None:
        """Set a password on this workbook."""
    @property
    def workbookPassword(self):
        """Return the workbook password value, regardless of hash."""
    @workbookPassword.setter
    def workbookPassword(self, value) -> None:
        """Set a workbook password directly, forcing a hash step."""
    def set_revisions_password(self, value: str = '', already_hashed: bool = False) -> None:
        """Set a revision password on this workbook."""
    @property
    def revisionsPassword(self):
        """Return the revisions password value, regardless of hash."""
    @revisionsPassword.setter
    def revisionsPassword(self, value) -> None:
        """Set a revisions password directly, forcing a hash step."""
    @classmethod
    def from_tree(cls, node):
        """Don't hash passwords when deserialising from XML"""
DocumentSecurity = WorkbookProtection

class FileSharing(Serialisable):
    tagname: str
    readOnlyRecommended: Incomplete
    userName: Incomplete
    reservationPassword: Incomplete
    algorithmName: Incomplete
    hashValue: Incomplete
    saltValue: Incomplete
    spinCount: Incomplete
    def __init__(self, readOnlyRecommended: Incomplete | None = None, userName: Incomplete | None = None, reservationPassword: Incomplete | None = None, algorithmName: Incomplete | None = None, hashValue: Incomplete | None = None, saltValue: Incomplete | None = None, spinCount: Incomplete | None = None) -> None: ...
