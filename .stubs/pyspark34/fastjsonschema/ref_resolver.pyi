from .exceptions import JsonSchemaDefinitionException as JsonSchemaDefinitionException
from _typeshed import Incomplete

def get_id(schema):
    """
    Originally ID was `id` and since v7 it's `$id`.
    """
def resolve_path(schema, fragment):
    """
    Return definition from path.

    Path is unescaped according https://tools.ietf.org/html/rfc6901
    """
def normalize(uri): ...
def resolve_remote(uri, handlers):
    """
    Resolve a remote ``uri``.

    .. note::

        urllib library is used to fetch requests from the remote ``uri``
        if handlers does notdefine otherwise.
    """

class RefResolver:
    """
    Resolve JSON References.
    """
    base_uri: Incomplete
    resolution_scope: Incomplete
    schema: Incomplete
    store: Incomplete
    cache: Incomplete
    handlers: Incomplete
    def __init__(self, base_uri, schema, store={}, cache: bool = True, handlers={}) -> None:
        """
        `base_uri` is URI of the referring document from the `schema`.
        `store` is an dictionary that will be used to cache the fetched schemas
        (if `cache=True`).

        Please notice that you can have caching problems when compiling schemas
        with colliding `$ref`. To force overwriting use `cache=False` or
        explicitly pass the `store` argument (with a brand new dictionary)
        """
    @classmethod
    def from_schema(cls, schema, handlers={}, **kwargs):
        """
        Construct a resolver from a JSON schema object.
        """
    def in_scope(self, scope: str):
        """
        Context manager to handle current scope.
        """
    def resolving(self, ref: str):
        """
        Context manager which resolves a JSON ``ref`` and enters the
        resolution scope of this ref.
        """
    def get_uri(self): ...
    def get_scope_name(self):
        """
        Get current scope and return it as a valid function name.
        """
    def walk(self, node: dict):
        """
        Walk thru schema and dereferencing ``id`` and ``$ref`` instances
        """
