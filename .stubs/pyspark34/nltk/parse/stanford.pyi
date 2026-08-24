from _typeshed import Incomplete
from nltk.internals import config_java as config_java, find_jar_iter as find_jar_iter, find_jars_within_path as find_jars_within_path, java as java
from nltk.parse.api import ParserI as ParserI
from nltk.parse.dependencygraph import DependencyGraph as DependencyGraph
from nltk.tree import Tree as Tree

class GenericStanfordParser(ParserI):
    """Interface to the Stanford Parser"""
    model_path: Incomplete
    corenlp_options: Incomplete
    java_options: Incomplete
    def __init__(self, path_to_jar: Incomplete | None = None, path_to_models_jar: Incomplete | None = None, model_path: str = 'edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz', encoding: str = 'utf8', verbose: bool = False, java_options: str = '-mx4g', corenlp_options: str = '') -> None: ...
    def parse_sents(self, sentences, verbose: bool = False):
        """
        Use StanfordParser to parse multiple sentences. Takes multiple sentences as a
        list where each sentence is a list of words.
        Each sentence will be automatically tagged with this StanfordParser instance's
        tagger.
        If whitespaces exists inside a token, then the token will be treated as
        separate tokens.

        :param sentences: Input sentences to parse
        :type sentences: list(list(str))
        :rtype: iter(iter(Tree))
        """
    def raw_parse(self, sentence, verbose: bool = False):
        """
        Use StanfordParser to parse a sentence. Takes a sentence as a string;
        before parsing, it will be automatically tokenized and tagged by
        the Stanford Parser.

        :param sentence: Input sentence to parse
        :type sentence: str
        :rtype: iter(Tree)
        """
    def raw_parse_sents(self, sentences, verbose: bool = False):
        """
        Use StanfordParser to parse multiple sentences. Takes multiple sentences as a
        list of strings.
        Each sentence will be automatically tokenized and tagged by the Stanford Parser.

        :param sentences: Input sentences to parse
        :type sentences: list(str)
        :rtype: iter(iter(Tree))
        """
    def tagged_parse(self, sentence, verbose: bool = False):
        """
        Use StanfordParser to parse a sentence. Takes a sentence as a list of
        (word, tag) tuples; the sentence must have already been tokenized and
        tagged.

        :param sentence: Input sentence to parse
        :type sentence: list(tuple(str, str))
        :rtype: iter(Tree)
        """
    def tagged_parse_sents(self, sentences, verbose: bool = False):
        """
        Use StanfordParser to parse multiple sentences. Takes multiple sentences
        where each sentence is a list of (word, tag) tuples.
        The sentences must have already been tokenized and tagged.

        :param sentences: Input sentences to parse
        :type sentences: list(list(tuple(str, str)))
        :rtype: iter(iter(Tree))
        """

