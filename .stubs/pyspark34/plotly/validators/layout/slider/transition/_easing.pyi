import _plotly_utils.basevalidators

class EasingValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'easing', parent_name: str = 'layout.slider.transition', **kwargs) -> None: ...
