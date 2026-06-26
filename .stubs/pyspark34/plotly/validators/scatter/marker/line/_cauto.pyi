import _plotly_utils.basevalidators

class CautoValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name: str = 'cauto', parent_name: str = 'scatter.marker.line', **kwargs) -> None: ...
