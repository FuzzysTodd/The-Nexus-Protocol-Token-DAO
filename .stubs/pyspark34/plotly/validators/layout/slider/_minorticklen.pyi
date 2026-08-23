import _plotly_utils.basevalidators

class MinorticklenValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'minorticklen', parent_name: str = 'layout.slider', **kwargs) -> None: ...
