from _typeshed import Incomplete
from jax._src import core as core, source_info_util as source_info_util, util as util
from jax._src.lib import xla_client as xla_client
from typing import Any, Callable

map: Incomplete
unsafe_map: Incomplete
zip: Incomplete
unsafe_zip: Incomplete

def all_eqns(jaxpr: core.Jaxpr): ...
def collect_eqns(jaxpr: core.Jaxpr, key: Callable): ...
def histogram(jaxpr: core.Jaxpr, key: Callable, key_fmt: Callable = ...): ...
def primitives(jaxpr: core.Jaxpr): ...
def primitives_by_source(jaxpr: core.Jaxpr): ...
def primitives_by_shape(jaxpr: core.Jaxpr): ...
def source_locations(jaxpr: core.Jaxpr): ...

MaybeEqn: Incomplete

def var_defs_and_refs(jaxpr: core.Jaxpr): ...
def vars_by_fanout(jaxpr: core.Jaxpr): ...
def print_histogram(histogram: dict[Any, int]): ...
def pprof_equation_profile(jaxpr: core.Jaxpr) -> bytes:
    """Generates a pprof profile that maps jaxpr equations to Python stack traces.

  By visualizing the profile using pprof, one can identify Python code that is
  responsible for yielding large numbers of jaxpr equations.

  Args:
    jaxpr: a Jaxpr.

  Returns:
    A gzip-compressed pprof Profile protocol buffer, suitable for passing to
    pprof tool for visualization.
  """
