from . import base as base, coercions as coercions, crud as crud, elements as elements, functions as functions, operators as operators, roles as roles, schema as schema, selectable as selectable, sqltypes as sqltypes
from .. import exc as exc, util as util
from ..engine.cursor import CursorResultMetaData as CursorResultMetaData
from ..engine.interfaces import Dialect as Dialect, SchemaTranslateMapType as SchemaTranslateMapType, _CoreSingleExecuteParams, _DBAPIAnyExecuteParams, _DBAPISingleExecuteParams, _ExecuteOptions, _GenericSetInputSizesType, _MutableCoreSingleExecuteParams
from ..util import FastIntFlag as FastIntFlag
from ..util.typing import Literal as Literal, Protocol as Protocol, TypedDict as TypedDict
from ._typing import is_column_element as is_column_element, is_dml as is_dml
from .base import CompileState as CompileState, Executable as Executable, NO_ARG as NO_ARG, _AmbiguousTableNameMap
from .cache_key import CacheKey as CacheKey
from .ddl import ExecutableDDLElement as ExecutableDDLElement
from .dml import Insert as Insert, UpdateBase as UpdateBase, ValuesBase as ValuesBase
from .elements import BindParameter as BindParameter, ClauseElement as ClauseElement, ColumnClause as ColumnClause, ColumnElement as ColumnElement, Label as Label, quoted_name as quoted_name
from .functions import Function as Function
from .schema import Column as Column, Table as Table
from .selectable import AliasedReturnsRows as AliasedReturnsRows, CTE as CTE, CompoundSelectState as CompoundSelectState, FromClause as FromClause, NamedFromClause as NamedFromClause, ReturnsRows as ReturnsRows, Select as Select, SelectState as SelectState
from .sqltypes import TupleType as TupleType
from .type_api import TypeEngine as TypeEngine, _BindProcessorType
from .visitors import Visitable as Visitable, prefix_anon_map as prefix_anon_map
from _typeshed import Incomplete
from enum import IntEnum
from typing import Any, ClassVar, Dict, FrozenSet, List, Mapping, MutableMapping, NamedTuple, NoReturn, Sequence, Set, Tuple, Type

RESERVED_WORDS: Incomplete
LEGAL_CHARACTERS: Incomplete
LEGAL_CHARACTERS_PLUS_SPACE: Incomplete
ILLEGAL_INITIAL_CHARACTERS: Incomplete
FK_ON_DELETE: Incomplete
FK_ON_UPDATE: Incomplete
FK_INITIALLY: Incomplete
BIND_PARAMS: Incomplete
BIND_PARAMS_ESC: Incomplete
BIND_TEMPLATES: Incomplete
OPERATORS: Incomplete
FUNCTIONS: Dict[Type[Function[Any]], str]
EXTRACT_MAP: Incomplete
COMPOUND_KEYWORDS: Incomplete

class ResultColumnsEntry(NamedTuple):
    """Tracks a column expression that is expected to be represented
    in the result rows for this statement.

    This normally refers to the columns clause of a SELECT statement
    but may also refer to a RETURNING clause, as well as for dialect-specific
    emulations.

    """
    keyname: str
    name: str
    objects: Tuple[Any, ...]
    type: TypeEngine[Any]

class _ResultMapAppender(Protocol):
    def __call__(self, keyname: str, name: str, objects: Sequence[Any], type_: TypeEngine[Any]) -> None: ...

RM_RENDERED_NAME: Literal[0]
RM_NAME: Literal[1]
RM_OBJECTS: Literal[2]
RM_TYPE: Literal[3]

class _BaseCompilerStackEntry(TypedDict):
    asfrom_froms: Set[FromClause]
    correlate_froms: Set[FromClause]
    selectable: ReturnsRows

class _CompilerStackEntry(_BaseCompilerStackEntry, total=False):
    compile_state: CompileState
    need_result_map_for_nested: bool
    need_result_map_for_compound: bool
    select_0: ReturnsRows
    insert_from_select: Select[Any]

class ExpandedState(NamedTuple):
    '''represents state to use when producing "expanded" and
    "post compile" bound parameters for a statement.

    "expanded" parameters are parameters that are generated at
    statement execution time to suit a number of parameters passed, the most
    prominent example being the individual elements inside of an IN expression.

    "post compile" parameters are parameters where the SQL literal value
    will be rendered into the SQL statement at execution time, rather than
    being passed as separate parameters to the driver.

    To create an :class:`.ExpandedState` instance, use the
    :meth:`.SQLCompiler.construct_expanded_state` method on any
    :class:`.SQLCompiler` instance.

    '''
    statement: str
    parameters: _CoreSingleExecuteParams
    processors: Mapping[str, _BindProcessorType[Any]]
    positiontup: Sequence[str] | None
    parameter_expansion: Mapping[str, List[str]]
    @property
    def positional_parameters(self) -> Tuple[Any, ...]:
        """Tuple of positional parameters, for statements that were compiled
        using a positional paramstyle.

        """
    @property
    def additional_parameters(self) -> _CoreSingleExecuteParams:
        """synonym for :attr:`.ExpandedState.parameters`."""

