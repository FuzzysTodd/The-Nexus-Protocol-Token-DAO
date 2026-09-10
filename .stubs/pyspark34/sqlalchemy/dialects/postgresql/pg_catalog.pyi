from ... import Column as Column, MetaData as MetaData, Table as Table, func as func
from ...types import BigInteger as BigInteger, Boolean as Boolean, CHAR as CHAR, Float as Float, Integer as Integer, SmallInteger as SmallInteger, String as String, Text as Text, TypeDecorator as TypeDecorator
from .array import ARRAY as ARRAY
from .types import OID as OID, REGCLASS as REGCLASS
from _typeshed import Incomplete

class NAME(TypeDecorator):
    impl: Incomplete
    cache_ok: bool

class PG_NODE_TREE(TypeDecorator):
    impl: Incomplete
    cache_ok: bool

class INT2VECTOR(TypeDecorator):
    impl: Incomplete
    cache_ok: bool

class OIDVECTOR(TypeDecorator):
    impl: Incomplete
    cache_ok: bool

class _SpaceVector:
    def result_processor(self, dialect, coltype): ...
REGPROC = REGCLASS
quote_ident: Incomplete
pg_table_is_visible: Incomplete
pg_type_is_visible: Incomplete
pg_get_viewdef: Incomplete
pg_get_serial_sequence: Incomplete
format_type: Incomplete
pg_get_expr: Incomplete
pg_get_constraintdef: Incomplete
pg_get_indexdef: Incomplete
RELKINDS_TABLE_NO_FOREIGN: Incomplete
RELKINDS_TABLE: Incomplete
RELKINDS_VIEW: Incomplete
RELKINDS_MAT_VIEW: Incomplete
RELKINDS_ALL_TABLE_LIKE: Incomplete
pg_catalog_meta: Incomplete
pg_namespace: Incomplete
pg_class: Incomplete
pg_type: Incomplete
pg_index: Incomplete
pg_attribute: Incomplete
pg_constraint: Incomplete
pg_sequence: Incomplete
pg_attrdef: Incomplete
pg_description: Incomplete
pg_enum: Incomplete
pg_am: Incomplete
