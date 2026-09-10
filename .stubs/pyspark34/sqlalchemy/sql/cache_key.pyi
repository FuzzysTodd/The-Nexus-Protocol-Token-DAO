import enum
from .. import util as util
from ..engine.interfaces import _CoreSingleExecuteParams
from ..inspection import inspect as inspect
from ..util import HasMemoized as HasMemoized
from ..util.typing import Literal as Literal, Protocol as Protocol
from .elements import BindParameter as BindParameter, ClauseElement as ClauseElement
from .visitors import HasTraversalDispatch as HasTraversalDispatch, HasTraverseInternals as HasTraverseInternals, InternalTraversal as InternalTraversal, anon_map as anon_map, prefix_anon_map as prefix_anon_map
from _typeshed import Incomplete
from typing import Any, List, MutableMapping, NamedTuple, Sequence, Tuple

class _CacheKeyTraversalDispatchType(Protocol):
    def __call__(s, self: HasCacheKey, visitor: _CacheKeyTraversal) -> CacheKey: ...

class CacheConst(enum.Enum):
    NO_CACHE: int

NO_CACHE: Incomplete

class CacheTraverseTarget(enum.Enum):
    CACHE_IN_PLACE: int
    CALL_GEN_CACHE_KEY: int
    STATIC_CACHE_KEY: int
    PROPAGATE_ATTRS: int
    ANON_NAME: int

CACHE_IN_PLACE: Incomplete
CALL_GEN_CACHE_KEY: Incomplete
STATIC_CACHE_KEY: Incomplete
PROPAGATE_ATTRS: Incomplete
ANON_NAME: Incomplete

class HasCacheKey:
    """Mixin for objects which can produce a cache key.

    This class is usually in a hierarchy that starts with the
    :class:`.HasTraverseInternals` base, but this is optional.  Currently,
    the class should be able to work on its own without including
    :class:`.HasTraverseInternals`.

    .. seealso::

        :class:`.CacheKey`

        :ref:`sql_caching`

    """
    inherit_cache: bool | None

class HasCacheKeyTraverse(HasTraverseInternals, HasCacheKey): ...
class MemoizedHasCacheKey(HasCacheKey, HasMemoized): ...
class SlotsMemoizedHasCacheKey(HasCacheKey, util.MemoizedSlots): ...

class CacheKey(NamedTuple):
    """The key used to identify a SQL statement construct in the
    SQL compilation cache.

    .. seealso::

        :ref:`sql_caching`

    """
    key: Tuple[Any, ...]
    bindparams: Sequence[BindParameter[Any]]
    def __hash__(self) -> int | None:
        """CacheKey itself is not hashable - hash the .key portion"""
    def to_offline_string(self, statement_cache: MutableMapping[Any, str], statement: ClauseElement, parameters: _CoreSingleExecuteParams) -> str:
        '''Generate an "offline string" form of this :class:`.CacheKey`

        The "offline string" is basically the string SQL for the
        statement plus a repr of the bound parameter values in series.
        Whereas the :class:`.CacheKey` object is dependent on in-memory
        identities in order to work as a cache key, the "offline" version
        is suitable for a cache that will work for other processes as well.

        The given ``statement_cache`` is a dictionary-like object where the
        string form of the statement itself will be cached.  This dictionary
        should be in a longer lived scope in order to reduce the time spent
        stringifying statements.


        '''
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...

