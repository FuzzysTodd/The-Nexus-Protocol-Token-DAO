from _typeshed import Incomplete

class InputSpec:
    shape: Incomplete
    dtype: Incomplete
    range: Incomplete
    def __init__(self, shape, dtype: str = 'float32', range: Incomplete | None = None) -> None: ...

def spec_to_value(spec): ...
