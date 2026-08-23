from _typeshed import Incomplete
from isodate.isoerror import ISO8601Error as ISO8601Error
from isodate.isostrf import DATE_EXT_COMPLETE as DATE_EXT_COMPLETE, strftime as strftime

DATE_REGEX_CACHE: Incomplete

def build_date_regexps(yeardigits: int = 4, expanded: bool = False):
    """
    Compile set of regular expressions to parse ISO dates. The expressions will
    be created only if they are not already in REGEX_CACHE.

    It is necessary to fix the number of year digits, else it is not possible
    to automatically distinguish between various ISO date formats.

    ISO 8601 allows more than 4 digit years, on prior agreement, but then a +/-
    sign is required (expanded format). To support +/- sign for 4 digit years,
    the expanded parameter needs to be set to True.
    """
def parse_date(datestring, yeardigits: int = 4, expanded: bool = False, defaultmonth: int = 1, defaultday: int = 1):
    """
    Parse an ISO 8601 date string into a datetime.date object.

    As the datetime.date implementation is limited to dates starting from
    0001-01-01, negative dates (BC) and year 0 can not be parsed by this
    method.

    For incomplete dates, this method chooses the first day for it. For
    instance if only a century is given, this method returns the 1st of
    January in year 1 of this century.

    supported formats: (expanded formats are shown with 6 digits for year)
      YYYYMMDD    +-YYYYYYMMDD      basic complete date
      YYYY-MM-DD  +-YYYYYY-MM-DD    extended complete date
      YYYYWwwD    +-YYYYYYWwwD      basic complete week date
      YYYY-Www-D  +-YYYYYY-Www-D    extended complete week date
      YYYYDDD     +-YYYYYYDDD       basic ordinal date
      YYYY-DDD    +-YYYYYY-DDD      extended ordinal date
      YYYYWww     +-YYYYYYWww       basic incomplete week date
      YYYY-Www    +-YYYYYY-Www      extended incomplete week date
      YYYMM       +-YYYYYYMM        basic incomplete month date
      YYY-MM      +-YYYYYY-MM       incomplete month date
      YYYY        +-YYYYYY          incomplete year date
      YY          +-YYYY            incomplete century date

    @param datestring: the ISO date string to parse
    @param yeardigits: how many digits are used to represent a year
    @param expanded: if True then +/- signs are allowed. This parameter
                     is forced to True, if yeardigits != 4

    @return: a datetime.date instance represented by datestring
    @raise ISO8601Error: if this function can not parse the datestring
    @raise ValueError: if datestring can not be represented by datetime.date
    """
def date_isoformat(tdate, format=..., yeardigits: int = 4):
    """
    Format date strings.

    This method is just a wrapper around isodate.isostrf.strftime and uses
    Date-Extended-Complete as default format.
    """
