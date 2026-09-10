from collections.abc import Iterable, Iterator, Sequence
from referencing import exceptions as exceptions
from referencing._attrs import frozen as frozen
from referencing.typing import Anchor as AnchorType, D as D, Mapping as Mapping, Retrieve as Retrieve, URI as URI
from rpds import HashTrieSet, List
from typing import Any, Callable, ClassVar, Generic, Protocol, TypeVar

EMPTY_UNCRAWLED: HashTrieSet[URI]
EMPTY_PREVIOUS_RESOLVERS: List[URI]

class _MaybeInSubresource(Protocol[D]):
    def __call__(self, segments: Sequence[int | str], resolver: Resolver[D], subresource: Resource[D]) -> Resolver[D]: ...

class Specification(Generic[D]):
    """
    A specification which defines referencing behavior.

    The various methods of a `Specification` allow for varying referencing
    behavior across JSON Schema specification versions, etc.
    """
    name: str
    id_of: Callable[[D], URI | None]
    subresources_of: Callable[[D], Iterable[D]]
    maybe_in_subresource: _MaybeInSubresource[D]
    OPAQUE: ClassVar[Specification[Any]]
    def anchors_in(self, contents: D):
        """
        Retrieve the anchors contained in the given document.
        """
    def create_resource(self, contents: D) -> Resource[D]:
        """
        Create a resource which is interpreted using this specification.
        """

class Resource(Generic[D]):
    """
    A document (deserialized JSON) with a concrete interpretation under a spec.

    In other words, a Python object, along with an instance of `Specification`
    which describes how the document interacts with referencing -- both
    internally (how it refers to other `Resource`\\ s) and externally (how it
    should be identified such that it is referenceable by other documents).
    """
    contents: D
    @classmethod
    def from_contents(cls, contents: D, default_specification: Specification[D] = None) -> Resource[D]:
        """
        Attempt to discern which specification applies to the given contents.

        Raises:

            `CannotDetermineSpecification`

                if the given contents don't have any discernible
                information which could be used to guess which
                specification they identify as
        """
    @classmethod
    def opaque(cls, contents: D) -> Resource[D]:
        """
        Create an opaque `Resource` -- i.e. one with opaque specification.

        See `Specification.OPAQUE` for details.
        """
    def id(self) -> URI | None:
        """
        Retrieve this resource's (specification-specific) identifier.
        """
    def subresources(self) -> Iterable[Resource[D]]:
        """
        Retrieve this resource's subresources.
        """
    def anchors(self) -> Iterable[AnchorType[D]]:
        """
        Retrieve this resource's (specification-specific) identifier.
        """
    def pointer(self, pointer: str, resolver: Resolver[D]) -> Resolved[D]:
        """
        Resolve the given JSON pointer.

        Raises:

            `exceptions.PointerToNowhere`

                if the pointer points to a location not present in the document
        """

