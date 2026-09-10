from torchgen.api.lazy import LazyIrSchema as LazyIrSchema
from torchgen.api.types import OptionalCType as OptionalCType

def ts_lowering_body(schema: LazyIrSchema) -> str: ...
