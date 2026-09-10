import _plotly_utils.basevalidators

class LValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'l', parent_name: str = 'layout.slider.pad', **kwargs) -> None: ...
