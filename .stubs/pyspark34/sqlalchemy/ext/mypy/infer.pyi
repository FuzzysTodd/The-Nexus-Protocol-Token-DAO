from . import names as names, util as util
from mypy.nodes import AssignmentStmt as AssignmentStmt, Expression as Expression, RefExpr, TypeInfo, Var
from mypy.plugin import SemanticAnalyzerPluginInterface as SemanticAnalyzerPluginInterface
from mypy.types import ProperType as ProperType
from typing import Sequence

def infer_type_from_right_hand_nameexpr(api: SemanticAnalyzerPluginInterface, stmt: AssignmentStmt, node: Var, left_hand_explicit_type: ProperType | None, infer_from_right_side: RefExpr) -> ProperType | None: ...
def infer_type_from_left_hand_type_only(api: SemanticAnalyzerPluginInterface, node: Var, left_hand_explicit_type: ProperType | None) -> ProperType | None:
    """Determine the type based on explicit annotation only.

    if no annotation were present, note that we need one there to know
    the type.

    """
def extract_python_type_from_typeengine(api: SemanticAnalyzerPluginInterface, node: TypeInfo, type_args: Sequence[Expression]) -> ProperType: ...
