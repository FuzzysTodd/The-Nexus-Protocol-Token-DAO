import _plotly_utils.basevalidators

class TracerefValidator(_plotly_utils.basevalidators.IntegerValidator):
    def __init__(self, plotly_name: str = 'traceref', parent_name: str = 'scatter3d.error_y', **kwargs) -> None: ...
