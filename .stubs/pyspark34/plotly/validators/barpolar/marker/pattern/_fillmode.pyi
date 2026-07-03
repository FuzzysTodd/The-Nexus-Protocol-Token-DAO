import _plotly_utils.basevalidators

class FillmodeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'fillmode', parent_name: str = 'barpolar.marker.pattern', **kwargs) -> None: ...
