from . import DistlibException
from .version import PEP440_VERSION_RE
from _typeshed import Incomplete

__all__ = ['Metadata', 'PKG_INFO_ENCODING', 'PKG_INFO_PREFERRED_VERSION']

class MetadataMissingError(DistlibException):
    """A required metadata is missing"""
class MetadataConflictError(DistlibException):
    """Attempt to read or write metadata fields that are conflictual."""
class MetadataUnrecognizedVersionError(DistlibException):
    """Unknown metadata version number."""
class MetadataInvalidError(DistlibException):
    """A metadata value is invalid"""

PKG_INFO_ENCODING: str
PKG_INFO_PREFERRED_VERSION: str

class LegacyMetadata:
    """The legacy metadata of a release.

    Supports versions 1.0, 1.1, 1.2, 2.0 and 1.3/2.1 (auto-detected). You can
    instantiate the class with one of these arguments (or none):
    - *path*, the path to a metadata file
    - *fileobj* give a file-like object with metadata as content
    - *mapping* is a dict-like object
    - *scheme* is a version scheme name
    """
    requires_files: Incomplete
    scheme: Incomplete
    def __init__(self, path: Incomplete | None = None, fileobj: Incomplete | None = None, mapping: Incomplete | None = None, scheme: str = 'default') -> None: ...
    def set_metadata_version(self) -> None: ...
    def __getitem__(self, name): ...
    def __setitem__(self, name, value) -> None: ...
    def __delitem__(self, name) -> None: ...
    def __contains__(self, name) -> bool: ...
    def __getattr__(self, name): ...
    def get_fullname(self, filesafe: bool = False):
        """Return the distribution name with version.

        If filesafe is true, return a filename-escaped form."""
    def is_field(self, name):
        """return True if name is a valid metadata key"""
    def is_multi_field(self, name): ...
    def read(self, filepath) -> None:
        """Read the metadata values from a file path."""
    def read_file(self, fileob) -> None:
        """Read the metadata values from a file object."""
    def write(self, filepath, skip_unknown: bool = False) -> None:
        """Write the metadata fields to filepath."""
    def write_file(self, fileobject, skip_unknown: bool = False) -> None:
        """Write the PKG-INFO format data to a file object."""
    def update(self, other: Incomplete | None = None, **kwargs) -> None:
        """Set metadata values from the given iterable `other` and kwargs.

        Behavior is like `dict.update`: If `other` has a ``keys`` method,
        they are looped over and ``self[key]`` is assigned ``other[key]``.
        Else, ``other`` is an iterable of ``(key, value)`` iterables.

        Keys that don't match a metadata field or that have an empty value are
        dropped.
        """
    def set(self, name, value) -> None:
        """Control then set a metadata field."""
    def get(self, name, default=...):
        """Get a metadata field."""
    def check(self, strict: bool = False):
        """Check if the metadata is compliant. If strict is True then raise if
        no Name or Version are provided"""
    def todict(self, skip_missing: bool = False):
        """Return fields as a dict.

        Field names will be converted to use the underscore-lowercase style
        instead of hyphen-mixed case (i.e. home_page instead of Home-page).
        This is as per https://www.python.org/dev/peps/pep-0566/#id17.
        """
    def add_requirements(self, requirements) -> None: ...
    def keys(self): ...
    def __iter__(self): ...
    def values(self): ...
    def items(self): ...

class Metadata:
    """
    The metadata of a release. This implementation uses 2.1
    metadata where possible. If not possible, it wraps a LegacyMetadata
    instance which handles the key-value metadata format.
    """
    METADATA_VERSION_MATCHER: Incomplete
    NAME_MATCHER: Incomplete
    FIELDNAME_MATCHER: Incomplete
    VERSION_MATCHER = PEP440_VERSION_RE
    SUMMARY_MATCHER: Incomplete
    METADATA_VERSION: str
    GENERATOR: Incomplete
    MANDATORY_KEYS: Incomplete
    INDEX_KEYS: str
    DEPENDENCY_KEYS: str
    SYNTAX_VALIDATORS: Incomplete
    scheme: Incomplete
    def __init__(self, path: Incomplete | None = None, fileobj: Incomplete | None = None, mapping: Incomplete | None = None, scheme: str = 'default') -> None: ...
    common_keys: Incomplete
    none_list: Incomplete
    none_dict: Incomplete
    mapped_keys: Incomplete
    def __getattribute__(self, key): ...
    def __setattr__(self, key, value) -> None: ...
    @property
    def name_and_version(self): ...
    @property
    def provides(self): ...
    @provides.setter
    def provides(self, value) -> None: ...
    def get_requirements(self, reqts, extras: Incomplete | None = None, env: Incomplete | None = None):
        """
        Base method to get dependencies, given a set of extras
        to satisfy and an optional environment context.
        :param reqts: A list of sometimes-wanted dependencies,
                      perhaps dependent on extras and environment.
        :param extras: A list of optional components being requested.
        :param env: An optional environment for marker evaluation.
        """
    @property
    def dictionary(self): ...
    @property
    def dependencies(self): ...
    @dependencies.setter
    def dependencies(self, value) -> None: ...
    def validate(self) -> None: ...
    def todict(self): ...
    LEGACY_MAPPING: Incomplete
    def write(self, path: Incomplete | None = None, fileobj: Incomplete | None = None, legacy: bool = False, skip_unknown: bool = True) -> None: ...
    def add_requirements(self, requirements) -> None: ...
