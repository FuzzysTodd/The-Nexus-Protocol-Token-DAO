from _typeshed import Incomplete
from nltk.internals import Counter as Counter
from nltk.util import Trie as Trie

APP: str

class Tokens:
    LAMBDA: str
    LAMBDA_LIST: Incomplete
    EXISTS: str
    EXISTS_LIST: Incomplete
    ALL: str
    ALL_LIST: Incomplete
    IOTA: str
    IOTA_LIST: Incomplete
    DOT: str
    OPEN: str
    CLOSE: str
    COMMA: str
    NOT: str
    NOT_LIST: Incomplete
    AND: str
    AND_LIST: Incomplete
    OR: str
    OR_LIST: Incomplete
    IMP: str
    IMP_LIST: Incomplete
    IFF: str
    IFF_LIST: Incomplete
    EQ: str
    EQ_LIST: Incomplete
    NEQ: str
    NEQ_LIST: Incomplete
    BINOPS: Incomplete
    QUANTS: Incomplete
    PUNCT: Incomplete
    TOKENS: Incomplete
    SYMBOLS: Incomplete

def boolean_ops() -> None:
    """
    Boolean operators
    """
def equality_preds() -> None:
    """
    Equality predicates
    """
def binding_ops() -> None:
    """
    Binding operators
    """

class LogicParser:
    """A lambda calculus expression parser."""
    type_check: Incomplete
    quote_chars: Incomplete
    operator_precedence: Incomplete
    right_associated_operations: Incomplete
    def __init__(self, type_check: bool = False) -> None:
        """
        :param type_check: should type checking be performed
            to their types?
        :type type_check: bool
        """
    def parse(self, data, signature: Incomplete | None = None):
        """
        Parse the expression.

        :param data: str for the input to be parsed
        :param signature: ``dict<str, str>`` that maps variable names to type
            strings
        :returns: a parsed Expression
        """
    def process(self, data):
        """Split the data into tokens"""
    def process_quoted_token(self, data_idx, data): ...
    def get_all_symbols(self):
        """This method exists to be overridden"""
    def inRange(self, location):
        """Return TRUE if the given location is within the buffer"""
    def token(self, location: Incomplete | None = None):
        """Get the next waiting token.  If a location is given, then
        return the token at currentIndex+location without advancing
        currentIndex; setting it gives lookahead/lookback capability."""
    def isvariable(self, tok): ...
    def process_next_expression(self, context):
        """Parse the next complete expression from the stream and return it."""
    def handle(self, tok, context):
        """This method is intended to be overridden for logics that
        use different operators or expressions"""
    def attempt_adjuncts(self, expression, context): ...
    def handle_negation(self, tok, context): ...
    def make_NegatedExpression(self, expression): ...
    def handle_variable(self, tok, context): ...
    def get_next_token_variable(self, description): ...
    def handle_lambda(self, tok, context): ...
    def handle_quant(self, tok, context): ...
    def get_QuantifiedExpression_factory(self, tok):
        """This method serves as a hook for other logic parsers that
        have different quantifiers"""
    def make_QuanifiedExpression(self, factory, variable, term): ...
    def handle_open(self, tok, context): ...
    def attempt_EqualityExpression(self, expression, context):
        """Attempt to make an equality expression.  If the next token is an
        equality operator, then an EqualityExpression will be returned.
        Otherwise, the parameter will be returned."""
    def make_EqualityExpression(self, first, second):
        """This method serves as a hook for other logic parsers that
        have different equality expression classes"""
    def attempt_BooleanExpression(self, expression, context):
        """Attempt to make a boolean expression.  If the next token is a boolean
        operator, then a BooleanExpression will be returned.  Otherwise, the
        parameter will be returned."""
    def get_BooleanExpression_factory(self, tok):
        """This method serves as a hook for other logic parsers that
        have different boolean operators"""
    def make_BooleanExpression(self, factory, first, second): ...
    def attempt_ApplicationExpression(self, expression, context):
        """Attempt to make an application expression.  The next tokens are
        a list of arguments in parens, then the argument expression is a
        function being applied to the arguments.  Otherwise, return the
        argument expression."""
    def make_ApplicationExpression(self, function, argument): ...
    def make_VariableExpression(self, name): ...
    def make_LambdaExpression(self, variable, term): ...
    def has_priority(self, operation, context): ...
    def assertNextToken(self, expected) -> None: ...
    def assertToken(self, tok, expected) -> None: ...

