from . import attributes as attributes, interfaces as interfaces, loading as loading
from .. import future as future, inspect as inspect, sql as sql, util as util
from ..engine import Result as Result
from ..engine.interfaces import _CoreSingleExecuteParams
from ..sql import coercions as coercions, expression as expression, roles as roles, visitors as visitors
from ..sql._typing import _ColumnsClauseArgument, _TP, is_dml as is_dml, is_insert_update as is_insert_update, is_select_base as is_select_base
from ..sql.base import CacheableOptions as CacheableOptions, CompileState as CompileState, Executable as Executable, Generative as Generative, Options as Options
from ..sql.compiler import SQLCompiler as SQLCompiler
from ..sql.dml import UpdateBase as UpdateBase, _DMLTableElement
from ..sql.elements import ColumnElement as ColumnElement, GroupedElement as GroupedElement, TextClause as TextClause
from ..sql.selectable import CompoundSelectState as CompoundSelectState, ExecutableReturnsRows as ExecutableReturnsRows, LABEL_STYLE_DISAMBIGUATE_ONLY as LABEL_STYLE_DISAMBIGUATE_ONLY, LABEL_STYLE_NONE as LABEL_STYLE_NONE, LABEL_STYLE_TABLENAME_PLUS_COL as LABEL_STYLE_TABLENAME_PLUS_COL, Select as Select, SelectBase as SelectBase, SelectLabelStyle as SelectLabelStyle, SelectState as SelectState, TypedReturnsRows as TypedReturnsRows
from ..sql.type_api import TypeEngine as TypeEngine
from ..sql.visitors import InternalTraversal as InternalTraversal
from ._typing import OrmExecuteOptionsParameter as OrmExecuteOptionsParameter, _InternalEntityType
from .interfaces import ORMColumnDescription as ORMColumnDescription, ORMColumnsClauseRole as ORMColumnsClauseRole
from .loading import PostLoad as PostLoad
from .mapper import Mapper as Mapper
from .path_registry import PathRegistry as PathRegistry
from .query import Query as Query
from .session import Session as Session, _BindArguments
from .util import AliasedClass as AliasedClass, Bundle as Bundle, ORMAdapter as ORMAdapter, ORMStatementAdapter as ORMStatementAdapter
from _typeshed import Incomplete
from collections.abc import Generator
from typing import Any, Dict, Iterable, List, Set, Tuple, Type

LABEL_STYLE_LEGACY_ORM: Incomplete

class QueryContext:
    runid: int
    post_load_paths: Dict[PathRegistry, PostLoad]
    compile_state: ORMCompileState
    class default_load_options(Options): ...
    load_options: Incomplete
    execution_options: Incomplete
    bind_arguments: Incomplete
    query: Incomplete
    session: Incomplete
    loaders_require_buffering: bool
    loaders_require_uniquing: bool
    params: Incomplete
    top_level_context: Incomplete
    propagated_loader_options: Incomplete
    attributes: Incomplete
    autoflush: Incomplete
    populate_existing: Incomplete
    invoke_all_eagers: Incomplete
    version_check: Incomplete
    refresh_state: Incomplete
    yield_per: Incomplete
    identity_token: Incomplete
    def __init__(self, compile_state: CompileState, statement: Select[Any] | FromStatement[Any], params: _CoreSingleExecuteParams, session: Session, load_options: Type[QueryContext.default_load_options] | QueryContext.default_load_options, execution_options: OrmExecuteOptionsParameter | None = None, bind_arguments: _BindArguments | None = None) -> None: ...

class AbstractORMCompileState(CompileState):
    is_dml_returning: bool
    @classmethod
    def create_for_statement(cls, statement: Select | FromStatement, compiler: SQLCompiler | None, **kw: Any) -> AbstractORMCompileState:
        '''Create a context for a statement given a :class:`.Compiler`.

        This method is always invoked in the context of SQLCompiler.process().

        For a Select object, this would be invoked from
        SQLCompiler.visit_select(). For the special FromStatement object used
        by Query to indicate "Query.from_statement()", this is called by
        FromStatement._compiler_dispatch() that would be called by
        SQLCompiler.process().
        '''
    @classmethod
    def orm_pre_session_exec(cls, session, statement, params, execution_options, bind_arguments, is_pre_event) -> None: ...
    @classmethod
    def orm_execute_statement(cls, session, statement, params, execution_options, bind_arguments, conn) -> Result: ...
    @classmethod
    def orm_setup_cursor_result(cls, session, statement, params, execution_options, bind_arguments, result) -> None: ...

