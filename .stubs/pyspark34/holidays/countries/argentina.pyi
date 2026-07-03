from _typeshed import Incomplete
from holidays.calendars.gregorian import APR as APR, AUG as AUG, DEC as DEC, FEB as FEB, JAN as JAN, JUL as JUL, JUN as JUN, MAR as MAR, MAY as MAY, NOV as NOV, OCT as OCT, SEP as SEP
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays, StaticHolidays as StaticHolidays
from holidays.observed_holiday_base import ObservedHolidayBase as ObservedHolidayBase, THU_FRI_TO_NEXT_MON as THU_FRI_TO_NEXT_MON, THU_TO_NEXT_MON as THU_TO_NEXT_MON, TUE_WED_TO_PREV_MON as TUE_WED_TO_PREV_MON

class Argentina(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """
    A subclass of :py:class:`HolidayBase` representing public holidays
    in Argentina.


    References:

    - Based on:
        https://es.wikipedia.org/wiki/Anexo:D%C3%ADas_feriados_en_Argentina
    - [Ley 24455] Belgrano and San Martin Day as third Monday
    - [Ley 27399] - For 2018++
        https://www.argentina.gob.ar/normativa/nacional/ley-27399-281835/texto
    - [Decreto 1585/2010] - 2011-2013 Bridge Holidays, Movable Holidays Law
    - [Decreto 1768/2013] - 2014-2016 Bridge Holidays
    - [Decretos 52-80-923/2017] - 2017-2019 Bridge Holidays
    - [Decreto 717/2019] - 2020 Bridge Holidays
    - [Decreto 297/2020] - Veteran Day moved due to Covid-19
    - [Decreto 947/2020] - 2021 Bridge Holidays
    - [Decreto 789/2021] - 2022 Bridge Holidays
    - [Decreto 764/2022] - 2023 Bridge Holidays
    - [Always Update Calendar Year Link]
        https://www.argentina.gob.ar/interior/feriados
        http://servicios.lanacion.com.ar/feriados
        https://www.clarin.com/feriados/
    - [Specific Calendar Year]
        https://www.lanacion.com.ar/feriados/2024/
        https://www.argentina.gob.ar/interior/feriados-nacionales-2023
        https://www.argentina.gob.ar/interior/feriados-nacionales-2022
        https://www.argentina.gob.ar/interior/feriados-nacionales-2021
        https://www.argentina.gob.ar/interior/feriados-nacionales-2020
        https://www.cultura.gob.ar/feriados-2019-en-argentina_7326/
        https://servicios.lanacion.com.ar/app-mobile/feriados/2019
        https://servicios.lanacion.com.ar/app-mobile/feriados/2018
        https://servicios.lanacion.com.ar/app-mobile/feriados/2017
        https://servicios.lanacion.com.ar/app-mobile/feriados/2016
        https://servicios.lanacion.com.ar/app-mobile/feriados/2015

        Movable Holidays Laws:
    - Decreto 1584/2010: 2010-11-03
        - AUG 17, OCT 12, NOV 20 Holidays will always be on MON
    - Decreto 52/2017: 2017-01-23 (Reconfirmed in Ley 27399)
        - If TUE/WED - observed on previous MON
        - If THU/FRI - observed on next MON
    """
    country: str
    default_language: str
    supported_languages: Incomplete
    observed_label: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class AR(Argentina): ...
class ARG(Argentina): ...

class ArgentinaStaticHolidays:
    """
    Special Bridge Holidays are given upto 3 days a year
    as long as it's declared 50 days before calendar year's end
    There's no Bridge Holidays declared in 2017.
    """
    arg_bridge_public_holiday: Incomplete
    bicentennial_national_flag: Incomplete
    bicentennial_battle_tucuman: Incomplete
    bicentennial_assembly_1813: Incomplete
    bicentennial_battle_salta: Incomplete
    national_census_2022: Incomplete
    special_holidays: Incomplete
