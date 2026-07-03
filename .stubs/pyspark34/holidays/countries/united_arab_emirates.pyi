from _typeshed import Incomplete
from holidays.calendars import _CustomIslamicHolidays
from holidays.calendars.gregorian import APR as APR, AUG as AUG, FRI as FRI, JUL as JUL, JUN as JUN, MAY as MAY, NOV as NOV, SAT as SAT, SEP as SEP
from holidays.groups import InternationalHolidays as InternationalHolidays, IslamicHolidays as IslamicHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class UnitedArabEmirates(HolidayBase, InternationalHolidays, IslamicHolidays):
    """
    Holidays are regulated by the Article 74
    of Federal Law No. 08 for the year 1980:
    https://www.ilo.org/dyn/natlex/docs/ELECTRONIC/11956/69376/F417089305/ARE11956.pdf
    However the law is not applied literally,
    and was amended often in the past few years.
    Sources:
    2017: https://www.khaleejtimes.com/nation/uae-official-public-holidays-list-2017
    2018: https://www.thenational.ae/uae/government/uae-public-holidays-2018-announced-by-abu-dhabi-government-1.691393  # noqa: E501
    2019: https://www.thenational.ae/uae/government/uae-public-holidays-for-2019-and-2020-announced-by-cabinet-1.833425  # noqa: E501
    2020: https://u.ae/en/information-and-services/public-holidays-and-religious-affairs/public-holidays  # noqa: E501

    Holidays based on the Islamic Calendar are estimated (and so denoted),
    as are announced each year and based on moon sightings:
    - Eid al-Fitr
    - Eid al-Adha
    - Arafat (Hajj) Day
    - Al-Hijra (Islamic New Year
    - Mawlud al-Nabi (Prophet Mohammad's Birthday)
    - Leilat al-Miraj (Ascension of the Prophet), suspended after 2018.
    """
    country: str
    default_language: str
    estimated_label: Incomplete
    supported_languages: Incomplete
    weekend: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class AE(UnitedArabEmirates): ...
class ARE(UnitedArabEmirates): ...

class UnitedArabEmiratesIslamicHolidays(_CustomIslamicHolidays):
    EID_AL_ADHA_DATES: Incomplete
    EID_AL_FITR_DATES: Incomplete
    HIJRI_NEW_YEAR_DATES: Incomplete
    ISRA_AND_MIRAJ_DATES: Incomplete
    MAWLID_DATES: Incomplete
