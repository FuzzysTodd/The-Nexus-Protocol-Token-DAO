import _plotly_utils.basevalidators

class ShowriversValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name: str = 'showrivers', parent_name: str = 'layout.geo', **kwargs) -> None: ...
