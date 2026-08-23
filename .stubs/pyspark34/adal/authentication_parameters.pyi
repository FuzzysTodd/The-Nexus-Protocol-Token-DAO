from . import log as log, util as util
from .constants import HttpError as HttpError
from _typeshed import Incomplete

AUTHORIZATION_URI: str
RESOURCE: str
WWW_AUTHENTICATE_HEADER: str

class AuthenticationParameters:
    authorization_uri: Incomplete
    resource: Incomplete
    def __init__(self, authorization_uri, resource) -> None: ...

bearer_challenge_structure_validation: Incomplete
first_key_value_pair_regex: Incomplete
all_other_key_value_pair_regex: Incomplete

def parse_challenge(challenge): ...
def create_authentication_parameters_from_header(challenge): ...
def create_authentication_parameters_from_response(response): ...
def validate_url_object(url) -> None: ...
def create_authentication_parameters_from_url(url, correlation_id: Incomplete | None = None): ...
