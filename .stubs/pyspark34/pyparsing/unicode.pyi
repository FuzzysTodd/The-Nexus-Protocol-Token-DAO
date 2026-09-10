from _typeshed import Incomplete
from typing import List, Tuple

class _lazyclassproperty:
    fn: Incomplete
    __doc__: Incomplete
    def __init__(self, fn) -> None: ...
    def __get__(self, obj, cls): ...
UnicodeRangeList = List[Tuple[int, int] | Tuple[int]]

class unicode_set:
    """
    A set of Unicode characters, for language-specific strings for
    ``alphas``, ``nums``, ``alphanums``, and ``printables``.
    A unicode_set is defined by a list of ranges in the Unicode character
    set, in a class attribute ``_ranges``. Ranges can be specified using
    2-tuples or a 1-tuple, such as::

        _ranges = [
            (0x0020, 0x007e),
            (0x00a0, 0x00ff),
            (0x0100,),
            ]

    Ranges are left- and right-inclusive. A 1-tuple of (x,) is treated as (x, x).

    A unicode set can also be defined using multiple inheritance of other unicode sets::

        class CJK(Chinese, Japanese, Korean):
            pass
    """
    def printables(cls):
        """all non-whitespace characters in this range"""
    def alphas(cls):
        """all alphabetic characters in this range"""
    def nums(cls):
        """all numeric digit characters in this range"""
    def alphanums(cls):
        """all alphanumeric characters in this range"""
    def identchars(cls):
        """all characters in this range that are valid identifier characters, plus underscore '_'"""
    def identbodychars(cls):
        """
        all characters in this range that are valid identifier body characters,
        plus the digits 0-9
        """

class pyparsing_unicode(unicode_set):
    """
    A namespace class for defining common language unicode_sets.
    """
    class BasicMultilingualPlane(unicode_set):
        """Unicode set for the Basic Multilingual Plane"""
    class Latin1(unicode_set):
        """Unicode set for Latin-1 Unicode Character Range"""
    class LatinA(unicode_set):
        """Unicode set for Latin-A Unicode Character Range"""
    class LatinB(unicode_set):
        """Unicode set for Latin-B Unicode Character Range"""
    class Greek(unicode_set):
        """Unicode set for Greek Unicode Character Ranges"""
    class Cyrillic(unicode_set):
        """Unicode set for Cyrillic Unicode Character Range"""
    class Chinese(unicode_set):
        """Unicode set for Chinese Unicode Character Range"""
    class Japanese(unicode_set):
        """Unicode set for Japanese Unicode Character Range, combining Kanji, Hiragana, and Katakana ranges"""
        class Kanji(unicode_set):
            """Unicode set for Kanji Unicode Character Range"""
        class Hiragana(unicode_set):
            """Unicode set for Hiragana Unicode Character Range"""
        class Katakana(unicode_set):
            """Unicode set for Katakana  Unicode Character Range"""
    class Hangul(unicode_set):
        """Unicode set for Hangul (Korean) Unicode Character Range"""
    Korean = Hangul
    class CJK(Chinese, Japanese, Hangul):
        """Unicode set for combined Chinese, Japanese, and Korean (CJK) Unicode Character Range"""
    class Thai(unicode_set):
        """Unicode set for Thai Unicode Character Range"""
    class Arabic(unicode_set):
        """Unicode set for Arabic Unicode Character Range"""
    class Hebrew(unicode_set):
        """Unicode set for Hebrew Unicode Character Range"""
    class Devanagari(unicode_set):
        """Unicode set for Devanagari Unicode Character Range"""
