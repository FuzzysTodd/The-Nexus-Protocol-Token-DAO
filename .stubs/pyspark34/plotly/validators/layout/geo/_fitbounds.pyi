import _plotly_utils.basevalidators

class FitboundsValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'fitbounds', parent_name: str = 'layout.geo', **kwargs) -> None: ...
