import _plotly_utils.basevalidators

class ShowcoastlinesValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name: str = 'showcoastlines', parent_name: str = 'layout.geo', **kwargs) -> None: ...
