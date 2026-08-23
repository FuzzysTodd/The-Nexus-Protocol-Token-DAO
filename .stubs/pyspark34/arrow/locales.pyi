from _typeshed import Incomplete
from typing import Any, ClassVar, Dict, List, Mapping, Sequence, Tuple

TimeFrameLiteral: Incomplete

def get_locale(name: str) -> Locale:
    """Returns an appropriate :class:`Locale <arrow.locales.Locale>`
    corresponding to an input locale name.

    :param name: the name of the locale.

    """
def get_locale_by_class_name(name: str) -> Locale:
    """Returns an appropriate :class:`Locale <arrow.locales.Locale>`
    corresponding to an locale class name.

    :param name: the name of the locale class.

    """

class Locale:
    """Represents locale-specific data and functionality."""
    names: ClassVar[List[str]]
    timeframes: ClassVar[Mapping[TimeFrameLiteral, _TimeFrameElements]]
    meridians: ClassVar[Dict[str, str]]
    past: ClassVar[str]
    future: ClassVar[str]
    and_word: ClassVar[str | None]
    month_names: ClassVar[List[str]]
    month_abbreviations: ClassVar[List[str]]
    day_names: ClassVar[List[str]]
    day_abbreviations: ClassVar[List[str]]
    ordinal_day_re: ClassVar[str]
    def __init_subclass__(cls, **kwargs: Any) -> None: ...
    def __init__(self) -> None: ...
    def describe(self, timeframe: TimeFrameLiteral, delta: float | int = 0, only_distance: bool = False) -> str:
        '''Describes a delta within a timeframe in plain language.

        :param timeframe: a string representing a timeframe.
        :param delta: a quantity representing a delta in a timeframe.
        :param only_distance: return only distance eg: "11 seconds" without "in" or "ago" keywords
        '''
    def describe_multi(self, timeframes: Sequence[Tuple[TimeFrameLiteral, int | float]], only_distance: bool = False) -> str:
        '''Describes a delta within multiple timeframes in plain language.

        :param timeframes: a list of string, quantity pairs each representing a timeframe and delta.
        :param only_distance: return only distance eg: "2 hours and 11 seconds" without "in" or "ago" keywords
        '''
    def day_name(self, day: int) -> str:
        """Returns the day name for a specified day of the week.

        :param day: the ``int`` day of the week (1-7).

        """
    def day_abbreviation(self, day: int) -> str:
        """Returns the day abbreviation for a specified day of the week.

        :param day: the ``int`` day of the week (1-7).

        """
    def month_name(self, month: int) -> str:
        """Returns the month name for a specified month of the year.

        :param month: the ``int`` month of the year (1-12).

        """
    def month_abbreviation(self, month: int) -> str:
        """Returns the month abbreviation for a specified month of the year.

        :param month: the ``int`` month of the year (1-12).

        """
    def month_number(self, name: str) -> int | None:
        """Returns the month number for a month specified by name or abbreviation.

        :param name: the month name or abbreviation.

        """
    def year_full(self, year: int) -> str:
        """Returns the year for specific locale if available

        :param year: the ``int`` year (4-digit)
        """
    def year_abbreviation(self, year: int) -> str:
        """Returns the year for specific locale if available

        :param year: the ``int`` year (4-digit)
        """
    def meridian(self, hour: int, token: Any) -> str | None:
        """Returns the meridian indicator for a specified hour and format token.

        :param hour: the ``int`` hour of the day.
        :param token: the format token.
        """
    def ordinal_number(self, n: int) -> str:
        """Returns the ordinal format of a given integer

        :param n: an integer
        """

class EnglishLocale(Locale):
    names: Incomplete
    past: str
    future: str
    and_word: str
    timeframes: Incomplete
    meridians: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete
    ordinal_day_re: str
    def describe(self, timeframe: TimeFrameLiteral, delta: int | float = 0, only_distance: bool = False) -> str:
        '''Describes a delta within a timeframe in plain language.

        :param timeframe: a string representing a timeframe.
        :param delta: a quantity representing a delta in a timeframe.
        :param only_distance: return only distance eg: "11 seconds" without "in" or "ago" keywords
        '''

class ItalianLocale(Locale):
    names: Incomplete
    past: str
    future: str
    and_word: str
    timeframes: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete
    ordinal_day_re: str

class SpanishLocale(Locale):
    names: Incomplete
    past: str
    future: str
    and_word: str
    timeframes: Incomplete
    meridians: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete
    ordinal_day_re: str

class FrenchBaseLocale(Locale):
    past: str
    future: str
    and_word: str
    timeframes: Incomplete
    month_names: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete
    ordinal_day_re: str

