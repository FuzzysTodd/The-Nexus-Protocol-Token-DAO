from . import attributes as attributes, context as context, evaluator as evaluator, loading as loading, persistence as persistence
from .. import util as util
from ..engine import Connection as Connection, Dialect as Dialect, cursor as cursor, result as _result
from ..engine.interfaces import _CoreAnyExecuteParams
from ..sql import coercions as coercions, dml as dml, expression as expression, roles as roles, select as select, sqltypes as sqltypes
from ..sql.base import CompileState as CompileState, Options as Options
from ..sql.dml import DeleteDMLState as DeleteDMLState, InsertDMLState as InsertDMLState, UpdateDMLState as UpdateDMLState
from ..util import EMPTY_DICT as EMPTY_DICT
from ..util.typing import Literal as Literal
from ._typing import DMLStrategyArgument as DMLStrategyArgument, OrmExecuteOptionsParameter as OrmExecuteOptionsParameter, SynchronizeSessionArgument as SynchronizeSessionArgument
from .base import NO_VALUE as NO_VALUE
from .context import AbstractORMCompileState as AbstractORMCompileState, FromStatement as FromStatement, ORMFromStatementCompileState as ORMFromStatementCompileState, QueryContext as QueryContext
from .mapper import Mapper as Mapper
from .session import ORMExecuteState as ORMExecuteState, Session as Session, SessionTransaction as SessionTransaction, _BindArguments
from .state import InstanceState as InstanceState
from _typeshed import Incomplete
from typing import Any

class ORMDMLState(AbstractORMCompileState):
    is_dml_returning: bool
    from_statement_ctx: ORMFromStatementCompileState | None
    @classmethod
    def get_entity_description(cls, statement): ...
    @classmethod
    def get_returning_column_descriptions(cls, statement): ...

class BulkUDCompileState(ORMDMLState):
    class default_update_options(Options): ...
    @classmethod
    def can_use_returning(cls, dialect: Dialect, mapper: Mapper[Any], *, is_multitable: bool = False, is_update_from: bool = False, is_delete_using: bool = False, is_executemany: bool = False) -> bool: ...
    @classmethod
    def orm_pre_session_exec(cls, session, statement, params, execution_options, bind_arguments, is_pre_event): ...
    @classmethod
    def orm_setup_cursor_result(cls, session, statement, params, execution_options, bind_arguments, result): ...

class BulkORMInsert(ORMDMLState, InsertDMLState):
    class default_insert_options(Options): ...
    select_statement: FromStatement | None
    @classmethod
    def orm_pre_session_exec(cls, session, statement, params, execution_options, bind_arguments, is_pre_event): ...
    @classmethod
    def orm_execute_statement(cls, session: Session, statement: dml.Insert, params: _CoreAnyExecuteParams, execution_options: OrmExecuteOptionsParameter, bind_arguments: _BindArguments, conn: Connection) -> _result.Result: ...
    @classmethod
    def create_for_statement(cls, statement, compiler, **kw) -> BulkORMInsert: ...

class BulkORMUpdate(BulkUDCompileState, UpdateDMLState):
    @classmethod
    def create_for_statement(cls, statement, compiler, **kw): ...
    @classmethod
    def orm_execute_statement(cls, session: Session, statement: dml.Update, params: _CoreAnyExecuteParams, execution_options: OrmExecuteOptionsParameter, bind_arguments: _BindArguments, conn: Connection) -> _result.Result: ...
    @classmethod
    def can_use_returning(cls, dialect: Dialect, mapper: Mapper[Any], *, is_multitable: bool = False, is_update_from: bool = False, is_delete_using: bool = False, is_executemany: bool = False) -> bool: ...

class BulkORMDelete(BulkUDCompileState, DeleteDMLState):
    mapper: Incomplete
    statement: Incomplete
    @classmethod
    def create_for_statement(cls, statement, compiler, **kw): ...
    @classmethod
    def orm_execute_statement(cls, session: Session, statement: dml.Delete, params: _CoreAnyExecuteParams, execution_options: OrmExecuteOptionsParameter, bind_arguments: _BindArguments, conn: Connection) -> _result.Result: ...
    @classmethod
    def can_use_returning(cls, dialect: Dialect, mapper: Mapper[Any], *, is_multitable: bool = False, is_update_from: bool = False, is_delete_using: bool = False, is_executemany: bool = False) -> bool: ...
