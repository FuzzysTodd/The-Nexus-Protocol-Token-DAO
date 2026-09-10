import _plotly_utils.basevalidators

class TraceorderValidator(_plotly_utils.basevalidators.FlaglistValidator):
    def __init__(self, plotly_name: str = 'traceorder', parent_name: str = 'layout.legend', **kwargs) -> None: ...
