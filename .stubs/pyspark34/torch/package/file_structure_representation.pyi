from _typeshed import Incomplete

__all__ = ['Directory']

class Directory:
    """A file structure representation. Organized as Directory nodes that have lists of
    their Directory children. Directories for a package are created by calling
    :meth:`PackageImporter.file_structure`."""
    name: Incomplete
    is_dir: Incomplete
    children: Incomplete
    def __init__(self, name: str, is_dir: bool) -> None: ...
    def has_file(self, filename: str) -> bool:
        """Checks if a file is present in a :class:`Directory`.

        Args:
            filename (str): Path of file to search for.
        Returns:
            bool: If a :class:`Directory` contains the specified file.
        """
