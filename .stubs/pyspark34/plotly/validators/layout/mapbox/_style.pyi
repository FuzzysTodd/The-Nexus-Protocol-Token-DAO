import _plotly_utils.basevalidators

class StyleValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name: str = 'style', parent_name: str = 'layout.mapbox', **kwargs) -> None: ...
