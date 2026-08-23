from _typeshed import Incomplete
from nltk.featstruct import FeatDict
from nltk.probability import ImmutableProbabilisticMixIn

__all__ = ['Nonterminal', 'nonterminals', 'CFG', 'Production', 'PCFG', 'ProbabilisticProduction', 'DependencyGrammar', 'DependencyProduction', 'ProbabilisticDependencyGrammar', 'induce_pcfg', 'read_grammar']

class Nonterminal:
    '''
    A non-terminal symbol for a context free grammar.  ``Nonterminal``
    is a wrapper class for node values; it is used by ``Production``
    objects to distinguish node values from leaf values.
    The node value that is wrapped by a ``Nonterminal`` is known as its
    "symbol".  Symbols are typically strings representing phrasal
    categories (such as ``"NP"`` or ``"VP"``).  However, more complex
    symbol types are sometimes used (e.g., for lexicalized grammars).
    Since symbols are node values, they must be immutable and
    hashable.  Two ``Nonterminals`` are considered equal if their
    symbols are equal.

    :see: ``CFG``, ``Production``
    :type _symbol: any
    :ivar _symbol: The node value corresponding to this
        ``Nonterminal``.  This value must be immutable and hashable.
    '''
    def __init__(self, symbol) -> None:
        """
        Construct a new non-terminal from the given symbol.

        :type symbol: any
        :param symbol: The node value corresponding to this
            ``Nonterminal``.  This value must be immutable and
            hashable.
        """
    def symbol(self):
        """
        Return the node value corresponding to this ``Nonterminal``.

        :rtype: (any)
        """
    def __eq__(self, other):
        """
        Return True if this non-terminal is equal to ``other``.  In
        particular, return True if ``other`` is a ``Nonterminal``
        and this non-terminal's symbol is equal to ``other`` 's symbol.

        :rtype: bool
        """
    def __ne__(self, other): ...
    def __lt__(self, other): ...
    def __hash__(self): ...
    def __div__(self, rhs):
        """
        Return a new nonterminal whose symbol is ``A/B``, where ``A`` is
        the symbol for this nonterminal, and ``B`` is the symbol for rhs.

        :param rhs: The nonterminal used to form the right hand side
            of the new nonterminal.
        :type rhs: Nonterminal
        :rtype: Nonterminal
        """
    def __truediv__(self, rhs):
        """
        Return a new nonterminal whose symbol is ``A/B``, where ``A`` is
        the symbol for this nonterminal, and ``B`` is the symbol for rhs.
        This function allows use of the slash ``/`` operator with
        the future import of division.

        :param rhs: The nonterminal used to form the right hand side
            of the new nonterminal.
        :type rhs: Nonterminal
        :rtype: Nonterminal
        """

def nonterminals(symbols):
    """
    Given a string containing a list of symbol names, return a list of
    ``Nonterminals`` constructed from those symbols.

    :param symbols: The symbol name string.  This string can be
        delimited by either spaces or commas.
    :type symbols: str
    :return: A list of ``Nonterminals`` constructed from the symbol
        names given in ``symbols``.  The ``Nonterminals`` are sorted
        in the same order as the symbols names.
    :rtype: list(Nonterminal)
    """

class FeatStructNonterminal(FeatDict, Nonterminal):
    """A feature structure that's also a nonterminal.  It acts as its
    own symbol, and automatically freezes itself when hashed."""
    def __hash__(self): ...
    def symbol(self): ...

