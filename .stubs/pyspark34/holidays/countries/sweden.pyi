from _typeshed import Incomplete
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class Sweden(HolidayBase, ChristianHolidays, InternationalHolidays):
    '''
    Swedish holidays.
    Note that holidays falling on a sunday are "lost",
    it will not be moved to another day to make up for the collision.
    In Sweden, ALL sundays are considered a holiday
    (https://sv.wikipedia.org/wiki/Helgdagar_i_Sverige).
    Initialize this class with include_sundays=False
    to not include sundays as a holiday.
    Primary sources:
    https://sv.wikipedia.org/wiki/Helgdagar_i_Sverige and
    http://www.riksdagen.se/sv/dokument-lagar/dokument/svensk-forfattningssamling/lag-1989253-om-allmanna-helgdagar_sfs-1989-253
    '''
    country: str
    default_language: str
    supported_languages: Incomplete
    include_sundays: Incomplete
    def __init__(self, include_sundays: bool = True, *args, **kwargs) -> None:
        """
        :param include_sundays: Whether to consider sundays as a holiday
        (which they are in Sweden)
        :param kwargs:
        """

class SE(Sweden): ...
class SWE(Sweden): ...
