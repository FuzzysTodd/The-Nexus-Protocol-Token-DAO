from . import coercions as coercions, elements as elements, roles as roles, schema as schema, visitors as visitors
from .. import exc as exc, inspection as inspection, util as util
from ..util.typing import Literal as Literal
from .base import Executable as Executable, Options as Options
from .cache_key import CacheConst as CacheConst
from .elements import BindParameter as BindParameter, ClauseElement as ClauseElement
from .operators import ColumnOperators as ColumnOperators
from .roles import SQLRole as SQLRole
from _typeshed import Incomplete
from types import CodeType
from typing import Any, List, Tuple, Type

class LambdaOptions(Options):
    enable_tracking: bool
    track_closure_variables: bool
    track_on: object | None
    global_track_bound_values: bool
    track_bound_values: bool
    lambda_cache: _LambdaCacheType | None

def lambda_stmt(lmb: _StmtLambdaType, enable_tracking: bool = True, track_closure_variables: bool = True, track_on: object | None = None, global_track_bound_values: bool = True, track_bound_values: bool = True, lambda_cache: _LambdaCacheType | None = None) -> StatementLambdaElement:
    '''Produce a SQL statement that is cached as a lambda.

    The Python code object within the lambda is scanned for both Python
    literals that will become bound parameters as well as closure variables
    that refer to Core or ORM constructs that may vary.   The lambda itself
    will be invoked only once per particular set of constructs detected.

    E.g.::

        from sqlalchemy import lambda_stmt

        stmt = lambda_stmt(lambda: table.select())
        stmt += lambda s: s.where(table.c.id == 5)

        result = connection.execute(stmt)

    The object returned is an instance of :class:`_sql.StatementLambdaElement`.

    .. versionadded:: 1.4

    :param lmb: a Python function, typically a lambda, which takes no arguments
     and returns a SQL expression construct
    :param enable_tracking: when False, all scanning of the given lambda for
     changes in closure variables or bound parameters is disabled.  Use for
     a lambda that produces the identical results in all cases with no
     parameterization.
    :param track_closure_variables: when False, changes in closure variables
     within the lambda will not be scanned.   Use for a lambda where the
     state of its closure variables will never change the SQL structure
     returned by the lambda.
    :param track_bound_values: when False, bound parameter tracking will
     be disabled for the given lambda.  Use for a lambda that either does
     not produce any bound values, or where the initial bound values never
     change.
    :param global_track_bound_values: when False, bound parameter tracking
     will be disabled for the entire statement including additional links
     added via the :meth:`_sql.StatementLambdaElement.add_criteria` method.
    :param lambda_cache: a dictionary or other mapping-like object where
     information about the lambda\'s Python code as well as the tracked closure
     variables in the lambda itself will be stored.   Defaults
     to a global LRU cache.  This cache is independent of the "compiled_cache"
     used by the :class:`_engine.Connection` object.

    .. seealso::

        :ref:`engine_lambda_caching`


    '''

class LambdaElement(elements.ClauseElement):
    """A SQL construct where the state is stored as an un-invoked lambda.

    The :class:`_sql.LambdaElement` is produced transparently whenever
    passing lambda expressions into SQL constructs, such as::

        stmt = select(table).where(lambda: table.c.col == parameter)

    The :class:`_sql.LambdaElement` is the base of the
    :class:`_sql.StatementLambdaElement` which represents a full statement
    within a lambda.

    .. versionadded:: 1.4

    .. seealso::

        :ref:`engine_lambda_caching`

    """
    __visit_name__: str
    parent_lambda: StatementLambdaElement | None
    closure_cache_key: Tuple[Any, ...] | Literal[CacheConst.NO_CACHE]
    role: Type[SQLRole]
    fn: _AnyLambdaType
    tracker_key: Tuple[CodeType, ...]
    opts: Incomplete
    def __init__(self, fn: _LambdaType, role: Type[SQLRole], opts: Type[LambdaOptions] | LambdaOptions = ..., apply_propagate_attrs: ClauseElement | None = None) -> None: ...
    def __getattr__(self, key): ...

class DeferredLambdaElement(LambdaElement):
    """A LambdaElement where the lambda accepts arguments and is
    invoked within the compile phase with special context.

    This lambda doesn't normally produce its real SQL expression outside of the
    compile phase.  It is passed a fixed set of initial arguments
    so that it can generate a sample expression.

    """
    lambda_args: Incomplete
    def __init__(self, fn: _LambdaType, role: Type[roles.SQLRole], opts: Type[LambdaOptions] | LambdaOptions = ..., lambda_args: Tuple[Any, ...] = ()) -> None: ...

