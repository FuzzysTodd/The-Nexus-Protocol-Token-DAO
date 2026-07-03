from _typeshed import Incomplete

sign_defaults: Incomplete

class BenchmarkResult:
    """ The result of a benchmark run.
    """
    metric: Incomplete
    method: Incomplete
    value: Incomplete
    curve_x: Incomplete
    curve_y: Incomplete
    curve_y_std: Incomplete
    value_sign: Incomplete
    def __init__(self, metric, method, value: Incomplete | None = None, curve_x: Incomplete | None = None, curve_y: Incomplete | None = None, curve_y_std: Incomplete | None = None, value_sign: Incomplete | None = None) -> None: ...
    @property
    def full_name(self): ...