class _InsertManyValues(NamedTuple):
    '''represents state to use for executing an "insertmanyvalues" statement.

    The primary consumers of this object are the
    :meth:`.SQLCompiler._deliver_insertmanyvalues_batches` and
    :meth:`.DefaultDialect._deliver_insertmanyvalues_batches` methods.

    .. versionadded:: 2.0

    '''
    is_default_expr: bool
    single_values_expr: str
    insert_crud_params: List[crud._CrudParamElementStr]
    num_positional_params_counted: int
    sort_by_parameter_order: bool = ...
    includes_upsert_behaviors: bool = ...
    sentinel_columns: Sequence[Column[Any]] | None = ...
    num_sentinel_columns: int = ...
    sentinel_param_keys: Sequence[str | int] | None = ...
    implicit_sentinel: bool = ...
    embed_values_counter: bool = ...

class _InsertManyValuesBatch(NamedTuple):
    """represents an individual batch SQL statement for insertmanyvalues.

    This is passed through the
    :meth:`.SQLCompiler._deliver_insertmanyvalues_batches` and
    :meth:`.DefaultDialect._deliver_insertmanyvalues_batches` methods out
    to the :class:`.Connection` within the
    :meth:`.Connection._exec_insertmany_context` method.

    .. versionadded:: 2.0.10

    """
    replaced_statement: str
    replaced_parameters: _DBAPIAnyExecuteParams
    processed_setinputsizes: _GenericSetInputSizesType | None
    batch: Sequence[_DBAPISingleExecuteParams]
    batch_size: int
    batchnum: int
    total_batches: int
    rows_sorted: bool
    is_downgraded: bool

class InsertmanyvaluesSentinelOpts(FastIntFlag):
    """bitflag enum indicating styles of PK defaults
    which can work as implicit sentinel columns

    """
    NOT_SUPPORTED: int
    AUTOINCREMENT: int
    IDENTITY: int
    SEQUENCE: int
    ANY_AUTOINCREMENT: Incomplete
    USE_INSERT_FROM_SELECT: int
    RENDER_SELECT_COL_CASTS: int

class CompilerState(IntEnum):
    COMPILING: int
    STRING_APPLIED: int
    NO_STATEMENT: int

class Linting(IntEnum):
    """represent preferences for the 'SQL linting' feature.

    this feature currently includes support for flagging cartesian products
    in SQL statements.

    """
    NO_LINTING: int
    COLLECT_CARTESIAN_PRODUCTS: int
    WARN_LINTING: int
    FROM_LINTING: Incomplete

NO_LINTING: Incomplete
COLLECT_CARTESIAN_PRODUCTS: Incomplete
WARN_LINTING: Incomplete
FROM_LINTING: Incomplete

class FromLinter(NamedTuple('FromLinter', [('froms', Incomplete), ('edges', Incomplete)])):
    '''represents current state for the "cartesian product" detection
    feature.'''
    def lint(self, start: Incomplete | None = None): ...
    def warn(self, stmt_type: str = 'SELECT') -> None: ...

class Compiled:
    """Represent a compiled SQL or DDL expression.

    The ``__str__`` method of the ``Compiled`` object should produce
    the actual text of the statement.  ``Compiled`` objects are
    specific to their underlying database dialect, and also may
    or may not be specific to the columns referenced within a
    particular set of bind parameters.  In no case should the
    ``Compiled`` object be dependent on the actual values of those
    bind parameters, even though it may reference those values as
    defaults.
    """
    statement: ClauseElement | None
    string: str
    state: CompilerState
    is_sql: bool
    is_ddl: bool
    schema_translate_map: SchemaTranslateMapType | None
    execution_options: _ExecuteOptions
    preparer: IdentifierPreparer
    compile_state: CompileState | None
    dml_compile_state: CompileState | None
    cache_key: CacheKey | None
    dialect: Incomplete
    can_execute: Incomplete
    def __init__(self, dialect: Dialect, statement: ClauseElement | None, schema_translate_map: SchemaTranslateMapType | None = None, render_schema_translate: bool = False, compile_kwargs: Mapping[str, Any] = ...) -> None:
        """Construct a new :class:`.Compiled` object.

        :param dialect: :class:`.Dialect` to compile against.

        :param statement: :class:`_expression.ClauseElement` to be compiled.

        :param schema_translate_map: dictionary of schema names to be
         translated when forming the resultant SQL

         .. seealso::

            :ref:`schema_translating`

        :param compile_kwargs: additional kwargs that will be
         passed to the initial call to :meth:`.Compiled.process`.


        """
    def __init_subclass__(cls) -> None: ...
    def visit_unsupported_compilation(self, element, err, **kw) -> None: ...
    @property
    def sql_compiler(self) -> None:
        """Return a Compiled that is capable of processing SQL expressions.

        If this compiler is one, it would likely just return 'self'.

        """
    def process(self, obj: Visitable, **kwargs: Any) -> str: ...
    def construct_params(self, params: _CoreSingleExecuteParams | None = None, extracted_parameters: Sequence[BindParameter[Any]] | None = None, escape_names: bool = True) -> _MutableCoreSingleExecuteParams | None:
        """Return the bind params for this compiled object.

        :param params: a dict of string/object pairs whose values will
                       override bind values compiled in to the
                       statement.
        """
    @property
    def params(self):
        """Return the bind params for this compiled object."""

