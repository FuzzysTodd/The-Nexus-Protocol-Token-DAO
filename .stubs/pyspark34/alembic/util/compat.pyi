import io
import os
from _typeshed import Incomplete
from configparser import ConfigParser
from importlib_metadata import EntryPoint as EntryPoint
from sqlalchemy.util import inspect_getfullargspec as inspect_getfullargspec
from sqlalchemy.util.compat import inspect_formatargspec as inspect_formatargspec
from typing import Sequence

is_posix: Incomplete
py311: Incomplete
py310: Incomplete
py39: Incomplete
py38: Incomplete

class EncodedIO(io.TextIOWrapper):
    def close(self) -> None: ...

def importlib_metadata_get(group: str) -> Sequence[EntryPoint]: ...
def formatannotation_fwdref(annotation, base_module: Incomplete | None = None):
    """vendored from python 3.7"""
def read_config_parser(file_config: ConfigParser, file_argument: Sequence[str | os.PathLike[str]]) -> list[str]: ...
