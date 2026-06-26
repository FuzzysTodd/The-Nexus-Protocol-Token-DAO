import inspect
from typing import Any

def getargspec(func: Any) -> inspect.FullArgSpec:
    """Like inspect.getargspec but supports functools.partial as well."""
