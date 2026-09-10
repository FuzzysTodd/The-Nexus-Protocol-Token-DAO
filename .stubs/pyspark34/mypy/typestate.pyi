from _typeshed import Incomplete
from mypy.nodes import TypeInfo as TypeInfo
from mypy.server.trigger import make_trigger as make_trigger
from mypy.types import Instance as Instance, Type as Type, TypeVarId as TypeVarId, get_proper_type as get_proper_type
from typing_extensions import Final, TypeAlias as _TypeAlias

MAX_NEGATIVE_CACHE_TYPES: Final[int]
MAX_NEGATIVE_CACHE_ENTRIES: Final[int]
SubtypeRelationship: _TypeAlias
SubtypeKind: _TypeAlias
SubtypeCache: _TypeAlias

class TypeState:
    """This class provides subtype caching to improve performance of subtype checks.
    It also holds protocol fine grained dependencies.

    Note: to avoid leaking global state, 'reset_all_subtype_caches()' should be called
    after a build has finished and after a daemon shutdown. This subtype cache only exists for
    performance reasons, resetting subtype caches for a class has no semantic effect.
    The protocol dependencies however are only stored here, and shouldn't be deleted unless
    not needed any more (e.g. during daemon shutdown).
    """
    proto_deps: dict[str, set[str]] | None
    inferring: Final[list[tuple[Type, Type]]]
    infer_unions: bool
    def __init__(self) -> None: ...
    def is_assumed_subtype(self, left: Type, right: Type) -> bool: ...
    def is_assumed_proper_subtype(self, left: Type, right: Type) -> bool: ...
    def get_assumptions(self, is_proper: bool) -> list[tuple[Type, Type]]: ...
    def reset_all_subtype_caches(self) -> None:
        """Completely reset all known subtype caches."""
    def reset_subtype_caches_for(self, info: TypeInfo) -> None:
        """Reset subtype caches (if any) for a given supertype TypeInfo."""
    def reset_all_subtype_caches_for(self, info: TypeInfo) -> None:
        """Reset subtype caches (if any) for a given supertype TypeInfo and its MRO."""
    def is_cached_subtype_check(self, kind: SubtypeKind, left: Instance, right: Instance) -> bool: ...
    def is_cached_negative_subtype_check(self, kind: SubtypeKind, left: Instance, right: Instance) -> bool: ...
    def record_subtype_cache_entry(self, kind: SubtypeKind, left: Instance, right: Instance) -> None: ...
    def record_negative_subtype_cache_entry(self, kind: SubtypeKind, left: Instance, right: Instance) -> None: ...
    def reset_protocol_deps(self) -> None:
        """Reset dependencies after a full run or before a daemon shutdown."""
    def record_protocol_subtype_check(self, left_type: TypeInfo, right_type: TypeInfo) -> None: ...
    def update_protocol_deps(self, second_map: dict[str, set[str]] | None = None) -> None:
        """Update global protocol dependency map.

        We update the global map incrementally, using a snapshot only from recently
        type checked types. If second_map is given, update it as well. This is currently used
        by FineGrainedBuildManager that maintains normal (non-protocol) dependencies.
        """
    def add_all_protocol_deps(self, deps: dict[str, set[str]]) -> None:
        """Add all known protocol dependencies to deps.

        This is used by tests and debug output, and also when collecting
        all collected or loaded dependencies as part of build.
        """

type_state: Final[Incomplete]

def reset_global_state() -> None:
    """Reset most existing global state.

    Currently most of it is in this module. Few exceptions are strict optional status and
    and functools.lru_cache.
    """
