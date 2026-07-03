from _plotly_utils.basevalidators import EnumeratedValidator, NumberValidator

class EasingValidator(EnumeratedValidator):
    def __init__(self, plotly_name: str = 'easing', parent_name: str = 'batch_animate', **_) -> None: ...

class DurationValidator(NumberValidator):
    def __init__(self, plotly_name: str = 'duration') -> None: ...
