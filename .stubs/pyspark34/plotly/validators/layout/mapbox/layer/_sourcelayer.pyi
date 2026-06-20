import _plotly_utils.basevalidators

class SourcelayerValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name: str = 'sourcelayer', parent_name: str = 'layout.mapbox.layer', **kwargs) -> None: ...
