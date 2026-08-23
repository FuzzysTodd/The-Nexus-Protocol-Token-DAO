from _typeshed import Incomplete
from collections.abc import Generator

class _CaseFilter:
    ttype: Incomplete
    convert: Incomplete
    def __init__(self, case: Incomplete | None = None) -> None: ...
    def process(self, stream) -> Generator[Incomplete, None, None]: ...

class KeywordCaseFilter(_CaseFilter):
    ttype: Incomplete

class IdentifierCaseFilter(_CaseFilter):
    ttype: Incomplete
    def process(self, stream) -> Generator[Incomplete, None, None]: ...

class TruncateStringFilter:
    width: Incomplete
    char: Incomplete
    def __init__(self, width, char) -> None: ...
    def process(self, stream) -> Generator[Incomplete, None, None]: ...
