from . import csp_report_uri as csp_report_uri
from ...base.handlers import APIHandler as APIHandler
from _typeshed import Incomplete
from jupyter_server.auth import authorized as authorized

AUTH_RESOURCE: str

class CSPReportHandler(APIHandler):
    """Accepts a content security policy violation report"""
    auth_resource = AUTH_RESOURCE
    def skip_check_origin(self):
        """Don't check origin when reporting origin-check violations!"""
    def check_xsrf_cookie(self) -> None:
        """Don't check XSRF for CSP reports."""
    def post(self) -> None:
        """Log a content security policy violation report"""

default_handlers: Incomplete