class StatementLambdaElement(roles.AllowsLambdaRole, LambdaElement, Executable):
    """Represent a composable SQL statement as a :class:`_sql.LambdaElement`.

    The :class:`_sql.StatementLambdaElement` is constructed using the
    :func:`_sql.lambda_stmt` function::


        from sqlalchemy import lambda_stmt

        stmt = lambda_stmt(lambda: select(table))

    Once constructed, additional criteria can be built onto the statement
    by adding subsequent lambdas, which accept the existing statement
    object as a single parameter::

        stmt += lambda s: s.where(table.c.col == parameter)


    .. versionadded:: 1.4

    .. seealso::

        :ref:`engine_lambda_caching`

    """
    def __init__(self, fn: _StmtLambdaType, role: Type[SQLRole], opts: Type[LambdaOptions] | LambdaOptions = ..., apply_propagate_attrs: ClauseElement | None = None) -> None: ...
    def __add__(self, other: _StmtLambdaElementType[Any]) -> StatementLambdaElement: ...
    def add_criteria(self, other: _StmtLambdaElementType[Any], enable_tracking: bool = True, track_on: Any | None = None, track_closure_variables: bool = True, track_bound_values: bool = True) -> StatementLambdaElement:
        """Add new criteria to this :class:`_sql.StatementLambdaElement`.

        E.g.::

            >>> def my_stmt(parameter):
            ...     stmt = lambda_stmt(
            ...         lambda: select(table.c.x, table.c.y),
            ...     )
            ...     stmt = stmt.add_criteria(
            ...         lambda: table.c.x > parameter
            ...     )
            ...     return stmt

        The :meth:`_sql.StatementLambdaElement.add_criteria` method is
        equivalent to using the Python addition operator to add a new
        lambda, except that additional arguments may be added including
        ``track_closure_values`` and ``track_on``::

            >>> def my_stmt(self, foo):
            ...     stmt = lambda_stmt(
            ...         lambda: select(func.max(foo.x, foo.y)),
            ...         track_closure_variables=False
            ...     )
            ...     stmt = stmt.add_criteria(
            ...         lambda: self.where_criteria,
            ...         track_on=[self]
            ...     )
            ...     return stmt

        See :func:`_sql.lambda_stmt` for a description of the parameters
        accepted.

        """
    @property
    def is_select(self): ...
    @property
    def is_update(self): ...
    @property
    def is_insert(self): ...
    @property
    def is_text(self): ...
    @property
    def is_delete(self): ...
    @property
    def is_dml(self): ...
    def spoil(self) -> NullLambdaStatement:
        """Return a new :class:`.StatementLambdaElement` that will run
        all lambdas unconditionally each time.

        """

class NullLambdaStatement(roles.AllowsLambdaRole, elements.ClauseElement):
    """Provides the :class:`.StatementLambdaElement` API but does not
    cache or analyze lambdas.

    the lambdas are instead invoked immediately.

    The intended use is to isolate issues that may arise when using
    lambda statements.

    """
    __visit_name__: str
    def __init__(self, statement) -> None: ...
    def __getattr__(self, key): ...
    def __add__(self, other): ...
    def add_criteria(self, other, **kw): ...

class LinkedLambdaElement(StatementLambdaElement):
    """Represent subsequent links of a :class:`.StatementLambdaElement`."""
    parent_lambda: StatementLambdaElement
    opts: Incomplete
    fn: Incomplete
    tracker_key: Incomplete
    def __init__(self, fn: _StmtLambdaElementType[Any], parent_lambda: StatementLambdaElement, opts: Type[LambdaOptions] | LambdaOptions) -> None: ...

class AnalyzedCode:
    @classmethod
    def get(cls, fn, lambda_element, lambda_kw, **kw): ...
    track_bound_values: Incomplete
    track_closure_variables: Incomplete
    bindparam_trackers: Incomplete
    closure_trackers: Incomplete
    build_py_wrappers: Incomplete
    def __init__(self, fn, lambda_element, opts) -> None: ...

class NonAnalyzedFunction:
    closure_bindparams: List[BindParameter[Any]] | None
    bindparam_trackers: List[_BoundParameterGetter] | None
    is_sequence: bool
    expr: ClauseElement
    def __init__(self, expr: ClauseElement) -> None: ...
    @property
    def expected_expr(self) -> ClauseElement: ...

class AnalyzedFunction:
    closure_bindparams: List[BindParameter[Any]] | None
    expected_expr: ClauseElement | List[ClauseElement]
    bindparam_trackers: List[_BoundParameterGetter] | None
    analyzed_code: Incomplete
    fn: Incomplete
    def __init__(self, analyzed_code, lambda_element, apply_propagate_attrs, fn) -> None: ...

class PyWrapper(ColumnOperators):
    """A wrapper object that is injected into the ``__globals__`` and
    ``__closure__`` of a Python function.

    When the function is instrumented with :class:`.PyWrapper` objects, it is
    then invoked just once in order to set up the wrappers.  We look through
    all the :class:`.PyWrapper` objects we made to find the ones that generated
    a :class:`.BindParameter` object, e.g. the expression system interpreted
    something as a literal.   Those positions in the globals/closure are then
    ones that we will look at, each time a new lambda comes in that refers to
    the same ``__code__`` object.   In this way, we keep a single version of
    the SQL expression that this lambda produced, without calling upon the
    Python function that created it more than once, unless its other closure
    variables have changed.   The expression is then transformed to have the
    new bound values embedded into it.

    """
    fn: Incomplete
    track_bound_values: Incomplete
    def __init__(self, fn, name, to_evaluate, closure_index: Incomplete | None = None, getter: Incomplete | None = None, track_bound_values: bool = True) -> None: ...
    def __call__(self, *arg, **kw): ...
    def operate(self, op, *other, **kwargs): ...
    def reverse_operate(self, op, other, **kwargs): ...
    def __bool__(self) -> bool: ...
    def __getattribute__(self, key): ...
    def __iter__(self): ...
    def __getitem__(self, key): ...

def insp(lmb): ...
