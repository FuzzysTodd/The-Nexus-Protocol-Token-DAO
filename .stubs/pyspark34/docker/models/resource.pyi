from _typeshed import Incomplete

class Model:
    """
    A base class for representing a single object on the server.
    """
    id_attribute: str
    client: Incomplete
    collection: Incomplete
    attrs: Incomplete
    def __init__(self, attrs: Incomplete | None = None, client: Incomplete | None = None, collection: Incomplete | None = None) -> None: ...
    def __eq__(self, other): ...
    def __hash__(self): ...
    @property
    def id(self):
        """
        The ID of the object.
        """
    @property
    def short_id(self):
        """
        The ID of the object, truncated to 12 characters.
        """
    def reload(self) -> None:
        """
        Load this object from the server again and update ``attrs`` with the
        new data.
        """

class Collection:
    """
    A base class for representing all objects of a particular type on the
    server.
    """
    model: Incomplete
    client: Incomplete
    def __init__(self, client: Incomplete | None = None) -> None: ...
    def __call__(self, *args, **kwargs) -> None: ...
    def list(self) -> None: ...
    def get(self, key) -> None: ...
    def create(self, attrs: Incomplete | None = None) -> None: ...
    def prepare_model(self, attrs):
        """
        Create a model from a set of attributes.
        """
