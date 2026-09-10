from ..backend_config import BackendConfig
from .custom_config import FuseCustomConfig
from .fuse_handler import FuseHandler as FuseHandler
from torch.fx import GraphModule
from typing import Any, Dict

__all__ = ['fuse', 'FuseHandler']

def fuse(model: GraphModule, is_qat: bool, fuse_custom_config: FuseCustomConfig | Dict[str, Any] | None = None, backend_config: BackendConfig | Dict[str, Any] | None = None) -> GraphModule: ...
