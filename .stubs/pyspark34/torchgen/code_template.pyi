from _typeshed import Incomplete
from typing import Mapping

class CodeTemplate:
    substitution_str: str
    substitution: Incomplete
    pattern: str
    filename: str
    @staticmethod
    def from_file(filename: str) -> CodeTemplate: ...
    def __init__(self, pattern: str, filename: str = '') -> None: ...
    def substitute(self, env: Mapping[str, object] | None = None, **kwargs: object) -> str: ...
