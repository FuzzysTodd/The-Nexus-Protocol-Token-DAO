from . import log as log, util as util, xmlutil as xmlutil
from .adal_error import AdalError as AdalError
from .constants import WSTrustVersion as WSTrustVersion, XmlNamespaces as XmlNamespaces
from _typeshed import Incomplete

TRANSPORT_BINDING_XPATH: str
TRANSPORT_BINDING_2005_XPATH: str
SOAP_ACTION_XPATH: str
RST_SOAP_ACTION_13: str
RST_SOAP_ACTION_2005: str
SOAP_TRANSPORT_XPATH: str
SOAP_HTTP_TRANSPORT_VALUE: str
PORT_XPATH: str
ADDRESS_XPATH: str

class Mex:
    username_password_policy: Incomplete
    def __init__(self, call_context, url) -> None: ...
    def discover(self) -> None: ...