class StanfordParser(GenericStanfordParser):
    '''
    >>> parser=StanfordParser(
    ...     model_path="edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz"
    ... ) # doctest: +SKIP

    >>> list(parser.raw_parse("the quick brown fox jumps over the lazy dog")) # doctest: +NORMALIZE_WHITESPACE +SKIP
    [Tree(\'ROOT\', [Tree(\'NP\', [Tree(\'NP\', [Tree(\'DT\', [\'the\']), Tree(\'JJ\', [\'quick\']), Tree(\'JJ\', [\'brown\']),
    Tree(\'NN\', [\'fox\'])]), Tree(\'NP\', [Tree(\'NP\', [Tree(\'NNS\', [\'jumps\'])]), Tree(\'PP\', [Tree(\'IN\', [\'over\']),
    Tree(\'NP\', [Tree(\'DT\', [\'the\']), Tree(\'JJ\', [\'lazy\']), Tree(\'NN\', [\'dog\'])])])])])])]

    >>> sum([list(dep_graphs) for dep_graphs in parser.raw_parse_sents((
    ...     "the quick brown fox jumps over the lazy dog",
    ...     "the quick grey wolf jumps over the lazy fox"
    ... ))], []) # doctest: +NORMALIZE_WHITESPACE +SKIP
    [Tree(\'ROOT\', [Tree(\'NP\', [Tree(\'NP\', [Tree(\'DT\', [\'the\']), Tree(\'JJ\', [\'quick\']), Tree(\'JJ\', [\'brown\']),
    Tree(\'NN\', [\'fox\'])]), Tree(\'NP\', [Tree(\'NP\', [Tree(\'NNS\', [\'jumps\'])]), Tree(\'PP\', [Tree(\'IN\', [\'over\']),
    Tree(\'NP\', [Tree(\'DT\', [\'the\']), Tree(\'JJ\', [\'lazy\']), Tree(\'NN\', [\'dog\'])])])])])]), Tree(\'ROOT\', [Tree(\'NP\',
    [Tree(\'NP\', [Tree(\'DT\', [\'the\']), Tree(\'JJ\', [\'quick\']), Tree(\'JJ\', [\'grey\']), Tree(\'NN\', [\'wolf\'])]), Tree(\'NP\',
    [Tree(\'NP\', [Tree(\'NNS\', [\'jumps\'])]), Tree(\'PP\', [Tree(\'IN\', [\'over\']), Tree(\'NP\', [Tree(\'DT\', [\'the\']),
    Tree(\'JJ\', [\'lazy\']), Tree(\'NN\', [\'fox\'])])])])])])]

    >>> sum([list(dep_graphs) for dep_graphs in parser.parse_sents((
    ...     "I \'m a dog".split(),
    ...     "This is my friends \' cat ( the tabby )".split(),
    ... ))], []) # doctest: +NORMALIZE_WHITESPACE +SKIP
    [Tree(\'ROOT\', [Tree(\'S\', [Tree(\'NP\', [Tree(\'PRP\', [\'I\'])]), Tree(\'VP\', [Tree(\'VBP\', ["\'m"]),
    Tree(\'NP\', [Tree(\'DT\', [\'a\']), Tree(\'NN\', [\'dog\'])])])])]), Tree(\'ROOT\', [Tree(\'S\', [Tree(\'NP\',
    [Tree(\'DT\', [\'This\'])]), Tree(\'VP\', [Tree(\'VBZ\', [\'is\']), Tree(\'NP\', [Tree(\'NP\', [Tree(\'NP\', [Tree(\'PRP$\', [\'my\']),
    Tree(\'NNS\', [\'friends\']), Tree(\'POS\', ["\'"])]), Tree(\'NN\', [\'cat\'])]), Tree(\'PRN\', [Tree(\'-LRB-\', [Tree(\'\', []),
    Tree(\'NP\', [Tree(\'DT\', [\'the\']), Tree(\'NN\', [\'tabby\'])]), Tree(\'-RRB-\', [])])])])])])])]

    >>> sum([list(dep_graphs) for dep_graphs in parser.tagged_parse_sents((
    ...     (
    ...         ("The", "DT"),
    ...         ("quick", "JJ"),
    ...         ("brown", "JJ"),
    ...         ("fox", "NN"),
    ...         ("jumped", "VBD"),
    ...         ("over", "IN"),
    ...         ("the", "DT"),
    ...         ("lazy", "JJ"),
    ...         ("dog", "NN"),
    ...         (".", "."),
    ...     ),
    ... ))],[]) # doctest: +NORMALIZE_WHITESPACE +SKIP
    [Tree(\'ROOT\', [Tree(\'S\', [Tree(\'NP\', [Tree(\'DT\', [\'The\']), Tree(\'JJ\', [\'quick\']), Tree(\'JJ\', [\'brown\']),
    Tree(\'NN\', [\'fox\'])]), Tree(\'VP\', [Tree(\'VBD\', [\'jumped\']), Tree(\'PP\', [Tree(\'IN\', [\'over\']), Tree(\'NP\',
    [Tree(\'DT\', [\'the\']), Tree(\'JJ\', [\'lazy\']), Tree(\'NN\', [\'dog\'])])])]), Tree(\'.\', [\'.\'])])])]
    '''
    def __init__(self, *args, **kwargs) -> None: ...

