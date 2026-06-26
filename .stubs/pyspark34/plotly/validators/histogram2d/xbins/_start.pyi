import _plotly_utils.basevalidators

class StartValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name: str = 'start', parent_name: str = 'histogram2d.xbins', **kwargs) -> None: ...
