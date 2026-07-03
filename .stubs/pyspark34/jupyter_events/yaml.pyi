from pathlib import PurePath
from typing import Any

def loads(stream: Any) -> Any:
    """Load yaml from a stream."""
def dumps(stream: Any) -> str:
    """Parse the first YAML document in a stream as an object."""
def load(fpath: str | PurePath) -> Any:
    """Load yaml from a file."""
def dump(data: Any, outpath: str | PurePath) -> None:
    """Parse the a YAML document in a file as an object."""
