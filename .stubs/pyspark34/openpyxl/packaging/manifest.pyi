from _typeshed import Incomplete
from collections.abc import Generator
from openpyxl.descriptors import Sequence as Sequence, String as String
from openpyxl.descriptors.serialisable import Serialisable as Serialisable
from openpyxl.xml.constants import ACTIVEX as ACTIVEX, ARC_CONTENT_TYPES as ARC_CONTENT_TYPES, ARC_STYLE as ARC_STYLE, ARC_THEME as ARC_THEME, CONTYPES_NS as CONTYPES_NS, CTRL as CTRL, STYLES_TYPE as STYLES_TYPE, THEME_TYPE as THEME_TYPE, VBA as VBA
from openpyxl.xml.functions import fromstring as fromstring, tostring as tostring

mimetypes: Incomplete

class FileExtension(Serialisable):
    tagname: str
    Extension: Incomplete
    ContentType: Incomplete
    def __init__(self, Extension, ContentType) -> None: ...

class Override(Serialisable):
    tagname: str
    PartName: Incomplete
    ContentType: Incomplete
    def __init__(self, PartName, ContentType) -> None: ...

DEFAULT_TYPES: Incomplete
DEFAULT_OVERRIDE: Incomplete

class Manifest(Serialisable):
    tagname: str
    Default: Incomplete
    Override: Incomplete
    path: str
    __elements__: Incomplete
    def __init__(self, Default=(), Override=()) -> None: ...
    @property
    def filenames(self): ...
    @property
    def extensions(self):
        """
        Map content types to file extensions
        Skip parts without extensions
        """
    def to_tree(self):
        """
        Custom serialisation method to allow setting a default namespace
        """
    def __contains__(self, content_type) -> bool:
        """
        Check whether a particular content type is contained
        """
    def find(self, content_type):
        """
        Find specific content-type
        """
    def findall(self, content_type) -> Generator[Incomplete, None, None]:
        """
        Find all elements of a specific content-type
        """
    def append(self, obj) -> None:
        """
        Add content object to the package manifest
        # needs a contract...
        """
