from . import log as log, util as util, wstrust_response as wstrust_response
from .adal_error import AdalError as AdalError
from .constants import WSTrustVersion as WSTrustVersion

class WSTrustRequest:
    def __init__(self, call_context, wstrust_endpoint_url, applies_to, wstrust_endpoint_version) -> None: ...
    def acquire_token(self, username, password): ...
