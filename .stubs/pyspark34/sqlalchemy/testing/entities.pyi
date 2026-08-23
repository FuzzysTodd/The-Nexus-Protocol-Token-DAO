from ..orm.writeonly import WriteOnlyCollection as WriteOnlyCollection

class BasicEntity:
    def __init__(self, **kw) -> None: ...

class ComparableMixin:
    def __ne__(self, other): ...
    def __eq__(self, other):
        """'Deep, sparse compare.

        Deeply compare two entities, following the non-None attributes of the
        non-persisted object, if possible.

        """

class ComparableEntity(ComparableMixin, BasicEntity):
    def __hash__(self): ...