class AutoflushOnlyORMCompileState(AbstractORMCompileState):
    """ORM compile state that is a passthrough, except for autoflush."""
    @classmethod
    def orm_pre_session_exec(cls, session, statement, params, execution_options, bind_arguments, is_pre_event): ...
    @classmethod
    def orm_setup_cursor_result(cls, session, statement, params, execution_options, bind_arguments, result): ...

class ORMCompileState(AbstractORMCompileState):
    class default_compile_options(CacheableOptions): ...
    attributes: Dict[Any, Any]
    global_attributes: Dict[Any, Any]
    statement: Select[Any] | FromStatement[Any]
    select_statement: Select[Any] | FromStatement[Any]
    compile_options: Type[default_compile_options] | default_compile_options
    use_legacy_query_style: bool
    primary_columns: List[ColumnElement[Any]]
    secondary_columns: List[ColumnElement[Any]]
    dedupe_columns: Set[ColumnElement[Any]]
    create_eager_joins: List[Tuple[Any, ...]]
    current_path: PathRegistry
    def __init__(self, *arg, **kw) -> None: ...
    @classmethod
    def create_for_statement(cls, statement: Select | FromStatement, compiler: SQLCompiler | None, **kw: Any) -> ORMCompileState: ...
    @classmethod
    def get_column_descriptions(cls, statement): ...
    @classmethod
    def orm_pre_session_exec(cls, session, statement, params, execution_options, bind_arguments, is_pre_event): ...
    @classmethod
    def orm_setup_cursor_result(cls, session, statement, params, execution_options, bind_arguments, result): ...

class DMLReturningColFilter:
    """an adapter used for the DML RETURNING case.

    Has a subset of the interface used by
    :class:`.ORMAdapter` and is used for :class:`._QueryEntity`
    instances to set up their columns as used in RETURNING for a
    DML statement.

    """
    mapper: Incomplete
    columns: Incomplete
    def __init__(self, target_mapper, immediate_dml_mapper) -> None: ...
    def __call__(self, col, as_filter): ...
    def adapt_check_present(self, col): ...

class ORMFromStatementCompileState(ORMCompileState):
    statement_container: FromStatement
    requested_statement: SelectBase | TextClause | UpdateBase
    dml_table: _DMLTableElement | None
    multi_row_eager_loaders: bool
    eager_adding_joins: bool
    compound_eager_adapter: Incomplete
    extra_criteria_entities: Incomplete
    eager_joins: Incomplete
    use_legacy_query_style: Incomplete
    is_dml_returning: bool
    compile_options: Incomplete
    statement: Incomplete
    current_path: Incomplete
    primary_columns: Incomplete
    secondary_columns: Incomplete
    dedupe_columns: Incomplete
    create_eager_joins: Incomplete
    order_by: Incomplete
    @classmethod
    def create_for_statement(cls, statement_container: Select | FromStatement, compiler: SQLCompiler | None, **kw: Any) -> ORMFromStatementCompileState: ...
    def setup_dml_returning_compile_state(self, dml_mapper) -> None:
        """used by BulkORMInsert (and Update / Delete?) to set up a handler
        for RETURNING to return ORM objects and expressions

        """

class FromStatement(GroupedElement, Generative, TypedReturnsRows[_TP]):
    """Core construct that represents a load of ORM objects from various
    :class:`.ReturnsRows` and other classes including:

    :class:`.Select`, :class:`.TextClause`, :class:`.TextualSelect`,
    :class:`.CompoundSelect`, :class`.Insert`, :class:`.Update`,
    and in theory, :class:`.Delete`.

    """
    __visit_name__: str
    element: ExecutableReturnsRows | TextClause
    is_dml: Incomplete
    def __init__(self, entities: Iterable[_ColumnsClauseArgument[Any]], element: ExecutableReturnsRows | TextClause, _adapt_on_names: bool = True) -> None: ...
    @property
    def column_descriptions(self):
        """Return a :term:`plugin-enabled` 'column descriptions' structure
        referring to the columns which are SELECTed by this statement.

        See the section :ref:`queryguide_inspection` for an overview
        of this feature.

        .. seealso::

            :ref:`queryguide_inspection` - ORM background

        """
    def get_children(self, **kw) -> Generator[Incomplete, Incomplete, None]: ...

class CompoundSelectCompileState(AutoflushOnlyORMCompileState, CompoundSelectState): ...

