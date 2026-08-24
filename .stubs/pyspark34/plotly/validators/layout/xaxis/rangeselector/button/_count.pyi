import _plotly_utils.basevalidators

class CountValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'count', parent_name: str = 'layout.xaxis.rangeselector.button', **kwargs) -> None: ...
