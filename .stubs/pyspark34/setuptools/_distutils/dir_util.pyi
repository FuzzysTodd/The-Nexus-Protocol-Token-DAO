from ._log import log as log
from .errors import DistutilsFileError as DistutilsFileError, DistutilsInternalError as DistutilsInternalError

def mkpath(name, mode: int = 511, verbose: int = 1, dry_run: int = 0):
    """Create a directory and any missing ancestor directories.

    If the directory already exists (or if 'name' is the empty string, which
    means the current directory, which of course exists), then do nothing.
    Raise DistutilsFileError if unable to create some directory along the way
    (eg. some sub-path exists, but is a file rather than a directory).
    If 'verbose' is true, print a one-line summary of each mkdir to stdout.
    Return the list of directories actually created.

    os.makedirs is not used because:

    a) It's new to Python 1.5.2, and
    b) it blows up if the directory already exists (in which case it should
       silently succeed).
    """
def create_tree(base_dir, files, mode: int = 511, verbose: int = 1, dry_run: int = 0) -> None:
    """Create all the empty directories under 'base_dir' needed to put 'files'
    there.

    'base_dir' is just the name of a directory which doesn't necessarily
    exist yet; 'files' is a list of filenames to be interpreted relative to
    'base_dir'.  'base_dir' + the directory portion of every file in 'files'
    will be created if it doesn't already exist.  'mode', 'verbose' and
    'dry_run' flags are as for 'mkpath()'.
    """
def copy_tree(src, dst, preserve_mode: int = 1, preserve_times: int = 1, preserve_symlinks: int = 0, update: int = 0, verbose: int = 1, dry_run: int = 0):
    """Copy an entire directory tree 'src' to a new location 'dst'.

    Both 'src' and 'dst' must be directory names.  If 'src' is not a
    directory, raise DistutilsFileError.  If 'dst' does not exist, it is
    created with 'mkpath()'.  The end result of the copy is that every
    file in 'src' is copied to 'dst', and directories under 'src' are
    recursively copied to 'dst'.  Return the list of files that were
    copied or might have been copied, using their output name.  The
    return value is unaffected by 'update' or 'dry_run': it is simply
    the list of all files under 'src', with the names changed to be
    under 'dst'.

    'preserve_mode' and 'preserve_times' are the same as for
    'copy_file'; note that they only apply to regular files, not to
    directories.  If 'preserve_symlinks' is true, symlinks will be
    copied as symlinks (on platforms that support them!); otherwise
    (the default), the destination of the symlink will be copied.
    'update' and 'verbose' are the same as for 'copy_file'.
    """
def remove_tree(directory, verbose: int = 1, dry_run: int = 0) -> None:
    """Recursively remove an entire directory tree.

    Any errors are ignored (apart from being reported to stdout if 'verbose'
    is true).
    """
def ensure_relative(path):
    """Take the full path 'path', and make it a relative path.

    This is useful to make 'path' the second argument to os.path.join().
    """