class StanfordDependencyParser(GenericStanfordParser):
    '''
    >>> dep_parser=StanfordDependencyParser(
    ...     model_path="edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz"
    ... ) # doctest: +SKIP

    >>> [parse.tree() for parse in dep_parser.raw_parse("The quick brown fox jumps over the lazy dog.")] # doctest: +NORMALIZE_WHITESPACE +SKIP
    [Tree(\'jumps\', [Tree(\'fox\', [\'The\', \'quick\', \'brown\']), Tree(\'dog\', [\'over\', \'the\', \'lazy\'])])]

    >>> [list(parse.triples()) for parse in dep_parser.raw_parse("The quick brown fox jumps over the lazy dog.")] # doctest: +NORMALIZE_WHITESPACE +SKIP
    [[((u\'jumps\', u\'VBZ\'), u\'nsubj\', (u\'fox\', u\'NN\')), ((u\'fox\', u\'NN\'), u\'det\', (u\'The\', u\'DT\')),
    ((u\'fox\', u\'NN\'), u\'amod\', (u\'quick\', u\'JJ\')), ((u\'fox\', u\'NN\'), u\'amod\', (u\'brown\', u\'JJ\')),
    ((u\'jumps\', u\'VBZ\'), u\'nmod\', (u\'dog\', u\'NN\')), ((u\'dog\', u\'NN\'), u\'case\', (u\'over\', u\'IN\')),
    ((u\'dog\', u\'NN\'), u\'det\', (u\'the\', u\'DT\')), ((u\'dog\', u\'NN\'), u\'amod\', (u\'lazy\', u\'JJ\'))]]

    >>> sum([[parse.tree() for parse in dep_graphs] for dep_graphs in dep_parser.raw_parse_sents((
    ...     "The quick brown fox jumps over the lazy dog.",
    ...     "The quick grey wolf jumps over the lazy fox."
    ... ))], []) # doctest: +NORMALIZE_WHITESPACE +SKIP
    [Tree(\'jumps\', [Tree(\'fox\', [\'The\', \'quick\', \'brown\']), Tree(\'dog\', [\'over\', \'the\', \'lazy\'])]),
    Tree(\'jumps\', [Tree(\'wolf\', [\'The\', \'quick\', \'grey\']), Tree(\'fox\', [\'over\', \'the\', \'lazy\'])])]

    >>> sum([[parse.tree() for parse in dep_graphs] for dep_graphs in dep_parser.parse_sents((
    ...     "I \'m a dog".split(),
    ...     "This is my friends \' cat ( the tabby )".split(),
    ... ))], []) # doctest: +NORMALIZE_WHITESPACE +SKIP
    [Tree(\'dog\', [\'I\', "\'m", \'a\']), Tree(\'cat\', [\'This\', \'is\', Tree(\'friends\', [\'my\', "\'"]), Tree(\'tabby\', [\'the\'])])]

    >>> sum([[list(parse.triples()) for parse in dep_graphs] for dep_graphs in dep_parser.tagged_parse_sents((
    ...     (
    ...         ("The", "DT"),
    ...         ("quick", "JJ"),
    ...         ("brown", "JJ"),
    ...         ("fox", "NN"),
    ...         ("jumped", "VBD"),
    ...         ("over", "IN"),
    ...         ("the", "DT"),
    ...         ("lazy", "JJ"),
    ...         ("dog", "NN"),
    ...         (".", "."),
    ...     ),
    ... ))],[]) # doctest: +NORMALIZE_WHITESPACE +SKIP
    [[((u\'jumped\', u\'VBD\'), u\'nsubj\', (u\'fox\', u\'NN\')), ((u\'fox\', u\'NN\'), u\'det\', (u\'The\', u\'DT\')),
    ((u\'fox\', u\'NN\'), u\'amod\', (u\'quick\', u\'JJ\')), ((u\'fox\', u\'NN\'), u\'amod\', (u\'brown\', u\'JJ\')),
    ((u\'jumped\', u\'VBD\'), u\'nmod\', (u\'dog\', u\'NN\')), ((u\'dog\', u\'NN\'), u\'case\', (u\'over\', u\'IN\')),
    ((u\'dog\', u\'NN\'), u\'det\', (u\'the\', u\'DT\')), ((u\'dog\', u\'NN\'), u\'amod\', (u\'lazy\', u\'JJ\'))]]

    '''
    def __init__(self, *args, **kwargs) -> None: ...