class TypeCompiler(util.EnsureKWArg):
    """Produces DDL specification for TypeEngine objects."""
    ensure_kwarg: str
    dialect: Incomplete
    def __init__(self, dialect: Dialect) -> None: ...
    def process(self, type_: TypeEngine[Any], **kw: Any) -> str: ...
    def visit_unsupported_compilation(self, element: Any, err: Exception, **kw: Any) -> NoReturn: ...

class _CompileLabel(roles.BinaryElementRole[Any], elements.CompilerColumnElement):
    """lightweight label object which acts as an expression.Label."""
    __visit_name__: str
    element: Incomplete
    name: Incomplete
    def __init__(self, col, name, alt_names=()) -> None: ...
    @property
    def proxy_set(self): ...
    @property
    def type(self): ...
    def self_group(self, **kw): ...

class ilike_case_insensitive(roles.BinaryElementRole[Any], elements.CompilerColumnElement):
    '''produce a wrapping element for a case-insensitive portion of
    an ILIKE construct.

    The construct usually renders the ``lower()`` function, but on
    PostgreSQL will pass silently with the assumption that "ILIKE"
    is being used.

    .. versionadded:: 2.0

    '''
    __visit_name__: str
    element: Incomplete
    comparator: Incomplete
    def __init__(self, element) -> None: ...
    @property
    def proxy_set(self): ...
    @property
    def type(self): ...
    def self_group(self, **kw): ...

