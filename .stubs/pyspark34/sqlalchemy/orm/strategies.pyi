from . import attributes as attributes, interfaces as interfaces, loading as loading, path_registry as path_registry, properties as properties, query as query, relationships as relationships, unitofwork as unitofwork
from .. import event as event, inspect as inspect, log as log, sql as sql, util as util
from ..sql import visitors as visitors
from ..sql.elements import ColumnElement as ColumnElement
from ..sql.selectable import LABEL_STYLE_TABLENAME_PLUS_COL as LABEL_STYLE_TABLENAME_PLUS_COL, Select as Select
from .base import ATTR_WAS_SET as ATTR_WAS_SET, LoaderCallableStatus as LoaderCallableStatus, PASSIVE_OFF as PASSIVE_OFF, PassiveFlag as PassiveFlag
from .context import ORMCompileState as ORMCompileState, ORMSelectCompileState as ORMSelectCompileState, QueryContext as QueryContext
from .interfaces import LoaderStrategy as LoaderStrategy, StrategizedProperty as StrategizedProperty
from .relationships import RelationshipProperty as RelationshipProperty
from .state import InstanceState as InstanceState
from .strategy_options import Load as Load
from .util import AliasedClass as AliasedClass
from _typeshed import Incomplete
from typing import Any, NamedTuple, Tuple

class UninstrumentedColumnLoader(LoaderStrategy):
    """Represent a non-instrumented MapperProperty.

    The polymorphic_on argument of mapper() often results in this,
    if the argument is against the with_polymorphic selectable.

    """
    columns: Incomplete
    def __init__(self, parent, strategy_key) -> None: ...
    def setup_query(self, compile_state, query_entity, path, loadopt, adapter, column_collection: Incomplete | None = None, **kwargs) -> None: ...
    def create_row_processor(self, context, query_entity, path, loadopt, mapper, result, adapter, populators) -> None: ...

class ColumnLoader(LoaderStrategy):
    """Provide loading behavior for a :class:`.ColumnProperty`."""
    columns: Incomplete
    is_composite: Incomplete
    def __init__(self, parent, strategy_key) -> None: ...
    def setup_query(self, compile_state, query_entity, path, loadopt, adapter, column_collection, memoized_populators, check_for_adapt: bool = False, **kwargs) -> None: ...
    is_class_level: bool
    def init_class_attribute(self, mapper) -> None: ...
    def create_row_processor(self, context, query_entity, path, loadopt, mapper, result, adapter, populators) -> None: ...

class ExpressionColumnLoader(ColumnLoader):
    def __init__(self, parent, strategy_key) -> None: ...
    def setup_query(self, compile_state, query_entity, path, loadopt, adapter, column_collection, memoized_populators, **kwargs) -> None: ...
    def create_row_processor(self, context, query_entity, path, loadopt, mapper, result, adapter, populators) -> None: ...
    is_class_level: bool
    def init_class_attribute(self, mapper) -> None: ...

class DeferredColumnLoader(LoaderStrategy):
    """Provide loading behavior for a deferred :class:`.ColumnProperty`."""
    raiseload: Incomplete
    columns: Incomplete
    group: Incomplete
    def __init__(self, parent, strategy_key) -> None: ...
    def create_row_processor(self, context, query_entity, path, loadopt, mapper, result, adapter, populators) -> None: ...
    is_class_level: bool
    def init_class_attribute(self, mapper) -> None: ...
    def setup_query(self, compile_state, query_entity, path, loadopt, adapter, column_collection, memoized_populators, only_load_props: Incomplete | None = None, **kw) -> None: ...

class LoadDeferredColumns:
    """serializable loader object used by DeferredColumnLoader"""
    key: Incomplete
    raiseload: Incomplete
    def __init__(self, key: str, raiseload: bool = False) -> None: ...
    def __call__(self, state, passive=...): ...

class AbstractRelationshipLoader(LoaderStrategy):
    """LoaderStratgies which deal with related objects."""
    mapper: Incomplete
    entity: Incomplete
    target: Incomplete
    uselist: Incomplete
    def __init__(self, parent, strategy_key) -> None: ...

class DoNothingLoader(LoaderStrategy):
    """Relationship loader that makes no change to the object's state.

    Compared to NoLoader, this loader does not initialize the
    collection/attribute to empty/none; the usual default LazyLoader will
    take effect.

    """

