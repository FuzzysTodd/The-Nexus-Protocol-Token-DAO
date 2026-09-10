from _typeshed import Incomplete
from collections.abc import Generator
from openpyxl.descriptors import Alias as Alias, Sequence as Sequence, String as String
from openpyxl.descriptors.serialisable import Serialisable as Serialisable
from openpyxl.xml.constants import PKG_REL_NS as PKG_REL_NS, REL_NS as REL_NS
from openpyxl.xml.functions import Element as Element, fromstring as fromstring

class Relationship(Serialisable):
    """Represents many kinds of relationships."""
    tagname: str
    Type: Incomplete
    Target: Incomplete
    target: Incomplete
    TargetMode: Incomplete
    Id: Incomplete
    id: Incomplete
    def __init__(self, Id: Incomplete | None = None, Type: Incomplete | None = None, type: Incomplete | None = None, Target: Incomplete | None = None, TargetMode: Incomplete | None = None) -> None:
        """
        `type` can be used as a shorthand with the default relationships namespace
        otherwise the `Type` must be a fully qualified URL
        """

class RelationshipList(Serialisable):
    tagname: str
    Relationship: Incomplete
    def __init__(self, Relationship=()) -> None: ...
    def append(self, value) -> None: ...
    def __len__(self) -> int: ...
    def __bool__(self) -> bool: ...
    def find(self, content_type) -> Generator[Incomplete, None, None]:
        """
        Find relationships by content-type
        NB. these content-types namespaced objects and different to the MIME-types
        in the package manifest :-(
        """
    def __getitem__(self, key): ...
    def to_tree(self): ...

def get_rels_path(path):
    """
    Convert relative path to absolutes that can be loaded from a zip
    archive.
    The path to be passed in is that of containing object (workbook,
    worksheet, etc.)
    """
def get_dependents(archive, filename):
    """
    Normalise dependency file paths to absolute ones

    Relative paths are relative to parent object
    """
def get_rel(archive, deps, id: Incomplete | None = None, cls: Incomplete | None = None):
    """
    Get related object based on id or rel_type
    """
