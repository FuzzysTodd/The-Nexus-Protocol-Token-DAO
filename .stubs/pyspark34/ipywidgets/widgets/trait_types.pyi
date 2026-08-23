import datetime as dt
import traitlets
from _typeshed import Incomplete

class Color(traitlets.Unicode):
    """A string holding a valid HTML color such as 'blue', '#060482', '#A80'"""
    info_text: str
    default_value: Incomplete
    def validate(self, obj, value): ...

class Datetime(traitlets.TraitType):
    """A trait type holding a Python datetime object"""
    klass = dt.datetime
    default_value: Incomplete

class Date(traitlets.TraitType):
    """A trait type holding a Python date object"""
    klass = dt.date
    default_value: Incomplete

class Time(traitlets.TraitType):
    """A trait type holding a Python time object"""
    klass = dt.date
    default_value: Incomplete

def datetime_to_json(pydt, manager):
    """Serialize a Python datetime object to json.

    Instantiating a JavaScript Date object with a string assumes that the
    string is a UTC string, while instantiating it with constructor arguments
    assumes that it's in local time:

    >>> cdate = new Date('2015-05-12')
    Mon May 11 2015 20:00:00 GMT-0400 (Eastern Daylight Time)
    >>> cdate = new Date(2015, 4, 12) // Months are 0-based indices in JS
    Tue May 12 2015 00:00:00 GMT-0400 (Eastern Daylight Time)

    Attributes of this dictionary are to be passed to the JavaScript Date
    constructor.
    """
def datetime_from_json(js, manager):
    """Deserialize a Python datetime object from json."""

datetime_serialization: Incomplete

def naive_to_json(pydt, manager):
    """Serialize a naive Python datetime object to json.

    Instantiating a JavaScript Date object with a string assumes that the
    string is a UTC string, while instantiating it with constructor arguments
    assumes that it's in local time:

    >>> cdate = new Date('2015-05-12')
    Mon May 11 2015 20:00:00 GMT-0400 (Eastern Daylight Time)
    >>> cdate = new Date(2015, 4, 12) // Months are 0-based indices in JS
    Tue May 12 2015 00:00:00 GMT-0400 (Eastern Daylight Time)

    Attributes of this dictionary are to be passed to the JavaScript Date
    constructor.
    """
def naive_from_json(js, manager):
    """Deserialize a naive Python datetime object from json."""

naive_serialization: Incomplete

def date_to_json(pydate, manager):
    """Serialize a Python date object.

    Attributes of this dictionary are to be passed to the JavaScript Date
    constructor.
    """
def date_from_json(js, manager):
    """Deserialize a Javascript date."""

date_serialization: Incomplete

class ByteMemoryView(traitlets.TraitType):
    """A trait for memory views of bytes."""
    default_value: Incomplete
    info_text: str
    def validate(self, obj, value): ...
    def default_value_repr(self): ...

class CByteMemoryView(ByteMemoryView):
    """A casting version of the byte memory view trait."""
    def validate(self, obj, value): ...

def time_to_json(pyt, manager):
    """Serialize a Python time object to json."""
def time_from_json(js, manager):
    """Deserialize a Python time object from json."""

time_serialization: Incomplete

class InstanceDict(traitlets.Instance):
    """An instance trait which coerces a dict to an instance.

    This lets the instance be specified as a dict, which is used
    to initialize the instance.

    Also, we default to a trivial instance, even if args and kwargs
    is not specified."""
    def validate(self, obj, value): ...
    def make_dynamic_default(self): ...

class NumberFormat(traitlets.Unicode):
    """A string holding a number format specifier, e.g. '.3f'

    This traitlet holds a string that can be passed to the
    `d3-format <https://github.com/d3/d3-format>`_ JavaScript library.
    The format allowed is similar to the Python format specifier (PEP 3101).
    """
    info_text: str
    default_value: Incomplete
    def validate(self, obj, value): ...

class TypedTuple(traitlets.Container):
    """A trait for a tuple of any length with type-checked elements."""
    klass = tuple

def bytes_from_json(js, obj): ...

bytes_serialization: Incomplete
