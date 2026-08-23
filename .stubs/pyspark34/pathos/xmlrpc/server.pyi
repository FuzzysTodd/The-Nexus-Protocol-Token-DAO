from _typeshed import Incomplete
from http.server import BaseHTTPRequestHandler
from pathos.server import Server
from xmlrpc.server import SimpleXMLRPCDispatcher

__all__ = ['XMLRPCServer', 'XMLRPCRequestHandler']

class XMLRPCServer(Server, SimpleXMLRPCDispatcher):
    """extends base pathos server to an XML-RPC dispatcher"""
    def activate(self) -> None:
        """install callbacks"""
    def serve(self) -> None:
        """enter the select loop... and wait for service requests"""
    def __init__(self, host, port) -> None:
        """create a XML-RPC server

Takes two initial inputs:
    host  -- hostname of XML-RPC server host
    port  -- port number for server requests
        """

class XMLRPCRequestHandler(BaseHTTPRequestHandler):
    """ create a XML-RPC request handler """
    def do_POST(self):
        """ Access point from HTTP handler """
    def log_message(self, format, *args) -> None:
        """ Overriding BaseHTTPRequestHandler.log_message() """
    rfile: Incomplete
    wfile: Incomplete
    connection: Incomplete
    client_address: Incomplete
    def __init__(self, server, socket) -> None:
        """
Override BaseHTTPRequestHandler.__init__(): we need to be able
to have (potentially) multiple handler objects at a given time.

Inputs:
    server  -- server object to handle requests for 
    socket  -- socket connection 
        """
