from _typeshed import Incomplete
from nltk.inference.api import BaseProverCommand as BaseProverCommand, Prover as Prover
from nltk.sem import skolemize as skolemize
from nltk.sem.logic import AndExpression as AndExpression, ApplicationExpression as ApplicationExpression, EqualityExpression as EqualityExpression, Expression as Expression, IndividualVariableExpression as IndividualVariableExpression, NegatedExpression as NegatedExpression, OrExpression as OrExpression, Variable as Variable, VariableExpression as VariableExpression, is_indvar as is_indvar, unique_variable as unique_variable

class ProverParseError(Exception): ...

class ResolutionProver(Prover):
    ANSWER_KEY: str

class ResolutionProverCommand(BaseProverCommand):
    def __init__(self, goal: Incomplete | None = None, assumptions: Incomplete | None = None, prover: Incomplete | None = None) -> None:
        """
        :param goal: Input expression to prove
        :type goal: sem.Expression
        :param assumptions: Input expressions to use as assumptions in
            the proof.
        :type assumptions: list(sem.Expression)
        """
    def prove(self, verbose: bool = False):
        """
        Perform the actual proof.  Store the result to prevent unnecessary
        re-proving.
        """
    def find_answers(self, verbose: bool = False): ...

class Clause(list):
    def __init__(self, data) -> None: ...
    def unify(self, other, bindings: Incomplete | None = None, used: Incomplete | None = None, skipped: Incomplete | None = None, debug: bool = False):
        """
        Attempt to unify this Clause with the other, returning a list of
        resulting, unified, Clauses.

        :param other: ``Clause`` with which to unify
        :param bindings: ``BindingDict`` containing bindings that should be used
            during the unification
        :param used: tuple of two lists of atoms.  The first lists the
            atoms from 'self' that were successfully unified with atoms from
            'other'.  The second lists the atoms from 'other' that were successfully
            unified with atoms from 'self'.
        :param skipped: tuple of two ``Clause`` objects.  The first is a list of all
            the atoms from the 'self' Clause that have not been unified with
            anything on the path.  The second is same thing for the 'other' Clause.
        :param debug: bool indicating whether debug statements should print
        :return: list containing all the resulting ``Clause`` objects that could be
            obtained by unification
        """
    def isSubsetOf(self, other):
        """
        Return True iff every term in 'self' is a term in 'other'.

        :param other: ``Clause``
        :return: bool
        """
    def subsumes(self, other):
        """
        Return True iff 'self' subsumes 'other', this is, if there is a
        substitution such that every term in 'self' can be unified with a term
        in 'other'.

        :param other: ``Clause``
        :return: bool
        """
    def __getslice__(self, start, end): ...
    def __sub__(self, other): ...
    def __add__(self, other): ...
    def is_tautology(self):
        """
        Self is a tautology if it contains ground terms P and -P.  The ground
        term, P, must be an exact match, ie, not using unification.
        """
    def free(self): ...
    def replace(self, variable, expression):
        """
        Replace every instance of variable with expression across every atom
        in the clause

        :param variable: ``Variable``
        :param expression: ``Expression``
        """
    def substitute_bindings(self, bindings):
        """
        Replace every binding

        :param bindings: A list of tuples mapping Variable Expressions to the
            Expressions to which they are bound.
        :return: ``Clause``
        """

def clausify(expression):
    """
    Skolemize, clausify, and standardize the variables apart.
    """

class BindingDict:
    d: Incomplete
    def __init__(self, binding_list: Incomplete | None = None) -> None:
        """
        :param binding_list: list of (``AbstractVariableExpression``, ``AtomicExpression``) to initialize the dictionary
        """
    def __setitem__(self, variable, binding) -> None:
        """
        A binding is consistent with the dict if its variable is not already bound, OR if its
        variable is already bound to its argument.

        :param variable: ``Variable`` The variable to bind
        :param binding: ``Expression`` The atomic to which 'variable' should be bound
        :raise BindingException: If the variable cannot be bound in this dictionary
        """
    def __getitem__(self, variable):
        """
        Return the expression to which 'variable' is bound
        """
    def __contains__(self, item) -> bool: ...
    def __add__(self, other):
        """
        :param other: ``BindingDict`` The dict with which to combine self
        :return: ``BindingDict`` A new dict containing all the elements of both parameters
        :raise BindingException: If the parameter dictionaries are not consistent with each other
        """
    def __len__(self) -> int: ...

def most_general_unification(a, b, bindings: Incomplete | None = None):
    """
    Find the most general unification of the two given expressions

    :param a: ``Expression``
    :param b: ``Expression``
    :param bindings: ``BindingDict`` a starting set of bindings with which the
                     unification must be consistent
    :return: a list of bindings
    :raise BindingException: if the Expressions cannot be unified
    """

class BindingException(Exception):
    def __init__(self, arg) -> None: ...

class UnificationException(Exception):
    def __init__(self, a, b) -> None: ...

class DebugObject:
    enabled: Incomplete
    indent: Incomplete
    def __init__(self, enabled: bool = True, indent: int = 0) -> None: ...
    def __add__(self, i): ...
    def line(self, line) -> None: ...

def testResolutionProver() -> None: ...
def resolution_test(e) -> None: ...
def test_clausify() -> None: ...
def demo() -> None: ...
