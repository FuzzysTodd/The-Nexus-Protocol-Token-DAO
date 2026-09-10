from _typeshed import Incomplete
from click import ParamType

class WorkspaceLanguage:
    SCALA: str
    PYTHON: str
    SQL: str
    R: str
    ALL: Incomplete
    EXTENSIONS: Incomplete
    @classmethod
    def to_language_and_format(cls, path): ...
    @classmethod
    def to_extension(cls, language): ...
    @classmethod
    def get_extension(cls, path): ...

class LanguageClickType(ParamType):
    name: str
    def convert(self, value, param, ctx): ...

class WorkspaceFormat:
    SOURCE: str
    HTML: str
    JUPYTER: str
    DBC: str
    ALL: Incomplete

class FormatClickType(ParamType):
    name: str
    def convert(self, value, param, ctx): ...
