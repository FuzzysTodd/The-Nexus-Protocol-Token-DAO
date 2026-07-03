class _CustomCalendarType(type):
    """Helper class for simple calendar customization.

    Renames child class public attributes keeping the original data under a new
    name with a `CUSTOM_ATTR_POSTFIX` postfix.

    Allows for better readability of customized lunisolar calendar dates.
    """
    CUSTOM_ATTR_POSTFIX: str
    def __new__(cls, name, bases, namespace): ...

class _CustomCalendar(metaclass=_CustomCalendarType): ...
