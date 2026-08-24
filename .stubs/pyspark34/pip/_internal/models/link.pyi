import urllib.parse
from _typeshed import Incomplete
from dataclasses import dataclass
from pip._internal.index.collector import IndexContent as IndexContent
from pip._internal.utils.deprecation import deprecated as deprecated
from pip._internal.utils.filetypes import WHEEL_EXTENSION as WHEEL_EXTENSION
from pip._internal.utils.hashes import Hashes as Hashes
from pip._internal.utils.misc import pairwise as pairwise, redact_auth_from_url as redact_auth_from_url, split_auth_from_netloc as split_auth_from_netloc, splitext as splitext
from pip._internal.utils.models import KeyBasedCompareMixin as KeyBasedCompareMixin
from pip._internal.utils.urls import path_to_url as path_to_url, url_to_path as url_to_path
from typing import Any, Dict, List, Mapping, NamedTuple, Tuple

logger: Incomplete

@dataclass(frozen=True)
class LinkHash:
    """Links to content may have embedded hash values. This class parses those.

    `name` must be any member of `_SUPPORTED_HASHES`.

    This class can be converted to and from `ArchiveInfo`. While ArchiveInfo intends to
    be JSON-serializable to conform to PEP 610, this class contains the logic for
    parsing a hash name and value for correctness, and then checking whether that hash
    conforms to a schema with `.is_hash_allowed()`."""
    name: str
    value: str
    def __post_init__(self) -> None: ...
    @classmethod
    def find_hash_url_fragment(cls, url: str) -> LinkHash | None:
        """Search a string for a checksum algorithm name and encoded output value."""
    def as_dict(self) -> Dict[str, str]: ...
    def as_hashes(self) -> Hashes:
        """Return a Hashes instance which checks only for the current hash."""
    def is_hash_allowed(self, hashes: Hashes | None) -> bool:
        """
        Return True if the current hash is allowed by `hashes`.
        """
    def __init__(self, name, value) -> None: ...

@dataclass(frozen=True)
class MetadataFile:
    """Information about a core metadata file associated with a distribution."""
    hashes: Dict[str, str] | None
    def __post_init__(self) -> None: ...
    def __init__(self, hashes) -> None: ...

def supported_hashes(hashes: Dict[str, str] | None) -> Dict[str, str] | None: ...

class Link(KeyBasedCompareMixin):
    """Represents a parsed link from a Package Index's simple URL"""
    comes_from: Incomplete
    requires_python: Incomplete
    yanked_reason: Incomplete
    metadata_file_data: Incomplete
    cache_link_parsing: Incomplete
    egg_fragment: Incomplete
    def __init__(self, url: str, comes_from: str | IndexContent | None = None, requires_python: str | None = None, yanked_reason: str | None = None, metadata_file_data: MetadataFile | None = None, cache_link_parsing: bool = True, hashes: Mapping[str, str] | None = None) -> None:
        '''
        :param url: url of the resource pointed to (href of the link)
        :param comes_from: instance of IndexContent where the link was found,
            or string.
        :param requires_python: String containing the `Requires-Python`
            metadata field, specified in PEP 345. This may be specified by
            a data-requires-python attribute in the HTML link tag, as
            described in PEP 503.
        :param yanked_reason: the reason the file has been yanked, if the
            file has been yanked, or None if the file hasn\'t been yanked.
            This is the value of the "data-yanked" attribute, if present, in
            a simple repository HTML link. If the file has been yanked but
            no reason was provided, this should be the empty string. See
            PEP 592 for more information and the specification.
        :param metadata_file_data: the metadata attached to the file, or None if
            no such metadata is provided. This argument, if not None, indicates
            that a separate metadata file exists, and also optionally supplies
            hashes for that file.
        :param cache_link_parsing: A flag that is used elsewhere to determine
            whether resources retrieved from this link should be cached. PyPI
            URLs should generally have this set to False, for example.
        :param hashes: A mapping of hash names to digests to allow us to
            determine the validity of a download.
        '''
    @classmethod
    def from_json(cls, file_data: Dict[str, Any], page_url: str) -> Link | None:
        """
        Convert an pypi json document from a simple repository page into a Link.
        """
    @classmethod
    def from_element(cls, anchor_attribs: Dict[str, str | None], page_url: str, base_url: str) -> Link | None:
        """
        Convert an anchor element's attributes in a simple repository page to a Link.
        """
    @property
    def url(self) -> str: ...
    @property
    def filename(self) -> str: ...
    @property
    def file_path(self) -> str: ...
    @property
    def scheme(self) -> str: ...
    @property
    def netloc(self) -> str:
        """
        This can contain auth information.
        """
    @property
    def path(self) -> str: ...
    def splitext(self) -> Tuple[str, str]: ...
    @property
    def ext(self) -> str: ...
    @property
    def url_without_fragment(self) -> str: ...
    @property
    def subdirectory_fragment(self) -> str | None: ...
    def metadata_link(self) -> Link | None:
        """Return a link to the associated core metadata file (if any)."""
    def as_hashes(self) -> Hashes: ...
    @property
    def hash(self) -> str | None: ...
    @property
    def hash_name(self) -> str | None: ...
    @property
    def show_url(self) -> str: ...
    @property
    def is_file(self) -> bool: ...
    def is_existing_dir(self) -> bool: ...
    @property
    def is_wheel(self) -> bool: ...
    @property
    def is_vcs(self) -> bool: ...
    @property
    def is_yanked(self) -> bool: ...
    @property
    def has_hash(self) -> bool: ...
    def is_hash_allowed(self, hashes: Hashes | None) -> bool:
        """
        Return True if the link has a hash and it is allowed by `hashes`.
        """

class _CleanResult(NamedTuple):
    '''Convert link for equivalency check.

    This is used in the resolver to check whether two URL-specified requirements
    likely point to the same distribution and can be considered equivalent. This
    equivalency logic avoids comparing URLs literally, which can be too strict
    (e.g. "a=1&b=2" vs "b=2&a=1") and produce conflicts unexpecting to users.

    Currently this does three things:

    1. Drop the basic auth part. This is technically wrong since a server can
       serve different content based on auth, but if it does that, it is even
       impossible to guarantee two URLs without auth are equivalent, since
       the user can input different auth information when prompted. So the
       practical solution is to assume the auth doesn\'t affect the response.
    2. Parse the query to avoid the ordering issue. Note that ordering under the
       same key in the query are NOT cleaned; i.e. "a=1&a=2" and "a=2&a=1" are
       still considered different.
    3. Explicitly drop most of the fragment part, except ``subdirectory=`` and
       hash values, since it should have no impact the downloaded content. Note
       that this drops the "egg=" part historically used to denote the requested
       project (and extras), which is wrong in the strictest sense, but too many
       people are supplying it inconsistently to cause superfluous resolution
       conflicts, so we choose to also ignore them.
    '''
    parsed: urllib.parse.SplitResult
    query: Dict[str, List[str]]
    subdirectory: str
    hashes: Dict[str, str]

def links_equivalent(link1: Link, link2: Link) -> bool: ...