class Production:
    '''
    A grammar production.  Each production maps a single symbol
    on the "left-hand side" to a sequence of symbols on the
    "right-hand side".  (In the case of context-free productions,
    the left-hand side must be a ``Nonterminal``, and the right-hand
    side is a sequence of terminals and ``Nonterminals``.)
    "terminals" can be any immutable hashable object that is
    not a ``Nonterminal``.  Typically, terminals are strings
    representing words, such as ``"dog"`` or ``"under"``.

    :see: ``CFG``
    :see: ``DependencyGrammar``
    :see: ``Nonterminal``
    :type _lhs: Nonterminal
    :ivar _lhs: The left-hand side of the production.
    :type _rhs: tuple(Nonterminal, terminal)
    :ivar _rhs: The right-hand side of the production.
    '''
    def __init__(self, lhs, rhs) -> None:
        """
        Construct a new ``Production``.

        :param lhs: The left-hand side of the new ``Production``.
        :type lhs: Nonterminal
        :param rhs: The right-hand side of the new ``Production``.
        :type rhs: sequence(Nonterminal and terminal)
        """
    def lhs(self):
        """
        Return the left-hand side of this ``Production``.

        :rtype: Nonterminal
        """
    def rhs(self):
        """
        Return the right-hand side of this ``Production``.

        :rtype: sequence(Nonterminal and terminal)
        """
    def __len__(self) -> int:
        """
        Return the length of the right-hand side.

        :rtype: int
        """
    def is_nonlexical(self):
        """
        Return True if the right-hand side only contains ``Nonterminals``

        :rtype: bool
        """
    def is_lexical(self):
        """
        Return True if the right-hand contain at least one terminal token.

        :rtype: bool
        """
    def __eq__(self, other):
        """
        Return True if this ``Production`` is equal to ``other``.

        :rtype: bool
        """
    def __ne__(self, other): ...
    def __lt__(self, other): ...
    def __hash__(self):
        """
        Return a hash value for the ``Production``.

        :rtype: int
        """

class DependencyProduction(Production):
    """
    A dependency grammar production.  Each production maps a single
    head word to an unordered list of one or more modifier words.
    """

class ProbabilisticProduction(Production, ImmutableProbabilisticMixIn):
    """
    A probabilistic context free grammar production.
    A PCFG ``ProbabilisticProduction`` is essentially just a ``Production`` that
    has an associated probability, which represents how likely it is that
    this production will be used.  In particular, the probability of a
    ``ProbabilisticProduction`` records the likelihood that its right-hand side is
    the correct instantiation for any given occurrence of its left-hand side.

    :see: ``Production``
    """
    def __init__(self, lhs, rhs, **prob) -> None:
        """
        Construct a new ``ProbabilisticProduction``.

        :param lhs: The left-hand side of the new ``ProbabilisticProduction``.
        :type lhs: Nonterminal
        :param rhs: The right-hand side of the new ``ProbabilisticProduction``.
        :type rhs: sequence(Nonterminal and terminal)
        :param prob: Probability parameters of the new ``ProbabilisticProduction``.
        """
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __hash__(self): ...

