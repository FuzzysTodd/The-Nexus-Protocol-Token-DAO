import tarfile
from _typeshed import Incomplete
from pathlib import Path
from typing import Generator

__all__ = ['extract_stream', 'extract']

def extract_stream(stream: Generator[tuple[tarfile.TarFile, tarfile.TarInfo], None, None], dest_dir: Path | str):
    """
    Pipe ``stream_conda_component`` output here to extract every member into
    dest_dir.

    For ``.conda`` will need to be called twice (for info and pkg components);
    for ``.tar.bz2`` every member is extracted.
    """
def extract(filename, dest_dir: Incomplete | None = None, fileobj: Incomplete | None = None) -> None:
    """
    Extract all components of conda package to dest_dir.

    fileobj: must be seekable if provided, if a ``.conda`` package.
    """
