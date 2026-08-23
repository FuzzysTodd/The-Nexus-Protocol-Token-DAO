import _plotly_utils.basevalidators

class EnabledValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name: str = 'enabled', parent_name: str = 'histogram2dcontour.colorbar.tickformatstop', **kwargs) -> None: ...
