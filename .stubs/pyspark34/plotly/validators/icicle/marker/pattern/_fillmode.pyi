import _plotly_utils.basevalidators

class FillmodeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'fillmode', parent_name: str = 'icicle.marker.pattern', **kwargs) -> None: ...
