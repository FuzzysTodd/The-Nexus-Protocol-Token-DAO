import _plotly_utils.basevalidators

class ShowlakesValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name: str = 'showlakes', parent_name: str = 'layout.geo', **kwargs) -> None: ...
