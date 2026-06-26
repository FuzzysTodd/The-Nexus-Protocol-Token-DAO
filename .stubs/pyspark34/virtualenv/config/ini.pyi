from .convert import convert as convert
from _typeshed import Incomplete

class IniConfig:
    VIRTUALENV_CONFIG_FILE_ENV_VAR: str
    STATE: Incomplete
    section: str
    is_env_var: Incomplete
    config_file: Incomplete
    has_config_file: Incomplete
    config_parser: Incomplete
    has_virtualenv_section: Incomplete
    def __init__(self, env: Incomplete | None = None) -> None: ...
    def get(self, key, as_type): ...
    def __bool__(self) -> bool: ...
    @property
    def epilog(self): ...
