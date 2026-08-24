from ._log import log as log
from .errors import DistutilsInternalError as DistutilsInternalError, DistutilsTemplateError as DistutilsTemplateError
from .util import convert_path as convert_path
from _typeshed import Incomplete

class FileList:
    """A list of files built by on exploring the filesystem and filtered by
    applying various patterns to what we find there.

    Instance attributes:
      dir
        directory from which files will be taken -- only used if
        'allfiles' not supplied to constructor
      files
        list of filenames currently being built/filtered/manipulated
      allfiles
        complete list of files under consideration (ie. without any
        filtering applied)
    """
    allfiles: Incomplete
    files: Incomplete
    def __init__(self, warn: Incomplete | None = None, debug_print: Incomplete | None = None) -> None: ...
    def set_allfiles(self, allfiles) -> None: ...
    def findall(self, dir=...) -> None: ...
    def debug_print(self, msg) -> None:
        """Print 'msg' to stdout if the global DEBUG (taken from the
        DISTUTILS_DEBUG environment variable) flag is true.
        """
    def append(self, item) -> None: ...
    def extend(self, items) -> None: ...
    def sort(self) -> None: ...
    def remove_duplicates(self) -> None: ...
    def process_template_line(self, line) -> None: ...
    def include_pattern(self, pattern, anchor: int = 1, prefix: Incomplete | None = None, is_regex: int = 0):
        '''Select strings (presumably filenames) from \'self.files\' that
        match \'pattern\', a Unix-style wildcard (glob) pattern.  Patterns
        are not quite the same as implemented by the \'fnmatch\' module: \'*\'
        and \'?\'  match non-special characters, where "special" is platform-
        dependent: slash on Unix; colon, slash, and backslash on
        DOS/Windows; and colon on Mac OS.

        If \'anchor\' is true (the default), then the pattern match is more
        stringent: "*.py" will match "foo.py" but not "foo/bar.py".  If
        \'anchor\' is false, both of these will match.

        If \'prefix\' is supplied, then only filenames starting with \'prefix\'
        (itself a pattern) and ending with \'pattern\', with anything in between
        them, will match.  \'anchor\' is ignored in this case.

        If \'is_regex\' is true, \'anchor\' and \'prefix\' are ignored, and
        \'pattern\' is assumed to be either a string containing a regex or a
        regex object -- no translation is done, the regex is just compiled
        and used as-is.

        Selected strings will be added to self.files.

        Return True if files are found, False otherwise.
        '''
    def exclude_pattern(self, pattern, anchor: int = 1, prefix: Incomplete | None = None, is_regex: int = 0):
        """Remove strings (presumably filenames) from 'files' that match
        'pattern'.  Other parameters are the same as for
        'include_pattern()', above.
        The list 'self.files' is modified in place.
        Return True if files are found, False otherwise.
        """

class _UniqueDirs(set):
    """
    Exclude previously-seen dirs from walk results,
    avoiding infinite recursion.
    Ref https://bugs.python.org/issue44497.
    """
    def __call__(self, walk_item):
        """
        Given an item from an os.walk result, determine
        if the item represents a unique dir for this instance
        and if not, prevent further traversal.
        """
    @classmethod
    def filter(cls, items): ...

def findall(dir=...):
    """
    Find all files under 'dir' and return the list of full filenames.
    Unless dir is '.', return full filenames with dir prepended.
    """
def glob_to_re(pattern):
    '''Translate a shell-like glob pattern to a regular expression; return
    a string containing the regex.  Differs from \'fnmatch.translate()\' in
    that \'*\' does not match "special characters" (which are
    platform-specific).
    '''
def translate_pattern(pattern, anchor: int = 1, prefix: Incomplete | None = None, is_regex: int = 0):
    """Translate a shell-like wildcard pattern to a compiled regular
    expression.  Return the compiled regex.  If 'is_regex' true,
    then 'pattern' is directly compiled to a regex (if it's a string)
    or just returned as-is (assumes it's a regex object).
    """