class FrenchLocale(FrenchBaseLocale, Locale):
    names: Incomplete
    month_abbreviations: Incomplete

class FrenchCanadianLocale(FrenchBaseLocale, Locale):
    names: Incomplete
    month_abbreviations: Incomplete

class GreekLocale(Locale):
    names: Incomplete
    past: str
    future: str
    and_word: str
    timeframes: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class JapaneseLocale(Locale):
    names: Incomplete
    past: str
    future: str
    and_word: str
    timeframes: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class SwedishLocale(Locale):
    names: Incomplete
    past: str
    future: str
    and_word: str
    timeframes: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class FinnishLocale(Locale):
    names: Incomplete
    past: str
    future: str
    timeframes: ClassVar[Mapping[TimeFrameLiteral, str | Mapping[str, str]]]
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class ChineseCNLocale(Locale):
    names: Incomplete
    past: str
    future: str
    timeframes: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class ChineseTWLocale(Locale):
    names: Incomplete
    past: str
    future: str
    and_word: str
    timeframes: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class HongKongLocale(Locale):
    names: Incomplete
    past: str
    future: str
    timeframes: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class KoreanLocale(Locale):
    names: Incomplete
    past: str
    future: str
    timeframes: Incomplete
    special_dayframes: Incomplete
    special_yearframes: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class DutchLocale(Locale):
    names: Incomplete
    past: str
    future: str
    timeframes: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class SlavicBaseLocale(Locale):
    timeframes: ClassVar[Mapping[TimeFrameLiteral, str | Mapping[str, str]]]

class BelarusianLocale(SlavicBaseLocale):
    names: Incomplete
    past: str
    future: str
    timeframes: ClassVar[Mapping[TimeFrameLiteral, str | Mapping[str, str]]]
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class PolishLocale(SlavicBaseLocale):
    names: Incomplete
    past: str
    future: str
    timeframes: ClassVar[Mapping[TimeFrameLiteral, str | Mapping[str, str]]]
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class RussianLocale(SlavicBaseLocale):
    names: Incomplete
    past: str
    future: str
    timeframes: ClassVar[Mapping[TimeFrameLiteral, str | Mapping[str, str]]]
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class AfrikaansLocale(Locale):
    names: Incomplete
    past: str
    future: str
    timeframes: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class BulgarianLocale(SlavicBaseLocale):
    names: Incomplete
    past: str
    future: str
    timeframes: ClassVar[Mapping[TimeFrameLiteral, str | Mapping[str, str]]]
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class UkrainianLocale(SlavicBaseLocale):
    names: Incomplete
    past: str
    future: str
    timeframes: ClassVar[Mapping[TimeFrameLiteral, str | Mapping[str, str]]]
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class MacedonianLocale(SlavicBaseLocale):
    names: Incomplete
    past: str
    future: str
    timeframes: ClassVar[Mapping[TimeFrameLiteral, str | Mapping[str, str]]]
    meridians: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class GermanBaseLocale(Locale):
    past: str
    future: str
    and_word: str
    timeframes: ClassVar[Dict[TimeFrameLiteral, str]]
    timeframes_only_distance: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete
    def describe(self, timeframe: TimeFrameLiteral, delta: int | float = 0, only_distance: bool = False) -> str:
        '''Describes a delta within a timeframe in plain language.

        :param timeframe: a string representing a timeframe.
        :param delta: a quantity representing a delta in a timeframe.
        :param only_distance: return only distance eg: "11 seconds" without "in" or "ago" keywords
        '''

class GermanLocale(GermanBaseLocale, Locale):
    names: Incomplete

class SwissLocale(GermanBaseLocale, Locale):
    names: Incomplete

class AustrianLocale(GermanBaseLocale, Locale):
    names: Incomplete
    month_names: Incomplete

class NorwegianLocale(Locale):
    names: Incomplete
    past: str
    future: str
    timeframes: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class NewNorwegianLocale(Locale):
    names: Incomplete
    past: str
    future: str
    timeframes: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class PortugueseLocale(Locale):
    names: Incomplete
    past: str
    future: str
    and_word: str
    timeframes: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class BrazilianPortugueseLocale(PortugueseLocale):
    names: Incomplete
    past: str

class TagalogLocale(Locale):
    names: Incomplete
    past: str
    future: str
    timeframes: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete
    meridians: Incomplete

class VietnameseLocale(Locale):
    names: Incomplete
    past: str
    future: str
    timeframes: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class TurkishLocale(Locale):
    names: Incomplete
    past: str
    future: str
    and_word: str
    timeframes: Incomplete
    meridians: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class AzerbaijaniLocale(Locale):
    names: Incomplete
    past: str
    future: str
    timeframes: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class ArabicLocale(Locale):
    names: Incomplete
    past: str
    future: str
    timeframes: ClassVar[Mapping[TimeFrameLiteral, str | Mapping[str, str]]]
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class LevantArabicLocale(ArabicLocale):
    names: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete

