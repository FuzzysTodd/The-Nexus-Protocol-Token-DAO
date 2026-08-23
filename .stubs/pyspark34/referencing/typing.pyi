from referencing._core import Resolved as Resolved, Resolver as Resolver, Resource as Resource
from typing import Protocol, TypeVar

URI = str
D = TypeVar('D')

class Retrieve(Protocol[D]):
    """
    A retrieval callable, usable within a `Registry` for resource retrieval.

    Does not make assumptions about where the resource might be coming from.
    """
    def __call__(self, uri: URI) -> Resource[D]:
        """
        Retrieve the resource with the given URI.

        Raise `referencing.exceptions.NoSuchResource` if you wish to indicate
        the retriever cannot lookup the given URI.
        """

class Anchor(Protocol[D]):
    '''
    An anchor within a `Resource`.

    Beyond "simple" anchors, some specifications like JSON Schema\'s 2020
    version have dynamic anchors.
    '''
    @property
    def name(self) -> str:
        """
        Return the name of this anchor.
        """
    def resolve(self, resolver: Resolver[D]) -> Resolved[D]:
        """
        Return the resource for this anchor.
        """
