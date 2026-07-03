import ctypes as ct
from .._constants import VSCODE_CREDENTIALS_SECTION as VSCODE_CREDENTIALS_SECTION
from _typeshed import Incomplete

SUPPORTED_CREDKEYS: Incomplete

class _CREDENTIAL(ct.Structure): ...

def get_user_settings(): ...
def get_refresh_token(cloud_name): ...
