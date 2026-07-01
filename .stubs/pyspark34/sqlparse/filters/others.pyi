from sqlparse import sql as sql
from sqlparse.utils import split_unquoted_newlines as split_unquoted_newlines

class StripCommentsFilter:
    def process(self, stmt): ...

class StripWhitespaceFilter:
    def process(self, stmt, depth: int = 0): ...

class SpacesAroundOperatorsFilter:
    def process(self, stmt): ...

class SerializerUnicode:
    @staticmethod
    def process(stmt): ...
