from .utils import TemporaryDirectory as TemporaryDirectory
from _typeshed import Incomplete
from pathlib import Path

def validate_converted_files_match(src_file_or_folder, subject, reference_ext: str = ''): ...
def hash_fn(): ...

IGNORE_FIELDS: Incomplete

def validate_converted_files_match_streaming(src: str | Path, reference: str | Path, *, strict: bool = True):
    '''
    Check that two .tar.bz2 or .conda files (either of src_file and
    reference_file can be either format) match exactly, down to the timestamps
    etc.

    Does not check outside of the info- and pkg- components of a .conda.
    (conda\'s metadata.json, which gives the version "2" of the format)

    If strict = True, also check for matching uid, gid, mtime, uname, gname.
    '''
