from _typeshed import Incomplete
from collections.abc import Set as Set
from referencing import Anchor as Anchor, Registry as Registry, Resource as Resource, Specification as Specification, exceptions as exceptions
from referencing._attrs import frozen as frozen
from referencing._core import Resolved as _Resolved, Resolver as _Resolver
from referencing.typing import Mapping as Mapping, URI as URI
from typing import Any

ObjectSchema = Mapping[str, Any]
Schema = bool | ObjectSchema
SchemaRegistry = Registry[Schema]

class UnknownDialect(Exception):
    '''
    A dialect identifier was found for a dialect unknown by this library.

    If it\'s a custom ("unofficial") dialect, be sure you\'ve registered it.
    '''
    uri: URI

DRAFT202012: Incomplete
DRAFT201909: Incomplete
DRAFT7: Incomplete
DRAFT6: Incomplete
DRAFT4: Incomplete
DRAFT3: Incomplete

def specification_with(dialect_id: URI, default: Specification[Any] = None) -> Specification[Any]:
    """
    Retrieve the `Specification` with the given dialect identifier.

    Raises:

        `UnknownDialect`

            if the given ``dialect_id`` isn't known
    """

class DynamicAnchor:
    """
    Dynamic anchors, introduced in draft 2020.
    """
    name: str
    resource: Resource[Schema]
    def resolve(self, resolver: _Resolver[Schema]) -> _Resolved[Schema]:
        """
        Resolve this anchor dynamically.
        """

def lookup_recursive_ref(resolver: _Resolver[Schema]) -> _Resolved[Schema]:
    """
    Recursive references (via recursive anchors), present only in draft 2019.

    As per the 2019 specification (§ 8.2.4.2.1), only the ``#`` recursive
    reference is supported (and is therefore assumed to be the relevant
    reference).
    """