class AlgeriaTunisiaArabicLocale(ArabicLocale):
    names: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete

class MauritaniaArabicLocale(ArabicLocale):
    names: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete

class MoroccoArabicLocale(ArabicLocale):
    names: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete

class IcelandicLocale(Locale):
    names: Incomplete
    past: str
    future: str
    timeframes: ClassVar[Mapping[TimeFrameLiteral, str | Mapping[str, str]]]
    meridians: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class DanishLocale(Locale):
    names: Incomplete
    past: str
    future: str
    and_word: str
    timeframes: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class MalayalamLocale(Locale):
    names: Incomplete
    past: str
    future: str
    timeframes: Incomplete
    meridians: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class HindiLocale(Locale):
    names: Incomplete
    past: str
    future: str
    timeframes: Incomplete
    meridians: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class CzechLocale(Locale):
    names: Incomplete
    timeframes: ClassVar[Mapping[TimeFrameLiteral, str | Mapping[str, str]]]
    past: str
    future: str
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class SlovakLocale(Locale):
    names: Incomplete
    timeframes: ClassVar[Mapping[TimeFrameLiteral, str | Mapping[str, str]]]
    past: str
    future: str
    and_word: str
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class FarsiLocale(Locale):
    names: Incomplete
    past: str
    future: str
    timeframes: Incomplete
    meridians: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class HebrewLocale(Locale):
    names: Incomplete
    past: str
    future: str
    and_word: str
    timeframes: ClassVar[Mapping[TimeFrameLiteral, str | Mapping[str, str]]]
    meridians: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete
    def describe_multi(self, timeframes: Sequence[Tuple[TimeFrameLiteral, int | float]], only_distance: bool = False) -> str:
        '''Describes a delta within multiple timeframes in plain language.
        In Hebrew, the and word behaves a bit differently.

        :param timeframes: a list of string, quantity pairs each representing a timeframe and delta.
        :param only_distance: return only distance eg: "2 hours and 11 seconds" without "in" or "ago" keywords
        '''

class MarathiLocale(Locale):
    names: Incomplete
    past: str
    future: str
    timeframes: Incomplete
    meridians: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class CatalanLocale(Locale):
    names: Incomplete
    past: str
    future: str
    and_word: str
    timeframes: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class BasqueLocale(Locale):
    names: Incomplete
    past: str
    future: str
    timeframes: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class HungarianLocale(Locale):
    names: Incomplete
    past: str
    future: str
    timeframes: ClassVar[Mapping[TimeFrameLiteral, str | Mapping[str, str]]]
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete
    meridians: Incomplete

class EsperantoLocale(Locale):
    names: Incomplete
    past: str
    future: str
    timeframes: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete
    meridians: Incomplete
    ordinal_day_re: str

class ThaiLocale(Locale):
    names: Incomplete
    past: str
    future: str
    timeframes: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete
    meridians: Incomplete
    BE_OFFSET: int
    def year_full(self, year: int) -> str:
        """Thai always use Buddhist Era (BE) which is CE + 543"""
    def year_abbreviation(self, year: int) -> str:
        """Thai always use Buddhist Era (BE) which is CE + 543"""

class LaotianLocale(Locale):
    names: Incomplete
    past: str
    future: str
    timeframes: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete
    BE_OFFSET: int
    def year_full(self, year: int) -> str:
        """Lao always use Buddhist Era (BE) which is CE + 543"""
    def year_abbreviation(self, year: int) -> str:
        """Lao always use Buddhist Era (BE) which is CE + 543"""

