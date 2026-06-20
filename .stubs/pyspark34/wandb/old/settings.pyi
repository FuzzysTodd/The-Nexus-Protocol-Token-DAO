from _typeshed import Incomplete
from typing import Any
from wandb import env as env
from wandb.old import core as core
from wandb.sdk.lib import filesystem as filesystem

class Settings:
    """Global W&B settings stored under $WANDB_CONFIG_DIR/settings."""
    DEFAULT_SECTION: str
    root_dir: Incomplete
    def __init__(self, load_settings: bool = True, root_dir: str | None = None) -> None: ...
    def get(self, section: str, key: str, fallback: Any = ...) -> Any: ...
    def set(self, section, key, value, globally: bool = False, persist: bool = False) -> None:
        """Persist settings to disk if persist = True"""
    def clear(self, section, key, globally: bool = False, persist: bool = False) -> None: ...
    def items(self, section: Incomplete | None = None): ...
