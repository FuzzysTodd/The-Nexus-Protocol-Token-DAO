from typing import BinaryIO

def sha_fileobj(fileobj: BinaryIO, chunk_size: int | None = None) -> bytes:
    '''
    Computes the sha256 hash of the given file object, by chunks of size `chunk_size`.

    Args:
        fileobj (file-like object):
            The File object to compute sha256 for, typically obtained with `open(path, "rb")`
        chunk_size (`int`, *optional*):
            The number of bytes to read from `fileobj` at once, defaults to 1MB.

    Returns:
        `bytes`: `fileobj`\'s sha256 hash as bytes
    '''
