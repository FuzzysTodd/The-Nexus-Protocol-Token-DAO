import _plotly_utils.basevalidators

class DurationValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'duration', parent_name: str = 'layout.slider.transition', **kwargs) -> None: ...
