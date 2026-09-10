from .config import BaseConfig as BaseConfig, Extra as Extra
from .fields import ModelField as ModelField
from .main import BaseModel as BaseModel
from .typing import StrPath as StrPath, display_as_type as display_as_type, get_origin as get_origin, is_union as is_union
from .utils import deep_update as deep_update, path_type as path_type, sequence_like as sequence_like
from _typeshed import Incomplete
from pathlib import Path
from typing import Any, ClassVar, Dict, List, Mapping, Tuple, Type

env_file_sentinel: Incomplete
SettingsSourceCallable: Incomplete
DotenvType = StrPath | List[StrPath] | Tuple[StrPath, ...]

class SettingsError(ValueError): ...

class BaseSettings(BaseModel):
    """
    Base class for settings, allowing values to be overridden by environment variables.

    This is useful in production for secrets you do not wish to save in code, it plays nicely with docker(-compose),
    Heroku and any 12 factor app design.
    """
    def __init__(__pydantic_self__, _env_file: DotenvType | None = ..., _env_file_encoding: str | None = None, _env_nested_delimiter: str | None = None, _secrets_dir: StrPath | None = None, **values: Any) -> None: ...
    class Config(BaseConfig):
        env_prefix: str
        env_file: DotenvType | None
        env_file_encoding: str | None
        env_nested_delimiter: str | None
        secrets_dir: StrPath | None
        validate_all: bool
        extra: Extra
        arbitrary_types_allowed: bool
        case_sensitive: bool
        @classmethod
        def prepare_field(cls, field: ModelField) -> None: ...
        @classmethod
        def customise_sources(cls, init_settings: SettingsSourceCallable, env_settings: SettingsSourceCallable, file_secret_settings: SettingsSourceCallable) -> Tuple[SettingsSourceCallable, ...]: ...
        @classmethod
        def parse_env_var(cls, field_name: str, raw_val: str) -> Any: ...
    __config__: ClassVar[Type[Config]]

class InitSettingsSource:
    init_kwargs: Incomplete
    def __init__(self, init_kwargs: Dict[str, Any]) -> None: ...
    def __call__(self, settings: BaseSettings) -> Dict[str, Any]: ...

class EnvSettingsSource:
    env_file: Incomplete
    env_file_encoding: Incomplete
    env_nested_delimiter: Incomplete
    env_prefix_len: Incomplete
    def __init__(self, env_file: DotenvType | None, env_file_encoding: str | None, env_nested_delimiter: str | None = None, env_prefix_len: int = 0) -> None: ...
    def __call__(self, settings: BaseSettings) -> Dict[str, Any]:
        """
        Build environment variables suitable for passing to the Model.
        """
    def field_is_complex(self, field: ModelField) -> Tuple[bool, bool]:
        """
        Find out if a field is complex, and if so whether JSON errors should be ignored
        """
    def explode_env_vars(self, field: ModelField, env_vars: Mapping[str, str | None]) -> Dict[str, Any]:
        """
        Process env_vars and extract the values of keys containing env_nested_delimiter into nested dictionaries.

        This is applied to a single field, hence filtering by env_var prefix.
        """

class SecretsSettingsSource:
    secrets_dir: Incomplete
    def __init__(self, secrets_dir: StrPath | None) -> None: ...
    def __call__(self, settings: BaseSettings) -> Dict[str, Any]:
        '''
        Build fields from "secrets" files.
        '''

def read_env_file(file_path: StrPath, *, encoding: str = None, case_sensitive: bool = False) -> Dict[str, str | None]: ...
def find_case_path(dir_path: Path, file_name: str, case_sensitive: bool) -> Path | None:
    """
    Find a file within path's directory matching filename, optionally ignoring case.
    """
