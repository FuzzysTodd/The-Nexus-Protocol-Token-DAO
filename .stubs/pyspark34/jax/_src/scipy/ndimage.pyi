from collections.abc import Sequence
from jax import lax as lax
from jax._src import api as api, util as util
from jax._src.typing import Array as Array, ArrayLike as ArrayLike

def map_coordinates(input: ArrayLike, coordinates: Sequence[ArrayLike], order: int, mode: str = 'constant', cval: ArrayLike = 0.0): ...
