from .auth import User as User
from .prometheus.log_functions import prometheus_log_method as prometheus_log_method

def log_request(handler) -> None:
    """log a bit more information about each request than tornado's default

    - move static file get success to debug-level (reduces noise)
    - get proxied IP instead of proxy IP
    - log referer for redirect and failed requests
    - log user-agent for failed requests
    """
