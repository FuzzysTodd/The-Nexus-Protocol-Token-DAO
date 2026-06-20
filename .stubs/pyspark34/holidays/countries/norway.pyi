from _typeshed import Incomplete
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class Norway(HolidayBase, ChristianHolidays, InternationalHolidays):
    '''
    Norwegian holidays.
    Note that holidays falling on a sunday is "lost",
    it will not be moved to another day to make up for the collision.

    In Norway, ALL sundays are considered a holiday (https://snl.no/helligdag).
    Initialize this class with include_sundays=False
    to not include sundays as a holiday.

    Primary sources:
    https://lovdata.no/dokument/NL/lov/1947-04-26-1
    https://no.wikipedia.org/wiki/Helligdager_i_Norge
    https://www.timeanddate.no/merkedag/norge/
    '''
    country: str
    default_language: str
    supported_languages: Incomplete
    include_sundays: Incomplete
    def __init__(self, include_sundays: bool = False, *args, **kwargs) -> None:
        """
        :param include_sundays: Whether to consider sundays as a holiday
        (which they are in Norway)
        :param kwargs:
        """

class NO(Norway): ...
class NOR(Norway): ...
