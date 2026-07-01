from _typeshed import Incomplete

class SpeedupError(Exception):
    msg: Incomplete
    def __init__(self, msg) -> None: ...

class EmptyLayerError(SpeedupError):
    def __init__(self) -> None: ...

class ShapeMisMatchError(SpeedupError):
    def __init__(self) -> None: ...

class InputsNumberError(SpeedupError):
    def __init__(self) -> None: ...

class OutputTypeError(SpeedupError):
    def __init__(self, current_type, target_type) -> None: ...

class UnBalancedGroupError(SpeedupError):
    def __init__(self) -> None: ...
