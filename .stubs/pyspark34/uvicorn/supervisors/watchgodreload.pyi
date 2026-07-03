from _typeshed import Incomplete
from pathlib import Path
from socket import socket
from typing import Callable, List
from uvicorn.config import Config as Config
from uvicorn.supervisors.basereload import BaseReload as BaseReload
from watchgod import DefaultWatcher

DirEntry: Incomplete
logger: Incomplete

class CustomWatcher(DefaultWatcher):
    includes: Incomplete
    excludes: Incomplete
    watched_dirs: Incomplete
    watched_files: Incomplete
    dirs_includes: Incomplete
    dirs_excludes: Incomplete
    resolved_root: Incomplete
    def __init__(self, root_path: Path, config: Config) -> None: ...
    def should_watch_file(self, entry: DirEntry) -> bool: ...
    def should_watch_dir(self, entry: DirEntry) -> bool: ...

class WatchGodReload(BaseReload):
    reloader_name: str
    watchers: Incomplete
    def __init__(self, config: Config, target: Callable[[List[socket] | None], None], sockets: List[socket]) -> None: ...
    def should_restart(self) -> List[Path] | None: ...
