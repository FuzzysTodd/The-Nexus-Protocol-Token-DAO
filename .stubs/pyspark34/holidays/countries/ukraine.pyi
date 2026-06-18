from _typeshed import Incomplete
from holidays.calendars.gregorian import APR as APR, AUG as AUG, DEC as DEC, FEB as FEB, GREGORIAN_CALENDAR as GREGORIAN_CALENDAR, JAN as JAN, JUL as JUL, JUN as JUN, MAR as MAR, MAY as MAY, OCT as OCT, SEP as SEP
from holidays.calendars.julian import JULIAN_CALENDAR as JULIAN_CALENDAR
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays, StaticHolidays as StaticHolidays
from holidays.observed_holiday_base import ObservedHolidayBase as ObservedHolidayBase, SAT_SUN_TO_NEXT_WORKDAY as SAT_SUN_TO_NEXT_WORKDAY

class Ukraine(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """
    Current holidays list:
    https://zakon1.rada.gov.ua/laws/show/322-08/paran454#n454

    Substituted holidays:
    2001 - https://zakon.rada.gov.ua/laws/show/138-2001-%D1%80
    2002,
    2003 - https://zakon.rada.gov.ua/laws/show/202-2002-%D1%80,
           https://zakon.rada.gov.ua/laws/show/705-2002-%D1%80
    2004 - https://zakon.rada.gov.ua/laws/show/773-2003-%D1%80
    2005 - https://zakon.rada.gov.ua/laws/show/936-2004-%D1%80,
           https://zakon.rada.gov.ua/laws/show/133-2005-%D1%80
    2006 - https://zakon.rada.gov.ua/laws/show/490-2005-%D1%80,
           https://zakon.rada.gov.ua/laws/show/562-2005-%D1%80
    2007 - https://zakon.rada.gov.ua/laws/show/612-2006-%D1%80
    2008 - https://zakon.rada.gov.ua/laws/show/1059-2007-%D1%80,
           https://zakon.rada.gov.ua/laws/show/538-2008-%D1%80
    2009 - https://zakon.rada.gov.ua/laws/show/1458-2008-%D1%80
    2010 - https://zakon.rada.gov.ua/laws/show/1412-2009-%D1%80
    2011 - https://zakon.rada.gov.ua/laws/show/2130-2010-%D1%80
    2012 - https://zakon.rada.gov.ua/laws/show/1210-2011-%D1%80
    2013 - https://zakon.rada.gov.ua/laws/show/1043-2012-%D1%80
    2014 - https://zakon.rada.gov.ua/laws/show/920-2013-%D1%80
    2015 - https://zakon.rada.gov.ua/laws/show/1084-2014-%D1%80
    2016 - https://zakon.rada.gov.ua/laws/show/1155-2015-%D1%80
    2017 - https://zakon.rada.gov.ua/laws/show/850-2016-%D1%80
    2018 - https://zakon.rada.gov.ua/laws/show/1-2018-%D1%80
    2019 - https://zakon.rada.gov.ua/laws/show/7-2019-%D1%80
    2020 - https://zakon.rada.gov.ua/laws/show/995-2019-%D1%80
    2021 - https://zakon.rada.gov.ua/laws/show/1191-2020-%D1%80
    2022 - https://zakon.rada.gov.ua/laws/show/1004-2021-%D1%80
    """
    country: str
    default_language: str
    observed_label: Incomplete
    supported_languages: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class UA(Ukraine): ...
class UKR(Ukraine): ...

class UkraineStaticHolidays:
    substituted_date_format: Incomplete
    substituted_label: Incomplete
    substituted_holidays: Incomplete
