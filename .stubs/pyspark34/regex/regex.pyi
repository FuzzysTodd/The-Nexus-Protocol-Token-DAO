from regex._regex_core import *
from _typeshed import Incomplete

__all__ = ['cache_all', 'compile', 'DEFAULT_VERSION', 'escape', 'findall', 'finditer', 'fullmatch', 'match', 'purge', 'search', 'split', 'splititer', 'sub', 'subf', 'subfn', 'subn', 'template', 'Scanner', 'A', 'ASCII', 'B', 'BESTMATCH', 'D', 'DEBUG', 'E', 'ENHANCEMATCH', 'S', 'DOTALL', 'F', 'FULLCASE', 'I', 'IGNORECASE', 'L', 'LOCALE', 'M', 'MULTILINE', 'P', 'POSIX', 'R', 'REVERSE', 'T', 'TEMPLATE', 'U', 'UNICODE', 'V0', 'VERSION0', 'V1', 'VERSION1', 'X', 'VERBOSE', 'W', 'WORD', 'error', 'Regex', '__version__', '__doc__', 'RegexFlag', 'Pattern', 'Match']

__version__: str

def match(pattern, string, flags: int = 0, pos: Incomplete | None = None, endpos: Incomplete | None = None, partial: bool = False, concurrent: Incomplete | None = None, timeout: Incomplete | None = None, ignore_unused: bool = False, **kwargs):
    """Try to apply the pattern at the start of the string, returning a match
    object, or None if no match was found."""
def fullmatch(pattern, string, flags: int = 0, pos: Incomplete | None = None, endpos: Incomplete | None = None, partial: bool = False, concurrent: Incomplete | None = None, timeout: Incomplete | None = None, ignore_unused: bool = False, **kwargs):
    """Try to apply the pattern against all of the string, returning a match
    object, or None if no match was found."""
def search(pattern, string, flags: int = 0, pos: Incomplete | None = None, endpos: Incomplete | None = None, partial: bool = False, concurrent: Incomplete | None = None, timeout: Incomplete | None = None, ignore_unused: bool = False, **kwargs):
    """Search through string looking for a match to the pattern, returning a
    match object, or None if no match was found."""
def sub(pattern, repl, string, count: int = 0, flags: int = 0, pos: Incomplete | None = None, endpos: Incomplete | None = None, concurrent: Incomplete | None = None, timeout: Incomplete | None = None, ignore_unused: bool = False, **kwargs):
    """Return the string obtained by replacing the leftmost (or rightmost with a
    reverse pattern) non-overlapping occurrences of the pattern in string by the
    replacement repl. repl can be either a string or a callable; if a string,
    backslash escapes in it are processed; if a callable, it's passed the match
    object and must return a replacement string to be used."""
def subf(pattern, format, string, count: int = 0, flags: int = 0, pos: Incomplete | None = None, endpos: Incomplete | None = None, concurrent: Incomplete | None = None, timeout: Incomplete | None = None, ignore_unused: bool = False, **kwargs):
    """Return the string obtained by replacing the leftmost (or rightmost with a
    reverse pattern) non-overlapping occurrences of the pattern in string by the
    replacement format. format can be either a string or a callable; if a string,
    it's treated as a format string; if a callable, it's passed the match object
    and must return a replacement string to be used."""
def subn(pattern, repl, string, count: int = 0, flags: int = 0, pos: Incomplete | None = None, endpos: Incomplete | None = None, concurrent: Incomplete | None = None, timeout: Incomplete | None = None, ignore_unused: bool = False, **kwargs):
    """Return a 2-tuple containing (new_string, number). new_string is the string
    obtained by replacing the leftmost (or rightmost with a reverse pattern)
    non-overlapping occurrences of the pattern in the source string by the
    replacement repl. number is the number of substitutions that were made. repl
    can be either a string or a callable; if a string, backslash escapes in it
    are processed; if a callable, it's passed the match object and must return a
    replacement string to be used."""
