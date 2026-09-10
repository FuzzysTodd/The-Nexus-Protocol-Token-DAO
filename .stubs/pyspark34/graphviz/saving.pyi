import os
from . import base, encoding
from _typeshed import Incomplete

__all__ = ['Save']

class Save(encoding.Encoding, base.Base):
    """Save DOT source lines to file."""
    directory: str
    filename: Incomplete
    def __init__(self, *, filename: os.PathLike | str, directory: os.PathLike | str | None = None, **kwargs) -> None: ...
    @property
    def filepath(self) -> str:
        """The target path for saving the DOT source file."""
    def save(self, filename: os.PathLike | str | None = None, directory: os.PathLike | str | None = None, *, skip_existing: bool | None = False) -> str:
        """Save the DOT source to file. Ensure the file ends with a newline.

        Args:
            filename: Filename for saving the source (defaults to ``name`` + ``'.gv'``)
            directory: (Sub)directory for source saving and rendering.
            skip_existing: Skip write if file exists (default: ``False``).

        Returns:
            The (possibly relative) path of the saved source file.
        """
