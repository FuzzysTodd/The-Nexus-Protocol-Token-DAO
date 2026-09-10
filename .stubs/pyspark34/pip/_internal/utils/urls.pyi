from .compat import WINDOWS as WINDOWS

def get_url_scheme(url: str) -> str | None: ...
def path_to_url(path: str) -> str:
    """
    Convert a path to a file: URL.  The path will be made absolute and have
    quoted path parts.
    """
def url_to_path(url: str) -> str:
    """
    Convert a file: URL to a path.
    """