def subfn(pattern, format, string, count: int = 0, flags: int = 0, pos: Incomplete | None = None, endpos: Incomplete | None = None, concurrent: Incomplete | None = None, timeout: Incomplete | None = None, ignore_unused: bool = False, **kwargs):
    """Return a 2-tuple containing (new_string, number). new_string is the string
    obtained by replacing the leftmost (or rightmost with a reverse pattern)
    non-overlapping occurrences of the pattern in the source string by the
    replacement format. number is the number of substitutions that were made. format
    can be either a string or a callable; if a string, it's treated as a format
    string; if a callable, it's passed the match object and must return a
    replacement string to be used."""
def split(pattern, string, maxsplit: int = 0, flags: int = 0, concurrent: Incomplete | None = None, timeout: Incomplete | None = None, ignore_unused: bool = False, **kwargs):
    """Split the source string by the occurrences of the pattern, returning a
    list containing the resulting substrings.  If capturing parentheses are used
    in pattern, then the text of all groups in the pattern are also returned as
    part of the resulting list.  If maxsplit is nonzero, at most maxsplit splits
    occur, and the remainder of the string is returned as the final element of
    the list."""
def splititer(pattern, string, maxsplit: int = 0, flags: int = 0, concurrent: Incomplete | None = None, timeout: Incomplete | None = None, ignore_unused: bool = False, **kwargs):
    """Return an iterator yielding the parts of a split string."""
def findall(pattern, string, flags: int = 0, pos: Incomplete | None = None, endpos: Incomplete | None = None, overlapped: bool = False, concurrent: Incomplete | None = None, timeout: Incomplete | None = None, ignore_unused: bool = False, **kwargs):
    """Return a list of all matches in the string. The matches may be overlapped
    if overlapped is True. If one or more groups are present in the pattern,
    return a list of groups; this will be a list of tuples if the pattern has
    more than one group. Empty matches are included in the result."""
def finditer(pattern, string, flags: int = 0, pos: Incomplete | None = None, endpos: Incomplete | None = None, overlapped: bool = False, partial: bool = False, concurrent: Incomplete | None = None, timeout: Incomplete | None = None, ignore_unused: bool = False, **kwargs):
    """Return an iterator over all matches in the string. The matches may be
    overlapped if overlapped is True. For each match, the iterator returns a
    match object. Empty matches are included in the result."""
def compile(pattern, flags: int = 0, ignore_unused: bool = False, cache_pattern: Incomplete | None = None, **kwargs):
    """Compile a regular expression pattern, returning a pattern object."""
def purge() -> None:
    """Clear the regular expression cache"""
def cache_all(value: bool = True):
    """Sets whether to cache all patterns, even those are compiled explicitly.
    Passing None has no effect, but returns the current setting."""
def template(pattern, flags: int = 0):
    """Compile a template pattern, returning a pattern object."""
def escape(pattern, special_only: bool = True, literal_spaces: bool = False):
    """Escape a string for use as a literal in a pattern. If special_only is
    True, escape only special characters, else escape all non-alphanumeric
    characters. If literal_spaces is True, don't escape spaces."""
DEFAULT_VERSION = VERSION0
Pattern: Incomplete
Match: Incomplete
Regex = compile

# Names in __all__ with no definition:
#   A
#   ASCII
#   B
#   BESTMATCH
#   D
#   DEBUG
#   DOTALL
#   E
#   ENHANCEMATCH
#   F
#   FULLCASE
#   I
#   IGNORECASE
#   L
#   LOCALE
#   M
#   MULTILINE
#   P
#   POSIX
#   R
#   REVERSE
#   RegexFlag
#   S
#   Scanner
#   T
#   TEMPLATE
#   U
#   UNICODE
#   V0
#   V1
#   VERBOSE
#   VERSION0
#   VERSION1
#   W
#   WORD
#   X
#   __doc__
#   error
