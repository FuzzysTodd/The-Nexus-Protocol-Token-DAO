from . import coercions as coercions, dml as dml, elements as elements, roles as roles
from .. import exc as exc, util as util
from ..util.typing import Literal as Literal
from .compiler import SQLCompiler as SQLCompiler
from .dml import DMLState as DMLState, ValuesBase as ValuesBase
from .elements import ColumnClause as ColumnClause, ColumnElement as ColumnElement, KeyedColumnElement as KeyedColumnElement
from .schema import Column as Column, default_is_clause_element as default_is_clause_element, default_is_sequence as default_is_sequence
from .selectable import Select as Select, TableClause as TableClause
from _typeshed import Incomplete
from typing import Any, List, NamedTuple, Sequence

REQUIRED: Incomplete

class _CrudParams(NamedTuple):
    single_params: _CrudParamSequence
    all_multi_params: List[Sequence[_CrudParamElementStr]]
    is_default_metavalue_only: bool = ...
    use_insertmanyvalues: bool = ...
    use_sentinel_columns: Sequence[Column[Any]] | None = ...

class _multiparam_column(elements.ColumnElement[Any]):
    index: Incomplete
    key: Incomplete
    original: Incomplete
    default: Incomplete
    type: Incomplete
    def __init__(self, original, index) -> None: ...
    def compare(self, other, **kw) -> None: ...
    def __eq__(self, other): ...
