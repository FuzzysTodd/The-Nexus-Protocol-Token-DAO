from _typeshed import Incomplete
from jax._src import core as core
from jax._src.state import AbstractRef as AbstractRef
from jax._src.state.primitives import ref_get as ref_get
from jax._src.util import merge_lists as merge_lists, partition_list as partition_list, safe_map as safe_map, safe_zip as safe_zip, split_list as split_list

map: Incomplete
unsafe_map: Incomplete
zip: Incomplete
unsafe_zip: Incomplete

def hoist_consts_to_refs(jaxpr: core.Jaxpr) -> core.Jaxpr: ...
def val_to_ref_aval(x) -> AbstractRef: ...
