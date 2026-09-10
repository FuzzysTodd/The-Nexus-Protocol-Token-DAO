from .service_discovery import get_fabric_env_config as get_fabric_env_config
from _typeshed import Incomplete
from typing import Dict

kusto_logger: Incomplete
FABRIC_FAKE_TELEMETRY_REPORT_CALLS: str

def fire_and_forget(f): ...
def report_usage_telemetry(feature_name: str, activity_name: str, attributes: Dict[str, str] = {}): ...
