import numpy as np
from _typeshed import Incomplete
from jax import lax as lax, tree_util as tree_util
from jax._src import test_util as jtu
from jax._src.typing import DTypeLike as DTypeLike
from jax.experimental import sparse as sparse
from jax.util import safe_zip as safe_zip, split_list as split_list
from typing import Any, Callable

def is_sparse(x): ...

class SparseTestCase(jtu.JaxTestCase):
    def assertSparseArraysEquivalent(self, x, y, *, check_dtypes: bool = True, atol: Incomplete | None = None, rtol: Incomplete | None = None, canonicalize_dtypes: bool = True, err_msg: str = '') -> None: ...

def rand_bcoo(rng: np.random.RandomState, rand_method: Callable[..., Any] = ..., nse: int | float = 0.5, n_batch: int = 0, n_dense: int = 0):
    """Generates a random BCOO array."""
def rand_bcsr(rng: np.random.RandomState, rand_method: Callable[..., Any] = ..., nse: int | float = 0.5, n_batch: int = 0, n_dense: int = 0):
    """Generates a random BCSR array."""
