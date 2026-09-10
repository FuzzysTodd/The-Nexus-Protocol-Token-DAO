from _typeshed import Incomplete
from holidays.calendars.gregorian import APR as APR, AUG as AUG
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class Aruba(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    https://www.government.aw/information-public-services/hiring-people_47940/item/holidays_43823.html  # noqa: E501
    https://www.overheid.aw/informatie-dienstverlening/ondernemen-en-werken-subthemas_46970/item/feestdagen_37375.html  # noqa: E501
    https://www.gobierno.aw/informacion-tocante-servicio/haci-negoshi-y-traha-sub-topics_47789/item/dia-di-fiesta_41242.html  # noqa: E501
    https://www.visitaruba.com/about-aruba/national-holidays-and-celebrations/
    https://www.arubatoday.com/we-celebrate-our-national-hero-betico-croes/
    https://www.caribbeannewsglobal.com/carnival-monday-remains-a-festive-day-in-aruba/  # noqa: E501
    https://www.aruba.com/us/calendar/national-anthem-and-flag-day
    """
    country: str
    default_language: str
    supported_languages: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class AW(Aruba): ...
class ABW(Aruba): ...
