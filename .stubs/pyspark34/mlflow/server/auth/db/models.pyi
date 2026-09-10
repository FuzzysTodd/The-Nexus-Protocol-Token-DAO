from _typeshed import Incomplete
from mlflow.server.auth.entities import ExperimentPermission as ExperimentPermission, RegisteredModelPermission as RegisteredModelPermission, User as User

Base: Incomplete

class SqlUser(Base):
    __tablename__: str
    id: Incomplete
    username: Incomplete
    password_hash: Incomplete
    is_admin: Incomplete
    experiment_permissions: Incomplete
    registered_model_permissions: Incomplete
    def to_mlflow_entity(self): ...

class SqlExperimentPermission(Base):
    __tablename__: str
    id: Incomplete
    experiment_id: Incomplete
    user_id: Incomplete
    permission: Incomplete
    __table_args__: Incomplete
    def to_mlflow_entity(self): ...

class SqlRegisteredModelPermission(Base):
    __tablename__: str
    id: Incomplete
    name: Incomplete
    user_id: Incomplete
    permission: Incomplete
    __table_args__: Incomplete
    def to_mlflow_entity(self): ...
