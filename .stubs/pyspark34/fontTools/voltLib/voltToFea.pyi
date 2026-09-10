from _typeshed import Incomplete
from fontTools.feaLib import ast as ast
from fontTools.ttLib import TTFont as TTFont, TTLibError as TTLibError

log: Incomplete
TABLES: Incomplete

class MarkClassDefinition(ast.MarkClassDefinition):
    def asFea(self, indent: str = ''): ...

class Group:
    name: Incomplete
    groups: Incomplete
    def __init__(self, group) -> None: ...
    def __lt__(self, other): ...

class VoltToFea:
    def __init__(self, file_or_path, font: Incomplete | None = None) -> None: ...
    def convert(self, tables: Incomplete | None = None): ...

def main(args: Incomplete | None = None):
    """Convert MS VOLT to AFDKO feature files."""
