from _typeshed import Incomplete
from optuna import distributions as distributions
from optuna._study_direction import StudyDirection as StudyDirection
from optuna.trial import TrialState as TrialState
from sqlalchemy import orm
from typing import Any, List

SCHEMA_VERSION: int
MAX_INDEXED_STRING_LENGTH: int
MAX_VERSION_LENGTH: int
NOT_FOUND_MSG: str
BaseModel: Any

class StudyModel(BaseModel):
    __tablename__: str
    study_id: Incomplete
    study_name: Incomplete
    @classmethod
    def find_or_raise_by_id(cls, study_id: int, session: orm.Session, for_update: bool = False) -> StudyModel: ...
    @classmethod
    def find_by_name(cls, study_name: str, session: orm.Session) -> StudyModel | None: ...
    @classmethod
    def find_or_raise_by_name(cls, study_name: str, session: orm.Session) -> StudyModel: ...

class StudyDirectionModel(BaseModel):
    __tablename__: str
    __table_args__: Any
    study_direction_id: Incomplete
    direction: Incomplete
    study_id: Incomplete
    objective: Incomplete
    study: Incomplete
    @classmethod
    def find_by_study_and_objective(cls, study: StudyModel, objective: int, session: orm.Session) -> StudyDirectionModel | None: ...
    @classmethod
    def where_study_id(cls, study_id: int, session: orm.Session) -> List['StudyDirectionModel']: ...

class StudyUserAttributeModel(BaseModel):
    __tablename__: str
    __table_args__: Any
    study_user_attribute_id: Incomplete
    study_id: Incomplete
    key: Incomplete
    value_json: Incomplete
    study: Incomplete
    @classmethod
    def find_by_study_and_key(cls, study: StudyModel, key: str, session: orm.Session) -> StudyUserAttributeModel | None: ...
    @classmethod
    def where_study_id(cls, study_id: int, session: orm.Session) -> List['StudyUserAttributeModel']: ...

class StudySystemAttributeModel(BaseModel):
    __tablename__: str
    __table_args__: Any
    study_system_attribute_id: Incomplete
    study_id: Incomplete
    key: Incomplete
    value_json: Incomplete
    study: Incomplete
    @classmethod
    def find_by_study_and_key(cls, study: StudyModel, key: str, session: orm.Session) -> StudySystemAttributeModel | None: ...
    @classmethod
    def where_study_id(cls, study_id: int, session: orm.Session) -> List['StudySystemAttributeModel']: ...

class TrialModel(BaseModel):
    __tablename__: str
    trial_id: Incomplete
    number: Incomplete
    study_id: Incomplete
    state: Incomplete
    datetime_start: Incomplete
    datetime_complete: Incomplete
    study: Incomplete
    @classmethod
    def find_max_value_trial(cls, study_id: int, objective: int, session: orm.Session) -> TrialModel: ...
    @classmethod
    def find_min_value_trial(cls, study_id: int, objective: int, session: orm.Session) -> TrialModel: ...
    @classmethod
    def find_or_raise_by_id(cls, trial_id: int, session: orm.Session, for_update: bool = False) -> TrialModel: ...
    @classmethod
    def count(cls, session: orm.Session, study: StudyModel | None = None, state: TrialState | None = None) -> int: ...
    def count_past_trials(self, session: orm.Session) -> int: ...

class TrialUserAttributeModel(BaseModel):
    __tablename__: str
    __table_args__: Any
    trial_user_attribute_id: Incomplete
    trial_id: Incomplete
    key: Incomplete
    value_json: Incomplete
    trial: Incomplete
    @classmethod
    def find_by_trial_and_key(cls, trial: TrialModel, key: str, session: orm.Session) -> TrialUserAttributeModel | None: ...
    @classmethod
    def where_trial_id(cls, trial_id: int, session: orm.Session) -> List['TrialUserAttributeModel']: ...

class TrialSystemAttributeModel(BaseModel):
    __tablename__: str
    __table_args__: Any
    trial_system_attribute_id: Incomplete
    trial_id: Incomplete
    key: Incomplete
    value_json: Incomplete
    trial: Incomplete
    @classmethod
    def find_by_trial_and_key(cls, trial: TrialModel, key: str, session: orm.Session) -> TrialSystemAttributeModel | None: ...
    @classmethod
    def where_trial_id(cls, trial_id: int, session: orm.Session) -> List['TrialSystemAttributeModel']: ...

class TrialParamModel(BaseModel):
    __tablename__: str
    __table_args__: Any
    param_id: Incomplete
    trial_id: Incomplete
    param_name: Incomplete
    param_value: Incomplete
    distribution_json: Incomplete
    trial: Incomplete
    def check_and_add(self, session: orm.Session) -> None: ...
    @classmethod
    def find_by_trial_and_param_name(cls, trial: TrialModel, param_name: str, session: orm.Session) -> TrialParamModel | None: ...
    @classmethod
    def find_or_raise_by_trial_and_param_name(cls, trial: TrialModel, param_name: str, session: orm.Session) -> TrialParamModel: ...
    @classmethod
    def where_trial_id(cls, trial_id: int, session: orm.Session) -> List['TrialParamModel']: ...

class TrialValueModel(BaseModel):
    __tablename__: str
    __table_args__: Any
    trial_value_id: Incomplete
    trial_id: Incomplete
    objective: Incomplete
    value: Incomplete
    trial: Incomplete
    @classmethod
    def find_by_trial_and_objective(cls, trial: TrialModel, objective: int, session: orm.Session) -> TrialValueModel | None: ...
    @classmethod
    def where_trial_id(cls, trial_id: int, session: orm.Session) -> List['TrialValueModel']: ...

class TrialIntermediateValueModel(BaseModel):
    __tablename__: str
    __table_args__: Any
    trial_intermediate_value_id: Incomplete
    trial_id: Incomplete
    step: Incomplete
    intermediate_value: Incomplete
    trial: Incomplete
    @classmethod
    def find_by_trial_and_step(cls, trial: TrialModel, step: int, session: orm.Session) -> TrialIntermediateValueModel | None: ...
    @classmethod
    def where_trial_id(cls, trial_id: int, session: orm.Session) -> List['TrialIntermediateValueModel']: ...

class TrialHeartbeatModel(BaseModel):
    __tablename__: str
    __table_args__: Any
    trial_heartbeat_id: Incomplete
    trial_id: Incomplete
    heartbeat: Incomplete
    trial: Incomplete
    @classmethod
    def where_trial_id(cls, trial_id: int, session: orm.Session) -> TrialHeartbeatModel | None: ...

class VersionInfoModel(BaseModel):
    __tablename__: str
    __table_args__: Any
    version_info_id: Incomplete
    schema_version: Incomplete
    library_version: Incomplete
    @classmethod
    def find(cls, session: orm.Session) -> VersionInfoModel: ...
