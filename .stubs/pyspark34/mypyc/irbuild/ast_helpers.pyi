from mypy.nodes import Expression as Expression
from mypyc.ir.ops import BasicBlock as BasicBlock
from mypyc.ir.rtypes import is_fixed_width_rtype as is_fixed_width_rtype, is_tagged as is_tagged
from mypyc.irbuild.builder import IRBuilder as IRBuilder
from mypyc.irbuild.constant_fold import constant_fold_expr as constant_fold_expr

def process_conditional(self, e: Expression, true: BasicBlock, false: BasicBlock) -> None: ...
def maybe_process_conditional_comparison(self, e: Expression, true: BasicBlock, false: BasicBlock) -> bool:
    """Transform simple tagged integer comparisons in a conditional context.

    Return True if the operation is supported (and was transformed). Otherwise,
    do nothing and return False.

    Args:
        e: Arbitrary expression
        true: Branch target if comparison is true
        false: Branch target if comparison is false
    """
def is_borrow_friendly_expr(self, expr: Expression) -> bool:
    """Can the result of the expression borrowed temporarily?

    Borrowing means keeping a reference without incrementing the reference count.
    """
