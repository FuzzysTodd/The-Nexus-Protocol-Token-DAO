from _typeshed import Incomplete
from collections.abc import Sequence
from jax import config as config
from jax._src import ad_util as ad_util, core as core, dispatch as dispatch, dtypes as dtypes, effects as effects, source_info_util as source_info_util, util as util
from jax._src.core import ConcreteArray as ConcreteArray, raise_to_shaped as raise_to_shaped, replace_jaxpr_effects as replace_jaxpr_effects
from jax._src.interpreters import ad as ad, batching as batching, mlir as mlir, xla as xla
from jax._src.lax import lax as lax
from jax._src.lib.mlir import ir as ir
from jax._src.lib.mlir.dialects import hlo as hlo
from jax._src.state.discharge import discharge_state as discharge_state, register_discharge_rule as register_discharge_rule
from jax._src.state.types import AbstractRef as AbstractRef, RefEffect as RefEffect
from jax._src.traceback_util import api_boundary as api_boundary
from jax._src.util import partition_list as partition_list, safe_map as safe_map, split_list as split_list
from jax.tree_util import tree_flatten as tree_flatten, tree_unflatten as tree_unflatten
from typing import Callable

map: Incomplete
unsafe_map: Incomplete

def switch(index, branches: Sequence[Callable], *operands, operand=...):
    """Apply exactly one of ``branches`` given by ``index``.

  If ``index`` is out of bounds, it is clamped to within bounds.

  Has the semantics of the following Python::

    def switch(index, branches, *operands):
      index = clamp(0, index, len(branches) - 1)
      return branches[index](*operands)

  Internally this wraps XLA's `Conditional
  <https://www.tensorflow.org/xla/operation_semantics#conditional>`_
  operator. However, when transformed with :func:`~jax.vmap` to operate over a
  batch of predicates, ``cond`` is converted to :func:`~jax.lax.select`.

  Args:
    index: Integer scalar type, indicating which branch function to apply.
    branches: Sequence of functions (A -> B) to be applied based on ``index``.
    operands: Operands (A) input to whichever branch is applied.

  Returns:
    Value (B) of ``branch(*operands)`` for the branch that was selected based
    on ``index``.
  """
def cond(*args, **kwargs): ...
def cond_bind(*args, branches, linear): ...

cond_p: Incomplete
