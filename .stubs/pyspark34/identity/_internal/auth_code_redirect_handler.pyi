from _typeshed import Incomplete
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Any, Mapping

class AuthCodeRedirectHandler(BaseHTTPRequestHandler):
    """HTTP request handler to capture the authentication server's response.
    Mostly from the Azure CLI: https://github.com/Azure/azure-cli/blob/dev/src/azure-cli-core/azure/cli/core/_profile.py
    """
    def do_GET(self) -> None: ...
    def log_message(self, format, *args) -> None: ...

class AuthCodeRedirectServer(HTTPServer):
    """HTTP server that listens for the redirect request following an authorization code authentication"""
    query_params: Mapping[str, Any]
    timeout: Incomplete
    def __init__(self, hostname: str, port: int, timeout: int) -> None: ...
    def wait_for_redirect(self) -> Mapping[str, Any]: ...
    def handle_timeout(self) -> None:
        """Break the request-handling loop by tearing down the server"""
