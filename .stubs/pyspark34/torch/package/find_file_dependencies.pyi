import ast
from _typeshed import Incomplete
from typing import List, Tuple

class _ExtractModuleReferences(ast.NodeVisitor):
    """
    Extract the list of global variables a block of code will read and write
    """
    @classmethod
    def run(cls, src: str, package: str) -> List[Tuple[str, str | None]]: ...
    package: Incomplete
    references: Incomplete
    def __init__(self, package) -> None: ...
    def visit_Import(self, node) -> None: ...
    def visit_ImportFrom(self, node) -> None: ...
    def visit_Call(self, node) -> None: ...

find_files_source_depends_on: Incomplete
