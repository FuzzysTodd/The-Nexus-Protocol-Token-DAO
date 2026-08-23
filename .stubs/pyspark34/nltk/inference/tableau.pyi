from _typeshed import Incomplete
from nltk.inference.api import BaseProverCommand as BaseProverCommand, Prover as Prover
from nltk.internals import Counter as Counter
from nltk.sem.logic import AbstractVariableExpression as AbstractVariableExpression, AllExpression as AllExpression, AndExpression as AndExpression, ApplicationExpression as ApplicationExpression, EqualityExpression as EqualityExpression, ExistsExpression as ExistsExpression, Expression as Expression, FunctionVariableExpression as FunctionVariableExpression, IffExpression as IffExpression, ImpExpression as ImpExpression, LambdaExpression as LambdaExpression, NegatedExpression as NegatedExpression, OrExpression as OrExpression, Variable as Variable, VariableExpression as VariableExpression, unique_variable as unique_variable

class ProverParseError(Exception): ...

class TableauProver(Prover):
    @staticmethod
    def is_atom(e): ...

class TableauProverCommand(BaseProverCommand):
    def __init__(self, goal: Incomplete | None = None, assumptions: Incomplete | None = None, prover: Incomplete | None = None) -> None:
        """
        :param goal: Input expression to prove
        :type goal: sem.Expression
        :param assumptions: Input expressions to use as assumptions in
            the proof.
        :type assumptions: list(sem.Expression)
        """

class Agenda:
    sets: Incomplete
    def __init__(self) -> None: ...
    def clone(self): ...
    def __getitem__(self, index): ...
    def put(self, expression, context: Incomplete | None = None) -> None: ...
    def put_all(self, expressions) -> None: ...
    def put_atoms(self, atoms) -> None: ...
    def pop_first(self):
        """Pop the first expression that appears in the agenda"""
    def replace_all(self, old, new) -> None: ...
    def mark_alls_fresh(self) -> None: ...
    def mark_neqs_fresh(self) -> None: ...

class Debug:
    verbose: Incomplete
    indent: Incomplete
    lines: Incomplete
    def __init__(self, verbose, indent: int = 0, lines: Incomplete | None = None) -> None: ...
    def __add__(self, increment): ...
    def line(self, data, indent: int = 0) -> None: ...

class Categories:
    ATOM: int
    PROP: int
    N_ATOM: int
    N_PROP: int
    APP: int
    N_APP: int
    N_EQ: int
    D_NEG: int
    N_ALL: int
    N_EXISTS: int
    AND: int
    N_OR: int
    N_IMP: int
    OR: int
    IMP: int
    N_AND: int
    IFF: int
    N_IFF: int
    EQ: int
    EXISTS: int
    ALL: int

def testTableauProver() -> None: ...
def testHigherOrderTableauProver() -> None: ...
def tableau_test(c, ps: Incomplete | None = None, verbose: bool = False) -> None: ...
def demo() -> None: ...
