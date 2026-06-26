import _plotly_utils.basevalidators

class SourceValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name: str = 'source', parent_name: str = 'layout.mapbox.layer', **kwargs) -> None: ...
