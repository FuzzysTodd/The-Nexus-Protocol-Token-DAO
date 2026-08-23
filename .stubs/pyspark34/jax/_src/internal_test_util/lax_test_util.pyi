from _typeshed import Incomplete
from jax import config as config, lax as lax
from jax._src import dtypes as dtypes, test_util as test_util
from jax._src.util import safe_map as safe_map, safe_zip as safe_zip
from typing import NamedTuple

map: Incomplete
unsafe_map: Incomplete
zip: Incomplete
unsafe_zip: Incomplete
float_dtypes: Incomplete
complex_elem_dtypes: Incomplete
complex_dtypes: Incomplete
inexact_dtypes: Incomplete
int_dtypes: Incomplete
uint_dtypes: Incomplete
bool_dtypes: Incomplete
default_dtypes: Incomplete
all_dtypes: Incomplete
python_scalar_types: Incomplete
compatible_shapes: Incomplete

class OpRecord(NamedTuple):
    op: Incomplete
    nargs: Incomplete
    dtypes: Incomplete
    rng_factory: Incomplete
    tol: Incomplete

def op_record(op, nargs, dtypes, rng_factory, tol: Incomplete | None = None): ...

class ReducerOpRecord(NamedTuple):
    op: Incomplete
    reference_op: Incomplete
    init_val: Incomplete
    dtypes: Incomplete
    primitive: Incomplete

def lax_reduce_ops(): ...
def lax_ops(): ...
def all_bdims(*shapes): ...
def add_bdim(bdim_size, bdim, shape): ...
def slicer(x, bdim): ...
def args_slicer(args, bdims): ...