class Registry(Mapping[URI, Resource[D]]):
    """
    A registry of `Resource`\\ s, each identified by their canonical URIs.

    Registries store a collection of in-memory resources, and optionally
    enable additional resources which may be stored elsewhere (e.g. in a
    database, a separate set of files, over the network, etc.).

    They also lazily walk their known resources, looking for subresources
    within them. In other words, subresources contained within any added
    resources will be retrievable via their own IDs (though this discovery of
    subresources will be delayed until necessary).

    Registries are immutable, and their methods return new instances of the
    registry with the additional resources added to them.

    The ``retrieve`` argument can be used to configure retrieval of resources
    dynamically, either over the network, from a database, or the like.
    Pass it a callable which will be called if any URI not present in the
    registry is accessed. It must either return a `Resource` or else raise a
    `NoSuchResource` exception indicating that the resource does not exist
    even according to the retrieval logic.
    """
    def __getitem__(self, uri: URI) -> Resource[D]:
        """
        Return the (already crawled) `Resource` identified by the given URI.
        """
    def __iter__(self) -> Iterator[URI]:
        """
        Iterate over all crawled URIs in the registry.
        """
    def __len__(self) -> int:
        """
        Count the total number of fully crawled resources in this registry.
        """
    def __rmatmul__(self, new: Resource[D] | Iterable[Resource[D]]) -> Registry[D]:
        """
        Create a new registry with resource(s) added using their internal IDs.

        Resources must have a internal IDs (e.g. the :kw:`$id` keyword in
        modern JSON Schema versions), otherwise an error will be raised.

        Both a single resource as well as an iterable of resources works, i.e.:

            * ``resource @ registry`` or

            * ``[iterable, of, multiple, resources] @ registry``

        which -- again, assuming the resources have internal IDs -- is
        equivalent to calling `Registry.with_resources` as such:

        .. code:: python

            registry.with_resources(
                (resource.id(), resource) for resource in new_resources
            )

        Raises:

            `NoInternalID`

                if the resource(s) in fact do not have IDs
        """
    def get_or_retrieve(self, uri: URI) -> Retrieved[D, Resource[D]]:
        """
        Get a resource from the registry, crawling or retrieving if necessary.

        May involve crawling to find the given URI if it is not already known,
        so the returned object is a `Retrieved` object which contains both the
        resource value as well as the registry which ultimately contained it.
        """
    def remove(self, uri: URI):
        """
        Return a registry with the resource identified by a given URI removed.
        """
    def anchor(self, uri: URI, name: str):
        """
        Retrieve a given anchor from a resource which must already be crawled.
        """
    def contents(self, uri: URI) -> D:
        """
        Retrieve the (already crawled) contents identified by the given URI.
        """
    def crawl(self) -> Registry[D]:
        """
        Crawl all added resources, discovering subresources.
        """
    def with_resource(self, uri: URI, resource: Resource[D]):
        """
        Add the given `Resource` to the registry, without crawling it.
        """
    def with_resources(self, pairs: Iterable[tuple[URI, Resource[D]]]) -> Registry[D]:
        """
        Add the given `Resource`\\ s to the registry, without crawling them.
        """
    def with_contents(self, pairs: Iterable[tuple[URI, D]], **kwargs: Any) -> Registry[D]:
        """
        Add the given contents to the registry, autodetecting when necessary.
        """
    def combine(self, *registries: Registry[D]) -> Registry[D]:
        """
        Combine together one or more other registries, producing a unified one.
        """
    def resolver(self, base_uri: URI = '') -> Resolver[D]:
        """
        Return a `Resolver` which resolves references against this registry.
        """
    def resolver_with_root(self, resource: Resource[D]) -> Resolver[D]:
        """
        Return a `Resolver` with a specific root resource.
        """
AnchorOrResource = TypeVar('AnchorOrResource', AnchorType[Any], Resource[Any])

class Retrieved(Generic[D, AnchorOrResource]):
    """
    A value retrieved from a `Registry`.
    """
    value: AnchorOrResource
    registry: Registry[D]

class Resolved(Generic[D]):
    """
    A reference resolved to its contents by a `Resolver`.
    """
    contents: D
    resolver: Resolver[D]

class Resolver(Generic[D]):
    """
    A reference resolver.

    Resolvers help resolve references (including relative ones) by
    pairing a fixed base URI with a `Registry`.

    This object, under normal circumstances, is expected to be used by
    *implementers of libraries* built on top of `referencing` (e.g. JSON Schema
    implementations or other libraries resolving JSON references),
    not directly by end-users populating registries or while writing
    schemas or other resources.

    References are resolved against the base URI, and the combined URI
    is then looked up within the registry.

    The process of resolving a reference may itself involve calculating
    a *new* base URI for future reference resolution (e.g. if an
    intermediate resource sets a new base URI), or may involve encountering
    additional subresources and adding them to a new registry.
    """
    def lookup(self, ref: URI) -> Resolved[D]:
        """
        Resolve the given reference to the resource it points to.

        Raises:

            `exceptions.Unresolvable`

                or a subclass thereof (see below) if the reference isn't
                resolvable

            `exceptions.NoSuchAnchor`

                if the reference is to a URI where a resource exists but
                contains a plain name fragment which does not exist within
                the resource

            `exceptions.PointerToNowhere`

                if the reference is to a URI where a resource exists but
                contains a JSON pointer to a location within the resource
                that does not exist
        """
    def in_subresource(self, subresource: Resource[D]) -> Resolver[D]:
        """
        Create a resolver for a subresource (which may have a new base URI).
        """
    def dynamic_scope(self) -> Iterable[tuple[URI, Registry[D]]]:
        """
        In specs with such a notion, return the URIs in the dynamic scope.
        """

class Anchor(Generic[D]):
    """
    A simple anchor in a `Resource`.
    """
    name: str
    resource: Resource[D]
    def resolve(self, resolver: Resolver[D]):
        """
        Return the resource for this anchor.
        """