def read_logic(s, logic_parser: Incomplete | None = None, encoding: Incomplete | None = None):
    """
    Convert a file of First Order Formulas into a list of {Expression}s.

    :param s: the contents of the file
    :type s: str
    :param logic_parser: The parser to be used to parse the logical expression
    :type logic_parser: LogicParser
    :param encoding: the encoding of the input string, if it is binary
    :type encoding: str
    :return: a list of parsed formulas.
    :rtype: list(Expression)
    """

class Variable:
    name: Incomplete
    def __init__(self, name) -> None:
        """
        :param name: the name of the variable
        """
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __lt__(self, other): ...
    def substitute_bindings(self, bindings): ...
    def __hash__(self): ...

def unique_variable(pattern: Incomplete | None = None, ignore: Incomplete | None = None):
    """
    Return a new, unique variable.

    :param pattern: ``Variable`` that is being replaced.  The new variable must
        be the same type.
    :param term: a set of ``Variable`` objects that should not be returned from
        this function.
    :rtype: Variable
    """
def skolem_function(univ_scope: Incomplete | None = None):
    """
    Return a skolem function over the variables in univ_scope
    param univ_scope
    """

class Type:
    def __hash__(self): ...
    @classmethod
    def fromstring(cls, s): ...

class ComplexType(Type):
    first: Incomplete
    second: Incomplete
    def __init__(self, first, second) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    __hash__: Incomplete
    def matches(self, other): ...
    def resolve(self, other): ...
    def str(self): ...

class BasicType(Type):
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    __hash__: Incomplete
    def matches(self, other): ...
    def resolve(self, other): ...

class EntityType(BasicType):
    def str(self): ...

class TruthValueType(BasicType):
    def str(self): ...

class EventType(BasicType):
    def str(self): ...

