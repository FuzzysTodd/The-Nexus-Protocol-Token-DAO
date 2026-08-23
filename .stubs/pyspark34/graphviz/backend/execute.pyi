import os
import subprocess
import typing

__all__ = ['run_check', 'ExecutableNotFound', 'CalledProcessError']

@typing.overload
def run_check(cmd: typing.Sequence[os.PathLike | str], *, input_lines: typing.Iterator[bytes] | None = ..., encoding: None = ..., quiet: bool = ..., **kwargs) -> subprocess.CompletedProcess:
    """Accept bytes input_lines with default ``encoding=None```."""
@typing.overload
def run_check(cmd: typing.Sequence[os.PathLike | str], *, input_lines: typing.Iterator[str] | None = ..., encoding: str, quiet: bool = ..., **kwargs) -> subprocess.CompletedProcess:
    """Accept string input_lines when given ``encoding``."""
@typing.overload
def run_check(cmd: typing.Sequence[os.PathLike | str], *, input_lines: BytesOrStrIterator | None = ..., encoding: str | None = ..., capture_output: bool = ..., quiet: bool = ..., **kwargs) -> subprocess.CompletedProcess:
    """Accept bytes or string input_lines depending on ``encoding``."""

class ExecutableNotFound(RuntimeError):
    """:exc:`RuntimeError` raised if the Graphviz executable is not found."""
    def __init__(self, args) -> None: ...

class CalledProcessError(subprocess.CalledProcessError):
    """:exc:`~subprocess.CalledProcessError` raised if a subprocess ``returncode`` is not ``0``."""
