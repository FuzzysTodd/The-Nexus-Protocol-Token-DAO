import xmlrpc.client
from _typeshed import Incomplete
from pip._internal.exceptions import NetworkConnectionError as NetworkConnectionError
from pip._internal.network.session import PipSession as PipSession
from pip._internal.network.utils import raise_for_status as raise_for_status
from typing import Tuple
from xmlrpc.client import _HostType, _Marshallable

logger: Incomplete

class PipXmlrpcTransport(xmlrpc.client.Transport):
    """Provide a `xmlrpclib.Transport` implementation via a `PipSession`
    object.
    """
    def __init__(self, index_url: str, session: PipSession, use_datetime: bool = False) -> None: ...
    verbose: Incomplete
    def request(self, host: _HostType, handler: str, request_body: bytes, verbose: bool = False) -> Tuple['_Marshallable', ...]: ...
