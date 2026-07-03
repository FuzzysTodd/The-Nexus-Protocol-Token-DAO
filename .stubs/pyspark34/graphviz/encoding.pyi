from . import copying

__all__ = ['DEFAULT_ENCODING', 'Encoding']

DEFAULT_ENCODING: str

class Encoding(copying.CopyBase):
    """Encoding used for input and output with ``'utf-8'`` default."""
    def __init__(self, *, encoding: str | None = ..., **kwargs) -> None: ...
    @property
    def encoding(self) -> str:
        """The encoding for the saved source file."""
    @encoding.setter
    def encoding(self, encoding: str | None) -> None: ...
