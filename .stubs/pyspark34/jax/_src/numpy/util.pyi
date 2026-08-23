from _typeshed import Incomplete
from jax._src import api as api, core as core, dtypes as dtypes
from jax._src.config import config as config
from jax._src.lax import lax as lax
from jax._src.typing import Array as Array, ArrayLike as ArrayLike, DType as DType, DTypeLike as DTypeLike, Shape as Shape
from jax._src.util import safe_map as safe_map, safe_zip as safe_zip
from typing import Any, NamedTuple

zip: Incomplete
unsafe_zip: Incomplete
map: Incomplete
unsafe_map: Incomplete

class ParsedDoc(NamedTuple):
    """
  docstr: full docstring
  signature: signature from docstring.
  summary: summary from docstring.
  front_matter: front matter before sections.
  sections: dictionary of section titles to section content.
  """
    docstr: str | None
    signature: str = ...
    summary: str = ...
    front_matter: str = ...
    sections: dict[str, str] = ...

def promote_shapes(fun_name: str, *args: ArrayLike) -> list[Array]:
    """Apply NumPy-style broadcasting, making args shape-compatible for lax.py."""
def promote_dtypes(*args: ArrayLike) -> list[Array]:
    """Convenience function to apply Numpy argument dtype promotion."""
def promote_dtypes_inexact(*args: ArrayLike) -> list[Array]:
    """Convenience function to apply Numpy argument dtype promotion.

  Promotes arguments to an inexact type."""
def promote_dtypes_numeric(*args: ArrayLike) -> list[Array]:
    """Convenience function to apply Numpy argument dtype promotion.

  Promotes arguments to a numeric (non-bool) type."""
def promote_dtypes_complex(*args: ArrayLike) -> list[Array]:
    """Convenience function to apply Numpy argument dtype promotion.

  Promotes arguments to a complex type."""
def check_arraylike(fun_name: str, *args: Any, emit_warning: bool = False, stacklevel: int = 3):
    """Check if all args fit JAX's definition of arraylike."""
def check_arraylike_or_none(fun_name: str, *args: Any): ...
def check_no_float0s(fun_name: str, *args: Any):
    """Check if none of the args have dtype float0."""
def promote_args(fun_name: str, *args: ArrayLike) -> list[Array]:
    """Convenience function to apply Numpy argument shape and dtype promotion."""
def promote_args_numeric(fun_name: str, *args: ArrayLike) -> list[Array]: ...
def promote_args_inexact(fun_name: str, *args: ArrayLike) -> list[Array]:
    """Convenience function to apply Numpy argument shape and dtype promotion.

  Promotes non-inexact types to an inexact type."""
