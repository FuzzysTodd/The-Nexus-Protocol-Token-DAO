from ..public import PythonMongoishQueryGenerator as PythonMongoishQueryGenerator, QueryGenerator as QueryGenerator, Runs as Runs
from .util import Attr as Attr, Base as Base, coalesce as coalesce, generate_name as generate_name, nested_get as nested_get, nested_set as nested_set
from _typeshed import Incomplete
from typing import Any, Dict, TypeVar

T = TypeVar('T')

class Runset(Base):
    entity: str | None
    project: str | None
    name: str
    query: str
    filters: dict
    groupby: list
    order: list
    query_generator: Incomplete
    pm_query_generator: Incomplete
    def __init__(self, entity: Incomplete | None = None, project: Incomplete | None = None, name: str = 'Run set', query: str = '', filters: Incomplete | None = None, groupby: Incomplete | None = None, order: Incomplete | None = None, *args, **kwargs) -> None: ...
    @classmethod
    def from_json(cls, spec: Dict[str, Any]) -> T:
        """This has a custom implementation because sometimes runsets are missing the project field."""
    def set_filters_with_python_expr(self, expr): ...
    @property
    def runs(self) -> Runs: ...