class _CacheKeyTraversal(HasTraversalDispatch):
    visit_has_cache_key = CALL_GEN_CACHE_KEY
    visit_clauseelement = CALL_GEN_CACHE_KEY
    visit_clauseelement_list: Incomplete
    visit_annotations_key: Incomplete
    visit_clauseelement_tuple: Incomplete
    visit_memoized_select_entities: Incomplete
    visit_string = CACHE_IN_PLACE
    visit_boolean = CACHE_IN_PLACE
    visit_operator = CACHE_IN_PLACE
    visit_plain_obj = CACHE_IN_PLACE
    visit_statement_hint_list = CACHE_IN_PLACE
    visit_type = STATIC_CACHE_KEY
    visit_anon_name = ANON_NAME
    visit_propagate_attrs = PROPAGATE_ATTRS
    def visit_with_context_options(self, attrname: str, obj: Any, parent: Any, anon_map: anon_map, bindparams: List[BindParameter[Any]]) -> Tuple[Any, ...]: ...
    def visit_inspectable(self, attrname: str, obj: Any, parent: Any, anon_map: anon_map, bindparams: List[BindParameter[Any]]) -> Tuple[Any, ...]: ...
    def visit_string_list(self, attrname: str, obj: Any, parent: Any, anon_map: anon_map, bindparams: List[BindParameter[Any]]) -> Tuple[Any, ...]: ...
    def visit_multi(self, attrname: str, obj: Any, parent: Any, anon_map: anon_map, bindparams: List[BindParameter[Any]]) -> Tuple[Any, ...]: ...
    def visit_multi_list(self, attrname: str, obj: Any, parent: Any, anon_map: anon_map, bindparams: List[BindParameter[Any]]) -> Tuple[Any, ...]: ...
    def visit_has_cache_key_tuples(self, attrname: str, obj: Any, parent: Any, anon_map: anon_map, bindparams: List[BindParameter[Any]]) -> Tuple[Any, ...]: ...
    def visit_has_cache_key_list(self, attrname: str, obj: Any, parent: Any, anon_map: anon_map, bindparams: List[BindParameter[Any]]) -> Tuple[Any, ...]: ...
    def visit_executable_options(self, attrname: str, obj: Any, parent: Any, anon_map: anon_map, bindparams: List[BindParameter[Any]]) -> Tuple[Any, ...]: ...
    def visit_inspectable_list(self, attrname: str, obj: Any, parent: Any, anon_map: anon_map, bindparams: List[BindParameter[Any]]) -> Tuple[Any, ...]: ...
    def visit_clauseelement_tuples(self, attrname: str, obj: Any, parent: Any, anon_map: anon_map, bindparams: List[BindParameter[Any]]) -> Tuple[Any, ...]: ...
    def visit_fromclause_ordered_set(self, attrname: str, obj: Any, parent: Any, anon_map: anon_map, bindparams: List[BindParameter[Any]]) -> Tuple[Any, ...]: ...
    def visit_clauseelement_unordered_set(self, attrname: str, obj: Any, parent: Any, anon_map: anon_map, bindparams: List[BindParameter[Any]]) -> Tuple[Any, ...]: ...
    def visit_named_ddl_element(self, attrname: str, obj: Any, parent: Any, anon_map: anon_map, bindparams: List[BindParameter[Any]]) -> Tuple[Any, ...]: ...
    def visit_prefix_sequence(self, attrname: str, obj: Any, parent: Any, anon_map: anon_map, bindparams: List[BindParameter[Any]]) -> Tuple[Any, ...]: ...
    def visit_setup_join_tuple(self, attrname: str, obj: Any, parent: Any, anon_map: anon_map, bindparams: List[BindParameter[Any]]) -> Tuple[Any, ...]: ...
    def visit_table_hint_list(self, attrname: str, obj: Any, parent: Any, anon_map: anon_map, bindparams: List[BindParameter[Any]]) -> Tuple[Any, ...]: ...
    def visit_plain_dict(self, attrname: str, obj: Any, parent: Any, anon_map: anon_map, bindparams: List[BindParameter[Any]]) -> Tuple[Any, ...]: ...
    def visit_dialect_options(self, attrname: str, obj: Any, parent: Any, anon_map: anon_map, bindparams: List[BindParameter[Any]]) -> Tuple[Any, ...]: ...
    def visit_string_clauseelement_dict(self, attrname: str, obj: Any, parent: Any, anon_map: anon_map, bindparams: List[BindParameter[Any]]) -> Tuple[Any, ...]: ...
    def visit_string_multi_dict(self, attrname: str, obj: Any, parent: Any, anon_map: anon_map, bindparams: List[BindParameter[Any]]) -> Tuple[Any, ...]: ...
    def visit_fromclause_canonical_column_collection(self, attrname: str, obj: Any, parent: Any, anon_map: anon_map, bindparams: List[BindParameter[Any]]) -> Tuple[Any, ...]: ...
    def visit_unknown_structure(self, attrname: str, obj: Any, parent: Any, anon_map: anon_map, bindparams: List[BindParameter[Any]]) -> Tuple[Any, ...]: ...
    def visit_dml_ordered_values(self, attrname: str, obj: Any, parent: Any, anon_map: anon_map, bindparams: List[BindParameter[Any]]) -> Tuple[Any, ...]: ...
    def visit_dml_values(self, attrname: str, obj: Any, parent: Any, anon_map: anon_map, bindparams: List[BindParameter[Any]]) -> Tuple[Any, ...]: ...
    def visit_dml_multi_values(self, attrname: str, obj: Any, parent: Any, anon_map: anon_map, bindparams: List[BindParameter[Any]]) -> Tuple[Any, ...]: ...
