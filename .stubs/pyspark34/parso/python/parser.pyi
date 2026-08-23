from _typeshed import Incomplete
from parso.parser import BaseParser as BaseParser
from parso.python import tree as tree
from parso.python.token import PythonTokenTypes as PythonTokenTypes

NAME: Incomplete
INDENT: Incomplete
DEDENT: Incomplete

class Parser(BaseParser):
    """
    This class is used to parse a Python file, it then divides them into a
    class structure of different scopes.

    :param pgen_grammar: The grammar object of pgen2. Loaded by load_grammar.
    """
    node_map: Incomplete
    default_node = tree.PythonNode
    syntax_errors: Incomplete
    def __init__(self, pgen_grammar, error_recovery: bool = True, start_nonterminal: str = 'file_input') -> None: ...
    def parse(self, tokens): ...
    def convert_node(self, nonterminal, children):
        """
        Convert raw node information to a PythonBaseNode instance.

        This is passed to the parser driver which calls it whenever a reduction of a
        grammar rule produces a new complete node, so that the tree is build
        strictly bottom-up.
        """
    def convert_leaf(self, type, value, prefix, start_pos): ...
    def error_recovery(self, token): ...
