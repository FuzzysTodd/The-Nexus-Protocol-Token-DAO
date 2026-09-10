from pathlib import Path

__all__ = ['raise_on_not_writable_file', 'ensure_directory_exists']

def raise_on_not_writable_file(filename: str) -> None:
    """
    Raise an exception if attempting to open the file for writing would fail.
    This is done so files that will never be writable can be separated from
    files that are writable but currently locked
    :param filename: file to check
    :raises OSError: as if the file was opened for writing.
    """
def ensure_directory_exists(filename: Path | str) -> None:
    """
    Ensure the directory containing the file exists (create it if necessary)
    :param filename: file.
    """