class SQLCompiler(Compiled):
    """Default implementation of :class:`.Compiled`.

    Compiles :class:`_expression.ClauseElement` objects into SQL strings.

    """
    extract_map = EXTRACT_MAP
    bindname_escape_characters: ClassVar[Mapping[str, str]]
    is_sql: bool
    compound_keywords = COMPOUND_KEYWORDS
    isdelete: bool
    isinsert: bool
    isupdate: bool
    postfetch: List[Column[Any]] | None
    insert_prefetch: Sequence[Column[Any]]
    update_prefetch: Sequence[Column[Any]]
    implicit_returning: Sequence[ColumnElement[Any]] | None
    isplaintext: bool
    binds: Dict[str, BindParameter[Any]]
    bind_names: Dict[BindParameter[Any], str]
    stack: List[_CompilerStackEntry]
    returning_precedes_values: bool
    render_table_with_column_in_update_from: bool
    ansi_bind_rules: bool
    bindtemplate: str
    compilation_bindtemplate: str
    literal_execute_params: FrozenSet[BindParameter[Any]]
    post_compile_params: FrozenSet[BindParameter[Any]]
    escaped_bind_names: util.immutabledict[str, str]
    has_out_parameters: bool
    postfetch_lastrowid: bool
    positiontup: List[str] | None
    inline: bool
    ctes: MutableMapping[CTE, str] | None
    ctes_by_level_name: Dict[Tuple[int, str], CTE]
    level_name_by_cte: Dict[CTE, Tuple[int, str, selectable._CTEOpts]]
    ctes_recursive: bool
    column_keys: Incomplete
    cache_key: Incomplete
    for_executemany: Incomplete
    linting: Incomplete
    positional: Incomplete
    label_length: Incomplete
    anon_map: Incomplete
    truncated_names: Incomplete
    def __init__(self, dialect: Dialect, statement: ClauseElement | None, cache_key: CacheKey | None = None, column_keys: Sequence[str] | None = None, for_executemany: bool = False, linting: Linting = ..., **kwargs: Any) -> None:
        '''Construct a new :class:`.SQLCompiler` object.

        :param dialect: :class:`.Dialect` to be used

        :param statement: :class:`_expression.ClauseElement` to be compiled

        :param column_keys:  a list of column names to be compiled into an
         INSERT or UPDATE statement.

        :param for_executemany: whether INSERT / UPDATE statements should
         expect that they are to be invoked in an "executemany" style,
         which may impact how the statement will be expected to return the
         values of defaults and autoincrement / sequences and similar.
         Depending on the backend and driver in use, support for retrieving
         these values may be disabled which means SQL expressions may
         be rendered inline, RETURNING may not be rendered, etc.

        :param kwargs: additional keyword arguments to be consumed by the
         superclass.

        '''
    @property
    def insert_single_values_expr(self) -> str | None:
        """When an INSERT is compiled with a single set of parameters inside
        a VALUES expression, the string is assigned here, where it can be
        used for insert batching schemes to rewrite the VALUES expression.

        .. versionadded:: 1.3.8

        .. versionchanged:: 2.0 This collection is no longer used by
           SQLAlchemy's built-in dialects, in favor of the currently
           internal ``_insertmanyvalues`` collection that is used only by
           :class:`.SQLCompiler`.

        """
    def effective_returning(self) -> Sequence[ColumnElement[Any]] | None:
        '''The effective "returning" columns for INSERT, UPDATE or DELETE.

        This is either the so-called "implicit returning" columns which are
        calculated by the compiler on the fly, or those present based on what\'s
        present in ``self.statement._returning`` (expanded into individual
        columns using the ``._all_selected_columns`` attribute) i.e. those set
        explicitly using the :meth:`.UpdateBase.returning` method.

        .. versionadded:: 2.0

        '''
    @property
    def returning(self):
        """backwards compatibility; returns the
        effective_returning collection.

        """
    @property
    def current_executable(self):
        '''Return the current \'executable\' that is being compiled.

        This is currently the :class:`_sql.Select`, :class:`_sql.Insert`,
        :class:`_sql.Update`, :class:`_sql.Delete`,
        :class:`_sql.CompoundSelect` object that is being compiled.
        Specifically it\'s assigned to the ``self.stack`` list of elements.

        When a statement like the above is being compiled, it normally
        is also assigned to the ``.statement`` attribute of the
        :class:`_sql.Compiler` object.   However, all SQL constructs are
        ultimately nestable, and this attribute should never be consulted
        by a ``visit_`` method, as it is not guaranteed to be assigned
        nor guaranteed to correspond to the current statement being compiled.

        .. versionadded:: 1.3.21

            For compatibility with previous versions, use the following
            recipe::

                statement = getattr(self, "current_executable", False)
                if statement is False:
                    statement = self.stack[-1]["selectable"]

            For versions 1.4 and above, ensure only .current_executable
            is used; the format of "self.stack" may change.


        '''
    @property
    def prefetch(self): ...
    def is_subquery(self): ...
    @property
    def sql_compiler(self): ...
    def construct_expanded_state(self, params: _CoreSingleExecuteParams | None = None, escape_names: bool = True) -> ExpandedState:
        '''Return a new :class:`.ExpandedState` for a given parameter set.

        For queries that use "expanding" or other late-rendered parameters,
        this method will provide for both the finalized SQL string as well
        as the parameters that would be used for a particular parameter set.

        .. versionadded:: 2.0.0rc1

        '''
    def construct_params(self, params: _CoreSingleExecuteParams | None = None, extracted_parameters: Sequence[BindParameter[Any]] | None = None, escape_names: bool = True, _group_number: int | None = None, _check: bool = True, _no_postcompile: bool = False) -> _MutableCoreSingleExecuteParams:
        """return a dictionary of bind parameter keys and values"""
    @property
    def params(self):
        """Return the bind param dictionary embedded into this
        compiled object, for those values that are present.

        .. seealso::

            :ref:`faq_sql_expression_string` - includes a usage example for
            debugging use cases.

        """
    def default_from(self):
        """Called when a SELECT statement has no froms, and no FROM clause is
        to be appended.

        Gives Oracle a chance to tack on a ``FROM DUAL`` to the string output.

        """
    def visit_grouping(self, grouping, asfrom: bool = False, **kwargs): ...
    def visit_select_statement_grouping(self, grouping, **kwargs): ...
    def visit_label_reference(self, element, within_columns_clause: bool = False, **kwargs): ...
    def visit_textual_label_reference(self, element, within_columns_clause: bool = False, **kwargs): ...
    def visit_label(self, label, add_to_result_map: Incomplete | None = None, within_label_clause: bool = False, within_columns_clause: bool = False, render_label_as_label: Incomplete | None = None, result_map_targets=(), **kw): ...
    def visit_lambda_element(self, element, **kw): ...
    def visit_column(self, column: ColumnClause[Any], add_to_result_map: _ResultMapAppender | None = None, include_table: bool = True, result_map_targets: Tuple[Any, ...] = (), ambiguous_table_name_map: _AmbiguousTableNameMap | None = None, **kwargs: Any) -> str: ...
    def visit_collation(self, element, **kw): ...
    def visit_fromclause(self, fromclause, **kwargs): ...
    def visit_index(self, index, **kwargs): ...
    def visit_typeclause(self, typeclause, **kw): ...
    def post_process_text(self, text): ...
    def escape_literal_column(self, text): ...
    def visit_textclause(self, textclause, add_to_result_map: Incomplete | None = None, **kw): ...
    def visit_textual_select(self, taf, compound_index: Incomplete | None = None, asfrom: bool = False, **kw): ...
    def visit_null(self, expr, **kw): ...
    def visit_true(self, expr, **kw): ...
    def visit_false(self, expr, **kw): ...
    def visit_tuple(self, clauselist, **kw): ...
    def visit_clauselist(self, clauselist, **kw): ...
    def visit_expression_clauselist(self, clauselist, **kw): ...
    def visit_case(self, clause, **kwargs): ...
    def visit_type_coerce(self, type_coerce, **kw): ...
    def visit_cast(self, cast, **kwargs): ...
    def visit_over(self, over, **kwargs): ...
    def visit_withingroup(self, withingroup, **kwargs): ...
    def visit_funcfilter(self, funcfilter, **kwargs): ...
    def visit_extract(self, extract, **kwargs): ...
    def visit_scalar_function_column(self, element, **kw): ...
    def visit_function(self, func: Function[Any], add_to_result_map: _ResultMapAppender | None = None, **kwargs: Any) -> str: ...
    def visit_next_value_func(self, next_value, **kw): ...
    def visit_sequence(self, sequence, **kw) -> None: ...
    def function_argspec(self, func, **kwargs): ...
    compile_state: Incomplete
    def visit_compound_select(self, cs, asfrom: bool = False, compound_index: Incomplete | None = None, **kwargs): ...
    def visit_unary(self, unary, add_to_result_map: Incomplete | None = None, result_map_targets=(), **kw): ...
    def visit_truediv_binary(self, binary, operator, **kw): ...
    def visit_floordiv_binary(self, binary, operator, **kw): ...
    def visit_is_true_unary_operator(self, element, operator, **kw): ...
    def visit_is_false_unary_operator(self, element, operator, **kw): ...
    def visit_not_match_op_binary(self, binary, operator, **kw): ...
    def visit_not_in_op_binary(self, binary, operator, **kw): ...
    def visit_empty_set_op_expr(self, type_, expand_op, **kw): ...
    def visit_empty_set_expr(self, element_types, **kw) -> None: ...
    def visit_binary(self, binary, override_operator: Incomplete | None = None, eager_grouping: bool = False, from_linter: Incomplete | None = None, lateral_from_linter: Incomplete | None = None, **kw): ...
    def visit_function_as_comparison_op_binary(self, element, operator, **kw): ...
    def visit_mod_binary(self, binary, operator, **kw): ...
    def visit_custom_op_binary(self, element, operator, **kw): ...
    def visit_custom_op_unary_operator(self, element, operator, **kw): ...
    def visit_custom_op_unary_modifier(self, element, operator, **kw): ...
    def visit_ilike_case_insensitive_operand(self, element, **kw): ...
    def visit_contains_op_binary(self, binary, operator, **kw): ...
    def visit_not_contains_op_binary(self, binary, operator, **kw): ...
    def visit_icontains_op_binary(self, binary, operator, **kw): ...
    def visit_not_icontains_op_binary(self, binary, operator, **kw): ...
    def visit_startswith_op_binary(self, binary, operator, **kw): ...
    def visit_not_startswith_op_binary(self, binary, operator, **kw): ...
    def visit_istartswith_op_binary(self, binary, operator, **kw): ...
    def visit_not_istartswith_op_binary(self, binary, operator, **kw): ...
    def visit_endswith_op_binary(self, binary, operator, **kw): ...
    def visit_not_endswith_op_binary(self, binary, operator, **kw): ...
    def visit_iendswith_op_binary(self, binary, operator, **kw): ...
    def visit_not_iendswith_op_binary(self, binary, operator, **kw): ...
    def visit_like_op_binary(self, binary, operator, **kw): ...
    def visit_not_like_op_binary(self, binary, operator, **kw): ...
    def visit_ilike_op_binary(self, binary, operator, **kw): ...
    def visit_not_ilike_op_binary(self, binary, operator, **kw): ...
    def visit_between_op_binary(self, binary, operator, **kw): ...
    def visit_not_between_op_binary(self, binary, operator, **kw): ...
    def visit_regexp_match_op_binary(self, binary, operator, **kw) -> None: ...
    def visit_not_regexp_match_op_binary(self, binary, operator, **kw) -> None: ...
    def visit_regexp_replace_op_binary(self, binary, operator, **kw) -> None: ...
    def visit_bindparam(self, bindparam, within_columns_clause: bool = False, literal_binds: bool = False, skip_bind_expression: bool = False, literal_execute: bool = False, render_postcompile: bool = False, **kwargs): ...
    def render_bind_cast(self, type_, dbapi_type, sqltext) -> None: ...
    def render_literal_bindparam(self, bindparam, render_literal_value=..., bind_expression_template: Incomplete | None = None, **kw): ...
    def render_literal_value(self, value, type_):
        """Render the value of a bind parameter as a quoted literal.

        This is used for statement sections that do not accept bind parameters
        on the target driver/database.

        This should be implemented by subclasses using the quoting services
        of the DBAPI.

        """
    def bindparam_string(self, name: str, post_compile: bool = False, expanding: bool = False, escaped_from: str | None = None, bindparam_type: TypeEngine[Any] | None = None, accumulate_bind_names: Set[str] | None = None, visited_bindparam: List[str] | None = None, **kw: Any) -> str: ...
    def visit_cte(self, cte: CTE, asfrom: bool = False, ashint: bool = False, fromhints: _FromHintsType | None = None, visiting_cte: CTE | None = None, from_linter: FromLinter | None = None, cte_opts: selectable._CTEOpts = ..., **kwargs: Any) -> str | None: ...
    def visit_table_valued_alias(self, element, **kw): ...
    def visit_table_valued_column(self, element, **kw): ...
    def visit_alias(self, alias, asfrom: bool = False, ashint: bool = False, iscrud: bool = False, fromhints: Incomplete | None = None, subquery: bool = False, lateral: bool = False, enclosing_alias: Incomplete | None = None, from_linter: Incomplete | None = None, **kwargs): ...
    def visit_subquery(self, subquery, **kw): ...
    def visit_lateral(self, lateral_, **kw): ...
    def visit_tablesample(self, tablesample, asfrom: bool = False, **kw): ...
    def visit_values(self, element, asfrom: bool = False, from_linter: Incomplete | None = None, **kw): ...
    def visit_scalar_values(self, element, **kw): ...
    def get_render_as_alias_suffix(self, alias_name_text): ...
    def format_from_hint_text(self, sqltext, table, hint, iscrud): ...
    def get_select_hint_text(self, byfroms) -> None: ...
    def get_from_hint_text(self, table, text) -> None: ...
    def get_crud_hint_text(self, table, text) -> None: ...
    def get_statement_hint_text(self, hint_texts): ...
    translate_select_structure: Any
    def visit_select(self, select_stmt, asfrom: bool = False, insert_into: bool = False, fromhints: Incomplete | None = None, compound_index: Incomplete | None = None, select_wraps_for: Incomplete | None = None, lateral: bool = False, from_linter: Incomplete | None = None, **kwargs): ...
    def get_cte_preamble(self, recursive): ...
    def get_select_precolumns(self, select, **kw):
        """Called when building a ``SELECT`` statement, position is just
        before column list.

        """
    def group_by_clause(self, select, **kw):
        """allow dialects to customize how GROUP BY is rendered."""
    def order_by_clause(self, select, **kw):
        """allow dialects to customize how ORDER BY is rendered."""
    def for_update_clause(self, select, **kw): ...
    def returning_clause(self, stmt: UpdateBase, returning_cols: Sequence[ColumnElement[Any]], *, populate_result_map: bool, **kw: Any) -> str: ...
    def limit_clause(self, select, **kw): ...
    def fetch_clause(self, select, fetch_clause: Incomplete | None = None, require_offset: bool = False, use_literal_execute_for_simple_int: bool = False, **kw): ...
    def visit_table(self, table, asfrom: bool = False, iscrud: bool = False, ashint: bool = False, fromhints: Incomplete | None = None, use_schema: bool = True, from_linter: Incomplete | None = None, ambiguous_table_name_map: Incomplete | None = None, **kwargs): ...
    def visit_join(self, join, asfrom: bool = False, from_linter: Incomplete | None = None, **kwargs): ...
    dml_compile_state: Incomplete
    def visit_insert(self, insert_stmt, visited_bindparam: Incomplete | None = None, **kw): ...
    def update_limit_clause(self, update_stmt) -> None:
        """Provide a hook for MySQL to add LIMIT to the UPDATE"""
    def update_tables_clause(self, update_stmt, from_table, extra_froms, **kw):
        """Provide a hook to override the initial table clause
        in an UPDATE statement.

        MySQL overrides this.

        """
    def update_from_clause(self, update_stmt, from_table, extra_froms, from_hints, **kw) -> None:
        """Provide a hook to override the generation of an
        UPDATE..FROM clause.

        MySQL and MSSQL override this.

        """
    from_linter: Incomplete
    def visit_update(self, update_stmt, **kw): ...
    def delete_extra_from_clause(self, update_stmt, from_table, extra_froms, from_hints, **kw) -> None:
        """Provide a hook to override the generation of an
        DELETE..FROM clause.

        This can be used to implement DELETE..USING for example.

        MySQL and MSSQL override this.

        """
    def delete_table_clause(self, delete_stmt, from_table, extra_froms, **kw): ...
    def visit_delete(self, delete_stmt, **kw): ...
    def visit_savepoint(self, savepoint_stmt, **kw): ...
    def visit_rollback_to_savepoint(self, savepoint_stmt, **kw): ...
    def visit_release_savepoint(self, savepoint_stmt, **kw): ...

