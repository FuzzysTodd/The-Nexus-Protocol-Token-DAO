from . import events as events
from .. import event as event, exc as exc
from .schema import CheckConstraint as CheckConstraint, Column as Column, Constraint as Constraint, ForeignKeyConstraint as ForeignKeyConstraint, Index as Index, PrimaryKeyConstraint as PrimaryKeyConstraint, Table as Table, UniqueConstraint as UniqueConstraint
from _typeshed import Incomplete

class ConventionDict:
    const: Incomplete
    table: Incomplete
    convention: Incomplete
    def __init__(self, const, table, convention) -> None: ...
    def __getitem__(self, key): ...
