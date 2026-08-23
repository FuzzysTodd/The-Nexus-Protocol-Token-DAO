from sentry_sdk._compat import iteritems as iteritems
from sentry_sdk._types import TYPE_CHECKING as TYPE_CHECKING
from typing import Dict

def get_host(environ: Dict[str, str], use_x_forwarded_for: bool = False) -> str:
    """
    Return the host for the given WSGI environment.
    """
