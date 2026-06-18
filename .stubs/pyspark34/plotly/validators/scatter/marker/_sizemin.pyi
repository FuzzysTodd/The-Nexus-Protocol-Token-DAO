import _plotly_utils.basevalidators

class SizeminValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'sizemin', parent_name: str = 'scatter.marker', **kwargs) -> None: ...
