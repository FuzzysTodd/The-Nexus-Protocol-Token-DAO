from _typeshed import Incomplete
from nltk.sem.logic import APP as APP, AbstractVariableExpression as AbstractVariableExpression, AllExpression as AllExpression, AndExpression as AndExpression, ApplicationExpression as ApplicationExpression, BinaryExpression as BinaryExpression, BooleanExpression as BooleanExpression, ConstantExpression as ConstantExpression, EqualityExpression as EqualityExpression, EventVariableExpression as EventVariableExpression, ExistsExpression as ExistsExpression, Expression as Expression, FunctionVariableExpression as FunctionVariableExpression, ImpExpression as ImpExpression, IndividualVariableExpression as IndividualVariableExpression, LambdaExpression as LambdaExpression, LogicParser as LogicParser, NegatedExpression as NegatedExpression, OrExpression as OrExpression, Tokens as Tokens, Variable as Variable, is_eventvar as is_eventvar, is_funcvar as is_funcvar, is_indvar as is_indvar, unique_variable as unique_variable
from nltk.util import in_idle as in_idle

class DrtTokens(Tokens):
    DRS: str
    DRS_CONC: str
    PRONOUN: str
    OPEN_BRACKET: str
    CLOSE_BRACKET: str
    COLON: str
    PUNCT: Incomplete
    SYMBOLS: Incomplete
    TOKENS: Incomplete

class DrtParser(LogicParser):
    """A lambda calculus expression parser."""
    operator_precedence: Incomplete
    def __init__(self) -> None: ...
    def get_all_symbols(self):
        """This method exists to be overridden"""
    def isvariable(self, tok): ...
    def handle(self, tok, context):
        """This method is intended to be overridden for logics that
        use different operators or expressions"""
    def make_NegatedExpression(self, expression): ...
    def handle_DRS(self, tok, context): ...
    def handle_refs(self): ...
    def handle_conds(self, context): ...
    def handle_prop(self, tok, context): ...
    def make_EqualityExpression(self, first, second):
        """This method serves as a hook for other logic parsers that
        have different equality expression classes"""
    def get_BooleanExpression_factory(self, tok):
        """This method serves as a hook for other logic parsers that
        have different boolean operators"""
    def make_BooleanExpression(self, factory, first, second): ...
    def make_ApplicationExpression(self, function, argument): ...
    def make_VariableExpression(self, name): ...
    def make_LambdaExpression(self, variables, term): ...

class DrtExpression:
    """
    This is the base abstract DRT Expression from which every DRT
    Expression extends.
    """
    @classmethod
    def fromstring(cls, s): ...
    def applyto(self, other): ...
    def __neg__(self): ...
    def __and__(self, other): ...
    def __or__(self, other): ...
    def __gt__(self, other): ...
    def equiv(self, other, prover: Incomplete | None = None):
        """
        Check for logical equivalence.
        Pass the expression (self <-> other) to the theorem prover.
        If the prover says it is valid, then the self and other are equal.

        :param other: an ``DrtExpression`` to check equality against
        :param prover: a ``nltk.inference.api.Prover``
        """
    @property
    def type(self) -> None: ...
    def typecheck(self, signature: Incomplete | None = None) -> None: ...
    def __add__(self, other): ...
    def get_refs(self, recursive: bool = False) -> None:
        """
        Return the set of discourse referents in this DRS.
        :param recursive: bool Also find discourse referents in subterms?
        :return: list of ``Variable`` objects
        """
    def is_pronoun_function(self):
        '''Is self of the form "PRO(x)"?'''
    def make_EqualityExpression(self, first, second): ...
    def make_VariableExpression(self, variable): ...
    def resolve_anaphora(self): ...
    def eliminate_equality(self): ...
    def pretty_format(self):
        """
        Draw the DRS
        :return: the pretty print string
        """
    def pretty_print(self) -> None: ...
    def draw(self) -> None: ...

class DRS(DrtExpression, Expression):
    """A Discourse Representation Structure."""
    refs: Incomplete
    conds: Incomplete
    consequent: Incomplete
    def __init__(self, refs, conds, consequent: Incomplete | None = None) -> None:
        """
        :param refs: list of ``DrtIndividualVariableExpression`` for the
            discourse referents
        :param conds: list of ``Expression`` for the conditions
        """
    def replace(self, variable, expression, replace_bound: bool = False, alpha_convert: bool = True):
        """Replace all instances of variable v with expression E in self,
        where v is free in self."""
    def free(self):
        """:see: Expression.free()"""
    def get_refs(self, recursive: bool = False):
        """:see: AbstractExpression.get_refs()"""
    def visit(self, function, combinator):
        """:see: Expression.visit()"""
    def visit_structured(self, function, combinator):
        """:see: Expression.visit_structured()"""
    def eliminate_equality(self): ...
    def fol(self): ...
    def __eq__(self, other):
        """Defines equality modulo alphabetic variance.
        If we are comparing \\x.M  and \\y.N, then check equality of M and N[x/y]."""
    def __ne__(self, other): ...
    __hash__: Incomplete