class CFG:
    """
    A context-free grammar.  A grammar consists of a start state and
    a set of productions.  The set of terminals and nonterminals is
    implicitly specified by the productions.

    If you need efficient key-based access to productions, you
    can use a subclass to implement it.
    """
    def __init__(self, start, productions, calculate_leftcorners: bool = True) -> None:
        """
        Create a new context-free grammar, from the given start state
        and set of ``Production`` instances.

        :param start: The start symbol
        :type start: Nonterminal
        :param productions: The list of productions that defines the grammar
        :type productions: list(Production)
        :param calculate_leftcorners: False if we don't want to calculate the
            leftcorner relation. In that case, some optimized chart parsers won't work.
        :type calculate_leftcorners: bool
        """
    @classmethod
    def fromstring(cls, input, encoding: Incomplete | None = None):
        """
        Return the grammar instance corresponding to the input string(s).

        :param input: a grammar, either in the form of a string or as a list of strings.
        """
    def start(self):
        """
        Return the start symbol of the grammar

        :rtype: Nonterminal
        """
    def productions(self, lhs: Incomplete | None = None, rhs: Incomplete | None = None, empty: bool = False):
        """
        Return the grammar productions, filtered by the left-hand side
        or the first item in the right-hand side.

        :param lhs: Only return productions with the given left-hand side.
        :param rhs: Only return productions with the given first item
            in the right-hand side.
        :param empty: Only return productions with an empty right-hand side.
        :return: A list of productions matching the given constraints.
        :rtype: list(Production)
        """
    def leftcorners(self, cat):
        """
        Return the set of all nonterminals that the given nonterminal
        can start with, including itself.

        This is the reflexive, transitive closure of the immediate
        leftcorner relation:  (A > B)  iff  (A -> B beta)

        :param cat: the parent of the leftcorners
        :type cat: Nonterminal
        :return: the set of all leftcorners
        :rtype: set(Nonterminal)
        """
    def is_leftcorner(self, cat, left):
        """
        True if left is a leftcorner of cat, where left can be a
        terminal or a nonterminal.

        :param cat: the parent of the leftcorner
        :type cat: Nonterminal
        :param left: the suggested leftcorner
        :type left: Terminal or Nonterminal
        :rtype: bool
        """
    def leftcorner_parents(self, cat):
        """
        Return the set of all nonterminals for which the given category
        is a left corner. This is the inverse of the leftcorner relation.

        :param cat: the suggested leftcorner
        :type cat: Nonterminal
        :return: the set of all parents to the leftcorner
        :rtype: set(Nonterminal)
        """
    def check_coverage(self, tokens) -> None:
        """
        Check whether the grammar rules cover the given list of tokens.
        If not, then raise an exception.

        :type tokens: list(str)
        """
    def is_lexical(self):
        """
        Return True if all productions are lexicalised.
        """
    def is_nonlexical(self):
        '''
        Return True if all lexical rules are "preterminals", that is,
        unary rules which can be separated in a preprocessing step.

        This means that all productions are of the forms
        A -> B1 ... Bn (n>=0), or A -> "s".

        Note: is_lexical() and is_nonlexical() are not opposites.
        There are grammars which are neither, and grammars which are both.
        '''
    def min_len(self):
        """
        Return the right-hand side length of the shortest grammar production.
        """
    def max_len(self):
        """
        Return the right-hand side length of the longest grammar production.
        """
    def is_nonempty(self):
        """
        Return True if there are no empty productions.
        """
    def is_binarised(self):
        """
        Return True if all productions are at most binary.
        Note that there can still be empty and unary productions.
        """
    def is_flexible_chomsky_normal_form(self):
        '''
        Return True if all productions are of the forms
        A -> B C, A -> B, or A -> "s".
        '''
    def is_chomsky_normal_form(self):
        '''
        Return True if the grammar is of Chomsky Normal Form, i.e. all productions
        are of the form A -> B C, or A -> "s".
        '''
    def chomsky_normal_form(self, new_token_padding: str = '@$@', flexible: bool = False):
        """
        Returns a new Grammar that is in chomsky normal

        :param: new_token_padding
            Customise new rule formation during binarisation
        """
    @classmethod
    def remove_unitary_rules(cls, grammar):
        """
        Remove nonlexical unitary rules and convert them to
        lexical
        """
    @classmethod
    def binarize(cls, grammar, padding: str = '@$@'):
        """
        Convert all non-binary rules into binary by introducing
        new tokens.
        Example::

            Original:
                A => B C D
            After Conversion:
                A => B A@$@B
                A@$@B => C D
        """
    @classmethod
    def eliminate_start(cls, grammar):
        """
        Eliminate start rule in case it appears on RHS
        Example: S -> S0 S1 and S0 -> S1 S
        Then another rule S0_Sigma -> S is added
        """

class FeatureGrammar(CFG):
    """
    A feature-based grammar.  This is equivalent to a
    ``CFG`` whose nonterminals are all
    ``FeatStructNonterminal``.

    A grammar consists of a start state and a set of
    productions.  The set of terminals and nonterminals
    is implicitly specified by the productions.
    """
    def __init__(self, start, productions) -> None:
        """
        Create a new feature-based grammar, from the given start
        state and set of ``Productions``.

        :param start: The start symbol
        :type start: FeatStructNonterminal
        :param productions: The list of productions that defines the grammar
        :type productions: list(Production)
        """
    @classmethod
    def fromstring(cls, input, features: Incomplete | None = None, logic_parser: Incomplete | None = None, fstruct_reader: Incomplete | None = None, encoding: Incomplete | None = None):
        """
        Return a feature structure based grammar.

        :param input: a grammar, either in the form of a string or else
        as a list of strings.
        :param features: a tuple of features (default: SLASH, TYPE)
        :param logic_parser: a parser for lambda-expressions,
        by default, ``LogicParser()``
        :param fstruct_reader: a feature structure parser
        (only if features and logic_parser is None)
        """
    def productions(self, lhs: Incomplete | None = None, rhs: Incomplete | None = None, empty: bool = False):
        """
        Return the grammar productions, filtered by the left-hand side
        or the first item in the right-hand side.

        :param lhs: Only return productions with the given left-hand side.
        :param rhs: Only return productions with the given first item
            in the right-hand side.
        :param empty: Only return productions with an empty right-hand side.
        :rtype: list(Production)
        """
    def leftcorners(self, cat) -> None:
        '''
        Return the set of all words that the given category can start with.
        Also called the "first set" in compiler construction.
        '''
    def leftcorner_parents(self, cat) -> None:
        """
        Return the set of all categories for which the given category
        is a left corner.
        """