class StanfordNeuralDependencyParser(GenericStanfordParser):
    '''
    >>> from nltk.parse.stanford import StanfordNeuralDependencyParser # doctest: +SKIP
    >>> dep_parser=StanfordNeuralDependencyParser(java_options=\'-mx4g\')# doctest: +SKIP

    >>> [parse.tree() for parse in dep_parser.raw_parse("The quick brown fox jumps over the lazy dog.")] # doctest: +NORMALIZE_WHITESPACE +SKIP
    [Tree(\'jumps\', [Tree(\'fox\', [\'The\', \'quick\', \'brown\']), Tree(\'dog\', [\'over\', \'the\', \'lazy\']), \'.\'])]

    >>> [list(parse.triples()) for parse in dep_parser.raw_parse("The quick brown fox jumps over the lazy dog.")] # doctest: +NORMALIZE_WHITESPACE +SKIP
    [[((u\'jumps\', u\'VBZ\'), u\'nsubj\', (u\'fox\', u\'NN\')), ((u\'fox\', u\'NN\'), u\'det\',
    (u\'The\', u\'DT\')), ((u\'fox\', u\'NN\'), u\'amod\', (u\'quick\', u\'JJ\')), ((u\'fox\', u\'NN\'),
    u\'amod\', (u\'brown\', u\'JJ\')), ((u\'jumps\', u\'VBZ\'), u\'nmod\', (u\'dog\', u\'NN\')),
    ((u\'dog\', u\'NN\'), u\'case\', (u\'over\', u\'IN\')), ((u\'dog\', u\'NN\'), u\'det\',
    (u\'the\', u\'DT\')), ((u\'dog\', u\'NN\'), u\'amod\', (u\'lazy\', u\'JJ\')), ((u\'jumps\', u\'VBZ\'),
    u\'punct\', (u\'.\', u\'.\'))]]

    >>> sum([[parse.tree() for parse in dep_graphs] for dep_graphs in dep_parser.raw_parse_sents((
    ...     "The quick brown fox jumps over the lazy dog.",
    ...     "The quick grey wolf jumps over the lazy fox."
    ... ))], []) # doctest: +NORMALIZE_WHITESPACE +SKIP
    [Tree(\'jumps\', [Tree(\'fox\', [\'The\', \'quick\', \'brown\']), Tree(\'dog\', [\'over\',
    \'the\', \'lazy\']), \'.\']), Tree(\'jumps\', [Tree(\'wolf\', [\'The\', \'quick\', \'grey\']),
    Tree(\'fox\', [\'over\', \'the\', \'lazy\']), \'.\'])]

    >>> sum([[parse.tree() for parse in dep_graphs] for dep_graphs in dep_parser.parse_sents((
    ...     "I \'m a dog".split(),
    ...     "This is my friends \' cat ( the tabby )".split(),
    ... ))], []) # doctest: +NORMALIZE_WHITESPACE +SKIP
    [Tree(\'dog\', [\'I\', "\'m", \'a\']), Tree(\'cat\', [\'This\', \'is\', Tree(\'friends\',
    [\'my\', "\'"]), Tree(\'tabby\', [\'-LRB-\', \'the\', \'-RRB-\'])])]
    '''
    def __init__(self, *args, **kwargs) -> None: ...
    def tagged_parse_sents(self, sentences, verbose: bool = False) -> None:
        """
        Currently unimplemented because the neural dependency parser (and
        the StanfordCoreNLP pipeline class) doesn't support passing in pre-
        tagged tokens.
        """
