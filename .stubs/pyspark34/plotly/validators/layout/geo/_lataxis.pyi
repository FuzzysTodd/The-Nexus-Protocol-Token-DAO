import _plotly_utils.basevalidators

class LataxisValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name: str = 'lataxis', parent_name: str = 'layout.geo', **kwargs) -> None: ...
