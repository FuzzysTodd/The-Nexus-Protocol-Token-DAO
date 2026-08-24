import _plotly_utils.basevalidators

class StepmodeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'stepmode', parent_name: str = 'layout.xaxis.rangeselector.button', **kwargs) -> None: ...