class ORMSelectCompileState(ORMCompileState, SelectState):
    multi_row_eager_loaders: bool
    eager_adding_joins: bool
    compound_eager_adapter: Incomplete
    correlate: Incomplete
    correlate_except: Incomplete
    select_statement: Incomplete
    for_statement: Incomplete
    use_legacy_query_style: Incomplete
    compile_options: Incomplete
    label_style: Incomplete
    current_path: Incomplete
    eager_order_by: Incomplete
    primary_columns: Incomplete
    secondary_columns: Incomplete
    dedupe_columns: Incomplete
    eager_joins: Incomplete
    extra_criteria_entities: Incomplete
    create_eager_joins: Incomplete
    from_clauses: Incomplete
    @classmethod
    def create_for_statement(cls, statement: Select | FromStatement, compiler: SQLCompiler | None, **kw: Any) -> ORMSelectCompileState:
        """compiler hook, we arrive here from compiler.visit_select() only."""
    @classmethod
    def determine_last_joined_entity(cls, statement): ...
    @classmethod
    def all_selected_columns(cls, statement) -> Generator[Incomplete, Incomplete, None]: ...
    @classmethod
    def get_columns_clause_froms(cls, statement): ...
    @classmethod
    def from_statement(cls, statement, from_statement): ...

class _QueryEntity:
    """represent an entity column returned within a Query result."""
    supports_single_entity: bool
    use_id_for_hash: bool
    type: Type[Any] | TypeEngine[Any]
    expr: _InternalEntityType | ColumnElement[Any]
    entity_zero: _InternalEntityType | None
    def setup_compile_state(self, compile_state: ORMCompileState) -> None: ...
    def setup_dml_returning_compile_state(self, compile_state: ORMCompileState, adapter: DMLReturningColFilter) -> None: ...
    def row_processor(self, context, result) -> None: ...
    @classmethod
    def to_compile_state(cls, compile_state, entities, entities_collection, is_current_entities): ...

class _MapperEntity(_QueryEntity):
    """mapper/class/AliasedClass entity"""
    expr: _InternalEntityType
    mapper: Mapper[Any]
    entity_zero: _InternalEntityType
    is_aliased_class: bool
    path: PathRegistry
    selectable: Incomplete
    def __init__(self, compile_state, entity, entities_collection, is_current_entities) -> None: ...
    supports_single_entity: bool
    use_id_for_hash: bool
    @property
    def type(self): ...
    @property
    def entity_zero_or_selectable(self): ...
    def corresponds_to(self, entity): ...
    def row_processor(self, context, result): ...
    def setup_dml_returning_compile_state(self, compile_state: ORMCompileState, adapter: DMLReturningColFilter) -> None: ...
    def setup_compile_state(self, compile_state) -> None: ...

class _BundleEntity(_QueryEntity):
    bundle: Bundle
    type: Type[Any]
    supports_single_entity: bool
    expr: Bundle
    def __init__(self, compile_state, expr, entities_collection, is_current_entities, setup_entities: bool = True, parent_bundle: Incomplete | None = None) -> None: ...
    @property
    def mapper(self): ...
    @property
    def entity_zero(self): ...
    def corresponds_to(self, entity): ...
    @property
    def entity_zero_or_selectable(self): ...
    def setup_compile_state(self, compile_state) -> None: ...
    def row_processor(self, context, result): ...

class _ColumnEntity(_QueryEntity):
    @property
    def type(self): ...
    def row_processor(self, context, result): ...

class _RawColumnEntity(_ColumnEntity):
    entity_zero: Incomplete
    mapper: Incomplete
    supports_single_entity: bool
    expr: Incomplete
    raw_column_index: Incomplete
    translate_raw_column: Incomplete
    column: Incomplete
    entity_zero_or_selectable: Incomplete
    def __init__(self, compile_state, column, entities_collection, raw_column_index, is_current_entities, parent_bundle: Incomplete | None = None) -> None: ...
    def corresponds_to(self, entity): ...
    def setup_dml_returning_compile_state(self, compile_state: ORMCompileState, adapter: DMLReturningColFilter) -> None: ...
    def setup_compile_state(self, compile_state) -> None: ...

class _ORMColumnEntity(_ColumnEntity):
    """Column/expression based entity."""
    supports_single_entity: bool
    expr: Incomplete
    translate_raw_column: bool
    raw_column_index: Incomplete
    entity_zero: Incomplete
    mapper: Incomplete
    column: Incomplete
    def __init__(self, compile_state, column, entities_collection, parententity, raw_column_index, is_current_entities, parent_bundle: Incomplete | None = None) -> None: ...
    def corresponds_to(self, entity): ...
    def setup_dml_returning_compile_state(self, compile_state: ORMCompileState, adapter: DMLReturningColFilter) -> None: ...
    def setup_compile_state(self, compile_state) -> None: ...

class _IdentityTokenEntity(_ORMColumnEntity):
    translate_raw_column: bool
    def setup_compile_state(self, compile_state) -> None: ...
    def row_processor(self, context, result): ...
