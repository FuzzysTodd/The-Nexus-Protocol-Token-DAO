from pip._internal.models.direct_url import ArchiveInfo as ArchiveInfo, DirInfo as DirInfo, DirectUrl as DirectUrl, VcsInfo as VcsInfo
from pip._internal.models.link import Link as Link
from pip._internal.utils.urls import path_to_url as path_to_url
from pip._internal.vcs import vcs as vcs

def direct_url_as_pep440_direct_reference(direct_url: DirectUrl, name: str) -> str:
    """Convert a DirectUrl to a pip requirement string."""
def direct_url_for_editable(source_dir: str) -> DirectUrl: ...
def direct_url_from_link(link: Link, source_dir: str | None = None, link_is_in_wheel_cache: bool = False) -> DirectUrl: ...
