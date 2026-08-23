from . import constants as constants, log as log, util as util
from .adal_error import AdalError as AdalError
from _typeshed import Incomplete

USER_REALM_PATH_TEMPLATE: str
ACCOUNT_TYPE: Incomplete
FEDERATION_PROTOCOL_TYPE: Incomplete

class UserRealm:
    api_version: str
    federation_protocol: Incomplete
    account_type: Incomplete
    federation_metadata_url: Incomplete
    federation_active_auth_url: Incomplete
    cloud_audience_urn: Incomplete
    def __init__(self, call_context, user_principle, authority_url) -> None: ...
    def discover(self) -> None: ...
