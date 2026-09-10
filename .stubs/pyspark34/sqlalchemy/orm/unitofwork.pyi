from . import attributes as attributes
from .. import event as event, util as util
from ..util import topological as topological
from .dependency import DependencyProcessor as DependencyProcessor
from .interfaces import MapperProperty as MapperProperty
from .mapper import Mapper as Mapper
from .session import Session as Session, SessionTransaction as SessionTransaction
from .state import InstanceState as InstanceState
from _typeshed import Incomplete
from collections.abc import Generator
from typing import Any, Dict, Set

def track_cascade_events(descriptor, prop):
    """Establish event listeners on object attributes which handle
    cascade-on-set/append.

    """

class UOWTransaction:
    session: Session
    transaction: SessionTransaction
    attributes: Dict[str, Any]
    deps: util.defaultdict[Mapper[Any], Set[DependencyProcessor]]
    mappers: util.defaultdict[Mapper[Any], Set[InstanceState[Any]]]
    presort_actions: Incomplete
    postsort_actions: Incomplete
    dependencies: Incomplete
    states: Incomplete
    post_update_states: Incomplete
    def __init__(self, session: Session) -> None: ...
    @property
    def has_work(self): ...
    def was_already_deleted(self, state):
        """Return ``True`` if the given state is expired and was deleted
        previously.
        """
    def is_deleted(self, state):
        """Return ``True`` if the given state is marked as deleted
        within this uowtransaction."""
    def memo(self, key, callable_): ...
    def remove_state_actions(self, state) -> None:
        """Remove pending actions for a state from the uowtransaction."""
    def get_attribute_history(self, state, key, passive=...):
        """Facade to attributes.get_state_history(), including
        caching of results."""
    def has_dep(self, processor): ...
    def register_preprocessor(self, processor, fromparent) -> None: ...
    def register_object(self, state: InstanceState[Any], isdelete: bool = False, listonly: bool = False, cancel_delete: bool = False, operation: str | None = None, prop: MapperProperty | None = None) -> bool: ...
    def register_post_update(self, state, post_update_cols) -> None: ...
    def filter_states_for_dep(self, dep, states):
        """Filter the given list of InstanceStates to those relevant to the
        given DependencyProcessor.

        """
    def states_for_mapper_hierarchy(self, mapper, isdelete, listonly) -> Generator[Incomplete, None, None]: ...
    def execute(self) -> None: ...
    def finalize_flush_changes(self) -> None:
        """Mark processed objects as clean / deleted after a successful
        flush().

        This method is called within the flush() method after the
        execute() method has succeeded and the transaction has been committed.

        """

class IterateMappersMixin: ...

class Preprocess(IterateMappersMixin):
    dependency_processor: Incomplete
    fromparent: Incomplete
    processed: Incomplete
    setup_flush_actions: bool
    def __init__(self, dependency_processor, fromparent) -> None: ...
    def execute(self, uow): ...

class PostSortRec:
    def __new__(cls, uow, *args): ...
    def execute_aggregate(self, uow, recs) -> None: ...

class ProcessAll(IterateMappersMixin, PostSortRec):
    dependency_processor: Incomplete
    sort_key: Incomplete
    isdelete: Incomplete
    fromparent: Incomplete
    def __init__(self, uow, dependency_processor, isdelete, fromparent) -> None: ...
    def execute(self, uow) -> None: ...
    def per_state_flush_actions(self, uow): ...

class PostUpdateAll(PostSortRec):
    mapper: Incomplete
    isdelete: Incomplete
    sort_key: Incomplete
    def __init__(self, uow, mapper, isdelete) -> None: ...
    def execute(self, uow) -> None: ...

class SaveUpdateAll(PostSortRec):
    mapper: Incomplete
    sort_key: Incomplete
    def __init__(self, uow, mapper) -> None: ...
    def execute(self, uow) -> None: ...
    def per_state_flush_actions(self, uow) -> Generator[Incomplete, None, None]: ...

class DeleteAll(PostSortRec):
    mapper: Incomplete
    sort_key: Incomplete
    def __init__(self, uow, mapper) -> None: ...
    def execute(self, uow) -> None: ...
    def per_state_flush_actions(self, uow) -> Generator[Incomplete, None, None]: ...

class ProcessState(PostSortRec):
    dependency_processor: Incomplete
    sort_key: Incomplete
    isdelete: Incomplete
    state: Incomplete
    def __init__(self, uow, dependency_processor, isdelete, state) -> None: ...
    def execute_aggregate(self, uow, recs) -> None: ...

class SaveUpdateState(PostSortRec):
    state: Incomplete
    mapper: Incomplete
    sort_key: Incomplete
    def __init__(self, uow, state) -> None: ...
    def execute_aggregate(self, uow, recs) -> None: ...

class DeleteState(PostSortRec):
    state: Incomplete
    mapper: Incomplete
    sort_key: Incomplete
    def __init__(self, uow, state) -> None: ...
    def execute_aggregate(self, uow, recs) -> None: ...
