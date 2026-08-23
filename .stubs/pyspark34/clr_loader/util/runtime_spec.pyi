from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, TextIO

@dataclass
class DotnetCoreRuntimeSpec:
    """Specification of an installed .NET Core runtime"""
    name: str
    version: str
    path: Path
    @property
    def tfm(self) -> str: ...
    @property
    def floor_version(self) -> str: ...
    @property
    def runtime_config(self) -> Dict[str, Any]: ...
    def write_config(self, f: TextIO) -> None: ...
    def __init__(self, name, version, path) -> None: ...
