from _typeshed import Incomplete
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class Germany(HolidayBase, ChristianHolidays, InternationalHolidays):
    '''Official holidays for Germany in its current form.

    This class doesn\'t return any holidays before 1990-10-03.

    Before that date the current Germany was separated into the "German
    Democratic Republic" and the "Federal Republic of Germany" which both had
    somewhat different holidays. Since this class is called "Germany" it
    doesn\'t really make sense to include the days from the two former
    countries.

    Note that Germany doesn\'t have rules for holidays that happen on a
    Sunday. Those holidays are still holiday days but there is no additional
    day to make up for the "lost" day.

    Also note that German holidays are partly declared by each province there
    are some weired edge cases:

        - "Mariä Himmelfahrt" is only a holiday in Bavaria (BY) if your
          municipality is mostly catholic which in term depends on census data.
          Since we don\'t have this data but most municipalities in Bavaria
          *are* mostly catholic, we count that as holiday for whole Bavaria.
          We added BYP for the municipality in Bavaria with more protestants.
          Here this is excluded.
        - There is an "Augsburger Friedensfest" which only exists in the town
          Augsburg. This is excluded for Bavaria.
        - "Gründonnerstag" (Thursday before easter) is not a holiday but pupils
           don\'t have to go to school (but only in Baden Württemberg) which is
           solved by adjusting school holidays to include this day. It is
           excluded from our list.
        - "Fronleichnam" is a holiday in certain, explicitly defined
          municipalities in Saxony (SN) and Thuringia (TH). We exclude it from
          both provinces.
    '''
    country: str
    default_language: str
    supported_languages: Incomplete
    subdivisions: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class DE(Germany): ...
class DEU(Germany): ...
