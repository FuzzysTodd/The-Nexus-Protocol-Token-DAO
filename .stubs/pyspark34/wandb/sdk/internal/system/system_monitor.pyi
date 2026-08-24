from .assets.asset_registry import asset_registry as asset_registry
from .assets.interfaces import Asset as Asset, Interface as Interface
from .assets.open_metrics import OpenMetrics as OpenMetrics
from .system_info import SystemInfo as SystemInfo
from _typeshed import Incomplete
from wandb.proto.wandb_telemetry_pb2 import TelemetryRecord as TelemetryRecord
from wandb.sdk.interface.interface import FilesDict as FilesDict
from wandb.sdk.internal.settings_static import SettingsStatic as SettingsStatic

logger: Incomplete

class AssetInterface:
    metrics_queue: Incomplete
    telemetry_queue: Incomplete
    def __init__(self) -> None: ...
    def publish_stats(self, stats: dict) -> None: ...
    def publish_files(self, files_dict: FilesDict) -> None: ...

class SystemMonitor:
    PUBLISHING_INTERVAL_DELAY_FACTOR: int
    settings: Incomplete
    publishing_interval: Incomplete
    join_assets: Incomplete
    backend_interface: Incomplete
    asset_interface: Incomplete
    assets: Incomplete
    system_info: Incomplete
    buffer: Incomplete
    def __init__(self, settings: SettingsStatic, interface: Interface) -> None: ...
    def aggregate_and_publish_asset_metrics(self) -> None: ...
    def publish_telemetry(self) -> None: ...
    def start(self) -> None: ...
    def finish(self) -> None: ...
    def probe(self, publish: bool = True) -> None: ...
