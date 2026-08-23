import _plotly_utils.basevalidators

class DashValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'dash', parent_name: str = 'scattergl.line', **kwargs) -> None: ...
