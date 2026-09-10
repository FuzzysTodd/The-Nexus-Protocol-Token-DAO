from ..pipeline import PipelineContext as PipelineContext, PipelineRequest as PipelineRequest, PipelineResponse as PipelineResponse
from ..pipeline.policies import SansIOHTTPPolicy as SansIOHTTPPolicy
from _typeshed import Incomplete
from azure.core.pipeline.transport import HttpRequest as PipelineTransportHttpRequest
from azure.core.rest._rest_py3 import HttpRequest as RestHttpRequestPy3
from http.client import HTTPConnection

HTTPRequestType = RestHttpRequestPy3 | PipelineTransportHttpRequest
binary_type = str

class BytesIOSocket:
    '''Mocking the "makefile" of socket for HTTPResponse.
    This can be used to create a http.client.HTTPResponse object
    based on bytes and not a real socket.

    :param bytes bytes_data: The bytes to use to mock the socket.
    '''
    bytes_data: Incomplete
    def __init__(self, bytes_data) -> None: ...
    def makefile(self, *_): ...

class _HTTPSerializer(HTTPConnection):
    """Hacking the stdlib HTTPConnection to serialize HTTP request as strings."""
    buffer: bytes
    def __init__(self, *args, **kwargs) -> None: ...
    def putheader(self, header, *values) -> None: ...
    def send(self, data) -> None: ...
