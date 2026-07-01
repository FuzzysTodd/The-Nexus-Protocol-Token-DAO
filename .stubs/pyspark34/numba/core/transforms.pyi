from _typeshed import Incomplete
from numba.core import errors as errors, ir as ir, ir_utils as ir_utils
from numba.core.analysis import compute_cfg_from_blocks as compute_cfg_from_blocks, compute_use_defs as compute_use_defs, find_top_level_loops as find_top_level_loops
from numba.core.utils import PYVERSION as PYVERSION
from typing import NamedTuple

def find_region_inout_vars(blocks, livemap, callfrom, returnto, body_block_ids):
    """Find input and output variables to a block region.
    """

class _loop_lift_info(NamedTuple):
    loop: Incomplete
    inputs: Incomplete
    outputs: Incomplete
    callfrom: Incomplete
    returnto: Incomplete

def loop_lifting(func_ir, typingctx, targetctx, flags, locals):
    """
    Loop lifting transformation.

    Given a interpreter `func_ir` returns a 2 tuple of
    `(toplevel_interp, [loop0_interp, loop1_interp, ....])`
    """
def canonicalize_cfg_single_backedge(blocks):
    """
    Rewrite loops that have multiple backedges.
    """
def canonicalize_cfg(blocks):
    """
    Rewrite the given blocks to canonicalize the CFG.
    Returns a new dictionary of blocks.
    """
def with_lifting(func_ir, typingctx, targetctx, flags, locals):
    """With-lifting transformation

    Rewrite the IR to extract all withs.
    Only the top-level withs are extracted.
    Returns the (the_new_ir, the_lifted_with_ir)
    """
def find_setupwiths(func_ir):
    """Find all top-level with.

    Returns a list of ranges for the with-regions.
    """
def consolidate_multi_exit_withs(withs: dict, blocks, func_ir):
    """Modify the FunctionIR to merge the exit blocks of with constructs.
    """
