import typing
from . import backend, base, encoding

__all__ = ['Pipe']

class Pipe(encoding.Encoding, base.Base, backend.Pipe):
    """Pipe source lines through the Graphviz layout command."""
    @typing.overload
    def pipe(self, format: str | None = ..., renderer: str | None = ..., formatter: str | None = ..., neato_no_op: bool | int | None = ..., quiet: bool = ..., *, engine: str | None = ..., encoding: None = ...) -> bytes:
        """Return bytes with default ``encoding=None``."""
    @typing.overload
    def pipe(self, format: str | None = ..., renderer: str | None = ..., formatter: str | None = ..., neato_no_op: bool | int | None = ..., quiet: bool = ..., *, engine: str | None = ..., encoding: str) -> str:
        """Return string when given encoding."""
    @typing.overload
    def pipe(self, format: str | None = ..., renderer: str | None = ..., formatter: str | None = ..., neato_no_op: bool | int | None = ..., quiet: bool = ..., *, engine: str | None = ..., encoding: str | None) -> bytes | str:
        """Return bytes or string depending on encoding argument."""
