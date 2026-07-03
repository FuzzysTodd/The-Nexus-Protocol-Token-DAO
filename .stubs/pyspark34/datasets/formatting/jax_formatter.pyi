import jax
import pyarrow as pa
from .. import config as config
from ..utils.logging import get_logger as get_logger
from ..utils.py_utils import map_nested as map_nested
from .formatting import TensorFormatter as TensorFormatter
from _typeshed import Incomplete
from collections.abc import Mapping

logger: Incomplete
DEVICE_MAPPING: dict | None

class JaxFormatter(TensorFormatter[Mapping, 'jax.Array', Mapping]):
    device: Incomplete
    jnp_array_kwargs: Incomplete
    def __init__(self, features: Incomplete | None = None, device: Incomplete | None = None, **jnp_array_kwargs) -> None: ...
    def recursive_tensorize(self, data_struct: dict): ...
    def format_row(self, pa_table: pa.Table) -> Mapping: ...
    def format_column(self, pa_table: pa.Table) -> jax.Array: ...
    def format_batch(self, pa_table: pa.Table) -> Mapping: ...
