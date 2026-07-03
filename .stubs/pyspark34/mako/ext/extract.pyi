from _typeshed import Incomplete
from collections.abc import Generator
from mako import lexer as lexer, parsetree as parsetree

class MessageExtractor:
    use_bytes: bool
    def process_file(self, fileobj) -> Generator[Incomplete, Incomplete, None]: ...
    def extract_nodes(self, nodes) -> Generator[Incomplete, Incomplete, None]: ...
