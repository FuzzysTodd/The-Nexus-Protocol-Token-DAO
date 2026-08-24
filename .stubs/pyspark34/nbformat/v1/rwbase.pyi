class NotebookReader:
    """The base notebook reader."""
    def reads(self, s, **kwargs) -> None:
        """Read a notebook from a string."""
    def read(self, fp, **kwargs):
        """Read a notebook from a file like object"""

class NotebookWriter:
    """The base notebook writer."""
    def writes(self, nb, **kwargs) -> None:
        """Write a notebook to a string."""
    def write(self, nb, fp, **kwargs):
        """Write a notebook to a file like object"""
