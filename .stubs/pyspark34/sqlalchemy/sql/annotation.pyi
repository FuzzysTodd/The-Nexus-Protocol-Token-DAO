from . import operators as operators
from .. import util as util
from ..util.typing import Literal as Literal, Self as Self
from .base import _EntityNamespace
from .cache_key import HasCacheKey as HasCacheKey
from .visitors import ExternallyTraversible as ExternallyTraversible, InternalTraversal as InternalTraversal, anon_map as anon_map
from _typeshed import Incomplete
from typing import Any, Dict, FrozenSet, Tuple, Type

EMPTY_ANNOTATIONS: util.immutabledict[str, Any]

class SupportsAnnotations(ExternallyTraversible):
    proxy_set: util.generic_fn_descriptor[FrozenSet[Any]]

class SupportsWrappingAnnotations(SupportsAnnotations):
    def entity_namespace(self) -> _EntityNamespace: ...

class SupportsCloneAnnotations(SupportsWrappingAnnotations): ...

class Annotated(SupportsAnnotations):
    '''clones a SupportsAnnotations and applies an \'annotations\' dictionary.

    Unlike regular clones, this clone also mimics __hash__() and
    __eq__() of the original element so that it takes its place
    in hashed collections.

    A reference to the original element is maintained, for the important
    reason of keeping its hash value current.  When GC\'ed, the
    hash value may be reused, causing conflicts.

    .. note::  The rationale for Annotated producing a brand new class,
       rather than placing the functionality directly within ClauseElement,
       is **performance**.  The __hash__() method is absent on plain
       ClauseElement which leads to significantly reduced function call
       overhead, as the use of sets and dictionaries against ClauseElement
       objects is prevalent, but most are not "annotated".

    '''
    def __new__(cls, *args: Any) -> Self: ...
    __dict__: Incomplete
    def __init__(self, element: SupportsWrappingAnnotations, values: _AnnotationDict) -> None: ...
    def __reduce__(self) -> Tuple[Type[Annotated], Tuple[Any, ...]]: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def entity_namespace(self) -> _EntityNamespace: ...

annotated_classes: Dict[Type[SupportsWrappingAnnotations], Type[Annotated]]
