import _plotly_utils.basevalidators

class NticksValidator(_plotly_utils.basevalidators.IntegerValidator):
    def __init__(self, plotly_name: str = 'nticks', parent_name: str = 'scattergl.marker.colorbar', **kwargs) -> None: ...
