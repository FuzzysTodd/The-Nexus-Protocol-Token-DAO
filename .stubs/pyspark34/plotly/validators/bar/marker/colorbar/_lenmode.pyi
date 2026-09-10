import _plotly_utils.basevalidators

class LenmodeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'lenmode', parent_name: str = 'bar.marker.colorbar', **kwargs) -> None: ...