class FeatureValueType:
    '''
    A helper class for ``FeatureGrammars``, designed to be different
    from ordinary strings.  This is to stop the ``FeatStruct``
    ``FOO[]`` from being compare equal to the terminal "FOO".
    '''
    def __init__(self, value) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __lt__(self, other): ...
    def __hash__(self): ...

class DependencyGrammar:
    """
    A dependency grammar.  A DependencyGrammar consists of a set of
    productions.  Each production specifies a head/modifier relationship
    between a pair of words.
    """
    def __init__(self, productions) -> None:
        """
        Create a new dependency grammar, from the set of ``Productions``.

        :param productions: The list of productions that defines the grammar
        :type productions: list(Production)
        """
    @classmethod
    def fromstring(cls, input): ...
    def contains(self, head, mod):
        """
        :param head: A head word.
        :type head: str
        :param mod: A mod word, to test as a modifier of 'head'.
        :type mod: str

        :return: true if this ``DependencyGrammar`` contains a
            ``DependencyProduction`` mapping 'head' to 'mod'.
        :rtype: bool
        """
    def __contains__(self, head_mod) -> bool:
        """
        Return True if this ``DependencyGrammar`` contains a
        ``DependencyProduction`` mapping 'head' to 'mod'.

        :param head_mod: A tuple of a head word and a mod word,
            to test as a modifier of 'head'.
        :type head: Tuple[str, str]
        :rtype: bool
        """

class ProbabilisticDependencyGrammar:
    """ """
    def __init__(self, productions, events, tags) -> None: ...
    def contains(self, head, mod):
        """
        Return True if this ``DependencyGrammar`` contains a
        ``DependencyProduction`` mapping 'head' to 'mod'.

        :param head: A head word.
        :type head: str
        :param mod: A mod word, to test as a modifier of 'head'.
        :type mod: str
        :rtype: bool
        """

class PCFG(CFG):
    """
    A probabilistic context-free grammar.  A PCFG consists of a
    start state and a set of productions with probabilities.  The set of
    terminals and nonterminals is implicitly specified by the productions.

    PCFG productions use the ``ProbabilisticProduction`` class.
    ``PCFGs`` impose the constraint that the set of productions with
    any given left-hand-side must have probabilities that sum to 1
    (allowing for a small margin of error).

    If you need efficient key-based access to productions, you can use
    a subclass to implement it.

    :type EPSILON: float
    :cvar EPSILON: The acceptable margin of error for checking that
        productions with a given left-hand side have probabilities
        that sum to 1.
    """
    EPSILON: float
    def __init__(self, start, productions, calculate_leftcorners: bool = True) -> None:
        """
        Create a new context-free grammar, from the given start state
        and set of ``ProbabilisticProductions``.

        :param start: The start symbol
        :type start: Nonterminal
        :param productions: The list of productions that defines the grammar
        :type productions: list(Production)
        :raise ValueError: if the set of productions with any left-hand-side
            do not have probabilities that sum to a value within
            EPSILON of 1.
        :param calculate_leftcorners: False if we don't want to calculate the
            leftcorner relation. In that case, some optimized chart parsers won't work.
        :type calculate_leftcorners: bool
        """
    @classmethod
    def fromstring(cls, input, encoding: Incomplete | None = None):
        """
        Return a probabilistic context-free grammar corresponding to the
        input string(s).

        :param input: a grammar, either in the form of a string or else
             as a list of strings.
        """

def induce_pcfg(start, productions):
    """
    Induce a PCFG grammar from a list of productions.

    The probability of a production A -> B C in a PCFG is:

    |                count(A -> B C)
    |  P(B, C | A) = ---------------       where \\* is any right hand side
    |                 count(A -> \\*)

    :param start: The start symbol
    :type start: Nonterminal
    :param productions: The list of productions that defines the grammar
    :type productions: list(Production)
    """
def read_grammar(input, nonterm_parser, probabilistic: bool = False, encoding: Incomplete | None = None):
    """
    Return a pair consisting of a starting category and a list of
    ``Productions``.

    :param input: a grammar, either in the form of a string or else
        as a list of strings.
    :param nonterm_parser: a function for parsing nonterminals.
        It should take a ``(string, position)`` as argument and
        return a ``(nonterminal, position)`` as result.
    :param probabilistic: are the grammar rules probabilistic?
    :type probabilistic: bool
    :param encoding: the encoding of the grammar, if it is a binary string
    :type encoding: str
    """
