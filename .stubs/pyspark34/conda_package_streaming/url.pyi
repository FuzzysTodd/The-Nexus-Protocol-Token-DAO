from . import package_streaming as package_streaming
from .lazy_wheel import LazyConda as LazyConda
from _typeshed import Incomplete
from collections.abc import Generator

log: Incomplete
session: Incomplete
METADATA_CHECKLIST: Incomplete

def extract_conda_info(url, destdir, checklist=..., session=...) -> None:
    """
    Extract info/index.json and info/recipe/meta.yaml from url to destdir; close
    url as soon as those files are found.
    """
def stream_conda_info(url, session=...) -> Generator[Incomplete, Incomplete, None]:
    '''
    Yield (tar, member) for conda package at url

    Just "info/" for .conda, all members for tar.
    '''
def conda_reader_for_url(url, session=...):
    """
    Return (name, file_like) suitable for package_streaming APIs
    """
