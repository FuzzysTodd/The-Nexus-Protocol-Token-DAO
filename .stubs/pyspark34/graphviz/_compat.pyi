import os
import typing
from _typeshed import Incomplete
from typing import Literal

PY38: Incomplete
Literal: typing.Any
Literal = Literal

def get_startupinfo() -> None:
    """Return None for startupinfo argument of ``subprocess.Popen``."""
def make_subprocess_arg(arg: str | os.PathLike) -> str | os.PathLike:
    """Return subprocess argument as is (default no-op)."""