def DrtVariableExpression(variable):
    """
    This is a factory method that instantiates and returns a subtype of
    ``DrtAbstractVariableExpression`` appropriate for the given variable.
    """

class DrtAbstractVariableExpression(DrtExpression, AbstractVariableExpression):
    def fol(self): ...
    def get_refs(self, recursive: bool = False):
        """:see: AbstractExpression.get_refs()"""
    def eliminate_equality(self): ...

class DrtIndividualVariableExpression(DrtAbstractVariableExpression, IndividualVariableExpression): ...
class DrtFunctionVariableExpression(DrtAbstractVariableExpression, FunctionVariableExpression): ...
class DrtEventVariableExpression(DrtIndividualVariableExpression, EventVariableExpression): ...
class DrtConstantExpression(DrtAbstractVariableExpression, ConstantExpression): ...

class DrtProposition(DrtExpression, Expression):
    variable: Incomplete
    drs: Incomplete
    def __init__(self, variable, drs) -> None: ...
    def replace(self, variable, expression, replace_bound: bool = False, alpha_convert: bool = True): ...
    def eliminate_equality(self): ...
    def get_refs(self, recursive: bool = False): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    __hash__: Incomplete
    def fol(self): ...
    def visit(self, function, combinator):
        """:see: Expression.visit()"""
    def visit_structured(self, function, combinator):
        """:see: Expression.visit_structured()"""

class DrtNegatedExpression(DrtExpression, NegatedExpression):
    def fol(self): ...
    def get_refs(self, recursive: bool = False):
        """:see: AbstractExpression.get_refs()"""

class DrtLambdaExpression(DrtExpression, LambdaExpression):
    def alpha_convert(self, newvar):
        """Rename all occurrences of the variable introduced by this variable
        binder in the expression to ``newvar``.
        :param newvar: ``Variable``, for the new variable
        """
    def fol(self): ...
    def get_refs(self, recursive: bool = False):
        """:see: AbstractExpression.get_refs()"""

class DrtBinaryExpression(DrtExpression, BinaryExpression):
    def get_refs(self, recursive: bool = False):
        """:see: AbstractExpression.get_refs()"""

class DrtBooleanExpression(DrtBinaryExpression, BooleanExpression): ...

class DrtOrExpression(DrtBooleanExpression, OrExpression):
    def fol(self): ...

class DrtEqualityExpression(DrtBinaryExpression, EqualityExpression):
    def fol(self): ...

class DrtConcatenation(DrtBooleanExpression):
    """DRS of the form '(DRS + DRS)'"""
    consequent: Incomplete
    def __init__(self, first, second, consequent: Incomplete | None = None) -> None: ...
    def replace(self, variable, expression, replace_bound: bool = False, alpha_convert: bool = True):
        """Replace all instances of variable v with expression E in self,
        where v is free in self."""
    def eliminate_equality(self): ...
    def simplify(self): ...
    def get_refs(self, recursive: bool = False):
        """:see: AbstractExpression.get_refs()"""
    def getOp(self): ...
    def __eq__(self, other):
        """Defines equality modulo alphabetic variance.
        If we are comparing \\x.M  and \\y.N, then check equality of M and N[x/y]."""
    def __ne__(self, other): ...
    __hash__: Incomplete
    def fol(self): ...
    def visit(self, function, combinator):
        """:see: Expression.visit()"""

class DrtApplicationExpression(DrtExpression, ApplicationExpression):
    def fol(self): ...
    def get_refs(self, recursive: bool = False):
        """:see: AbstractExpression.get_refs()"""

class PossibleAntecedents(list, DrtExpression, Expression):
    def free(self):
        """Set of free variables."""
    def replace(self, variable, expression, replace_bound: bool = False, alpha_convert: bool = True):
        """Replace all instances of variable v with expression E in self,
        where v is free in self."""

class AnaphoraResolutionException(Exception): ...

def resolve_anaphora(expression, trail=[]): ...

class DrsDrawer:
    BUFFER: int
    TOPSPACE: int
    OUTERSPACE: int
    canvas: Incomplete
    drs: Incomplete
    master: Incomplete
    def __init__(self, drs, size_canvas: bool = True, canvas: Incomplete | None = None) -> None:
        """
        :param drs: ``DrtExpression``, The DRS to be drawn
        :param size_canvas: bool, True if the canvas size should be the exact size of the DRS
        :param canvas: ``Canvas`` The canvas on which to draw the DRS.  If none is given, create a new canvas.
        """
    def draw(self, x=..., y=...):
        """Draw the DRS"""

def demo() -> None: ...
def test_draw() -> None: ...
