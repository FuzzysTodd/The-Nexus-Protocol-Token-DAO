import _plotly_utils.basevalidators

class SizeValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name: str = 'size', parent_name: str = 'histogram.xbins', **kwargs) -> None: ...
