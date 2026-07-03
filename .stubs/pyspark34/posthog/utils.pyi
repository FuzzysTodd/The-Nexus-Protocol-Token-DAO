from _typeshed import Incomplete
from collections import defaultdict

log: Incomplete

def is_naive(dt):
    """Determines if a given datetime.datetime is naive."""
def total_seconds(delta):
    """Determines total seconds with python < 2.7 compat."""
def guess_timezone(dt):
    """Attempts to convert a naive datetime to an aware datetime."""
def remove_trailing_slash(host): ...
def clean(item): ...
def is_valid_regex(value) -> bool: ...

class SizeLimitedDict(defaultdict):
    max_size: Incomplete
    def __init__(self, max_size, *args, **kwargs) -> None: ...
    def __setitem__(self, key, value) -> None: ...

def convert_to_datetime_aware(date_obj): ...
