from ..telemetry_utils import report_usage_telemetry as report_usage_telemetry
from .iprerun import IPrerun as IPrerun
from _typeshed import Incomplete
from importlib.machinery import ModuleSpec
from pyspark.sql.session import SparkSession as SparkSession
from typing import Any, Callable, Dict, Set

MAX_CALL_STACK_DEPTH: int
IMPORT_HOOK_FRAME_NAME: str
kusto_logger: Incomplete
FABRIC_USAGE_TELEMETRY: str
USER_FRAME_NAMES: Set[str]

def disable_usage_telemetry() -> None: ...
def enable_usage_telemetry() -> None: ...
def without_usage_telemetry(func): ...

class ModuleState:
    NOT_USED: str
    IMPORTED_BY_USER: str
    EXPLICITLY_IMPORTED_BY_USER: str
    module_name: Incomplete
    telemetry_activity_names: Incomplete
    spec: Incomplete
    getattr: Incomplete
    record_usage: Incomplete
    usage_recorded: Incomplete
    def __init__(self, module_name: str, spec: ModuleSpec | None = None, getattr: Callable[[str], Any] | None = None, record_usage: bool = True) -> None: ...

module_states: Dict[str, ModuleState]

def get_module_states(): ...
def add_user_frame_names(frame_name: str): ...
def inspect_explicit_import(frame, module_name: str) -> bool: ...

class ModuleSpecHook:
    parent_module_name: Incomplete
    def __init__(self, parent_module_name: str) -> None: ...
    def modify_spec(self, module): ...

class UsageTelemetryPrerun(IPrerun):
    package_list_with_usage_telemetry: Incomplete
    @classmethod
    def detect_synapseml_submodules(cls) -> None: ...
    @classmethod
    def detect_fabric_submodules(cls) -> None: ...
    def initialize(self, global_namespace: dict) -> None: ...
    def init_personalized_session(self, spark: SparkSession) -> None: ...
    def add_custom_magic(self, jvmMagicHelper) -> None: ...
