from nltk.sem import evaluate as evaluate

def parse_sents(inputs, grammar, trace: int = 0):
    """
    Convert input sentences into syntactic trees.

    :param inputs: sentences to be parsed
    :type inputs: list(str)
    :param grammar: ``FeatureGrammar`` or name of feature-based grammar
    :type grammar: nltk.grammar.FeatureGrammar
    :rtype: list(nltk.tree.Tree) or dict(list(str)): list(Tree)
    :return: a mapping from input sentences to a list of ``Tree`` instances.
    """
def root_semrep(syntree, semkey: str = 'SEM'):
    """
    Find the semantic representation at the root of a tree.

    :param syntree: a parse ``Tree``
    :param semkey: the feature label to use for the root semantics in the tree
    :return: the semantic representation at the root of a ``Tree``
    :rtype: sem.Expression
    """
def interpret_sents(inputs, grammar, semkey: str = 'SEM', trace: int = 0):
    """
    Add the semantic representation to each syntactic parse tree
    of each input sentence.

    :param inputs: a list of sentences
    :type inputs: list(str)
    :param grammar: ``FeatureGrammar`` or name of feature-based grammar
    :type grammar: nltk.grammar.FeatureGrammar
    :return: a mapping from sentences to lists of pairs (parse-tree, semantic-representations)
    :rtype: list(list(tuple(nltk.tree.Tree, nltk.sem.logic.ConstantExpression)))
    """
def evaluate_sents(inputs, grammar, model, assignment, trace: int = 0):
    """
    Add the truth-in-a-model value to each semantic representation
    for each syntactic parse of each input sentences.

    :param inputs: a list of sentences
    :type inputs: list(str)
    :param grammar: ``FeatureGrammar`` or name of feature-based grammar
    :type grammar: nltk.grammar.FeatureGrammar
    :return: a mapping from sentences to lists of triples (parse-tree, semantic-representations, evaluation-in-model)
    :rtype: list(list(tuple(nltk.tree.Tree, nltk.sem.logic.ConstantExpression, bool or dict(str): bool)))
    """
def demo_model0() -> None: ...
def read_sents(filename, encoding: str = 'utf8'): ...
def demo_legacy_grammar() -> None:
    """
    Check that interpret_sents() is compatible with legacy grammars that use
    a lowercase 'sem' feature.

    Define 'test.fcfg' to be the following

    """
def demo() -> None: ...