class NoLoader(AbstractRelationshipLoader):
    '''Provide loading behavior for a :class:`.Relationship`
    with "lazy=None".

    '''
    is_class_level: bool
    def init_class_attribute(self, mapper) -> None: ...
    def create_row_processor(self, context, query_entity, path, loadopt, mapper, result, adapter, populators) -> None: ...

class LazyLoader(AbstractRelationshipLoader, util.MemoizedSlots, log.Identified):
    '''Provide loading behavior for a :class:`.Relationship`
    with "lazy=True", that is loads when first accessed.

    '''
    parent_property: RelationshipProperty[Any]
    is_aliased_class: Incomplete
    use_get: Incomplete
    def __init__(self, parent: RelationshipProperty[Any], strategy_key: Tuple[Any, ...]) -> None: ...
    is_class_level: bool
    def init_class_attribute(self, mapper) -> None: ...
    def create_row_processor(self, context, query_entity, path, loadopt, mapper, result, adapter, populators): ...

class LoadLazyAttribute:
    """semi-serializable loader object used by LazyLoader

    Historically, this object would be carried along with instances that
    needed to run lazyloaders, so it had to be serializable to support
    cached instances.

    this is no longer a general requirement, and the case where this object
    is used is exactly the case where we can't really serialize easily,
    which is when extra criteria in the loader option is present.

    We can't reliably serialize that as it refers to mapped entities and
    AliasedClass objects that are local to the current process, which would
    need to be matched up on deserialize e.g. the sqlalchemy.ext.serializer
    approach.

    """
    key: Incomplete
    strategy_key: Incomplete
    loadopt: Incomplete
    extra_criteria: Incomplete
    def __init__(self, key, initiating_strategy, loadopt, extra_criteria) -> None: ...
    def __call__(self, state, passive=...): ...

class PostLoader(AbstractRelationshipLoader):
    """A relationship loader that emits a second SELECT statement."""

class ImmediateLoader(PostLoader):
    join_depth: Incomplete
    def __init__(self, parent, strategy_key) -> None: ...
    def init_class_attribute(self, mapper) -> None: ...
    def create_row_processor(self, context, query_entity, path, loadopt, mapper, result, adapter, populators) -> None: ...

class SubqueryLoader(PostLoader):
    join_depth: Incomplete
    def __init__(self, parent, strategy_key) -> None: ...
    def init_class_attribute(self, mapper) -> None: ...
    class _SubqCollections:
        '''Given a :class:`_query.Query` used to emit the "subquery load",
        provide a load interface that executes the query at the
        first moment a value is needed.

        '''
        session: Incomplete
        execution_options: Incomplete
        load_options: Incomplete
        params: Incomplete
        subq: Incomplete
        def __init__(self, context, subq) -> None: ...
        def get(self, key, default): ...
        def loader(self, state, dict_, row) -> None: ...
    def create_row_processor(self, context, query_entity, path, loadopt, mapper, result, adapter, populators): ...

class JoinedLoader(AbstractRelationshipLoader):
    """Provide loading behavior for a :class:`.Relationship`
    using joined eager loading.

    """
    join_depth: Incomplete
    def __init__(self, parent, strategy_key) -> None: ...
    def init_class_attribute(self, mapper) -> None: ...
    def setup_query(self, compile_state, query_entity, path, loadopt, adapter, column_collection: Incomplete | None = None, parentmapper: Incomplete | None = None, chained_from_outerjoin: bool = False, **kwargs) -> None:
        """Add a left outer join to the statement that's being constructed."""
    def create_row_processor(self, context, query_entity, path, loadopt, mapper, result, adapter, populators) -> None: ...

class SelectInLoader(PostLoader, util.MemoizedSlots):

    class query_info(NamedTuple):
        load_only_child: Incomplete
        load_with_join: Incomplete
        in_expr: Incomplete
        pk_cols: Incomplete
        zero_idx: Incomplete
        child_lookup_cols: Incomplete
    join_depth: Incomplete
    omit_join: Incomplete
    def __init__(self, parent, strategy_key) -> None: ...
    def init_class_attribute(self, mapper) -> None: ...
    def create_row_processor(self, context, query_entity, path, loadopt, mapper, result, adapter, populators): ...

def single_parent_validator(desc, prop): ...
