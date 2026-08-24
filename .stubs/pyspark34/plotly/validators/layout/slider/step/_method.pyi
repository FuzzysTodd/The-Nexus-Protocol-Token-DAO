import _plotly_utils.basevalidators

class MethodValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'method', parent_name: str = 'layout.slider.step', **kwargs) -> None: ...