class StrSQLCompiler(SQLCompiler):
    """A :class:`.SQLCompiler` subclass which allows a small selection
    of non-standard SQL features to render into a string value.

    The :class:`.StrSQLCompiler` is invoked whenever a Core expression
    element is directly stringified without calling upon the
    :meth:`_expression.ClauseElement.compile` method.
    It can render a limited set
    of non-standard SQL constructs to assist in basic stringification,
    however for more substantial custom or dialect-specific SQL constructs,
    it will be necessary to make use of
    :meth:`_expression.ClauseElement.compile`
    directly.

    .. seealso::

        :ref:`faq_sql_expression_string`

    """
    def visit_unsupported_compilation(self, element, err, **kw): ...
    def visit_getitem_binary(self, binary, operator, **kw): ...
    def visit_json_getitem_op_binary(self, binary, operator, **kw): ...
    def visit_json_path_getitem_op_binary(self, binary, operator, **kw): ...
    def visit_sequence(self, seq, **kw): ...
    def returning_clause(self, stmt: UpdateBase, returning_cols: Sequence[ColumnElement[Any]], *, populate_result_map: bool, **kw: Any) -> str: ...
    def update_from_clause(self, update_stmt, from_table, extra_froms, from_hints, **kw): ...
    def delete_extra_from_clause(self, update_stmt, from_table, extra_froms, from_hints, **kw): ...
    def visit_empty_set_expr(self, type_, **kw): ...
    def get_from_hint_text(self, table, text): ...
    def visit_regexp_match_op_binary(self, binary, operator, **kw): ...
    def visit_not_regexp_match_op_binary(self, binary, operator, **kw): ...
    def visit_regexp_replace_op_binary(self, binary, operator, **kw): ...
    def visit_try_cast(self, cast, **kwargs): ...

