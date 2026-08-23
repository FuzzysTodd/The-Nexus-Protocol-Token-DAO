from mlflow.environment_variables import MLFLOW_AUTH_CONFIG_PATH as MLFLOW_AUTH_CONFIG_PATH
from typing import NamedTuple

class AuthConfig(NamedTuple):
    default_permission: str
    database_uri: str
    admin_username: str
    admin_password: str

def read_auth_config() -> AuthConfig: ...
