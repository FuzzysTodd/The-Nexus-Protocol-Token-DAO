from _typeshed import Incomplete
from pip._internal.models.candidate import InstallationCandidate as InstallationCandidate
from pip._internal.models.link import Link as Link
from pip._internal.utils.urls import path_to_url as path_to_url, url_to_path as url_to_path
from pip._internal.vcs import is_url as is_url
from typing import Callable, Iterable, Tuple

logger: Incomplete
FoundCandidates = Iterable[InstallationCandidate]
FoundLinks = Iterable[Link]
CandidatesFromPage = Callable[[Link], Iterable[InstallationCandidate]]
PageValidator = Callable[[Link], bool]

class LinkSource:
    @property
    def link(self) -> Link | None:
        """Returns the underlying link, if there's one."""
    def page_candidates(self) -> FoundCandidates:
        """Candidates found by parsing an archive listing HTML file."""
    def file_links(self) -> FoundLinks:
        """Links found by specifying archives directly."""

class _FlatDirectorySource(LinkSource):
    """Link source specified by ``--find-links=<path-to-dir>``.

    This looks the content of the directory, and returns:

    * ``page_candidates``: Links listed on each HTML file in the directory.
    * ``file_candidates``: Archives in the directory.
    """
    def __init__(self, candidates_from_page: CandidatesFromPage, path: str) -> None: ...
    @property
    def link(self) -> Link | None: ...
    def page_candidates(self) -> FoundCandidates: ...
    def file_links(self) -> FoundLinks: ...

class _LocalFileSource(LinkSource):
    """``--find-links=<path-or-url>`` or ``--[extra-]index-url=<path-or-url>``.

    If a URL is supplied, it must be a ``file:`` URL. If a path is supplied to
    the option, it is converted to a URL first. This returns:

    * ``page_candidates``: Links listed on an HTML file.
    * ``file_candidates``: The non-HTML file.
    """
    def __init__(self, candidates_from_page: CandidatesFromPage, link: Link) -> None: ...
    @property
    def link(self) -> Link | None: ...
    def page_candidates(self) -> FoundCandidates: ...
    def file_links(self) -> FoundLinks: ...

class _RemoteFileSource(LinkSource):
    """``--find-links=<url>`` or ``--[extra-]index-url=<url>``.

    This returns:

    * ``page_candidates``: Links listed on an HTML file.
    * ``file_candidates``: The non-HTML file.
    """
    def __init__(self, candidates_from_page: CandidatesFromPage, page_validator: PageValidator, link: Link) -> None: ...
    @property
    def link(self) -> Link | None: ...
    def page_candidates(self) -> FoundCandidates: ...
    def file_links(self) -> FoundLinks: ...

class _IndexDirectorySource(LinkSource):
    """``--[extra-]index-url=<path-to-directory>``.

    This is treated like a remote URL; ``candidates_from_page`` contains logic
    for this by appending ``index.html`` to the link.
    """
    def __init__(self, candidates_from_page: CandidatesFromPage, link: Link) -> None: ...
    @property
    def link(self) -> Link | None: ...
    def page_candidates(self) -> FoundCandidates: ...
    def file_links(self) -> FoundLinks: ...

def build_source(location: str, *, candidates_from_page: CandidatesFromPage, page_validator: PageValidator, expand_dir: bool, cache_link_parsing: bool) -> Tuple[str | None, LinkSource | None]: ...
