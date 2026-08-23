import _plotly_utils.basevalidators

class EnabledValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name: str = 'enabled', parent_name: str = 'scatterpolar.marker.colorbar.tickformatstop', **kwargs) -> None: ...