class BengaliLocale(Locale):
    names: Incomplete
    past: str
    future: str
    timeframes: Incomplete
    meridians: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class RomanshLocale(Locale):
    names: Incomplete
    past: str
    future: str
    timeframes: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class RomanianLocale(Locale):
    names: Incomplete
    past: str
    future: str
    and_word: str
    timeframes: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class SlovenianLocale(Locale):
    names: Incomplete
    past: str
    future: str
    and_word: str
    timeframes: Incomplete
    meridians: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class IndonesianLocale(Locale):
    names: Incomplete
    past: str
    future: str
    and_word: str
    timeframes: Incomplete
    meridians: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class NepaliLocale(Locale):
    names: Incomplete
    past: str
    future: str
    timeframes: Incomplete
    meridians: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class EstonianLocale(Locale):
    names: Incomplete
    past: str
    future: str
    and_word: str
    timeframes: ClassVar[Mapping[TimeFrameLiteral, Mapping[str, str]]]
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class LatvianLocale(Locale):
    names: Incomplete
    past: str
    future: str
    and_word: str
    timeframes: ClassVar[Mapping[TimeFrameLiteral, str | Mapping[str, str]]]
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class SwahiliLocale(Locale):
    names: Incomplete
    past: str
    future: str
    and_word: str
    timeframes: Incomplete
    meridians: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class CroatianLocale(Locale):
    names: Incomplete
    past: str
    future: str
    and_word: str
    timeframes: ClassVar[Mapping[TimeFrameLiteral, str | Mapping[str, str]]]
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class LatinLocale(Locale):
    names: Incomplete
    past: str
    future: str
    and_word: str
    timeframes: ClassVar[Mapping[TimeFrameLiteral, str | Mapping[str, str]]]
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class LithuanianLocale(Locale):
    names: Incomplete
    past: str
    future: str
    and_word: str
    timeframes: ClassVar[Mapping[TimeFrameLiteral, str | Mapping[str, str]]]
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class MalayLocale(Locale):
    names: Incomplete
    past: str
    future: str
    and_word: str
    timeframes: ClassVar[Mapping[TimeFrameLiteral, str | Mapping[str, str]]]
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class MalteseLocale(Locale):
    names: Incomplete
    past: str
    future: str
    and_word: str
    timeframes: ClassVar[Mapping[TimeFrameLiteral, str | Mapping[str, str]]]
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class SamiLocale(Locale):
    names: Incomplete
    past: str
    future: str
    timeframes: ClassVar[Mapping[TimeFrameLiteral, str | Mapping[str, str]]]
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class OdiaLocale(Locale):
    names: Incomplete
    past: str
    future: str
    timeframes: Incomplete
    meridians: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class SerbianLocale(Locale):
    names: Incomplete
    past: str
    future: str
    and_word: str
    timeframes: ClassVar[Mapping[TimeFrameLiteral, str | Mapping[str, str]]]
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class LuxembourgishLocale(Locale):
    names: Incomplete
    past: str
    future: str
    and_word: str
    timeframes: ClassVar[Dict[TimeFrameLiteral, str]]
    timeframes_only_distance: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete
    def describe(self, timeframe: TimeFrameLiteral, delta: int | float = 0, only_distance: bool = False) -> str: ...

class ZuluLocale(Locale):
    names: Incomplete
    past: str
    future: str
    and_word: str
    timeframes: ClassVar[Mapping[TimeFrameLiteral, Mapping[str, str] | str]]
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class TamilLocale(Locale):
    names: Incomplete
    past: str
    future: str
    timeframes: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class AlbanianLocale(Locale):
    names: Incomplete
    past: str
    future: str
    and_word: str
    timeframes: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class GeorgianLocale(Locale):
    names: Incomplete
    past: str
    future: str
    and_word: str
    timeframes: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class SinhalaLocale(Locale):
    names: Incomplete
    past: str
    future: str
    and_word: str
    timeframes: ClassVar[Mapping[TimeFrameLiteral, Mapping[str, str] | str]]
    timeframes_only_distance: Incomplete
    def describe(self, timeframe: TimeFrameLiteral, delta: float | int = 1, only_distance: bool = False) -> str:
        '''Describes a delta within a timeframe in plain language.

        :param timeframe: a string representing a timeframe.
        :param delta: a quantity representing a delta in a timeframe.
        :param only_distance: return only distance eg: "11 seconds" without "in" or "ago" keywords
        '''
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class UrduLocale(Locale):
    names: Incomplete
    past: str
    future: str
    and_word: str
    timeframes: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class KazakhLocale(Locale):
    names: Incomplete
    past: str
    future: str
    timeframes: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class AmharicLocale(Locale):
    names: Incomplete
    past: str
    future: str
    and_word: str
    timeframes: ClassVar[Mapping[TimeFrameLiteral, Mapping[str, str] | str]]
    timeframes_only_distance: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete
    def describe(self, timeframe: TimeFrameLiteral, delta: float | int = 1, only_distance: bool = False) -> str:
        '''Describes a delta within a timeframe in plain language.

        :param timeframe: a string representing a timeframe.
        :param delta: a quantity representing a delta in a timeframe.
        :param only_distance: return only distance eg: "11 seconds" without "in" or "ago" keywords
        '''

class ArmenianLocale(Locale):
    names: Incomplete
    past: str
    future: str
    and_word: str
    timeframes: Incomplete
    meridians: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete

class UzbekLocale(Locale):
    names: Incomplete
    past: str
    future: str
    timeframes: Incomplete
    month_names: Incomplete
    month_abbreviations: Incomplete
    day_names: Incomplete
    day_abbreviations: Incomplete
