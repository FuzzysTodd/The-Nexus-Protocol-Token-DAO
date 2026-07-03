from _typeshed import Incomplete
from nltk.grammar import Nonterminal as Nonterminal

def generate(grammar, start: Incomplete | None = None, depth: Incomplete | None = None, n: Incomplete | None = None):
    """
    Generates an iterator of all sentences from a CFG.

    :param grammar: The Grammar used to generate sentences.
    :param start: The Nonterminal from which to start generate sentences.
    :param depth: The maximal depth of the generated tree.
    :param n: The maximum number of sentences to return.
    :return: An iterator of lists of terminal tokens.
    """

demo_grammar: str

def demo(N: int = 23) -> None: ...