class DDLCompiler(Compiled):
    is_ddl: bool
    def __init__(self, dialect: Dialect, statement: ExecutableDDLElement, schema_translate_map: SchemaTranslateMapType | None = ..., render_schema_translate: bool = ..., compile_kwargs: Mapping[str, Any] = ...) -> None: ...
    def sql_compiler(self): ...
    def type_compiler(self): ...
    def construct_params(self, params: _CoreSingleExecuteParams | None = None, extracted_parameters: Sequence[BindParameter[Any]] | None = None, escape_names: bool = True) -> _MutableCoreSingleExecuteParams | None: ...
    def visit_ddl(self, ddl, **kwargs): ...
    def visit_create_schema(self, create, **kw): ...
    def visit_drop_schema(self, drop, **kw): ...
    def visit_create_table(self, create, **kw): ...
    def visit_create_column(self, create, first_pk: bool = False, **kw): ...
    def create_table_constraints(self, table, _include_foreign_key_constraints: Incomplete | None = None, **kw): ...
    def visit_drop_table(self, drop, **kw): ...
    def visit_drop_view(self, drop, **kw): ...
    def visit_create_index(self, create, include_schema: bool = False, include_table_schema: bool = True, **kw): ...
    def visit_drop_index(self, drop, **kw): ...
    def visit_add_constraint(self, create, **kw): ...
    def visit_set_table_comment(self, create, **kw): ...
    def visit_drop_table_comment(self, drop, **kw): ...
    def visit_set_column_comment(self, create, **kw): ...
    def visit_drop_column_comment(self, drop, **kw): ...
    def visit_set_constraint_comment(self, create, **kw) -> None: ...
    def visit_drop_constraint_comment(self, drop, **kw) -> None: ...
    def get_identity_options(self, identity_options): ...
    def visit_create_sequence(self, create, prefix: Incomplete | None = None, **kw): ...
    def visit_drop_sequence(self, drop, **kw): ...
    def visit_drop_constraint(self, drop, **kw): ...
    def get_column_specification(self, column, **kwargs): ...
    def create_table_suffix(self, table): ...
    def post_create_table(self, table): ...
    def get_column_default_string(self, column): ...
    def render_default_string(self, default): ...
    def visit_table_or_column_check_constraint(self, constraint, **kw): ...
    def visit_check_constraint(self, constraint, **kw): ...
    def visit_column_check_constraint(self, constraint, **kw): ...
    def visit_primary_key_constraint(self, constraint, **kw): ...
    def visit_foreign_key_constraint(self, constraint, **kw): ...
    def define_constraint_remote_table(self, constraint, table, preparer):
        """Format the remote table clause of a CREATE CONSTRAINT clause."""
    def visit_unique_constraint(self, constraint, **kw): ...
    def define_unique_constraint_distinct(self, constraint, **kw): ...
    def define_constraint_cascades(self, constraint): ...
    def define_constraint_deferrability(self, constraint): ...
    def define_constraint_match(self, constraint): ...
    def visit_computed_column(self, generated, **kw): ...
    def visit_identity_column(self, identity, **kw): ...

