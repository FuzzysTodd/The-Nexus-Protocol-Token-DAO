from _typeshed import Incomplete

SMOOTHER_STATE: int
SMOOTHER_STATE_COV: int
SMOOTHER_DISTURBANCE: int
SMOOTHER_DISTURBANCE_COV: int
SMOOTHER_ALL: Incomplete

class _KalmanSmoother:
    model: Incomplete
    kfilter: Incomplete
    smoother_output: Incomplete
    scaled_smoothed_estimator: Incomplete
    scaled_smoothed_estimator_cov: Incomplete
    smoothing_error: Incomplete
    smoothed_state: Incomplete
    smoothed_state_cov: Incomplete
    smoothed_state_disturbance: Incomplete
    smoothed_state_disturbance_cov: Incomplete
    smoothed_measurement_disturbance: Incomplete
    smoothed_measurement_disturbance_cov: Incomplete
    tmp_L: Incomplete
    def __init__(self, model, kfilter, smoother_output) -> None: ...
    t: Incomplete
    def seek(self, t) -> None: ...
    def __iter__(self): ...
    def __call__(self) -> None: ...
    def next(self): ...
    def __next__(self) -> None: ...
