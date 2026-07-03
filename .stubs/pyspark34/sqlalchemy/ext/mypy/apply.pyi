from . import infer as infer, util as util
from .names import NAMED_TYPE_SQLA_MAPPED as NAMED_TYPE_SQLA_MAPPED, expr_to_mapped_constructor as expr_to_mapped_constructor
from mypy.nodes import AssignmentStmt, ClassDef as ClassDef, NameExpr, StrExpr
from mypy.plugin import SemanticAnalyzerPluginInterface as SemanticAnalyzerPluginInterface
from mypy.types import ProperType as ProperType
from typing import List

def apply_mypy_mapped_attr(cls, api: SemanticAnalyzerPluginInterface, item: NameExpr | StrExpr, attributes: List[util.SQLAlchemyAttribute]) -> None: ...
def re_apply_declarative_assignments(cls, api: SemanticAnalyzerPluginInterface, attributes: List[util.SQLAlchemyAttribute]) -> None:
    """For multiple class passes, re-apply our left-hand side types as mypy
    seems to reset them in place.

    """
def apply_type_to_mapped_statement(api: SemanticAnalyzerPluginInterface, stmt: AssignmentStmt, lvalue: NameExpr, left_hand_explicit_type: ProperType | None, python_type_for_type: ProperType | None) -> None:
    """Apply the Mapped[<type>] annotation and right hand object to a
    declarative assignment statement.

    This converts a Python declarative class statement such as::

        class User(Base):
            # ...

            attrname = Column(Integer)

    To one that describes the final Python behavior to Mypy::

        class User(Base):
            # ...

            attrname : Mapped[Optional[int]] = <meaningless temp node>

    """
def add_additional_orm_attributes(cls, api: SemanticAnalyzerPluginInterface, attributes: List[util.SQLAlchemyAttribute]) -> None:
    """Apply __init__, __table__ and other attributes to the mapped class."""
