import os
import typing
from . import jupyter_integration, piping, rendering, saving, unflattening

__all__ = ['Source']

class Source(rendering.Render, saving.Save, jupyter_integration.JupyterIntegration, piping.Pipe, unflattening.Unflatten):
    """Verbatim DOT source code string to be rendered by Graphviz.

    Args:
        source: The verbatim DOT source code string.
        filename: Filename for saving the source (defaults to ``'Source.gv'``).
        directory: (Sub)directory for source saving and rendering.
        format: Rendering output format (``'pdf'``, ``'png'``, ...).
        engine: Layout engine used (``'dot'``, ``'neato'``, ...).
        encoding: Encoding for saving the source.

    Note:
        All parameters except ``source`` are optional. All of them
        can be changed under their corresponding attribute name
        after instance creation.
    """
    @classmethod
    def from_file(cls, filename: os.PathLike | str, directory: os.PathLike | str | None = None, format: str | None = None, engine: str | None = None, encoding: str | None = ..., renderer: str | None = None, formatter: str | None = None) -> Source:
        """Return an instance with the source string read from the given file.

        Args:
            filename: Filename for loading/saving the source.
            directory: (Sub)directory for source loading/saving and rendering.
            format: Rendering output format (``'pdf'``, ``'png'``, ...).
            engine: Layout command used (``'dot'``, ``'neato'``, ...).
            encoding: Encoding for loading/saving the source.
        """
    def __init__(self, source: str, filename: os.PathLike | str | None = None, directory: os.PathLike | str | None = None, format: str | None = None, engine: str | None = None, encoding: str | None = ..., *, renderer: str | None = None, formatter: str | None = None, loaded_from_path: os.PathLike | None = None) -> None: ...
    def __iter__(self) -> typing.Iterator[str]:
        """Yield the DOT source code read from file line by line.

        Yields: Line ending with a newline (``'\\n'``).
        """
    @property
    def source(self) -> str:
        """The DOT source code as string.

        Normalizes so that the string always ends in a final newline.
        """
    def save(self, filename: os.PathLike | str | None = None, directory: os.PathLike | str | None = None, *, skip_existing: bool | None = None) -> str:
        """Save the DOT source to file. Ensure the file ends with a newline.

        Args:
            filename: Filename for saving the source (defaults to ``name`` + ``'.gv'``)
            directory: (Sub)directory for source saving and rendering.
            skip_existing: Skip write if file exists (default: ``None``).
                By default skips if instance was loaded from the target path:
                ``.from_file(self.filepath)``.

        Returns:
            The (possibly relative) path of the saved source file.
        """
