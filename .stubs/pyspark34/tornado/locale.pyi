import datetime
import gettext
from _typeshed import Incomplete
from tornado import escape as escape
from tornado._locale_data import LOCALE_NAMES as LOCALE_NAMES
from tornado.log import gen_log as gen_log
from typing import Any, Dict, Iterable

CONTEXT_SEPARATOR: str

def get(*locale_codes: str) -> Locale:
    '''Returns the closest match for the given locale codes.

    We iterate over all given locale codes in order. If we have a tight
    or a loose match for the code (e.g., "en" for "en_US"), we return
    the locale. Otherwise we move to the next code in the list.

    By default we return ``en_US`` if no translations are found for any of
    the specified locales. You can change the default locale with
    `set_default_locale()`.
    '''
def set_default_locale(code: str) -> None:
    """Sets the default locale.

    The default locale is assumed to be the language used for all strings
    in the system. The translations loaded from disk are mappings from
    the default locale to the destination locale. Consequently, you don't
    need to create a translation file for the default locale.
    """
def load_translations(directory: str, encoding: str | None = None) -> None:
    '''Loads translations from CSV files in a directory.

    Translations are strings with optional Python-style named placeholders
    (e.g., ``My name is %(name)s``) and their associated translations.

    The directory should have translation files of the form ``LOCALE.csv``,
    e.g. ``es_GT.csv``. The CSV files should have two or three columns: string,
    translation, and an optional plural indicator. Plural indicators should
    be one of "plural" or "singular". A given string can have both singular
    and plural forms. For example ``%(name)s liked this`` may have a
    different verb conjugation depending on whether %(name)s is one
    name or a list of names. There should be two rows in the CSV file for
    that string, one with plural indicator "singular", and one "plural".
    For strings with no verbs that would change on translation, simply
    use "unknown" or the empty string (or don\'t include the column at all).

    The file is read using the `csv` module in the default "excel" dialect.
    In this format there should not be spaces after the commas.

    If no ``encoding`` parameter is given, the encoding will be
    detected automatically (among UTF-8 and UTF-16) if the file
    contains a byte-order marker (BOM), defaulting to UTF-8 if no BOM
    is present.

    Example translation ``es_LA.csv``::

        "I love you","Te amo"
        "%(name)s liked this","A %(name)s les gustó esto","plural"
        "%(name)s liked this","A %(name)s le gustó esto","singular"

    .. versionchanged:: 4.3
       Added ``encoding`` parameter. Added support for BOM-based encoding
       detection, UTF-16, and UTF-8-with-BOM.
    '''
def load_gettext_translations(directory: str, domain: str) -> None:
    """Loads translations from `gettext`'s locale tree

    Locale tree is similar to system's ``/usr/share/locale``, like::

        {directory}/{lang}/LC_MESSAGES/{domain}.mo

    Three steps are required to have your app translated:

    1. Generate POT translation file::

        xgettext --language=Python --keyword=_:1,2 -d mydomain file1.py file2.html etc

    2. Merge against existing POT file::

        msgmerge old.po mydomain.po > new.po

    3. Compile::

        msgfmt mydomain.po -o {directory}/pt_BR/LC_MESSAGES/mydomain.mo
    """
def get_supported_locales() -> Iterable[str]:
    """Returns a list of all the supported locale codes."""

class Locale:
    """Object representing a locale.

    After calling one of `load_translations` or `load_gettext_translations`,
    call `get` or `get_closest` to get a Locale object.
    """
    @classmethod
    def get_closest(cls, *locale_codes: str) -> Locale:
        """Returns the closest match for the given locale code."""
    @classmethod
    def get(cls, code: str) -> Locale:
        """Returns the Locale for the given locale code.

        If it is not supported, we raise an exception.
        """
    code: Incomplete
    name: Incomplete
    rtl: bool
    def __init__(self, code: str) -> None: ...
    def translate(self, message: str, plural_message: str | None = None, count: int | None = None) -> str:
        """Returns the translation for the given message for this locale.

        If ``plural_message`` is given, you must also provide
        ``count``. We return ``plural_message`` when ``count != 1``,
        and we return the singular form for the given message when
        ``count == 1``.
        """
    def pgettext(self, context: str, message: str, plural_message: str | None = None, count: int | None = None) -> str: ...
    def format_date(self, date: int | float | datetime.datetime, gmt_offset: int = 0, relative: bool = True, shorter: bool = False, full_format: bool = False) -> str:
        '''Formats the given date (which should be GMT).

        By default, we return a relative time (e.g., "2 minutes ago"). You
        can return an absolute date string with ``relative=False``.

        You can force a full format date ("July 10, 1980") with
        ``full_format=True``.

        This method is primarily intended for dates in the past.
        For dates in the future, we fall back to full format.
        '''
    def format_day(self, date: datetime.datetime, gmt_offset: int = 0, dow: bool = True) -> bool:
        '''Formats the given date as a day of week.

        Example: "Monday, January 22". You can remove the day of week with
        ``dow=False``.
        '''
    def list(self, parts: Any) -> str:
        '''Returns a comma-separated list for the given list of parts.

        The format is, e.g., "A, B and C", "A and B" or just "A" for lists
        of size 1.
        '''
    def friendly_number(self, value: int) -> str:
        """Returns a comma-separated number for the given integer."""

class CSVLocale(Locale):
    """Locale implementation using tornado's CSV translation format."""
    translations: Incomplete
    def __init__(self, code: str, translations: Dict[str, Dict[str, str]]) -> None: ...
    def translate(self, message: str, plural_message: str | None = None, count: int | None = None) -> str: ...
    def pgettext(self, context: str, message: str, plural_message: str | None = None, count: int | None = None) -> str: ...

class GettextLocale(Locale):
    """Locale implementation using the `gettext` module."""
    ngettext: Incomplete
    gettext: Incomplete
    def __init__(self, code: str, translations: gettext.NullTranslations) -> None: ...
    def translate(self, message: str, plural_message: str | None = None, count: int | None = None) -> str: ...
    def pgettext(self, context: str, message: str, plural_message: str | None = None, count: int | None = None) -> str:
        '''Allows to set context for translation, accepts plural forms.

        Usage example::

            pgettext("law", "right")
            pgettext("good", "right")

        Plural message example::

            pgettext("organization", "club", "clubs", len(clubs))
            pgettext("stick", "club", "clubs", len(clubs))

        To generate POT file with context, add following options to step 1
        of `load_gettext_translations` sequence::

            xgettext [basic options] --keyword=pgettext:1c,2 --keyword=pgettext:1c,2,3

        .. versionadded:: 4.2
        '''
