from _typeshed import Incomplete
from fsspec.spec import AbstractBufferedFile as AbstractBufferedFile

def noop_file(file, mode, **kwargs): ...

compr: Incomplete

def register_compression(name, callback, extensions, force: bool = False) -> None:
    '''Register an "inferable" file compression type.

    Registers transparent file compression type for use with fsspec.open.
    Compression can be specified by name in open, or "infer"-ed for any files
    ending with the given extensions.

    Args:
        name: (str) The compression type name. Eg. "gzip".
        callback: A callable of form (infile, mode, **kwargs) -> file-like.
            Accepts an input file-like object, the target mode and kwargs.
            Returns a wrapped file-like object.
        extensions: (str, Iterable[str]) A file extension, or list of file
            extensions for which to infer this compression scheme. Eg. "gz".
        force: (bool) Force re-registration of compression type or extensions.

    Raises:
        ValueError: If name or extensions already registered, and not force.

    '''
def unzip(infile, mode: str = 'rb', filename: Incomplete | None = None, **kwargs): ...
def isal(infile, mode: str = 'rb', **kwargs): ...

class SnappyFile(AbstractBufferedFile):
    infile: Incomplete
    codec: Incomplete
    def __init__(self, infile, mode, **kwargs) -> None: ...
    def seek(self, loc, whence: int = 0) -> None: ...
    def seekable(self): ...

def zstandard_file(infile, mode: str = 'rb'): ...
def available_compressions():
    """Return a list of the implemented compressions."""
