from .table_wide import WIDE_EASTASIAN as WIDE_EASTASIAN
from .table_zero import ZERO_WIDTH as ZERO_WIDTH
from .unicode_versions import list_versions as list_versions
from _typeshed import Incomplete

ZERO_WIDTH_CF: Incomplete

def wcwidth(wc, unicode_version: str = 'auto'):
    """
    Given one Unicode character, return its printable length on a terminal.

    :param str wc: A single Unicode character.
    :param str unicode_version: A Unicode version number, such as
        ``'6.0.0'``, the list of available version levels may be
        listed by pairing function :func:`list_versions`.

        Any version string may be specified without error -- the nearest
        matching version is selected.  When ``latest`` (default), the
        highest Unicode version level is used.
    :return: The width, in cells, necessary to display the character of
        Unicode string character, ``wc``.  Returns 0 if the ``wc`` argument has
        no printable effect on a terminal (such as NUL '\\0'), -1 if ``wc`` is
        not printable, or has an indeterminate effect on the terminal, such as
        a control character.  Otherwise, the number of column positions the
        character occupies on a graphic terminal (1 or 2) is returned.
    :rtype: int

    The following have a column width of -1:

        - C0 control characters (U+001 through U+01F).

        - C1 control characters and DEL (U+07F through U+0A0).

    The following have a column width of 0:

    - Non-spacing and enclosing combining characters (general
      category code Mn or Me in the Unicode database).

    - NULL (``U+0000``).

    - COMBINING GRAPHEME JOINER (``U+034F``).

    - ZERO WIDTH SPACE (``U+200B``) *through*
      RIGHT-TO-LEFT MARK (``U+200F``).

    - LINE SEPARATOR (``U+2028``) *and*
      PARAGRAPH SEPARATOR (``U+2029``).

    - LEFT-TO-RIGHT EMBEDDING (``U+202A``) *through*
      RIGHT-TO-LEFT OVERRIDE (``U+202E``).

    - WORD JOINER (``U+2060``) *through*
      INVISIBLE SEPARATOR (``U+2063``).

    The following have a column width of 1:

    - SOFT HYPHEN (``U+00AD``).

    - All remaining characters, including all printable ISO 8859-1
      and WGL4 characters, Unicode control characters, etc.

    The following have a column width of 2:

        - Spacing characters in the East Asian Wide (W) or East Asian
          Full-width (F) category as defined in Unicode Technical
          Report #11 have a column width of 2.

         - Some kinds of Emoji or symbols.
    """
def wcswidth(pwcs, n: Incomplete | None = None, unicode_version: str = 'auto'):
    """
    Given a unicode string, return its printable length on a terminal.

    :param str pwcs: Measure width of given unicode string.
    :param int n: When ``n`` is None (default), return the length of the
        entire string, otherwise width the first ``n`` characters specified.
    :param str unicode_version: An explicit definition of the unicode version
        level to use for determination, may be ``auto`` (default), which uses
        the Environment Variable, ``UNICODE_VERSION`` if defined, or the latest
        available unicode version, otherwise.
    :rtype: int
    :returns: The width, in cells, necessary to display the first ``n``
        characters of the unicode string ``pwcs``.  Returns ``-1`` if
        a non-printable character is encountered.
    """
