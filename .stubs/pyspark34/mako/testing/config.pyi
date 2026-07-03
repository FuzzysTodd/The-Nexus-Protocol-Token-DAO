from ._config import ReadsCfg as ReadsCfg
from .helpers import make_path as make_path
from _typeshed import Incomplete
from dataclasses import dataclass
from pathlib import Path

@dataclass
class Config(ReadsCfg):
    module_base: Path
    template_base: Path
    section_header = ...
    converters = ...
    def __init__(self, module_base, template_base) -> None: ...

config: Incomplete
