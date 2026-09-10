import dataclasses
from typing import List

@dataclasses.dataclass
class PropertyBag:
    """Key/value pairs that provide additional information about the object."""
    tags: List[str] | None = ...
    def __init__(self, tags) -> None: ...
