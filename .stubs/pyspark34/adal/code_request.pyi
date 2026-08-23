from . import constants as constants, log as log, oauth2_client as oauth2_client
from _typeshed import Incomplete

OAUTH2_PARAMETERS: Incomplete

class CodeRequest:
    def __init__(self, call_context, authentication_context, client_id, resource) -> None: ...
    def get_user_code_info(self, language): ...