class GenericTypeCompiler(TypeCompiler):
    def visit_FLOAT(self, type_, **kw): ...
    def visit_DOUBLE(self, type_, **kw): ...
    def visit_DOUBLE_PRECISION(self, type_, **kw): ...
    def visit_REAL(self, type_, **kw): ...
    def visit_NUMERIC(self, type_, **kw): ...
    def visit_DECIMAL(self, type_, **kw): ...
    def visit_INTEGER(self, type_, **kw): ...
    def visit_SMALLINT(self, type_, **kw): ...
    def visit_BIGINT(self, type_, **kw): ...
    def visit_TIMESTAMP(self, type_, **kw): ...
    def visit_DATETIME(self, type_, **kw): ...
    def visit_DATE(self, type_, **kw): ...
    def visit_TIME(self, type_, **kw): ...
    def visit_CLOB(self, type_, **kw): ...
    def visit_NCLOB(self, type_, **kw): ...
    def visit_CHAR(self, type_, **kw): ...
    def visit_NCHAR(self, type_, **kw): ...
    def visit_VARCHAR(self, type_, **kw): ...
    def visit_NVARCHAR(self, type_, **kw): ...
    def visit_TEXT(self, type_, **kw): ...
    def visit_BLOB(self, type_, **kw): ...
    def visit_BINARY(self, type_, **kw): ...
    def visit_VARBINARY(self, type_, **kw): ...
    def visit_BOOLEAN(self, type_, **kw): ...
    def visit_uuid(self, type_, **kw): ...
    def visit_large_binary(self, type_, **kw): ...
    def visit_boolean(self, type_, **kw): ...
    def visit_time(self, type_, **kw): ...
    def visit_datetime(self, type_, **kw): ...
    def visit_date(self, type_, **kw): ...
    def visit_big_integer(self, type_, **kw): ...
    def visit_small_integer(self, type_, **kw): ...
    def visit_integer(self, type_, **kw): ...
    def visit_real(self, type_, **kw): ...
    def visit_float(self, type_, **kw): ...
    def visit_double(self, type_, **kw): ...
    def visit_numeric(self, type_, **kw): ...
    def visit_string(self, type_, **kw): ...
    def visit_unicode(self, type_, **kw): ...
    def visit_text(self, type_, **kw): ...
    def visit_unicode_text(self, type_, **kw): ...
    def visit_enum(self, type_, **kw): ...
    def visit_null(self, type_, **kw) -> None: ...
    def visit_type_decorator(self, type_, **kw): ...
    def visit_user_defined(self, type_, **kw): ...

