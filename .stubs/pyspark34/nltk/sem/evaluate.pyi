from _typeshed import Incomplete
from nltk.decorators import decorator as decorator
from nltk.sem.logic import AbstractVariableExpression as AbstractVariableExpression, AllExpression as AllExpression, AndExpression as AndExpression, ApplicationExpression as ApplicationExpression, EqualityExpression as EqualityExpression, ExistsExpression as ExistsExpression, Expression as Expression, IffExpression as IffExpression, ImpExpression as ImpExpression, IndividualVariableExpression as IndividualVariableExpression, IotaExpression as IotaExpression, LambdaExpression as LambdaExpression, NegatedExpression as NegatedExpression, OrExpression as OrExpression, Variable as Variable, is_indvar as is_indvar

class Error(Exception): ...
class Undefined(Error): ...

def trace(f, *args, **kw): ...
def is_rel(s):
    """
    Check whether a set represents a relation (of any arity).

    :param s: a set containing tuples of str elements
    :type s: set
    :rtype: bool
    """
def set2rel(s):
    """
    Convert a set containing individuals (strings or numbers) into a set of
    unary tuples. Any tuples of strings already in the set are passed through
    unchanged.

    For example:
      - set(['a', 'b']) => set([('a',), ('b',)])
      - set([3, 27]) => set([('3',), ('27',)])

    :type s: set
    :rtype: set of tuple of str
    """
def arity(rel):
    """
    Check the arity of a relation.
    :type rel: set of tuples
    :rtype: int of tuple of str
    """

class Valuation(dict):
    """
    A dictionary which represents a model-theoretic Valuation of non-logical constants.
    Keys are strings representing the constants to be interpreted, and values correspond
    to individuals (represented as strings) and n-ary relations (represented as sets of tuples
    of strings).

    An instance of ``Valuation`` will raise a KeyError exception (i.e.,
    just behave like a standard  dictionary) if indexed with an expression that
    is not in its list of symbols.
    """
    def __init__(self, xs) -> None:
        """
        :param xs: a list of (symbol, value) pairs.
        """
    def __getitem__(self, key): ...
    @property
    def domain(self):
        """Set-theoretic domain of the value-space of a Valuation."""
    @property
    def symbols(self):
        """The non-logical constants which the Valuation recognizes."""
    @classmethod
    def fromstring(cls, s): ...

def read_valuation(s, encoding: Incomplete | None = None):
    """
    Convert a valuation string into a valuation.

    :param s: a valuation string
    :type s: str
    :param encoding: the encoding of the input string, if it is binary
    :type encoding: str
    :return: a ``nltk.sem`` valuation
    :rtype: Valuation
    """

class Assignment(dict):
    """
    A dictionary which represents an assignment of values to variables.

    An assignment can only assign values from its domain.

    If an unknown expression *a* is passed to a model *M*\\ 's
    interpretation function *i*, *i* will first check whether *M*\\ 's
    valuation assigns an interpretation to *a* as a constant, and if
    this fails, *i* will delegate the interpretation of *a* to
    *g*. *g* only assigns values to individual variables (i.e.,
    members of the class ``IndividualVariableExpression`` in the ``logic``
    module. If a variable is not assigned a value by *g*, it will raise
    an ``Undefined`` exception.

    A variable *Assignment* is a mapping from individual variables to
    entities in the domain. Individual variables are usually indicated
    with the letters ``'x'``, ``'y'``, ``'w'`` and ``'z'``, optionally
    followed by an integer (e.g., ``'x0'``, ``'y332'``).  Assignments are
    created using the ``Assignment`` constructor, which also takes the
    domain as a parameter.

        >>> from nltk.sem.evaluate import Assignment
        >>> dom = set(['u1', 'u2', 'u3', 'u4'])
        >>> g3 = Assignment(dom, [('x', 'u1'), ('y', 'u2')])
        >>> g3 == {'x': 'u1', 'y': 'u2'}
        True

    There is also a ``print`` format for assignments which uses a notation
    closer to that in logic textbooks:

        >>> print(g3)
        g[u1/x][u2/y]

    It is also possible to update an assignment using the ``add`` method:

        >>> dom = set(['u1', 'u2', 'u3', 'u4'])
        >>> g4 = Assignment(dom)
        >>> g4.add('x', 'u1')
        {'x': 'u1'}

    With no arguments, ``purge()`` is equivalent to ``clear()`` on a dictionary:

        >>> g4.purge()
        >>> g4
        {}

    :param domain: the domain of discourse
    :type domain: set
    :param assign: a list of (varname, value) associations
    :type assign: list
    """
    domain: Incomplete
    variant: Incomplete
    def __init__(self, domain, assign: Incomplete | None = None) -> None: ...
    def __getitem__(self, key): ...
    def copy(self): ...
    def purge(self, var: Incomplete | None = None) -> None:
        """
        Remove one or all keys (i.e. logic variables) from an
        assignment, and update ``self.variant``.

        :param var: a Variable acting as a key for the assignment.
        """
    def add(self, var, val):
        """
        Add a new variable-value pair to the assignment, and update
        ``self.variant``.

        """

