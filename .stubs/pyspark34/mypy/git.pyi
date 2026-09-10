def is_git_repo(dir: str) -> bool:
    """Is the given directory version-controlled with git?"""
def have_git() -> bool:
    """Can we run the git executable?"""
def git_revision(dir: str) -> bytes:
    """Get the SHA-1 of the HEAD of a git repository."""
def is_dirty(dir: str) -> bool:
    """Check whether a git repository has uncommitted changes."""
