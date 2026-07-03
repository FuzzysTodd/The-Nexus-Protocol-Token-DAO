import _plotly_utils.basevalidators

class ArgsValidator(_plotly_utils.basevalidators.InfoArrayValidator):
    def __init__(self, plotly_name: str = 'args', parent_name: str = 'layout.slider.step', **kwargs) -> None: ...
