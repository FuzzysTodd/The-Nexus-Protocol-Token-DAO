from ..base import ConfigBase
from dataclasses import dataclass
from typing_extensions import Literal

__all__ = ['K8sStorageConfig', 'K8sAzureStorageConfig', 'K8sNfsConfig']

@dataclass(init=False)
class K8sStorageConfig(ConfigBase):
    storage_type: str
    azure_account: str | None = ...
    azure_share: str | None = ...
    key_vault_name: str | None = ...
    key_vault_key: str | None = ...
    server: str | None = ...
    path: str | None = ...

@dataclass(init=False)
class K8sNfsConfig(K8sStorageConfig):
    storage: Literal['nfs'] = ...
    server: str
    path: str

@dataclass(init=False)
class K8sAzureStorageConfig(K8sStorageConfig):
    storage: Literal['azureStorage'] = ...
    azure_account: str
    azure_share: str
    key_vault_name: str
    key_vault_key: str
