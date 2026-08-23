from . import log as log, util as util
from .adal_error import AdalError as AdalError
from .constants import AADConstants as AADConstants
from _typeshed import Incomplete

class Authority:
    token_endpoint: Incomplete
    device_code_endpoint: Incomplete
    is_adfs_authority: Incomplete
    def __init__(self, authority_url, validate_authority: bool = True) -> None: ...
    @property
    def url(self): ...
    def validate(self, call_context) -> None: ...
