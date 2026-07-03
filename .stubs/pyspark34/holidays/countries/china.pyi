from _typeshed import Incomplete
from holidays.calendars.gregorian import DEC as DEC, JAN as JAN, MAY as MAY, OCT as OCT, SEP as SEP
from holidays.constants import HALF_DAY as HALF_DAY, PUBLIC as PUBLIC
from holidays.groups import ChineseCalendarHolidays as ChineseCalendarHolidays, InternationalHolidays as InternationalHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class China(HolidayBase, ChineseCalendarHolidays, InternationalHolidays):
    """
    References:
    - https://en.wikipedia.org/wiki/Public_holidays_in_China
    - https://zh.wikipedia.org/wiki/中华人民共和国节日与公众假期
    - https://www.gov.cn/gongbao/content/2023/content_5736714.htm # 2023
    - https://www.gov.cn/gongbao/content/2021/content_5651728.htm # 2022
    - https://www.gov.cn/gongbao/content/2020/content_5567750.htm # 2021
    - https://www.gov.cn/gongbao/content/2019/content_5459138.htm # 2020
    - https://www.gov.cn/gongbao/content/2018/content_5350046.htm # 2019
    - https://www.gov.cn/gongbao/content/2017/content_5248221.htm # 2018
    - https://www.gov.cn/gongbao/content/2016/content_5148793.htm # 2017
    - https://www.gov.cn/gongbao/content/2016/content_2979719.htm # 2016
    - https://www.gov.cn/gongbao/content/2015/content_2799019.htm # 2015
    - https://www.gov.cn/gongbao/content/2014/content_2561299.htm # 2014
    - https://www.gov.cn/gongbao/content/2012/content_2292057.htm # 2013
    - https://www.gov.cn/gongbao/content/2011/content_2020918.htm # 2012
    - https://www.gov.cn/gongbao/content/2010/content_1765282.htm # 2011
    - https://www.gov.cn/gongbao/content/2009/content_1487011.htm # 2010
    - https://www.gov.cn/gongbao/content/2008/content_1175823.htm # 2009
    - https://www.gov.cn/gongbao/content/2008/content_859870.htm # 2008
    - https://www.gov.cn/gongbao/content/2007/content_503397.htm # 2007
    - https://zh.wikisource.org/wiki/国务院办公厅关于2006年部分节假日安排的通知 # 2006
    - https://zh.wikisource.org/wiki/国务院办公厅关于2005年部分节假日安排的通知 # 2005
    - https://zh.wikisource.org/wiki/国务院办公厅关于2004年部分节假日安排的通知 # 2004
    - https://zh.wikisource.org/wiki/国务院办公厅关于2003年部分节假日休息安排的通知 # 2003
    - https://zh.wikisource.org/wiki/国务院办公厅关于2002年部分节假日休息安排的通知 # 2002
    - https://zh.wikisource.org/wiki/国务院办公厅关于2001年春节、“五一”、“十一”放假安排的通知 # 2001

    Checked With:
    - https://www.officeholidays.com/countries/china/2023
    - https://www.china-briefing.com/news/china-public-holiday-2023-schedule/
    - https://www.timeanddate.com/calendar/?year=2023&country=41
    - https://m.wannianli.tianqi.com/fangjiaanpai/2001.html # 2001-2010

    Limitations:

    - Only checked with the official General Office of the State Council Notice from 2001 onwards.

    - Due to its complexity, need yearly checks 3-weeks before year's end each year.
    """
    country: str
    supported_categories: Incomplete
    default_language: str
    supported_languages: Incomplete
    new_years_day_overflow: Incomplete
    national_day_2008_golden_week: Incomplete
    mid_autumn_festival_2010_special: Incomplete
    special_public_holidays: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class CN(China): ...
class CHN(China): ...
