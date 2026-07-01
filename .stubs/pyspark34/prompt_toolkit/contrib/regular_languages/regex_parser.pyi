from _typeshed import Incomplete

__all__ = ['Repeat', 'Variable', 'Regex', 'Lookahead', 'tokenize_regex', 'parse_regex']

class Node:
    """
    Base class for all the grammar nodes.
    (You don't initialize this one.)
    """
    def __add__(self, other_node: Node) -> NodeSequence: ...
    def __or__(self, other_node: Node) -> AnyNode: ...

class AnyNode(Node):
    '''
    Union operation (OR operation) between several grammars. You don\'t
    initialize this yourself, but it\'s a result of a "Grammar1 | Grammar2"
    operation.
    '''
    children: Incomplete
    def __init__(self, children: list[Node]) -> None: ...
    def __or__(self, other_node: Node) -> AnyNode: ...

class NodeSequence(Node):
    '''
    Concatenation operation of several grammars. You don\'t initialize this
    yourself, but it\'s a result of a "Grammar1 + Grammar2" operation.
    '''
    children: Incomplete
    def __init__(self, children: list[Node]) -> None: ...
    def __add__(self, other_node: Node) -> NodeSequence: ...

class Regex(Node):
    """
    Regular expression.
    """
    regex: Incomplete
    def __init__(self, regex: str) -> None: ...

class Lookahead(Node):
    """
    Lookahead expression.
    """
    childnode: Incomplete
    negative: Incomplete
    def __init__(self, childnode: Node, negative: bool = False) -> None: ...

class Variable(Node):
    """
    Mark a variable in the regular grammar. This will be translated into a
    named group. Each variable can have his own completer, validator, etc..

    :param childnode: The grammar which is wrapped inside this variable.
    :param varname: String.
    """
    childnode: Incomplete
    varname: Incomplete
    def __init__(self, childnode: Node, varname: str = '') -> None: ...

class Repeat(Node):
    childnode: Incomplete
    min_repeat: Incomplete
    max_repeat: Incomplete
    greedy: Incomplete
    def __init__(self, childnode: Node, min_repeat: int = 0, max_repeat: int | None = None, greedy: bool = True) -> None: ...

def tokenize_regex(input: str) -> list[str]:
    """
    Takes a string, representing a regular expression as input, and tokenizes
    it.

    :param input: string, representing a regular expression.
    :returns: List of tokens.
    """
def parse_regex(regex_tokens: list[str]) -> Node:
    """
    Takes a list of tokens from the tokenizer, and returns a parse tree.
    """