class StrSQLTypeCompiler(GenericTypeCompiler):
    def process(self, type_, **kw): ...
    def __getattr__(self, key): ...
    def visit_null(self, type_, **kw): ...
    def visit_user_defined(self, type_, **kw): ...

class _SchemaForObjectCallable(Protocol):
    def __call__(self, obj: Any) -> str: ...

class _BindNameForColProtocol(Protocol):
    def __call__(self, col: ColumnClause[Any]) -> str: ...

class IdentifierPreparer:
    """Handle quoting and case-folding of identifiers based on options."""
    reserved_words = RESERVED_WORDS
    legal_characters = LEGAL_CHARACTERS
    illegal_initial_characters = ILLEGAL_INITIAL_CHARACTERS
    initial_quote: str
    final_quote: str
    schema_for_object: _SchemaForObjectCallable
    dialect: Incomplete
    escape_quote: Incomplete
    escape_to_quote: Incomplete
    omit_schema: Incomplete
    quote_case_sensitive_collations: Incomplete
    def __init__(self, dialect, initial_quote: str = '"', final_quote: Incomplete | None = None, escape_quote: str = '"', quote_case_sensitive_collations: bool = True, omit_schema: bool = False) -> None:
        """Construct a new ``IdentifierPreparer`` object.

        initial_quote
          Character that begins a delimited identifier.

        final_quote
          Character that ends a delimited identifier. Defaults to
          `initial_quote`.

        omit_schema
          Prevent prepending schema name. Useful for databases that do
          not support schemae.
        """
    def validate_sql_phrase(self, element, reg):
        '''keyword sequence filter.

        a filter for elements that are intended to represent keyword sequences,
        such as "INITIALLY", "INITIALLY DEFERRED", etc.   no special characters
        should be present.

        .. versionadded:: 1.3

        '''
    def quote_identifier(self, value: str) -> str:
        """Quote an identifier.

        Subclasses should override this to provide database-dependent
        quoting behavior.
        """
    def quote_schema(self, schema: str, force: Any = None) -> str:
        """Conditionally quote a schema name.


        The name is quoted if it is a reserved word, contains quote-necessary
        characters, or is an instance of :class:`.quoted_name` which includes
        ``quote`` set to ``True``.

        Subclasses can override this to provide database-dependent
        quoting behavior for schema names.

        :param schema: string schema name
        :param force: unused

            .. deprecated:: 0.9

                The :paramref:`.IdentifierPreparer.quote_schema.force`
                parameter is deprecated and will be removed in a future
                release.  This flag has no effect on the behavior of the
                :meth:`.IdentifierPreparer.quote` method; please refer to
                :class:`.quoted_name`.

        """
    def quote(self, ident: str, force: Any = None) -> str:
        """Conditionally quote an identifier.

        The identifier is quoted if it is a reserved word, contains
        quote-necessary characters, or is an instance of
        :class:`.quoted_name` which includes ``quote`` set to ``True``.

        Subclasses can override this to provide database-dependent
        quoting behavior for identifier names.

        :param ident: string identifier
        :param force: unused

            .. deprecated:: 0.9

                The :paramref:`.IdentifierPreparer.quote.force`
                parameter is deprecated and will be removed in a future
                release.  This flag has no effect on the behavior of the
                :meth:`.IdentifierPreparer.quote` method; please refer to
                :class:`.quoted_name`.

        """
    def format_collation(self, collation_name): ...
    def format_sequence(self, sequence, use_schema: bool = True): ...
    def format_label(self, label: Label[Any], name: str | None = None) -> str: ...
    def format_alias(self, alias: AliasedReturnsRows | None, name: str | None = None) -> str: ...
    def format_savepoint(self, savepoint, name: Incomplete | None = None): ...
    def format_constraint(self, constraint, _alembic_quote: bool = True): ...
    def truncate_and_render_index_name(self, name, _alembic_quote: bool = True): ...
    def truncate_and_render_constraint_name(self, name, _alembic_quote: bool = True): ...
    def format_index(self, index): ...
    def format_table(self, table, use_schema: bool = True, name: Incomplete | None = None):
        """Prepare a quoted table and schema name."""
    def format_schema(self, name):
        """Prepare a quoted schema name."""
    def format_label_name(self, name, anon_map: Incomplete | None = None):
        """Prepare a quoted column name."""
    def format_column(self, column, use_table: bool = False, name: Incomplete | None = None, table_name: Incomplete | None = None, use_schema: bool = False, anon_map: Incomplete | None = None):
        """Prepare a quoted column name."""
    def format_table_seq(self, table, use_schema: bool = True):
        """Format table name and schema as a tuple."""
    def unformat_identifiers(self, identifiers):
        """Unpack 'schema.table.column'-like strings into components."""
