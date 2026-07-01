import _plotly_utils.basevalidators

class ShowcountriesValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name: str = 'showcountries', parent_name: str = 'layout.geo', **kwargs) -> None: ...
