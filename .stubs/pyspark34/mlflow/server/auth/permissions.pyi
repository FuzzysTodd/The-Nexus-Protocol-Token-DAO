from _typeshed import Incomplete
from dataclasses import dataclass
from mlflow import MlflowException as MlflowException
from mlflow.protos.databricks_pb2 import INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE

@dataclass
class Permission:
    name: str
    can_read: bool
    can_update: bool
    can_delete: bool
    can_manage: bool
    def __init__(self, name, can_read, can_update, can_delete, can_manage) -> None: ...

READ: Incomplete
EDIT: Incomplete
MANAGE: Incomplete
NO_PERMISSIONS: Incomplete
ALL_PERMISSIONS: Incomplete

def get_permission(permission: str) -> Permission: ...
