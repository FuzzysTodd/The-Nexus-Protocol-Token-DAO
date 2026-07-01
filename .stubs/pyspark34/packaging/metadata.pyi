import typing
from . import requirements as requirements, specifiers as specifiers, utils as utils, version as version_module
from _typeshed import Incomplete
from typing import Dict, Generic, List, Tuple, Type, TypedDict

T = typing.TypeVar('T')
ExceptionGroup: Incomplete

class ExceptionGroup(Exception):
    """A minimal implementation of :external:exc:`ExceptionGroup` from Python 3.11.

        If :external:exc:`ExceptionGroup` is already defined by Python itself,
        that version is used instead.
        """
    message: str
    exceptions: List[Exception]
    def __init__(self, message: str, exceptions: List[Exception]) -> None: ...

class InvalidMetadata(ValueError):
    """A metadata field contains invalid data."""
    field: str
    def __init__(self, field: str, message: str) -> None: ...

class RawMetadata(TypedDict, total=False):
    """A dictionary of raw core metadata.

    Each field in core metadata maps to a key of this dictionary (when data is
    provided). The key is lower-case and underscores are used instead of dashes
    compared to the equivalent core metadata field. Any core metadata field that
    can be specified multiple times or can hold multiple values in a single
    field have a key with a plural name. See :class:`Metadata` whose attributes
    match the keys of this dictionary.

    Core metadata fields that can be specified multiple times are stored as a
    list or dict depending on which is appropriate for the field. Any fields
    which hold multiple values in a single field are stored as a list.

    """
    metadata_version: str
    name: str
    version: str
    platforms: List[str]
    summary: str
    description: str
    keywords: List[str]
    home_page: str
    author: str
    author_email: str
    license: str
    supported_platforms: List[str]
    download_url: str
    classifiers: List[str]
    requires: List[str]
    provides: List[str]
    obsoletes: List[str]
    maintainer: str
    maintainer_email: str
    requires_dist: List[str]
    provides_dist: List[str]
    obsoletes_dist: List[str]
    requires_python: str
    requires_external: List[str]
    project_urls: Dict[str, str]
    description_content_type: str
    provides_extra: List[str]
    dynamic: List[str]

def parse_email(data: bytes | str) -> Tuple[RawMetadata, Dict[str, List[str]]]:
    """Parse a distribution's metadata stored as email headers (e.g. from ``METADATA``).

    This function returns a two-item tuple of dicts. The first dict is of
    recognized fields from the core metadata specification. Fields that can be
    parsed and translated into Python's built-in types are converted
    appropriately. All other fields are left as-is. Fields that are allowed to
    appear multiple times are stored as lists.

    The second dict contains all other fields from the metadata. This includes
    any unrecognized fields. It also includes any fields which are expected to
    be parsed into a built-in type but were not formatted appropriately. Finally,
    any fields that are expected to appear only once but are repeated are
    included in this dict.

    """

class _Validator(Generic[T]):
    '''Validate a metadata field.

    All _process_*() methods correspond to a core metadata field. The method is
    called with the field\'s raw value. If the raw value is valid it is returned
    in its "enriched" form (e.g. ``version.Version`` for the ``Version`` field).
    If the raw value is invalid, :exc:`InvalidMetadata` is raised (with a cause
    as appropriate).
    '''
    name: str
    raw_name: str
    added: _MetadataVersion
    def __init__(self, *, added: _MetadataVersion = '1.0') -> None: ...
    def __set_name__(self, _owner: Metadata, name: str) -> None: ...
    def __get__(self, instance: Metadata, _owner: Type['Metadata']) -> T: ...

class Metadata:
    """Representation of distribution metadata.

    Compared to :class:`RawMetadata`, this class provides objects representing
    metadata fields instead of only using built-in types. Any invalid metadata
    will cause :exc:`InvalidMetadata` to be raised (with a
    :py:attr:`~BaseException.__cause__` attribute as appropriate).
    """
    @classmethod
    def from_raw(cls, data: RawMetadata, *, validate: bool = True) -> Metadata:
        """Create an instance from :class:`RawMetadata`.

        If *validate* is true, all metadata will be validated. All exceptions
        related to validation will be gathered and raised as an :class:`ExceptionGroup`.
        """
    @classmethod
    def from_email(cls, data: bytes | str, *, validate: bool = True) -> Metadata:
        """Parse metadata from email headers.

        If *validate* is true, the metadata will be validated. All exceptions
        related to validation will be gathered and raised as an :class:`ExceptionGroup`.
        """
    metadata_version: _Validator[_MetadataVersion]
    name: _Validator[str]
    version: _Validator[version_module.Version]
    dynamic: _Validator[List[str]]
    platforms: _Validator[List[str]]
    supported_platforms: _Validator[List[str]]
    summary: _Validator[str]
    description: _Validator[str]
    description_content_type: _Validator[str]
    keywords: _Validator[List[str]]
    home_page: _Validator[str]
    download_url: _Validator[str]
    author: _Validator[str]
    author_email: _Validator[str]
    maintainer: _Validator[str]
    maintainer_email: _Validator[str]
    license: _Validator[str]
    classifiers: _Validator[List[str]]
    requires_dist: _Validator[List[requirements.Requirement]]
    requires_python: _Validator[specifiers.SpecifierSet]
    requires_external: _Validator[List[str]]
    project_urls: _Validator[Dict[str, str]]
    provides_extra: _Validator[List[utils.NormalizedName]]
    provides_dist: _Validator[List[str]]
    obsoletes_dist: _Validator[List[str]]
    requires: _Validator[List[str]]
    provides: _Validator[List[str]]
    obsoletes: _Validator[List[str]]
