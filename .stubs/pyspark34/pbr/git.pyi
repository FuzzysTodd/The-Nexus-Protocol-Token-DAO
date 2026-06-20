from _typeshed import Incomplete
from pbr import options as options, version as version

def get_is_release(git_dir): ...
def get_git_short_sha(git_dir: Incomplete | None = None):
    """Return the short sha for this repo, if it exists."""
def write_git_changelog(git_dir: Incomplete | None = None, dest_dir=..., option_dict: Incomplete | None = None, changelog: Incomplete | None = None) -> None:
    """Write a changelog based on the git changelog."""
def generate_authors(git_dir: Incomplete | None = None, dest_dir: str = '.', option_dict=...) -> None:
    """Create AUTHORS file using git commits."""
