from mlflow.environment_variables import MLFLOW_TRACKING_PASSWORD as MLFLOW_TRACKING_PASSWORD, MLFLOW_TRACKING_USERNAME as MLFLOW_TRACKING_USERNAME
from typing import NamedTuple

class MlflowCreds(NamedTuple):
    username: str | None
    password: str | None

def read_mlflow_creds() -> MlflowCreds: ...
