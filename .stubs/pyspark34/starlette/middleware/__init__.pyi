import typing
from _typeshed import Incomplete

class Middleware:
    cls: Incomplete
    options: Incomplete
    def __init__(self, cls: type, **options: typing.Any) -> None: ...
    def __iter__(self) -> typing.Iterator: ...
