from _typeshed import Incomplete
from openpyxl.styles import numbers as numbers

PERCENT_REGEX: Incomplete
TIME_REGEX: Incomplete
NUMBER_REGEX: Incomplete

def cast_numeric(value):
    """Explicitly convert a string to a numeric value"""
def cast_percentage(value):
    """Explicitly convert a string to numeric value and format as a
    percentage"""
def cast_time(value):
    """Explicitly convert a string to a number and format as datetime or
    time"""
