import _plotly_utils.basevalidators

class SourcetypeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'sourcetype', parent_name: str = 'layout.mapbox.layer', **kwargs) -> None: ...
