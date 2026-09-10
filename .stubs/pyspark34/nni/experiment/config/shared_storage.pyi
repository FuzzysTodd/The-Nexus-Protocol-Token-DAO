from .base import ConfigBase
from .utils import PathLike
from dataclasses import dataclass

__all__ = ['NfsConfig', 'AzureBlobConfig']

@dataclass(init=False)
class SharedStorageConfig(ConfigBase):
    storage_type: str
    local_mount_point: PathLike
    remote_mount_point: str
    local_mounted: str
    storage_account_name: str | None = ...
    storage_account_key: str | None = ...
    container_name: str | None = ...
    nfs_server: str | None = ...
    exported_directory: str | None = ...

@dataclass(init=False)
class NfsConfig(SharedStorageConfig):
    storage_type: str = ...
    nfs_server: str
    exported_directory: str

@dataclass(init=False)
class AzureBlobConfig(SharedStorageConfig):
    storage_type: str = ...
    storage_account_name: str
    storage_account_key: str | None = ...
    container_name: str
