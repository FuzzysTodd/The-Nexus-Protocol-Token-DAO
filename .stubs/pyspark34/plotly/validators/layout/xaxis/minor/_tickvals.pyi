import _plotly_utils.basevalidators

class TickvalsValidator(_plotly_utils.basevalidators.DataArrayValidator):
    def __init__(self, plotly_name: str = 'tickvals', parent_name: str = 'layout.xaxis.minor', **kwargs) -> None: ...
