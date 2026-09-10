from .common_utils import print_error as print_error
from .constants import REST_TIME_OUT as REST_TIME_OUT
from .url_utils import check_status_url as check_status_url

def rest_put(url, data, timeout, show_error: bool = False):
    """Call rest put method"""
def rest_post(url, data, timeout, show_error: bool = False):
    """Call rest post method"""
def rest_get(url, timeout, show_error: bool = False):
    """Call rest get method"""
def rest_delete(url, timeout, show_error: bool = False):
    """Call rest delete method"""
def check_rest_server(rest_port):
    """Check if restful server is ready"""
def check_rest_server_quick(rest_port):
    """Check if restful server is ready, only check once"""
def check_response(response):
    """Check if a response is success according to status_code"""
