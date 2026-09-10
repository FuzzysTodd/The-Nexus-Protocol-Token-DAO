from datetime import date

class _Persian:
    """
    Persian calendar (Solar Hijri) for 1901-2100 years.

    https://en.wikipedia.org/wiki/Solar_Hijri_calendar
    """
    START_YEAR: int
    END_YEAR: int
    def new_year_date(self, year: int) -> date | None:
        """
        Return Gregorian date of Persian new year (1 Farvardin) in a given Gregorian year.
        """
    def persian_to_gregorian(self, year: int, j_month: int, j_day: int) -> date | None:
        """
        Return Gregorian date of Persian day and month in a given Gregorian year.
        """