class Model:
    """
    A first order model is a domain *D* of discourse and a valuation *V*.

    A domain *D* is a set, and a valuation *V* is a map that associates
    expressions with values in the model.
    The domain of *V* should be a subset of *D*.

    Construct a new ``Model``.

    :type domain: set
    :param domain: A set of entities representing the domain of discourse of the model.
    :type valuation: Valuation
    :param valuation: the valuation of the model.
    :param prop: If this is set, then we are building a propositional    model and don't require the domain of *V* to be subset of *D*.
    """
    domain: Incomplete
    valuation: Incomplete
    def __init__(self, domain, valuation) -> None: ...
    def evaluate(self, expr, g, trace: Incomplete | None = None):
        """
        Read input expressions, and provide a handler for ``satisfy``
        that blocks further propagation of the ``Undefined`` error.
        :param expr: An ``Expression`` of ``logic``.
        :type g: Assignment
        :param g: an assignment to individual variables.
        :rtype: bool or 'Undefined'
        """
    def satisfy(self, parsed, g, trace: Incomplete | None = None):
        """
        Recursive interpretation function for a formula of first-order logic.

        Raises an ``Undefined`` error when ``parsed`` is an atomic string
        but is not a symbol or an individual variable.

        :return: Returns a truth value or ``Undefined`` if ``parsed`` is        complex, and calls the interpretation function ``i`` if ``parsed``        is atomic.

        :param parsed: An expression of ``logic``.
        :type g: Assignment
        :param g: an assignment to individual variables.
        """
    def i(self, parsed, g, trace: bool = False):
        """
        An interpretation function.

        Assuming that ``parsed`` is atomic:

        - if ``parsed`` is a non-logical constant, calls the valuation *V*
        - else if ``parsed`` is an individual variable, calls assignment *g*
        - else returns ``Undefined``.

        :param parsed: an ``Expression`` of ``logic``.
        :type g: Assignment
        :param g: an assignment to individual variables.
        :return: a semantic value
        """
    def satisfiers(self, parsed, varex, g, trace: Incomplete | None = None, nesting: int = 0):
        """
        Generate the entities from the model's domain that satisfy an open formula.

        :param parsed: an open formula
        :type parsed: Expression
        :param varex: the relevant free individual variable in ``parsed``.
        :type varex: VariableExpression or str
        :param g: a variable assignment
        :type g:  Assignment
        :return: a set of the entities that satisfy ``parsed``.
        """

mult: int

def propdemo(trace: Incomplete | None = None) -> None:
    """Example of a propositional model."""
def folmodel(quiet: bool = False, trace: Incomplete | None = None) -> None:
    """Example of a first-order model."""
def foldemo(trace: Incomplete | None = None) -> None:
    """
    Interpretation of closed expressions in a first-order model.
    """
def satdemo(trace: Incomplete | None = None) -> None:
    """Satisfiers of an open formula in a first order model."""
def demo(num: int = 0, trace: Incomplete | None = None) -> None:
    """
    Run exists demos.

     - num = 1: propositional logic demo
     - num = 2: first order model demo (only if trace is set)
     - num = 3: first order sentences demo
     - num = 4: satisfaction of open formulas demo
     - any other value: run all the demos

    :param trace: trace = 1, or trace = 2 for more verbose tracing
    """