class AnyType(BasicType, ComplexType):
    def __init__(self) -> None: ...
    @property
    def first(self): ...
    @property
    def second(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    __hash__: Incomplete
    def matches(self, other): ...
    def resolve(self, other): ...
    def str(self): ...

TRUTH_TYPE: Incomplete
ENTITY_TYPE: Incomplete
EVENT_TYPE: Incomplete
ANY_TYPE: Incomplete

def read_type(type_string): ...

class TypeException(Exception):
    def __init__(self, msg) -> None: ...

class InconsistentTypeHierarchyException(TypeException):
    def __init__(self, variable, expression: Incomplete | None = None) -> None: ...

class TypeResolutionException(TypeException):
    def __init__(self, expression, other_type) -> None: ...

class IllegalTypeException(TypeException):
    def __init__(self, expression, other_type, allowed_type) -> None: ...

def typecheck(expressions, signature: Incomplete | None = None):
    """
    Ensure correct typing across a collection of ``Expression`` objects.
    :param expressions: a collection of expressions
    :param signature: dict that maps variable names to types (or string
    representations of types)
    """

class SubstituteBindingsI:
    """
    An interface for classes that can perform substitutions for
    variables.
    """
    def substitute_bindings(self, bindings) -> None:
        """
        :return: The object that is obtained by replacing
            each variable bound by ``bindings`` with its values.
            Aliases are already resolved. (maybe?)
        :rtype: (any)
        """
    def variables(self) -> None:
        """
        :return: A list of all variables in this object.
        """

class Expression(SubstituteBindingsI):
    """This is the base abstract object for all logical expressions"""
    @classmethod
    def fromstring(cls, s, type_check: bool = False, signature: Incomplete | None = None): ...
    def __call__(self, other, *additional): ...
    def applyto(self, other): ...
    def __neg__(self): ...
    def negate(self):
        """If this is a negated expression, remove the negation.
        Otherwise add a negation."""
    def __and__(self, other): ...
    def __or__(self, other): ...
    def __gt__(self, other): ...
    def __lt__(self, other): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def equiv(self, other, prover: Incomplete | None = None):
        """
        Check for logical equivalence.
        Pass the expression (self <-> other) to the theorem prover.
        If the prover says it is valid, then the self and other are equal.

        :param other: an ``Expression`` to check equality against
        :param prover: a ``nltk.inference.api.Prover``
        """
    def __hash__(self): ...
    def substitute_bindings(self, bindings): ...
    def typecheck(self, signature: Incomplete | None = None):
        """
        Infer and check types.  Raise exceptions if necessary.

        :param signature: dict that maps variable names to types (or string
            representations of types)
        :return: the signature, plus any additional type mappings
        """
    def findtype(self, variable) -> None:
        '''
        Find the type of the given variable as it is used in this expression.
        For example, finding the type of "P" in "P(x) & Q(x,y)" yields "<e,t>"

        :param variable: Variable
        '''
    def replace(self, variable, expression, replace_bound: bool = False, alpha_convert: bool = True):
        """
        Replace every instance of 'variable' with 'expression'
        :param variable: ``Variable`` The variable to replace
        :param expression: ``Expression`` The expression with which to replace it
        :param replace_bound: bool Should bound variables be replaced?
        :param alpha_convert: bool Alpha convert automatically to avoid name clashes?
        """
    def normalize(self, newvars: Incomplete | None = None):
        """Rename auto-generated unique variables"""
    def visit(self, function, combinator) -> None:
        """
        Recursively visit subexpressions.  Apply 'function' to each
        subexpression and pass the result of each function application
        to the 'combinator' for aggregation:

            return combinator(map(function, self.subexpressions))

        Bound variables are neither applied upon by the function nor given to
        the combinator.
        :param function: ``Function<Expression,T>`` to call on each subexpression
        :param combinator: ``Function<list<T>,R>`` to combine the results of the
        function calls
        :return: result of combination ``R``
        """
    def visit_structured(self, function, combinator):
        """
        Recursively visit subexpressions.  Apply 'function' to each
        subexpression and pass the result of each function application
        to the 'combinator' for aggregation.  The combinator must have
        the same signature as the constructor.  The function is not
        applied to bound variables, but they are passed to the
        combinator.
        :param function: ``Function`` to call on each subexpression
        :param combinator: ``Function`` with the same signature as the
        constructor, to combine the results of the function calls
        :return: result of combination
        """
    def variables(self):
        """
        Return a set of all the variables for binding substitution.
        The variables returned include all free (non-bound) individual
        variables and any variable starting with '?' or '@'.
        :return: set of ``Variable`` objects
        """
    def free(self):
        """
        Return a set of all the free (non-bound) variables.  This includes
        both individual and predicate variables, but not constants.
        :return: set of ``Variable`` objects
        """
    def constants(self):
        """
        Return a set of individual constants (non-predicates).
        :return: set of ``Variable`` objects
        """
    def predicates(self):
        """
        Return a set of predicates (constants, not variables).
        :return: set of ``Variable`` objects
        """
    def simplify(self):
        """
        :return: beta-converted version of this expression
        """
    def make_VariableExpression(self, variable): ...

class ApplicationExpression(Expression):
    '''
    This class is used to represent two related types of logical expressions.

    The first is a Predicate Expression, such as "P(x,y)".  A predicate
    expression is comprised of a ``FunctionVariableExpression`` or
    ``ConstantExpression`` as the predicate and a list of Expressions as the
    arguments.

    The second is a an application of one expression to another, such as
    "(\\x.dog(x))(fido)".

    The reason Predicate Expressions are treated as Application Expressions is
    that the Variable Expression predicate of the expression may be replaced
    with another Expression, such as a LambdaExpression, which would mean that
    the Predicate should be thought of as being applied to the arguments.

    The logical expression reader will always curry arguments in a application expression.
    So, "\\x y.see(x,y)(john,mary)" will be represented internally as
    "((\\x y.(see(x))(y))(john))(mary)".  This simplifies the internals since
    there will always be exactly one argument in an application.

    The str() method will usually print the curried forms of application
    expressions.  The one exception is when the the application expression is
    really a predicate expression (ie, underlying function is an
    ``AbstractVariableExpression``).  This means that the example from above
    will be returned as "(\\x y.see(x,y)(john))(mary)".
    '''
    function: Incomplete
    argument: Incomplete
    def __init__(self, function, argument) -> None:
        """
        :param function: ``Expression``, for the function expression
        :param argument: ``Expression``, for the argument
        """
    def simplify(self): ...
    @property
    def type(self): ...
    def findtype(self, variable):
        """:see Expression.findtype()"""
    def constants(self):
        """:see: Expression.constants()"""
    def predicates(self):
        """:see: Expression.predicates()"""
    def visit(self, function, combinator):
        """:see: Expression.visit()"""
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    __hash__: Incomplete
    def uncurry(self):
        """
        Uncurry this application expression

        return: A tuple (base-function, arg-list)
        """
    @property
    def pred(self):
        """
        Return uncurried base-function.
        If this is an atom, then the result will be a variable expression.
        Otherwise, it will be a lambda expression.
        """
    @property
    def args(self):
        """
        Return uncurried arg-list
        """
    def is_atom(self):
        """
        Is this expression an atom (as opposed to a lambda expression applied
        to a term)?
        """

class AbstractVariableExpression(Expression):
    """This class represents a variable to be used as a predicate or entity"""
    variable: Incomplete
    def __init__(self, variable) -> None:
        """
        :param variable: ``Variable``, for the variable
        """
    def simplify(self): ...
    def replace(self, variable, expression, replace_bound: bool = False, alpha_convert: bool = True):
        """:see: Expression.replace()"""
    def findtype(self, variable):
        """:see Expression.findtype()"""
    def predicates(self):
        """:see: Expression.predicates()"""
    def __eq__(self, other):
        """Allow equality between instances of ``AbstractVariableExpression``
        subtypes."""
    def __ne__(self, other): ...
    def __lt__(self, other): ...
    __hash__: Incomplete

class IndividualVariableExpression(AbstractVariableExpression):
    """This class represents variables that take the form of a single lowercase
    character (other than 'e') followed by zero or more digits."""
    type: Incomplete
    def free(self):
        """:see: Expression.free()"""
    def constants(self):
        """:see: Expression.constants()"""

class FunctionVariableExpression(AbstractVariableExpression):
    """This class represents variables that take the form of a single uppercase
    character followed by zero or more digits."""
    type = ANY_TYPE
    def free(self):
        """:see: Expression.free()"""
    def constants(self):
        """:see: Expression.constants()"""

class EventVariableExpression(IndividualVariableExpression):
    """This class represents variables that take the form of a single lowercase
    'e' character followed by zero or more digits."""
    type = EVENT_TYPE

class ConstantExpression(AbstractVariableExpression):
    """This class represents variables that do not take the form of a single
    character followed by zero or more digits."""
    type = ENTITY_TYPE
    def free(self):
        """:see: Expression.free()"""
    def constants(self):
        """:see: Expression.constants()"""

def VariableExpression(variable):
    """
    This is a factory method that instantiates and returns a subtype of
    ``AbstractVariableExpression`` appropriate for the given variable.
    """

class VariableBinderExpression(Expression):
    """This an abstract class for any Expression that binds a variable in an
    Expression.  This includes LambdaExpressions and Quantified Expressions"""
    variable: Incomplete
    term: Incomplete
    def __init__(self, variable, term) -> None:
        """
        :param variable: ``Variable``, for the variable
        :param term: ``Expression``, for the term
        """
    def replace(self, variable, expression, replace_bound: bool = False, alpha_convert: bool = True):
        """:see: Expression.replace()"""
    def alpha_convert(self, newvar):
        """Rename all occurrences of the variable introduced by this variable
        binder in the expression to ``newvar``.
        :param newvar: ``Variable``, for the new variable
        """
    def free(self):
        """:see: Expression.free()"""
    def findtype(self, variable):
        """:see Expression.findtype()"""
    def visit(self, function, combinator):
        """:see: Expression.visit()"""
    def visit_structured(self, function, combinator):
        """:see: Expression.visit_structured()"""
    def __eq__(self, other):
        """Defines equality modulo alphabetic variance.  If we are comparing
        \\x.M  and \\y.N, then check equality of M and N[x/y]."""
    def __ne__(self, other): ...
    __hash__: Incomplete

class LambdaExpression(VariableBinderExpression):
    @property
    def type(self): ...

class QuantifiedExpression(VariableBinderExpression):
    @property
    def type(self): ...

class ExistsExpression(QuantifiedExpression):
    def getQuantifier(self): ...

class AllExpression(QuantifiedExpression):
    def getQuantifier(self): ...

class IotaExpression(QuantifiedExpression):
    def getQuantifier(self): ...

class NegatedExpression(Expression):
    term: Incomplete
    def __init__(self, term) -> None: ...
    @property
    def type(self): ...
    def findtype(self, variable): ...
    def visit(self, function, combinator):
        """:see: Expression.visit()"""
    def negate(self):
        """:see: Expression.negate()"""
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    __hash__: Incomplete

class BinaryExpression(Expression):
    first: Incomplete
    second: Incomplete
    def __init__(self, first, second) -> None: ...
    @property
    def type(self): ...
    def findtype(self, variable):
        """:see Expression.findtype()"""
    def visit(self, function, combinator):
        """:see: Expression.visit()"""
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    __hash__: Incomplete

class BooleanExpression(BinaryExpression): ...

class AndExpression(BooleanExpression):
    """This class represents conjunctions"""
    def getOp(self): ...

class OrExpression(BooleanExpression):
    """This class represents disjunctions"""
    def getOp(self): ...

class ImpExpression(BooleanExpression):
    """This class represents implications"""
    def getOp(self): ...

class IffExpression(BooleanExpression):
    """This class represents biconditionals"""
    def getOp(self): ...

class EqualityExpression(BinaryExpression):
    '''This class represents equality expressions like "(x = y)".'''
    def getOp(self): ...

class LogicalExpressionException(Exception):
    index: Incomplete
    def __init__(self, index, message) -> None: ...

class UnexpectedTokenException(LogicalExpressionException):
    def __init__(self, index, unexpected: Incomplete | None = None, expected: Incomplete | None = None, message: Incomplete | None = None) -> None: ...

class ExpectedMoreTokensException(LogicalExpressionException):
    def __init__(self, index, message: Incomplete | None = None) -> None: ...

def is_indvar(expr):
    """
    An individual variable must be a single lowercase character other than 'e',
    followed by zero or more digits.

    :param expr: str
    :return: bool True if expr is of the correct form
    """
def is_funcvar(expr):
    """
    A function variable must be a single uppercase character followed by
    zero or more digits.

    :param expr: str
    :return: bool True if expr is of the correct form
    """
def is_eventvar(expr):
    """
    An event variable must be a single lowercase 'e' character followed by
    zero or more digits.

    :param expr: str
    :return: bool True if expr is of the correct form
    """
def demo() -> None: ...
def demo_errors() -> None: ...
def demoException(s) -> None: ...
def printtype(ex) -> None: ...
